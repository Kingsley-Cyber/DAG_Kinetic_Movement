# Run 005 — kitchen at dawn (camera-only, no performer)

## Ask

> A slow reveal of an empty kitchen at dawn as light moves across the counter, 6 seconds.

Target model: seedance (route unconfirmed; 2,000-character budget from third-party API docs, see
`profiles/seedance.yaml`).

## Intent brief

Locked by the user: an empty kitchen, dawn, light that moves across the counter, a slow reveal,
6 seconds. Open: the room's layout, the objects on the counter, the colour of the light, where
the window is, where the camera starts, the aspect ratio, the look. Implied: nobody appears; the
only thing that changes in the world is the light; the camera does the revealing.

Forced decisions. (1) No performer: no hands ledger entries, no pathways, no physics events.
(2) The world's change is the content: three beats, owned by time, each a state of the light
(it reaches the counter edge; it crosses the counter; it settles on the far wall), described as
what the camera sees. (3) One camera move chosen by function ("reveal") from the catalog:
`dolly_out`, a physical move backward that lets more of the room enter the frame; alternatives
in `decisions.jsonl`. (4) Layout: the window is in the left wall, the counter runs away from the
camera along that wall, the far wall faces the camera; the camera starts close at the counter's
near end. (5) The light's pace is carried by the beats and by the camera's `speed` field; no
comparison of two paces is made, so there are no anchors.

## Pass plan summary

Active: intent, entity, world (the light is an environment state that changes), time, camera,
light_color, style, synthesis. Continuity is also active (the room stays empty and unmoved).
Inactive with reason: action, interaction, physics, staging, performance, attention, audio.
A 6-second video clip, one continuous take, no cuts.
