# Cold read-back — run 003 (seedance profile, 2026-10-02)

A separate LLM call (Haiku, no tools) saw only `prompt.txt` and the five instructions. Raw record in
`readback_raw.md`. The call was launched by the session that wrote the IR; it is a different model
call, not an independent human reader.

## Beat order: MATCH

The reader's list (it numbered 23 camera-seen items) collapses onto the IR's six beats in the same
order: b1 step up, raise both hands, light tap on the chest, rocks back on his heels, steps forward
laughing → b2 plants the front foot, swings both arms forward, palms drive onto the chest, upper
body rocks back, arms fly out, heels slide off the edge, starts to fall → b3 tips backwards over the
water and drops → b4 enters back first fully clothed, back and shoulders on the surface, crown of
water, spray over the edge, goes fully under, bubbles rise → b5 surfaces and shakes the water from
his hair → b6 treads water laughing, wiping his face, looking at his friend. Nothing missing, nothing
reordered.

## Causal order and state changes: MATCH

Both contacts are read as cause → contact → reaction → settle in order: the tap (rocks back, then
upright again) before the shove ("pushed hard", rocks back, heels slide off, falling), and the entry
(surface hit) before the splash ("water erupts in crown", spray, under, bubbles). Wet state after
surfacing is read: clothes dry → soaked and clinging, hair dry → wet, both persistent; the pool
"rocking continues". The splash comes after the entry, the wet state after the surfacing.

## Camera: MATCH

Handheld, medium-wide, from the lawn side at chest height, standard lens, responsive and organic;
man in red screen-left, friend screen-right with the pool behind, action running left to right into
the water; ends on the friend treading water with the man in red still in frame.

## Findings for the emitter / IR (not fixed in this run; evidence first)

| Finding | Cause | Follow-up |
|---|---|---|
| "arriving fast and settling" and "easing in and out" were read as ambiguous (the reader asked what settles, and whether "easing in and out" meant treading) and listed as items of the action | the spacing clause is appended to a beat sentence without saying what it describes (`diremit.py` `SPACING_CLAUSE`) | wording variant that names the motion ("the push arrives fast and settles"), or drop `ease_in_out` on a rising beat; no IR change made because beat order, state and camera all match |
| "nothing changes before it is touched" read as a mid-prompt rule | `interaction.contact_causal_chain` short form | known (runs 001 and 002 dedup finding) |
| The tap and the shove were read as the same arms described twice with different force | anchor sentence and event sentence each state a palms contact | intended: the second is "much more intense than the first nudge"; the reader did read it as the intense one |
| "the pool keeps rocking" read as vague | `continuity.wet_state` short form | the full form says "rocking in widening ripples"; budget chose the short |
| The reader's count (680–720 words) is about double the real 359 words | the reader counted its own list items | none; the count is not used |
| 359 words / 1,968 characters vs third-party Seedance guidance of 60–100 words | full IR emitted as prose | Phase 2 lean-vs-full renders |

Verdict for the exit test: the read-back lists the same beats in the same order, the splash after the
entry, and the wet state after surfacing. PASS (read-back MATCH). `c_laugh`, `c_pace` and
`c_negatives` were dropped for budget, so the prompt carries no performance direction beyond
"laughing" in the tap anchor and in b6.
