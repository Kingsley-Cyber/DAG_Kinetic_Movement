from __future__ import annotations

from dataclasses import dataclass
import json
import re
from typing import Any

from .models import (
    CapabilityClass,
    CapabilityMapping,
    CompilationLossItem,
    CompilationResult,
    ProviderCapabilityContract,
    ScenePlan,
    Severity,
)
from .temporal import STNSolver
from .validation import validate_scene


class CompilationError(RuntimeError):
    pass


@dataclass(frozen=True)
class CompileOptions:
    allow_required_loss: bool = False


def compile_scene(
    scene: ScenePlan,
    contract: ProviderCapabilityContract,
    *,
    options: CompileOptions | None = None,
) -> CompilationResult:
    """Compile a solved scene through one pinned capability contract.

    The function is intentionally fail-closed. It does not invoke a provider. The
    returned ``provider_request`` is a deterministic request-body candidate for
    exact API/local-workflow contracts; a ``product_profile`` is non-executable.
    """
    options = options or CompileOptions()
    if contract.contract_kind == "product_profile":
        raise CompilationError(
            f"Contract {contract.contract_id} is a product profile, not an executable API/local-workflow contract"
        )

    temporal = STNSolver(scene.temporal_constraints, origin=scene.origin_point).solve()
    validation = validate_scene(scene, temporal)
    hard_validation_failure = any(i.severity == Severity.ERROR for i in validation)
    if not temporal.consistent:
        raise CompilationError(temporal.conflict.message if temporal.conflict else "Temporal solve failed")

    prompt_parts = [_compile_action_text(scene, temporal.schedule_s)]
    provider_request: dict[str, Any] = {"model": contract.model_id}
    loss: list[CompilationLossItem] = []
    required_loss = False

    for control in scene.control_requests:
        mapping = contract.mapping_for(control.canonical_path)
        if mapping is None:
            item = CompilationLossItem(
                control_id=control.control_id,
                canonical_path=control.canonical_path,
                requested_value=control.value,
                required=control.required,
                classification=CapabilityClass.UNKNOWN,
                residual_risk="No capability mapping exists in the pinned contract.",
            )
            loss.append(item)
            required_loss |= control.required
            continue

        limit_problem = _limit_violation(control.value, mapping)
        if limit_problem:
            loss.append(CompilationLossItem(
                control_id=control.control_id,
                canonical_path=control.canonical_path,
                requested_value=control.value,
                required=control.required,
                classification=CapabilityClass.UNSUPPORTED,
                carrier=mapping.carrier,
                provider_parameter=mapping.provider_parameter,
                residual_risk=f"Requested value violates the pinned contract: {limit_problem}",
                evidence_source=mapping.evidence_source,
            ))
            required_loss |= control.required
            continue

        compiled_value: Any = None
        residual: str | None = None
        classification = mapping.classification
        if classification == CapabilityClass.NATIVE:
            compiled_value = _apply_transform(control.value, mapping.transform)
            if mapping.provider_parameter:
                _set_path(provider_request, mapping.provider_parameter, compiled_value)
            elif mapping.carrier == "fixed_model_setting":
                residual = "Satisfied by the pinned model's fixed setting; no request-body field is emitted."
            else:
                residual = "Native capability is documented, but this contract has no executable request-field mapping."
                classification = CapabilityClass.UNKNOWN
                required_loss |= control.required
        elif classification == CapabilityClass.MEDIA_CONDITIONED:
            compiled_value = _apply_transform(control.value, mapping.transform)
            residual = (
                "Adherence depends on the conditioning asset and model response; "
                "it is not a hard trajectory constraint."
            )
            if mapping.provider_parameter:
                _set_path(provider_request, mapping.provider_parameter, compiled_value)
            else:
                residual += " No executable request-field mapping is present."
                classification = CapabilityClass.UNKNOWN
                required_loss |= control.required
        elif classification == CapabilityClass.SEMANTIC_TEXT_ONLY:
            phrase = _semantic_phrase(control.canonical_path, control.value)
            prompt_parts.append(phrase)
            compiled_value = phrase
            residual = "Converted to semantic text; numeric or causal semantics are not guaranteed."
        elif classification == CapabilityClass.APPROXIMATED:
            compiled_value = _apply_transform(control.value, mapping.transform)
            if mapping.provider_parameter:
                _set_path(provider_request, mapping.provider_parameter, compiled_value)
            else:
                phrase = _semantic_phrase(control.canonical_path, compiled_value)
                prompt_parts.append(phrase)
                compiled_value = phrase
            residual = "Approximated using an alternate carrier; information loss is expected."
        elif classification == CapabilityClass.UNSUPPORTED:
            residual = "The pinned provider/model surface has no documented carrier for this control."
            required_loss |= control.required
        else:
            residual = "Capability cannot be verified from the pinned official documentation."
            required_loss |= control.required

        loss.append(CompilationLossItem(
            control_id=control.control_id,
            canonical_path=control.canonical_path,
            requested_value=control.value,
            required=control.required,
            classification=classification,
            carrier=mapping.carrier,
            provider_parameter=mapping.provider_parameter,
            compiled_value=compiled_value,
            residual_risk=residual,
            evidence_source=mapping.evidence_source,
        ))

    prompt = "\n".join(p for p in prompt_parts if p).strip()
    prompt_mapping = contract.mapping_for("prompt.text")
    if (
        prompt_mapping
        and prompt_mapping.classification == CapabilityClass.NATIVE
        and prompt_mapping.provider_parameter
    ):
        _set_path(provider_request, prompt_mapping.provider_parameter, prompt)
    else:
        provider_request["prompt"] = prompt

    hard_failure = hard_validation_failure or required_loss
    result = CompilationResult(
        scene_id=scene.scene_id,
        contract_id=contract.contract_id,
        solved_timeline_s={k: round(v, 6) for k, v in temporal.schedule_s.items()},
        provider_request=provider_request,
        prompt=prompt,
        loss_report=loss,
        validation_issues=validation,
        hard_failure=hard_failure,
    )
    if hard_failure and not options.allow_required_loss:
        causes = []
        if hard_validation_failure:
            causes.append("scene validation contains errors")
        if required_loss:
            causes.append("one or more required controls are unsupported, unknown, or outside contract limits")
        raise CompilationError("Compilation failed closed: " + "; ".join(causes))
    return result


def _compile_action_text(scene: ScenePlan, schedule: dict[str, float]) -> str:
    def start(action: Any) -> float:
        return schedule.get(action.start_point, 0.0)

    lines = [f"Scene: {scene.title or scene.scene_id}. Duration {scene.duration_s:g}s."]
    for action in sorted(scene.actions, key=lambda a: (start(a), a.action_id)):
        s = schedule.get(action.start_point)
        e = schedule.get(action.end_point)
        window = f"{s:.2f}-{e:.2f}s" if s is not None and e is not None else "unscheduled"
        target = f" toward {action.target_ref}" if action.target_ref else ""
        lines.append(f"[{window}] {action.actor_id}: {action.verb}{target}.")
    for contact in scene.contacts:
        s = schedule.get(contact.start_point)
        when = f" at {s:.2f}s" if s is not None else ""
        lines.append(
            f"Contact{when}: {contact.actor_a}.{contact.site_a} -> "
            f"{contact.target_ref}.{contact.site_b} ({contact.contact_type.value})."
        )
    return "\n".join(lines)


def _semantic_phrase(path: str, value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return f"Control intent — {path}: {payload}."


def _apply_transform(value: Any, transform: str | None) -> Any:
    if not transform or transform == "identity":
        return value
    if transform == "seconds_to_integer":
        return int(value)
    if transform == "list_first":
        return value[0] if isinstance(value, list) and value else value
    raise CompilationError(f"Unknown deterministic transform: {transform}")


def _limit_violation(value: Any, mapping: CapabilityMapping) -> str | None:
    limits = mapping.limits
    if not limits:
        return None
    if limits.get("integer") and (isinstance(value, bool) or not isinstance(value, int)):
        return f"expected an integer, got {value!r}"
    allowed = limits.get("allowed")
    if allowed is not None and value not in allowed:
        return f"{value!r} is not in allowed values {allowed!r}"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "min" in limits and value < limits["min"]:
            return f"{value!r} is below minimum {limits['min']!r}"
        if "max" in limits and value > limits["max"]:
            return f"{value!r} exceeds maximum {limits['max']!r}"
        if "divisible_by" in limits and value % limits["divisible_by"] != 0:
            return f"{value!r} is not divisible by {limits['divisible_by']!r}"
        if limits.get("shape") == "8n+1" and (int(value) - 1) % 8 != 0:
            return f"{value!r} does not satisfy frame-count form 8n+1"
    if isinstance(value, (list, tuple, dict, str)):
        n = len(value)
        if "min_items" in limits and n < limits["min_items"]:
            return f"contains {n} item(s), below minimum {limits['min_items']}"
        if "max_items" in limits and n > limits["max_items"]:
            return f"contains {n} item(s), above maximum {limits['max_items']}"
    return None


_PATH_TOKEN = re.compile(r"([^.\[\]]+)|\[(\d+)\]")


def _set_path(target: dict[str, Any], path: str, value: Any) -> None:
    """Set dotted/list-index paths such as ``instances[0].prompt``."""
    tokens: list[str | int] = []
    for name, index in _PATH_TOKEN.findall(path):
        tokens.append(int(index) if index else name)
    if not tokens:
        raise CompilationError(f"Invalid provider parameter path: {path!r}")

    cursor: Any = target
    for pos, token in enumerate(tokens[:-1]):
        next_token = tokens[pos + 1]
        if isinstance(token, str):
            if not isinstance(cursor, dict):
                raise CompilationError(f"Provider parameter path collision at {path}")
            expected = [] if isinstance(next_token, int) else {}
            existing = cursor.get(token)
            if existing is None:
                cursor[token] = expected
            elif not isinstance(existing, type(expected)):
                raise CompilationError(f"Provider parameter path collision at {path}")
            cursor = cursor[token]
        else:
            if not isinstance(cursor, list):
                raise CompilationError(f"Provider parameter path collision at {path}")
            while len(cursor) <= token:
                cursor.append(None)
            expected = [] if isinstance(next_token, int) else {}
            if cursor[token] is None:
                cursor[token] = expected
            elif not isinstance(cursor[token], type(expected)):
                raise CompilationError(f"Provider parameter path collision at {path}")
            cursor = cursor[token]

    final = tokens[-1]
    if isinstance(final, str):
        if not isinstance(cursor, dict):
            raise CompilationError(f"Provider parameter path collision at {path}")
        cursor[final] = value
    else:
        if not isinstance(cursor, list):
            raise CompilationError(f"Provider parameter path collision at {path}")
        while len(cursor) <= final:
            cursor.append(None)
        cursor[final] = value
