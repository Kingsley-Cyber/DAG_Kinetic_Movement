---
id: cpcs.synthesis.cross_framework_composition
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§30]
primary_route: cpcs/runtime/04_synthesis/performance/
secondary_routes:
  - cpcs/runtime/05_strategy/
interfaces: []
---

# Cross-Framework Composition

FACS, Laban, Bartenieff, gaze, breath, posture and camera controls are **not**
independent additive sliders. A composition may:

```text
reinforce · constrain · conflict · subordinate · substitute · sequence
```

## Composition record

```yaml
composition:
  id: composition.defensive_counter
  controls: [facs.au4, gaze.target.hands, laban.effort.flow.bound,
             laban.effort.space.direct, bartenieff.upper_lower]
  interactions:
    - { type: reinforces, source: gaze.target.hands, target: defensive_preparation }
    - { type: reinforces, source: laban.effort.flow.bound, target: restrained_action }
    - { type: constrains, source: laban.effort.flow.bound, target: follow_through }
  evidence_class: cpcs_proposed
```

## Saturation policy

A director should not stack semantically redundant controls merely because
they are available. The compiler may reduce redundant controls when A already
strongly expresses the same realization, B adds little, and provider attention
is limited. This must be logged as deterministic compiler behavior.

## Verification

`test_cross_framework_controls_preserve_framework_identity`.
