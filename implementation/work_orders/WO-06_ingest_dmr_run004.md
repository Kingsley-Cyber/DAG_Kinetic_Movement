# WO-06 — First ingest (DMR package), run 004 glass fixture, camera move validator (T36, T38)

## Goal

Run `plan/INGEST.md` on the owner's DMR research once, land its implementable claims as rules,
and prove them on the DMR shared fixture.

## Read first

`plan/INGEST.md` (all, especially §4 the pre-triaged table) ·
`Additional/06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md` ·
`Research_distillation_folder/research/continue_detail/director_motion_reasoning_complete_package/`
(find its gap register and decision tables; read only those and the sections they point to) ·
`cpcs/runtime/06_canonical/temporal_tracks/temporal_coupling.md` ·
`director/vocab/camera_moves.yaml` · `plan/CONTROL_LAYER.md` R-50…R-53.

## Part A — triage (no code)

Write `plan/ingest/DMR_triage.md`: one row per gap G001–G022 with status (closed,
implementable_now, requires_experiment, unknown, deferred, rejected), the reason, and where it
lands. Start from INGEST §4; correct it where the package says otherwise; recover G010, G018 and
G022 from the package's register, do not infer them from numbering.

## Part B — rules (code, tests first)

1. **Typed outcomes (R-51).** `CheckResult` gains `outcomes`: a list of
   `{rule, outcome, detail}` with outcome in `pass, fail, indeterminate, not_applicable,
   unobservable`. Existing errors map to `fail`; a rule that could not run because its input is
   absent records `not_applicable`; the fit verdict with no duration records `indeterminate`.
   `--json` prints them. Existing `errors`/`warnings` lists and messages stay exactly as they are.
2. **Camera move validator (R-53).** A camera control whose value has key `move`: the id must be
   in `camera_moves.yaml` or be `custom` (then a decision record with that control id must exist
   in `decisions.jsonl`) → error `"unknown camera move"`. If the catalog entry's `layer` is
   `optics` and the control's value text contains "camera moves", "moves the camera", "dolly" or
   "track" → error `"optics written as camera motion"`. Two camera controls with `move` and no
   `beat` → error `"one camera move per shot"`.
3. **Profile lifecycle (R-52).** `emit` reads `status` from the profile: `reprobe_due` or
   `invalidated` → block native dispositions with `"profile status"`. `stale` → warning.

Tests (new class `IngestDMR`): `test_outcomes_include_not_applicable_and_indeterminate`,
`test_unknown_camera_move_fails`, `test_custom_move_needs_decision_record`,
`test_zoom_written_as_motion_fails`, `test_two_unscoped_moves_fail`,
`test_invalidated_profile_blocks_native`.

## Part C — run 004 (the DMR shared fixture)

> Actor A rotates toward a table and accidentally strikes a drinking glass with the right forearm.
> The glass leaves the table, breaks on the floor, and the shards persist. Actor B notices the
> impact after a short reaction delay. The camera reframes to Actor B, then reveals the broken
> glass. 8 seconds.

Decisions already made: two actors with stable ids and named sides; physics events on separate
beats (forearm strikes glass; glass hits floor and breaks); B's reaction `depends_on` the break
and comes **after** it (latency as order, not a number of milliseconds); shards persist
(continuity lock); two camera controls scoped to beats (reframe to B, then reveal the glass) with
catalog moves; at least one control is given `capability: unsupported` on this profile with an
honest reason (for example an exact reaction latency in milliseconds, `exactness: exact`,
unlocked) so the loss ledger shows a non-semantic disposition. Procedure and acceptance as WO-04
steps 1–7, folder `director/runs/004_glass_strike/`.

## Acceptance

Triage table complete with reasons; six new tests green and all earlier tests green and
unmodified; run 004 `check` GREEN, read-back MATCH with B's reaction after the break and the
shards visible at the end; `plan/INGEST.md` §4 corrected where the package differed.

## Stop if

The package has no gap register you can find: list what you searched under Blocked.
