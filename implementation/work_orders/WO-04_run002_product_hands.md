# WO-04 — Run 002: product handling with two hands (T12; handoff test)

## Goal

Run a second ask end to end as the reasoning LLM, using only the protocol and the treatments.
This is the handoff test: every point where you had to guess is a finding.

## The ask (verbatim)

> A man unboxes a pair of wireless earbuds at a desk, opens the charging case and puts one earbud
> in his ear, 8 seconds, shot on a phone held by a friend.

Target model: `seedance`.

## Read first

`director/protocol.md` (all) · `director/passes.yaml` · `director/runs/001_bottle_selfie/` (the
worked example: ask, ir, decisions, readback, readback_raw, verdict) · the treatments under
`director/treatments/` · `Additional/HANDS_CONTACT_MANIPULATION.md` §1–§3, §5, §7 ·
`Additional/CAPTURE_SURFACE_REALISM.md` §4–§5 · `director/vocab/camera_moves.yaml`.

## Decisions already made

- The phone is held by a friend, so both of the man's hands are free; the camera is `handheld`
  from the catalog (not the selfie treatment).
- Three physical tasks in 8 s is likely OVERLOADED. Run `check`; if it is, resolve it in the open
  with the options `check` prints (cut, overlap, split, lengthen) and record the choice in
  `decisions.jsonl`. Do not shrink `min_s` values to make it fit.
- Use anchors (WO-01) for at least one quality, and a physics event (WO-02) for the case opening
  (trigger: thumb, contact surface: case lid, primary reaction: lid swings up).
- New treatments are allowed only where no existing one fits; each needs ≥ 3 triggers, `from`,
  `backs` (use `cpcs.contact.interaction_lifecycle` and `cpcs.mx.affordance_constraints` where
  apt), origin, `core` and `core short` wording, failure signs, effects (unverified).

## Steps

1. `director/runs/002_earbuds_unbox/ask.md`: the ask, intent brief, pass plan summary.
2. `ir.json` and `decisions.jsonl` by the protocol. Every INFERENCE → `director/gaps.jsonl`.
3. `check` until GREEN. Fix the IR, never the prompt.
4. `emit --model seedance`. Read `emit_report.json`: note drops and compressions.
5. `baseline.txt`: the ask, verbatim.
6. Cold read-back: a separate call (subagent) that sees only `prompt.txt` and the five
   instructions in `runs/001_bottle_selfie/readback_raw.md`. Save the input and the full response
   in `readback_raw.md`; write the comparison in `readback.md` (beat order, state changes, camera:
   MATCH or the differences). A mismatch → repair the IR with the smallest change and repeat 3–6.
7. `verdict.md`: copy run 001's template; add the per-event checklist (contact happened, reaction
   followed, end pose sane) and any `must_not_imply` lines.
8. In `plan/STATUS.md` list **every guess you had to make** (what the protocol or a treatment did
   not specify), with file and line where the gap is.

## Acceptance

`check` GREEN; prompt within the profile limit; receipt complete; read-back MATCH on beat order
and state changes; guesses listed; no existing test changed; all tests green.

## Stop if

`check` stays RED after two repair rounds for a reason you cannot fix in the IR: write the error
and your reading of it under Blocked.
