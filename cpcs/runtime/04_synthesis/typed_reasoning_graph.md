---
id: cpcs.runtime.typed_reasoning_graph
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.4, §11.4]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/knowledge/00_foundations/causality/
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.adrg.execution_edge_vocabulary
  - cpcs.found.causality.causal_event_semantics
  - cpcs.runtime.reasoning_atom
  - cpcs.runtime.execution_reasoning_state_schema
---

# Department-Aware Typed Reasoning Graph

> **Source:** SRC-006 §4.4 — "Department-aware typed graph"

## Principle

The recommended object is `reasoning_dependency_graph`, not an autonomous
"department society." A view is a producer/consumer label over shared
canonical objects; it does not own a parallel ontology. Do not reuse the
research KG or VOG as this graph.

## Views

```text
performance · motion · camera · editing · audio · VFX
narrative · provider_realization · verification
```

## Node types

```text
requirement · proposal · accepted_decision · constraint
verification_condition · failure · repair · provider_mapping
```

## Edge types

```text
depends_on · requires · enables · precedes · causes · motivates
constrains · conflicts_with · realizes · verifies · invalidates
protects · supersedes · derived_from
```

## Aggregation rules

1. Nodes write to canonical paths, not prose-only conclusions.
2. A shared-path collision becomes an explicit conflict record.
3. Hard constraints dominate preferences.
4. `precedes` does not imply `causes`.
5. Acyclic dependency components are topologically evaluated.
6. Cycles are permitted only for declared feedback loops and receive an
   iteration bound.
7. Unresolved hard conflicts block compilation.
8. Soft conflicts remain as Pareto alternatives or require an authored
   tie-break.
9. Aggregation produces a new accepted state revision; it does not mutate
   source nodes.

## When to use it

Use graph aggregation when at least two independently useful partial
decisions must be merged, or when cross-view constraints cannot be
represented as a simple sequence. Do not invoke it for a single-shot task
with no meaningful cross-view dependency.

## Verification

`test_graph_shared_path_collision_yields_conflict_record`,
`test_graph_undeclared_cycle_fails`,
`test_declared_feedback_cycle_stops_at_bound`,
`test_graph_precedes_does_not_imply_causes`,
`test_aggregation_immutable_source_nodes` (SRC-006 §11.4).
