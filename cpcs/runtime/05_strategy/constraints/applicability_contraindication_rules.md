---
id: cpcs.strategy.applicability_contraindication
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§19, §20, §34]
primary_route: cpcs/runtime/05_strategy/constraints/
secondary_routes:
  - cpcs/runtime/03_retrieval/
interfaces: []
---

# Applicability and Contraindication Rules

A reasoning system must know **when to use** a concept and **when not to**.
`ApplicabilityRule` and `ContraindicationRule` are CPCS reasoning constructs,
not framework concepts.

## ApplicabilityRule (L2.§19.2)

```yaml
applicability_rule:
  id: rule.laban.flow.bound.performance_control
  target_concept: laban.effort.flow.bound
  applies_when: [movement_requires_visible_control, director_intent_requires_restraint]
  avoid_when: [intended_motion_requires_unrestricted_release]
  does_not_imply: [rigid_motion, frozen_joints, low_velocity]
  evidence_class: source_supported_interpretation
  confidence: medium
```

Applicability is conditioned by dimensions (intent, action, actor role, shot
scale, camera, body scope, interaction, style, temporal phase, provider,
evidence state) — contextual dimensions, **not** a second ontology.

## ContraindicationRule (L2.§20)

```yaml
contraindication_rule:
  id: rule.facs.au12.not_private_emotion
  target_concept: facs.au12
  do_not_infer: [private_happiness, sincerity, internal_emotional_state]
  allowed_use: [authored_smile_display, observed_facial_movement]
  evidence_class: source_established
```

Fundamental boundaries: `AU12 ≠ happy`; `Laban Strong ≠ angry`;
`Bartenieff Cross-Lateral ≠ confident`. The observation layer must not reverse
an authored control into an unsupported private-state claim.

## Semantic guardrails (L2.§34)

Every high-value concept should carry a machine-readable guardrail
(means / does_not_mean / common_provider_failure / mitigation). Promotion of
guardrail failure statements to authority requires source/package verification.
