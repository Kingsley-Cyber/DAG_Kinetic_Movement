from __future__ import annotations

from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class EvidenceClass(str, Enum):
    MEASURED = "measured"
    DETECTED = "detected"
    INFERRED = "inferred"
    INTERPRETED = "interpreted"
    AUTHORED = "authored"


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    UNKNOWN = "unknown"


class CapabilityClass(str, Enum):
    NATIVE = "native"
    MEDIA_CONDITIONED = "media-conditioned"
    SEMANTIC_TEXT_ONLY = "semantic-text-only"
    APPROXIMATED = "approximated"
    UNSUPPORTED = "unsupported"
    UNKNOWN = "unknown"


class ContactType(str, Enum):
    SUPPORT = "support"
    TOUCH = "touch"
    IMPACT = "impact"
    NEAR_MISS = "near_miss"
    GUARD = "guard_contact"
    GRASP = "grasp"
    HOLD = "sustained_hold"
    RELEASE = "release"
    SLIDE = "slide"
    PUSH = "push"
    PULL = "pull"
    BRACE = "brace"


class EvidenceRef(StrictModel):
    evidence_id: str
    source_uri: str | None = None
    locator: str | None = None
    evidence_class: EvidenceClass
    confidence: float = Field(ge=0.0, le=1.0)
    extractor: str | None = None
    accessed_at: str | None = None


class Actor(StrictModel):
    actor_id: str
    display_name: str | None = None
    morphology_profile_id: str | None = None
    reference_asset_ids: list[str] = Field(default_factory=list)
    initial_screen_side: Literal["left", "center", "right", "unknown"] = "unknown"
    initial_support_effectors: list[str] = Field(default_factory=list)
    initial_held_objects: dict[str, str] = Field(
        default_factory=dict,
        description="Map hand/effector to object_id.",
    )


class SceneObject(StrictModel):
    object_id: str
    display_name: str | None = None
    initial_owner_actor_id: str | None = None


class ActionPhase(StrictModel):
    phase_id: str
    action_id: str
    kind: Literal[
        "preparation",
        "anticipation",
        "execution",
        "contact",
        "follow_through",
        "flight",
        "landing",
        "reaction",
        "recovery",
        "hold",
        "release",
        "other",
    ]
    start_point: str
    end_point: str


class StateCondition(StrictModel):
    kind: Literal[
        "support_present",
        "support_absent",
        "object_held",
        "object_not_held",
        "screen_side",
        "grounded",
        "airborne",
        "region_free",
    ]
    actor_id: str
    key: str | None = None
    value: str | bool | None = None


class StateEffect(StrictModel):
    kind: Literal[
        "add_support",
        "remove_support",
        "acquire_object",
        "release_object",
        "set_screen_side",
        "set_grounded",
        "set_airborne",
    ]
    actor_id: str
    key: str | None = None
    value: str | bool | None = None


class Action(StrictModel):
    action_id: str
    actor_id: str
    verb: str
    target_ref: str | None = None
    start_point: str
    end_point: str
    body_regions: list[str] = Field(default_factory=list)
    resource_locks: list[str] = Field(
        default_factory=list,
        description="Actor-local mutually exclusive resources, e.g. right_hand or left_leg.",
    )
    preconditions: list[StateCondition] = Field(default_factory=list)
    effects: list[StateEffect] = Field(default_factory=list)
    reacts_to_contact_id: str | None = None
    recovers_from_action_id: str | None = None
    evidence: list[EvidenceRef] = Field(default_factory=list)


class Contact(StrictModel):
    contact_id: str
    contact_type: ContactType
    actor_a: str
    site_a: str
    target_ref: str
    site_b: str
    start_point: str
    end_point: str
    contact_normal: tuple[float, float, float] | None = None
    relative_velocity_mps: float | None = None
    minimum_distance_m: float | None = Field(default=None, ge=0.0)
    visibility: Literal["visible", "occluded", "partial", "unknown"] = "unknown"
    support_status: Literal["supporting", "non_supporting", "unknown"] = "unknown"
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    reaction_action_id: str | None = None
    camera_presentation: str | None = None
    cinematic_cheat_allowed: bool = False
    evidence: list[EvidenceRef] = Field(default_factory=list)


class TemporalConstraint(StrictModel):
    constraint_id: str
    left_point: str
    right_point: str
    min_delta_s: float
    max_delta_s: float
    hard: bool = True
    explanation: str | None = None
    evidence: list[EvidenceRef] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_bounds(self) -> "TemporalConstraint":
        if self.min_delta_s > self.max_delta_s:
            raise ValueError("min_delta_s must be <= max_delta_s")
        return self


class CameraEvent(StrictModel):
    camera_event_id: str
    kind: Literal[
        "static",
        "pan",
        "tilt",
        "dolly",
        "truck",
        "crane",
        "orbit",
        "zoom",
        "shake",
        "reframe",
        "other",
    ]
    start_point: str
    end_point: str
    subject_ref: str | None = None
    parameters: dict[str, Any] = Field(default_factory=dict)


class AssetRef(StrictModel):
    asset_id: str
    role: Literal[
        "first_frame",
        "last_frame",
        "reference_image",
        "reference_video",
        "audio",
        "pose",
        "depth",
        "mask",
        "flow",
        "other",
    ]
    uri: str
    sha256: str | None = None


class ControlRequest(StrictModel):
    control_id: str
    canonical_path: str
    value: Any
    required: bool = False
    preferred_carrier: str | None = None
    rationale: str | None = None


class AcceptanceGate(StrictModel):
    metric: str
    operator: Literal["<", "<=", "==", ">=", ">"]
    value: float | int | bool | str
    hard: bool = True


class ScenePlan(StrictModel):
    schema_id: Literal["dmr.scene-plan/0.1"] = "dmr.scene-plan/0.1"
    scene_id: str
    title: str | None = None
    duration_s: float = Field(gt=0.0)
    fps: float = Field(gt=0.0)
    origin_point: str = "scene:start"
    end_point: str = "scene:end"
    actors: list[Actor]
    objects: list[SceneObject] = Field(default_factory=list)
    assets: list[AssetRef] = Field(default_factory=list)
    actions: list[Action]
    phases: list[ActionPhase] = Field(default_factory=list)
    contacts: list[Contact] = Field(default_factory=list)
    temporal_constraints: list[TemporalConstraint]
    camera_events: list[CameraEvent] = Field(default_factory=list)
    control_requests: list[ControlRequest] = Field(default_factory=list)
    acceptance_gates: list[AcceptanceGate] = Field(default_factory=list)
    provenance: list[EvidenceRef] = Field(default_factory=list)

    @model_validator(mode="after")
    def unique_ids_and_references(self) -> "ScenePlan":
        groups = {
            "actor": [x.actor_id for x in self.actors],
            "object": [x.object_id for x in self.objects],
            "action": [x.action_id for x in self.actions],
            "phase": [x.phase_id for x in self.phases],
            "contact": [x.contact_id for x in self.contacts],
            "temporal_constraint": [x.constraint_id for x in self.temporal_constraints],
            "camera_event": [x.camera_event_id for x in self.camera_events],
            "control": [x.control_id for x in self.control_requests],
        }
        for label, ids in groups.items():
            if len(ids) != len(set(ids)):
                raise ValueError(f"duplicate {label} IDs")
        actor_ids = set(groups["actor"])
        action_ids = set(groups["action"])
        contact_ids = set(groups["contact"])
        for action in self.actions:
            if action.actor_id not in actor_ids:
                raise ValueError(f"action {action.action_id} references unknown actor {action.actor_id}")
            if action.recovers_from_action_id and action.recovers_from_action_id not in action_ids:
                raise ValueError(f"action {action.action_id} references unknown recovery source")
            if action.reacts_to_contact_id and action.reacts_to_contact_id not in contact_ids:
                raise ValueError(f"action {action.action_id} references unknown contact")
        for contact in self.contacts:
            if contact.actor_a not in actor_ids:
                raise ValueError(f"contact {contact.contact_id} references unknown actor_a")
            if contact.reaction_action_id and contact.reaction_action_id not in action_ids:
                raise ValueError(f"contact {contact.contact_id} references unknown reaction action")
        return self


class CapabilityMapping(StrictModel):
    canonical_path: str
    classification: CapabilityClass
    carrier: str | None = None
    provider_parameter: str | None = None
    transform: str | None = None
    limits: dict[str, Any] = Field(default_factory=dict)
    evidence_source: str | None = None
    notes: str | None = None


class ProviderCapabilityContract(StrictModel):
    schema_id: Literal["dmr.provider-capability-contract/0.1"] = "dmr.provider-capability-contract/0.1"
    contract_id: str
    provider: str
    api_surface: str
    model_id: str
    contract_kind: Literal["api", "product_profile", "local_workflow"] = "api"
    verified_on: str
    documentation_urls: list[str]
    lifecycle: dict[str, Any] = Field(default_factory=dict)
    mappings: list[CapabilityMapping]
    unknowns: list[str] = Field(default_factory=list)

    def mapping_for(self, canonical_path: str) -> CapabilityMapping | None:
        exact = next((m for m in self.mappings if m.canonical_path == canonical_path), None)
        if exact:
            return exact
        candidates = [m for m in self.mappings if m.canonical_path.endswith(".*")]
        candidates.sort(key=lambda m: len(m.canonical_path), reverse=True)
        for mapping in candidates:
            prefix = mapping.canonical_path[:-1]
            if canonical_path.startswith(prefix):
                return mapping
        return None


class ValidationIssue(StrictModel):
    issue_id: str
    severity: Severity
    code: str
    message: str
    responsible_paths: list[str] = Field(default_factory=list)
    earliest_causal_layer: str | None = None
    suggested_patch: dict[str, Any] | None = None


class CompilationLossItem(StrictModel):
    control_id: str
    canonical_path: str
    requested_value: Any
    required: bool
    classification: CapabilityClass
    carrier: str | None = None
    provider_parameter: str | None = None
    compiled_value: Any = None
    residual_risk: str | None = None
    evidence_source: str | None = None


class CompilationResult(StrictModel):
    scene_id: str
    contract_id: str
    solved_timeline_s: dict[str, float]
    provider_request: dict[str, Any]
    prompt: str
    loss_report: list[CompilationLossItem]
    validation_issues: list[ValidationIssue]
    hard_failure: bool
