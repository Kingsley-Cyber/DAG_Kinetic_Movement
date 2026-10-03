"""Director check: validates an IR the LLM wrote. Never parses the ask or reasons about the scene.

Python 3.9, stdlib + pyyaml + jsonschema. Split from director.py (CLI) and diremit.py (emitter).
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]  # director/
SCHEMA_PATH = ROOT / "ir.schema.json"
PASSES_PATH = ROOT / "passes.yaml"
TREATMENTS_DIR = ROOT / "treatments"
PROFILES_DIR = ROOT / "profiles"
CAMERA_MOVES_PATH = ROOT / "vocab" / "camera_moves.yaml"
# R-53: words that make an optics (lens) move read as the camera body moving. Conventions.
OPTICS_MOTION_PHRASES = ("camera moves", "moves the camera", "dolly", "track")
OUTCOME_KINDS = ("pass", "fail", "indeterminate", "not_applicable", "unobservable")

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
STAGE_MIN_S = 0.2  # convention (R-57): minimum readable seconds per pathway stage on a beat
SPEECH_WPM_MAX = 190  # NATURAL_DIALOGUE_MODE.md / ugc_realism_reference: 150–190 wpm

# Relative prompting (R-16) and vague-word lint (R-59). The word lists are conventions. The
# magnitude lint is a warning; it is promoted to a failure only by experiment E2 (plan/EXPERIMENTS.md).
COMPARATIVES = {  # quality → (more, less)
    "speed": ("faster", "slower"),
    "weight": ("heavier", "lighter"),
    "reach": ("wider", "tighter"),
    "size": ("bigger", "smaller"),
    "intensity": ("more intense", "gentler"),
    "distance": ("farther", "closer"),
    "tempo": ("quicker", "slower"),
}
MAGNITUDE_WORDS = ("fast", "heavy", "powerful", "strong", "wide", "hard", "big", "exaggerated")
NAMED_TECHNIQUES = ("slow motion", "real-time", "speed ramp", "time-lapse",  # learned meaning: allowed
                    "wide shot", "wide lens", "wide angle", "wide-angle", "hard cut", "hard light", "big close-up")
VAGUE_STYLE_WORDS = ("cinematic", "epic", "beautiful", "stunning", "dramatic", "dynamic", "professional", "high quality")


def comparison_clause(relative: List[dict], anchors: Dict[str, dict]) -> str:
    """'slightly slower than the first reach and heavier than the jab' from a beat's deltas."""
    parts = []
    for r in relative:
        more, less = COMPARATIVES[r["quality"]]
        word = more if r["direction"] == "more" else less
        if r["step"] == "slightly":
            word = "slightly " + word
        elif r["step"] == "much":
            word = "much " + word
        parts.append("%s than %s" % (word, anchors[r["relative_to"]]["label"].strip()))
    return " and ".join(parts)


def lint_text(where: str, text: str, warnings: List[str]) -> None:
    """Warn on bare magnitude words and vague style words in LLM-written free text."""
    for sentence in re.split(r"(?<=[.!?;])\s+", text or ""):
        low = sentence.lower()
        masked = low
        for phrase in NAMED_TECHNIQUES:
            masked = masked.replace(phrase, " ")
        if not re.search(r"\bthan\b", low):
            for word in MAGNITUDE_WORDS:
                if re.search(r"\b%s\b" % re.escape(word), masked):
                    warnings.append("%s: bare magnitude word '%s' (state it relative to an anchor, or name the technique)" % (where, word))
        for word in VAGUE_STYLE_WORDS:
            if re.search(r"\b%s\b" % re.escape(word), low):
                warnings.append("%s: vague style word '%s': name the variables (colour, framing, lens, frame rate, mount, light)" % (where, word))


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
        self.outcomes: List[dict] = []

    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict:
        return {"ok": self.ok(), "errors": self.errors, "warnings": self.warnings,
                "notes": self.notes, "fit": self.fit, "outcomes": self.outcomes}


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


def _decision_controls(run_dir: Path) -> set:
    """Control ids that have a decision record in decisions.jsonl (missing file = none)."""
    path = Path(run_dir) / "decisions.jsonl"
    found: set = set()
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if isinstance(rec, dict) and rec.get("control"):
                found.add(rec["control"])
    return found


def _check_all(run_dir: Path) -> CheckResult:
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

    # relative prompting: anchors and deltas (R-16, IR level: hard)
    anchor_list = ir.get("anchors", [])
    anchors = {a["id"]: a for a in anchor_list}
    if len(anchors) != len(anchor_list):
        res.errors.append("anchors: duplicate anchor ids")
    for a in anchor_list:
        if a["beat"] not in beat_order:
            res.errors.append("anchors: %s: anchor references unknown beat '%s'" % (a["id"], a["beat"]))
    for b in beats:
        seen_qualities: set = set()
        for r in b.get("relative", []):
            a = anchors.get(r["relative_to"])
            if a is None:
                res.errors.append("beats: %s: unknown anchor '%s'" % (b["id"], r["relative_to"]))
                continue
            if a["beat"] in beat_order and beat_order[a["beat"]] >= b["order"]:
                res.errors.append("beats: %s: anchor is not earlier ('%s' sits on %s)" % (b["id"], a["id"], a["beat"]))
            if a["quality"] != r["quality"]:
                res.errors.append("beats: %s: quality mismatch (delta '%s' against a '%s' anchor)" % (b["id"], r["quality"], a["quality"]))
            if r["quality"] in seen_qualities:
                res.errors.append("beats: %s: one escalation per quality (two deltas for '%s')" % (b["id"], r["quality"]))
            seen_qualities.add(r["quality"])

    # physics causal events (R-41, R-42): one per beat, named cause, stated reaction and settle
    events = ir.get("physics_events", [])
    event_beat: Dict[str, str] = {}
    beats_with_event: set = set()
    for ev in events:
        eid = ev["event_id"]
        if eid in event_beat:
            res.errors.append("physics_events: duplicate event id '%s'" % eid)
        event_beat[eid] = ev["beat"]
        if ev["beat"] not in beat_order:
            res.errors.append("physics_events %s: event references unknown beat '%s'" % (eid, ev["beat"]))
        elif ev["beat"] in beats_with_event:
            res.errors.append("physics_events %s: one causal event per beat (beat %s already has one)" % (eid, ev["beat"]))
        beats_with_event.add(ev["beat"])
        for name in ("contact_surface", "primary_reaction", "settle"):
            if not ev[name].strip():
                res.errors.append("physics_events %s: edge admission: '%s' is empty (no effect without a named cause, contact and settle)" % (eid, name))
        if ev["contact_state"] == "near_contact" and ev["primary_reaction"].strip() and not ev.get("must_not_imply"):
            res.warnings.append("physics_events %s: near contact with a reaction: state what must not be implied" % eid)
        force = ev.get("force")
        if force is not None and ev["beat"] in beat_order:
            ref = force["relative_to"]
            if ref is None:
                own = [a for a in anchor_list if a["beat"] == ev["beat"] and a["quality"] in ("weight", "intensity")]
                if not own:
                    res.errors.append("physics_events %s: force anchor: a first event needs a weight or intensity anchor on its own beat" % eid)
            else:
                a = anchors.get(ref)
                if a is None:
                    res.errors.append("physics_events %s: force anchor: unknown anchor '%s'" % (eid, ref))
                elif a["quality"] not in ("weight", "intensity"):
                    res.errors.append("physics_events %s: force anchor: '%s' is a %s anchor, not weight or intensity" % (eid, ref, a["quality"]))
                elif a["beat"] in beat_order and beat_order[a["beat"]] >= beat_order[ev["beat"]]:
                    res.errors.append("physics_events %s: force anchor: '%s' is not earlier than the event" % (eid, ref))
    for ev in events:
        for dep in ev.get("depends_on", []):
            if dep not in event_beat:
                res.errors.append("physics_events %s: depends_on unknown event '%s'" % (ev["event_id"], dep))
            elif (event_beat[dep] in beat_order and ev["beat"] in beat_order
                  and beat_order[event_beat[dep]] >= beat_order[ev["beat"]]):
                res.errors.append("physics_events %s: depends_on '%s' which is not earlier (cause before effect)" % (ev["event_id"], dep))

    # spacing (R-60): constant motion throughout is the default failure
    if "action" in active:
        declared = [b["spacing"] for b in beats if b.get("spacing")]
        if not declared or all(s == "even" for s in declared):
            res.warnings.append("beats: constant motion: no beat declares spacing other than 'even' (ease_in, ease_out, ease_in_out)")

    # wording lint on LLM-written free text (warnings; treatment wording is not scanned)
    for b in beats:
        lint_text("beats %s" % b["id"], b["description"], res.warnings)
        if b.get("short"):
            lint_text("beats %s (short)" % b["id"], b["short"], res.warnings)
    for ent in ir["entities"]:
        lint_text("entities %s" % ent["id"], ent["description"], res.warnings)
    for c in ir["controls"]:
        if isinstance(c["value"], str):
            lint_text("controls %s" % c["id"], c["value"], res.warnings)

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
            cuts, remaining = [], load  # cut lowest-importance beats until the rest fits
            for cand in sorted(beats, key=lambda x: (x["importance"], x["order"])):
                if remaining <= duration:
                    break
                cuts.append(cand["id"])
                remaining -= cand["min_s"]
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
    # coupling checks (R-57): keep these few
    def _strings(value) -> str:
        if isinstance(value, str):
            return value
        if isinstance(value, dict):
            return " ".join(_strings(v) for v in value.values())
        if isinstance(value, (list, tuple)):
            return " ".join(_strings(v) for v in value)
        return ""

    event_on_beat = {ev["beat"]: ev for ev in events}
    for ev in events:
        if not ev["trigger"]["actor"].strip() or not ev["trigger"]["part"].strip():
            res.errors.append("physics_events %s: explicit: trigger needs actor and part" % ev["event_id"])
    for c in ir["controls"]:
        scoped = c.get("beat")
        if scoped is None:
            continue
        if scoped not in beat_order:
            res.errors.append("controls %s: control on unknown beat '%s'" % (c["id"], scoped))
            continue
        ev = event_on_beat.get(scoped)
        if ev is None or not c["field"].startswith("camera."):
            continue
        text = _strings(c["value"]).lower()
        if ev["contact_state"] in ("occluded_contact", "editorial_impact"):
            if ev["contact_surface"].strip().lower() in text and ("close-up" in text or "close up" in text):
                res.errors.append("controls %s: camera shows a hidden contact (event %s is %s)" % (c["id"], ev["event_id"], ev["contact_state"]))
        elif ev["contact_state"] == "physical_contact_confirmed":
            if any(phrase in text for phrase in ("off-screen", "out of frame", "cut away")):
                res.errors.append("controls %s: camera hides a confirmed contact (event %s)" % (c["id"], ev["event_id"]))
    stages_on_beat: Dict[str, int] = {}
    for pw in ir["pathways"]:
        for s in pw["stages"]:
            stages_on_beat[s["beat"]] = stages_on_beat.get(s["beat"], 0) + 1
    for b in beats:
        need = STAGE_MIN_S * stages_on_beat.get(b["id"], 0)
        if b["min_s"] + 1e-9 < need:
            res.errors.append("beats: %s: beat does not cover its pathway stages (%d stages need at least %.1fs; min_s is %.1fs)"
                              % (b["id"], stages_on_beat[b["id"]], need, b["min_s"]))

    # camera move validator (R-53): catalog id or custom + decision record; optics never as motion;
    # one move per shot unless beats order them
    move_controls = [c for c in ir["controls"] if c["field"].startswith("camera.")
                     and isinstance(c["value"], dict) and "move" in c["value"]]
    if move_controls:
        catalog = {m["id"]: m for m in load_yaml(CAMERA_MOVES_PATH)["moves"]}
        decided = _decision_controls(run_dir)
        for c in move_controls:
            move = c["value"]["move"]
            if move == "custom":
                if c["id"] not in decided:
                    res.errors.append("camera_move %s: unknown camera move: 'custom' needs a decision record with control '%s' in decisions.jsonl" % (c["id"], c["id"]))
            elif move not in catalog:
                res.errors.append("camera_move %s: unknown camera move '%s' (not in camera_moves.yaml; use 'custom' with a decision record)" % (c["id"], move))
            elif catalog[move].get("layer") == "optics":
                text = _strings(c["value"]).lower()
                hit = [p for p in OPTICS_MOTION_PHRASES if p in text]
                if hit:
                    res.errors.append("camera_move %s: optics written as camera motion ('%s' is a lens change but the value says '%s')" % (c["id"], move, hit[0]))
        unscoped = [c["id"] for c in move_controls if not c.get("beat")]
        if len(unscoped) > 1:
            res.errors.append("camera_move: one camera move per shot (controls %s have no beat; scope each move to a beat or keep one)" % ", ".join(unscoped))

    if "camera" in active:
        if not ({"motion", "movement", "move", "phrase"} & camera_cov):
            res.errors.append("camera: no camera.motion control (explicit camera grammar is mandatory)")
        if not ({"framing", "optics"} & camera_cov):
            res.errors.append("camera: no camera.framing or camera.optics control (explicit camera grammar is mandatory)")

    return res


# ----------------------------------------------------------------------------- scratchpad (R-58)

# Which pass owns each rule group. Error and warning messages start with the group name.
GROUP_OWNER = {
    "pass_plan": "synthesis",
    "beats": "time",
    "fit": "time",
    "anchors": "time",
    "hands": "interaction",
    "pathway": "interaction",
    "physics_events": "physics",
    "camera": "camera",
    "camera_move": "camera",
}
OPEN_KINDS = ("alternative", "conflict", "revision_request")
OPEN_STATUSES = ("open", "resolved", "escalated")
OPEN_REQUIRED = ("id", "kind", "from_pass", "to_pass", "field", "reason", "status")


def _group_of(message: str, control_pass: Dict[str, str]) -> Tuple[str, Optional[str]]:
    """Return (rule group, owner pass) for one error or warning message."""
    head = re.match(r"^([a-z_]+)(?: ([A-Za-z0-9_.-]+))?", message)
    group = head.group(1) if head else "other"
    if group == "controls":
        return "controls", control_pass.get(head.group(2) or "")
    if group == "schema":
        return "schema", None
    return group, GROUP_OWNER.get(group)


def _absent_input(ir: dict, group: str) -> Optional[str]:
    """Why a rule group had nothing to run on (R-51 not_applicable), or None."""
    if group == "anchors" and not ir.get("anchors") and not any(b.get("relative") for b in ir.get("beats", [])):
        return "no anchors or relative deltas in the IR"
    if group == "physics_events" and not ir.get("physics_events"):
        return "no physics events in the IR"
    if group == "hands" and not ir.get("hands"):
        return "no hand ledger entries in the IR"
    if group == "pathway" and not ir.get("pathways"):
        return "no pathways in the IR"
    if group == "controls" and not ir.get("controls"):
        return "no controls in the IR"
    if group == "camera":
        planned = {p["pass"]: p for p in ir.get("pass_plan", [])}
        if not planned.get("camera", {}).get("active"):
            return "camera pass is not active"
    if group == "camera_move" and not any(
            c["field"].startswith("camera.") and isinstance(c["value"], dict) and "move" in c["value"]
            for c in ir.get("controls", [])):
        return "no camera control names a catalog move"
    return None


def check(run_dir: Path, only_pass: Optional[str] = None) -> CheckResult:
    """Validate a run. With `only_pass`, keep only the rules that pass owns (per-pass acceptance).

    `outcomes` is one typed record per rule group: {rule, owner, outcome, detail}, outcome in OUTCOME_KINDS.
    """
    res = _check_all(run_dir)
    try:
        ir = load_ir(run_dir)
        control_pass = {c["id"]: c["pass"] for c in ir.get("controls", []) if isinstance(c, dict) and "id" in c}
    except Exception:
        ir, control_pass = {}, {}
    failing: Dict[str, set] = {}
    messages: Dict[str, List[str]] = {}
    for message in res.errors:
        group, owner = _group_of(message, control_pass)
        failing.setdefault(group, set()).add(owner)
        messages.setdefault(group, []).append(message)
    schema_failed = bool(messages.get("schema"))
    groups = sorted(set(GROUP_OWNER) | {"controls"})
    outcomes = [{"rule": "schema", "owner": "per control", "outcome": "fail" if schema_failed else "pass",
                 "detail": _detail(messages.get("schema", []))}]
    for group in groups:
        owner = GROUP_OWNER.get(group)
        if schema_failed:
            outcome, detail = "indeterminate", "schema invalid; rule not run"
        elif only_pass is not None and group != "controls" and owner != only_pass:
            outcome, detail = "not_applicable", "owned by pass '%s'; not run for pass '%s'" % (owner, only_pass)
        elif only_pass is not None and group == "controls" and only_pass not in failing.get("controls", {only_pass}):
            outcome, detail = "pass", ""
        elif group in failing and (only_pass is None or group != "controls" or only_pass in failing[group]):
            outcome, detail = "fail", _detail(messages.get(group, []))
        else:
            outcome, detail = "pass", ""
        if outcome == "pass":
            absent = _absent_input(ir, group)
            if absent:
                outcome, detail = "not_applicable", absent
        if group == "fit" and outcome == "pass" and res.fit.get("verdict") == "UNDERSPECIFIED":
            outcome, detail = "indeterminate", "no duration: order and relative shares only, no seconds invented"
        outcomes.append({"rule": group, "owner": owner or "per control", "outcome": outcome, "detail": detail})
    res.outcomes = outcomes
    if only_pass is not None:
        def keep(message: str) -> bool:
            group, owner = _group_of(message, control_pass)
            return group == "schema" or owner == only_pass
        res.errors = [m for m in res.errors if keep(m)]
        res.warnings = [m for m in res.warnings if keep(m)]
    return res


def _detail(messages: List[str]) -> str:
    if not messages:
        return ""
    return messages[0] if len(messages) == 1 else "%s (+%d more)" % (messages[0], len(messages) - 1)


def load_open_items(run_dir: Path) -> List[dict]:
    """Read open.jsonl (alternatives, conflicts, revision requests). Missing file = no items."""
    path = Path(run_dir) / "open.jsonl"
    if not path.exists():
        return []
    items = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except ValueError:
            raise ValueError("open.jsonl line %d: not valid JSON" % n)
        missing = [k for k in OPEN_REQUIRED if k not in item]
        if missing or item.get("kind") not in OPEN_KINDS or item.get("status") not in OPEN_STATUSES:
            raise ValueError("open.jsonl line %d: needs %s; kind in %s; status in %s"
                             % (n, ", ".join(OPEN_REQUIRED), "/".join(OPEN_KINDS), "/".join(OPEN_STATUSES)))
        items.append(item)
    return items


def blocking_open_items(run_dir: Path) -> List[dict]:
    return [i for i in load_open_items(run_dir)
            if i["status"] == "open" and i["kind"] in ("conflict", "revision_request")]


def pack(run_dir: Path, pass_id: str) -> dict:
    """The view of the scratchpad one pass receives: its entry, what it reads, locks, treatments, open items."""
    passes = load_passes()
    if pass_id not in passes:
        raise ValueError("unknown pass '%s'" % pass_id)
    entry = passes[pass_id]
    ir = load_ir(Path(run_dir))
    reads: Dict[str, object] = {}
    wanted = entry.get("reads", [])
    if "everything" in wanted:
        wanted = ["entities", "hands", "pathways", "beats", "anchors", "physics_events"] + ["controls:%s" % p for p in passes]
    for area in wanted:
        if area.startswith("controls:"):
            owner = area.split(":", 1)[1]
            found = [c for c in ir.get("controls", []) if c.get("pass") == owner]
            if found:
                reads[area] = found
        elif ir.get(area):
            reads[area] = ir[area]
    treatments = [
        {"id": t["id"], "triggers": t.get("triggers", []), "not_when": t.get("not_when", []),
         "from": t.get("from"), "origin": t.get("origin"), "path": t["_path"]}
        for t in load_treatments().values() if t.get("pass") == pass_id
    ]
    out = {
        "run_id": ir.get("run_id"),
        "ask": ir.get("ask"),
        "clip": ir.get("clip"),
        "pass": {k: entry.get(k) for k in ("id", "tier", "activate", "when", "after", "owns", "reads", "question", "sub_modules", "notes", "procedure") if entry.get(k) is not None},
        "reads": reads,
        "locked_controls": [c for c in ir.get("controls", []) if c.get("lock")],
        "treatments": sorted(treatments, key=lambda t: t["id"]),
        "open_items": [i for i in load_open_items(Path(run_dir)) if i.get("to_pass") == pass_id and i.get("status") == "open"],
    }
    if pass_id == "camera":
        moves = load_yaml(ROOT / "vocab" / "camera_moves.yaml")["moves"]
        out["camera_moves"] = [{"id": m["id"], "layer": m["layer"], "category": m["category"], "function": m["function"]} for m in moves]
    return out

