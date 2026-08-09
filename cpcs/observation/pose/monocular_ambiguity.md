---
id: cpcs.obs.pose.monocular_ambiguity
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §1.2, SRC-001-U02, SRC-001-U03]
primary_route: cpcs/observation/pose/
secondary_routes:
  - cpcs/knowledge/00_foundations/uncertainty/
interfaces: [motion_x_camera]
---

# Monocular 3D Pose Ambiguity

## Principle

Monocular 3D pose estimation is fundamentally ill-posed: multiple 3D
configurations can project to similar 2D observations (depth ambiguity and
occlusion; explicitly stated by 2026 CVPR work per SRC-001 §1.2).

Therefore CPCS must not turn an estimated 3D pose into false exact physical
truth. Estimated poses carry `acquisition: detected/estimated` and their
epistemic state honestly (see the two-axis evidence model in
`knowledge/00_foundations/uncertainty/`).

## External support

- Human3.6M (U02): millions of 3D poses across four viewpoints — supports
  structured pose representation but not a universal authoring vocabulary.
- VideoPose3D (U03): temporal modeling of pose sequences — frames are not
  independent; temporal context improves estimation.

## Open question

How CPCS should represent uncertainty when multiple 3D pose hypotheses are
equally plausible (SRC-001 §26 Q10 — see `research/gaps/`).

## Applies when

Any observation pipeline stage consumes monocular video.

## Failure mode

Treating a single-hypothesis pose estimate as measured ground truth in
verification or world-model state.
