#!/usr/bin/env python3
"""Offline structural and semantic validator for the CPCS knowledge-base package."""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date, datetime
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

SOURCE_RE = re.compile(r"^S\d{3}$")
TOPIC_RE = re.compile(r"^T\d{2}$")


def read_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: pathlib.Path) -> list[Any]:
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            raise ValueError(f"{path}:{lineno}: {exc}") from exc
    return rows


def iter_strings(obj: Any):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from iter_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_strings(v)


def add(report: dict, level: str, code: str, path: str, message: str, **details):
    rec = {"level": level, "code": code, "path": path, "message": message}
    if details:
        rec["details"] = details
    report[level + "s"].append(rec)


def validate(root: pathlib.Path, as_of: date) -> dict:
    report = {
        "package_root": str(root),
        "validated_at": datetime.now().astimezone().isoformat(),
        "as_of_date": as_of.isoformat(),
        "errors": [],
        "warnings": [],
        "checks": {},
        "counts": {},
    }

    # Parse every machine-readable artifact.
    parse_counts = {"json": 0, "jsonl": 0, "yaml": 0, "xml": 0, "csv": 0}
    parsed: dict[pathlib.Path, Any] = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = str(path.relative_to(root))
        try:
            if path.suffix == ".json":
                parsed[path] = read_json(path); parse_counts["json"] += 1
            elif path.suffix == ".jsonl":
                parsed[path] = read_jsonl(path); parse_counts["jsonl"] += 1
            elif path.suffix in {".yaml", ".yml"}:
                parsed[path] = yaml.safe_load(path.read_text(encoding="utf-8")); parse_counts["yaml"] += 1
            elif path.suffix == ".xml":
                parsed[path] = ET.parse(path); parse_counts["xml"] += 1
            elif path.suffix == ".csv":
                with path.open(newline="", encoding="utf-8") as handle:
                    parsed[path] = list(csv.DictReader(handle)); parse_counts["csv"] += 1
        except Exception as exc:
            add(report, "error", "PARSE_ERROR", rel, str(exc))
    report["counts"]["parsed_files"] = parse_counts
    report["checks"]["parse_all_machine_readable"] = not any(e["code"] == "PARSE_ERROR" for e in report["errors"])

    # Schema metaschema and registry.
    schema_paths = sorted((root / "03_schemas").glob("*.schema.json"))
    registry = Registry()
    schemas = {}
    for path in schema_paths:
        rel = str(path.relative_to(root))
        try:
            schema = parsed.get(path) or read_json(path)
            Draft202012Validator.check_schema(schema)
            schemas[path.name] = schema
            if schema.get("$id"):
                registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        except Exception as exc:
            add(report, "error", "SCHEMA_INVALID", rel, str(exc))
    report["counts"]["schemas"] = len(schema_paths)
    report["checks"]["schema_metaschema"] = not any(e["code"] == "SCHEMA_INVALID" for e in report["errors"])

    def validate_instance(instance: Any, schema_name: str, rel: str):
        try:
            validator = Draft202012Validator(
                schemas[schema_name], registry=registry, format_checker=FormatChecker()
            )
            for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
                loc = "/".join(map(str, err.absolute_path)) or "<root>"
                add(report, "error", "INSTANCE_SCHEMA", rel, err.message, schema=schema_name, instance_path=loc)
        except Exception as exc:
            add(report, "error", "VALIDATOR_RUNTIME", rel, str(exc), schema=schema_name)

    # Schema validation of canonical examples and adapters.
    examples = sorted((root / "05_examples").glob("*/canonical.json"))
    for path in examples:
        validate_instance(parsed[path], "canonical_scene.schema.json", str(path.relative_to(root)))
    adapters = sorted((root / "12_adapters").glob("*.json"))
    for path in adapters:
        validate_instance(parsed[path], "model_adapter.schema.json", str(path.relative_to(root)))
    report["counts"]["canonical_examples"] = len(examples)
    report["counts"]["model_adapters"] = len(adapters)
    report["checks"]["example_schema_validation"] = not any(e["code"] == "INSTANCE_SCHEMA" and e["path"].startswith("05_examples/") for e in report["errors"])
    report["checks"]["adapter_schema_validation"] = not any(e["code"] == "INSTANCE_SCHEMA" and e["path"].startswith("12_adapters/") for e in report["errors"])

    # Source registry and source reference resolution.
    source_path = root / "06_evidence" / "sources.jsonl"
    sources = parsed.get(source_path, [])
    source_ids = {x.get("id") for x in sources if isinstance(x, dict)}
    duplicates = sorted({x for x in source_ids if sum(1 for r in sources if r.get("id") == x) > 1})
    if duplicates:
        add(report, "error", "DUPLICATE_SOURCE_ID", str(source_path.relative_to(root)), "Duplicate source IDs", ids=duplicates)
    all_refs = set()
    for path, obj in parsed.items():
        if path == source_path:
            continue
        for s in iter_strings(obj):
            if SOURCE_RE.match(s):
                all_refs.add((s, str(path.relative_to(root))))
    unresolved = [(sid, p) for sid, p in sorted(all_refs) if sid not in source_ids]
    for sid, p in unresolved:
        add(report, "error", "UNRESOLVED_SOURCE", p, f"Source ID {sid} does not exist")
    report["counts"]["sources"] = len(sources)
    report["counts"]["unique_source_references"] = len({s for s, _ in all_refs})
    report["checks"]["source_resolution"] = not unresolved and not duplicates

    # Also resolve source IDs embedded in human-readable notes and prompts.
    text_unresolved = []
    text_extensions = {".md", ".txt", ".cypher", ".xml", ".yaml", ".yml", ".csv"}
    for text_path in sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in text_extensions):
        try:
            text = text_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for sid in sorted(set(re.findall(r"\bS\d{3}\b", text))):
            if sid not in source_ids:
                text_unresolved.append((sid, str(text_path.relative_to(root))))
    for sid, p in text_unresolved:
        add(report, "error", "UNRESOLVED_TEXT_SOURCE", p, f"Source ID {sid} does not exist")
    report["counts"]["textual_source_references"] = sum(1 for p in root.rglob("*") if p.is_file() and p.suffix.lower() in text_extensions)
    report["checks"]["textual_source_resolution"] = not text_unresolved

    # Claims and maps.
    claims_path = root / "06_evidence" / "claims.jsonl"
    claims = parsed.get(claims_path, [])
    claim_ids = [c.get("claim_id") for c in claims]
    if len(claim_ids) != len(set(claim_ids)):
        add(report, "error", "DUPLICATE_CLAIM_ID", str(claims_path.relative_to(root)), "Claim IDs must be unique")
    for c in claims:
        for sid in c.get("source_ids", []):
            if sid not in source_ids:
                add(report, "error", "CLAIM_SOURCE_MISSING", str(claims_path.relative_to(root)), f"{c.get('claim_id')} references {sid}")
        conf = c.get("confidence")
        if conf is not None and not 0 <= conf <= 1:
            add(report, "error", "CLAIM_CONFIDENCE_RANGE", str(claims_path.relative_to(root)), f"{c.get('claim_id')} confidence outside [0,1]")
    map_path = root / "06_evidence" / "claim_source_map.jsonl"
    for m in parsed.get(map_path, []):
        if m.get("claim_id") not in set(claim_ids):
            add(report, "error", "CLAIM_MAP_CLAIM_MISSING", str(map_path.relative_to(root)), str(m))
        if m.get("source_id") not in source_ids:
            add(report, "error", "CLAIM_MAP_SOURCE_MISSING", str(map_path.relative_to(root)), str(m))
    report["counts"]["claims"] = len(claims)
    report["checks"]["claim_integrity"] = not any(e["code"].startswith("CLAIM_") or e["code"] == "DUPLICATE_CLAIM_ID" for e in report["errors"])

    # Topic pairing and topic IDs.
    topic_dir = root / "01_topics"
    mds = sorted(topic_dir.glob("[0-9][0-9]_*.md"))
    refs = sorted(topic_dir.glob("[0-9][0-9]_*_reference.json"))
    md_prefix = {p.name[:2] for p in mds}
    ref_prefix = {p.name[:2] for p in refs}
    if md_prefix != ref_prefix or len(md_prefix) != 14:
        add(report, "error", "TOPIC_PAIRING", str(topic_dir.relative_to(root)), "Expected 14 matching Markdown/JSON topic pairs", markdown=sorted(md_prefix), json=sorted(ref_prefix))
    for path in refs:
        d = parsed[path]
        expected = f"T{path.name[:2]}"
        if d.get("topic_id") != expected:
            add(report, "error", "TOPIC_ID_MISMATCH", str(path.relative_to(root)), f"Expected {expected}, found {d.get('topic_id')}")
    report["counts"]["topic_pairs"] = len(md_prefix & ref_prefix)
    report["checks"]["topic_pairing"] = not any(e["code"] in {"TOPIC_PAIRING", "TOPIC_ID_MISMATCH"} for e in report["errors"])

    # Semantic checks for canonical examples.
    for path in examples:
        d = parsed[path]
        rel = str(path.relative_to(root))
        duration = d.get("duration_s", 0)
        actor_ids = {a.get("actor_id") for a in d.get("actors", [])}
        if len(actor_ids) != len(d.get("actors", [])):
            add(report, "error", "DUPLICATE_ACTOR_ID", rel, "Actor IDs must be unique")
        for b in d.get("beats", []):
            a, z = b.get("start_s", 0), b.get("end_s", 0)
            if a > z or a < 0 or z > duration + 1e-9:
                add(report, "error", "BEAT_TIME", rel, f"Invalid beat {b.get('id')}: {a}..{z} in scene {duration}")
        for tr in d.get("affect_tracks", []):
            if tr.get("actor_id") not in actor_ids:
                add(report, "error", "AFFECT_ACTOR", rel, f"Unknown actor {tr.get('actor_id')}")
            times = [k.get("time_s", 0) for k in tr.get("keyframes", [])]
            if times != sorted(times) or any(t < 0 or t > duration + 1e-9 for t in times):
                add(report, "error", "AFFECT_TIME", rel, f"Invalid affect keyframe order/range in {tr.get('track_id')}")
        timelines = {x.get("timeline_id"): x for x in d.get("phase_timelines", [])}
        for tl in timelines.values():
            last = -1.0
            local_duration = tl.get("duration_s", 0)
            for ph in tl.get("phases", []):
                a, z = ph.get("t_start_s", 0), ph.get("t_end_s", 0)
                if a > z or a < -1e-9 or z > local_duration + 1e-9:
                    add(report, "error", "PHASE_TIME", rel, f"Invalid {tl.get('timeline_id')}/{ph.get('phase_id')}: {a}..{z} of {local_duration}")
                if a < last - 1e-9:
                    add(report, "error", "PHASE_ORDER", rel, f"Overlap/reversal in {tl.get('timeline_id')} at {ph.get('phase_id')}")
                last = max(last, z)
        for mp in d.get("motion_primitives", []):
            if mp.get("actor_id") not in actor_ids:
                add(report, "error", "PRIMITIVE_ACTOR", rel, f"Unknown actor {mp.get('actor_id')}")
            if mp.get("phase_timeline_id") and mp.get("phase_timeline_id") not in timelines:
                add(report, "error", "PRIMITIVE_TIMELINE", rel, f"Unknown timeline {mp.get('phase_timeline_id')}")
        for ft in d.get("facs_tracks", []):
            if ft.get("actor_id") not in actor_ids:
                add(report, "error", "FACS_ACTOR", rel, f"Unknown actor {ft.get('actor_id')}")
            for ev in ft.get("events", []):
                ts = [ev.get("t_onset_start_s", 0), ev.get("t_apex_start_s", 0), ev.get("t_apex_end_s", 0), ev.get("t_offset_end_s", 0)]
                if ts != sorted(ts) or ts[0] < 0 or ts[-1] > duration + 1e-9:
                    add(report, "error", "FACS_TIME", rel, f"Invalid FACS timing AU {ev.get('au_code')}: {ts}")
        for it in d.get("interactions", []):
            a, z = it.get("t_start_s", 0), it.get("t_end_s", 0)
            if a > z or a < 0 or z > duration + 1e-9:
                add(report, "error", "INTERACTION_TIME", rel, f"Invalid interaction {it.get('interaction_id')}: {a}..{z}")
            agent = str(it.get("agent_id", "")).split('.')[0]
            patient = str(it.get("patient_id", "")).split('.')[0]
            if agent not in actor_ids:
                add(report, "error", "INTERACTION_AGENT", rel, f"Unknown agent {it.get('agent_id')}")
            # Patient may be actor part, object, environment, or product; warn only if it looks like a missing actor identifier.
            if patient and patient.startswith(("fighter_", "actor_", "giver", "receiver")) and patient not in actor_ids:
                add(report, "warning", "INTERACTION_PATIENT_UNRESOLVED", rel, f"Patient {it.get('patient_id')} is not a declared actor/object")
        for cam in d.get("camera_tracks", []):
            a, z = cam.get("t_start_s", 0), cam.get("t_end_s", 0)
            if a > z or a < 0 or z > duration + 1e-9:
                add(report, "error", "CAMERA_TIME", rel, f"Invalid camera track {cam.get('track_id')}: {a}..{z}")
            for m in cam.get("motion_primitives", []):
                ma, mz = m.get("t_start_s", 0), m.get("t_end_s", 0)
                if ma > mz or ma < a - 1e-9 or mz > z + 1e-9:
                    add(report, "error", "CAMERA_MOTION_TIME", rel, f"Invalid camera primitive {m.get('type')}: {ma}..{mz}")
    semantic_codes = {"DUPLICATE_ACTOR_ID","BEAT_TIME","AFFECT_ACTOR","AFFECT_TIME","PHASE_TIME","PHASE_ORDER","PRIMITIVE_ACTOR","PRIMITIVE_TIMELINE","FACS_ACTOR","FACS_TIME","INTERACTION_TIME","INTERACTION_AGENT","CAMERA_TIME","CAMERA_MOTION_TIME"}
    report["checks"]["example_semantics"] = not any(e["code"] in semantic_codes for e in report["errors"])

    # Adapter date and status checks.
    for path in adapters:
        d = parsed[path]; rel = str(path.relative_to(root))
        try:
            verified = date.fromisoformat(d["verified_at"])
            age = (as_of - verified).days
            ttl = int(d.get("ttl_days", 30))
            if age < 0:
                add(report, "error", "ADAPTER_FUTURE_DATE", rel, f"Verified date {verified} is after as-of {as_of}")
            elif age > ttl:
                add(report, "warning", "ADAPTER_STALE", rel, f"Snapshot is {age} days old, exceeding TTL {ttl}")
        except Exception as exc:
            add(report, "error", "ADAPTER_DATE", rel, str(exc))
        if d.get("status") == "legacy_deprecating" and not d.get("unsupported"):
            add(report, "warning", "LEGACY_WITHOUT_BLOCK", rel, "Legacy adapter should state unsupported/new-dependency policy")
    report["checks"]["adapter_freshness"] = not any(e["code"] in {"ADAPTER_FUTURE_DATE","ADAPTER_DATE"} for e in report["errors"])

    # Graph integrity.
    ent_path = root / "11_graph_seed" / "entities.jsonl"
    rel_path = root / "11_graph_seed" / "relations.jsonl"
    entities = parsed.get(ent_path, [])
    relations = parsed.get(rel_path, [])
    eids = [e.get("entity_id") for e in entities]
    if len(eids) != len(set(eids)):
        add(report, "error", "DUPLICATE_ENTITY", str(ent_path.relative_to(root)), "Entity IDs must be unique")
    eset = set(eids)
    rids = [r.get("relation_id") for r in relations]
    if len(rids) != len(set(rids)):
        add(report, "error", "DUPLICATE_RELATION", str(rel_path.relative_to(root)), "Relation IDs must be unique")
    for r in relations:
        if r.get("source") not in eset:
            add(report, "error", "GRAPH_SOURCE_MISSING", str(rel_path.relative_to(root)), str(r))
        if r.get("target") not in eset:
            add(report, "error", "GRAPH_TARGET_MISSING", str(rel_path.relative_to(root)), str(r))
    report["counts"]["graph_entities"] = len(entities)
    report["counts"]["graph_relations"] = len(relations)
    report["checks"]["graph_integrity"] = not any(e["code"].startswith("GRAPH_") or e["code"].startswith("DUPLICATE_ENTITY") or e["code"].startswith("DUPLICATE_RELATION") for e in report["errors"])

    # XML roots and YAML intents.
    for p in sorted((root / "05_examples").glob("*/beats.xml")):
        tree = parsed[p]
        if tree.getroot().tag not in {"bml", "cpcsBeats", "timeline", "scene", "cpcs-sequence"}:
            add(report, "warning", "XML_ROOT", str(p.relative_to(root)), f"Unexpected root tag {tree.getroot().tag}")
    for p in sorted((root / "05_examples").glob("*/intent.yaml")):
        y = parsed[p]
        if not isinstance(y, dict) or not (y.get("intent") or y.get("primary_intent")):
            add(report, "error", "YAML_INTENT", str(p.relative_to(root)), "Expected top-level intent")
    report["checks"]["example_sidecars"] = not any(e["code"] == "YAML_INTENT" for e in report["errors"])

    # Required root structure and nonempty Markdown.
    required_dirs = ["00_scope","01_topics","02_canonical_model","03_schemas","04_pipeline","05_examples","06_evidence","07_prompts","08_evaluation","09_source_notes","10_scripts","11_graph_seed","12_adapters"]
    for name in required_dirs:
        p = root / name
        if not p.is_dir():
            add(report, "error", "REQUIRED_DIR", name, "Required directory missing")
    empty_md = [str(p.relative_to(root)) for p in root.rglob("*.md") if not p.read_text(encoding="utf-8").strip()]
    for p in empty_md:
        add(report, "error", "EMPTY_MARKDOWN", p, "Markdown file is empty")
    report["checks"]["repository_structure"] = not any(e["code"] in {"REQUIRED_DIR","EMPTY_MARKDOWN"} for e in report["errors"])

    report["summary"] = {
        "passed": len(report["errors"]) == 0,
        "error_count": len(report["errors"]),
        "warning_count": len(report["warnings"]),
        "check_count": len(report["checks"]),
        "checks_passed": sum(bool(v) for v in report["checks"].values()),
    }
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    ap.add_argument("--as-of", default="2026-07-31")
    ap.add_argument("--output", type=pathlib.Path)
    args = ap.parse_args()
    report = validate(args.root.resolve(), date.fromisoformat(args.as_of))
    out = args.output or args.root / "validation_report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"Report: {out}")
    return 0 if report["summary"]["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
