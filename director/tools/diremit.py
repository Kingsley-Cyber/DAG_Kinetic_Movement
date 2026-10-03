"""Director emit: deterministic prompt assembly from treatments, per model profile, with a receipt
and loss records. Runs `check` first and refuses on any error.
"""
import datetime as _dt
import hashlib
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from dircheck import (
    FIELD_CLAUSE,
    PROFILES_DIR,
    check,
    comparison_clause,
    load_ir,
    load_treatments,
    load_yaml,
)

# ----------------------------------------------------------------------------- emit

# Text fallbacks for API-level controls when the selected route has no native field for them.
# A native control is never dropped silently: it is carried as text (compressed_to_text, with a
# loss record) or, when locked and no text form exists, emission blocks.
NATIVE_TEXT = {
    "duration_s": "{v}-second clip",
    "aspect_ratio": "{v} aspect ratio",
    "fps": "{v} fps",
}
LEVER_EVIDENCE_RANK = {"documented": 0, "measured": 1, "documented_thirdparty": 2, "owner_observed": 3, "unknown": 4}


def select_lever(profile: dict, intent: str) -> Optional[dict]:
    """Deterministic lever choice: best evidence first, then file order."""
    levers = [l for l in (profile.get("dialect", {}) or {}).get("levers", []) or [] if l.get("intent") == intent]
    if not levers:
        return None
    indexed = list(enumerate(levers))
    indexed.sort(key=lambda il: (LEVER_EVIDENCE_RANK.get(il[1].get("evidence", "unknown"), 9), il[0]))
    return indexed[0][1]


def apply_emphasis(text: str, words: List[str], lever: dict, warnings: List[str], cid: str) -> str:
    for w in words:
        pattern = r"\b%s\b" % re.escape(str(w))
        if not re.search(pattern, text):
            warnings.append("%s: emphasis word '%s' not present in the emitted wording" % (cid, w))
            continue
        text = re.sub(pattern, lever["syntax"].replace("{word}", str(w)), text, count=1)
    return text


LABAN_WORDS = {
    "weight": ("light, easy", "grounded, forceful"),
    "time": ("unhurried", "quick, sudden"),
    "space": ("meandering", "direct, focused"),
    "flow": ("loose, released", "controlled, held"),
}


def derive_laban(value: dict) -> Dict[str, str]:
    out = {}
    for k, (lo, hi) in LABAN_WORDS.items():
        v = value.get(k)
        if v is None:
            continue
        if v <= 0.4:
            out[k + "_word"] = lo
        elif v >= 0.6:
            out[k + "_word"] = hi
        else:
            out[k + "_word"] = ""
    return out


def fill(template: str, value, warnings: List[str], cid: str) -> str:
    mapping: Dict[str, str] = {}
    if isinstance(value, dict):
        for k, v in value.items():
            mapping[k] = ", ".join(str(x) for x in v) if isinstance(v, list) else str(v)
        if {"weight", "time", "space", "flow"} & set(value.keys()):
            mapping.update(derive_laban(value))
    elif isinstance(value, list):
        mapping["value"] = ", ".join(str(x) for x in value)
    else:
        mapping["value"] = str(value)

    def repl(m):
        key = m.group(1)
        if key in mapping:
            return mapping[key]
        warnings.append("%s: placeholder {%s} not filled" % (cid, key))
        return ""
    text = re.sub(r"\{([A-Za-z0-9_]+)\}", repl, template)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\s+([,.;])", r"\1", text)
    return text.strip()


def _clause_for(control: dict) -> str:
    if control.get("clause"):
        return control["clause"]
    for prefix, clause in FIELD_CLAUSE:
        if control["field"].startswith(prefix):
            return clause
    return "subject_action"


def _loss(loss_id, field, requested, model, capability, projection, replacement, ltype, severity, accepted=True, code=None):
    rec = {"loss_id": loss_id, "canonical_field": field, "requested": requested, "provider": model,
           "capability": capability, "projection": projection, "replacement": replacement,
           "loss": {"type": ltype, "severity": severity}, "accepted": accepted}
    if code:
        rec["loss_code"] = code
    return rec


def emit(run_dir: Path, model: str) -> dict:
    result = check(run_dir)
    if not result.ok():
        raise SystemExit("emit blocked: check failed\n" + "\n".join(" - " + e for e in result.errors))
    ir = load_ir(run_dir)
    profile = load_yaml(PROFILES_DIR / ("%s.yaml" % model))
    treatments = load_treatments()
    warnings: List[str] = list(result.warnings)
    losses: List[dict] = []
    settings: Dict[str, object] = {}
    native_fields = set(profile.get("native_fields", []))
    limit = None
    for f in profile.get("facts", []):
        if f.get("key") == "prompt_char_limit":
            limit = f.get("value")
    negative_field = any(f.get("key") == "negative_prompt_field" and f.get("value") for f in profile.get("facts", []))

    # Candidate lines: (clause, sort_key, text, source)
    lines: List[dict] = []

    # entities → subject_action (subject first: identity/subject leads the compression order)
    for i, ent in enumerate(ir["entities"]):
        if not ent["description"].strip():
            continue
        lines.append({"clause": "subject_action", "key": (0, i), "text": ent["description"].strip().rstrip(".") + ".",
                      "short": (ent.get("short") or "").strip().rstrip(".") + "." if ent.get("short") else None,
                      "source": {"kind": "entity", "id": ent["id"], "origin": ent.get("origin", "UNKNOWN")},
                      "importance": 1.0, "lock": True, "droppable": False})

    # beats → ordered action sentences
    beats = sorted(ir["beats"], key=lambda b: b["order"])
    n = len(beats)
    anchors_by_id = {a["id"]: a for a in ir.get("anchors", [])}
    for i, b in enumerate(beats):
        lead = "First," if i == 0 else ("Finally," if i == n - 1 else "Then")
        delta = comparison_clause(b["relative"], anchors_by_id) if b.get("relative") else ""
        def beat_text(desc: str, with_pose: bool) -> str:
            desc = desc.strip().rstrip(".")
            body = desc[0].lower() + desc[1:] if desc and lead != "First," else desc
            t = "%s %s%s." % (lead, body, ", " + delta if delta else "")
            if with_pose and b.get("key_pose"):
                t += " Key pose: %s." % b["key_pose"].strip().rstrip(".")
            return t
        lines.append({"clause": "subject_action", "key": (1, b["order"]), "text": beat_text(b["description"], True),
                      "short": beat_text(b["short"], False) if b.get("short") else None,
                      "source": {"kind": "beat", "id": b["id"], "origin": b.get("origin", "UNKNOWN")},
                      "importance": b["importance"], "lock": True, "droppable": False})
        # the anchor is stated once, as a visible fact, right after its beat (R-16)
        for a in ir.get("anchors", []):
            if a["beat"] == b["id"]:
                lines.append({"clause": "subject_action", "key": (1, b["order"] + 0.5),
                              "text": a["description"].strip().rstrip(".") + ".", "short": None,
                              "source": {"kind": "anchor", "id": a["id"], "origin": "PROJECT_DERIVED"},
                              "importance": 1.0, "lock": True, "droppable": False})

    # controls
    emitted_controls = []
    for c in sorted(ir["controls"], key=lambda x: (-x["importance"], x["id"])):
        disp = c["disposition"]
        requested = {"value": c["value"], "unit": None}
        if disp in ("omitted", "unsupported", "unknown"):
            ltype = {"omitted": "priority_suppression", "unsupported": "unsupported_semantic", "unknown": "observability_loss"}[disp]
            losses.append(_loss("loss_%s" % c["id"], c["field"], requested, model, c["capability"], disp, None, ltype,
                                "high" if c["lock"] else "medium", accepted=not c["lock"]))
            continue
        if disp == "approximated":
            losses.append(_loss("loss_%s" % c["id"], c["field"], requested, model, c["capability"], "approximate",
                                "approximate wording", "approximation", "medium"))
        if disp == "semantic" and c.get("exactness") == "exact":
            ltype = "temporal_loss" if c["field"].startswith(("time.", "beats")) else "approximation"
            losses.append(_loss("loss_%s" % c["id"], c["field"], requested, model, c["capability"], "semantic",
                                "order wording", ltype, "medium", code="temporal_precision_unenforceable" if ltype == "temporal_loss" else None))
        native_text = None
        if disp == "native":
            field_key = c["field"].split(".")[-1]
            if field_key in native_fields or c["field"] in native_fields:
                settings[field_key] = c["value"]
            else:
                # Resolve against the selected route: carry through text or block; never drop silently.
                tmpl = NATIVE_TEXT.get(field_key)
                if tmpl:
                    native_text = tmpl.format(v=c["value"])
                    losses.append(_loss("loss_%s_route" % c["id"], c["field"], requested, model, "semantic", "compressed_to_text",
                                        native_text, "approximation", "medium" if c["lock"] else "low",
                                        code="native_field_unsupported_by_route"))
                elif c["lock"]:
                    raise SystemExit("emit blocked: locked native control %s (%s) has no channel on %s: no native field and no text fallback (unsupported_error)"
                                     % (c["id"], c["field"], model))
                else:
                    losses.append(_loss("loss_%s_route" % c["id"], c["field"], requested, model, "unknown", "omitted", None,
                                        "unsupported_semantic", "low", accepted=True, code="native_field_unsupported_by_route"))
                    continue
        # wording
        text = native_text
        short = None
        tid = c.get("treatment")
        if tid:
            t = treatments[tid]
            w = t["_wording"]
            template = w["dialects"].get(model) or w["core"]
            if template:
                text = fill(template, c["value"], warnings, c["id"])
            if w.get("short"):
                short = fill(w["short"], c["value"], warnings, c["id"])
        if text is None and disp == "native":
            continue  # API settings carry native controls; no prose unless a treatment gives it
        if text is None:
            if c["field"].startswith("negatives"):
                text = fill("{value}", c["value"], warnings, c["id"])
            elif isinstance(c["value"], (str, int, float)):
                text = str(c["value"])
            elif isinstance(c["value"], dict):
                text = "; ".join("%s: %s" % (k, v) for k, v in c["value"].items())
            else:
                text = ", ".join(str(v) for v in c["value"])
        if not text:
            continue
        # dialect lens: agnostic intents in the IR, model syntax applied here and recorded in the receipt
        lever_used = None
        emphasis = c["value"].get("emphasis") if isinstance(c["value"], dict) else None
        if emphasis:
            lever = select_lever(profile, "emphasis")
            if lever:
                text = apply_emphasis(text, emphasis, lever, warnings, c["id"])
                if short:
                    short = apply_emphasis(short, emphasis, lever, [], c["id"])
                lever_used = {"intent": "emphasis", "syntax": lever["syntax"], "evidence": lever.get("evidence", "unknown")}
            elif c["importance"] >= 0.7:
                losses.append(_loss("loss_%s_emphasis" % c["id"], c["field"], {"value": emphasis, "unit": None}, model, "unknown",
                                    "semantic", "core wording, no emphasis marks", "provider_attention_loss", "low",
                                    code="no_lever_for_intent:emphasis"))
        clause = _clause_for(c)
        source = {"kind": "control", "id": c["id"], "treatment": tid, "origin": c["origin"]}
        if lever_used:
            source["lever"] = lever_used
        if native_text is not None:
            source["realization"] = "compressed_to_text"
        lines.append({"clause": clause, "key": (2, -c["importance"], c["id"]), "text": text, "short": short,
                      "source": source,
                      "importance": c["importance"], "lock": c["lock"], "droppable": not c["lock"], "control": c})
        emitted_controls.append(c["id"])

    def assemble(active_lines: List[dict]) -> Tuple[str, List[dict], Optional[str]]:
        clause_order = profile.get("clause_order", ["shot", "subject_action", "performance", "timing", "camera", "negatives"])
        prompt_parts: List[str] = []
        receipt: List[dict] = []
        negative_text = None
        line_no = 0
        for clause in clause_order:
            items = sorted([l for l in active_lines if l["clause"] == clause], key=lambda l: l["key"])
            if not items:
                continue
            if clause == "negatives":
                neg_texts = [l["text"].rstrip(".") for l in items]
                joined = "; ".join(neg_texts)
                if negative_field:
                    negative_text = joined
                    for l in items:
                        line_no += 1
                        receipt.append({"line": line_no, "clause": clause, "channel": "negative_prompt", "text": l["text"], "source": l["source"]})
                    continue
                text = "Avoid: %s." % joined
                line_no += 1
                prompt_parts.append(text)
                receipt.append({"line": line_no, "clause": clause, "channel": "prompt", "text": text,
                                "source": [l["source"] for l in items]})
                continue
            texts = []
            for l in items:
                t = l["text"].strip()
                if not t.endswith((".", "!", "?")):
                    t += "."
                texts.append(t)
                line_no += 1
                receipt.append({"line": line_no, "clause": clause, "channel": "prompt", "text": t, "source": l["source"]})
            prompt_parts.append(" ".join(texts))
        return "\n\n".join(prompt_parts), receipt, negative_text

    active_lines = list(lines)
    dropped: List[str] = []
    compressed: List[str] = []
    prompt, receipt, negative_text = assemble(active_lines)
    # Budget, in the research's compression order: first compress lines to their short form
    # (lowest importance first; compressed_to_text), then drop unlocked lines (priority_suppression),
    # then block with options. Locked content is never squeezed silently.
    while limit and len(prompt) > limit:
        compressible = [l for l in active_lines if l.get("short") and l["text"] != l["short"]]
        if compressible:
            victim = sorted(compressible, key=lambda l: (l["importance"], str(l["source"]["id"])))[0]
            victim["text"] = victim["short"]
            compressed.append(victim["source"]["id"])
            c = victim.get("control", {})
            losses.append(_loss("loss_%s_short" % victim["source"]["id"], c.get("field", victim["source"]["kind"]),
                                {"value": "full wording", "unit": None}, model, c.get("capability", "semantic"),
                                "compressed_to_text", "short wording", "approximation", "low", code="token_budget"))
            prompt, receipt, negative_text = assemble(active_lines)
            continue
        droppable = [l for l in active_lines if l.get("droppable")]
        if not droppable:
            state_changing = [pw["id"] for pw in ir["pathways"] if any(s["kind"] == "effect" for s in pw["stages"])]
            options = ["raise the model's prompt limit in the profile if the real route allows it",
                       "shorten locked content in the IR (beats, locks, camera) and re-emit"]
            if len(state_changing) > 1:
                options.insert(0, "split into one clip per causal event (research rule R3): pathways %s" % ", ".join(state_changing))
            raise SystemExit("emit blocked: prompt is %d chars against a %d-char limit and only locked content remains (unsupported_error). Options: %s"
                             % (len(prompt), limit, " | ".join(options)))
        victim = sorted(droppable, key=lambda l: (l["importance"], str(l["source"]["id"])))[0]
        active_lines.remove(victim)
        c = victim.get("control", {})
        dropped.append(victim["source"]["id"])
        losses.append(_loss("loss_%s_budget" % victim["source"]["id"], c.get("field", "?"), {"value": c.get("value"), "unit": None},
                            model, c.get("capability", "semantic"), "omitted", None, "priority_suppression", "low", code="token_budget"))
        prompt, receipt, negative_text = assemble(active_lines)

    prompt_bytes = (prompt + "\n").encode("utf-8")
    (run_dir / "prompt.txt").write_bytes(prompt_bytes)
    if negative_text is not None:
        (run_dir / "negative.txt").write_text(negative_text + "\n", encoding="utf-8")
    with open(run_dir / "loss.jsonl", "w", encoding="utf-8") as fh:
        for rec in losses:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    receipt_doc = {"run_id": ir["run_id"], "model": model,
                   "prompt_sha256": hashlib.sha256(prompt_bytes).hexdigest(),
                   "prompt_sha256_of": "prompt.txt bytes as written (including the trailing newline)",
                   "lines": receipt}
    (run_dir / "receipt.json").write_text(json.dumps(receipt_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    dispositions: Dict[str, int] = {}
    for c in ir["controls"]:
        dispositions[c["disposition"]] = dispositions.get(c["disposition"], 0) + 1
    report = {"run_id": ir["run_id"], "model": model, "emitted_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
              "chars": len(prompt), "char_limit": limit, "mode": "C→A text_interpretation_only", "control_level": "L0–L1",
              "settings": settings, "dispositions": dispositions, "dropped_for_budget": dropped,
              "compressed_for_budget": compressed,
              "loss_records": len(losses), "fit": result.fit, "warnings": warnings,
              "validity": {"parses": True, "schema": True, "decisions_correct": "not judged by code", "render_succeeded": "pending"}}
    (run_dir / "emit_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report
