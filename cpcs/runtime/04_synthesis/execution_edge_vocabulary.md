---
id: cpcs.adrg.execution_edge_vocabulary
kind: vocabulary
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §6, §27]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/knowledge/00_foundations/causality/
  - cpcs/runtime/06_canonical/
interfaces: [cpcs.found.causality.causal_event_semantics, cpcs.found.causality.universal_relation_vocabulary]
---

# Execution-Only Edge Vocabulary

A separate execution-edge namespace for per-decision dependencies and audit
relationships. This is distinct from the authored knowledge-graph edge policy
(SRC-004 §6.1). The two may be projected into a derived union graph for
retrieval/visualization, but their authorities remain separate.

```text
knowledge graph edges    = durable reusable semantic relationships
reasoning execution edges = per-decision dependencies and audit relationships
```

## 21 execution-only edges

```text
supports
contradicts
requires
depends_on
proposes
alternative_to
selected_over
rejected_because
refines
replaces
motivates
design_causes
prevents
verifies
derived_from
compiled_to
realized_as
fails
repaired_by
revalidated_by
measured_by
```

Do not inject all ADRG execution edges into the existing authored edge policy.

## Causal vocabulary distinction

```text
design_causes
```

means: *this treatment is intended to cause this control/effect.*

```text
causal_claim
```

means: *empirical evidence supports that changing X causes Y.*

These are not the same. Empirical causal promotion should require a controlled
comparison. Design causality is an authored intent; empirical causality is a
research finding.

## Canonical ADRG graph example

A minimal graph uses four planes (SRC-004 §20):

```text
scene_intent_control  → goal/problem nodes
reasoning_execution   → candidate/decision nodes
scene_intent_control  → transform/control nodes
verification_experiment → validation nodes
```

Edges connect nodes across planes: `proposes`, `selected_over`, `compiled_to`,
`validated_by` (with `realization_status` and `target_adapter`).

## Compiler operations

```text
resolve_decision · admit_candidate · enforce_invariants ·
apply_variant_delta · route_operator · contract_state ·
resolve_capability · compile_existing_strategy · emit_loss ·
emit_verification_ref · propose_repair · apply_json_patch · revalidate
```

## ADRG-specific validators

```text
decision_schema · candidate_schema · decision_reference_integrity ·
invariant_preservation · alternative_delta_integrity ·
execution_dependency_acyclicity · repair_bound ·
compile_loss_completeness · provenance_resolution ·
capability_profile_freshness
```

## Verification

`test_design_causal_edge_not_empirical_causal_claim`,
`test_execution_dependency_acyclicity`,
`test_causal_edge_type_validity`.
