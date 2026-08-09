---
id: cpcs.mx.long_form_scheduler
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §103, §104, §105, §106]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/06_canonical/
interfaces: [cpcs.mx.continuity_state, cpcs.found.causal_event_semantics]
---

# Long-Form Scheduler, State Transition, and Constrained State Evolution

For multi-beat sequences, the compiler needs a stateful scheduler that
maintains actor state, object state, spatial state, support state, continuity
state, camera state, active contacts, and pending outcomes. A long-form motion
generator cannot independently solve every beat from scratch.

## State transition

```yaml
state_transition:
  from:
    support: bilateral
    object_holder: actor_A
    actor_relation: left_of
  event:
    type: release
  to:
    support: bilateral
    object_holder: none
    object_state: airborne
```

## Event causality with preconditions and postconditions

Every significant event should support:

```text
preconditions · trigger · effects · postconditions · failure_outcomes
```

```yaml
event:
  id: release_object
  preconditions:
    - object_held_by_actor
  trigger:
    type: hand_open
  effects:
    - remove_hold_constraint
  postconditions:
    - object_no_longer_attached
  failure:
    - grip_persists
```

## Constrained state evolution

The deepest architectural formulation:

```text
STATE_t + ACTION_t + CONTROL_t → STATE_t+1
```

where state contains: actor pose, actor root, support, contact, object
transforms, spatial relations, camera, continuity, phase.

The hierarchy (`scene → shot → beat → action → primitive`) organizes content.
The state-transition system governs execution. Both are required.

## Verification

`test_state_persists_across_beats`,
`test_event_preconditions_checked`,
`test_state_transition_explicit`.
