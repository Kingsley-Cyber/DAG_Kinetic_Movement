---
id: cpcs.mx.relative_motion
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §73, §74]
primary_route: cpcs/knowledge/06_body_motion/
secondary_routes:
  - cpcs/knowledge/11_blocking_screen_space/
interfaces: [cpcs.mx.spatial_state, cpcs.contact.interaction_lifecycle]
---

# RelativeMotion and Multi-Actor Roles

For multi-actor choreography, absolute positions are often less useful than
relative distance, velocity, heading, orientation, and phase.

## Relative motion

```yaml
relative_motion:
  subject: actor_A
  reference: actor_B
  distance:
    trend: decreasing
  relative_heading:
    trend: converging
  phase_relation:
    value: synchronized
```

Essential for: chase, fight, dance, conversation, passing, catching, group
movement.

## Multi-actor role semantics

Do not treat actors as independent motion graphs when the action is relational.

```text
leader · follower · target · initiator · responder · counterpart · observer
```

```yaml
interaction_roles:
  initiator: actor_A
  responder: actor_B
  target: actor_B
```

Then `A strikes → B reacts` becomes a causal coupled action rather than two
unrelated actions.

## Coupled timing

Two actors can be simultaneous, offset, counterphase, leader-follow, or
reaction-delayed.

```yaml
coordination:
  actor_A:
    phase: execution
  actor_B:
    phase_relation:
      type: delayed_response
      offset: relative
```

Do not force all synchronization into exact timestamps.

## Verification

`test_relative_motion_present_for_multi_actor`,
`test_roles_assigned_for_relational_action`,
`test_coupled_timing_not_forced_to_exact_timestamps`.
