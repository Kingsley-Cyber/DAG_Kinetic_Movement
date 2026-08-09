---
id: cpcs.lab.variant_lineage
kind: mechanism
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U11, SRC-010-U16]
primary_route: cpcs/evaluation/benchmark_runs/
secondary_routes:
  - cpcs/knowledge/09_evaluation/
interfaces:
  - cpcs.lab.architecture
  - cpcs.lab.ab_test_protocol
  - cpcs.lab.pattern_registry
  - cpcs.runtime.kinematic_validation
---

# Variant Lineage (v001–v006 + naruto)

> **Source:** SRC-010 `lab/variants/` + `lab/runs/results.csv`. The only
> populated render history in the CPCS corpus: 6 tracked variants plus one
> worked-example variant, each with model, scores, verdict, and lineage edges.

## Lineage map

```text
v001 (champion, prose+YAML-in-XML, 5/5/4/5)
 ├─ format swap        → v002 (YAML+JSON, 5/5/4/5)   — p006 format-neutral proof
 ├─ scored upgrade     → v003 (scored FACS/Laban, "too movie like") — FAIL, pivot
 └─ skin lever         → v004 (smooth skin, 2/1/4/5)  — ANTI-PATTERN
v004 paradigm switch   → v005 (JSON canon truth alone, 5/5/5) — new paradigm (p008)
v005 precision fix     → v006 (hybrid YAML+JSON, reach-fixed, 0 failures)
v006 domain transfer   → naruto_sasuke_rooftop_clash (10 s shonen anime worked example)
```

## Variant records

| Variant | Paradigm / format | Model | Scores | Verdict |
|---|---|---|---|---|
| v001 | descriptive_prose, YAML-in-XML | Veo-3.1 | 5/5/4/5 | **champion** — iPhone-12 raw UGC, user-validated |
| v002 | same content, YAML+JSON | Veo-3.1 | 5/5/4/5 | format-neutrality proof (p006) |
| v003 | scored FACS/Laban cinematic | Veo-3.1 | — | FAIL — "too movie like" → raw pivot |
| v004 | smooth skin (one lever off v001) | Veo-3.1 | 2/1/4/5 | **ANTI-PATTERN** — plastic-skin; never "smooth" |
| v005 | numeric_canonical_truth, JSON alone | Veo-3.1 | 5/5/5 | new paradigm — motion driven by canon truth, no prose (p008) |
| v006 | hybrid YAML+JSON, reach-verified | Veo-3.1 | pass | 0 failures on validate_kinematics; 10 additions over v005 |
| naruto | cpcs-authoring/1.1, anime_cel overrides | LTX-2.3 | worked example | 10 s / 24 fps / 240 frames, bpm 160, power curve 0.30→1.00 |

## The v005 → v006 lesson (precision is found by tooling, not by eye)

v005 authored combat geometry that **contradicted itself**: fighters were
placed 1.60 m apart at first contact (c01) while the combined reach of the
two actors' strikes was only 1.42 m — a **0.18 m deficit**. The canon could
not be executed. The defect was found by `validate_kinematics.py` (contact
geometry check family), not by watching the render.

Consequence: a numeric canonical truth document needs **self-consistency
verification before render** (see `cpcs.runtime.kinematic_validation`). v006
is v005 plus reach-verified geometry, a 0.25 s sample rate, joint rotations,
velocity vectors, easing, contact normals + impulse + peak_force, foot-contact
and CoM tracks, secondary motion, and a Veo optics block — and it passed all
8 check families with 0 failures.

## Anti-pattern v004

Changing exactly one lever (skin.strategy: real_microtexture_forbid_smooth →
smooth) collapsed skin realism from 5 to 1 (2/1/4/5). This is the cleanest
attribution in the lab (feeds p001/e002) and the lab's **original** failure
mode: the paper's 15 named failures do not include plastic-skin.

## Lineage rules

- Every variant carries its **lever_tags** (one value per relevant lever) so
  any two variants are diffable lever-by-lever.
- The lineage records **decisions**, not just results: v003's "too movie
  like" verdict caused the raw pivot; v004's collapse caused the paradigm
  switch to numeric truth.
- Historical rows are never edited (append-only ledger).

## Boundary

Scores are single-observer, single-session, qualitative. The lineage is ground
truth for *what happened*, not for *what generalizes* — generalization claims
live in the pattern registry with honest confidence.
