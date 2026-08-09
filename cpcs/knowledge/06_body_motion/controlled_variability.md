---
id: cpcs.mx.controlled_variability
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-003 §88]
primary_route: cpcs/knowledge/06_body_motion/
secondary_routes:
  - cpcs/knowledge/06_body_motion/biomechanics/
interfaces: [cpcs.mx.constraint_feasibility]
---

# Controlled Variability

Realistic motion is not perfectly identical on every repetition. Motor-control
research describes "repetition without repetition": task outcomes can remain
stable while kinematic details vary.

## Variation policy

```yaml
variation_policy:
  invariant:
    - target_contact
    - actor_identity
  variable:
    - elbow_path
    - torso_micro_adjustment
  variability:
    level: moderate
```

This is a major anti-overconstraint principle. Distinguish required invariant
from allowed variation.

## Verification

`test_invariant_vs_variable_separated`,
`test_variability_level_present`.
