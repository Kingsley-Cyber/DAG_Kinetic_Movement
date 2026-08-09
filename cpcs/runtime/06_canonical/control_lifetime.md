---
id: cpcs.mx.control_lifetime
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §13]
primary_route: cpcs/runtime/06_canonical/
secondary_routes:
  - cpcs/runtime/06_canonical/field_policies/
interfaces: [cpcs.canonical.control_scope, cpcs.canonical.control_envelopes]
---

# ControlLifetime

A control without a lifetime is ambiguous — the same `recoil` value could mean
a brief recovery phase or a persistent state across the entire shot.

## Canonical lifetime object

```json
{
  "control_lifetime": {
    "control": "recoil",
    "scope": { "actor": "A", "action": "strike", "phase": "recovery" },
    "start": "contact_event",
    "end": "stabilization_event",
    "max_duration": "relative_to_action"
  }
}
```

## Lifetime types

```text
event_lifetime     — bound to a specific event onset/offset
phase_lifetime      — bound to an action phase
action_lifetime     — bound to an action template instance
shot_lifetime        — bound to a shot
scene_lifetime       — bound to a scene
persistent           — until explicitly revoked
```

## Inheritance

Unspecified lifetimes inherit from the enclosing execution context rather than
becoming implicit persistent controls.

## Verification

`test_lifetime_does_not_leak` — a brief recoil must not persist into unrelated
later action. `test_lifetime_boundary_alignment` — lifetime must start/end at
meaningful events, not arbitrary timestamps.
