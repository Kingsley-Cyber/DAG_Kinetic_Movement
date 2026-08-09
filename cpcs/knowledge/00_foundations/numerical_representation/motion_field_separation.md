---
id: cpcs.found.numeric.motion_field_separation
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §3.2, §20.3]
primary_route: cpcs/knowledge/00_foundations/numerical_representation/
secondary_routes:
  - cpcs/knowledge/06_body_motion/kinematics/
  - cpcs/knowledge/09_force_physics/
interfaces: [motion_x_physics]
---

# Motion Quantity Field Separation

## Principle

`speed`, `amplitude`, `intensity`, `effort`, and `force` must **never** be
aliases of one another:

| Field | Meaning |
| --- | --- |
| `speed` | temporal rate of movement |
| `amplitude` | spatial/angular extent |
| `acceleration_profile` | how velocity changes through time |
| `effort` | expressive movement quality (Laban sense) — not Newtons |
| `force` | physical quantity requiring measurement, estimation under a declared model, or `unknown` |

## Applies when

Any canonical motion object (`MotionEvent`) semantics block is authored,
resolved, or compiled.

## Avoid when

— (unconditional; schema-level rule)

## Failure modes

- A fast movement read as high force (speed ≠ force).
- Expressive labels (`heavy`, `explosive`) emitted into physical fields.
- Providers receiving one blended "intensity" scalar that erases which
  dimension was actually directed.

## Verification

Schema validation: the five fields are distinct keys; cross-population from
one to another without a labeled transform is rejected.

## Primary versus derived tracks (SRC-005 §3)

CPCS-MX differentiates **authoritative tracks** from **derived tracks**. If
root position is authoritative, velocity and acceleration are calculated from
it under a specified filter. Maintaining two incompatible authoritative
versions of the same quantity creates an overconstrained system. This extends
the field-separation principle: not only must fields be semantically distinct,
but each field must declare which track is authoritative.

Recommended authority order:

```text
locked event timing
→ locked contacts and support
→ locked root trajectory
→ locked key joint targets
→ style and expressive fields
→ generated in-betweens
→ secondary simulation
```

This order is configurable. A physics-first workflow may instead lock masses
and contacts and allow the root path to emerge. See
`cpcs.found.layer_architecture` for the full 14-layer stack.
