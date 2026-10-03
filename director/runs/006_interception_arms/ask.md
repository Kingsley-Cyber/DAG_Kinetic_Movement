# Run 006 — interception arms (experiments E2 and E3)

## Ask

> On a rain-wet steel platform high inside a reactor shaft, Veyr walks toward the reactor core.
> Mara cuts across the platform and blocks him, forearm against forearm, turning him off his line.
> 4 seconds, 2D action anime.

The owner did not type this ask. It is the interception from the owner's fight IR
(`Additional/TERMINAL_DESCENT_FIGHT_IR_v1.json`: beats `b01_route_interception` and the onset of
`b02`, contact `c01_forearm_redirect`, action `a01_mara_intercept_and_ride`) written in plain
words by the implementing session, as `implementation/work_orders/WO-08_experiment_arms.md` asks.

Target model: seedance (route unconfirmed). Clip length 4 s: the shortest duration the profile
lists (`durations_s: "4-15"`), the rule WO-08 sets.

## What this run is for

One IR, five emissions. The arms differ only in the wording under test; entities, beats, camera,
style and negatives are identical. No arm was compressed or had a line dropped for budget.

| Arm folder | Command flags | Tests |
|---|---|---|
| `arms/E2_relative` | `--magnitudes relative` | E2: magnitudes stated against an anchor in the clip |
| `arms/E2_absolute` | `--magnitudes absolute` | E2: bare magnitude words, no anchor sentences |
| `arms/E3_visible` | `--rung visible` | E3: movement quality as visible behaviour (same prompt as `E2_relative`) |
| `arms/E3_term` | `--rung term` | E3: movement quality as Laban Effort pole names |
| `arms/E3_numeric` | `--rung numeric` | E3: movement quality as a numeric block |

`E2_relative/prompt.txt` and `E3_visible/prompt.txt` are byte-identical: render it once per seed
and score it for both experiments. Four distinct prompts × three seeds = 12 renders.

## Intent brief

From the fight IR: two fighters (Mara, Veyr); Veyr's objective is the reactor core; Mara cuts
across his route; first contact is Mara's left forearm on Veyr's right forearm; the medium is
contemporary 2D action anime; movement profile strong, sudden, direct, bound during contact.
Authored here because the fight IR is silent: both appearances, the screen sides, the camera
move, the force baseline (Veyr's footfalls).

Left out on purpose (one causal event per test): Veyr's stored-force rail charge and its release,
the glass partition, Mara's shoulder injury, the camera impulse on contact, the storm audio bed.

## Pass plan summary

Active: intent, entity, interaction, physics, staging, time, performance, camera, style, synthesis.
Inactive with reason: world, action (covered by interaction and physics), continuity, attention,
light_color, audio.
