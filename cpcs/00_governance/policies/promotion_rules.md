---
id: cpcs.gov.promotion_rules
kind: policy
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §25, §28]
primary_route: cpcs/00_governance/policies/
secondary_routes:
  - cpcs/research/sources/experiments/
  - cpcs/runtime/04_synthesis/
interfaces: [cpcs.gov.distillation_implementation_priority, cpcs.adrg.experiments]
---

# Promotion Rules

A new reasoning policy, operator, or representation must remain `unexplored`
until evidence supports its promotion (SRC-004 §25). This is consistent with the
existing repository integration plan and the distillation priority policy.

## Promotion ladder

```text
unexplored
  → experiment_supports (isolated experiment)
  → repeats_or_scoped (multiple tasks or explicit scope)
  → cost_and_failure_recorded
  → no_rights_safety_issue
  → evidence_calibrated_confidence
  → PROMOTED
```

No step may be skipped. A policy that passes one step but fails a later step
returns to `unexplored` with the failure recorded.

## Implementation order

Promotion follows the 6-phase implementation order (SRC-004 §28):

1. **Phase 1 — semantic bridge**: DecisionRecord, Candidate, Invariant,
   Consequence. Emit from existing reasoning runtime.
2. **Phase 2 — decision-aware routing**: Add routing features to routing state.
   Do not remove existing six executors.
3. **Phase 3 — compiler linkage**: Attach decision_id, candidate_id, loss_id,
   verification_id to existing strategy/compiler result.
4. **Phase 4 — bounded repair**: Connect validator failures to FailureRecord →
   RepairRecord → JSON Patch → recompile → revalidate.
5. **Phase 5 — state contraction**: Introduce explicit
   active/compressed/source/decision/failure memory.
6. **Phase 6 — experiments**: Run E-ADRG-001 through E-ADRG-006. Only after
   measurement should new routing defaults become verified policy.

## Boundary

No universal claim that any single format or reasoning operator is globally
superior (SRC-004 §30). Promotion is per-task-class, not universal.

## Verification

`test_promotion_requires_experiment_evidence`,
`test_implementation_phase_order_respected`,
`test_no_universal_carrier_claim_without_experiment`.
