---
id: cpcs.mx.momentum_impulse
kind: mechanism
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §66]
primary_route: cpcs/knowledge/09_force_physics/
interfaces: [cpcs.force.fail_closed_dynamics, cpcs.mx.motion_realization]
---

# Momentum and Impulse

The MX model discusses acceleration and force, but a motion director often
needs momentum, impulse, angular momentum, deceleration, and energy transfer.
These are different from instantaneous force.

## Dynamic intent

For example, `heavy` may be visually realized through large momentum, rapid
momentum transfer, strong deceleration, visible recoil, and longer settling
rather than an arbitrary numeric force.

```yaml
dynamic_intent:
  momentum:
    qualitative: high
  impulse:
    qualitative: sharp
  angular_momentum:
    qualitative: high
  force_value:
    status: unspecified
```

This keeps dynamics conceptually correct without fabricating physical
measurements.

## Verification

`test_dynamic_intent_qualitative_not_fabricated`,
`test_momentum_consistent_with_action_class`.
