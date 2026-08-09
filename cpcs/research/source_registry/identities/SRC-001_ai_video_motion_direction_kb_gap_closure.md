---
id: SRC-001
title: CPCS AI Video Motion Direction — Research Closure
version: v1.1
epistemic_class: authored
status: registered
---

# Source Identity — SRC-001

| Field | Value |
| --- | --- |
| source_id | SRC-001 |
| title | CPCS AI Video Motion Direction — Research Closure |
| file | `Research_distillation_folder/01_AI_VIDEO_MOTION_DIRECTION_KB_GAP_CLOSURE_RESEARCH.md` |
| version | research closure v1.1 (continuity/causality closure applied) |
| research_family | motion direction / canonical representation / compiler contracts |
| lines | 2503 |
| sections | 29 numbered sections |
| epistemic_class | authored (CPCS-internal closure analysis; cites 16 external sources) |

## Scope

Motion, phase, bilateral semantics, dynamics, interaction, camera/image
formation, style, complexity, representation carriers, compiler behavior,
verification, and (v1.1) continuity/persistence/occlusion and causal event
structure.

## Known status limitations (self-declared by source)

- The referenced frozen KB package `CPCS_AI_Video_Motion_Direction_KB_v1.0.0.zip`
  was NOT supplied to the closure process; package-by-package coverage claims
  are marked **not verifiable from the supplied files**.
- The continuity/causality objects (`ContinuityState`, `StateTransition`,
  `OcclusionInterval`, `PersistenceConstraint`, `CausalEvent`) are **proposed
  CPCS representations**, not externally established ontologies.

## Primary/authoritative sources cited (source_units SRC-001-U01 … U16)

1. U01 — Loper et al., SMPL: A Skinned Multi-Person Linear Model, SIGGRAPH Asia 2015
2. U02 — Ionescu et al., Human3.6M, IEEE TPAMI 2014
3. U03 — Pavllo et al., 3D Human Pose Estimation in Video (VideoPose3D), CVPR 2019
4. U04 — Zhou et al., On the Continuity of Rotation Representations in Neural Networks, CVPR 2019
5. U05 — Paul Ekman Group, Facial Action Coding System
6. U06 — McNeill Lab (U. Chicago), Gesture Annotation / Coding Manual
7. U07 — Kroemer et al., Hierarchical Skills for Multi-Phase Manipulation, ICRA 2015
8. U08 — Hakala & Häkkinen, Contact Points in Human–Object Interaction (IR cameras), Frontiers in Robotics and AI
9. U09 — Li et al., Estimating 3D Motion and Forces of Person-Object Interactions from Monocular Video, 2019
10. U10 — OpenCV Camera Calibration documentation
11. U11 — OpenStax mechanics (force, friction, angular momentum)
12. U12 — Runway Gen-4 Video Prompting Guide + Image-to-Video prompting guidance
13. U13 — Google DeepMind, How to create effective prompts with Veo 3
14. U14 — Kling AI Camera Control Guide
15. U15 — Singh et al., The Structured Output Benchmark, 2026
16. U16 — Yang et al., StructEval, TMLR 2026

## Lineage

- Distilled: 2026-08-08, CPCS Research Distillation Agent
- Ledger: `cpcs/research/distillation/ledger/01_ai_video_motion_direction_kb_gap_closure.md`
- Referenced but absent: `Pasted markdown(9).md` (architectural critique that
  motivated the v1.1 continuity additions) — not in repository.
