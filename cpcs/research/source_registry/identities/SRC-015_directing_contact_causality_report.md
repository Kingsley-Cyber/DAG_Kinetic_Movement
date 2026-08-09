---
id: SRC-015
title: AI Video Directing for Causal Human-Object Manipulation (user research return)
version: 1.0
epistemic_class: research_package
status: COMPLETE
lines: 1 file (34.8 KB) — gap_answer_04 (UG-008 case study)
file: gap_answer_04_directing_contact_causality_report.md (repo root; also committed)
kind: research_package
epistemic_status: PACKAGE_ESTABLISHED
acquisition: authored
sources: [SRC-015]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-015 — AI Video Directing for Causal Human-Object Manipulation

## Source identity

A **user research return** (D9 loop) — case study: bimanual opening and
closing of a zippered bag. Research question: how should an AI video
directing system represent, prompt, and verify causal human-object
manipulation sequences without treating unzipping as equivalent to opening
the bag panel? Returned 2026-08-09 as `gap_answer_04_...md` in the repo
root. Uses five internal evidence classes: source evidence / source-linked
inference / directing choice / provider-specific compromise / untested
hypothesis.

The return's Executive Answer: represent the task as a sequence of
**state-changing events over object parts, contacts, and visibility** —
UNZIP changes zipper-tooth closure state locally along the slider path;
OPEN changes panel angle after release/reach/regrasp of the panel lip with
the other hand stabilizing an anchored part; CLOSE reverses panel motion;
ZIP re-secures already seated zipper halves.

## Core claims

1. **Slider motion is a local closure-state operation** — teeth mesh or
   separate only when passed through the slider (YKK structure); the
   "passed region" flips state, the region ahead keeps its prior state.
2. **ZIP requires seated/aligned zipper halves** before slider motion;
   "zip while panel misaligned" is mechanically invalid (YKK usage manual).
3. **Gusset expansion follows panel displacement**, never precedes it;
   bag anatomy names front panel, rear shell, bottom hinge/base, side
   gussets, and zipper halves separately.
4. **Bimanual roles persist (Guiard 1987)** — skilled bimanual activity
   uses two hands in different, non-interchangeable roles (acting vs
   supporting); roles must stay stable across frames and cuts.
5. **Release/reach/regrasp is a necessary observable transition** when a
   hand changes object part (regrasp-planning literature); contact modes
   label contact as sliding/rolling/sticking/breaking free (Modern
   Robotics); contact-rich skills need explicit precondition functions
   (Liang 2023).
6. **Verification must be event- and frame-observable** — score contact,
   hand pose, object identity, grasp region (ContactPose); general quality
   metrics (VBench) and prompt adherence do not certify physics
   (PhyGenBench); provider surfaces are model/version/date scoped (Sora 2
   API deprecated, shutdown 2026-09-24).

## Evidence registry

YKK Americas structure + usage manual · Eagle Flexible Packaging side
gusset pouches · Arsutoria bag construction vocabulary · Guiard 1987
(bimanual roles) · Modern Robotics grasping/manipulation + contact modes ·
Wan 2016 regrasp graphs · Liang 2023 precondition functions · Fox & Long
PDDL2.1 · Meta AI ContactPose · OpenAI Sora report + video-generation
guide · Google DeepMind Veo prompt guide + Cloud best practices +
reference-image guide · Runway Gen-4 guide (prompting + creating) ·
VBench · PhyGenBench. Full citations with locators in the return file.

## Distillation

See `cpcs/research/distillation/ledger/15_directing_contact_causality_report.md`
(DIST-015): 2 EXTENDs — affordance_constraints (mechanism vocabulary for
closure manipulation) and interaction_lifecycle (bimanual role permanence +
regrasp observability); corroborates SRC-013 contact identity and
FAIL-01/02 taxonomy.
