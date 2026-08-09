---
id: cpcs.motion.phase.evidence_vs_engineering
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-001 §1.2, §6, SRC-001-U06, SRC-001-U07]
primary_route: cpcs/knowledge/06_body_motion/phase_grammar/
secondary_routes:
  - cpcs/knowledge/10_time_rhythm/
interfaces: [motion_x_audio, motion_x_contact]
---

# Phase Grammar: Evidence-Backed vs Engineering Phases

## Principle

CPCS must separate phases supported by external research from the CPCS
engineering grammar.

**Evidence-backed concepts** (gesture research U06; robotics multi-phase
tasks U07):

```text
preparation · stroke/action · retraction · optional holds
(preparation → prestroke hold → stroke → poststroke hold → retraction)
plus: temporal segmentation · contact onset/offset · action boundaries
```

**CPCS engineering grammar** (useful normalized execution grammar, but must
be tagged `derived` or `authored`, never as a universal law of movement):

```text
precondition → anticipation → initiation → acceleration → action_apex
→ contact → deceleration → follow-through → recovery → postcondition
```

## Canonical phase object

```json
{
  "phase_id": "p3",
  "role": "contact",
  "start": 1.20,
  "end": 1.32,
  "boundary_basis": "detected",
  "confidence": 0.88,
  "preconditions": ["hand_near_target"],
  "postconditions": ["contact_established"]
}
```

Phase boundary provenance must be declared — one of:
`observed` / `authored` / `derived` (kinematic/contact thresholds) /
`provider-oriented`.

## Critical distinction

`action_apex` is **not automatically** `contact`. A near-miss has an apex
without contact; compilers must not emit `contact=true` for near-misses.

## Exceptions

Not every physical action has exactly the gesture-research phases; the
evidence supports the phase concept, not a universal fixed sequence.

## Open question

Which phase boundaries are reproducible across annotators enough to become
canonical (SRC-001 §26 Q1 — see `research/gaps/`).

## Seven-phase production grammar (SRC-012 EXTEND — fulfills SRC-003 E18)

> **Source:** SRC-012 topic 3 — "Motion Phase Grammar"; `map_phase_bml_v1`
> from the KB canonical model

The KB contributes a third, normalized **production grammar** used for
authoring and compilation — tagged CPCS_CONVENTION, never a universal
movement law:

```text
initiation → preparation → acceleration → stroke → overshoot → recovery → settle
```

### Relationship to the grammars above

| Grammar | Origin | Role |
|---|---|---|
| gesture research (preparation → stroke → retraction + holds) | evidence-backed (U06) | semantic structure of communicative action |
| robotics multi-phase tasks (U07) | evidence-backed | temporal segmentation |
| 10-step engineering grammar (precondition → … → postcondition) | CPCS engineering | compiler-oriented normalized execution |
| seven-phase grammar (initiation → … → settle) | KB CPCS_CONVENTION | production authoring/compilation profile |

- **Optionality:** initiation, preparation, overshoot, recovery, settle are
  optional; acceleration and stroke are required. A blink may have no useful
  preparation; continuous walking normally has no settle between steps; a
  collision can interrupt recovery. Skipped phases are exposed, never
  inserted as zero-duration ghosts.
- **Role-based stroke:** `stroke` is contact, maximum extension, or grasp
  onset depending on action class; in locomotion it may be renamed `contact`
  to avoid implying a communicative gesture.
- **BML sync points are a different taxonomy** (`start · ready · stroke_start
  · stroke · stroke_end · relax · end`). The KB maps phases to sync points
  (`map_phase_bml_v1`: initiation→start, preparation→ready/stroke_start,
  stroke→stroke, overshoot→stroke_end, recovery→relax, settle→end) as a
  **compile-time projection target**, never as an identity — a CPCS `stroke`
  may be contact, maximum extension, or grasp onset, while BML `stroke` is
  the meaning-bearing phase.
- **Timing presets** (explosive … microgesture, normalized ratios summing to
  1) and per-phase roles are in `cpcs.motion.phase.timing_presets`;
  SRC-010's 4-phase strike ratios are a third compatible granularity
  (`cpcs.combat.math_metrics_layer`).

The apex/contact distinction above is preserved: semantic apex and physical
contact are **separately addressable events**; compilers must not emit
`contact=true` for near-misses.

## Verification

`test_seven_phase_grammar_tagged_cpcs_convention`,
`test_phase_optionality_respected`,
`test_phase_not_relabeled_as_bml_syncpoint`,
`test_apex_distinct_from_contact`.
