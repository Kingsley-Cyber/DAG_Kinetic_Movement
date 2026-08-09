---
id: cpcs.research.cpcs_mx_experiments
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §30]
primary_route: cpcs/research/sources/experiments/
secondary_routes:
  - cpcs/verification/
  - cpcs/research/sources/
interfaces:
  - cpcs.found.layer_architecture
  - cpcs.runtime.constraint_compilation
  - cpcs.runtime.canonical_schema
  - cpcs.verification.semantic.verification_contract
---

# CPCS-MX Experimental Program

> **Source:** SRC-005 §30 — "Experimental program"

## Principle

CPCS-MX should be evaluated as a representation and compiler, not only
through visually selected demos. A rigorous program separates schema
expressiveness, compilation accuracy, model controllability, and perceived
motion quality.

## Research questions

1. Does explicit phase and contact coding improve temporal compliance over
   text-only prompting?
2. Do Laban and mannerism layers improve perceived performance specificity
   without reducing action correctness?
3. Does separating anatomical motion from stylized deformation reduce rig
   failures in superhuman clips?
4. Do dense pose controls outperform key poses for fight-scene contact timing?
5. Does a canonical score improve transfer of choreography across characters
   and morphologies?
6. Does re-extraction enable targeted correction with fewer full regenerations?
7. Which fields remain unsupported by current generation adapters?

## Test suite

### Natural locomotion

walk, stop, turn, reach; uneven-ground foot placement; speed changes; habitual
asymmetry; gaze and breath coordination.

### High-fidelity UGC

direct lens address; speech gesture; product pickup and demonstration;
self-framing adjustment; natural pause and CTA hold.

### Staged combat

step-in and camera-side strike-like action; block or dodge; staged
near-contact; recoil and recovery; two-character timing and screen direction.

### Anime/superhuman

held anticipation key; compressed execution; smear frame; reduced-gravity
aerial phase; exaggerated but readable landing; VFX and camera emphasis.

## Ablation conditions

```text
A: text only
B: text + action graph
C: B + phase/contact events
D: C + root and key-joint constraints
E: D + Laban/mannerism/face/breath
F: E + style transform
G: F + full dense control and closed-loop verification
```

Keep model, seed strategy, references, duration, and camera constant where
possible. Report failures and discarded samples.

## Metrics

### Primary

action-order accuracy; event timing error; contact distance and contact-time
error; root and joint trajectory error; foot slip; retargeted end-effector
error; joint-limit and penetration violations; camera and screen-direction
compliance; face/gaze event error; perceived movement-quality match; persona
consistency; generation attempts to acceptance.

### Secondary

prompt/token length; compiler runtime; adapter coverage; human correction
time; RAG retrieval precision; schema-invalid output rate; conflict-resolution
rate.

## Calibration studies

Laban proxy profiles require calibration: have trained movement analysts label
clips, compute candidate features, and evaluate whether the proxy is predictive
without collapsing distinct concepts. Mannerism profiles require repeated
performances from the same character or performer to distinguish stable traits
from one-shot action demands. Perceptual metrics require human ratings and
reliability analysis.

## Reproducibility package

Each run stores: input score and hashes, compiler and adapter versions, source
and reference assets, model identifier, seed and generation parameters, output
videos, re-extracted observations, metric reports, human-rating protocol and
anonymized data, and failure log. A curated demo without failed candidates is
not sufficient evidence of control.

## Success criteria

The project should define task-specific thresholds before generation.
Engineering gates might require action-order equality, contact within one or
two frames, foot slip below a chosen distance, and no hard joint-limit
violations. Such thresholds are not universal; they derive from shot purpose,
frame rate, scale, and intended style.
