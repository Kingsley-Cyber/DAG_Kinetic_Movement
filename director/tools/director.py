#!/usr/bin/env python3
"""Director tools: `check` validates an IR the LLM wrote; `emit` writes the prompt deterministically.

Code never parses the ask or reasons about the scene. It checks consistency of what the LLM
decided and assembles wording from treatments. Python 3.9, stdlib + pyyaml + jsonschema.
"""
import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]  # director/
SCHEMA_PATH = ROOT / "ir.schema.json"
PASSES_PATH = ROOT / "passes.yaml"
TREATMENTS_DIR = ROOT / "treatments"
PROFILES_DIR = ROOT / "profiles"

STAGE_ORDER = ["precondition", "anticipation", "approach", "contact", "transfer",
               "effect", "follow_through", "recovery", "postcondition"]
CAPABILITY_TO_DISPOSITIONS = {
    "native": {"native"},
    "approximate": {"approximated", "omitted"},
    "semantic": {"semantic", "omitted"},
    "unsupported": {"unsupported"},
    "unknown": {"unknown", "omitted"},
}
# Field prefix → natural-language clause (format_ownership.md clause order).
FIELD_CLAUSE = [
    ("clip.", "shot"), ("camera.", "camera"), ("light_color.", "camera"), ("style.", "camera"),
    ("performance.", "performance"), ("audio.", "performance"),
    ("time.", "timing"), ("attention.", "timing"),
    ("negatives", "negatives"),
    ("entities", "subject_action"), ("interaction.", "subject_action"), ("action.", "subject_action"),
    ("physics.", "subject_action"), ("world.", "subject_action"), ("staging.", "subject_action"),
    ("continuity.", "subject_action"), ("intent.", "subject_action"),
]
FIT_FITS, FIT_TIGHT = 0.85, 1.0
SPEECH_WPM_MAX = 190  # NATURAL_DIALOGUE_MODE.md / ugc_realism_reference: 150–190 wpm


# ----------------------------------------------------------------------------- loading

def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_ir(run_dir: Path) -> dict:
    return load_json(run_dir / "ir.json")


def load_passes() -> dict:
    data = load_yaml(PASSES_PATH)
    return {p["id"]: p for p in data["passes"]}


def parse_treatment(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("treatment without frontmatter: %s" % path)
    front = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    wording = {"core": None, "short": None, "dialects": {}}
    for block in re.finditer(r"```prompt([^\n]*)\n(.*?)```", body, re.S):
        tag = block.group(1).strip()
        content = block.group(2).strip()
        if tag == "core":
            wording["core"] = content
        elif tag == "core short":
            wording["short"] = content
        else:
            dm = re.match(r"dialect=([A-Za-z0-9_.-]+)", tag)
            if dm:
                wording["dialects"][dm.group(1)] = content
    front["_path"] = str(path.relative_to(ROOT))
    front["_wording"] = wording
    return front


def load_treatments() -> Dict[str, dict]:
    out = {}
    if not TREATMENTS_DIR.exists():
        return out
    for path in sorted(TREATMENTS_DIR.rglob("*.md")):
        t = parse_treatment(path)
        if "id" in t:
            out[t["id"]] = t
    return out


# ----------------------------------------------------------------------------- check

class CheckResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.notes: List[str] = []
        self.fit: dict = {}

    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict:
        return {"ok": self.ok(), "errors": self.errors, "warnings": self.warnings,
                "notes": self.notes, "fit": self.fit}


def _field_owner(field: str, passes: dict) -> Optional[str]:
    best, best_len = None, -1
    for pid, p in passes.items():
        for prefix in p.get("owns", []):
            if field == prefix or field.startswith(prefix + ".") or field.startswith(prefix):
                if len(prefix) > best_len:
                    best, best_len = pid, len(prefix)
    return best


def _causal_closure(beats: List[dict]) -> Dict[str, set]:
    by_id = {b["id"]: b for b in beats}
    memo: Dict[str, set] = {}

    def reach(bid: str, seen: Tuple[str, ...] = ()) -> set:
        if bid in memo:
            return memo[bid]
        out = set()
        for parent in by_id.get(bid, {}).get("caused_by", []):
            if parent in seen:
                continue
            out.add(parent)
            out |= reach(parent, seen + (bid,))
        memo[bid] = out
        return out

    return {b["id"]: reach(b["id"]) for b in beats}


def check(run_dir: Path) -> CheckResult:
    res = CheckResult()
    ir = load_ir(run_dir)
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(ir), key=lambda e: list(e.path))
    for e in schema_errors:
        loc = "/".join(str(p) for p in e.path) or "<root>"
        res.errors.append("schema: %s: %s" % (loc, e.message))
    if schema_errors:
        return res

    passes = load_passes()
    treatments = load_treatments()
    beats = sorted(ir["beats"], key=lambda b: b["order"])
    beat_ids = [b["id"] for b in beats]
    beat_order = {b["id"]: b["order"] for b in beats}

    # pass plan
    planned = {p["pass"]: p for p in ir["pass_plan"]}
    for pid, p in passes.items():
        if pid not in planned:
            res.errors.append("pass_plan: pass '%s' missing from pass_plan" % pid)
        elif p.get("activate") == "mandatory" and not planned[pid]["active"]:
            res.errors.append("pass_plan: mandatory pass '%s' is inactive" % pid)
    for pid in planned:
        if pid not in passes:
            res.errors.append("pass_plan: unknown pass '%s'" % pid)
    active = {pid for pid, p in planned.items() if p["active"]}

    # beats: order, references
    orders = [b["order"] for b in beats]
    if orders != list(range(1, len(beats) + 1)):
        res.errors.append("beats: order must be 1..n without gaps; got %s" % orders)
    if len(set(beat_ids)) != len(beat_ids):
        res.errors.append("beats: duplicate beat ids")
    for b in beats:
        for ref in b["after"]:
            if ref not in beat_order:
                res.errors.append("beats: %s.after references unknown beat '%s'" % (b["id"], ref))
            elif beat_order[ref] >= b["order"]:
                res.errors.append("beats: %s.after '%s' is not earlier" % (b["id"], ref))
        for ref in b["caused_by"]:
            if ref not in beat_order:
                res.errors.append("beats: %s.caused_by references unknown beat '%s'" % (b["id"], ref))
            elif beat_order[ref] >= b["order"]:
                res.errors.append("beats: %s caused_by '%s' which is not earlier (a reaction cannot precede its cause)" % (b["id"], ref))

    # beats: fit
    load = sum(b["min_s"] for b in beats)
    duration = ir["clip"]["duration_s"]
    if duration is None:
        res.fit = {"verdict": "UNDERSPECIFIED", "load_s": round(load, 3), "duration_s": None}
        res.notes.append("fit: no duration; order and relative shares only, no seconds invented")
    else:
        ratio = load / duration
        verdict = "FITS" if ratio <= FIT_FITS else ("TIGHT" if ratio <= FIT_TIGHT else "OVERLOADED")
        res.fit = {"verdict": verdict, "load_s": round(load, 3), "duration_s": duration, "ratio": round(ratio, 3)}
        if verdict == "TIGHT":
            res.warnings.append("fit: TIGHT (load %.2fs of %.2fs)" % (load, duration))
        if verdict == "OVERLOADED":
            closure = _causal_closure(beats)
            cuts = [b["id"] for b in sorted(beats, key=lambda x: (x["importance"], x["order"]))][:2]
            overlappable = []
            for i, a in enumerate(beats):
                for c in beats[i + 1:]:
                    if a["id"] not in closure[c["id"]] and c["id"] not in closure[a["id"]]:
                        overlappable.append("%s+%s" % (a["id"], c["id"]))
            res.fit["options"] = {
                "cut_lowest_importance": cuts,
                "overlap_non_causal_pairs": overlappable[:6],
                "split": "split into more shots or clips with a state handoff",
                "lengthen": "raise duration if the model allows",
            }
            res.errors.append("fit: OVERLOADED (load %.2fs > %.2fs). Options: %s" % (load, duration, json.dumps(res.fit["options"])))

    # hands ledger
    ledger: Dict[Tuple[str, str, str], str] = {}
    for h in ir["hands"]:
        key = (h["actor"], h["hand"], h["beat"])
        if key in ledger:
            res.errors.append("hands: duplicate ledger entry for %s" % (key,))
        ledger[key] = h["state"]
        if h["beat"] not in beat_order:
            res.errors.append("hands: ledger entry references unknown beat '%s'" % h["beat"])

    # pathways
    for pw in ir["pathways"]:
        allowed_holdings = {pw["object"]} | set(pw.get("parts", []))
        stages = pw["stages"]
        kinds = [s["kind"] for s in stages]
        idx = [STAGE_ORDER.index(k) for k in kinds]
        if idx != sorted(idx):
            res.errors.append("pathway %s: stages out of causal order %s" % (pw["id"], kinds))
        kindset = set(kinds)
        if "anticipation" not in kindset:
            res.errors.append("pathway %s: no anticipation stage (minimum anticipation → action → aftermath)" % pw["id"])
        if not kindset & {"contact", "transfer", "effect"}:
            res.errors.append("pathway %s: no action stage (contact/transfer/effect)" % pw["id"])
        if not kindset & {"follow_through", "recovery", "postcondition"}:
            res.errors.append("pathway %s: no aftermath stage" % pw["id"])
        if stages and stages[-1]["state_after"] != pw["end_state"]:
            res.errors.append("pathway %s: last stage ends in '%s', not end_state '%s'" % (pw["id"], stages[-1]["state_after"], pw["end_state"]))
        seen_kinds: set = set()
        last_beat_order = 0
        prev_state_after: Optional[str] = None
        for s in stages:
            # within-pathway state continuity: each stage starts where the previous one ended
            if prev_state_after is not None and s["state_before"] != prev_state_after:
                res.errors.append("pathway %s/%s: disconnected state chain: begins in '%s' but the previous stage ended in '%s'"
                                  % (pw["id"], s["id"], s["state_before"], prev_state_after))
            prev_state_after = s["state_after"]
            if s["beat"] not in beat_order:
                res.errors.append("pathway %s/%s: unknown beat '%s'" % (pw["id"], s["id"], s["beat"]))
            else:
                if beat_order[s["beat"]] < last_beat_order:
                    res.errors.append("pathway %s/%s: beat order goes backwards" % (pw["id"], s["id"]))
                last_beat_order = beat_order[s["beat"]]
            changes_state = s["state_after"] != s["state_before"]
            if changes_state:
                # A contact may establish the grip; a transfer needs a contact first; any later
                # state change (effect, follow-through, ...) needs both a contact and a transfer.
                if s["kind"] in ("anticipation", "approach"):
                    missing = ["contact", "transfer"]
                elif s["kind"] == "transfer":
                    missing = [k for k in ("contact",) if k not in seen_kinds]
                elif s["kind"] in ("effect", "follow_through", "recovery", "postcondition"):
                    missing = [k for k in ("contact", "transfer") if k not in seen_kinds]
                else:
                    missing = []
                if missing:
                    res.errors.append("pathway %s/%s: state changes '%s' → '%s' without prior %s stage(s) (magic jump)"
                                      % (pw["id"], s["id"], s["state_before"], s["state_after"], "/".join(missing)))
            if s["kind"] == "effect" and not (s.get("reaction") or "").strip():
                res.errors.append("pathway %s/%s: effect stage has no stated reaction (impact-and-physics language)" % (pw["id"], s["id"]))
            # hands: distinct (actor, hand) pairs only; one hand cannot be counted twice
            pairs = [(hd["actor"], hd["hand"]) for hd in s["hands"]]
            if len(set(pairs)) < len(pairs):
                res.errors.append("pathway %s/%s: the same hand is listed twice (%s)" % (pw["id"], s["id"], pairs))
            if len(set(pairs)) < s["hands_required"]:
                res.errors.append("pathway %s/%s: needs %d hand(s), lists %d distinct hand(s)" % (pw["id"], s["id"], s["hands_required"], len(set(pairs))))
            for hd in s["hands"]:
                state = ledger.get((hd["actor"], hd["hand"], s["beat"]))
                if state is None:
                    res.errors.append("pathway %s/%s: no ledger entry for %s %s hand at beat %s" % (pw["id"], s["id"], hd["actor"], hd["hand"], s["beat"]))
                    continue
                if state == "camera":
                    res.errors.append("pathway %s/%s: %s %s hand holds the camera at beat %s and cannot be used (hand ledger)" % (pw["id"], s["id"], hd["actor"], hd["hand"], s["beat"]))
                elif state.startswith("holding:") and state.split(":", 1)[1] not in allowed_holdings:
                    res.errors.append("pathway %s/%s: %s %s hand is %s at beat %s; needed for %s" % (pw["id"], s["id"], hd["actor"], hd["hand"], state, s["beat"], pw["object"]))
                elif state.startswith("on:"):
                    res.errors.append("pathway %s/%s: %s %s hand is %s at beat %s" % (pw["id"], s["id"], hd["actor"], hd["hand"], state, s["beat"]))
            seen_kinds.add(s["kind"])
        contacts = [i for i, s in enumerate(stages) if s["kind"] == "contact"]
        for ci in contacts:
            later_effects = [s for s in stages[ci + 1:] if s["kind"] == "effect" and (s.get("reaction") or "").strip()]
            if not later_effects:
                res.errors.append("pathway %s: contact '%s' has no later effect with a stated reaction" % (pw["id"], stages[ci]["id"]))

    # controls
    seen_ids: set = set()
    camera_cov: set = set()
    style_tier_passes = {pid for pid, p in passes.items() if p.get("tier") in ("style", "render")}
    for c in ir["controls"]:
        if c["id"] in seen_ids:
            res.errors.append("controls: duplicate id '%s'" % c["id"])
        seen_ids.add(c["id"])
        if c["pass"] not in passes:
            res.errors.append("controls %s: unknown pass '%s'" % (c["id"], c["pass"]))
            continue
        if c["pass"] not in active:
            res.errors.append("controls %s: pass '%s' is not active in pass_plan" % (c["id"], c["pass"]))
        owner = _field_owner(c["field"], passes)
        if owner is None:
            res.errors.append("controls %s: field '%s' has no owner pass" % (c["id"], c["field"]))
        elif owner != c["pass"]:
            res.errors.append("controls %s: field '%s' is owned by '%s', written by '%s' (one owner per field)" % (c["id"], c["field"], owner, c["pass"]))
        allowed = CAPABILITY_TO_DISPOSITIONS[c["capability"]]
        if c["disposition"] not in allowed:
            res.errors.append("controls %s: disposition '%s' inconsistent with capability '%s'" % (c["id"], c["disposition"], c["capability"]))
        if c["lock"] and c["disposition"] == "omitted":
            res.errors.append("controls %s: locked control cannot be omitted" % c["id"])
        if c["lock"] and c.get("exactness") == "exact" and c["capability"] in ("semantic", "unknown", "unsupported"):
            res.errors.append("controls %s: locked exact request cannot be enforced by text (capability %s); block or degrade explicitly" % (c["id"], c["capability"]))
        if c.get("treatment") and c["treatment"] not in treatments:
            res.errors.append("controls %s: treatment '%s' not found" % (c["id"], c["treatment"]))
        if c["pass"] in style_tier_passes and re.match(r"^(beats|pathways|hands)", c["field"]):
            res.errors.append("controls %s: a %s-tier pass may not write '%s' (order first, texture second)" % (c["id"], passes[c["pass"]]["tier"], c["field"]))
        if c["field"].startswith("camera."):
            camera_cov.add(c["field"].split(".")[1])
            if isinstance(c["value"], dict):
                camera_cov |= set(c["value"].keys())
        if c["field"] == "audio.dialogue" and isinstance(c["value"], str) and duration:
            words = len(c["value"].split())
            cap = duration * SPEECH_WPM_MAX / 60.0
            if words > cap:
                res.errors.append("controls %s: %d words exceed speech capacity %.1f for %.1fs" % (c["id"], words, cap, duration))
    if "camera" in active:
        if not ({"motion"} & camera_cov):
            res.errors.append("camera: no camera.motion control (explicit camera grammar is mandatory)")
        if not ({"framing", "optics"} & camera_cov):
            res.errors.append("camera: no camera.framing or camera.optics control (explicit camera grammar is mandatory)")

    return res


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
    for i, b in enumerate(beats):
        lead = "First," if i == 0 else ("Finally," if i == n - 1 else "Then")
        def beat_text(desc: str, with_pose: bool) -> str:
            desc = desc.strip().rstrip(".")
            t = "%s %s." % (lead, desc[0].lower() + desc[1:] if desc and lead != "First," else desc)
            if with_pose and b.get("key_pose"):
                t += " Key pose: %s." % b["key_pose"].strip().rstrip(".")
            return t
        lines.append({"clause": "subject_action", "key": (1, b["order"]), "text": beat_text(b["description"], True),
                      "short": beat_text(b["short"], False) if b.get("short") else None,
                      "source": {"kind": "beat", "id": b["id"], "origin": b.get("origin", "UNKNOWN")},
                      "importance": b["importance"], "lock": True, "droppable": False})

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


# ----------------------------------------------------------------------------- cli

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="director", description="check an IR; emit a prompt")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pc = sub.add_parser("check", help="validate a run's ir.json")
    pc.add_argument("run_dir")
    pc.add_argument("--json", action="store_true")
    pe = sub.add_parser("emit", help="emit prompt.txt + receipt + loss records for a model profile")
    pe.add_argument("run_dir")
    pe.add_argument("--model", required=True)
    args = ap.parse_args(argv)
    run_dir = Path(args.run_dir).resolve()
    if args.cmd == "check":
        res = check(run_dir)
        if args.json:
            print(json.dumps(res.to_dict(), indent=2))
        else:
            for e in res.errors:
                print("ERROR  " + e)
            for w in res.warnings:
                print("WARN   " + w)
            for n in res.notes:
                print("NOTE   " + n)
            print("fit: %s" % json.dumps(res.fit))
            print("CHECK %s" % ("GREEN" if res.ok() else "RED (%d error%s)" % (len(res.errors), "" if len(res.errors) == 1 else "s")))
        return 0 if res.ok() else 1
    if args.cmd == "emit":
        report = emit(run_dir, args.model)
        print(json.dumps(report, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
