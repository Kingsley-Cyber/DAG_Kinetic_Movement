---
id: cpcs.mx.material_response
kind: mechanism
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §22, §23]
primary_route: cpcs/knowledge/17_vfx_secondary_motion/
interfaces: [cpcs.found.causal_event_semantics, cpcs.mx.motion_realization]
---

# MaterialResponse and SecondaryMotion

Secondary motion is not enough. Interactions with materials/environment need a
causal response object that binds effects to events.

## MaterialResponse

```json
{
  "material_response": {
    "material": "water",
    "trigger": { "event": "foot_contact" },
    "origin": { "bind_to": "contact_site" },
    "immediate_response": ["local_displacement", "splash"],
    "secondary_response": ["ripples"],
    "persistence": { "mode": "decay" }
  }
}
```

This turns `splash` from arbitrary decorative VFX into a consequence of an
event. The same pattern applies to: dust, mud, snow, sand, cloth, hair, rope,
debris, smoke, liquid, glass.

## SecondaryMotion contract

```json
{
  "secondary_motion": {
    "asset": "coat",
    "driver": "torso_turn",
    "behavior": {
      "lag": "moderate",
      "overshoot": "slight",
      "damping": "natural"
    },
    "constraints": {
      "attached_at": ["left_shoulder", "right_shoulder"],
      "avoid_body_interpenetration": true
    }
  }
}
```

Exact simulation parameters can remain in a simulation artifact rather than
canonical semantic IR.

## Verification

`test_material_response_bound_to_event`,
`test_secondary_motion_origin_at_contact_site`,
`test_response_persistence_mode`.
