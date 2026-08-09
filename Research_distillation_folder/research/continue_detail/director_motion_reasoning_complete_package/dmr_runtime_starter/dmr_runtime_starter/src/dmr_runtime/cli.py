from __future__ import annotations

import argparse
import json
from pathlib import Path

from .capabilities import load_contract
from .compiler import CompileOptions, CompilationError, compile_scene
from .models import ScenePlan
from .temporal import STNSolver
from .validation import validate_scene


def _load_scene(path: Path) -> ScenePlan:
    return ScenePlan.model_validate(json.loads(path.read_text(encoding="utf-8")))


def main() -> int:
    parser = argparse.ArgumentParser(prog="dmr-runtime")
    sub = parser.add_subparsers(dest="cmd", required=True)
    solve = sub.add_parser("solve")
    solve.add_argument("scene", type=Path)
    validate = sub.add_parser("validate")
    validate.add_argument("scene", type=Path)
    compile_cmd = sub.add_parser("compile")
    compile_cmd.add_argument("scene", type=Path)
    compile_cmd.add_argument("contract", type=Path)
    compile_cmd.add_argument("--allow-required-loss", action="store_true")
    compile_cmd.add_argument("--output", type=Path)
    args = parser.parse_args()

    scene = _load_scene(args.scene)
    temporal = STNSolver(scene.temporal_constraints, origin=scene.origin_point).solve()
    if args.cmd == "solve":
        print(json.dumps({
            "consistent": temporal.consistent,
            "schedule_s": temporal.schedule_s,
            "earliest_s": temporal.earliest_s,
            "latest_s": temporal.latest_s,
            "underconstrained_points": temporal.underconstrained_points,
            "conflict": temporal.conflict.__dict__ if temporal.conflict else None,
        }, indent=2))
        return 0 if temporal.consistent else 2
    if args.cmd == "validate":
        issues = validate_scene(scene, temporal)
        print(json.dumps([i.model_dump(mode="json") for i in issues], indent=2))
        return 2 if any(i.severity.value == "error" for i in issues) else 0

    contract = load_contract(args.contract)
    try:
        result = compile_scene(
            scene,
            contract,
            options=CompileOptions(allow_required_loss=args.allow_required_loss),
        )
    except CompilationError as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, indent=2))
        return 3
    text = result.model_dump_json(indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 2 if result.hard_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
