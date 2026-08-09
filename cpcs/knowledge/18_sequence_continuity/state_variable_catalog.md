---
id: cpcs.runtime.state_variable_catalog
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007 G003, G004]
primary_route: cpcs/knowledge/18_sequence_continuity/
secondary_routes:
  - cpcs/runtime/04_synthesis/
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.mx.continuity_state
  - cpcs.runtime.continuity_capsule
  - cpcs.runtime.reasoning_atom
---

# Action State and Persistent State Catalog

> **Source:** SRC-007 G003/G004 — "Action and persistent state"

## Principle

Executable action preconditions/effects over persistent state:

```text
STATE(t) + EVENT → STATE(t+1)
```

with invariant checking and atomic event application.

## Seven state categories

| Category | Meaning | Examples |
| --- | --- | --- |
| identity invariants | must never change | actor identity, anatomy |
| persistent fluents | survive across scenes until changed | held object, ownership, injury, damage, wardrobe |
| continuous measured state | sampled physical quantities | position, orientation, wetness, lighting |
| ephemeral execution state | transient within a shot | stance, gaze target, open event state |
| derived state | computed from other state | speed, fatigue display from exertion |
| visual-only display cues | rendered appearance, not world truth | residue that exists only for camera |
| epistemic state | what agents/audience know | viewer-known facts, character knowledge |

## Atomic state patch

Event application is an atomic state patch:

```text
precondition evaluation → effect commit → invariant validation
→ rollback/failure behavior
```

Each exemplar field declares: identity scope, value type, units/frame,
initialization, write authority, update rule, persistence, reversibility,
observability, uncertainty, and termination.

## Required failure cases

- competing events that write the same state (conflict or ordering
  resolution must be explicit);
- missing initial state (unknown, not assumed);
- an effect known only after observing the generated video (observed, not
  authored);
- the exact continuity error prevented by consulting state (e.g. prop
  replacement, identity disappearance, stance flip).

## Verification

`test_event_application_atomic_with_rollback`,
`test_competing_state_writes_resolved`,
`test_missing_initial_state_is_unknown_not_assumed`,
`test_post_generation_effect_labeled_observed`,
`test_continuity_error_prevented_by_state_consult`.
