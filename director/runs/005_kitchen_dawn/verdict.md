# Verdict — run 005 (owner fills in after rendering)

Render each prompt on the same model, route and settings. Note seeds if the model exposes them.

| Prompt | File | Rendered on | Seed | Link or filename |
|---|---|---|---|---|
| compiled (full) | `prompt.txt` | | | |
| baseline (plain ask) | `baseline.txt` | | | |

Scores 1–5 per adherence dimension (compiled / baseline):

| Dimension | Compiled | Baseline | Notes (failure signs seen) |
|---|---|---|---|
| identity (same kitchen throughout: window left, counter along the left wall, kettle and bowl, plaster far wall) | | | |
| action (the light: reaches the counter edge → crosses the counter → settles on the far wall) | | | |
| spatial (light travels away from the camera along the counter; far wall comes into view at the end) | | | |
| temporal (order kept; the light moves one way and rests; no flicker or jump) | | | |
| performance quality (n/a: no performer; nobody appears) | | | |
| facial (n/a) | | | |
| connectivity (n/a: no hands, no contact) | | | |
| camera (one slow backward move from the counter edge, ending wider; no zoom, no cut) | | | |
| continuity (kettle and bowl unmoved; room empty to the last frame) | | | |

Per-event checklist: there are no physics events (no contact). Check instead the three states of
the light (`b1`, `b2`, `b3`):

| State | Seen | In order | End state held |
|---|---|---|---|
| b1: a thin band of sunlight reaches the near edge of the counter | | | |
| b2: the light spreads along the counter over the bowl and the kettle, long shadows | | | |
| b3: the light settles as a bright patch on the far wall and stays | | | |

`must_not_imply` lines: none written (no physics events). Failure signs from the treatment
`light_color.dawn_window_light`: flat even light with no visible edge; flicker or reversal; the
whole room brightening at once; clipped highlights or a heavy grade.

Loss ledger (see `loss.jsonl`): two lines compressed to short wording for the 2,000-character
limit (`b1`, `c_light`); nothing dropped.

Overall: compiled beats baseline? yes / no / mixed. One line why:

Then append one line to `director/runs/ledger.jsonl`:
`{"run": "005_kitchen_dawn", "model": "...", "prompt": "compiled|baseline", "seed": null, "scores": {...}, "verdict": "...", "notes": "..."}`
