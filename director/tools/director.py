#!/usr/bin/env python3
"""Director tools: `check` validates an IR the LLM wrote; `emit` writes the prompt deterministically.

Code never parses the ask or reasons about the scene. It checks consistency of what the LLM
decided and assembles wording from treatments. Python 3.9, stdlib + pyyaml + jsonschema.

Modules: dircheck.py (validators, loaders, lint) · diremit.py (emitter) · director.py (CLI).
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import List, Optional

from dircheck import (  # noqa: F401  (re-exported)
    CheckResult, blocking_open_items, check, lint_text, load_ir, load_open_items, load_passes, load_treatments, pack,
)
from diremit import emit, select_lever  # noqa: F401  (re-exported)

# ----------------------------------------------------------------------------- cli

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="director", description="check an IR; emit a prompt; show a pass its view")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pc = sub.add_parser("check", help="validate a run's ir.json (writes check_report.json)")
    pc.add_argument("run_dir")
    pc.add_argument("--json", action="store_true")
    pc.add_argument("--pass", dest="only_pass", help="per-pass acceptance: only the rules this pass owns")
    pc.add_argument("--no-write", action="store_true", help="do not write check_report.json")
    pe = sub.add_parser("emit", help="emit prompt.txt + receipt + loss records for a model profile")
    pe.add_argument("run_dir")
    pe.add_argument("--model", required=True)
    pe.add_argument("--magnitudes", choices=["relative", "absolute"], default="relative",
                    help="experiment arm (E2): absolute writes bare magnitude words and omits anchor sentences")
    pe.add_argument("--rung", choices=["visible", "term", "numeric"], default="visible",
                    help="experiment arm (E3): wording rung for controls that carry Laban scales")
    pe.add_argument("--out", help="write the outputs into this folder instead of the run folder")
    pp = sub.add_parser("pack", help="print the scratchpad view one pass receives")
    pp.add_argument("run_dir")
    pp.add_argument("pass_id")
    args = ap.parse_args(argv)
    run_dir = Path(args.run_dir).resolve()
    if args.cmd == "check":
        res = check(run_dir, only_pass=args.only_pass)
        if args.only_pass is None and not args.no_write:
            report = {"ok": res.ok(), "errors": res.errors, "warnings": res.warnings, "outcomes": res.outcomes,
                      "fit": res.fit, "ir_sha256": hashlib.sha256((run_dir / "ir.json").read_bytes()).hexdigest()}
            (run_dir / "check_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
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
            scope = " (pass %s)" % args.only_pass if args.only_pass else ""
            print("CHECK %s%s" % ("GREEN" if res.ok() else "RED (%d error%s)" % (len(res.errors), "" if len(res.errors) == 1 else "s"), scope))
        return 0 if res.ok() else 1
    if args.cmd == "emit":
        report = emit(run_dir, args.model, magnitudes=args.magnitudes, rung=args.rung,
                      out_dir=Path(args.out).resolve() if args.out else None)
        print(json.dumps(report, indent=2))
        return 0
    if args.cmd == "pack":
        print(json.dumps(pack(run_dir, args.pass_id), indent=2, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
