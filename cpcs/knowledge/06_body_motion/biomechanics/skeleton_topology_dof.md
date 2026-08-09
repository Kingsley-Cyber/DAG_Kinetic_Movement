---
id: cpcs.body.skeleton_topology
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §5]
primary_route: cpcs/knowledge/06_body_motion/biomechanics/
secondary_routes:
  - cpcs/knowledge/06_body_motion/root_motion/
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.body.retarget_contract
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.interchange_manifests
  - cpcs.found.timebase_systems
---

# Skeleton Topology, DoF, and Joint Limits

> **Source:** SRC-005 §5 — "Skeleton topology, degrees of freedom, and joint limits"

## Problem

A skeletal track is meaningful only relative to a declared topology and rest
configuration. Two characters can both have a joint called `shoulder_r` while
differing in parent hierarchy, local axes, rest orientation, segment length,
twist distribution, and degrees of freedom. Copying rotations between
non-identical skeletons produces semantic and geometric failures.

## Skeleton declaration

The schema stores:

```text
stable joint identifiers and parent relationships
rest transforms
local coordinate axes
rotational and translational degrees of freedom
segment lengths and optional mass/inertia estimates
skinning or deformation references
semantic regions (hand, forearm, torso, head, support foot)
retarget chains and end effectors
joint limits and preferred angles
virtual or stylized deformation controls that are not skeletal joints
```

A compact example:

```json
{
  "joint_id": "elbow_r",
  "parent": "upper_arm_r",
  "dof": ["flexion_extension", "pronation_supination_proxy"],
  "rotation_representation": "quaternion_xyzw",
  "limits": {
    "mode": "rig_specific",
    "flexion_extension_rad": [-0.05, 2.62],
    "soft_margin_rad": 0.12
  },
  "preferred_angle_rad": 0.35
}
```

Numerical ranges are illustrative, not universal clinical ranges.

## Three limit domains

| Domain | Meaning |
| --- | --- |
| `anatomical_reference` | evidence-based ranges for a particular human model or performer |
| `rig_safe` | what a production skeleton and skinning system can support without unacceptable deformation |
| `virtual_stylized` | deliberate nonhuman deformation (squash/stretch, lattice, blendshapes, segment scaling, key-shape) |

This separation corrects the unsafe simplification "increase human joint range
by 30% for superhuman motion." Directly extending an anatomical elbow, knee, or
spine limit can produce visually broken or injury-like poses. A photoreal human
rig keeps anatomical or rig limits. A stylized character may exceed the visible
human silhouette through a separate deformation layer while the underlying
skeleton remains within declared limits, or may declare itself a nonhuman
virtual skeleton with its own limits.

## Coupled constraints

Not all joints are independent ball joints. CPCS-MX can represent coupled
constraints such as scapular rhythm, patellar motion proxies, twist
distribution along a forearm, or a locked prop grip. These constraints should
be implemented in the solver or retarget adapter, not merely documented as
prose.

## Rest pose and topology versioning

A canonical motion file must reference a skeleton version and rest-pose hash.
Changing a rest pose can alter every local rotation while leaving the visible
pose similar. For agent workflows, skeleton metadata is retrieved with the
motion chunk. Dense joint data without topology is treated as incomplete.

## Boundary

This card defines topology declaration. It does not prescribe a universal
joint naming convention; it requires that joint identifiers be stable and
that their definitions be retrievable.
