# Cold read-back — run 005 (seedance profile, 2026-10-02)

A separate LLM call (Haiku, no tools) saw only `prompt.txt` and the five instructions. Raw record in
`readback_raw.md`. The call was launched by the session that wrote the IR; it is a different model
call, not an independent human reader.

## Light's three states, in order: MATCH

The reader's 8 items collapse onto the IR's three beats in the same order: b1 a thin band of
sunlight appears at the counter's near edge (item 1) -> b2 the light spreads along the counter away
from the camera, over the bowl and the kettle, long shadows (items 2-4) -> b3 the light leaves the
far end of the counter and settles as a bright patch on the plaster far wall, then holds (items
5-7). Nothing missing, nothing reordered. The reader lists the bowl before the kettle; the prompt
says "the bowl and the kettle" in that order.

## Object states: MATCH

Kettle and bowl: present and stationary throughout. Light: thin band at the near edge -> spreads
along the counter -> reaches the far end -> bright patch on the far wall -> holds. The reader adds
"absent/dim at start" (an inference from "the rest of the room dim"; harmless).

## Camera: MATCH

Moving: a slow, smooth, steady dolly backward in a straight line away from the counter's near end,
easing to a stop on the final beat; low close framing at counter height, standard lens, opening on
the counter edge and the window and ending wider with the counter and the lit patch both visible;
height and lens direction constant; no zoom, no cut. Light from the window in the left wall, low,
warm, hard-edged; real footage, ungraded, deep focus. Camera grammar states where (opening frame),
movement, lens and end.

## Performer language: none

The reader listed no person, hand, body or action word. The only mention of people is the
negation ("no person, hand or animal appears"), which the reader did not turn into a beat.

## Findings (not fixed in this run; evidence first)

| Finding | Cause | Follow-up |
|---|---|---|
| "settles" and "stays there" read as a repeat | beat description plus the key pose line | known duplication (runs 001-004 dedup finding, T21 after the kill check) |
| "the window above it" and "under the window" read as the same fact worded twice | entity line puts the counter under the window; the framing control puts the window above the counter edge | wording only; layout is consistent |
| "nothing in the room moves", "the room stays empty" read as stated three times | `c_world_light` and `c_room_lock` both lock the room | merge the two locks in a later IR edit; order, state and camera all match, so no change now |
| "close", "near end", "counter height" read as three specs | `c_cam_frame` packs three framing facts | none |
| the camera retreat is described as "continues retreating" after the light settles, so the reader treats the move as spanning all beats | the move is unscoped on purpose (one move per shot) | none |

Verdict for the exit test: the read-back lists the light's three states in order, the held end
state, one backward camera move that ends wider, and no performer. PASS (read-back MATCH). Nothing
was dropped for budget; two lines (`b1`, `c_light`) were compressed to short wording.
