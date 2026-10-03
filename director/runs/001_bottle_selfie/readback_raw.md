# Cold read-back — raw record (run 001, seedance profile, 2026-10-02)

Independent call: a `general-purpose` subagent on Haiku, launched from the planning session with no
file or tool access. Input: only the five instructions below and the text of `prompt.txt` as it
was at that time (before the "faint sensor noise" wording fix; otherwise identical). Output
copied verbatim.

## Instructions given

1. List, in order, every distinct beat you would expect to see, numbered, as what a camera would see.
2. List every state change of an object in the order they happen.
3. Describe the camera: moving or static, framing, lens look.
4. Name anything ambiguous, contradictory, or stated twice in different words.
5. Count the words (approximate).

## Raw response

### 1. Beats (in order, what camera sees)

1. Woman seated at table leans forward, glances at lens; sealed water bottle sits in foreground
2. Woman's hands move down toward bottle
3. Left hand grips bottle body; right hand fingers pinch the cap
4. Cap rotates counter-clockwise one full turn
5. Cap separates from bottle with audible click
6. Water inside bottle ripples visibly
7. Cap lifts clear in right hand; bottle rises in left hand
8. Woman's eyes shift to the bottle as it rises
9. Bottle rim reaches woman's mouth
10. Woman swallows (once, then again)
11. Water level visibly drops inside bottle
12. Woman lowers bottle from face
13. Woman exhales
14. Woman glances back to camera lens
15. Woman holds still, facing lens

### 2. State Changes (in order)

- Bottle: sealed → cap turning → unseal/opened
- Cap: threaded on bottle → loose/lifted → held separately in fingers
- Water level: full → drops (during swallowing)
- Water surface: still → ripples (when cap releases)
- Woman's gaze: lens → downward → lens
- Woman's hands: at rest → reaching → gripping/pinching → raised holding bottle → at lips → lowered

### 3. Camera

Static, propped iPhone front camera. Medium close-up framing, slightly low angle. Wide/deep focus,
no bokeh. 30fps, flat HDR tone, natural sensor noise, ungraded. Real skin texture, visible pores,
not smoothed.

### 4. Ambiguities & Redundancies

- Repetition: main action sequence described twice, once in opening narrative, then restated in
  "In order" section
- Redundancy: "deep focus" stated twice in camera section
- Redundancy: "no cuts" + "one continuous take" (same meaning)
- Redundancy: "vertical phone selfie clip" setup + "propped phone, static" (same info)
- "label facing the camera" vs earlier "label to camera" (same thing, phrased twice)
- Vague timing: "reaches down" duration not specified
- Unclear phrasing: "light sensor noise" (noise level is light, or adds a light quality?)

### 5. Word Count

Approximately 475 words.

## Comparison

See `readback.md`. Beat order MATCH (15 micro-beats collapse onto b1–b7 in order); state changes
MATCH; camera MATCH. The raw call trace (request id) was not captured; future read-backs record
the prompt text given and the full response in this file at the time of the call.
