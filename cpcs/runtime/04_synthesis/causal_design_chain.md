---
id: cpcs.adrg.causal_design_chain
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §10]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/knowledge/00_foundations/causality/
  - cpcs/verification/
interfaces: [cpcs.found.causality.causal_event_semantics, cpcs.adrg.decision_record]
---

# Causal Design Chain

CPCS has controls and mappings, but ADRG needs an explicit design-causality chain
(SRC-004 §10). This must not be confused with an empirical scientific causal
claim.

## The chain

```text
problem
  → treatment
  → directorial decision
  → canonical control
  → expected visual effect
  → verification target
```

Example:

```text
problem:        strike reads as instantaneous
treatment:      visible preparation before strike
decision:       add anticipation phase
control:        phase.anticipation
expected_effect: increased action readability
verification:  measure preparation-to-action timing and reviewer readability
```

## Seven causal claim classes

1. **Design causality** — the treatment is *intended* to cause the control/effect
   (`design_causes`). Authored intent, not empirical evidence.
2. **Empirical causal claim** — evidence supports that changing X causes Y
   (`causal_claim`). Requires controlled comparison to promote.
3. **Temporal succession** — A precedes B (no causal claim).
4. **Correlation** — A co-occurs with B (no causal claim).
5. **Narrative motivation** — A motivates B in the story logic.
6. **Dependency** — A requires/depends_on B (structural, not causal).
7. **Prevention** — A prevents B (causal inhibitory).

Design causality and empirical causality must not be conflated. The first is an
authored intent; the second requires experimental evidence.

## Distinction from existing causal event semantics

The existing `causal_event_semantics` card covers event-level causality (A_kick
causes water_splash). The causal design chain operates at the decision level:
a directorial treatment is intended to cause a canonical control, which is
expected to produce a visual effect, which is then verified. They are different
planes of the same causal principle.

## Verification

`test_design_causal_edge_not_empirical_causal_claim`,
`test_causal_chain_trace_complete`,
`test_expected_effect_has_verification_target`.
