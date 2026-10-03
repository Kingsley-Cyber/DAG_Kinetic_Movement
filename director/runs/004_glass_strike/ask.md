# Run 004 — glass strike (the DMR shared fixture)

## Ask

> Actor A rotates toward a table and accidentally strikes a drinking glass with the right
> forearm. The glass leaves the table, breaks on the floor, and the shards persist. Actor B
> notices the impact after a short reaction delay. The camera reframes to Actor B, then reveals the
> broken glass. 8 seconds.

Target model: seedance (route unconfirmed; 2,000-character budget from third-party API docs, see
`profiles/seedance.yaml`). Source of the fixture: `plan/INGEST.md` §4, `plan/ingest/DMR_triage.md`.

## Intent brief

Locked by the user: two actors (A and B); A rotates toward a table; the right forearm strikes a
drinking glass by accident; the glass leaves the table, breaks on the floor and the shards
persist; B notices after a short delay; the camera reframes to B, then reveals the broken glass; 8
seconds. Open: names, clothes, room, floor, camera height, aspect ratio, the look. Implied: no one
is hurt; the strike is a glancing accident, not a swipe.

Forced decisions. (1) Names and sides: A is Ines, screen-left; B is Theo, screen-right in a
doorway; the table is between them, nearer Ines. (2) Two contacts on separate beats (forearm on
glass, glass on floor), each with a pathway and one physics event; the break `depends_on` the
strike. (3) Theo's reaction is a later beat caused by the break; the latency is order and a still
hold, never a number of milliseconds. The exact-millisecond request is kept as an unlocked control
the profile cannot honour (`c_latency`, capability `unsupported`), so the loss ledger shows it.
(4) Two camera moves, each scoped to a beat: pan right to Theo, then tilt down to the floor. (5)
The shards persist as a continuity lock.

## Pass plan summary

Active: intent, entity, world, interaction, physics, staging, continuity, time, camera, synthesis.
Inactive with reason: action (covered by interaction and physics), performance (no register
asked), attention (nothing withheld), light_color, style, audio (not asked).
