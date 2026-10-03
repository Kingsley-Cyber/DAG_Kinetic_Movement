# WO-02 — Physics causal events, first slice (T35; R-41, R-42, R-44)

## Goal

Give the IR a cause-and-effect record per beat and make the emitter write it as one sentence in
the order cause → contact → reaction → settle. Risk-based degradation and the failures registry
are **not** part of this work order.

## Read first

`plan/ARCHITECTURE.md` §3.5.7 · `plan/CONTROL_LAYER.md` R-41, R-42, R-44 · WO-01 (anchors exist).

## Decisions already made

- Field name `physics_events` (top level, optional array). One event per beat at most.
- `force.relative_to` points at an **anchor** (WO-01) of quality `weight` or `intensity`, or is
  `null` for the first event, which then needs an anchor declared on its own beat.
- `must_not_imply` is stored and copied into `verdict.md` as checklist lines; it is never emitted.
- `contact_state` is stored and emitted as written; no automatic downgrade in this slice.
- Pathways stay as they are. An event may name `pathway_stage` (a stage id) to link them, optional.

## Schema

`physics_events[]`, `additionalProperties: false`, required: `event_id, beat, trigger,
contact_surface, contact_state, primary_reaction, settle`.

| Field | Type |
|---|---|
| `event_id` | string, unique |
| `beat` | beat id |
| `trigger` | `{actor, part, action}` strings |
| `contact_surface` | string |
| `contact_state` | `physical_contact_confirmed · near_contact · occluded_contact · editorial_impact · unknown` |
| `force` | optional `{relative_to: anchor id or null, step, direction}` (same enums as WO-01) |
| `primary_reaction` | string |
| `secondary` | array of strings |
| `settle` | string |
| `depends_on` | array of event ids |
| `must_not_imply` | array of strings |
| `risk` | `low · medium · high` |
| `pathway_stage` | optional string |
| `origin` | origin enum |

## Check rules (errors; exact substrings)

1. Two events on one beat → `"one causal event per beat"`.
2. Unknown beat → `"event references unknown beat"`.
3. `depends_on` names an unknown event, or one whose beat is not earlier → `"depends_on"`.
4. `force.relative_to` names an unknown anchor, or an anchor not earlier than the event's beat →
   `"force anchor"`.
5. Empty `contact_surface`, `primary_reaction` or `settle` (after strip) → `"edge admission"`.
6. `contact_state` is `near_contact` and `primary_reaction` is non-empty **and** `must_not_imply`
   is empty → warning `"near contact with a reaction: state what must not be implied"`.

## Emit rules

One sentence pair per event, placed directly after its beat's sentence, source kind `event`:

`"<Actor>'s <part> <action><force clause>, landing on <contact_surface>. <Primary reaction> as
<secondary joined with ' and '>, then <settle>."`

- `<force clause>`: empty when `force` is absent; otherwise `", <comparison> than <anchor label>"`
  using the `weight` or `intensity` words from WO-01.
- No `secondary` → drop the " as …" part. Capitalise sentence starts; strip trailing full stops
  from the inputs before joining.
- `contact_state`: `near_contact` → replace "landing on" with "passing just short of";
  `occluded_contact` → "reaching <contact_surface> out of the camera's view";
  `editorial_impact` → omit the landing clause and start the second sentence with "Cut to: ".
- Events are locked and not droppable. No short form in this slice.
- `verdict.md` for a run: append one checklist block per event (contact happened? reaction
  followed? end pose sane?) and one line per `must_not_imply`. Do this in the run work orders, not
  in code.

## Tests to add (new class `CausalEvents`)

- `test_two_events_on_one_beat_fail`
- `test_event_depends_on_later_event_fails`
- `test_force_anchor_must_exist_and_be_earlier`
- `test_empty_reaction_or_settle_fails_edge_admission`
- `test_emit_orders_cause_contact_reaction_settle` (assert the four parts appear in that order
  in the prompt)
- `test_near_contact_changes_landing_wording`
- `test_must_not_imply_is_never_emitted`

## Acceptance

All earlier tests green and unmodified; seven new tests green; run 001 unchanged and GREEN.

## Records

`QUEUE.md` · `plan/TASKS.md` (T35 "first slice done; degradation, eval-log fields and failures
registry remain") · `plan/CONTROL_LAYER.md` R-41, R-42, R-44 status · `plan/STATUS.md`.

## Stop if

A run needs two causal events on one beat. Split the beat instead; if that breaks the fit, write
it under Blocked.
