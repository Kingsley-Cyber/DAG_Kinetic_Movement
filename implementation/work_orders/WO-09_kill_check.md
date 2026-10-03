# WO-09 — Kill check and effects (T13 result, T14) — only after GATE A

## Goal

Read the owner's verdicts, decide whether the approach continues, and write the evidence back
into the treatments.

## Read first

Every `director/runs/*/verdict.md` · `plan/EXPERIMENTS.md` · `plan/PHASES.md` (kill criteria,
render evidence procedure).

## Steps

1. For each filled verdict, append one line per rendered arm to `director/runs/ledger.jsonl`:
   `{run, arm, model, route, version, seed, prompt_sha256, ir_sha256, scores: {…}, events: [{event_id,
   contact_happened, reaction_followed, end_pose_sane}], verdict, notes}`. Hashes come from
   `receipt.json` and the IR file bytes. Missing scores stay `null`; do not fill them in.
2. **E1 kill check.** A run counts for the compiled prompt when the owner's overall line says
   compiled beats baseline. Compiled wins on most runs (at least 3 of 5) → continue. Otherwise
   write "KILL CHECK FAILED" at the top of `plan/STATUS.md` with the per-run table, and stop: no
   further work orders.
3. **E2, E3** decisions by the rules in `EXPERIMENTS.md`; record each in `plan/DECISIONS.md` and
   update `director/profiles/<model>.yaml` (`defaults_to_counter`, default rung) with
   `evidence: measured` and the run ids.
4. **Effects.** For each treatment used by a rendered run, update its `## Effects` lines:
   evidence_status supported / contradicted / inconclusive, model, run ids. Change wording of a
   treatment only if a verdict names the failure it caused; record the change.
5. `director/failures.jsonl`: one line per failure sign the owner noted
   (`{run, event_or_beat, failure, class: vocabulary_gap | ceiling | unknown, hypothesis}`).
6. If the kill check passed, write the Phase 3 work orders (T20–T29, T39) in this folder in the
   same format, ordered by which failures the verdicts showed, and add them to `QUEUE.md`.

## Acceptance

Ledger lines for every rendered arm; a clear continue or stop in `STATUS.md`; treatments and
profiles updated only from recorded verdicts.
