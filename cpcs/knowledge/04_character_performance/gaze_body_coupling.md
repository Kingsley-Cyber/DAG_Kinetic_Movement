---
id: cpcs.mx.gaze_body_coupling
kind: mechanism
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §76]
primary_route: cpcs/knowledge/04_character_performance/
secondary_routes:
  - cpcs/knowledge/06_body_motion/
interfaces: [cpcs.facs.descriptive_not_emotion]
---

# Gaze-Body Coordination

A motion can require eyes to target one thing while head follows partially,
torso follows delayed, and lower body remains oriented elsewhere. That is a
coordination pattern, not a single gaze direction.

## Coupling model

```yaml
gaze_body_coupling:
  gaze_target: actor_B
  head_follow: partial
  torso_follow: delayed
  lower_body_orientation: independent
```

This is particularly important for believable dialogue, surveillance, pursuit
and reaction shots.

## Verification

`test_gaze_body_coupling_present`,
`test_head_torso_follow_independent`.
