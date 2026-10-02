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


if __name__ == "__main__":
    unittest.main()
