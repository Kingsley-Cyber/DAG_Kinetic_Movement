#!/usr/bin/env python3
"""Build the CPCS ADRG RAG corpus deterministically from the Markdown paper.

The builder is marker-aware, heading-aware, and conservative about code blocks and
Markdown tables. It emits one document record, one or more records per RAG marker,
and one record per structured source in the reference index.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import jsonschema
import yaml

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAPER = PACKAGE_ROOT / "paper" / "CPCS_Adaptive_Director_Reasoning_Graph_and_Polyglot_Prompt_Compiler.md"
DEFAULT_SOURCES = PACKAGE_ROOT / "references" / "ADRG_Reference_Index.json"
DEFAULT_SCHEMA = PACKAGE_ROOT / "schemas" / "CPCS_ADRG_RAG_Record_Schema.json"
DEFAULT_OUTPUT = PACKAGE_ROOT / "rag" / "CPCS_ADRG_RAG_Corpus.jsonl"
DEFAULT_MANIFEST = PACKAGE_ROOT / "manifests" / "rag_manifest.json"

MARKER_RE = re.compile(
    r'<!--\s*RAG_CHUNK\s+id="(?P<id>[^"]+)"\s+title="(?P<title>[^"]+)"\s+concepts="(?P<concepts>[^"]*)"\s*-->'
)
DOC_SUMMARY_RE = re.compile(r"<!--\s*RAG_DOC_SUMMARY:\s*(.*?)\s*-->", re.DOTALL)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ANCHOR_RE = re.compile(r'<a\s+id="([^"]+)"\s*></a>')
SOURCE_ID_RE = re.compile(r"\[(S\d{3})\]")
EVIDENCE_RE = re.compile(r"\[(ESTABLISHED|EMERGING|PROPOSED|OPERATIONALIZATION|PROJECT-OBSERVED|CAUTION)(?:\s+OPERATIONALIZATION)?\]")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def estimate_tokens(text: str) -> int:
    # Deterministic approximation for package validation; not a tokenizer claim.
    return max(1, round(len(text.split()) * 1.33))


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONT_MATTER_RE.search(text)
    if not match:
        raise ValueError("Paper is missing YAML front matter")
    metadata = yaml.safe_load(match.group(1)) or {}
    return metadata, text[match.end():]


def split_atomic_blocks(text: str) -> list[str]:
    """Split on blank lines while preserving fenced code and Markdown tables."""
    lines = text.splitlines()
    blocks: list[str] = []
    current: list[str] = []
    in_fence = False
    fence_token = ""

    def flush() -> None:
        nonlocal current
        if current:
            block = "\n".join(current).strip()
            if block:
                blocks.append(block)
            current = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            token = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_token = token
            elif token == fence_token:
                in_fence = False
                fence_token = ""
            current.append(line)
            i += 1
            continue

        if not in_fence and stripped == "":
            flush()
            i += 1
            continue

        # Preserve consecutive Markdown table rows as one block.
        if not in_fence and stripped.startswith("|"):
            flush()
            table_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            blocks.append("\n".join(table_lines).strip())
            continue

        current.append(line)
        i += 1

    flush()
    return blocks


def split_oversize_plain_block(block: str, maximum_tokens: int) -> list[str]:
    if estimate_tokens(block) <= maximum_tokens or block.lstrip().startswith(("```", "~~~", "|")):
        return [block]
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9`*])", block)
    parts: list[str] = []
    current: list[str] = []
    for sentence in sentences:
        candidate = " ".join(current + [sentence]).strip()
        if current and estimate_tokens(candidate) > maximum_tokens:
            parts.append(" ".join(current).strip())
            current = [sentence]
        else:
            current.append(sentence)
    if current:
        parts.append(" ".join(current).strip())
    return parts


def chunk_section(text: str, target_tokens: int, maximum_tokens: int) -> list[str]:
    atomic: list[str] = []
    for block in split_atomic_blocks(text):
        atomic.extend(split_oversize_plain_block(block, maximum_tokens))

    chunks: list[str] = []
    current: list[str] = []
    for block in atomic:
        candidate = "\n\n".join(current + [block]).strip()
        if current and estimate_tokens(candidate) > maximum_tokens:
            chunks.append("\n\n".join(current).strip())
            current = [block]
        else:
            current.append(block)
        if current and estimate_tokens("\n\n".join(current)) >= target_tokens:
            chunks.append("\n\n".join(current).strip())
            current = []
    if current:
        chunks.append("\n\n".join(current).strip())
    return chunks


def heading_path(text: str) -> list[str]:
    path: list[str] = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = re.sub(r"\s+#+$", "", match.group(2)).strip()
        while len(path) >= level:
            path.pop()
        path.append(title)
    return path


def evidence_labels(text: str) -> list[str]:
    labels = {m.group(1) for m in EVIDENCE_RE.finditer(text)}
    if "PROPOSED" in text and "OPERATIONALIZATION" in text:
        labels.add("OPERATIONALIZATION")
    return sorted(labels)


def extract_sections(body: str) -> list[dict[str, Any]]:
    # Stop before references because sources are emitted from the structured index.
    body = body.split("\n# Full Reference List", 1)[0]
    matches = list(MARKER_RE.finditer(body))
    if not matches:
        raise ValueError("No RAG_CHUNK markers found")
    sections: list[dict[str, Any]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        section_text = body[start:end].strip()
        concepts = [c.strip() for c in match.group("concepts").split(",") if c.strip()]
        sections.append(
            {
                "marker_id": match.group("id"),
                "title": match.group("title"),
                "concepts": concepts,
                "text": section_text,
            }
        )
    return sections


def tail_words(text: str, count: int) -> str:
    words = text.split()
    return " ".join(words[-count:]) if words else ""


def make_record_id(marker_id: str, subindex: int, total: int) -> str:
    return marker_id if total == 1 else f"{marker_id}.{subindex:02d}"


def build_records(
    paper_path: Path,
    sources_path: Path,
    target_tokens: int,
    maximum_tokens: int,
    overlap_tokens: int,
) -> list[dict[str, Any]]:
    raw = paper_path.read_text(encoding="utf-8")
    metadata, body = parse_front_matter(raw)
    summary_match = DOC_SUMMARY_RE.search(body)
    summary = " ".join(summary_match.group(1).split()) if summary_match else ""
    document_id = str(metadata.get("document_id", "CPCS-ADRG-RP-2026-01"))
    version = str(metadata.get("version", "1.0"))

    records: list[dict[str, Any]] = []
    document_text = summary or str(metadata.get("title", "CPCS ADRG Research Paper"))
    records.append(
        {
            "record_id": f"{document_id}.document",
            "record_type": "document",
            "document_id": document_id,
            "version": version,
            "title": str(metadata.get("title", "CPCS ADRG Research Paper")),
            "heading_path": [],
            "chunk_index": 0,
            "text": document_text,
            "context_before": "",
            "summary": summary,
            "concepts": [str(x) for x in metadata.get("knowledge_domains", [])],
            "source_ids": [],
            "evidence_labels": ["PROPOSED"],
            "anchors": ["adrg-abstract"],
            "word_count": len(document_text.split()),
            "estimated_tokens": estimate_tokens(document_text),
            "source_hash": sha256_text(raw),
            "metadata": {
                "date": metadata.get("date"),
                "literature_cutoff": metadata.get("literature_cutoff"),
                "status": metadata.get("status"),
                "framework_name": metadata.get("framework_name"),
                "paper_path": str(paper_path.relative_to(PACKAGE_ROOT)),
            },
        }
    )

    prior_text = ""
    chunk_index = 1
    for section in extract_sections(body):
        chunks = chunk_section(section["text"], target_tokens, maximum_tokens)
        for subindex, chunk in enumerate(chunks):
            rid = make_record_id(section["marker_id"], subindex, len(chunks))
            records.append(
                {
                    "record_id": rid,
                    "record_type": "paper_chunk",
                    "document_id": document_id,
                    "version": version,
                    "title": section["title"],
                    "heading_path": heading_path(chunk),
                    "chunk_index": chunk_index,
                    "text": chunk,
                    "context_before": tail_words(prior_text, overlap_tokens),
                    "summary": "",
                    "concepts": section["concepts"],
                    "source_ids": sorted(set(SOURCE_ID_RE.findall(chunk))),
                    "evidence_labels": evidence_labels(chunk),
                    "anchors": sorted(set(ANCHOR_RE.findall(chunk))),
                    "word_count": len(chunk.split()),
                    "estimated_tokens": estimate_tokens(chunk),
                    "source_hash": sha256_text(chunk),
                    "metadata": {
                        "marker_id": section["marker_id"],
                        "subchunk_index": subindex,
                        "subchunk_count": len(chunks),
                    },
                }
            )
            prior_text = chunk
            chunk_index += 1

    sources = json.loads(sources_path.read_text(encoding="utf-8"))
    for source in sources:
        authors = ", ".join(source["authors"])
        locator = source.get("url") or source.get("uri")
        text = f"{source['title']} ({source['year']}). Authors: {authors}. Type: {source['type']}. Locator: {locator}. Domains: {', '.join(source['domains'])}."
        records.append(
            {
                "record_id": f"source.{source['source_id']}",
                "record_type": "source",
                "document_id": document_id,
                "version": version,
                "title": source["title"],
                "heading_path": ["Full Reference List"],
                "chunk_index": chunk_index,
                "text": text,
                "context_before": "",
                "summary": "",
                "concepts": source["domains"],
                "source_ids": [source["source_id"]],
                "evidence_labels": ["EMERGING" if source["evidence_tier"].startswith("emerging") else "ESTABLISHED"],
                "anchors": [],
                "word_count": len(text.split()),
                "estimated_tokens": estimate_tokens(text),
                "source_hash": sha256_text(json.dumps(source, sort_keys=True, ensure_ascii=False)),
                "source": source,
                "metadata": {},
            }
        )
        chunk_index += 1

    return records


def validate_records(records: Iterable[dict[str, Any]], schema_path: Path) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    seen: set[str] = set()
    errors: list[str] = []
    for line_no, record in enumerate(records, 1):
        rid = record.get("record_id", f"line-{line_no}")
        if rid in seen:
            errors.append(f"duplicate record_id: {rid}")
        seen.add(rid)
        for error in validator.iter_errors(record):
            path = "/".join(str(p) for p in error.absolute_path)
            errors.append(f"{rid} {path}: {error.message}")
    if errors:
        raise ValueError("RAG validation failed:\n" + "\n".join(errors))


def write_jsonl(records: Iterable[dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def write_manifest(records: list[dict[str, Any]], output_path: Path, corpus_path: Path, paper_path: Path) -> None:
    counts: dict[str, int] = {}
    for record in records:
        counts[record["record_type"]] = counts.get(record["record_type"], 0) + 1
    manifest = {
        "manifest_version": "1.0",
        "document_id": "CPCS-ADRG-RP-2026-01",
        "generated_by": "scripts/build_adrg_rag.py",
        "record_count": len(records),
        "record_counts": counts,
        "paper_sha256": hashlib.sha256(paper_path.read_bytes()).hexdigest(),
        "corpus_sha256": hashlib.sha256(corpus_path.read_bytes()).hexdigest(),
        "corpus_path": str(corpus_path.relative_to(PACKAGE_ROOT)),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", type=Path, default=DEFAULT_PAPER)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--target-tokens", type=int, default=650)
    parser.add_argument("--maximum-tokens", type=int, default=950)
    parser.add_argument("--overlap-tokens", type=int, default=90)
    args = parser.parse_args()

    records = build_records(
        args.paper,
        args.sources,
        args.target_tokens,
        args.maximum_tokens,
        args.overlap_tokens,
    )
    validate_records(records, args.schema)
    write_jsonl(records, args.output)
    write_manifest(records, args.manifest, args.output, args.paper)
    print(json.dumps({
        "status": "ok",
        "records": len(records),
        "output": str(args.output),
        "manifest": str(args.manifest),
    }, indent=2))


if __name__ == "__main__":
    main()
