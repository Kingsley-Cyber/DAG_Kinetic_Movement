---
id: cpcs.strategy.semantic_guardrails
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§34]
primary_route: cpcs/runtime/05_strategy/constraints/
secondary_routes:
  - cpcs/knowledge/00_foundations/invariants/
interfaces: []
---

# Semantic Guardrails

Every high-value concept should have a machine-readable guardrail record:
means / does_not_mean / common_provider_failure / mitigation.

## Laban example

```yaml
semantic_guardrail:
  concept: laban.effort.time.sudden
  means: [sudden_temporal_quality]
  does_not_mean: [entire_clip_is_fast, maximum_velocity, zero_anticipation]
  common_provider_failure: [globally_speed_up_motion]
  mitigation: [localize_control_to_action_phase]
  evidence_class: source_supported_interpretation
```

## FACS example

```yaml
semantic_guardrail:
  concept: facs.au12
  means: [visible_facial_action_as_defined_by_facs]
  does_not_mean: [happiness, sincerity, private_emotional_state]
  provider_failure: [exaggerated_smile]
```

## Bartenieff example

```yaml
semantic_guardrail:
  concept: bartenieff.cross_lateral
  means: [cross_body_connectivity_pattern]
  does_not_mean: [any_left_right_alternation, generic_coordination]
  provider_failure: [arbitrary_arm_leg_crossing]
```

The final failure statements require source/package verification before
promotion to authority.
