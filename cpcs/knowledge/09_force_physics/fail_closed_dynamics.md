---
id: cpcs.physics.force.fail_closed_dynamics
kind: doctrine
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §1.2, §8.2, §8.3, §24, SRC-001-U09, SRC-001-U11]
primary_route: cpcs/knowledge/09_force_physics/
secondary_routes:
  - cpcs/knowledge/09_force_physics/perceived_weight/
  - cpcs/knowledge/00_foundations/uncertainty/
interfaces: [motion_x_physics, object_x_physics]
---

# Fail-Closed Dynamics Doctrine

## Doctrine

Force, momentum, torque, impulse, mass, and friction have precise physical
meanings. Recovering them from ordinary monocular video requires assumptions,
additional sensing, or physics-informed estimation. Therefore:

> **`force` and related quantities are fail-closed by default: they are
> `estimated` under a declared model, or `unknown`/`unobservable` — never
> silently promoted from visual observation to measured fact.**

## External support

- Monocular joint estimation of 3D motion, contact, and force is possible
  (U09) but is **estimation under a model**, not direct measurement.
- 2026 video inverse-dynamics literature: numerical differentiation strongly
  amplifies pose noise toward physical quantities.
- Mechanics fundamentals (U11) define the quantities themselves.

## Safe force representation

With declared assumptions (`known_or_estimated_mass`, `known_contact`,
`camera_geometry_estimated`):

```json
{
  "force": {
    "status": "estimated",
    "vector": { "value": [0.0, 0.0, 0.0], "unit": "N", "frame": "world" },
    "method": "physics_informed_video_estimator",
    "confidence": 0.61,
    "assumptions": ["known_or_estimated_mass", "known_contact", "camera_geometry_estimated"]
  }
}
```

Without them:

```json
{ "force": { "status": "unobservable",
             "reason": "monocular_video_without_force_or_mass_constraints" } }
```

## Do not infer force from speed alone

A fast movement is not equivalent to high measured force. See the epistemic
firewall card for the expressive-label boundary (`effort=strong` ≠ 500 N).

## Applies when

Any dynamics field is authored, observed, or compiled. Force/torque inference
from ordinary video is a **P2 experiment** before becoming authoritative.

## Failure mode

Silent certainty inflation: downstream verification treats estimated forces
as ground truth, corrupting physics verification.
