---
id: cpcs.lab.runbooks
kind: method
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U17, SRC-010-U18, SRC-010-U19, SRC-010-U20]
primary_route: cpcs/evaluation/reference_video/
secondary_routes:
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.lab.architecture
  - cpcs.runtime.kinematic_validation
  - cpcs.evaluation.reference_video_distillation
  - cpcs.evaluation.extraction_pipeline_stages
  - cpcs.runtime.cross_format_compiler_reference
---

# Lab Runbooks (4 operational procedures)

> **Source:** SRC-010 `lab/RUNBOOK_*.md` ×4. Named workflows with trigger
> phrases, step sequences, and gates — the operational layer of the lab.

## 1. Pegasus extraction (semantic lane)

**Trigger:** prose source describes movement; intent matters more than
measurement.

- Semantic lane runs at ~1 fps — it captures **what is described**, never
  measures. Minimum clip 4 s.
- Schema > prompt: records conform to the record schema before wording is
  trusted; movement-analyst prompt is the fixed extraction persona.
- **Provenance pinning:** every record keeps its source clip, time window, and
  pass label (261k/98k token split for long inputs).
- **Slow-proxy time conversion:** duration estimates from a 0.25×–0.5× slow
  playback are converted back to real-time before recording.
- Normalization mapping table converts free-form descriptions into canonical
  fields (record normalization).
- **Known limits:** body_phase defaults to `travel` when unstated; no force
  claims are ever emitted from prose.

## 2. Reference → kinematic truth

**Trigger:** a reference video must become a numeric canon (breakdown →
reconstruction loop, 8 steps).

1. Rights gate first (no unlicensed reference work).
2. Run the 4-tier ladder (semantic → pose → calibrated → measurement; see
   `cpcs.runtime.kinematic_validation`).
3. Tier 2 = `extract_pose_tier2.py` (mediapipe, num-poses 2, keyframe 0.5 s,
   greedy nearest-centroid tracking).
4. Merge lanes: measured wins on conflict, semantic label retained
   (e.g., semantic 1.4 s vs pose 1.55 s → 1.55 s recorded, label kept).
5. Round-trip: 50 ms / 0.05 m thresholds against the final canon.
6. Honest bounds: Tier-2 output is 2D `detected`, never `measured`.

## 3. Cross-style switching

**Trigger:** porting a scene/choreography across styles (UGC ↔ cinematic ↔
anime) while preserving identity and intent.

- **4-layer separation:** separate identity, action/choreography, style, and
  presentation layers so one can change without disturbing the others.
- **8 invariants** must survive any style switch (identity, causality, beat
  order, contact truth, …).
- Style profile inheritance: a style layer inherits from a base profile and
  overrides only its own fields.
- **Typed transform vector:** a 10-dimension vector (e.g., exposure, camera
  amplitude, time-warp strength, deformation scale) transforms base content
  into the target style; each dimension has an owner.
- Superhuman virtual physics split: what looks superhuman in presentation is
  authored separately from the choreographic skeleton (staged near-contact
  kept honest).
- **Style ablation:** 7-condition ablation (base + each style dimension alone
  + full) attributes each dimension's effect.
- Promote procedure: promote a style layer only after its ablation passes.

## 4. Format mixing and tinkering

**Trigger:** a prompt/package misbehaves, or a production needs a format
combination.

- **Part A — mixing compiler:** intent → package table (which format owns
  which intent); 7 merge laws (one authority per quantity; YAML resolves down
  into JSON; XML owns order + triggers only; JSON wins on conflict, reported
  not averaged; resolution order profile < scope < local override < human
  lock; typed merges only; two-document clock agreement); 5 combo recipes
  (YAML-in-XML, YAML+JSON, JSONL evidence streams, …).
- **Part B — tinkering map:** 14-row symptom → field → format table (e.g.,
  "motion drifts" → retime_map → JSON; "skin plastic" → skin.strategy →
  YAML block; "events out of order" → XML trigger sequence).
- **Part C — growth protocol:** 7-step cannibalize flow — extract a working
  pattern from a one-off prompt, promote it to a block, log it, and gate the
  promotion with `sync_repo.py` (checks S1–S4).

## Trigger phrase summary

| Runbook | Trigger |
|---|---|
| pegasus_extraction | prose → structured movement record |
| reference_to_kinematic_truth | reference video → numeric canon |
| cross_style_switching | same content, different style |
| format_mixing_and_tinkering | misbehaving output / format assembly |

## Boundary

Runbooks encode lab practice, not guarantees: each output inherits the lab's
honest confidence levels and must be verified by the tooling gates before use.
