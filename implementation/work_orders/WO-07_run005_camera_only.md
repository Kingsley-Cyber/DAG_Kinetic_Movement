# WO-07 — Run 005: camera-only (T12)

## The ask (verbatim)

> A slow reveal of an empty kitchen at dawn as light moves across the counter, 6 seconds.

Target model: `seedance`.

## Decisions already made

- No performer: performance, interaction and action are inactive; no hands ledger entries; no
  pathways (the schema allows empty arrays).
- The schema needs at least one beat: use the world's change as beats (light reaches the counter
  edge; light crosses the counter; light settles on the far wall), owned by time, described as
  what the camera sees.
- Active: intent, entity (the kitchen and its objects as entities with locks), world (light as an
  environment state that changes), time, camera (mandatory), light_color, style, synthesis.
- One camera move from the catalog chosen by `function` ("reveal"): record the alternatives
  considered in `decisions.jsonl`.
- "slow" in the ask is a magnitude word: express pace through the camera's `speed` field and an
  anchor if two paces are compared; if the lint still warns on the ask text inside `ask`, that is
  expected (the ask is the user's words and is not scanned).
- Write `light_color` treatments only if needed: `director/treatments/light_color/dawn_window_light.md`
  from `Additional/CAPTURE_SURFACE_REALISM.md` §2 and §5 rule 1 and rule 5.

## Steps and acceptance

Same as WO-04 steps 1–7, folder `director/runs/005_kitchen_dawn/`. Additional acceptance: no
performer language in the prompt; camera grammar states where, movement, lens and end; read-back
lists the light's three states in order.

## Stop if

`check` requires hands or pathways for a run with none: that is a tool defect; fix it with a test
(`test_run_without_performers_is_valid`) and continue.
