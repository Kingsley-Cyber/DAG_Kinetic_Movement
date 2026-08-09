---
id: cpcs.found.relation_vocabulary
kind: vocabulary
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 §28, L2.§40, L2.§59]
primary_route: cpcs/knowledge/00_foundations/causality/
secondary_routes:
  - cpcs/runtime/06_canonical/
interfaces: []
---

# Universal Relation Vocabulary

Do **not** create dozens of new domain predicates. Use existing universal
relations and add only relationships that have executable consumers.

## Closed relation set

```text
describes · targets · coactivates_with · temporally_overlaps · precedes ·
follows · measured_by · detected_by · derived_from · has_proxy ·
calibrated_by · confusable_with · nonadditive_with · constrained_by ·
compiled_to · approximates · unsupported_by
```

`approximates` is load-bearing — it prevents a proxy from becoming a semantic
synonym:

```text
Laban.direct --approximates--> path_straightness
```

## Application-layer relations (SRC-002 L2.§40, §59)

```text
applies_when · contraindicated_when · expressed_by · realized_by ·
modulates · reinforces · constrains · conflicts_with · requires ·
precedes · lags · synchronizes_with · causes · enables · persists_until ·
scoped_to · verified_by · compiled_via · fallback_to
```

## Graph separation (L2.§40)

- Research KG = source-grounded concepts and evidence
- Execution/Reasoning Graph = application rules, candidate controls, dependencies, runtime state
- Video Observation Graph = measured/detected observations from rendered media

Application relations must **not** be dumped into the research graph
indiscriminately. Do not create a new graph database or parallel ontology
solely for these relations.
