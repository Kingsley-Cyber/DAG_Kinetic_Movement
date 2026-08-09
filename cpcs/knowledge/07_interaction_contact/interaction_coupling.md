---
id: cpcs.mx.interaction_coupling
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-003 §71, §72]
primary_route: cpcs/knowledge/07_interaction_contact/
secondary_routes:
  - cpcs/knowledge/08_objects_affordances/
interfaces: [cpcs.contact.interaction_lifecycle, cpcs.mx.motion_realization]
---

# InteractionCoupling and Moving Targets

For a held object, actor hand, object transform, contact, and object response
should be one coupled execution relationship. Human-object interaction
generation explicitly models human motion, object motion, and contact as
interdependent rather than independent streams.

## Interaction coupling

```yaml
interaction_coupling:
  actor: A
  effector: right_hand
  object: hammer
  coupling:
    mode: grasped
  object_motion:
    source: actor_motion
  release_event:
    unlocks_object_motion: true
```

## Moving targets

A target can move while an actor reaches toward it. The MX model needs target
state, velocity, prediction horizon, and interception point.

```yaml
target:
  state: moving
  predicted_position:
    horizon: relative_time
  interaction:
    mode: interception
```

Examples: catch ball, hit moving target, grab moving object, follow another
actor. This is a distinct reasoning class from static reachability.

## Verification

`test_object_motion_coupled_to_actor`,
`test_release_unlocks_object_motion`,
`test_moving_target_prediction_present`.
