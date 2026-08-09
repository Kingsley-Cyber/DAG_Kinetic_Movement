#!/usr/bin/env python3
"""Validate the CPCS ADRG research package and optionally refresh manifests."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper" / "CPCS_Adaptive_Director_Reasoning_Graph_and_Polyglot_Prompt_Compiler.md"
RAG = ROOT / "rag" / "CPCS_ADRG_RAG_Corpus.jsonl"
RAG_SCHEMA = ROOT / "schemas" / "CPCS_ADRG_RAG_Record_Schema.json"
GRAPH_SCHEMA = ROOT / "schemas" / "CPCS_ADRG_Reasoning_Graph_Schema.json"
SOURCE_SCHEMA = ROOT / "schemas" / "CPCS_ADRG_Source_Index_Schema.json"
SOURCES = ROOT / "references" / "ADRG_Reference_Index.json"
GRAPH_EXAMPLE = ROOT / "examples" / "canonical_reasoning_graph.json"
CONCEPTS = ROOT / "integration" / "concept_cards.proposed.jsonl"
PACKAGE_MANIFEST = ROOT / "manifests" / "package_manifest.json"
CHECKSUMS = ROOT / "SHA256SUMS.txt"

MARKER_RE = re.compile(r'<!--\s*RAG_CHUNK\s+id="([^"]+)"\s+title="([^"]+)"\s+concepts="([^"]*)"\s*-->')
SOURCE_RE = re.compile(r"\[(S\d{3})\]")
FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader: UniqueKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"Duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping,
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema(instance: Any, schema_path: Path, label: str) -> list[str]:
    schema = load_json(schema_path)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
        p = "/".join(str(x) for x in error.absolute_path)
        errors.append(f"{label} {p}: {error.message}")
    return errors


def validate_paper() -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    raw = PAPER.read_text(encoding="utf-8")
    front = FRONT_RE.search(raw)
    if not front:
        return ["paper: missing YAML front matter"], {}
    try:
        metadata = yaml.load(front.group(1), Loader=UniqueKeyLoader) or {}
    except Exception as exc:
        return [f"paper front matter: {exc}"], {}

    for field in ["document_id", "version", "date", "literature_cutoff", "rag_ready"]:
        if field not in metadata:
            errors.append(f"paper front matter: missing {field}")
    if metadata.get("rag_ready") is not True:
        errors.append("paper front matter: rag_ready must be true")

    markers = MARKER_RE.findall(raw)
    marker_ids = [m[0] for m in markers]
    duplicates = [x for x, n in Counter(marker_ids).items() if n > 1]
    if duplicates:
        errors.append(f"paper: duplicate RAG marker IDs: {duplicates}")
    if len(marker_ids) < 20:
        errors.append(f"paper: expected at least 20 RAG markers, found {len(marker_ids)}")
    if "RAG_DOC_SUMMARY" not in raw:
        errors.append("paper: missing RAG_DOC_SUMMARY")

    source_index = {s["source_id"] for s in load_json(SOURCES)}
    paper_source_ids = set(SOURCE_RE.findall(raw))
    missing = sorted(paper_source_ids - source_index)
    if missing:
        errors.append(f"paper: unresolved source IDs: {missing}")
    return errors, metadata


def validate_sources() -> list[str]:
    errors: list[str] = []
    sources = load_json(SOURCES)
    errors.extend(validate_schema(sources, SOURCE_SCHEMA, "source index"))
    ids = [s.get("source_id") for s in sources]
    duplicates = [x for x, n in Counter(ids).items() if n > 1]
    if duplicates:
        errors.append(f"source index: duplicate IDs: {duplicates}")
    return errors


def validate_examples() -> list[str]:
    errors: list[str] = []
    for name in ["reasoning_policy.yaml", "director_request.yaml"]:
        path = ROOT / "examples" / name
        try:
            yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
        except Exception as exc:
            errors.append(f"{rel(path)}: {exc}")
    try:
        ET.parse(ROOT / "examples" / "director_envelope.xml")
    except Exception as exc:
        errors.append(f"examples/director_envelope.xml: {exc}")

    try:
        graph = load_json(GRAPH_EXAMPLE)
    except Exception as exc:
        return errors + [f"examples/canonical_reasoning_graph.json: {exc}"]
    errors.extend(validate_schema(graph, GRAPH_SCHEMA, "reasoning graph"))
    errors.extend(validate_graph_semantics(graph))
    return errors


def validate_graph_semantics(graph: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = [n.get("id") for n in nodes]
    node_set = set(node_ids)
    duplicates = [x for x, n in Counter(node_ids).items() if n > 1]
    if duplicates:
        errors.append(f"reasoning graph: duplicate node IDs: {duplicates}")
    edge_ids = [e.get("id") for e in edges]
    duplicates = [x for x, n in Counter(edge_ids).items() if n > 1]
    if duplicates:
        errors.append(f"reasoning graph: duplicate edge IDs: {duplicates}")

    decision_node_ids = {n["id"] for n in nodes if n.get("type") == "decision"}
    decision_record_ids = {d["decision_id"] for d in graph.get("decisions", [])}
    for edge in edges:
        if edge.get("from") not in node_set:
            errors.append(f"reasoning graph edge {edge.get('id')}: missing from node {edge.get('from')}")
        if edge.get("to") not in node_set:
            errors.append(f"reasoning graph edge {edge.get('id')}: missing to node {edge.get('to')}")
        if edge.get("type") == "selected_over":
            did = edge.get("decision_id")
            if did not in decision_node_ids or did not in decision_record_ids:
                errors.append(f"reasoning graph edge {edge.get('id')}: unresolved decision_id {did}")

    for decision in graph.get("decisions", []):
        if decision.get("selected") not in decision.get("alternatives", []):
            errors.append(f"decision {decision.get('decision_id')}: selected value is not in alternatives")

    # Detect cycles in strict depends_on edges using Kahn's algorithm.
    adjacency: dict[str, list[str]] = defaultdict(list)
    indegree: dict[str, int] = {nid: 0 for nid in node_set}
    for edge in edges:
        if edge.get("type") == "depends_on":
            src, dst = edge["from"], edge["to"]
            adjacency[src].append(dst)
            indegree[dst] += 1
    queue = deque([nid for nid, degree in indegree.items() if degree == 0])
    visited = 0
    while queue:
        nid = queue.popleft()
        visited += 1
        for nxt in adjacency[nid]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    if visited != len(node_set):
        errors.append("reasoning graph: depends_on subgraph contains a cycle")
    return errors


def validate_rag() -> list[str]:
    errors: list[str] = []
    if not RAG.exists():
        return ["RAG corpus is missing; run scripts/build_adrg_rag.py"]
    schema = load_json(RAG_SCHEMA)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    source_ids = {s["source_id"] for s in load_json(SOURCES)}
    records: list[dict[str, Any]] = []
    for line_no, line in enumerate(RAG.read_text(encoding="utf-8").splitlines(), 1):
        try:
            record = json.loads(line)
        except Exception as exc:
            errors.append(f"RAG line {line_no}: invalid JSON: {exc}")
            continue
        records.append(record)
        for error in validator.iter_errors(record):
            p = "/".join(str(x) for x in error.absolute_path)
            errors.append(f"RAG {record.get('record_id', line_no)} {p}: {error.message}")
        missing = sorted(set(record.get("source_ids", [])) - source_ids)
        if missing:
            errors.append(f"RAG {record.get('record_id')}: unresolved source IDs {missing}")
        if record.get("record_type") == "paper_chunk" and record.get("estimated_tokens", 0) > 950:
            errors.append(f"RAG {record.get('record_id')}: exceeds 950 estimated tokens")

    ids = [r.get("record_id") for r in records]
    duplicates = [x for x, n in Counter(ids).items() if n > 1]
    if duplicates:
        errors.append(f"RAG: duplicate record IDs: {duplicates}")
    counts = Counter(r.get("record_type") for r in records)
    if counts["document"] != 1:
        errors.append(f"RAG: expected 1 document record, found {counts['document']}")
    if counts["paper_chunk"] < 20:
        errors.append(f"RAG: expected at least 20 paper chunks, found {counts['paper_chunk']}")
    if counts["source"] != len(source_ids):
        errors.append(f"RAG: expected {len(source_ids)} source records, found {counts['source']}")
    return errors


def validate_concepts() -> list[str]:
    errors: list[str] = []
    required = {"id", "kind", "name", "what", "use_when", "nl_triggers", "pairs_with", "conflicts", "status", "evidence", "source", "layer"}
    cards: list[dict[str, Any]] = []
    for line_no, line in enumerate(CONCEPTS.read_text(encoding="utf-8").splitlines(), 1):
        try:
            card = json.loads(line)
        except Exception as exc:
            errors.append(f"concept line {line_no}: invalid JSON: {exc}")
            continue
        cards.append(card)
        missing = sorted(required - set(card))
        if missing:
            errors.append(f"concept {card.get('id', line_no)}: missing fields {missing}")
        if not str(card.get("id", "")).startswith("c_"):
            errors.append(f"concept line {line_no}: ID must start c_")
        if len(card.get("nl_triggers", [])) < 3:
            errors.append(f"concept {card.get('id')}: fewer than 3 nl_triggers")
        if card.get("status") != "unexplored":
            errors.append(f"concept {card.get('id')}: proposed cards must start unexplored")
    ids = [c.get("id") for c in cards]
    duplicates = [x for x, n in Counter(ids).items() if n > 1]
    if duplicates:
        errors.append(f"concept cards: duplicate IDs: {duplicates}")
    return errors


def content_files_for_manifest() -> list[Path]:
    excluded = {PACKAGE_MANIFEST.resolve(), CHECKSUMS.resolve()}
    return sorted(
        [p for p in ROOT.rglob("*") if p.is_file() and p.resolve() not in excluded],
        key=lambda p: rel(p),
    )


def refresh_package_manifest() -> None:
    files = content_files_for_manifest()
    entries = [{"path": rel(p), "sha256": sha256_file(p), "bytes": p.stat().st_size} for p in files]
    manifest = {
        "manifest_version": "1.0",
        "package_id": "CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0",
        "document_id": "CPCS-ADRG-RP-2026-01",
        "version": "1.0",
        "date": "2026-07-23",
        "file_count": len(entries),
        "files": entries,
    }
    PACKAGE_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    PACKAGE_MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def refresh_checksums() -> None:
    files = sorted([p for p in ROOT.rglob("*") if p.is_file() and p.resolve() != CHECKSUMS.resolve()], key=lambda p: rel(p))
    text = "".join(f"{sha256_file(p)}  {rel(p)}\n" for p in files)
    CHECKSUMS.write_text(text, encoding="utf-8")


def validate_manifest_and_checksums() -> list[str]:
    errors: list[str] = []
    if not PACKAGE_MANIFEST.exists():
        errors.append("package manifest missing")
    else:
        manifest = load_json(PACKAGE_MANIFEST)
        expected = {entry["path"]: entry for entry in manifest.get("files", [])}
        actual_files = content_files_for_manifest()
        actual_paths = {rel(p) for p in actual_files}
        if set(expected) != actual_paths:
            errors.append("package manifest file set does not match package contents")
        for path in actual_files:
            entry = expected.get(rel(path))
            if entry and entry.get("sha256") != sha256_file(path):
                errors.append(f"package manifest hash mismatch: {rel(path)}")
            if entry and entry.get("bytes") != path.stat().st_size:
                errors.append(f"package manifest size mismatch: {rel(path)}")

    if not CHECKSUMS.exists():
        errors.append("SHA256SUMS.txt missing")
    else:
        entries: dict[str, str] = {}
        for line_no, line in enumerate(CHECKSUMS.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                digest, path = line.split("  ", 1)
            except ValueError:
                errors.append(f"SHA256SUMS line {line_no}: invalid format")
                continue
            entries[path] = digest
        expected_files = sorted([p for p in ROOT.rglob("*") if p.is_file() and p.resolve() != CHECKSUMS.resolve()], key=lambda p: rel(p))
        if set(entries) != {rel(p) for p in expected_files}:
            errors.append("SHA256SUMS file set does not match package contents")
        for path in expected_files:
            if entries.get(rel(path)) != sha256_file(path):
                errors.append(f"SHA256SUMS mismatch: {rel(path)}")
    return errors


def rebuild_rag() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_adrg_rag.py")], check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="Rebuild RAG and refresh manifests/checksums before validation")
    args = parser.parse_args()

    if args.refresh:
        rebuild_rag()
        refresh_package_manifest()
        refresh_checksums()

    checks = [
        ("paper", validate_paper()[0]),
        ("sources", validate_sources()),
        ("examples", validate_examples()),
        ("rag", validate_rag()),
        ("concepts", validate_concepts()),
        ("manifest", validate_manifest_and_checksums()),
    ]
    errors = [(name, err) for name, errs in checks for err in errs]
    if errors:
        print("PACKAGE VALIDATION: FAIL")
        for name, error in errors:
            print(f"- [{name}] {error}")
        return 1

    print("PACKAGE VALIDATION: PASS")
    for name, _ in checks:
        print(f"- {name}: ok")
    print(f"- package files: {sum(1 for p in ROOT.rglob('*') if p.is_file())}")
    print(f"- rag records: {sum(1 for _ in RAG.open(encoding='utf-8'))}")
    print(f"- proposed concepts: {sum(1 for _ in CONCEPTS.open(encoding='utf-8'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
