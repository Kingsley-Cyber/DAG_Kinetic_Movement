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
