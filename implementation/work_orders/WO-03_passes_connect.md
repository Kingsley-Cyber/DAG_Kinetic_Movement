# WO-03 — Passes connect: `reads`, beat-scoped controls, coupling checks (T17; R-56, R-57)

## Goal

Carry dependencies between passes so decisions cohere: each pass declares what it reads, controls
can be scoped to a beat, and four coupling checks catch contradictions.

## Read first

`plan/ARCHITECTURE.md` §2.7, §2.8 · `plan/CONTROL_LAYER.md` R-56, R-57 · `director/passes.yaml` ·
`director/protocol.md` §4·0 · WO-01 and WO-02 results.

## Decisions already made

- `reads` is documentation plus data for a later `pack` command; `check` does not enforce it.
- Keep the coupling checks to the four below. Do not add more.
- Camera stays one control per shot unless a control has `beat`; then it applies to that beat only.

## Changes

1. `director/passes.yaml`: add `reads:` (list of IR areas) to these passes:

   | Pass | reads |
   |---|---|
   | physics | pathways, hands, anchors |
   | time | pathways, physics_events, anchors |
   | staging | entities, pathways |
   | continuity | entities, pathways, physics_events |
   | performance | beats, anchors, physics_events |
   | camera | beats, pathways, physics_events, staging controls |
   | attention | beats, camera controls |
   | light_color | camera controls, continuity controls |
   | style | camera controls, light_color controls |
   | audio | beats, physics_events |
   | synthesis | everything |

2. Schema: optional `beat` (beat id) on a control.

3. Coupling checks in `check` (errors; exact substrings):

   a. `"camera shows a hidden contact"` — a camera control scoped to a beat whose physics event has
      `contact_state` `occluded_contact` or `editorial_impact`, when the control's value (any string
      in it, lower-cased) contains the event's `contact_surface` (lower-cased) together with
      "close-up" or "close up".
   b. `"camera hides a confirmed contact"` — a camera control scoped to a beat whose event is
      `physical_contact_confirmed`, when its value contains "off-screen", "out of frame" or
      "cut away".
   c. `"beat does not cover its pathway stages"` — a beat whose `min_s` is less than
      0.2 × the number of pathway stages assigned to it (0.2 s per stage is a convention; put it
      in a named constant with a comment).
   d. `"control on unknown beat"` — a control whose `beat` is not a known beat.

4. Explicit-contract check (errors): every pathway stage of kind `contact` or `transfer` with
   `hands_required` ≥ 1 must list at least one hand (already true by R-09; add no new rule), and
   every physics event must have `trigger.actor` and `trigger.part` non-empty →
   `"explicit: trigger needs actor and part"`.

## Tests to add (new class `PassCoupling`)

- `test_control_on_unknown_beat_fails`
- `test_camera_close_up_on_hidden_contact_fails`
- `test_camera_cutaway_on_confirmed_contact_fails`
- `test_beat_too_short_for_its_pathway_stages_fails`
- `test_event_trigger_needs_actor_and_part`
- `test_passes_yaml_reads_reference_known_ir_areas` (load `passes.yaml`; every `reads` entry is in
  the allowed vocabulary used in the table above)

## Acceptance

All earlier tests green and unmodified; six new tests green; run 001 GREEN and its prompt
byte-identical.

## Records

`QUEUE.md` · `plan/TASKS.md` T17 · `plan/CONTROL_LAYER.md` R-56, R-57 · `plan/STATUS.md` ·
`director/protocol.md`: add one line that a control may carry `beat`.

## Stop if

Run 001 fails check 3c (it should not: each beat has at most four stages and at least 0.6 s). If
it does, lower the constant, record the value in `DECISIONS.md`, and continue.
