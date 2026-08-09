---
id: cpcs.adrg.reasoning_graph_schema
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-011 §5, §6, §7, §8, §18, schemas/CPCS_ADRG_Reasoning_Graph_Schema.json]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.runtime.typed_reasoning_graph
  - cpcs.adrg.decision_record
  - cpcs.adrg.model_scaled_policy
  - cpcs.adrg.decision_aware_routing
---

# ADRG Reasoning Graph Schema v1.0

> **Source:** SRC-011 §5–§8, §18 + `schemas/CPCS_ADRG_Reasoning_Graph_Schema.json`
> (schema_version const `cpcs-adrg/1.0`).

The Adaptive Director Reasoning Graph is a typed directed multigraph
\(G_R = (V_R, E_R, P, B, A)\): nodes (goals, questions, candidates, decisions,
validators, failures, repairs), typed edges, policies, budgets, and
annotations. It is the **reasoning control plane** above the CPCS compiler
(ASL → CIR → TEP → VER) — it decides, then feeds the existing compiler
(SRC-004 §21 boundary: it never replaces the compiler or becomes a second
reasoning authority/database).

## Input contract

- `hard_invariants` — must never change (identity, action identity, duration,
  contact topology, continuity locks).
- `variation_axes` — declared axes with allowed values
  (e.g. `camera_treatment: [late_dolly_in, telephoto_observer]`).
- `maximum_simultaneous_deltas` — default 2.
- `requested_outputs` — which artifacts to emit.
- `target_model_profile` — pinned adapter URI + date.

## Output contract (4 artifacts)

1. canonical reasoning graph (JSON per schema)
2. decision records (per decision node)
3. director envelope (XML, namespaced)
4. compiled natural-language prompt (with compile-loss report)

## Eleven execution phases (Phase 0–10)

Phase 0 normalize request → 1 retrieve bundle → 2 decompose into departments →
3 propose candidates on declared axes → 4 admit/prune branches → 5 select
(decision records) → 6 compile to canonical controls → 7 negotiate target
capabilities → 8 emit target artifacts with loss ledger → 9 validate
(checkpoints A–I) → 10 repair or escalate, then reverify.

## Five graph planes + cross-plane invariants

| Plane | Owns |
| --- | --- |
| A knowledge/evidence | retrieval objects, evidence results, source refs |
| B scene intent/control | goals, constraints, canonical controls |
| C reasoning execution | questions, candidates, decisions, transforms |
| D compilation/realization | compile mappings, artifacts, realization statuses |
| E verification/experiments | validations, failures, repairs, metrics, experiments |

Six cross-plane invariants (SRC-011 §6): a node may not claim another
plane's authority; evidence enters only via plane A; decisions in C resolve
only into controls in B; controls reach D only through compile mappings;
every failure in E links back to its responsible node; every decision has a
validator or an explicit `unresolved` entry.

## Node ontology (18 types)

`goal · constraint · question · retrieval_query · evidence_result · candidate ·
decision · transform · compile_mapping · validation · failure · repair ·
metric · experiment · artifact · model_policy · budget · branch · merge`

Status vocabulary (9): `planned → ready → running → resolved | blocked |
failed → repaired → revalidated | superseded`. A node may be `resolved`
(decision made), `blocked` (needs input), or `failed` (validator rejected) —
then `repaired` → `revalidated`, or `superseded` by a newer revision.

## Edge ontology (~42 types, 5 groups)

- **Knowledge:** pairs_with, conflicts_with, supported_by, contradicted_by,
  sourced_from, alias_of, specializes
- **Reasoning:** decomposes_to, depends_on, grounds, proposes, variant_of,
  selected_over, rejected_because, aggregates, requires_tool
- **Scene/temporal:** precedes, overlaps, triggers, synchronizes_with,
  targets, contacts, observed_by, preserves
- **Compilation:** compiled_to, native_exact, native_approximate,
  baked_into_reference, compressed_to_text, postprocess_only,
  evaluation_only, dropped_with_warning, unsupported_error
- **Validation:** validated_by, passes, fails, caused_by, mitigated_by,
  repaired_by, revalidated_by

Eight edge constraints (schema `allOf`): `selected_over` requires a
`decision_id`; `compiled_to` requires `target_adapter` +
`realization_status`; `depends_on` must be acyclic except declared feedback
loops with bounds; `proposes` requires a declared axis or open question;
`grounds` requires a resolved evidence node; `fails` requires the failing
validator id; `repairs` requires the failure id; `revalidated_by` requires
the prior failed validation id.

## Realization statuses

`native_exact · native_approximate · baked_into_reference ·
compressed_to_text · postprocess_only · evaluation_only ·
dropped_with_warning · unsupported_error` — identical vocabulary to
capability_classes_and_loss_records (SRC-004 §22); the graph schema makes it
an edge constraint rather than a free field.

## DecisionRecord (per decision node)

Required: `decision_id, question, alternatives, selected, criteria,
confidence`. Optional: `scores, evidence_refs, assumptions, unresolved, loss`.
`selected` must be one of `alternatives`; `evidence_refs` must resolve to
nodes in plane A; missing hard control → `unsupported` or `escalation`,
never silent drop.

## Worked example (mini policy, §18)

Request: 6s single shot, Mara approaches concealing fear, recognition at
final foot plant, end close-up (`examples/director_request.yaml`). Mini
profile runs a fixed A→G sequence: goal → question (camera treatment) →
2 candidates (late dolly-in, telephoto observer) → decision record
(selected late_dolly_in, confidence 0.77, criteria recognition_emphasis /
timing_clarity / generation_reliability) → canonical control (native_exact)
→ compiled NL prompt (compressed_to_text, loss: exact camera path) →
validation (graph integrity pass). The full instance lives in
`examples/canonical_reasoning_graph.json` (valid against the schema).

## Relationship to the department graph

`typed_reasoning_graph` (SRC-006 §4.4) is the department-view aggregation
graph (9 node / 14 edge types) used when independent partial decisions must
merge. This schema is the ADRG execution-graph control plane: same family,
more granular vocabulary, schema-constrained. Aggregation rules from the
department graph still apply; the ADRG graph adds plane discipline and
realization-status constraints on edges.

## Verification

`test_graph_instances_validate_against_schema`,
`test_selected_over_requires_decision_id`,
`test_compiled_to_requires_realization_status`,
`test_depends_on_acyclic`,
`test_every_decision_has_validator_or_unresolved`.
