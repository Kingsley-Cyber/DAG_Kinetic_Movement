# WO-01 — Relative prompting: anchors, comparisons, magnitude lint (T16, R-16)

## Goal

Make relative prompting a compile invariant at the IR level and a lint at the wording level.
The IR can declare anchors; beats can declare a delta against an anchor; the emitter writes the
anchor once and then a comparison in words; the checker warns on bare magnitude words.

## Read first

`plan/ARCHITECTURE.md` §3.5.3 · `plan/CONTROL_LAYER.md` R-16 · `plan/EXPERIMENTS.md` E2 ·
`director/tools/director.py` (functions `check`, `emit`, `assemble`) ·
`director/tools/tests/test_director.py` (pattern: `TempRun`, `errors_for`).

## Decisions already made

- New fields are optional. Run 001 is not edited; tests add anchors through `TempRun` mutation.
- A delta always points at an anchor, never at another delta, so chains cannot exist.
- The wording check is a **warning**. It never fails `check`.
- Multipliers and physical units are never emitted; the emitter writes words.

## Schema (`director/ir.schema.json`)

Add top-level optional `anchors` (array of objects, `additionalProperties: false`):

| Field | Type | Rule |
|---|---|---|
| `id` | string | unique |
| `quality` | enum | `speed, weight, reach, size, intensity, distance, tempo` |
| `beat` | string | id of the beat where the baseline is seen |
| `label` | string | short phrase used to refer back, e.g. "the first cast" |
| `description` | string | a visible fact, at least 20 characters |

Add optional `relative` on a beat (array of objects):
`{quality (same enum), relative_to (anchor id), step: slightly | more | much, direction: more | less}`.

## Check rules (errors; exact substrings the tests look for)

1. `relative_to` names no anchor → `"unknown anchor"`.
2. The anchor's beat is later than the beat carrying the delta → `"anchor is not earlier"`.
   (Same beat is also an error: an anchor cannot be compared with itself.)
3. Two `relative` entries with the same `quality` on one beat → `"one escalation per quality"`.
4. An anchor whose `quality` differs from the delta's `quality` → `"quality mismatch"`.
5. Anchor `beat` not a known beat → `"anchor references unknown beat"`.

## Check rule (warnings)

Scan beat `description` and `short`, entity `description`, and string control values. Split into
sentences. Warn `"bare magnitude word '<w>'"` when a sentence contains one of
`fast, heavy, powerful, strong, wide, hard, big, exaggerated` as a whole word, does not contain
the word `than`, and the word is not inside an allowed phrase:
`slow motion, real-time, speed ramp, time-lapse` plus every string in the active profile's
`defaults_to_counter` (profile is known only in `emit`; in `check` use the fixed list).
Record both word lists as module constants with a comment "convention (R-16); promoted by E2".

## Emit rules

- An anchor adds one sentence directly after its beat's sentence: the `description`, ending with
  a full stop. Receipt source: `{"kind": "anchor", "id": ..., "origin": "PROJECT_DERIVED"}`.
  Locked, not droppable, no short form.
- A beat with `relative` gets a clause appended to its sentence: `", <comparison> than <label>"`.
  Comparison words:

  | quality | more | less |
  |---|---|---|
  | speed | faster | slower |
  | weight | heavier | lighter |
  | reach | wider | tighter |
  | size | bigger | smaller |
  | intensity | more intense | gentler |
  | distance | farther | closer |
  | tempo | quicker | slower |

  `step`: `slightly` → "slightly <word>", `more` → "<word>", `much` → "much <word>".
  Several deltas on one beat join with " and ".
- The same clause is appended to the beat's `short` form when it is used.

## Tests to add (new class `RelativePrompting`)

- `test_unknown_anchor_reference_fails`
- `test_anchor_not_earlier_than_delta_fails`
- `test_two_deltas_same_quality_on_one_beat_fail`
- `test_quality_mismatch_fails`
- `test_bare_magnitude_word_warns_but_check_stays_green` (inject "she moves fast" into a beat)
- `test_named_technique_does_not_warn` ("slow motion on the pour")
- `test_comparative_with_than_does_not_warn` ("faster than the first reach")
- `test_emit_writes_anchor_once_then_comparison` (anchor on b2 quality speed label "the first
  reach"; delta on b5 `{speed, slightly, less}` → prompt contains the anchor description exactly
  once and "slightly slower than the first reach"; receipt has a line with source kind `anchor`)

## Commands

```
python3 -m unittest discover -s director/tools/tests
python3 director/tools/director.py check director/runs/001_bottle_selfie
python3 director/tools/director.py emit director/runs/001_bottle_selfie --model seedance
```

## Acceptance

All previous tests green and unmodified; the eight new tests green; run 001 `check` GREEN and its
`prompt.txt` byte-identical to before this work order (anchors are optional and unused there).

## Records

`QUEUE.md` WO-01 done · `plan/TASKS.md` T16 done · `plan/CONTROL_LAYER.md` R-16 status ·
`plan/STATUS.md` entry · protocol §4·0 already describes the rule; add the field names there.

## Stop if

The comparison table cannot express something a run needs (write the case under Blocked).
