---
id: cpcs.lab.pattern_registry
kind: catalog
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U02, SRC-010-U11]
primary_route: cpcs/knowledge/09_evaluation/
secondary_routes:
  - cpcs/evaluation/benchmark_runs/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.lab.architecture
  - cpcs.lab.ab_test_protocol
  - cpcs.lab.variant_lineage
  - cpcs.evaluation.cpcs_evaluation_framework
---

# Empirical Pattern Registry (p001–p009)

> **Source:** SRC-010 `lab/registry.yaml → patterns`. The recommendation engine of
> the lab: curated "lever(s) → effect" findings, each with a confidence level and
> an evidence chain. Every pattern traces to an actual render on Veo-3.1 / LTX-2.3.

## The registry

| ID | Statement | Confidence | Evidence chain | Recommend when |
|----|-----------|------------|----------------|----------------|
| p001 | Real skin needs **microtexture**; "smooth" is the #1 AI tell — forbid-list negatives + positive microtexture recipe | **high** | e002 (isolated_confirmed), r001, r004 | talking-head UGC, close-ups, product demos — anywhere skin is visible |
| p002 | 30 fps cadence reads as UGC (vs 24 fps cinematic) | low | e001 (hypothesis; bundled in champion) | iPhone-look UGC — treat as proposed experiment, not a rule |
| p003 | Deep focus (small depth of field) reads cinematic | low | bundled in v003 | — |
| p004 | **Loose, casual performance direction** beats scored beats for UGC | medium | v001/v002 champion scores | UGC talking-head performance |
| p005 | Alive face motion (micro head/eye drift) increases realism | low | bundled in champion | — |
| p006 | **Format is realism-neutral for look**: identical content in YAML-in-XML vs YAML+JSON → identical scores | **high** | v001 vs v002, both 5/5/4/5 | cross-model portability; format debates |
| p007 | `raw_ugc` render style + anti-cinematic block increases UGC realism | medium | v001 champion | UGC domain |
| p008 | **Numeric canonical truth carries precision prose cannot**: motion/choreography driven by JSON alone | medium | r005 (v005, JSON alone, 5/5/5) | precise motion, choreography, timing, contact, identity lock |
| p009 | Format variance yields **options, not quality**: same content across N formats → output variance to select from | low | e003 (hypothesis) | multi-format A/B delivery when render cost allows |

## Confidence discipline (the honesty rule)

`confidence` reflects **evidence, not conviction**. A lever bundled inside a
good champion stays `low` until an **isolated A/B** (one lever changed, same
seed) confirms it. Current seed data comes from a single authoring session
(qualitative 1–5 scores). The champion v001 is real and user-validated;
single-lever attributions (p002, p003, p005) are hypotheses awaiting isolated
renders.

Evidence chain reading: `p001: [e002, r001, r004]` means "confirmed by the
isolated experiment e002, and consistent with runs r001 and r004" — not
"three independent confirmations".

## Patterns ↔ blocks

Each pattern is implemented as one or more tested blocks (`blocks.yaml`), which
carry their own confidence and `pairs_with` / `conflicts_with` constraints:

- p001 → `blk_skin_real_microtexture` (high) + `blk_render_negatives` (high)
- p007 → `blk_render_negatives` (high), `blk_env_ordinary`, `blk_audio_phone_mic` (medium)
- p004 → `blk_perform_loose_casual` (medium) — conflicts with `blk_perform_scored_beats`
- p005 → `blk_face_motion_alive` (medium)
- p008 → `blk_kinematic_skeleton` + `blk_contact_solver` + `blk_effort_vectors` + `blk_camera_keyframes` (medium)
- unproven: `blk_facs_au_track` (FACS as numeric AU track) — flagged, never silently included

## Recommendation procedure

1. Prefer higher-confidence patterns for the target domain.
2. Resolve `conflicts_with` before assembling (e.g., loose vs scored performance).
3. Cite each block's confidence + evidence in the delivered rationale.
4. Flag any unproven block used out of necessity as a **proposed experiment**
   with its A/B design (see `cpcs.lab.ab_test_protocol`).

## Boundary

The registry is a working lab record, not a statistical study: single-observer,
single-session scores; only e002 is `isolated_confirmed`; p009's variance claim
(not quality claim) is the only role e003 supports.
