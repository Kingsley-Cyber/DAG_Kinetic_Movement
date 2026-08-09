---
id: cpcs.body.superhuman_transform
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §19]
primary_route: cpcs/knowledge/06_body_motion/root_motion/
secondary_routes:
  - cpcs/knowledge/16_style_visual_language/
  - cpcs/knowledge/06_body_motion/biomechanics/
interfaces:
  - cpcs.style.anime_sakuga
  - cpcs.found.exactness_taxonomy
  - cpcs.mx.style_mechanics
  - cpcs.body.skeleton_topology
---

# Superhuman Motion as Constrained Transformation

> **Source:** SRC-005 §19 — "Superhuman motion as constrained transformation"

## The wrong model

A global "2.5x strength" or "1.5x speed" parameter is too coarse. It can
shorten actions until they become unreadable, break contacts, create
impossible joint velocities, desynchronize effects, and eliminate
character-specific timing. Superhuman motion should be a **phase- and
domain-specific transformation** applied to a coherent base action.

## Transformation vector

```json
{
  "superhuman_transform": {
    "scope": "virtual_only",
    "temporal": {
      "preparation_scale": 0.82,
      "execution_scale": 0.55,
      "recovery_scale": 1.20,
      "hang_time_scale": 1.65
    },
    "spatial": {
      "root_displacement_scale": 1.80,
      "reach_scale": 1.15,
      "arc_height_scale": 1.45
    },
    "dynamics": {
      "gravity_scale": 0.68,
      "virtual_actuator_scale": 2.4,
      "impact_impulse_scale": 1.9,
      "environment_response_scale": 2.8
    },
    "graphic": {
      "deformation_scale": 1.35,
      "smear_strength": 0.70,
      "effect_density": 0.65
    },
    "invariants": [
      "action_order",
      "takeoff_contact",
      "landing_target",
      "screen_direction",
      "hero_silhouette_at_apex"
    ]
  }
}
```

## Gravity and hang time

Reducing gravity changes the entire ballistic arc, not only a single frame. A
compiler can solve the required takeoff velocity for a desired apex and landing
time under the virtual gravity vector. If an artist wants an impossible pause
at the apex, the score marks a `time_suspension` or `graphic_hold` rather than
pretending it follows ordinary ballistics.

## Momentum-defying pivots

A sudden midair direction change requires one of the following explanations:

```text
contact with a surface or object
propulsion or energy effect
aerodynamic or nonhuman capability
camera-relative illusion
explicit cartoon-physics discontinuity
```

The score declares which explanation is intended.

## Virtual capacity profile

A character has a declared capacity profile separate from any real performer:

```yaml
virtual_capacity:
  morphology: nonhuman_humanoid
  joint_limit_domain: rig_specific
  max_virtual_torque_scale: 2.4
  gravity_tolerance: 0.6
  impact_resilience: 3.0
  aerial_control: enabled
  injury_model: cinematic_none
```

This prevents an agent from translating virtual parameters into unsafe physical
rehearsal.

## Design rule

Superhuman speed often needs more anticipation, a held key, a camera setup, or
time dilation — not less. The execution can be physically fast while the
presentation allocates screen time for the audience to understand the event.
Stage time and presentation time may differ through retiming and editing
tracks.

## Boundary

The transformation vector applies to virtual characters only. It does not
define real-world athletic performance capacity. The `invariants` list
prevents the transform from breaking action readability or causal order.
