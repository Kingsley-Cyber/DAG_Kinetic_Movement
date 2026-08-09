---
id: cpcs.knowledge.cpcs_evaluation_framework
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §24]
primary_route: cpcs/knowledge/09_evaluation/
interfaces:
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.evaluation.video_observation_graph
---

# CPCS Evaluation Framework

> Distilled from CPCS paper §24. Defines 6 evaluation families with detailed
> metrics per domain, plus a multi-objective scorecard with hard gates.

## 6 evaluation families

### 1. Control compliance
- AU event timing error (onset, apex, offset)
- AU intensity MAE
- Laban quality agreement (per dimension)
- Phase marker agreement
- Contact event timing
- Camera trajectory RMSE
- Duration error
- Aspect ratio compliance

### 2. Temporal/causal
- Action order agreement (Kendall tau)
- Causal edge agreement
- Reaction delay error
- Beat boundary F1
- Temporal compositionality (TC-Bench style)
- Event-time error for cuts, gaze changes, product reveal, contact, reaction, CTA

### 3. Physical plausibility
- Foot skating rate
- Support violation (floating, clipping)
- Center-of-mass over support base
- Joint angle limits violation
- Contact force direction agreement
- Momentum conservation (approximate)
- Collision penetration

### 4. Appearance/identity
- Face identity similarity (ArcFace or equivalent)
- Body identity consistency
- Wardrobe/prop consistency
- Identity preservation score (minimum threshold)

### 5. Semantic/cinematic
- Director study: does the shot communicate the intended beat?
- Viewer study: naive viewer comprehension
- Affect legibility (can a reviewer identify the intended emotion?)
- Shot scale agreement
- Screen direction agreement
- Camera motion type agreement

### 6. General quality
- FVD (Fréchet Video Distance)
- FVM (Fréchet Video Motion Distance)
- CLIP score (text-image alignment)
- Human preference rating

## Multi-objective scorecard with hard gates

No single aggregate score. Instead:

```text
HARD GATES (must pass):
  - identity_preservation >= 0.90
  - contact_timing_error_s <= 0.15
  - foot_skating_rate <= 0.05
  - action_order_tau >= 0.80
  - duration_error_s <= 0.5

SOFT METRICS (reported, ranked):
  - AU apex timing MAE
  - Laban quality agreement
  - camera trajectory RMSE
  - FVD, FVM, CLIP
  - director study score
  - viewer comprehension
```

## Experimental program (6 hypotheses)

| Hypothesis | Test |
| --- | --- |
| H1: Structured temporal controls improve action timing | Ablation: text-only vs structured score |
| H2: Affect/expression separation improves facial legibility | Ablation: VAC-only vs VAC+FACS |
| H3: Laban variation produces perceptually distinct motion | Human rating of Laban-varied walks |
| H4: Phase/contact improves physical plausibility | Foot skating, contact timing, collision rate |
| H5: Decoupled camera/performer improves both | Ablation: coupled vs decoupled camera |
| H6: RAG with provenance improves retrieval accuracy | Ablation: flat RAG vs evidence-labeled RAG |

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

## 10-task suite

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

## Lab scorecard as empirical instantiation (SRC-010 EXTEND)

The Prompt Lab is the only empirical instantiation of this framework to date
(`cpcs.lab.architecture`):

- **4 manual dims** (realism · skin · motion · adherence, 1–5, single
  observer) approximate the 6 metric families by eye — the same objectives,
  no tooling.
- **Hard-gate analog:** v006 passed 0 failures on `validate_kinematics.py`
  (8 check families: frame math, velocity vectors, position/velocity
  coherence, contact geometry, closing speed, foot contacts, monotonic time,
  near-miss clearance); canon documents carry verification blocks
  (contact_time_error_ms ≤ 50, contact_distance_m ≤ 0.05) for the paper's
  gates (contact_timing_error_s ≤ 0.15, etc.).
- **Ablation analog:** the lab's 7-condition style ablation and the one-lever
  A/B discipline (e002 = skin microtexture, the sole isolated_confirmed
  experiment) mirror the paper's 8-condition factorial design at smaller
  scale.
- **Honesty gap:** the lab's scores are qualitative/single-observer; the
  paper's families are objective metrics. Bridging them (running the paper's
  metrics on lab renders) is an open experiment — tracked in
  `cpcs/research/gaps/src010_open_research_questions.md`.
