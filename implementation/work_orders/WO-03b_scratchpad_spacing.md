# WO-03b — Shared scratchpad, pass views, spacing (R-58, R-60; T33 first slice)

## Goal

Make the run folder a real shared scratchpad: a pass gets its view, proposes, is validated, and
only then is accepted; open items are tracked; validation results are saved. Add spacing to beats.

## Read first

`plan/ARCHITECTURE.md` §2.8, §2.9, §4.3a · `plan/CONTROL_LAYER.md` R-51, R-58, R-60 ·
`director/protocol.md` §4·1 · WO-03 result (`reads` in `passes.yaml`).

## Decisions already made

- No new store: the scratchpad is the run folder.
- Agent-run stays the default: these commands are what a session calls between passes. They are
  also the pieces an orchestrator loop would call later; do not build the loop.
- `open.jsonl` and `check_report.json` are optional for old runs (run 001 has neither and stays
  valid).

## Changes

1. `director.py pack <run_dir> <pass>` prints JSON: the pass entry from `passes.yaml` (question,
   owns, sub-modules, notes), the IR areas named in its `reads` (present values only), all locked
   controls, the treatments under `treatments/<pass>/` (id, triggers, not_when, `from`), and the
   open items addressed to this pass. For `camera` it also includes the move ids and `function`
   hints from `vocab/camera_moves.yaml`.
2. `director.py check <run_dir> --pass <pass>` runs only the rules whose inputs that pass owns
   (map rule → owner pass in one table in the code) and reports the rest as `not_applicable`.
   Without `--pass` behaviour is unchanged.
3. `check` (full) writes `check_report.json` in the run folder: `{ok, errors, warnings, outcomes,
   fit, checked_at}`. `--no-write` suppresses it (tests use it so fixtures stay clean).
4. `open.jsonl` lines: `{"id", "kind": "alternative" | "conflict" | "revision_request", "from_pass",
   "to_pass", "field", "reason", "status": "open" | "resolved" | "escalated", "resolution"}`.
   `emit` refuses when any line has `status: open` and kind `conflict` or `revision_request` →
   error `"open items block emit"`. Malformed lines → `"open.jsonl line"`.
5. Schema: optional `spacing` (`ease_in, ease_out, ease_in_out, even`) and `pose_role`
   (`key, extreme, breakdown`) on a beat; optional `variant_id` at the top level.
6. Warning `"constant motion"`: the action pass is active and no beat declares `spacing`, or every
   declared spacing is `even`.
7. Emit: a beat with `spacing` gets a clause from this table appended to its sentence:
   `ease_in` → "starting slow and accelerating"; `ease_out` → "arriving fast and settling";
   `ease_in_out` → "easing in and out"; `even` → no clause.

## Tests to add (new class `Scratchpad`)

- `test_pack_returns_reads_locks_treatments_for_pass`
- `test_pack_camera_includes_move_functions`
- `test_check_pass_limits_rules_and_marks_others_not_applicable`
- `test_check_writes_report_and_no_write_suppresses_it`
- `test_open_revision_request_blocks_emit`
- `test_resolved_items_do_not_block_emit`
- `test_constant_motion_warns_when_action_active_and_no_spacing`
- `test_spacing_clause_is_emitted`

## Acceptance

All earlier tests green and unmodified; eight new tests green; run 001 `check` GREEN and
`prompt.txt` byte-identical (no spacing or open items there).

## Records

`QUEUE.md` · `plan/CONTROL_LAYER.md` R-58, R-60 · `plan/TASKS.md` T33 (pack done; index still
later) · `plan/STATUS.md`.

## Stop if

The rule-to-owner table cannot place a rule under exactly one pass: list the rule under Blocked
rather than assigning it to two.
