---
id: cpcs.retrieval.agent_retrieval_contract
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§41, §51]
primary_route: cpcs/runtime/03_retrieval/
secondary_routes:
  - cpcs/runtime/05_strategy/
interfaces: []
---

# Agent Retrieval Contract

Retrieval must return structured knowledge with evidence boundaries, not
isolated terminology. A retrieval packet bundles:

```text
CONCEPT · DEFINITION · NON-MEANING · APPLICABILITY · CONTRAINDICATIONS ·
REALIZATION CANDIDATES · SCOPE · TEMPORAL BEHAVIOR · INTERACTIONS ·
GUARDRAILS · PROVIDER FALLBACKS · VERIFICATION · EVIDENCE
```

## Retrieval packet (L2.§41.1)

```yaml
retrieval_packet:
  concept: laban.effort.flow.bound
  semantic: { definition_ref: source_123 }
  application: { applies_when: [rule_014], avoid_when: [rule_022] }
  realization: { candidates: [realization_031, realization_044] }
  composition: { reinforces: [control_071], conflicts: [control_082] }
  compiler: { fallback: [fallback_009] }
  verification: { fixture: [fixture_laban_flow_003] }
```

## Completeness questions (L2.§51)

Before selecting a concept the agent must be able to answer: what is it · why
use it · when to avoid · what it changes · where it applies · how long · what
it interacts with · expected visible result · can the provider express it ·
how to know if it worked. If retrieval cannot answer these, the concept is
**incomplete application knowledge**.

## Graph separation (L2.§40)

Research KG = source-grounded concepts/evidence · Execution/Reasoning Graph
= application rules, candidate controls, dependencies, runtime state ·
Video Observation Graph = measured/detected observations from rendered media.
Application relations are **not** dumped into the research graph.
