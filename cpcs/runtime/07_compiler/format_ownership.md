---
id: cpcs.adrg.format_ownership
kind: doctrine
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §13, §14]
primary_route: cpcs/runtime/07_compiler/
secondary_routes:
  - cpcs/knowledge/00_foundations/invariants/
  - cpcs/runtime/07_compiler/semantic_mapping/
interfaces: [cpcs.found.invariant.epistemic_firewall, cpcs.compiler.capability_classes_loss_records]
---

# Format Ownership and Structured-Output Caution

## Format should not influence canonical reasoning

The canonical semantic IR must be format-agnostic. Reasoning happens in a compact
semantic IR; serialization to YAML/JSON/XML/NL happens as late as practical
(SRC-004 §13). A provider that cannot express a canonical control exactly must
not be treated as exact merely because the NL prompt mentions it.

## Format ownership table

| Format | Owns |
| --- | --- |
| Natural Language | creative rationale, audience-facing description |
| YAML | canonical control definitions |
| JSON | execution records, decision/candidate/consequence |
| XML | legacy/exchange serialization |
| JSONL | observation/audit streams |
| Media | evidence (reference images, video, pose) |

## Structured-output caution

Parse validity, schema validity, decision correctness, and render success are
four different things (SRC-004 §14):

```text
parse validity
  ≠
schema validity
  ≠
decision correctness
  ≠
render success
```

The system must report these separately. A model can produce perfectly valid
JSON and still select a candidate that violates a hard invariant.

## Per-format contracts (SRC-011 EXTEND)

> **Source:** SRC-011 §13–§16 — NL, YAML, JSON, XML contracts.

### Natural language — owns intent, audience effect, observable behavior

The director-language pattern uses bracketed clause classes in a fixed order:

```text
[SHOT AND DURATION] [SUBJECT AND ACTION] [PERFORMANCE]
[TIMING] [CAMERA AND PRESENTATION] [NEGATIVES]
```

Rules: describe **observable behavior, not affect words** ("a soft breath
interruption and subtle brow tension" not "she feels afraid"); dense tracks
are never serialized into prose; endpoint fields (duration, aspect ratio,
seed, reference assets) move to API fields when the adapter declares them
native. The compiled example for the 6s shot lives in
`examples/compiled_natural_language_prompt.txt`.

8-step prompt compression (SRC-011 §13): identity/subject → action identity,
count, event order → hard timing/duration/continuity → camera/composition →
observable performance/movement quality → environment/lighting → style and
secondary effects → critical negatives. Emit a loss record for every
compressed or omitted canonical control.

### YAML — owns authoring, policy, profiles, imports, variants, invariants

Nine safety rules (SRC-011 §14): restricted parser (no arbitrary tags, no
merge keys); reject unsafe constructs; validate against authoring schema;
resolve imports with pinned versions + digests; aliases are serialization
devices, not inheritance; typed merges only; scoped, typed overrides;
normalize units/timebase/coordinates; report conflicts, never resolve by
document order. Mini models get shallow YAML only.

### JSON — owns canonical resolved data

Canonical requirements: JSON Schema 2020-12; four validation levels —
(1) parse, (2) schema, (3) semantic/domain rules, (4) cross-field — reported
separately. Constrained generation (5 rules, SRC-011 §15): schema pinned by
version; `additionalProperties` controlled; enums not free strings;
`selected` must be one of `alternatives`; every output re-validated
externally. JSON Pointer/Patch (RFC 6901/6902) for surgical edits — Patch
always begins with a `test` operation.

### XML — owns ordered narrative and namespaced events

Director envelope pattern (`examples/director_envelope.xml`):
`urn:cpcs:adrg:1.0` for the envelope, `urn:cpcs:core:1.1` for score refs,
per-format namespaces (e.g. `urn:cpcs:performance:1.1`, `urn:cpcs:camera:1.1`)
for department events. XML owns beat/dialogue order and annotations; JSON
owns the resolved score it references. XML security: namespace-validate,
reject DTDs/external entities, forbid duplicate names.

## Principle

> Reason/decide in a compact semantic IR, then constrain/serialize as late as
> practical.

Hard output constraints can alter semantic accuracy in some small-model settings
(Ray, 2026). This is an experimental finding to be calibrated against the CPCS
model stack, not a universal provider claim.

## Verification

`test_parse_validity_reported_separately`,
`test_schema_validity_reported_separately`,
`test_decision_correctness_reported_separately`,
`test_render_success_reported_separately`.
