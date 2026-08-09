---
id: cpcs.found.numeric.bilateral_side_semantics
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §5.1, §5.2, §5.3, SRC-001-U05]
primary_route: cpcs/knowledge/00_foundations/numerical_representation/
secondary_routes:
  - cpcs/knowledge/04_character_performance/facs/
  - cpcs/knowledge/06_body_motion/
interfaces: [motion_x_camera]
---

# Bilateral / Side-Indexed Semantics

## Principle

Use side-indexed structures whenever left and right are semantically
independent. Never compress `hands.left` / `hands.right` into a single
`hand_position` when side matters.

```json
{
  "hands": {
    "left":  { "trajectory": "...", "contact": "object_01" },
    "right": { "trajectory": "...", "contact": null }
  },
  "symmetry": { "state": "asymmetric", "score": 0.28 }
}
```

## `bilateral` semantics

Use `bilateral` **only** when the source or author explicitly describes a
coupled bilateral action. `bilateral` does not mean "average left and right".
For asymmetric behavior, preserve side-specific observations and derive
symmetry/asymmetry metadata (e.g. `coupling: symmetric, symmetry: 0.94`).

## FACS application

FACS (U05) is a descriptive, anatomically based system for visually
discernible facial movement (Action Units). It remains a **facial movement
description layer, not an emotion inference layer**.

- Canonical intensity scale: `facs_A_E` (discrete letters).
- If a detector emits continuous intensity, preserve the detector scale
  (`scale: detector_continuous, value: 0.73, range: [0,1]`).
- **Never silently map detector values to FACS A–E.**
- FACS events carry timing: `onset / apex / offset`, plus side, evidence
  class, confidence.

## Failure modes

- Left/right collapse destroys verification targets (left_right_error).
- Averaging asymmetric bilateral behavior hides the side that interacts.
- Treating AU detections as emotion labels violates the epistemic firewall.

## Verification

`test_left_right_not_collapsed`, `test_bilateral_not_averaged` (SRC-001 §26).
