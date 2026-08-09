---
id: cpcs.body_topology_support_bridge
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§31]
primary_route: cpcs/knowledge/06_body_motion/biomechanics/
secondary_routes:
  - cpcs/knowledge/06_body_motion/bartenieff/
  - cpcs/knowledge/09_force_physics/
interfaces: [motion_x_contact]
---

# Body Topology and Support Bridge

Bartenieff connectivity refers to relationships among body regions and
whole-body organization. To become operational, CPCS needs a body-topology
**bridge** — an anatomical/kinematic representation layer, **not** another
movement-analysis ontology.

## Required concepts

```text
body_region · joint · joint_chain · effector · support_region · core ·
proximal_segment · distal_segment · ipsilateral_pair · contralateral_pair ·
support_chain · load_path
```

## Support state

```yaml
support_state:
  base: { type: asymmetric, planted: { left: true, right: false } }
  load: { dominant_side: left }
  center_of_mass: { direction: lowered }
  transfer: { from: left_leg, through: [pelvis, torso], toward: right_arm }
```

Measurement of this state requires a declared pose/kinematic source and
uncertainty. This is a **CPCS anatomical representation**, not a claim that
Bartenieff itself defines this exact machine schema.

## Verification

`test_support_stability`, `test_trajectory_commitment` (support chain
preservation across an action).
