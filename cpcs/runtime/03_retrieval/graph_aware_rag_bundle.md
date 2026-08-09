---
id: cpcs.adrg.graph_aware_rag
kind: method
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-011 §12]
primary_route: cpcs/runtime/03_retrieval/
secondary_routes:
  - cpcs/research/sources/
interfaces:
  - cpcs.retrieval.agent_retrieval_contract
  - cpcs.rag.ingestion_architecture
  - cpcs.adrg.reasoning_graph_schema
---

# Graph-Aware RAG Bundle Retrieval

> **Source:** SRC-011 §12 — "Graph-aware RAG".

Retrieve a **bundle, not a chunk**. A single nearest chunk cannot carry the
cross-domain evidence a director decision needs (performance + motion +
camera + capability + failure history). Retrieval must be typed, expanded
along declared edges, and reported with a coverage contract.

## Twelve retrieval object types

```text
concept_card · template · variant_record · decision_record · failure_card ·
evidence_result · capability_profile · adapter_contract · policy ·
budget_record · metric_definition · experiment_record
```

## Query decomposition

Split the request into department queries (narrative, performance, face/gaze,
body/movement, camera, presentation, target compilation, verification) and
retrieve per department; then merge with conflict awareness rather than
retrieving one blob.

## Ten-step hybrid pipeline

1. normalize and decompose the request
2. dense retrieval per department query (top_k per profile: 4/6/10)
3. typed-object filter (12 types)
4. **bounded graph expansion** along permitted edges only
   (`pairs_with`, `conflicts_with`, `supported_by`, `contradicted_by`,
   `requires_tool`, `failure` cards) — depth 2, max 24 nodes
5. include conflicts and failure cards explicitly (they are retrieval
   objects, not noise)
6. rerank by provenance, capability fit, and evidence label
7. pack context in a fixed order (intent → invariants → evidence → conflicts →
   failures → capability profile)
8. attach coverage report
9. schema-validate the bundle
10. hand off to the planner

## Retrieval score

\[
R(o \mid q) = \alpha \cdot \text{sim}(o, q) + \beta \cdot \text{provenance}(o)
+ \gamma \cdot \text{capability\_fit}(o) - \delta \cdot \text{stale}(o)
\]

Weights are defaults, not laws; the score is a ranking aid, and conflicts
are surfaced even when they score low.

## Context packing order

intent → hard invariants → evidence (by confidence) → conflicts →
failure cards → capability profile. Dense tracks are never serialized into
prose (SRC-011 §13); endpoint fields move to API fields when the adapter
declares them native.

## Coverage contract

Every retrieval returns a coverage report: which departments are covered,
which retrieval object types are missing, which invariants have no
supporting evidence, and which queries were under-served. The planner must
not treat absence of evidence as evidence of absence — under-covered
departments escalate or degrade explicitly.

## Relationship to existing retrieval cards

`agent_retrieval_contract` (cpcs.retrieval) defines the general agent
retrieval contract; `rag_ingestion_architecture` defines the record schema
for the corpus. This card defines the ADRG graph-expansion retrieval
procedure on top of both. The package's RAG corpus (`rag_manifest.json`,
78 records: 1 document + 35 paper chunks + 42 sources) is a reference
instantiation; `tests/retrieval_queries.json` (q001–q005) provides
retrieval acceptance queries with expected concepts, operators, and
must-include terms.

## Verification

`test_retrieval_returns_bundle_with_coverage`,
`test_graph_expansion_within_bounds`,
`test_conflicts_included_not_suppressed`,
`test_packing_order_respected`,
`test_underserved_department_escalates`.
