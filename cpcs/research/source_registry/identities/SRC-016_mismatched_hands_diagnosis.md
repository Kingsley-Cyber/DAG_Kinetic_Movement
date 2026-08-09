---
id: SRC-016
title: Why AI Video Adds Extra or Mismatched Hands (user research return)
version: 1.0
epistemic_class: research_package
status: COMPLETE
lines: 1 file (5.0 KB) — gap_answer_05 (UG-008 diagnosis brief)
file: gap_answer_05_mismatched-hands-diagnosis.md (repo root; also committed)
kind: research_package
epistemic_status: PACKAGE_ESTABLISHED
acquisition: authored
sources: [SRC-016]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-016 — Why AI Video Adds Extra or Mismatched Hands

## Source identity

A **user research return** (D9 loop) — a short diagnosis brief answering
the extra/mismatched-hands failure class of the sling-bag case. Returned
2026-08-09 as `gap_answer_05_...md` in the repo root.

The return's Short Diagnosis: the likely root cause is **identity
ambiguity**. A prompt that describes two physical hands but gives them
three changing role labels (`zipper_hand`, `anchor_hand`, `lip hand`)
invites the model to treat the labels as separate visual agents instead of
two persistent hands whose jobs change over time.

## Core claims

1. **Role renaming creates extra actors** — job labels that change with
   the beat are inferred as separate entities; in a scene with no face,
   body, or wider context anchoring identity, hands become the main
   characters and any identity ambiguity lands directly on them.
2. **Empty-hand transfer invites hallucination** — release → reach →
   grasp in open air is where the model loses which hand is moving,
   especially with another visible stationary hand.
3. **Hard cuts re-sample identity** — every cut is another chance for hand
   count, pose, side, or appearance to drift when hands are the main
   subject (Sora guidance: motion is the hardest part to control; keep
   simple subject action, timing in beats).
4. **Hands exiting and re-entering frame reset continuity** — identity is
   not preserved on return unless the prompt restates the same physical
   hand.
5. **POV forearms have a competing visual prior** — training examples of
   bags/zippers/manipulation are mostly third-person, where another hand
   can enter from center or side; ambiguity lets the model satisfy both
   interpretations.
6. **The failure is stacked, not singular** — ambiguous labels + contact
   break + hard cuts + exits/re-entries + POV framing + a high-DOF
   object-contact task; the highest-leverage fix is reducing the identity
   burden: two stable hand labels, one continuous contact path, fewer
   action changes per clip, start/end or reference frames when available.

## Evidence registry

Sora 2 prompting guide (motion control, beats, inferred details) ·
DiffH2O (geometry + semantics + timing of hand-object interaction) ·
JointHOI (contact errors → floating/interpenetration artifacts) ·
HanDiffuser (irregular hand poses, shapes, finger counts) · HandDiffuse
(self-occlusion, self-similarity, articulation in two-hand data) · Video
Storyboarding (video identity consistency harder than image) · OpenAI Sora
video generation + Veo reference images (conditioning exists because text
alone is not enough).

## Distillation

See `cpcs/research/distillation/ledger/16_mismatched_hands_diagnosis.md`
(DIST-016): 2 EXTENDs — interaction_lifecycle (hand-identity label
stability) and failure_mode_catalog (role_renaming / hand_spawn /
reentry_reset rows); corroborates SRC-013 FAIL-01/FAIL-03 and SRC-015 role
permanence.
