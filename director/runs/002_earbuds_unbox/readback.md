# Cold read-back — run 002 (seedance profile, 2026-10-03)

A separate LLM call (Haiku, no tools) saw only `prompt.txt` and the five instructions. Raw record in
`readback_raw.md`. The call was launched by the session that wrote the IR; it is a different model
call, not an independent human reader.

## Beat order: MATCH

The reader's 20 micro-beats collapse onto the IR's 8 beats in the same order:
b1 reach and grip the lid (reader 2) → b2 lid lifted and set beside the box, case shown (3–4) →
b3 left hand wraps the case (5) → b4 case lifted out, held upright in the left palm (6–7) →
b5 thumb push, lid swings up, earbuds show (8–10) → b6 right hand pinches one earbud and draws it
out (11–12) → b7 earbud raised to the right ear and pressed in (13–16) → b8 hand lowers, faint nod,
hold (17–20). Nothing missing, nothing extra, no reorder.

## State changes: MATCH

Box lid on → off → beside the box; case covered → visible → gripped → lifted out → upright in the
palm → lid open; one earbud in slot → pinched → drawn out → in the ear; the other earbud stays in
the case. All match the pathways p_unbox, p_takeout, p_open, p_ear. The reader's "right earbud" and
"left earbud" labels are its own; the IR does not say which of the two earbuds is taken.

## Camera: MATCH

Handheld medium shot from the front, held by the friend, responsive and organic, finishing on the
man with the earbud in; iPhone main camera, 30 fps, flat HDR, deep focus, no bokeh, sensor noise,
no grade, visible skin pores. The IR's framing (face, both hands, desk readable) was compressed away
by the budget; the reader still reported "medium shot".

## Findings for the emitter / IR (not fixed in this run; evidence first)

| Finding | Cause | Follow-up |
|---|---|---|
| The case opening is stated three times (beat b5, anchor sentence, physics event) | beat, anchor and event each emit a sentence for the same moment | beat b5 could carry only the lead-in when an event covers it; a dedup pass (same finding as run 001) |
| "slightly gentler than the thumb push" read as unclear reference | the anchor sentence is emitted right after b5 but the comparison sits two sentences later, after the b6/b7 beat lines | emit the comparison next to the anchor label, or restate the anchor label |
| "reaching the opening of his right ear out of the camera's view" read as awkward | occluded_contact template: "<cause>, reaching <surface> out of the camera's view" | wording variant for body-part surfaces |
| The closing summary line restates the grips | `c_grip` and `c_chain` both emitted | dedup pass |
| 374 words / 1,987 characters vs third-party Seedance guidance of 60–100 words | full IR emitted as prose, budget filled to the limit | Phase 2 lean-vs-full renders |

Verdict for the exit test: the read-back lists the same beats in the same order and the same state
changes. PASS (read-back MATCH). `c_register` (acting register), `c_pace` and `c_negatives` were
dropped for budget, so the prompt carries no performance direction beyond "nods faintly".
