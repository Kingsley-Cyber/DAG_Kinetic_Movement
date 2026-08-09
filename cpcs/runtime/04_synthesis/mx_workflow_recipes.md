---
id: cpcs.runtime.mx_workflow_recipes
kind: method
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008 §docs/AGENT_WORKFLOW_RECIPES.md]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/verification/
interfaces:
  - cpcs.runtime.agent_prompts
  - cpcs.runtime.mx_profiles
  - cpcs.runtime.canonical_schema
---

# CPCS-MX Agent Workflow Recipes

> Distilled from the frozen package's 10 operational recipes (405 lines). These
> are retrieval and compilation patterns — operational guidance, not a substitute
> for the canonical schema or cited external research.

## Shared agent topology

```text
semantic authoring agent
        ↓ proposed authoring YAML
resolver/compiler
        ↓ validated canonical JSON + capability report
verification agent
        ↓ evidence JSONL + compliance report
```

The authoring agent proposes. The compiler resolves and validates. The verifier
measures.

## Recipe summary

| # | Recipe | Key retrieval bundle | Compilation warning |
| --- | --- | --- | --- |
| 1 | Natural human movement | locomotion, biomechanics, root motion, contacts, breath, mannerism | Do not generate "human imperfection" by adding independent random noise to every joint |
| 2 | Realistic UGC recreation | UGC, mannerism, gaze, breath, camera-relative, source transfer | Re-extract and compare beat order, lens-address timing, gesture apex, product visibility — "looks authentic" is not sufficient |
| 3 | Professionally staged screen action | staged-combat, contact, phase, biomechanics, camera, safety | Default to `staged_near_contact`; do not convert visual impact cues into instructions for causing injury |
| 4 | Anime/sakuga transformation | anime/sakuga, superhuman, secondary-motion, style-transform schema | Do not use one `style_intensity` value as the entire algorithm |
| 5 | Virtual-superhuman movement | superhuman transform, virtual physics, invariants | Values are project controls, not biological safety limits |
| 6 | Diagnose foot skating | root motion, contacts, hard constraints, IK/retarget, verification metrics | Correct the earliest causal layer rather than hiding the error with camera motion |
| 7 | Diagnose unnatural "robotic" movement | phase overlap, proximal-to-distal, gaze, breath, support, mannerism, secondary motion, jerk | A perfectly smooth pose sequence may still lack weight transfer, anticipation, or recovery |
| 8 | Text to CPCS-MX | semantic parse → authoring YAML → compile → choose carrier → verify | Keep unsupplied timing or geometry as unresolved, not invented constants |
| 9 | Retrieval query templates | concept/schema/implementation/evidence questions | Avoid retrieving many superficially similar examples without the governing definition |
| 10 | Context assembly policy | research chunk → schema → example → prompt → sources → safety | Examples demonstrate syntax; they do not define universal human constants |

## UGC transfer policy (Recipe 2)

```yaml
retain:
  - beat_order
  - gesture_function
  - major_timing
  - gaze_to_lens_duty_cycle
  - camera_grammar
parameterize:
  - gesture_amplitude
  - speaking_rate
  - pause_duration
  - handheld_motion_scale
replace:
  - identity
  - voice
  - wardrobe
  - setting
  - product_or_brand_when_required
```

## Staged action causal score (Recipe 3)

```text
preparation
  → support change
  → initiation
  → proximal-to-distal propagation
  → staged near-contact or declared virtual contact
  → audiovisual impact accent
  → reaction delay
  → recoil
  → balance recovery
  → reset
```

Store actor trajectories, support states, target volumes, minimum distance,
occlusion, camera-side cheating, sound timing, VFX timing, and recovery
independently.

## Execution carrier selection (Recipe 8, Step 4)

| Need | Preferred carrier |
| --- | --- |
| semantic approximation | text prompt |
| key poses | first/last or sparse reference frames |
| exact screen-space body motion | pose-control video |
| editable contact and balance | rigged animation with IK |
| precise camera | camera trajectory or previsualization render |
| exact masks/occlusion | mask or segmentation video |
| stylized timing and effects | compositor/edit event package |

## Context assembly order (Recipe 10)

1. direct research chunk
2. relevant schema definition
3. one closest worked example
4. applicable agent prompt
5. source records for external claims
6. safety/rights documentation when identity, combat, or reference transfer is involved

**Avoid retrieving many superficially similar examples without the governing
definition.** Examples demonstrate syntax; they do not define universal human
constants.
