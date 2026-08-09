---
id: cpcs.mx.retarget_contract
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §24, §25, §67]
primary_route: cpcs/knowledge/06_body_motion/root_motion/
secondary_routes:
  - cpcs/knowledge/06_body_motion/biomechanics/
interfaces: [cpcs.body_topology_support_bridge, cpcs.mx.motion_realization]
---

# RetargetContract

Mechanical validity is insufficient. A retarget is successful only if required
semantic invariants survive.

## Required invariants

```json
{
  "retarget_contract": {
    "required_invariants": [
      "action_identity",
      "actor_identity",
      "side",
      "target_relation",
      "phase_order",
      "contact_intent"
    ],
    "adaptable": [
      "joint_angles",
      "trajectory_amplitude",
      "root_height"
    ]
  }
}
```

## Reachability policy

When a target is unreachable, the system must not improvise.

```json
{
  "retarget_failure_policy": {
    "condition": "target_unreachable",
    "allowed_adjustments": [
      "bounded_root_translation",
      "bounded_stance_adjustment"
    ],
    "forbidden": ["change_target", "change_side"],
    "otherwise": "fail"
  }
}
```

## Inertia and mass distribution

Two characters with identical joint angles can look very different because
segment lengths, mass distribution, limb proportions, COM, and moment of
inertia differ.

```text
mass_profile · inertial_profile · center_of_mass_profile
```

when dynamics or grounded motion are being modeled. If unavailable:
`status: unknown`, not an invented human default.

## Verification

`test_semantic_invariants_survive_retarget`,
`test_unreachable_target_fails_not_improvises`,
`test_no_silent_target_substitution`.
