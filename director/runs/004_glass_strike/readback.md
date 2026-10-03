# Cold read-back — run 004 (seedance profile, 2026-10-02)

A separate LLM call (Haiku, no tools) saw only `prompt.txt` and the five instructions. Raw record in
`readback_raw.md`. The call was launched by the session that wrote the IR; it is a different model
call, not an independent human reader.

## Beat order: MATCH

The reader's 16 items collapse onto the IR's five beats in the same order: b1 Ines spins toward the
table, right arm swinging out → b2 the swing carries the right forearm across the table edge and
knocks into the glass, the glass tips and slides off, spinning once → b3 airborne, falls, meets the
tile, bursts apart, pieces skid, spin and settle, lie still → b4 Theo turns toward the sound and
steps back (listed after the break, before the camera moves) → b5 pan right to Theo, tilt down,
the broken glass lies scattered and still. Nothing missing, nothing reordered.

## Causal order and state changes: MATCH

Glass: upright on the table edge → knocked → tips and slides off → airborne → impact → bursts into
pieces → pieces skid, spin, settle → lie still and scattered. The break follows the floor contact.
Theo: standing → turns → steps back, listed only after the pieces lie still, so his reaction comes
after the break. The shards are present at the end (item 16) and nothing on the table.

## Camera: MATCH

Medium-wide at standing height, standard lens; Ines and the table on the left, Theo small in the
doorway on the right, the floor in front of the table in frame; static until the break, then a pan
right from Ines to Theo settling with Theo centered in the doorway, then a tilt down that lands on
the broken glass. Order of the two moves correct; no cut, no zoom.

## Findings for the emitter / IR (not fixed in this run; evidence first)

| Finding | Cause | Follow-up |
|---|---|---|
| "The table stands screen-center" read as contradicting "beside a wooden table" at screen-left | the entity line puts Ines beside the table, the staging control puts the table at screen-center | next IR edit: say "Ines stands screen-left, the table to her right at screen-center"; no change now because order, state and camera all match |
| "Theo stays still, turns toward the sound and steps back" read as self-contradictory | the still hold is the stand-in for the reaction latency | wording variant: "after a moment's stillness, Theo turns..." (a latency wording treatment, not an emitter change) |
| "both keep their clothes and sides" read as a dangling pronoun | `c_shards` short form merges the pieces and the actors' locks | split the lock or drop the actors' half |
| "glass drops toward the tile floor" and "pieces lie still" / "lies scattered and still" read as repeats | beat, event and final beat each state the same moment | known (runs 001 to 003 dedup finding, T21 after the kill check) |
| "In order: ..." read as a redundant summary | `interaction.contact_causal_chain` | known |
| The reader's count (~374 words) is close to the real count | — | 352 words / 1,997 characters against third-party Seedance guidance of 60–100 words: Phase 2 lean-vs-full renders |

Verdict for the exit test: the read-back lists the same beats in the same order, Theo's reaction
after the break, the two camera moves in order, and the shards visible at the end. PASS
(read-back MATCH). Nothing was dropped for budget; eleven lines were compressed to short wording.
