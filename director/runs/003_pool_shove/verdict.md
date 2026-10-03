# Verdict — run 003 (owner fills in after rendering)

Render each prompt on the same model, route and settings. Note seeds if the model exposes them.

| Prompt | File | Rendered on | Seed | Link or filename |
|---|---|---|---|---|
| compiled (full) | `prompt.txt` | | | |
| baseline (plain ask) | `baseline.txt` | | | |

Scores 1–5 per adherence dimension (compiled / baseline):

| Dimension | Compiled | Baseline | Notes (failure signs seen) |
|---|---|---|---|
| identity (same two men, same clothes throughout; white shirt and jeans on the one who falls) | | | |
| action (nudge → shove → loses balance → water entry → surfaces → laughs) | | | |
| spatial (man in red screen-left, friend and pool screen-right; fall continues the push direction) | | | |
| temporal (order kept; no splash before the entry; not in the water before the shove lands) | | | |
| performance quality (grin at the nudge, gasp on entry, open laugh on surfacing) | | | |
| facial | | | |
| connectivity (palms on chest clean; no fusion of hands and shirt) | | | |
| camera (handheld, side-on, both contacts and the splash in frame) | | | |
| continuity (clothes and hair stay soaked after surfacing; pool keeps moving; pool unchanged in size and colour) | | | |

Per-event checklist (physics events in `ir.json`):

| Event | Contact happened | Reaction followed | End pose sane | `must_not_imply` seen? |
|---|---|---|---|---|
| ev_shove (b2): palms on his friend's chest, much more intense than the first nudge | | upper body rocks back from the hips, arms fly out, heels slide off the edge | weight past the edge, starting to fall | the shove lands before the foot is planted · the friend jumps or steps in by himself · the man in red falls in too · hands fused with the shirt |
| ev_water (b4): back and shoulders on the pool surface | | water bursts up and outward in a crown, spray over the stone edge, body goes fully under | water falls back, bubbles rise where he went under | a splash before his back touches the water · bouncing off or skating across the surface · staying dry · the splash hanging in the air |
| nudge anchor (b1, no event; pathway p_nudge): light two-handed tap | | rocks back on his heels, steps forward again | standing at the edge | — |

Prompt content dropped for budget (see `emit_report.json`): `c_laugh` (acting direction), `c_pace`,
`c_negatives`. Judge performance quality with that in mind. Spacing phrases "arriving fast and
settling" and "easing in and out" were read as unclear by the cold read-back.

Overall: compiled beats baseline? yes / no / mixed. One line why:

Then append one line to `director/runs/ledger.jsonl`:
`{"run": "003_pool_shove", "model": "...", "prompt": "compiled|baseline", "seed": null, "scores": {...}, "verdict": "...", "notes": "..."}`
