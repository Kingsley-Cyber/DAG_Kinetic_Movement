---
id: SRC-014
title: Causal Video-Generation Reliability Cheat Sheet (user research return)
version: 1.0
epistemic_class: research_package
status: COMPLETE
lines: 1 file (49.7 KB) — gap_answer_03 (UG-008 supplement)
file: gap_answer_03_video_generation_reliability_cheatsheet.md (repo root; also committed)
kind: research_package
epistemic_status: PACKAGE_ESTABLISHED
acquisition: authored
sources: [SRC-014]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-014 — Causal Video-Generation Reliability Cheat Sheet

## Source identity

A **user research return** (D9 loop) titled *"UG-008 Supplement — Causal
video-generation reliability cheat sheet"*: a research-backed workflow for
CPCS validation and human review, scoped to Veo 3.1, Sora 2, Kling VIDEO
3.0/3.0 Turbo, Runway Gen-4.5, and mechanism-heavy video generation.
Returned 2026-08-09 as `gap_answer_03_...md` in the repo root. Status line
in the return: *"staged research proposal; not curated repository truth."*

The return's BLUF: video generators produce plausible sequences but do not
guarantee mechanically valid state transitions; the most reliable stack is
`typed action operator → one causal event per clip → endpoint anchors →
provider-specific prompt compiler → causal verifier → clip chaining`.

## Core claims

1. **Pin state, contact, and order — not just appearance.** The failure
   surface includes identity loss, effect-before-contact, broken attachment,
   invalid kinematics, non-monotonic motion, and incorrect final state.
2. **The `pre / motion / post / forbid` contract is planning-inspired, not
   literal STRIPS.** `pre` maps to preconditions, `post` to add/delete
   effects; `motion` belongs to a trajectory/durative-action layer; `forbid`
   is an invariant/output validator, not a STRIPS delete list.
3. **First/last-frame conditioning is an endpoint constraint, not a
   deterministic physics solver.** Boundary states tighten, but the model
   can still morph, teleport, penetrate, or reverse causality between them.
4. **One physical handoff per generation is the safest default.** Zipper
   motion, contact transfer, panel folding, and cavity reveal must not be
   one unconstrained event (engineering inference; Sora guide shorter-clip
   recommendation + benchmark evidence).
5. **The negative-prompt assumption must be corrected for current
   products:** Veo exposes a dedicated `negativePrompt`; Kling 3.0 combines
   positive + negative in one prompt; Sora 2 documents no negative field;
   Runway Gen-4.5 recommends positive phrasing, no negative field.
6. **Camera vocabulary is recognized by provider guides** (shot, movement,
   lens, focus, lighting, temporal terms); the stronger "provider defaults
   to cinematic because training captions came from film/stock" claim is
   plausible but unestablished by cited official documentation.

## Evidence registry (E1–E16)

E1 OpenAI Sora report (limitations) · E2 VideoPhy · E3 PhyGenBench · E4
STRIPS (classical planning refs) · E5 PDDL durative semantics · E6
first/last-frame literature · E7 Sora guide shorter-clip recommendation ·
E8 Veo 3.1 prompt guide · E9 Veo first/last-frame API · E10 Sora 2 Videos
API guide · E11 Sora 2 API deprecation/shutdown 2026-09-24 · E12 Kling
VIDEO 3.0/3.0 Turbo API · E13 Runway Gen-4.5 guide · E14 Runway positive-
phrasing guidance · E15 Runway Animate with Keyframes · E16 Runway
`promptText` limits. Full citations with locators in the return file.

## Provider facts (staged — dated 2026-08-09, change fast)

Veo: negativePrompt + first/last-frame, 4/6/8 s · Sora 2: no negative
field, first-frame `input_reference` only, deprecated (shutdown
2026-09-24) · Kling 3.0: combined positives/negatives, 3,072-char limit
(2,500 recommended, 512/shot), first+last frame supported, Turbo first
frame only, 3–15 s · Runway Gen-4.5: no negative field, `promptText`
1–1,000 UTF-16 units, keyframes app, 2–10 s.

## Distillation

See `cpcs/research/distillation/ledger/14_video_generation_reliability_cheatsheet.md`
(DIST-014): 1 EXTEND — capability_classes_and_loss_records (provider
control-surface matrix + negative-prompt precedence); corroborates SRC-013
carrier rules R1–R3.
