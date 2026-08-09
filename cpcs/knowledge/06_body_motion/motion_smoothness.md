---
id: cpcs.mx.motion_smoothness
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §85, §86, §87]
primary_route: cpcs/knowledge/06_body_motion/
secondary_routes:
  - cpcs/knowledge/06_body_motion/trajectories/
interfaces: [cpcs.canonical.temporal_coupling]
---

# Motion Smoothness, Path Geometry, and Timing Profiles

Do not collapse smoothness into one metric. At least distinguish position
continuity, velocity continuity, acceleration continuity, jerk continuity, and
semantic continuity.

## Smoothness levels

A movement can be geometrically smooth but semantically wrong (e.g., hand
trajectory smooth but contact occurs too early). Verification should identify
which continuity layer failed.

## Path geometry

Trajectory is not only position + velocity. For directing: straight, arc,
spiral, hook, S-curve, approach-and-retreat can matter.

```yaml
path_geometry:
  family: arc
  curvature:
    qualitative: moderate
  direction_change:
    count: 1
```

Avoid exact curvature unless measured or authored.

## Timing profile

Two actions can have identical duration but different temporal profiles:
constant, early burst, late burst, ease-in, ease-out, symmetric pulse,
hold-release.

```yaml
timing_profile:
  duration: relative
  velocity_profile: late_burst
```

Especially important for "snappy", "deliberate", "hesitant", and "explosive."

## Verification

`test_smoothness_level_identified_on_failure`,
`test_path_geometry_present_when_curved`,
`test_timing_profile_distinct_from_duration`.
