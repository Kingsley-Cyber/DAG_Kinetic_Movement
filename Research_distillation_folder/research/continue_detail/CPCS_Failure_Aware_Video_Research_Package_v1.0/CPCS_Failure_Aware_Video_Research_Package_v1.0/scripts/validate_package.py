#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_jsonl(path: Path):
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path}:{lineno}: {exc}") from exc
    return rows


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    checks = []

    required = [
        "README.md", "FAILURE_TAXONOMY.md", "FAILURE_CAUSE_MODEL.md",
        "OCCLUSION_AND_HIDDEN_STATE_FAILURES.md",
        "IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md",
        "SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md",
        "TEMPORAL_ACTION_CAUSALITY_FAILURES.md",
        "CONTACT_BALANCE_AND_PHYSICS_FAILURES.md",
        "FLUID_MATERIAL_AND_VFX_FAILURES.md",
        "CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md",
        "PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md",
        "AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md", "MITIGATION_HIERARCHY.md",
        "PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv", "FAILURE_MITIGATION_MATRIX.csv",
        "SOURCE_CATALOG.csv", "CLAIM_SOURCE_MATRIX.csv", "FAILURE_RECORDS.jsonl",
        "FAILURE_RECORD.schema.json", "EVALUATION_METRICS.schema.json", "EVALUATION_METRICS.jsonl",
        "MINIMUM_SUFFICIENT_REPRESENTATION.md", "FINAL_RESEARCH_ANSWER.md",
        "EMPIRICAL_EXECUTION_STATUS.md", "REPOSITORY_AUDIT.md",
        "EXPERIMENT_AND_ABLATION_PLAN.md", "PROMPT_COMPILER_RULES.md",
        "SHOT_DECOMPOSITION_RULES.md", "LOCALIZED_REPAIR_PLAYBOOK.md",
        "CPCS_INTEGRATION_RECOMMENDATIONS.md", "UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL.md"
    ]
    missing = [p for p in required if not (root / p).is_file()]
    if missing:
        raise RuntimeError(f"Missing required outputs: {missing}")
    checks.append({"check": "required_outputs", "status": "passed", "count": len(required)})

    source_rows = list(csv.DictReader((root / "SOURCE_CATALOG.csv").open(encoding="utf-8")))
    source_ids = {r["source_id"] for r in source_rows}
    if len(source_ids) != len(source_rows):
        raise RuntimeError("Duplicate source IDs")

    failure_schema = json.loads((root / "FAILURE_RECORD.schema.json").read_text(encoding="utf-8"))
    metric_schema = json.loads((root / "EVALUATION_METRICS.schema.json").read_text(encoding="utf-8"))
    experiment_schema = json.loads((root / "schemas/EXPERIMENT_PLAN.schema.json").read_text(encoding="utf-8"))
    for schema in [failure_schema, metric_schema, experiment_schema]:
        Draft202012Validator.check_schema(schema)

    failures = load_jsonl(root / "FAILURE_RECORDS.jsonl")
    fv = Draft202012Validator(failure_schema)
    failure_ids = set()
    ordinals = set()
    for row in failures:
        errors = sorted(fv.iter_errors(row), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Failure record invalid {row.get('failure_id')}: {errors[0].message}")
        if row["failure_id"] in failure_ids:
            raise RuntimeError(f"Duplicate failure ID {row['failure_id']}")
        if row["ordinal"] in ordinals:
            raise RuntimeError(f"Duplicate failure ordinal {row['ordinal']}")
        failure_ids.add(row["failure_id"])
        ordinals.add(row["ordinal"])
        missing_refs = sorted(set(row["source_refs"]) - source_ids)
        if missing_refs:
            raise RuntimeError(f"Unknown source refs in {row['failure_id']}: {missing_refs}")
    checks.append({"check": "failure_records", "status": "passed", "count": len(failures)})

    metrics = load_jsonl(root / "EVALUATION_METRICS.jsonl")
    mv = Draft202012Validator(metric_schema)
    metric_ids = set()
    for row in metrics:
        errors = sorted(mv.iter_errors(row), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Metric invalid {row.get('metric_id')}: {errors[0].message}")
        if row["metric_id"] in metric_ids:
            raise RuntimeError(f"Duplicate metric ID {row['metric_id']}")
        metric_ids.add(row["metric_id"])
    referenced_metrics = {m for f in failures for m in f["verification_metrics"]}
    if referenced_metrics - metric_ids:
        raise RuntimeError(f"Missing metric definitions: {sorted(referenced_metrics - metric_ids)}")
    checks.append({"check": "evaluation_metrics", "status": "passed", "count": len(metrics)})

    ev = Draft202012Validator(experiment_schema)
    experiment_count = 0
    for path in sorted((root / "experiments").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(ev.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Experiment invalid {path.name}: {errors[0].message}")
        unknown_metrics = set(data["metrics"]) - metric_ids
        if unknown_metrics:
            raise RuntimeError(f"Experiment {path.name} references unknown metrics: {sorted(unknown_metrics)}")
        experiment_count += 1
    checks.append({"check": "experiment_plans", "status": "passed", "count": experiment_count})

    contract_pairs = [
        ("schemas/OCCLUSION_CONTINUITY_CONTRACT.schema.json", "examples/occlusion_continuity_water_splash.json"),
        ("schemas/STATE_LEDGER.schema.json", "examples/state_ledger_two_actor_water_scene.json"),
        ("schemas/CAUSAL_EVENT_GRAPH.schema.json", "examples/causal_event_graph_water_strike.json"),
        ("schemas/SPATIAL_STATE_TRANSITION.schema.json", "examples/spatial_state_transition_water_scene.json"),
        ("schemas/EVALUATOR_PROVENANCE.schema.json", "examples/evaluator_provenance_identity_check.json"),
    ]
    for schema_rel, example_rel in contract_pairs:
        schema = json.loads((root / schema_rel).read_text(encoding="utf-8"))
        example = json.loads((root / example_rel).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema).iter_errors(example), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Example invalid {example_rel}: {errors[0].message}")
    checks.append({"check": "contract_examples", "status": "passed", "count": len(contract_pairs)})

    provider_rows = list(csv.DictReader((root / "PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv").open(encoding="utf-8")))
    for row in provider_rows:
        refs = set(row["official_source_ids"].split())
        if refs - source_ids:
            raise RuntimeError(f"Provider row {row['model_or_endpoint_id']} has unknown sources {sorted(refs - source_ids)}")
    claim_rows = list(csv.DictReader((root / "CLAIM_SOURCE_MATRIX.csv").open(encoding="utf-8")))
    for row in claim_rows:
        if row["source_id"] not in source_ids:
            raise RuntimeError(f"Claim row {row['claim_id']} has unknown source {row['source_id']}")
    checks.append({"check": "source_traceability", "status": "passed", "sources": len(source_rows), "providers": len(provider_rows), "claim_source_edges": len(claim_rows)})

    manifest_path = root / "MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for item in manifest["files"]:
            path = root / item["path"]
            if not path.is_file():
                raise RuntimeError(f"Manifest file missing: {item['path']}")
            if path.stat().st_size != item["bytes"]:
                raise RuntimeError(f"Manifest byte size mismatch: {item['path']}")
            if sha256(path) != item["sha256"]:
                raise RuntimeError(f"Manifest hash mismatch: {item['path']}")
        checks.append({"check": "manifest", "status": "passed", "count": len(manifest["files"])})

    sums_path = root / "SHA256SUMS.txt"
    if sums_path.exists():
        count = 0
        for line in sums_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, rel = line.split("  ", 1)
            path = root / rel
            if sha256(path) != digest:
                raise RuntimeError(f"SHA256SUMS mismatch: {rel}")
            count += 1
        checks.append({"check": "sha256sums", "status": "passed", "count": count})

    report = {"status": "passed", "root": str(root), "checks": checks}
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
