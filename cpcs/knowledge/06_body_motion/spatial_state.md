---
id: cpcs.mx.spatial_state
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §7, §8, §9]
primary_route: cpcs/knowledge/06_body_motion/
secondary_routes:
  - cpcs/knowledge/11_blocking_screen_space/
interfaces: [cpcs.found.coordinate_systems, cpcs.mx.action_template]
---

# SpatialState

SpatialState is distinct from coordinate frames. A coordinate frame answers
where a point is numerically. SpatialState answers how entities are arranged
for the director.

## Required distinction

```text
numeric:
    actor_B.position = [0.4, 1.2, -2.8]

semantic:
    actor_B is right_of actor_A
    actor_B remains behind table
    weapon remains between actors
    hand passes outside face
    actor remains above water
```

## Canonical structure

```json
{
  "spatial_state": {
    "frame": "shot_world",
    "relations": [
      {
        "subject": "actor_B",
        "predicate": "right_of",
        "object": "actor_A",
        "persistence": "shot"
      },
      {
        "subject": "actor_A",
        "predicate": "above_surface",
        "object": "water"
      }
    ],
    "action_axes": [
      {
        "id": "fight_axis",
        "orientation": "actor_relative"
      }
    ]
  }
}
```

## Direction must carry a reference frame

Never emit ambiguous `forward`, `right`, `left`, `up`, `down`, `advance`,
`retreat` without a frame.

```json
{
  "direction": {
    "value": "forward",
    "frame": "actor_root"
  }
}
```

Possible semantic frames: `world`, `camera`, `screen`, `actor_root`, `target`,
`surface`, `object`. This is separate from the numeric coordinate frame.

## ActionAxis

Many cinematic interactions are governed by a semantic axis rather than raw
coordinates: fight axis, conversation axis, travel direction, screen-left/right
relationship, approach vector, retreat vector, camera-to-subject axis.

```json
{
  "action_axis": {
    "id": "fight_axis",
    "reference": "actor_A_to_actor_B",
    "persistence": "shot",
    "allow_crossing": false
  }
}
```

This provides a deterministic place for "don't cross the line" style directing
constraints.

## Verification

`test_spatial_relation_persistence`,
`test_direction_frame_present`,
`test_axis_crossing_policy_enforced`.
