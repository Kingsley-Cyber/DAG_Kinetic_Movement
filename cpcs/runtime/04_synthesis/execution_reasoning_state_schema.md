---
id: cpcs.runtime.execution_reasoning_state_schema
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §6, §7]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.reasoning_atom
  - cpcs.runtime.continuity_capsule
  - cpcs.runtime.state_equivalence_keys
  - cpcs.runtime.canonical_schema
---

# Execution Reasoning State Schema

> **Source:** SRC-006 §6.1–§6.7 — "Canonical JSON Schema" and projections

## Top-level state object

JSON Schema Draft 2020-12, `urn:cpcs:schema:execution-reasoning-state:0.1.0`.
Required fields:

```text
schema_version · state_id · revision · task_id · executor_id
status · continuity_capsule · atoms · budget · equivalence
```

Optional: `parent_state_ids`, `reasoning_mode`, `graph`, `branches`,
`failures`, `repairs`, `audit_refs`.

- `status`: `open | feasible | accepted | rejected | blocked | exhausted`
- `reasoning_mode`: `direct | bounded_refine | selective_tree_search |
  typed_graph_aggregation | bounded_local_search | aot_prompting |
  failure_directed_repair | hybrid`
- `origin_class` enum keeps `unknown` and `unobservable` distinct from
  `evidence`, `inference`, `authored`, `creative_choice`, `derived`,
  `interpreted`, `measured`, `detected`, `simulated`.
- `unevaluatedProperties: false` at closed leaves catches accidental
  parallel fields; extension points are explicit.
- `value` stays open: it must reference existing CPCS semantic definitions,
  never duplicate them inside the reasoning schema.
- `format: date-time` is an annotation unless the validator asserts it;
  validator behavior is fixed in the runtime contract.

## Projection roles

- **YAML** — authored intent, inheritance, profiles, comments; resolves
  deterministically to canonical JSON before hashing.
- **Canonical JSON** — resolved meaning, validation, hashing, diffing.
- **XML** — only for ordered/namespaced/mixed-content envelopes; XML order
  must not be mistaken for causality.
- **Natural language** — provider-facing, not round-trippable truth; the
  compiler records omitted fields as expected representation loss.
- **JSONL audit** — append-only audit events; timestamps and run IDs belong
  in the audit stream and are normally excluded from semantic equivalence.

## Round-trip rule

Only YAML ↔ resolved JSON and JSON ↔ XML with explicit schemas are
candidates for semantic round-trip tests. Natural language is evaluated by
field preservation and provider adherence, not exact round-trip equality.

## Schema notes

- The patch `$defs` is abbreviated; production must enforce RFC 6902
  operation-specific requirements.
- Placeholder hashes and capability versions in examples must never enter
  fixtures as if computed.
