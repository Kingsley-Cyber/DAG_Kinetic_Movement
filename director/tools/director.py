#!/usr/bin/env python3
"""Director tools: `check` validates an IR the LLM wrote; `emit` writes the prompt deterministically.

Code never parses the ask or reasons about the scene. It checks consistency of what the LLM
decided and assembles wording from treatments. Python 3.9, stdlib + pyyaml + jsonschema.

Modules: dircheck.py (validators, loaders, lint) · diremit.py (emitter) · director.py (CLI).
"""
import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from dircheck import CheckResult, check, lint_text, load_ir, load_passes, load_treatments  # noqa: F401  (re-exported)
from diremit import emit, select_lever  # noqa: F401  (re-exported)

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
