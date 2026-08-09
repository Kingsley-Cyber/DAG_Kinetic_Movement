---
id: cpcs.found.numeric.rotation_representation_contract
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §4, SRC-001-U01, SRC-001-U04]
primary_route: cpcs/knowledge/00_foundations/numerical_representation/
secondary_routes:
  - cpcs/knowledge/06_body_motion/biomechanics/joint_kinematics/
  - cpcs/knowledge/12_camera_image_formation/camera_geometry/orientation/
interfaces: [motion_x_camera]
---

# Rotation Representation Contract

## Principle

Orientation values are meaningless without a declared convention. The
semantic IR stays representation-independent but MUST declare representation,
convention, frame, and units.

Canonical semantic shape:

```json
{
  "rotation": {
    "representation": "quaternion",
    "convention": "wxyz",
    "frame": "parent_local",
    "unit": "unitless",
    "value": [0.9239, 0.0, 0.3827, 0.0]
  }
}
```

Authored (human-readable) shape compiles to the above:

```yaml
rotation:
  axis: y
  angle: 45deg
  frame: parent_local
```

## External support

- SMPL (U01): pose parameters are joint rotations; geometry via skinning —
  supports structured pose/motion representation, but does not establish one
  universal CPCS authoring vocabulary (that remains a CPCS design decision).
- Zhou et al. (U04, CVPR 2019): ≤4D Euclidean rotation representations (Euler,
  quaternion) are discontinuous for neural-network learning; continuous 5D/6D
  representations are better for learned rotation regression.

## Key boundary

6D rotation is a valid **ML adapter representation only**. It must not
replace the semantic rotation contract.

## Validation rules (reject or quarantine)

- undeclared axis convention
- undeclared frame
- malformed quaternion
- quaternion norm outside tolerance
- Euler angles without axis order
- angle units omitted when not obvious from schema

`wxyz` vs `xyzw` cannot be inferred safely — it must be declared.
