---
id: cpcs.lab.ab_test_protocol
kind: method
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U10, SRC-010-U12, SRC-010-U02]
primary_route: cpcs/evaluation/benchmark_runs/
secondary_routes:
  - cpcs/knowledge/09_evaluation/
  - cpcs/research/sources/
interfaces:
  - cpcs.lab.architecture
  - cpcs.lab.pattern_registry
  - cpcs.lab.variant_lineage
  - cpcs.evaluation.cpcs_evaluation_framework
---

# Lab A/B Test Protocol

> **Source:** SRC-010 `lab/experiments/` (e001–e003),
> `lab/schema/records.schema.json`, `lab/runs/results.csv`. The discipline that
> makes a delta attributable: change **one lever**, keep everything else fixed.

## One-lever discipline

An experiment changes **exactly one lever** (see the 13-lever vocabulary in
`cpcs.lab.architecture`) between control and test variants, on the **same
model, same seed**. Only then can a score delta be attributed to that lever.
Anything else is a bundled change and must be labeled `hypothesis` — even if
the resulting clip is good.

## Experiment record (schema `$defs.experiment`)

```yaml
experiment:
  id: e002                # e001..e003 so far
  hypothesis: "real_microtexture_forbid_smooth beats smooth for skin realism"
  lever: skin.strategy
  control_variant: v004   # smooth
  test_variant: v001      # real_microtexture_forbid_smooth
  status: isolated_confirmed   # hypothesis | qualitative_confirmed | isolated_confirmed | refuted
  evidence: [r001, r004]
```

Status ladder — a pattern may be promoted only one rung at a time:

```text
hypothesis  →  qualitative_confirmed (bundled/seen, not isolated)
            →  isolated_confirmed (one-lever A/B, same seed)
            →  refuted (later isolated run contradicts)
```

## Run ledger (results.csv)

Append-only: one row per generation. Never edit or average away historical
rows — lineage integrity depends on the ledger.

| Field | Meaning |
|---|---|
| variant_id | which tracked package was rendered |
| model | Veo-3.1 / LTX-2.3 / … |
| scores | 4 dims, 1–5: realism · skin · motion · adherence |
| verdict | pass / fail / note |
| date, provider_session | provenance for the render |

Current ledger: r001–r006 covering v001–v006 (see `cpcs.lab.variant_lineage`).

## Score dimensions

`realism` (looks real) · `skin` (skin microtexture honesty) · `motion`
(kinematic plausibility) · `adherence` (followed the prompt). Qualitative
1–5, single observer. These 4 manual dims are the lab's empirical
instantiation of the paper's 6 metric families — they measure the same
objectives by eye.

## Procedure (agent)

1. **Pick a hypothesis** from the pattern registry's `low`-confidence items or
   an unexplored frontier channel.
2. **Name the lever** and its two values (control vs test).
3. **Build two variants** differing in exactly that lever; same seed template.
4. **Render both** on the same model, same session conditions.
5. **Score both** on the 4 dims; record rows in the ledger.
6. **Update the experiment record**: status per the ladder; append evidence.
7. **Update the pattern**: promote/demote per evidence, never per preference.

## Promotion / demotion rules

- Promote a pattern only when an **isolated** A/B confirms it (e002 is the
  sole `isolated_confirmed` in the lab).
- Demote immediately when a later isolated run contradicts — the honesty rule
  applies to demotions too: evidence, not conviction.
- Bundled evidence keeps confidence `low` even inside a champion variant.

## Boundary

Single-observer, single-session, non-seed-controlled statistics. The protocol
is designed to be run repeatedly until the frontier channels are closed; the
open experiments are tracked in `cpcs/research/gaps/src010_open_research_questions.md`.
