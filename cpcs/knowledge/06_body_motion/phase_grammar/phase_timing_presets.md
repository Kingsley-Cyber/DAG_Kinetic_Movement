---
id: cpcs.motion.phase.timing_presets
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-012]
primary_route: cpcs/knowledge/06_body_motion/phase_grammar/
secondary_routes:
  - cpcs/knowledge/10_time_rhythm/
  - cpcs/knowledge/05_action/combat/
interfaces:
  - cpcs.motion.phase.evidence_vs_engineering
  - cpcs.rhythm.metrics_contract
  - cpcs.rhythm.beat_syncpoint_alignment
  - cpcs.contact.interaction_lifecycle
---

# Phase Timing Presets and Phase Roles

> **Source:** SRC-012 topic 3 — "Motion Phase Grammar"

## Principle

The seven-phase sequence is a good **CPCS production grammar**, not an
established universal motion model. It synthesizes gesture research
(preparation, optional holds, meaning-bearing stroke, retraction), BML sync
points, animation (anticipation, follow-through, overlap), and action
biomechanics. The compiler must permit **omission and merging**: a blink may
have no useful preparation; continuous walking usually has no settle between
steps; a held conversational gesture can add prestroke/poststroke holds; a
collision can interrupt recovery.

## Canonical phases

| # | Phase | Purpose | Optional | Carries |
|---|---|---|---|---|
| 1 | initiation | first observable/inferred commitment | True | intent, attention shift, deception setup |
| 2 | preparation | organize support, alignment, backswing, guard, anticipation | True | readability, feint information, pre-tension |
| 3 | acceleration | increase linear/angular velocity toward focal event | False | force development, urgency, commitment |
| 4 | stroke | meaning-bearing apex, target acquisition, or contact | False | semantic payload, contact, emotion accent |
| 5 | overshoot | post-apex continuation (momentum/follow-through/exaggeration) | True | perceived force, style exaggeration |
| 6 | recovery | retract, recoil, redirect, or return toward stable organization | True | defensive readiness, recoil, aftereffect |
| 7 | settle | dissipate residual motion; establish next stable state | True | weight resolution, secondary motion, reaction beat |

`stroke` is **role-based**: in a gesture it is the meaningful excursion; in a
punch it can be contact or maximum extension; in a reach it can be grasp
onset; in locomotion it may be renamed `contact` to avoid implying a
communicative gesture.

## Timing presets (normalized phase ratios, sum to 1)

| Preset | Ratios (initiation → settle) | Status |
|---|---|---|
| explosive | 0.03 / 0.09 / 0.19 / 0.22 / 0.14 / 0.22 / 0.11 | CPCS_CONVENTION |
| ballistic | 0.03 / 0.07 / 0.21 / 0.22 / 0.20 / 0.18 / 0.09 | CPCS_CONVENTION |
| controlled | 0.07 / 0.17 / 0.17 / 0.22 / 0.07 / 0.19 / 0.11 | CPCS_CONVENTION |
| sustained | 0.07 / 0.14 / 0.17 / 0.27 / 0.06 / 0.18 / 0.11 | CPCS_CONVENTION |
| microgesture | 0.08 / 0.10 / 0.16 / 0.30 / 0.04 / 0.18 / 0.14 | CPCS_CONVENTION |

Ratios are **initialization presets only** — learn them per action, actor,
genre, and model through immutable experiments. A clip that looks "floaty"
may need shorter acceleration and more localized jerk, but blindly applying
an explosive preset can remove intended hesitation or weight.

> **Delta (documented, do not merge):** the rhythm-oriented presets in
> `rhythm_metrics_contract.md` use different values for the same phase names
> (e.g., explosive 0.05/0.22/0.18/0.10/0.10/0.20/0.15). Both are CPCS
> conventions; the compiler reconciles them as a recorded decision and never
> silently overrides one with the other. A third granularity exists in
> `combat_math_metrics_layer.md` (SRC-010 4-phase strike ratios with contact
> as a bin) — compatible, not identical.

## Phase roles

Every phase exposes start/end time, progress curve, primary joints, contacts,
force role, semantic role, emotional role, and confidence — one physical
interval can carry several functions without conflating them (a punch's
Preparation may carry deception, force preloading, and visible anger at once).

| Phase | Semantic role | Force role | Emotion role |
|---|---|---|---|
| initiation | commit | align | focused |
| preparation | load | preload | restrained anger |
| acceleration | approach | propulsive | high arousal |
| stroke | blocked contact | impact | accent |
| overshoot | follow-through | momentum | accent decay |
| recovery | guard return | recoil | controlled |
| settle | stance reset | dissipate | ready |

(Worked values from `ex_cross_punch_01`.)

Expressive roles:
- **Force:** preparation/acceleration establish support/velocity; stroke
  carries contact; overshoot externalizes commitment; recovery shows recoil.
- **Deception:** initiation/preparation can be hidden, redirected, repeated,
  or aborted; a false preparation creates a branch.
- **Emotion:** facial/postural onset may lead the action, peak at stroke, or
  lag as aftermath. **Do not force all channels to peak simultaneously.**
- **Readability:** anticipation and settle give causal boundaries; a
  realistic action can be unreadable when the camera or edit erases them.

## State-machine rules

Default transitions follow phase order, but the schema permits
`initiation→acceleration`, `preparation→stroke`, `stroke→recovery`,
`stroke→settle`, `recovery→next initiation`. **Interruptions are first-class
events**: a block/collision may branch to a new interaction chain; a feint
may abort before stroke; a moving target may cause retargeting; balance loss
may invoke protective recovery.

## Action decompositions (editable priors, not coaching doctrine)

| Action | CPCS phase interpretation |
|---|---|
| jab | gaze/guard intent → minimal hidden preparation → lead-side acceleration → contact/max extension → small overshoot → rapid guard return → stance restabilizes |
| cross_punch | ground/hip commitment → rear-side load → leg–pelvis–trunk–arm acceleration → contact → rotational continuation → recoil/deceleration → guard reset |
| roundhouse_kick | weight shift → chamber/pivot → pelvis–thigh–shank acceleration → foot/shin contact → rotational continuation → re-chamber/step-through → stance reset |
| block | threat orientation → interception preparation → blocking surface acceleration → contact/deflection → redirect → return/counter → new guard |
| evade | attention/weight release → base organization → COM leaves line → maximum clearance → optional angle continuation → reorient → counter-ready position |
| reach | gaze to object → postural organization → hand approach → grasp/contact → optional miss overshoot → transport/retract → new contact state |
| turn | eyes/head orient → base preload → pelvis/trunk rotate → new orientation → secondary lag → braking → stable posture |
| walk_step | weight transfer → swing limb unload → swing advances → foot contact → COM progresses → opposite transition → **normally no settle in continuous gait** |

Templates are stored as editable priors (boxing measurements differ across
protocols; the axe-kick review documents technique-phase variation).

## Compiler requirements

- Pin contact events **before** time warping and preserve event order.
- Do not synthesize overshoot when the interaction constraint forbids it.
- Keep semantic apex and physical contact as separately addressable events.
- Expose skipped phases rather than inserting zero-duration ghosts.
- Validate non-negative phase durations; cover the action interval exactly
  when coverage is required.
- Permit overlapping actions and nested phase hierarchies for two-person
  exchanges.

## DAG representation

```text
action →(HAS_PHASE ordered)→ phase_1 … phase_7
phase →(binds)→ contact_event  (contact_event_ids on stroke/overshoot)
phase →(interrupts)→ phase     (interruption edge, first-class)
action →(anchors_at)→ beat     (scene offset via beat start)
phase →(mapped_to)→ sync_point (BML; see beat_syncpoint_alignment)
```

Phase timelines are **action-local** (primitive-relative times); scene
anchoring happens through beat start + contact event binding
(worked example: timeline 0–1.1 s anchored at scene 0.7 s; contact at scene
1.13 s).

## Verification

`test_preset_ratios_sum_to_one`,
`test_contact_pinned_before_warp`,
`test_skipped_phase_exposed_not_zero_ghost`,
`test_phase_order_valid_without_interruption`,
`test_apex_distinct_from_contact`.
