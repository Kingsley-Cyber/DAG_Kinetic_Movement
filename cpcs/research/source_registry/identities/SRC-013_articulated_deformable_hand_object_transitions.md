---
id: SRC-013
title: Articulated and Deformable Hand–Object State Transitions (user research return)
version: 1.0
epistemic_class: research_package
status: COMPLETE
lines: 2 files (~83 KB) — gap_answer_01 (report, 33 KB) + gap_answer_02 (curated, 663 lines)
file: gap_answer_01_Articulated and Deformable Hand-Obj.txt, gap_answer_02_articulated_deformable_hand_object_transitions.md (repo root; also committed)
kind: research_package
epistemic_status: PACKAGE_ESTABLISHED
acquisition: authored
sources: [SRC-013]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-013 — Articulated and Deformable Hand–Object State Transitions

## Source identity

A **user research return** (D9 loop) answering the sling-bag zipped→open
hard-cut gap: how articulated and deformable hand–object state transitions
must be represented, causally compiled, and verified for generative video.
Returned 2026-08-09 as two files in the repo root:
`gap_answer_01_Articulated and Deformable Hand-Obj.txt` (dense report) and
`gap_answer_02_articulated_deformable_hand_object_transitions.md` (curated,
663 lines). Status line in the return: *"staged research proposal; not
curated repository truth."*

The return's BLUF: the sling-bag failure is a **representation and
execution-carrier failure**, not merely a weak prompt — a continuous
generation asked to invent contact transfer, seam release, panel motion,
gusset deformation, and cavity reveal at once.

## Core claims

1. **Typed part–connection–region representation** — objects are typed
   graphs (rigid / articulated_rigid / surface_deformable / volume_deformable
   / distributed_closure / unknown), not single meshes; rest representation,
   material behavior, persistence, and observables are separate fields;
   appearance, collision/simulation, and semantic identity may differ.
2. **Durative causal transitions** — `open` compiles as a causal transition
   with start conditions, interval invariants, phase effects, end conditions,
   and named failure states (PDDL2.1-style semantics; not PDDL storage).
3. **Contact identity** — monocular RGB supports observed/detected contact
   evidence, not measurement; contacts are identity-bearing, time-bounded
   hypotheses; occlusion ≠ absence, unknown ≠ false.
4. **Action-specific verification** — causal-order predicates (closure
   release, panel displacement, contact persistence, gusset expansion,
   cavity reveal, topology preservation, consistent final state), not a
   generic "looks plausible" score.
5. **Hard-cut discipline** — preserve an authored cut when the source uses
   one; never claim omitted stages as observed; continuous synthesis only
   when the product requirement rejects the cut, with additional evidence.
6. **Carrier selection** — text cannot communicate exact trajectories,
   topology splits, or multi-finger grasps; escalate to dense carriers
   (MANO tracks, part masks, keyframes, depth, 3DGS mobility, Plücker
   embeddings) per provider capability.

## Evidence registry (E1–E14)

E1 OpenUSD Physics schema · E2 NVIDIA Omni deformables · E3 PDDL2.1
durative semantics · E4 BEHAVIOR/BDDL · E5 ARCTIC dataset · E6 ContactPose ·
E7 TAP-Vid · E8 VBench · E9 PhyGenBench · E10 Google Veo first/last-frame ·
E11 Google Veo reference images · E12 Runway Gen-4.5 input controls ·
E13 Runway Edit Studio/Aleph 2.0 · E14 Adobe Firefly composition reference.
Full citations with locators and supporting passages in the return files.

## Numeric claims (staged — unvalidated until experiments)

Soft-tissue penetration ≤ 2 mm finger pads / ≤ 5 mm palm (DiffContact);
cavity visibility V ≥ 0.70; contact stability ≤ 0.05 m/s; kinematic Chamfer
≤ 11.3 mm². Recorded as SRC-013 evidence, NOT canonical values.

## Distillation

See `cpcs/research/distillation/ledger/13_articulated_deformable_hand_object_transitions.md`
(DIST-013): 5 EXTENDs — interaction_lifecycle (contact identity),
affordance_constraints (typed part graph), continuity_state (unobserved
transition interpolation), failure_mode_catalog (FAIL-01…05 + metrics),
capability_classes_and_loss_records (carrier decision rules R1–R4).
