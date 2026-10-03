# Cold read-back — raw record (run 005, seedance profile, 2026-10-02)

Independent call: a `general-purpose` subagent on Haiku, launched from the implementing session
(Agent tool, model override haiku). It was told to use no tools and to answer only from the text
given, and it made one tool call (its hand-back message). Input: the five instructions below and the
text of `prompt.txt` exactly as emitted (1961 characters plus the trailing newline). Output copied
verbatim (the harness indents the report; the indent is removed here, nothing else changed). The
request id was not captured.

## Instructions given

1. List, in order, every distinct beat you would expect to see, numbered, as what a camera would see.
2. List every state change of an object in the order they happen.
3. Describe the camera: moving or static, framing, lens look.
4. Name anything ambiguous, contradictory, or stated twice in different words.
5. Count the words (approximate).

## Prompt text given (verbatim `prompt.txt`)

```
A 6-second video clip, one continuous take, no cuts.

An empty kitchen at dawn, with nobody in it: a window in the left wall, a pale plaster wall at the far end facing the camera, and a tiled floor. A wooden counter with visible grain runs away from the camera along the left wall under the window, with a white kettle and a ceramic bowl standing on it. First, a thin band of sunlight reaches the near edge of the counter. Then the band of light spreads along the counter away from the camera, passing over the bowl and the kettle, which throw long shadows. Finally, the light leaves the far end of the counter and settles as a bright patch on the plaster far wall, then stays there. Key pose: a bright patch of light on the plaster far wall, nothing else changing. Only the light changes: no person, hand or animal appears and nothing in the room moves. Throughout, the kettle and the bowl stay where they stand and the room stays empty.

Low close framing at the near end of the counter at counter height, standard lens: the counter edge and the first of the light fill the left of frame, the window above it, with the far wall small and dim at the end of the counter. Camera: slow dolly out from the counter edge. Movement: move the camera physically backward in a straight line away from the counter's near end. Speed: slow, smooth, steady retreat across the whole clip, easing to a stop on the last beat. Framing: keep lens direction and camera height consistent while more of the kitchen enters the frame. End: finish in a wider composition that holds the counter and the lit patch on the far wall. Light comes only from the window in the left wall: low, warm, hard-edged dawn light, the rest of the room dim; faint noise in the shadows. Real footage, natural colour with no grade, deep focus.

Avoid: people or hands, the light flickering or jumping, the room brightening everywhere at once, objects moving by themselves, a cut or a zoom, on-screen text.
```

## Raw response

# Video Prompt Analysis

## 1. Distinct Beats (Camera Perspective)

1. Empty dawn kitchen; thin band of sunlight appears at near edge of counter
2. Light spreads along counter surface moving away from camera
3. Light passes over ceramic bowl, casting long shadow
4. Light passes over white kettle, casting long shadow
5. Light reaches far end of counter and leaves it
6. Bright patch of light settles on pale plaster far wall (key pose)
7. Light patch holds steady on wall; camera continues retreating, counter recedes in frame
8. Final wider composition stabilizes with counter and lit patch both visible; camera eases to stop

## 2. Object State Changes (In Order)

1. Kettle: present and stationary on counter (throughout—no change)
2. Bowl: present and stationary on counter (throughout—no change)
3. Light: absent/dim at start
4. Light: thin band appears at counter's near edge
5. Light: band spreads along counter surface away from camera
6. Light: band reaches and passes over bowl (shadow cast)
7. Light: band reaches and passes over kettle (shadow cast)
8. Light: band reaches far end of counter
9. Light: band leaves counter, appears on plaster far wall as bright patch
10. Light: patch settles and remains steady on far wall (no further change)

## 3. Camera

**Movement:** Slow dolly backward in a straight line away from the counter's near end; eases to stop on final beat

**Framing:** Low close framing at counter height; opens from tight view of counter edge and window to wider composition

**Lens:** Standard lens

**Height & Direction:** Consistent height and lens direction maintained throughout; keeps left wall/counter aligned left of frame as shot pulls back

**Speed:** Slow, smooth, steady retreat

**Light:** Natural dawn light from left wall window—low, warm, hard-edged; rest of room dim

**Film Style:** Real footage, natural colour (ungraded), deep focus

## 4. Ambiguities, Contradictions, Stated Twice

- **"settles" and "stays there"** (same action, restated): "settles as a bright patch on the plaster far wall, then stays there"
- **"the window above it" and "under the window"** (same spatial fact, different phrasing): counter runs "under the window" vs. "the window above it"
- **Redundant constraints** (same restriction stated three times): "Only the light changes: no person, hand or animal appears and nothing in the room moves" + "Throughout, the kettle and the bowl stay where they stand and the room stays empty" = repetition of "nothing moves" and "room stays empty"
- **"Low close framing at the near end of the counter at counter height"**: "close," "near end," and "counter height" may be one spatial instruction or three separate specs (minor unclear layering)

## 5. Word Count

Approximately **357 words**
- Opening: 9 words
- Scene description & constraints: 166 words
- Camera, movement, framing, lighting: 156 words
- Avoids list: 26 words

## Comparison

See `readback.md`.
