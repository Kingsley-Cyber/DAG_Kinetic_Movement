# Verdict — run 006, experiments E2 and E3 (owner fills in after rendering)

Same model, same route, same settings for every arm (4 s, 16:9). Use the same three seeds for
every arm, so arms differ only in the prompt. Write the seed numbers here: seed 1 = ___ ·
seed 2 = ___ · seed 3 = ___. `E2_relative` and `E3_visible` are the same prompt: render it once
per seed and score it for both experiments (12 renders in total).

Yes/no questions per render: **contact** (Mara's left forearm meets Veyr's right forearm) ·
**reaction** (Veyr's arm goes off his line and he gives a full step, only after the contact) ·
**end pose** (they hold forearm against forearm, Mara between Veyr and the core). Adherence
scores 1–5.

| Arm | Prompt file | Seed | Contact? | Reaction followed? | End pose sane? | Action 1–5 | Physical plausibility 1–5 | Performance quality 1–5 | Camera 1–5 | Notes (failure signs seen) |
|---|---|---|---|---|---|---|---|---|---|---|
| E2_relative = E3_visible | `arms/E2_relative/prompt.txt` | seed 1 | | | | | | | | |
| E2_relative = E3_visible | `arms/E2_relative/prompt.txt` | seed 2 | | | | | | | | |
| E2_relative = E3_visible | `arms/E2_relative/prompt.txt` | seed 3 | | | | | | | | |
| E2_absolute | `arms/E2_absolute/prompt.txt` | seed 1 | | | | | | | | |
| E2_absolute | `arms/E2_absolute/prompt.txt` | seed 2 | | | | | | | | |
| E2_absolute | `arms/E2_absolute/prompt.txt` | seed 3 | | | | | | | | |
| E3_term | `arms/E3_term/prompt.txt` | seed 1 | | | | | | | | |
| E3_term | `arms/E3_term/prompt.txt` | seed 2 | | | | | | | | |
| E3_term | `arms/E3_term/prompt.txt` | seed 3 | | | | | | | | |
| E3_numeric | `arms/E3_numeric/prompt.txt` | seed 1 | | | | | | | | |
| E3_numeric | `arms/E3_numeric/prompt.txt` | seed 2 | | | | | | | | |
| E3_numeric | `arms/E3_numeric/prompt.txt` | seed 3 | | | | | | | | |

Things to watch (from `plan/EXPERIMENTS.md`): absolute arm → stiff or exaggerated motion;
relative arm → the anchor drifts across the clip (Veyr's walk speeds up or Mara's run reads no
faster than his walk). Term and numeric arms → the pole words or the numbers appear as on-screen
text, or the block is delivered by the arm alone. From the cold read-back (`readback.md`):
"much heavier than Veyr's footfalls" may be read as body mass, not impact force.

`must_not_imply` for the one event (`ev_intercept`): a punch to the face or body · Veyr falling or
being thrown · one forearm passing through the other · Veyr leaving his line before the forearms
meet · the two bouncing apart to neutral stances.

## Decision rules (copied from `plan/EXPERIMENTS.md`)

**E2 — absolute vs relative magnitudes.** Relative better on at least two of three paired seeds
for physical plausibility with equal intent → the wording lint becomes a hard failure for that
model. Otherwise the warning stands. Either way the IR-level rule stays.

**E3 — wording rungs.** The best rung becomes that model's default in its profile; the others
stay available as experiments.

A result is per model and per route: `supported`, `contradicted` or `inconclusive`. Three seeds
are a convention for a decision, not statistics.

E2 result: relative better / absolute better / no difference. One line why:

E3 result: best rung = visible / term / numeric. One line why:

Then append one line per render to `director/runs/ledger.jsonl`:
`{"run": "006_interception_arms", "experiment": "E2|E3", "arm": "...", "model": "...", "seed": 0, "contact": true, "reaction": true, "end_pose": true, "scores": {...}, "notes": "..."}`
