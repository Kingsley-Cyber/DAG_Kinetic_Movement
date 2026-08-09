---
id: cpcs.canonical.control_envelopes
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§24]
primary_route: cpcs/runtime/06_canonical/
secondary_routes:
  - cpcs/runtime/06_canonical/temporal_tracks/
interfaces: []
---

# Control Envelopes

Static labels are insufficient — performance qualities evolve through a
phrase. Support `state · transition · apex · recovery` rather than only
`value = X`.

## Canonical envelope

```json
{
  "control": "laban.effort.flow",
  "scope": { "actor": "A", "action": "counter" },
  "envelope": [
    { "phase": "anticipation", "value": "bound" },
    { "phase": "release", "transition": "bound_to_free" },
    { "phase": "action", "value": "free" },
    { "phase": "recovery", "value": "bound" }
  ]
}
```

This does **not** assert that every Laban factor has a universally correct
numerical trajectory. For qualitative controls, symbolic phase states are
preferable unless research establishes a defensible numeric representation.

## Envelope types

```text
categorical_state_envelope · ordinal_envelope ·
continuous_measurement_envelope · event_envelope · phase_envelope
```

Each must declare its semantic basis.

## Verification

`test_local_temporal_control_does_not_globalize`,
`test_temporal_order`.
