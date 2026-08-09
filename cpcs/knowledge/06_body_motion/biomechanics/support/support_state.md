---
id: cpcs.mx.support_state
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §15, §16, §64, §65, §68]
primary_route: cpcs/knowledge/06_body_motion/biomechanics/support/
secondary_routes:
  - cpcs/knowledge/06_body_motion/biomechanics/
interfaces: [cpcs.body_topology_support_bridge, cpcs.mx.motion_realization]
---

# SupportState

Support should be explicit rather than scattered across contact, balance and
weight shift. SupportState is a core whole-body representation.

## Canonical structure

```json
{
  "support_state": {
    "actor": "actor_A",
    "contacts": {
      "left_foot": "planted",
      "right_foot": "planted"
    },
    "base_of_support": "bilateral",
    "load_distribution": {
      "left": "dominant",
      "right": "secondary"
    },
    "center_of_mass": {
      "relation": "inside_base"
    },
    "center_of_pressure": {
      "movement": "forward"
    },
    "ground_reaction": {
      "status": "inferred"
    },
    "transfer": {
      "from": "rear_leg",
      "to": "right_arm",
      "path": ["pelvis", "torso", "shoulder"]
    }
  }
}
```

COM alone is insufficient. For standing balance, COM, BOS, and COP interact;
postural adjustments actively manipulate these relationships.

## Dynamic balance state

Static COM-inside-BOS is not enough for walking, running, jumping or
directional changes.

```text
stable → controlled_instability → transition → recovery → loss_of_balance
```

```yaml
balance_state:
  state: controlled_instability
  phase: initiation
  recovery_plan:
    required: true
```

## Surface and friction

Support is not determined solely by contact. Walking, stopping, sliding,
pushing and landing depend on surface conditions.

```yaml
surface:
  id: wet_floor
  support: yes
  friction:
    class: low
  slope:
    status: unknown
```

Do not invent a coefficient of friction unless the source or simulation
supplies one.

## Support verification

For a planted foot:

```text
foot_height ≈ support_surface
foot_velocity ≈ 0
contact persists during support interval
```

Do not use visual prose as the acceptance test.

```json
{
  "verification_expectation": {
    "target": "left_foot_support",
    "metrics": ["foot_height_error", "foot_velocity"],
    "threshold": {
      "status": "experimental",
      "foot_velocity_max": null,
      "height_error_max": null
    },
    "verdict": "fail_if_exceeded"
  }
}
```

Thresholds must be calibrated against the intended capture/generation regime.

## Verification

`test_support_contact_persists`,
`test_com_inside_bos_when_stable`,
`test_foot_velocity_during_support`.
