# Cold read-back — run 001 (seedance profile, 2026-10-02)

A separate LLM call (Haiku) saw only `prompt.txt` and listed what it expected to see.

## Beat order: MATCH

Reader's 15 micro-beats collapse onto the IR's 7 beats in the same order:
b1 settle → b2 reach and grip → b3 twist → b4 cap free + ripple → b5 raise (eyes to bottle, cap
lowered) → b6 drink, two swallows, level drops → b7 lower, exhale, glance to lens, hold.

## State changes: MATCH

cap on → turning → off and held in fingers; water surface still → ripple at release; water level
drops only during swallowing. No state change appeared that the IR does not contain; none missing.

## Camera: MATCH

Static propped phone, medium close-up, slightly low angle, deep focus, no bokeh, 30fps, flat HDR,
sensor noise, ungraded, skin texture visible.

## Findings for the emitter (not fixed in this run; evidence first)

| Finding | Cause | Follow-up |
|---|---|---|
| Action sequence stated twice (beats, then the grip and chain controls) | emit does not detect wording already carried by a stronger line | add suppression reason `already_encoded_by_stronger_control` (research vocabulary) in a later phase; Phase 2 renders a lean variant to measure whether repetition helps or hurts |
| "deep focus" twice; "no cuts" + "one continuous take"; label phrasing twice | camera control and capture treatment overlap; shot line and clip facts overlap | same dedup pass |
| "light sensor noise" read as ambiguous | wording | changed to "faint sensor noise" in the capture treatment |
| ~475 words vs third-party Seedance guidance of 60–100 words | full IR emitted as prose | Phase 2 renders full vs lean vs baseline on the same model and settings |

Verdict for the slice exit test: read-back lists the same beats in the same order and the same
state changes. PASS.
