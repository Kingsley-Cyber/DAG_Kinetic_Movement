# Verdict — run 004 (owner fills in after rendering)

Render each prompt on the same model, route and settings. Note seeds if the model exposes them.

| Prompt | File | Rendered on | Seed | Link or filename |
|---|---|---|---|---|
| compiled (full) | `prompt.txt` | | | |
| baseline (plain ask) | `baseline.txt` | | | |

Scores 1–5 per adherence dimension (compiled / baseline):

| Dimension | Compiled | Baseline | Notes (failure signs seen) |
|---|---|---|---|
| identity (Ines grey sweater, screen-left; Theo navy shirt, screen-right in the doorway; same throughout) | | | |
| action (spin → forearm strike → glass off the table → break on the floor → Theo reacts → shards shown) | | | |
| spatial (sides hold across the strike, the pan and the tilt; shards in front of the table) | | | |
| temporal (order kept; Theo moves only after the break; no break in the air) | | | |
| performance quality (a visible still hold before Theo turns) | | | |
| facial | | | |
| connectivity (forearm meets the glass cleanly; no fusion of arm and glass) | | | |
| camera (opening medium-wide frame, then pan right to Theo, then tilt down to the floor, no cut or zoom) | | | |
| continuity (shards stay on the tile to the last frame; none on the table; clothes unchanged) | | | |

Per-event checklist (physics events in `ir.json`):

| Event | Contact happened | Reaction followed | End pose sane | `must_not_imply` seen? |
|---|---|---|---|---|
| ev_strike (b2): Ines's right forearm on the side of the glass near the base | | the glass tips and slides off the table edge, spinning once | airborne, falling toward the floor | a deliberate swipe or throw · the forearm passes through the glass · the glass leaves the table before the forearm touches it |
| ev_break (b3): the glass on the tile floor | | the glass bursts apart, pieces skid across the tile, a few spin and settle | the pieces lie still where they stopped | the glass bounces without breaking · it breaks in the air before it lands · pieces vanish or return to the table · it lands in Ines's hand |
| Theo's reaction (b4, no event): holds still, turns toward the sound, steps back | — | he moves only after the break | in the doorway, facing the floor | Theo moves before the glass breaks |

Loss ledger (see `loss.jsonl`): `c_latency` (an exact reaction latency in milliseconds) is
`unsupported` on this profile; the prompt carries the delay as a still hold and an order only.
Eleven lines were compressed to short wording for the 2,000-character limit; nothing was dropped.

Overall: compiled beats baseline? yes / no / mixed. One line why:

Then append one line to `director/runs/ledger.jsonl`:
`{"run": "004_glass_strike", "model": "...", "prompt": "compiled|baseline", "seed": null, "scores": {...}, "verdict": "...", "notes": "..."}`
