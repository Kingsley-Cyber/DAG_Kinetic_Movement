"""RED → GREEN tests for director.py check and emit, using run 001 as the golden fixture."""
import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import director  # noqa: E402

RUN = HERE.parent.parent / "runs" / "001_bottle_selfie"


class TempRun:
    """Copy the golden run into a temp dir and allow IR mutation."""

    def __init__(self, mutate=None):
        self.dir = Path(tempfile.mkdtemp(prefix="director_test_"))
        for name in ("ir.json", "decisions.jsonl", "ask.md"):
            shutil.copy(RUN / name, self.dir / name)
        if mutate:
            ir = json.loads((self.dir / "ir.json").read_text())
            mutate(ir)
            (self.dir / "ir.json").write_text(json.dumps(ir))

    def cleanup(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def errors_for(mutate):
    tr = TempRun(mutate)
    try:
        return director.check(tr.dir).errors
    finally:
        tr.cleanup()


class CheckGreen(unittest.TestCase):
    def test_golden_run_is_green(self):
        res = director.check(RUN)
        self.assertEqual(res.errors, [])
        self.assertEqual(res.fit["verdict"], "FITS")


class HandLedger(unittest.TestCase):
    def test_two_hand_twist_fails_when_a_hand_holds_the_camera(self):
        def mutate(ir):
            for h in ir["hands"]:
                if h["hand"] == "right" and h["beat"] in ("b2", "b3", "b4"):
                    h["state"] = "camera"
        errs = errors_for(mutate)
        self.assertTrue(any("holds the camera" in e for e in errs), errs)

    def test_stage_listing_fewer_hands_than_required_fails(self):
        def mutate(ir):
            ir["pathways"][0]["stages"][2]["hands"] = [{"actor": "woman", "hand": "left"}]
        errs = errors_for(mutate)
        self.assertTrue(any("needs 2 hand(s), lists 1" in e for e in errs), errs)

    def test_hand_holding_an_unrelated_object_fails(self):
        def mutate(ir):
            for h in ir["hands"]:
                if h["hand"] == "left" and h["beat"] == "b3":
                    h["state"] = "holding:phone"
        errs = errors_for(mutate)
        self.assertTrue(any("holding:phone" in e for e in errs), errs)


class ActionPathways(unittest.TestCase):
    def test_jump_straight_to_open_fails(self):
        def mutate(ir):
            pw = ir["pathways"][0]
            # remove contact and transfer: effect now jumps from sealed to open
            pw["stages"] = [s for s in pw["stages"] if s["kind"] not in ("contact", "transfer")]
            pw["stages"][2]["state_before"] = "sealed_on_table"
            for h in ir["hands"]:
                pass
        errs = errors_for(mutate)
        self.assertTrue(any("magic jump" in e for e in errs), errs)

    def test_effect_without_stated_reaction_fails(self):
        def mutate(ir):
            ir["pathways"][0]["stages"][4]["reaction"] = ""
        errs = errors_for(mutate)
        self.assertTrue(any("no stated reaction" in e for e in errs), errs)

    def test_missing_anticipation_fails(self):
        def mutate(ir):
            pw = ir["pathways"][1]
            pw["stages"] = [s for s in pw["stages"] if s["kind"] != "anticipation"]
        errs = errors_for(mutate)
        self.assertTrue(any("no anticipation stage" in e for e in errs), errs)

    def test_stages_out_of_order_fail(self):
        def mutate(ir):
            pw = ir["pathways"][0]
            pw["stages"][3], pw["stages"][4] = pw["stages"][4], pw["stages"][3]
        errs = errors_for(mutate)
        self.assertTrue(any("out of causal order" in e for e in errs), errs)


class Beats(unittest.TestCase):
    def test_overloaded_beats_fail_with_options(self):
        def mutate(ir):
            for b in ir["beats"]:
                b["min_s"] = 2.0  # 14 s of content in 8 s
        tr = TempRun(mutate)
        try:
            res = director.check(tr.dir)
            self.assertEqual(res.fit["verdict"], "OVERLOADED")
            self.assertIn("options", res.fit)
            self.assertTrue(any("OVERLOADED" in e for e in res.errors))
        finally:
            tr.cleanup()

    def test_unknown_duration_is_underspecified_not_error(self):
        def mutate(ir):
            ir["clip"]["duration_s"] = None
            ir["clip"]["duration_origin"] = "UNKNOWN"
        tr = TempRun(mutate)
        try:
            res = director.check(tr.dir)
            self.assertEqual(res.fit["verdict"], "UNDERSPECIFIED")
            self.assertEqual(res.errors, [])
        finally:
            tr.cleanup()

    def test_reaction_before_cause_fails(self):
        def mutate(ir):
            ir["beats"][2]["caused_by"] = ["b4"]  # twist caused by cap coming free
        errs = errors_for(mutate)
        self.assertTrue(any("cannot precede its cause" in e for e in errs), errs)


class Controls(unittest.TestCase):
    def test_disposition_inconsistent_with_capability_fails(self):
        def mutate(ir):
            ir["controls"][3]["disposition"] = "native"  # semantic capability
        errs = errors_for(mutate)
        self.assertTrue(any("inconsistent with capability" in e for e in errs), errs)

    def test_locked_exact_semantic_request_blocks(self):
        def mutate(ir):
            ir["controls"].append({"id": "c_frame36", "pass": "time", "field": "time.release_frame", "value": 36,
                                   "importance": 0.9, "lock": True, "origin": "USER_EXPLICIT", "treatment": None,
                                   "capability": "semantic", "disposition": "semantic", "exactness": "exact"})
        errs = errors_for(mutate)
        self.assertTrue(any("cannot be enforced by text" in e for e in errs), errs)

    def test_field_written_by_non_owner_fails(self):
        def mutate(ir):
            ir["controls"][3]["pass"] = "style"  # interaction.grip written by style
        errs = errors_for(mutate)
        self.assertTrue(any("one owner per field" in e for e in errs), errs)

    def test_missing_camera_grammar_fails(self):
        def mutate(ir):
            ir["controls"] = [c for c in ir["controls"] if c["pass"] != "camera"]
        errs = errors_for(mutate)
        self.assertTrue(any("camera grammar is mandatory" in e for e in errs), errs)

    def test_style_tier_cannot_write_beats(self):
        def mutate(ir):
            ir["controls"].append({"id": "c_bad", "pass": "style", "field": "beats.order", "value": "x",
                                   "importance": 0.5, "lock": False, "origin": "INFERENCE", "treatment": None,
                                   "capability": "semantic", "disposition": "semantic"})
        errs = errors_for(mutate)
        self.assertTrue(any("order first, texture second" in e for e in errs), errs)


class Emit(unittest.TestCase):
    def test_emit_within_budget_with_complete_receipt(self):
        tr = TempRun()
        try:
            report = director.emit(tr.dir, "seedance")
            prompt = (tr.dir / "prompt.txt").read_text()
            receipt = json.loads((tr.dir / "receipt.json").read_text())
            self.assertLessEqual(report["chars"], report["char_limit"])
            # every prompt line is traced to a source with an origin
            for line in receipt["lines"]:
                srcs = line["source"] if isinstance(line["source"], list) else [line["source"]]
                for s in srcs:
                    self.assertIn("origin", s)
                    self.assertIn(s["kind"], ("entity", "beat", "control"))
            # every emitted sentence appears in the prompt
            for line in receipt["lines"]:
                if line["channel"] == "prompt":
                    self.assertIn(line["text"].split(" ")[0], prompt)
            self.assertTrue((tr.dir / "loss.jsonl").exists())
            # locked content is never dropped
            for cid in report["dropped_for_budget"]:
                ctrl = [c for c in json.loads((tr.dir / "ir.json").read_text())["controls"] if c["id"] == cid][0]
                self.assertFalse(ctrl["lock"])
            # determinism
            report2 = director.emit(tr.dir, "seedance")
            self.assertEqual((tr.dir / "prompt.txt").read_text(), prompt)
            self.assertEqual(report2["chars"], report["chars"])
        finally:
            tr.cleanup()

    def test_emit_is_blocked_when_check_fails(self):
        def mutate(ir):
            ir["pathways"][0]["stages"][4]["reaction"] = ""
        tr = TempRun(mutate)
        try:
            with self.assertRaises(SystemExit):
                director.emit(tr.dir, "seedance")
        finally:
            tr.cleanup()

    def test_budget_compresses_then_drops_lowest_importance_unlocked(self):
        def mutate(ir):
            # inflate an unlocked low-importance control so the budget must act
            for c in ir["controls"]:
                if c["id"] == "c_reaction":
                    c["value"] = "The twist has a visible result. " * 60
        tr = TempRun(mutate)
        try:
            report = director.emit(tr.dir, "seedance")
            self.assertLessEqual(report["chars"], report["char_limit"])
            self.assertTrue(report["compressed_for_budget"], "short wording should be used before anything is dropped")
            self.assertIn("c_reaction", report["dropped_for_budget"])
            losses = [json.loads(l) for l in (tr.dir / "loss.jsonl").read_text().splitlines()]
            self.assertTrue(any(l.get("loss_code") == "token_budget" for l in losses))
        finally:
            tr.cleanup()

    def test_budget_blocks_with_options_when_only_locked_content_remains(self):
        def mutate(ir):
            for b in ir["beats"]:
                b["description"] = b["description"] + " " + ("and more detail " * 40)
                b.pop("short", None)
        tr = TempRun(mutate)
        try:
            with self.assertRaises(SystemExit) as ctx:
                director.emit(tr.dir, "seedance")
            self.assertIn("split into one clip per causal event", str(ctx.exception))
        finally:
            tr.cleanup()


class ReviewRegressions(unittest.TestCase):
    """Holes found by the 2026-10-02 external review (compiler-review.md): each was a green check or a
    successful emit on an invalid or lossy input."""

    def test_native_duration_is_carried_as_text_on_a_route_without_native_fields(self):
        tr = TempRun()
        try:
            report = director.emit(tr.dir, "hailuo")  # hailuo profile has native_fields: []
            prompt = (tr.dir / "prompt.txt").read_text()
            self.assertIn("8-second clip", prompt)
            self.assertEqual(report["settings"], {})
            losses = [json.loads(l) for l in (tr.dir / "loss.jsonl").read_text().splitlines()]
            self.assertTrue(any(l.get("loss_code") == "native_field_unsupported_by_route" and l["canonical_field"] == "clip.duration_s" for l in losses))
            receipt = json.loads((tr.dir / "receipt.json").read_text())
            srcs = [l["source"] for l in receipt["lines"] if isinstance(l["source"], dict)]
            self.assertTrue(any(s.get("id") == "c_duration" and s.get("realization") == "compressed_to_text" for s in srcs))
        finally:
            tr.cleanup()

    def test_locked_native_control_without_text_fallback_blocks(self):
        def mutate(ir):
            ir["controls"].append({"id": "c_seed", "pass": "time", "field": "time.seed", "value": 12345,
                                   "importance": 0.5, "lock": True, "origin": "USER_EXPLICIT", "treatment": None,
                                   "capability": "native", "disposition": "native", "exactness": "exact"})
        tr = TempRun(mutate)
        try:
            with self.assertRaises(SystemExit) as ctx:
                director.emit(tr.dir, "hailuo")
            self.assertIn("no channel", str(ctx.exception))
        finally:
            tr.cleanup()

    def test_same_hand_counted_twice_is_rejected(self):
        def mutate(ir):
            ir["pathways"][0]["stages"][2]["hands"] = [{"actor": "woman", "hand": "left"}, {"actor": "woman", "hand": "left"}]
        errs = errors_for(mutate)
        self.assertTrue(any("listed twice" in e for e in errs), errs)
        self.assertTrue(any("distinct hand" in e for e in errs), errs)

    def test_disconnected_state_chain_is_rejected(self):
        def mutate(ir):
            ir["pathways"][0]["stages"][3]["state_before"] = "sealed_on_table"  # transfer no longer starts where contact ended
        errs = errors_for(mutate)
        self.assertTrue(any("disconnected state chain" in e for e in errs), errs)

    def test_emphasis_lever_applies_for_hailuo_and_core_wording_for_seedance(self):
        def mutate(ir):
            for c in ir["controls"]:
                if c["id"] == "c_register":
                    c["value"]["emphasis"] = ["unforced"]
        tr = TempRun(mutate)
        try:
            director.emit(tr.dir, "hailuo")
            hailuo_prompt = (tr.dir / "prompt.txt").read_text()
            hailuo_receipt = json.loads((tr.dir / "receipt.json").read_text())
            self.assertIn("<i>unforced</i>", hailuo_prompt)
            self.assertTrue(any(isinstance(l["source"], dict) and l["source"].get("lever", {}).get("intent") == "emphasis"
                                for l in hailuo_receipt["lines"]))
            director.emit(tr.dir, "seedance")
            seedance_prompt = (tr.dir / "prompt.txt").read_text()
            self.assertIn("unforced", seedance_prompt)
            self.assertNotIn("<i>", seedance_prompt)
            losses = [json.loads(l) for l in (tr.dir / "loss.jsonl").read_text().splitlines()]
            self.assertTrue(any(l.get("loss_code") == "no_lever_for_intent:emphasis" for l in losses))
        finally:
            tr.cleanup()

    def test_receipt_hash_matches_prompt_file_bytes(self):
        import hashlib
        tr = TempRun()
        try:
            director.emit(tr.dir, "seedance")
            receipt = json.loads((tr.dir / "receipt.json").read_text())
            self.assertEqual(receipt["prompt_sha256"], hashlib.sha256((tr.dir / "prompt.txt").read_bytes()).hexdigest())
        finally:
            tr.cleanup()


class RelativePrompting(unittest.TestCase):
    """WO-01 / R-16, R-59: anchors, deltas, magnitude and vague-word lint."""

    @staticmethod
    def _anchor(ir, beat="b2", quality="speed"):
        ir.setdefault("anchors", []).append({
            "id": "a1", "quality": quality, "beat": beat, "label": "the first reach",
            "description": "She reaches for the bottle at an ordinary, everyday pace"})

    @staticmethod
    def _beat(ir, bid):
        return [b for b in ir["beats"] if b["id"] == bid][0]

    def test_unknown_anchor_reference_fails(self):
        def mutate(ir):
            self._beat(ir, "b5")["relative"] = [{"quality": "speed", "relative_to": "nope", "step": "slightly", "direction": "less"}]
        self.assertTrue(any("unknown anchor" in e for e in errors_for(mutate)))

    def test_anchor_not_earlier_than_delta_fails(self):
        def later(ir):
            self._anchor(ir, beat="b5")
            self._beat(ir, "b2")["relative"] = [{"quality": "speed", "relative_to": "a1", "step": "more", "direction": "more"}]
        self.assertTrue(any("anchor is not earlier" in e for e in errors_for(later)))

        def same(ir):
            self._anchor(ir, beat="b5")
            self._beat(ir, "b5")["relative"] = [{"quality": "speed", "relative_to": "a1", "step": "more", "direction": "more"}]
        self.assertTrue(any("anchor is not earlier" in e for e in errors_for(same)))

    def test_two_deltas_same_quality_on_one_beat_fail(self):
        def mutate(ir):
            self._anchor(ir)
            self._beat(ir, "b5")["relative"] = [
                {"quality": "speed", "relative_to": "a1", "step": "slightly", "direction": "less"},
                {"quality": "speed", "relative_to": "a1", "step": "much", "direction": "more"}]
        self.assertTrue(any("one escalation per quality" in e for e in errors_for(mutate)))

    def test_quality_mismatch_fails(self):
        def mutate(ir):
            self._anchor(ir, quality="speed")
            self._beat(ir, "b5")["relative"] = [{"quality": "weight", "relative_to": "a1", "step": "more", "direction": "more"}]
        self.assertTrue(any("quality mismatch" in e for e in errors_for(mutate)))

    def test_anchor_on_unknown_beat_fails(self):
        def mutate(ir):
            self._anchor(ir, beat="b99")
        self.assertTrue(any("anchor references unknown beat" in e for e in errors_for(mutate)))

    def _check(self, mutate):
        tr = TempRun(mutate)
        try:
            return director.check(tr.dir)
        finally:
            tr.cleanup()

    def test_bare_magnitude_word_warns_but_check_stays_green(self):
        def mutate(ir):
            self._beat(ir, "b3")["description"] += ". She pulls hard"
        res = self._check(mutate)
        self.assertEqual(res.errors, [])
        self.assertTrue(any("bare magnitude word 'hard'" in w for w in res.warnings), res.warnings)

    def test_named_technique_does_not_warn(self):
        def mutate(ir):
            self._beat(ir, "b4")["description"] += ". A hard cut would hide it, and slow motion is not used"
        res = self._check(mutate)
        self.assertFalse(any("bare magnitude word" in w for w in res.warnings), res.warnings)

    def test_comparative_with_than_does_not_warn(self):
        def mutate(ir):
            self._beat(ir, "b5")["description"] += ". Her arm is fast here, more than in the first reach"
        res = self._check(mutate)
        self.assertFalse(any("bare magnitude word" in w for w in res.warnings), res.warnings)

    def test_vague_style_word_warns(self):
        def mutate(ir):
            self._beat(ir, "b1")["description"] += ". It looks cinematic"
        res = self._check(mutate)
        self.assertEqual(res.errors, [])
        self.assertTrue(any("vague style word 'cinematic'" in w for w in res.warnings), res.warnings)

    def test_treatment_wording_is_not_linted(self):
        res = director.check(RUN)  # the capture treatment says "not cinematic"; only IR free text is scanned
        self.assertFalse(any("vague style word" in w or "bare magnitude word" in w for w in res.warnings), res.warnings)

    def test_emit_writes_anchor_once_then_comparison(self):
        def mutate(ir):
            self._anchor(ir)
            self._beat(ir, "b5")["relative"] = [{"quality": "speed", "relative_to": "a1", "step": "slightly", "direction": "less"}]
        tr = TempRun(mutate)
        try:
            director.emit(tr.dir, "seedance")
            prompt = (tr.dir / "prompt.txt").read_text()
            receipt = json.loads((tr.dir / "receipt.json").read_text())
            self.assertEqual(prompt.count("She reaches for the bottle at an ordinary, everyday pace"), 1)
            self.assertIn("slightly slower than the first reach", prompt)
            self.assertLess(prompt.index("ordinary, everyday pace"), prompt.index("slightly slower than the first reach"))
            kinds = [l["source"].get("kind") for l in receipt["lines"] if isinstance(l["source"], dict)]
            self.assertIn("anchor", kinds)
        finally:
            tr.cleanup()


def _event(beat="b4", **over):
    ev = {"event_id": "evt_open", "beat": beat,
          "trigger": {"actor": "woman", "part": "right thumb and index finger", "action": "twist the cap"},
          "contact_surface": "the ridged edge of the cap", "contact_state": "physical_contact_confirmed",
          "primary_reaction": "the cap breaks its seal and turns free",
          "secondary": ["a faint ripple runs through the water"],
          "settle": "the cap rests pinched in her right fingers, the bottle open in her left hand",
          "depends_on": [], "must_not_imply": [], "risk": "high", "origin": "INFERENCE"}
    ev.update(over)
    return ev


class CausalEvents(unittest.TestCase):
    """WO-02 / R-41, R-42, R-44: cause-and-effect records per beat."""

    def test_two_events_on_one_beat_fail(self):
        def mutate(ir):
            ir["physics_events"] = [_event(), _event(event_id="evt_two")]
        self.assertTrue(any("one causal event per beat" in e for e in errors_for(mutate)))

    def test_event_on_unknown_beat_fails(self):
        def mutate(ir):
            ir["physics_events"] = [_event(beat="b99")]
        self.assertTrue(any("event references unknown beat" in e for e in errors_for(mutate)))

    def test_event_depends_on_later_event_fails(self):
        def mutate(ir):
            ir["physics_events"] = [_event(depends_on=["evt_drink"]), _event(event_id="evt_drink", beat="b6")]
        self.assertTrue(any("depends_on" in e for e in errors_for(mutate)))

        def unknown(ir):
            ir["physics_events"] = [_event(depends_on=["nope"])]
        self.assertTrue(any("depends_on" in e for e in errors_for(unknown)))

    def test_force_anchor_must_exist_and_be_earlier(self):
        def missing(ir):
            ir["physics_events"] = [_event(force={"relative_to": "a_none", "step": "more", "direction": "more"})]
        self.assertTrue(any("force anchor" in e for e in errors_for(missing)))

        def later(ir):
            ir["anchors"] = [{"id": "a_w", "quality": "weight", "beat": "b6", "label": "the drink",
                              "description": "She tilts the bottle with an easy, light wrist"}]
            ir["physics_events"] = [_event(force={"relative_to": "a_w", "step": "more", "direction": "more"})]
        self.assertTrue(any("force anchor" in e for e in errors_for(later)))

        def good(ir):
            ir["anchors"] = [{"id": "a_w", "quality": "weight", "beat": "b2", "label": "her first grip",
                              "description": "Her fingers close on the bottle with a light, easy grip"}]
            ir["physics_events"] = [_event(force={"relative_to": "a_w", "step": "slightly", "direction": "more"})]
        self.assertEqual([e for e in errors_for(good) if "force anchor" in e], [])

    def test_empty_reaction_or_settle_fails_edge_admission(self):
        for field in ("primary_reaction", "settle", "contact_surface"):
            def mutate(ir, field=field):
                ir["physics_events"] = [_event(**{field: "  "})]
            self.assertTrue(any("edge admission" in e for e in errors_for(mutate)), field)

    def test_emit_orders_cause_contact_reaction_settle(self):
        def mutate(ir):
            ir["physics_events"] = [_event()]
        tr = TempRun(mutate)
        try:
            director.emit(tr.dir, "seedance")
            prompt = (tr.dir / "prompt.txt").read_text()
            order = [prompt.index("right thumb and index finger twist the cap"),
                     prompt.index("landing on the ridged edge of the cap"),
                     prompt.index("The cap breaks its seal and turns free"),
                     prompt.index("a faint ripple runs through the water"),
                     prompt.index("then the cap rests pinched in her right fingers")]
            self.assertEqual(order, sorted(order))
            receipt = json.loads((tr.dir / "receipt.json").read_text())
            self.assertIn("event", [l["source"].get("kind") for l in receipt["lines"] if isinstance(l["source"], dict)])
        finally:
            tr.cleanup()

    def test_near_contact_changes_landing_wording(self):
        def mutate(ir):
            ir["physics_events"] = [_event(contact_state="near_contact", must_not_imply=["the fingers never touch the cap"])]
        tr = TempRun(mutate)
        try:
            director.emit(tr.dir, "seedance")
            prompt = (tr.dir / "prompt.txt").read_text()
            self.assertIn("passing just short of the ridged edge of the cap", prompt)
            self.assertNotIn("landing on", prompt)
        finally:
            tr.cleanup()

    def test_must_not_imply_is_never_emitted(self):
        def mutate(ir):
            ir["physics_events"] = [_event(must_not_imply=["SECRET_CHECKLIST_LINE the cap is never bitten off"])]
        tr = TempRun(mutate)
        try:
            director.emit(tr.dir, "seedance")
            self.assertNotIn("SECRET_CHECKLIST_LINE", (tr.dir / "prompt.txt").read_text())
        finally:
            tr.cleanup()


class PassCoupling(unittest.TestCase):
    """WO-03 / R-56, R-57: beat-scoped controls and the four coupling checks."""

    @staticmethod
    def _camera(beat, text):
        return {"id": "c_cam_beat", "pass": "camera", "field": "camera.beat_framing", "value": text, "beat": beat,
                "importance": 0.8, "lock": False, "origin": "CREATIVE_CHOICE", "treatment": None,
                "capability": "semantic", "disposition": "semantic"}

    def test_control_on_unknown_beat_fails(self):
        def mutate(ir):
            ir["controls"].append(self._camera("b99", "medium shot"))
        self.assertTrue(any("control on unknown beat" in e for e in errors_for(mutate)))

    def test_camera_close_up_on_hidden_contact_fails(self):
        def mutate(ir):
            ir["physics_events"] = [_event(contact_state="occluded_contact")]
            ir["controls"].append(self._camera("b4", "close-up on the ridged edge of the cap as it turns"))
        self.assertTrue(any("camera shows a hidden contact" in e for e in errors_for(mutate)))

    def test_camera_cutaway_on_confirmed_contact_fails(self):
        def mutate(ir):
            ir["physics_events"] = [_event()]
            ir["controls"].append(self._camera("b4", "cut away to her face, the hands out of frame"))
        self.assertTrue(any("camera hides a confirmed contact" in e for e in errors_for(mutate)))

    def test_beat_too_short_for_its_pathway_stages_fails(self):
        def mutate(ir):
            for b in ir["beats"]:
                if b["id"] == "b6":
                    b["min_s"] = 0.3  # three pathway stages sit on b6
        self.assertTrue(any("beat does not cover its pathway stages" in e for e in errors_for(mutate)))

    def test_event_trigger_needs_actor_and_part(self):
        def mutate(ir):
            ir["physics_events"] = [_event(trigger={"actor": "woman", "part": " ", "action": "twist the cap"})]
        self.assertTrue(any("explicit: trigger needs actor and part" in e for e in errors_for(mutate)))

    def test_passes_yaml_reads_reference_known_ir_areas(self):
        passes = director.load_passes()
        allowed = {"entities", "hands", "pathways", "beats", "anchors", "physics_events", "everything"}
        allowed |= {"controls:%s" % pid for pid in passes}
        with_reads = 0
        for pid, p in passes.items():
            for area in p.get("reads", []):
                self.assertIn(area, allowed, "%s reads unknown area %s" % (pid, area))
            with_reads += 1 if p.get("reads") else 0
        self.assertGreaterEqual(with_reads, 10)
        self.assertEqual(passes["synthesis"]["reads"], ["everything"])


class Scratchpad(unittest.TestCase):
    """WO-03b / R-58, R-60: pass views, per-pass check, open items, saved validation, spacing."""

    def test_pack_returns_reads_locks_treatments_for_pass(self):
        pack = director.pack(RUN, "camera")
        self.assertEqual(pack["pass"]["id"], "camera")
        self.assertIn("beats", pack["reads"])
        self.assertIn("pathways", pack["reads"])
        self.assertTrue(all(c["lock"] for c in pack["locked_controls"]))
        self.assertIn("c_chain", [c["id"] for c in pack["locked_controls"]])
        ids = [t["id"] for t in pack["treatments"]]
        self.assertIn("camera.selfie_framing", ids)
        self.assertIn("camera.move_from_catalog", ids)
        self.assertEqual(pack["open_items"], [])

    def test_pack_camera_includes_move_functions(self):
        pack = director.pack(RUN, "camera")
        self.assertGreaterEqual(len(pack["camera_moves"]), 46)
        self.assertTrue(all("function" in m and "id" in m and "layer" in m for m in pack["camera_moves"]))
        self.assertNotIn("camera_moves", director.pack(RUN, "time"))

    def test_check_pass_limits_rules_and_marks_others_not_applicable(self):
        def mutate(ir):
            ir["controls"] = [c for c in ir["controls"] if c["pass"] != "camera"]  # camera failure
            for h in ir["hands"]:
                if h["hand"] == "right" and h["beat"] == "b3":
                    h["state"] = "camera"                                           # interaction failure
        tr = TempRun(mutate)
        try:
            full = director.check(tr.dir)
            cam = director.check(tr.dir, only_pass="camera")
            self.assertTrue(any("holds the camera" in e for e in full.errors))
            self.assertTrue(cam.errors and all(e.startswith("camera") for e in cam.errors), cam.errors)
            by_group = {o["rule"]: o["outcome"] for o in cam.outcomes}
            self.assertEqual(by_group["camera"], "fail")
            self.assertEqual(by_group["hands"], "not_applicable")
        finally:
            tr.cleanup()

    def test_check_writes_report_and_no_write_suppresses_it(self):
        tr = TempRun()
        try:
            self.assertEqual(director.main(["check", str(tr.dir), "--no-write"]), 0)
            self.assertFalse((tr.dir / "check_report.json").exists())
            self.assertEqual(director.main(["check", str(tr.dir)]), 0)
            report = json.loads((tr.dir / "check_report.json").read_text())
            self.assertTrue(report["ok"])
            self.assertIn("outcomes", report)
            self.assertIn("ir_sha256", report)
        finally:
            tr.cleanup()

    def _open(self, tr, status):
        line = {"id": "o1", "kind": "revision_request", "from_pass": "camera", "to_pass": "time",
                "field": "beats.b4.min_s", "reason": "the cap release needs a longer hold to read", "status": status,
                "resolution": None if status == "open" else "time raised b4 to 0.8 s"}
        (tr.dir / "open.jsonl").write_text(json.dumps(line) + "\n")

    def test_open_revision_request_blocks_emit(self):
        tr = TempRun()
        try:
            self._open(tr, "open")
            with self.assertRaises(SystemExit) as ctx:
                director.emit(tr.dir, "seedance")
            self.assertIn("open items block emit", str(ctx.exception))
            self.assertEqual(len(director.pack(tr.dir, "time")["open_items"]), 1)
        finally:
            tr.cleanup()

    def test_resolved_items_do_not_block_emit(self):
        tr = TempRun()
        try:
            self._open(tr, "resolved")
            director.emit(tr.dir, "seedance")
            self.assertTrue((tr.dir / "prompt.txt").exists())
        finally:
            tr.cleanup()

    def test_constant_motion_warns_when_action_active_and_no_spacing(self):
        def activate(ir):
            for p in ir["pass_plan"]:
                if p["pass"] == "action":
                    p["active"], p["reason"] = True, "a body moves"
        tr = TempRun(activate)
        try:
            self.assertTrue(any("constant motion" in w for w in director.check(tr.dir).warnings))
        finally:
            tr.cleanup()

        def spaced(ir):
            activate(ir)
            ir["beats"][2]["spacing"] = "ease_in"
        tr = TempRun(spaced)
        try:
            self.assertFalse(any("constant motion" in w for w in director.check(tr.dir).warnings))
        finally:
            tr.cleanup()

    def test_spacing_clause_is_emitted(self):
        def mutate(ir):
            ir["beats"][2]["spacing"] = "ease_in"
        tr = TempRun(mutate)
        try:
            director.emit(tr.dir, "seedance")
            self.assertIn("starting slow and accelerating", (tr.dir / "prompt.txt").read_text())
        finally:
            tr.cleanup()


if __name__ == "__main__":
    unittest.main()
