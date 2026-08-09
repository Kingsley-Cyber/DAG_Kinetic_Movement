---
id: cpcs.mx.typed_primitive_taxonomy
kind: vocabulary
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §4, §5]
primary_route: cpcs/knowledge/06_body_motion/action_primitives/
interfaces: [cpcs.mx.action_template]
---

# Typed Primitive Taxonomy

The existing primitive list mixes fundamentally different semantic classes.
Do not make these peer members of one `primitive` enum.

## Primitive

An operation that produces a movement:

```text
translate · rotate · reach · retract · shift_weight · grasp · release ·
jump · land · turn · redirect · stabilize · oscillate · gesture · gaze_shift
```

## Modifier

A property/process applied to motion:

```text
accelerate · decelerate · direct · curved · large_amplitude ·
small_amplitude · fast_onset · slow_onset
```

## Phase

A temporal organization:

```text
anticipation · initiation · acceleration · apex · contact ·
deceleration · follow_through · recovery
```

## Interaction state/event

```text
near_contact · contact · impact · support · grasp · release ·
separation · collision
```

## Support/stability behavior

```text
plant · brace · stabilize · transfer_support
```

## Primitive applicability

Every reusable primitive needs operational knowledge. Example:

```yaml
primitive:
  id: shift_weight
  meaning:
    concise: transfer support/load between body regions
  applies_when:
    - locomotion_initiation
    - directional_change
    - grounded_strike
    - landing_absorption
    - push_pull
    - balance_recovery
  less_relevant_when:
    - fully_airborne
    - isolated_facial_action
  modifies:
    - support_state
    - center_of_mass_relation
    - root_motion
    - downstream_chain_behavior
  visible_expectations:
    - support changes before or during action
  contraindications:
    - no_support_available
  verification:
    - support_transition
    - root_com_consistency
```

The purpose is to move primitive selection out of the model's private prior
knowledge and into retrievable research/application knowledge.

## Verification

`test_primitive_typed_correctly`,
`test_applicability_contraindication_consistent`.
