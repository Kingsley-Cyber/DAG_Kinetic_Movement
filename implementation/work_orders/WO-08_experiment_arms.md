# WO-08 — Experiment arms: absolute vs relative, wording rungs (T18; EXPERIMENTS E2, E3)

## Goal

Produce the prompt files the owner renders for E2 and E3, from one IR, without hand-editing
prompts.

## Read first

`plan/EXPERIMENTS.md` (common rules, E2, E3) · WO-01 result ·
`/Users/king/Downloads/Additional/TERMINAL_DESCENT_FIGHT_IR_v1.json` (the owner's fight IR; read
only; if the file is missing, stop).

## Decisions already made

- One beat only: the interception. Clip length: the shortest duration the profile lists, or 6 s
  when the profile has none.
- Arms are fair: no multipliers, newtons, metres per second or g-forces in any arm.
- Arms differ only in the targeted wording; entities, camera and everything else are identical.

## Part A — emitter flags (tests first)

1. `emit --magnitudes relative|absolute` (default `relative`). In `absolute` mode a beat's
   `relative` deltas are written as the bare word instead of a comparison ("faster than the first
   reach" → "fast"; use the WO-01 table's `more` column stem: fast, heavy, wide, big, intense,
   far, quick; `less` column: slow, light, tight, small, gentle, close, slow) and anchor
   sentences are omitted. The lint is not run on emitted text.
2. `emit --rung numeric|term|visible` (default `visible`) for controls whose value has Laban
   scale keys: `visible` = today's behaviour; `term` = "Effort: <weight pole>, <time pole>,
   <space pole>, <flow pole>" using pole names (light/strong, sustained/sudden, indirect/direct,
   free/bound; a scale between 0.4 and 0.6 is omitted); `numeric` = a one-line block
   `effort {weight: 0.8, time: 0.9, space: 0.9, flow: 0.2}`.
3. `emit --out <dir>` writes the outputs into that directory instead of the run folder root.

Tests (new class `ExperimentArms`): `test_absolute_mode_drops_anchor_and_comparison`,
`test_relative_mode_is_default_and_unchanged`, `test_rung_term_names_poles`,
`test_rung_numeric_prints_scales`, `test_out_dir_receives_all_outputs`.

## Part B — the run

`director/runs/006_interception_arms/`: write the ask (the interception beat in plain words, in
the owner's fight setting: Mara blocks Veyr from the reactor core), IR with an anchor on the first
beat (Veyr's steady walk as a visible fact), deltas for Mara's speed and the hit, one physics
event, a camera control from the catalog. `check` GREEN. Then:

```
emit … --magnitudes relative --out director/runs/006_interception_arms/arms/E2_relative
emit … --magnitudes absolute --out director/runs/006_interception_arms/arms/E2_absolute
emit … --rung visible --out …/arms/E3_visible
emit … --rung term    --out …/arms/E3_term
emit … --rung numeric --out …/arms/E3_numeric
```

`verdict.md`: a table with one row per arm and seed (three seeds), the three yes/no questions
and the adherence scores, plus the E2 and E3 decision rules copied from `EXPERIMENTS.md`.

## Acceptance

Five new tests green, all earlier tests green and unmodified; five arm folders each with
`prompt.txt`, `receipt.json`, `loss.jsonl`; a diff between the two E2 prompts shows only the
magnitude wording and anchor sentences differ.

## Stop if

The fight IR file is missing or unreadable: write that under Blocked; do not invent the fight.
