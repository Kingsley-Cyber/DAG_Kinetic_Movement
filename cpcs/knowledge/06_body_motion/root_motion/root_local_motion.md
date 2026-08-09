---
id: cpcs.mx.root_local_motion
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-003 §79, §80]
primary_route: cpcs/knowledge/06_body_motion/root_motion/
interfaces: [cpcs.mx.spatial_state, cpcs.mx.motion_realization]
---

# Root/Local Motion Separation and Trajectory History

Root trajectory and local body motion must be separately controllable. A
character can run forward while upper body rotates, or stand in place while
performing a large gesture. Motion Matching systems explicitly query both pose
and trajectory features, weighting trajectory separately from pose.

## Root vs local

```text
RootMotionPlan + LocalMotionPlan
```

should be separate but coordinated.

## Trajectory history and prediction

A single current position is inadequate for motion control. Motion Matching
explicitly uses trajectory samples at offsets in the past/future and pose
history to select motion.

```yaml
trajectory:
  history:
    required: true
  current:
    pose_ref: current
  prediction:
    horizon: relative
    samples:
      - early
      - middle
      - late
```

This is much stronger than one `trajectory` object.

## Verification

`test_root_local_separated`,
`test_trajectory_history_present`,
`test_prediction_horizon_present`.
