# Owner actions — the only things the model cannot do for you

Everything else is in the queue. These are short and in plain steps.

## 1. Tell the model which Seedance route you use (once)

Answer in one line in chat, or write it here:

- Route: (for example: Dreamina app, Volcengine API, Runway, fal)
- Model version:
- Prompt box limit if you know it:

Until you answer, the profile assumes a 2,000-character limit from third-party docs.

## 2. Render at GATE A (one sitting)

**Part 1 — the kill check (10 renders). Do this first.** For each of these five folders, render
`prompt.txt` and `baseline.txt` on the same model with the same settings, then fill in
`verdict.md` in that folder (scores 1 to 5, one line of notes; for contact moments also yes or no:
did the contact happen, did the reaction follow, is the end pose sane).

| Folder | Clip | Settings |
|---|---|---|
| `director/runs/001_bottle_selfie/` | woman opens a water bottle and drinks, selfie | 8 s, 9:16 |
| `director/runs/002_earbuds_unbox/` | man unboxes earbuds and puts one in | 8 s, 9:16 |
| `director/runs/003_pool_shove/` | he gets shoved into the pool | 8 s, 16:9 |
| `director/runs/004_glass_strike/` | forearm knocks a glass off a table, it breaks | 8 s, 16:9 |
| `director/runs/005_kitchen_dawn/` | empty kitchen at dawn, light crosses the counter | 6 s, 16:9 |

The exact settings for each run are in its `emit_report.json` under `settings`.

**Part 2 — the wording experiments (12 renders). Second sitting is fine.** Folder
`director/runs/006_interception_arms/arms/`. Four prompts, each rendered with the same three
seeds (4 s, 16:9):

1. `E2_relative/prompt.txt` (this is also `E3_visible`: one render counts for both)
2. `E2_absolute/prompt.txt`
3. `E3_term/prompt.txt`
4. `E3_numeric/prompt.txt`

Fill in the table in `director/runs/006_interception_arms/verdict.md`.

Then tell the model "verdicts are in". It reads them, runs the kill check and reports.

## 3. Say "push" when you want commits on GitHub

The model commits locally and never pushes on its own.

## Blocked questions from the model

(The implementing model writes questions here when it would otherwise have to guess.)
