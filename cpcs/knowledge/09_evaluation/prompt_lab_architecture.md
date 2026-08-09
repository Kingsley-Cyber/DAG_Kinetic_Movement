---
id: cpcs.lab.architecture
kind: mechanism
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U01, SRC-010-U02, SRC-010-U03, SRC-010-U04]
primary_route: cpcs/knowledge/09_evaluation/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/research/sources/
interfaces:
  - cpcs.lab.pattern_registry
  - cpcs.lab.ab_test_protocol
  - cpcs.evaluation.cpcs_evaluation_framework
  - cpcs.runtime.structured_prompting_architecture
---

# Prompt Lab Architecture

> **Source:** SRC-010 `lab/README.md`, `lab/AGENTS.md`, `lab/registry.yaml`, `lab/blocks.yaml`, `lab/CONTROL_SURFACE.md`. The only empirically validated component of the CPCS ecosystem — every claim traces to an actual render on Veo-3.1 / LTX-2.3.

## The model

```
levers  →  variants  →  runs (results.csv)  →  experiments (A/B)  →  patterns  →  recommendations
```

| Component | File | Role |
|---|---|---|
| Levers | `registry.yaml` | controlled vocabulary of knobs (camera.fps, skin.strategy, …), each with `values` + `affects` score dims |
| Variants | `variants/` | tracked prompt packages, each tagged with its lever values |
| Runs | `runs/results.csv` | append-only ledger: one row per generation (variant → model → 4 scores + verdict) |
| Experiments | `experiments/` | A/B tests that change **one lever** so a delta is attributable |
| Patterns | `registry.yaml → patterns` | curated "lever(s) → effect" findings with confidence + evidence — the recommendation engine |
| Blocks | `blocks.yaml` | tested modular prompt snippets with evidence, confidence, pairs_with / conflicts_with |

## Two control paradigms

| Paradigm | What the model consumes | Best for | Proven in |
|---|---|---|---|
| **descriptive_prose** | natural-language description | look, skin, vibe, performance *feel* (UGC) | v001–v004 |
| **numeric_canonical_truth** | explicit numeric tracks (keyframes, timings, vectors) | precise motion, choreography, timing, contact, identity lock | v005 (combat) |

Key finding (p008): for **motion/choreography**, numeric canonical truth carries precision prose cannot — v005 was driven by JSON *alone*. This refines p006: format is realism-neutral for *look*, but numeric structure is a genuine control channel for *motion*.

## Levers vocabulary (13)

`camera.device` · `camera.fps` (24/30/60) · `camera.dof` · `camera.stabilization` · `lighting` · `skin.strategy` (real_microtexture_forbid_smooth / heavy_texture / smooth / default) · `performance.direction` (loose_casual / scored_beats / neutral) · `face.motion` (alive_face_motion / minimal / none) · `format` (prose / yaml_xml / yaml_json / minified_json / xml) · `audio` · `render_style` (raw_ugc / cinematic) · `control_paradigm` (descriptive_prose / numeric_canonical_truth / hybrid) · `domain` (ugc_talkinghead / combat_action / dance / anime / product_demo / other) · `authoring_layers` (prose_only … tri_layer).

A variant = one chosen value per relevant lever. Keeping values in the vocabulary makes variants comparable and patterns minable.

## Channel catalog statuses

`proven` (a good run confirms it) · `partial` (bundled/seen, not isolated) · `unexplored`. Proven: camera.device/iPhone, skin.strategy (the #1 AI tell), body kinematics, contact solver, Laban effort vectors (combat), camera keyframes (combat), kinematic self-consistency tooling. Partial: lighting, performance.direction, face.motion, render_style, hard-constraint+verification blocks, joint rotations/velocity/easing, foot-contact track. Unexplored: microvariation, transition_smoothness, biomechanical realism.

**Unexplored frontier (8 channels, none tested):** FACS as numeric AU track · body-control curves (COM/gaze/breath) · effort vectors for UGC/dance · contact taxonomy beyond combat (grasp/press/tap on products) · style medium channel (photoreal vs anime_cel) · speed/time-warp channel · identity-lock token/reference binding · **verification loop post-render** (the pre-render half is tooled via `validate_kinematics.py`).

## Format discipline law (owner law)

1. Default output = the structured format(s) the control demands (pure fight/motion → JSON canonical; intent/style → YAML; ordered script/triggers → XML; full production → combination).
2. NL is an OPTION, produced transparently — one *labeled variant alongside* the structured form(s), never silently *instead of* them.
3. For A/B, multi-format is the elite move (p009): same content across NL/YAML/XML/JSON/combos = output variance = options to select from.
4. Before handing a single NL paragraph: which layer does this control, which format owns that layer? Deliver that format too.

## Honesty rule

`confidence` reflects **evidence, not conviction**. A lever bundled inside a good champion stays `low` until an **isolated** A/B (one lever changed, same seed) confirms it. Current seed data is from the authoring session (qualitative) — the champion v001 is real and user-validated; single-lever attributions are hypotheses awaiting isolated renders.

## Composition procedure (agent)

1. Classify goal → domain + paradigm (look/feel → prose; precise motion → numeric; both → hybrid).
2. Select blocks matching the domain; prefer higher confidence; resolve `conflicts_with`.
3. Assemble per `blocks.yaml → composition` (prose weave < 2000 chars; numeric = v005 shapes; hybrid = both).
4. Deliver with a rationale: which blocks, each block's confidence + evidence, unproven blocks flagged as proposed experiments.
5. Capability no block covers → look up `CONCEPT_INDEX.md` first (paper § refs), compose from the paper's definition, mark unproven, propose the isolated A/B.

## Three agent roles

Authoring proposes · compiler/resolver validates · verifier measures — run separately, never collapsed (`c_three_agent_topology`).

## Boundary

This is a working lab record, not a statistical study. All scores are single-observer qualitative (1–5) from one authoring session; patterns p001–p009 carry their confidence honestly and only e002 is isolated_confirmed.
