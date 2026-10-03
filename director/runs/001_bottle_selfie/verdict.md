# Verdict — run 001 (owner fills in after rendering)

Render each prompt on the same model, route and settings. Note seeds if the model exposes them.

| Prompt | File | Rendered on | Seed | Link or filename |
|---|---|---|---|---|
| compiled (full) | `prompt.txt` | | | |
| baseline (plain ask) | `baseline.txt` | | | |

Scores 1–5 per adherence dimension (compiled / baseline):

| Dimension | Compiled | Baseline | Notes (failure signs seen) |
|---|---|---|---|
| identity (same woman, same bottle throughout) | | | |
| action (grip → twist → cap free → raise → drink → lower) | | | |
| spatial (hands, bottle, cap where stated) | | | |
| temporal (order kept; no jump to "open") | | | |
| performance quality (casual, unhurried, alive face) | | | |
| facial | | | |
| connectivity (hand–bottle contact clean; no fusion) | | | |
| camera (static propped selfie, deep focus) | | | |
| continuity (cap stays visible; label and size constant; water drops only on drink) | | | |

Overall: compiled beats baseline? yes / no / mixed. One line why:

Then append one line to `director/runs/ledger.jsonl`:
`{"run": "001_bottle_selfie", "model": "...", "prompt": "compiled|baseline", "seed": null, "scores": {...}, "verdict": "...", "notes": "..."}`
