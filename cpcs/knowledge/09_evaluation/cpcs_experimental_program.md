---
id: cpcs.knowledge.cpcs_experimental_program
kind: experiment_design
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §24-25, Appendix D.5-D.6]
primary_route: cpcs/knowledge/09_evaluation/
interfaces:
  - cpcs.knowledge.cpcs_evaluation_framework
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.evaluation.video_observation_graph
---

# CPCS Experimental Program

> Distilled from CPCS paper §24-25 and Appendix D.5-D.6. Defines 6 core
> hypotheses, an 8-condition factorial ablation, a 10-task evaluation suite,
> metric arbitration policy, and ablation protocol.

## 6 core hypotheses

| ID | Hypothesis | Test |
| --- | --- | --- |
| H1 | Structured temporal controls improve action timing | Ablation: text-only vs structured score |
| H2 | Affect/expression separation improves facial legibility | Ablation: VAC-only vs VAC+FACS |
| H3 | Laban variation produces perceptually distinct motion | Human rating of Laban-varied walks |
| H4 | Phase/contact improves physical plausibility | Foot skating, contact timing, collision rate |
| H5 | Decoupled camera/performer improves both | Ablation: coupled vs decoupled camera |
| H6 | RAG with provenance improves retrieval accuracy | Ablation: flat RAG vs evidence-labeled RAG |

## 8-condition factorial ablation

| Condition | Text | Structured | FACS | Laban | Phase | Contact | Camera decoupled | RAG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | ✓ | | | | | | | |
| +Structured | | ✓ | | | | | | |
| +FACS | | ✓ | ✓ | | | | | |
| +Laban | | ✓ | | ✓ | | | | |
| +Phase+Contact | | ✓ | | | ✓ | ✓ | | |
| +Camera | | ✓ | | | | | ✓ | |
| +RAG | | ✓ | | | | | | ✓ |
| Full | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

For each condition: keep identity references, base prompt, seed set, model
version, shot length, and camera plan fixed where possible. Report both mean
performance and candidate variance.

## What Full CPCS should improve (beyond quality)

- Event timing accuracy
- Revision locality (change one note without damaging unrelated tracks)
- Agreement between independent directors about instruction compliance
- Action identity preservation while expressive controls vary
- Fewer generations required to obtain an approved take

## Metric arbitration (6-level lexicographic policy)

No single scalar decides whether a shot is correct. CPCS uses a gated policy:

1. **Safety and rights gates** — prohibited identity use, unsafe procedure,
   unlicensed assets → immediate fail
2. **Hard continuity and contact gates** — missing actor, wrong prop,
   impossible geography, prohibited collision → fail
3. **Control compliance** — facial, motion, event, camera constraints must
   meet specified tolerances
4. **Physical plausibility** — support, slip, penetration, timing, dynamics
   evaluated jointly
5. **Visual and identity quality** — artifacts, temporal stability, likeness,
   style
6. **Dramatic effectiveness** — director, editor, movement expert, audience
   judgments rank acceptable candidates

This ordering prevents a photorealistic but incorrectly staged clip from
outranking a slightly less polished clip that satisfies the shot's meaning.

## 7-condition ablation protocol (Appendix D.6)

| Condition | Components |
| --- | --- |
| T | Text prompt only |
| T+A | Text + affect trajectory |
| T+A+F | + FACS/gaze |
| T+A+L | + Laban without explicit mechanics |
| T+M | Text + motion/contact controls |
| T+A+F+L+M | Integrated performance score |
| Full CPCS | Integrated performance + camera + audio + RAG + verification |

## 10-task evaluation suite

1. Dialogue close-up with concealed emotion
2. Expressive walk (fast walk concealing panic)
3. Controlled fight beat (2 actors)
4. Product reveal UGC (9:16)
5. Anime-style superhuman transformation
6. Multi-actor scene with eyeline
7. Camera-driven reveal (dolly-in triggered by recognition)
8. Laban-varied locomotion (same path, different qualities)
9. Audio-synchronized action (impact on beat)
10. Marketing variant plan (same hook, different product)

Each task exercises a different combination of control domains. Tasks span
realistic, stylized, and marketing contexts.
