#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAILS: list[str] = []

def fail(msg: str) -> None:
    FAILS.append(msg)
    print(f"FAIL: {msg}")

def ok(msg: str) -> None:
    print(f"OK:   {msg}")

required = [
    'README.md','00_ORIGINAL_SPEC.txt','01_SPEC_AUDIT_AND_VERDICT.md',
    '02_REPO_GAP_MATRIX.csv','02_REPO_GAP_MATRIX.jsonl',
    '04_HARDENED_CODEX_EXECUTION_PROMPT.md','05_DEEP_RESEARCH_SOURCE_PROMPT.md',
    '06_REPO_INTEGRATION_PLAN.md','07_SOURCE_SEED_CATALOG.csv',
    'execution_manifest.json','execution_manifest.yaml','schemas/gap_record.schema.json'
]
for rel in required:
    p = ROOT / rel
    if p.is_file() and p.stat().st_size > 0:
        ok(f"present: {rel}")
    else:
        fail(f"missing/empty: {rel}")

manifest = json.loads((ROOT/'execution_manifest.json').read_text())
for rel in manifest['artifacts']:
    if not (ROOT/rel).exists() and rel != 'tools/validate_kit.py':
        fail(f"manifest artifact missing: {rel}")
ok('execution_manifest.json parses')

schema = json.loads((ROOT/'schemas/gap_record.schema.json').read_text())
required_keys = schema['required']
records = []
ids = set()
for lineno, line in enumerate((ROOT/'02_REPO_GAP_MATRIX.jsonl').read_text().splitlines(), 1):
    if not line.strip():
        continue
    rec = json.loads(line)
    records.append(rec)
    missing = [k for k in required_keys if k not in rec]
    if missing:
        fail(f"JSONL line {lineno}: missing {missing}")
    if not re.fullmatch(r'DMR-[0-9]{3}', rec.get('id','')):
        fail(f"JSONL line {lineno}: invalid id")
    if rec.get('id') in ids:
        fail(f"duplicate id: {rec.get('id')}")
    ids.add(rec.get('id'))
    if rec.get('status') not in {'existing_strong','existing_partial','missing','conflict'}:
        fail(f"{rec.get('id')}: invalid status")
    if rec.get('priority') not in {'P0','P1','P2','P3'}:
        fail(f"{rec.get('id')}: invalid priority")
ok(f"JSONL records parse and basic schema checks pass: {len(records)}")

with (ROOT/'02_REPO_GAP_MATRIX.csv').open(newline='', encoding='utf-8') as f:
    csv_records = list(csv.DictReader(f))
if len(csv_records) != len(records):
    fail(f"CSV/JSONL count mismatch: {len(csv_records)} vs {len(records)}")
else:
    ok(f"CSV/JSONL count parity: {len(records)}")
for a,b in zip(csv_records, records):
    if a != {k:str(v) for k,v in b.items()}:
        fail(f"CSV/JSONL content mismatch at {b.get('id')}")
        break
else:
    ok('CSV/JSONL content parity')

with (ROOT/'07_SOURCE_SEED_CATALOG.csv').open(newline='', encoding='utf-8') as f:
    srcs = list(csv.DictReader(f))
sids = [s['source_id'] for s in srcs]
if len(sids) != len(set(sids)):
    fail('duplicate source_id in source catalog')
else:
    ok(f"source IDs unique: {len(sids)}")

prompt = (ROOT/'04_HARDENED_CODEX_EXECUTION_PROMPT.md').read_text()
for phrase in [
    'Phase 0 — baseline and governance gate',
    'Mandatory seven-phase verdict',
    'Bartenieff',
    'Behavior Markup Language',
    'scene/VOG graph',
    'semantic equivalence',
    'python3 lab/scripts/validate_repo.py',
    'git ls-remote origin refs/heads/agent/director-motion-reasoning',
]:
    if phrase.lower() not in prompt.lower():
        fail(f"Codex prompt missing required phrase: {phrase}")
else:
    ok('Codex prompt contains required execution gates')

if FAILS:
    print(f"\nKIT VALIDATION FAILED: {len(FAILS)} issue(s)")
    sys.exit(1)
print('\nKIT VALIDATION PASSED')
