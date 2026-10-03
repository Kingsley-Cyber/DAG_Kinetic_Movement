# Verdict — run 002 (owner fills in after rendering)

Render each prompt on the same model, route and settings. Note seeds if the model exposes them.

| Prompt | File | Rendered on | Seed | Link or filename |
|---|---|---|---|---|
| compiled (full) | `prompt.txt` | | | |
| baseline (plain ask) | `baseline.txt` | | | |

Scores 1–5 per adherence dimension (compiled / baseline):

| Dimension | Compiled | Baseline | Notes (failure signs seen) |
|---|---|---|---|
| identity (same man, same box, case and earbuds throughout) | | | |
| action (lid off → case out → thumb opens lid → earbud out → earbud in ear) | | | |
| spatial (hands, box, case, earbud where stated; right hand to right ear) | | | |
| temporal (order kept; no jump to "open" or "in the ear") | | | |
| performance quality (casual, unhurried, alive face) | | | |
| facial | | | |
| connectivity (hand–case and hand–earbud contact clean; no fusion) | | | |
| camera (friend-held handheld, face and both hands readable, no close-up on the ear) | | | |
| continuity (box lid stays on the desk; case lid stays up; only one earbud leaves the case) | | | |

Per-event checklist (physics events in `ir.json`):

| Event | Contact happened | Reaction followed | End pose sane | `must_not_imply` seen? |
|---|---|---|---|---|
| ev_open (b5): left thumb on the case lid | | lid swings up, two earbuds show, lid stops upright and stays open | case open in the left palm | the lid open before the thumb touches it · the lid detaching from the case · the case turning or moving in the palm |
| ev_ear (b7): right fingers press the earbud into his right ear (occluded contact) | | earbud seats with its stem down, fingers release, earbud stays | earbud in the ear, hand lowered, case open in the left palm | the earbud fused with skin or the ear · an earbud in the hand and in the ear at once · both earbuds leaving the case · a close-up on the ear |

Prompt content dropped for budget (see `emit_report.json`): `c_register` (acting register), `c_pace`,
`c_negatives`. Judge performance quality with that in mind.

Overall: compiled beats baseline? yes / no / mixed. One line why:

Then append one line to `director/runs/ledger.jsonl`:
`{"run": "002_earbuds_unbox", "model": "...", "prompt": "compiled|baseline", "seed": null, "scores": {...}, "verdict": "...", "notes": "..."}`
