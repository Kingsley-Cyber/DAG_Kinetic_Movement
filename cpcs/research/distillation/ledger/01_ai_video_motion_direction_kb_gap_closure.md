---
distillation_id: DIST-001
source_id: SRC-001
status: complete
coverage: full
---

# Distillation Ledger — SRC-001

`01_AI_VIDEO_MOTION_DIRECTION_KB_GAP_CLOSURE_RESEARCH.md` → CPCS knowledge tree.
Distilled 2026-08-08. All objects below were written into their primary routes;
this ledger is the audit trail.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-001_...md`. CPCS-internal research
closure (v1.1), authored, citing 16 external primary sources. Self-declared
limitation: the frozen KB package it closes gaps against was not supplied, so
package-level coverage claims are **not verifiable from the supplied files**.

## PASS 1 — Structural map

29 sections: (1) executive gap closure, (2) evidence ledger, (3) canonical
semantic representation, (4) rotation, (5) bilateral/FACS, (6) phase grammar,
(7) kinematics/measurement, (8) dynamics fail-closed, (9) interaction lifecycle,
(10) continuity/causality closure, (10-duplicate-numbering) camera grammar,
(11) style grammar, (12) complexity, (13) representation equivalence,
(14) compiler semantics, (15) provider implications, (16) carrier experiment,
(17) verification contract, (18) implementation placement, (19) object family,
(20) critical design corrections, (21) schema sketch, (22) JSONL audit record,
(23) research-to-runtime example, (24) priority order, (25) closure matrix,
(26) agent build packet, (27) architectural conclusion, (28) revision note,
(29) cited sources. Note: the source numbers two sections "10" (continuity and
camera) — a source defect, no content lost.

## PASS 2 — Existing-knowledge search

Repository authority was empty at distillation time (skeleton only, 0 files).
No REUSE/EXTEND/MERGE candidates existed; every accepted object is therefore
the first canonical owner of its meaning. Dedup obligation transfers forward:
all later sources MUST check against the objects registered by this ledger.

## PASS 3–7 — Extraction summary

Written objects (primary route → file):

| # | Object | kind | route |
| --- | --- | --- | --- |
| 1 | epistemic firewall doctrine | doctrine | `knowledge/00_foundations/invariants/` |
| 2 | acquisition × epistemic-state evidence model | principle | `knowledge/00_foundations/uncertainty/` |
| 3 | kinematics/effort/force field separation | principle | `knowledge/00_foundations/numerical_representation/` |
| 4 | rotation representation contract | principle | `knowledge/00_foundations/numerical_representation/` |
| 5 | bilateral side-indexed semantics | principle | `knowledge/00_foundations/numerical_representation/` |
| 6 | monocular pose ambiguity | principle | `observation/pose/` |
| 7 | Laban layering (not canonical kinematics) | doctrine | `knowledge/06_body_motion/laban_bess/` |
| 8 | evidence-backed vs engineering phases | principle | `knowledge/06_body_motion/phase_grammar/` |
| 9 | kinematics measurement contract | method | `knowledge/06_body_motion/kinematics/` |
| 10 | dynamics fail-closed doctrine | doctrine | `knowledge/09_force_physics/` |
| 11 | jerk noise sensitivity | principle | `knowledge/09_force_physics/` |
| 12 | interaction lifecycle + occluded contact | mechanism | `knowledge/07_interaction_contact/actor_object/` |
| 13 | continuity semantics (visibility ≠ existence) | principle | `knowledge/18_sequence_continuity/occluded_hidden_state/` |
| 14 | causal event semantics | principle | `knowledge/00_foundations/causality/` |
| 15 | camera three-layer semantics + calibration | principle | `knowledge/12_camera_image_formation/` |
| 16 | style constraint model | principle | `knowledge/16_style_visual_language/invariants/` |
| 17 | complexity feature vector | principle | `knowledge/19_generation_complexity/` |
| 18 | carrier role semantics | doctrine | `runtime/07_compiler/carrier_planner/` |
| 19 | capability classes + loss records | doctrine | `runtime/07_compiler/semantic_mapping/` |
| 20 | universal object family (kernel) | PROJECT_DERIVED proposal | `schemas/world_model/` |
| 21 | carrier-effect experiment design | experiment | `research/sources/experiments/` |
| 22 | 14 open research questions | gap | `research/gaps/` |
| 23 | verification contract (8 lists) | method | `verification/semantic/` |
| 24 | Runway / Veo / Kling camera findings | provider finding | `providers/runway|veo|kling/` |
| 25 | P0/P1/P2 implementation priority | policy | `00_governance/policies/` |

## PASS 4 — Numerical findings (all dispositioned)

| Finding | Class | Value | Disposition |
| --- | --- | --- | --- |
| Confidence examples (0.84, 0.91, 0.89, 0.74, 0.63, 0.61, 0.54, 0.28, 0.94) | RANGE (illustrative) | [0,1] | illustrative only — not calibrated scales; recorded in carrier/verification examples |
| FACS intensity scale | STANDARDIZED_CODING_SCALE | A–E (U05) | card 5.3 of source → retained as `scale: facs_A_E`; detector-continuous [0,1] kept separate, no silent mapping |
| Sampling rate example | PHYSICAL_MEASUREMENT | 30 Hz | example in measurement contract |
| FOV example | EQUATION-derived | 39.6° horizontal @ 50 mm | derived, status `derived` — illustrates focal_length → FOV derivation |
| Quaternion example | EQUATION | [0.9239, 0, 0.3827, 0] ≈ 45° about y | illustrates convention declaration requirement (U04) |
| Carrier experiment sizes | PROJECT_DERIVED_SCALE | ≥100 motion / 50 interaction / 50 camera / 25 style / 25 mixed intents; 7 renderings; 13 metrics | experiment design object |
| complexity_score | PROJECT_DERIVED_SCALE | uncalibrated | explicitly `score: null` until calibration — no numeric invention |
| 6D rotation continuity result (U04) | EXPERIMENTAL_RESULT | qualitative | ≤4D Euclidean rotation reps are discontinuous for NN learning; 6D continuous — adapter-only |

No precision was invented. Qualitative source terms (`fast`, `heavy`, `strong`)
were NOT mapped to numbers; source §8.3/§20.3 forbid it.

## PASS 5 — Representation/compiler findings

Carrier roles (JSON canonical / YAML authored / XML ordered-projection / NL
lossy projection / JSONL append-only evidence) → `runtime/07_compiler/carrier_planner/`.
Capability classes native/approximate/semantic/unsupported + compilation-loss
record + fail-closed → `runtime/07_compiler/semantic_mapping/`.
Round-trip tests must target resolved JSON, not textual equality.

## PASS 6 — Cross-department interfaces

motion×physics, motion×camera, state×continuity, causality×editing,
style×motion, camera×lighting (not affected), blocking×camera (not affected).
Active interfaces recorded in card front-matter of objects 2, 6, 10, 12, 13, 15, 16, 17.

## PASS 7 — Contradictions / limitations

- No internal contradictions detected.
- Boundary: continuity/causality objects are PROPOSALS, not external standards (§28).
- Boundary: no carrier superiority claim is supported (§16.1) — experiment required.
- Boundary: force from ordinary monocular video is estimation under a model,
  never measurement (§8).
- Missing referenced artifacts: KB zip, `Pasted markdown(9).md`.

## PASS 8–10 — Placement, dedup, operationalization

All placements listed in PASS 3 table. Retrieval role: route cards are the
discovery surface; secondary routes are declared in front-matter rather than
duplicated files. Compiler implications recorded per card. Verification
implications consolidated in `verification/semantic/verification_contract.md`.

## PASS 11 — Coverage audit (section dispositions)

| § | Content | Disposition |
| --- | --- | --- |
| 1 | Executive gap closure | DISTILLED (cards 1–4, 6, 15, 18, 19) |
| 2 | Evidence ledger table | DISTILLED — reproduced below |
| 3 | Canonical semantic representation | DISTILLED (epistemic firewall + carrier doctrine) |
| 4 | Rotation representation | DISTILLED (card 4) |
| 5 | Bilateral + FACS | DISTILLED (card 5; FACS layer rule folded into card 1 firewall examples) |
| 6 | Phase grammar | DISTILLED (card 8) |
| 7 | Kinematics/measurement | DISTILLED (card 9) |
| 8 | Dynamics fail-closed | DISTILLED (cards 10, 11, 2) |
| 9 | Interaction lifecycle | DISTILLED (card 12) |
| 10 | Continuity/causality closure | DISTILLED (cards 13, 14, object 20) |
| 10' | Camera grammar | DISTILLED (card 15) |
| 11 | Style grammar | DISTILLED (card 16) |
| 12 | Complexity | DISTILLED (card 17) |
| 13 | Representation equivalence | DISTILLED (card 18) |
| 14 | Compiler semantics | DISTILLED (card 19) |
| 15 | Provider implications | PROVIDER_SPECIFIC (cards in providers/runway, veo, kling) |
| 16 | Carrier experiment | EXPERIMENT_ONLY (object 21) |
| 17 | Verification contract | DISTILLED (object 23) |
| 18 | Implementation placement | SUPPORTS_EXISTING (placement honored by this distillation) |
| 19 | Object family | DISTILLED (object 20, PROJECT_DERIVED) |
| 20 | Critical design corrections | DISTILLED (cards 1, 7, 10, 19) |
| 21 | Schema sketch | DISTILLED (folded into object 20 schema) |
| 22 | JSONL audit record | EXAMPLE_ONLY (retained as evidence-model example in card 2) |
| 23 | Research-to-runtime example | EXAMPLE_ONLY (near-miss punch; retained in card 12) |
| 24 | Priority order | DISTILLED (object 25 policy) |
| 25 | Closure matrix | DISTILLED — reproduced below |
| 26 | Agent build packet | DISTILLED (object 20 schema + fixtures/tests lists retained in ledger) |
| 27 | Architectural conclusion | DISTILLED (card 1) |
| 28 | Revision note | DISTILLED (source registration) |
| 29 | Cited sources | DISTILLED (source registry U01–U16) |

No meaningful section remains undispositioned.

## §2 Evidence ledger (verbatim semantics preserved)

| Field | Meaning | Evidence class | Source | Measurement status | CPCS status |
| --- | --- | --- | --- | --- | --- |
| root.position | root translation in declared frame | established concept + proposed field | SMPL/Human3.6M | measurable when scale/frame known, else estimated | implementable |
| root.orientation | root orientation in declared frame | established + proposed | SMPL; rotation lit. | measured/estimated | implementable |
| joint.rotation | local joint rotation vs parent | established | SMPL | measured/estimated | implementable |
| velocity | 1st temporal derivative | physics + proposed | mechanics; pose lit. | derived | implementable |
| acceleration | 2nd derivative | physics + proposed | mechanics | derived | implementable |
| jerk | 3rd derivative | mathematical | proposed CPCS use | derived, noise-sensitive | experimental/optional |
| trajectory | time-ordered state path | established + proposed | pose/video lit. | derived | implementable |
| phase | temporal segment with semantic role | supported + CPCS grammar | McNeill; robotics | observed/inferred/derived | implementable |
| anticipation | preparatory movement | supported | gesture/skilled-action lit. | observed/inferred | implementable |
| contact | temporal/spatial interaction event | supported | HOI literature | detected/estimated/observed | implementable |
| force | physical interaction force | established physics | OpenStax; inverse dynamics | generally ESTIMATED from video | **fail-closed by default** |
| mass_class | qualitative mass behavior | proposed abstraction | no universal standard | authored/inferred | experimental |
| camera.intrinsics | optical/image-formation params | established CV | OpenCV | measured/calibrated/unknown | implementable |
| camera.motion | camera pose/motion semantic | provider + cinematography | Runway/Veo/Kling | authored/detected/estimated | implementable |
| style.invariants | properties style preserves | proposed | no universal standard | authored/evidence-derived | implementable |
| complexity_score | bounded risk heuristic | proposed metric | no external calibration | low until benchmarked | **experiment required** |
| carrier_effect | JSON/YAML/XML/NL adherence impact | experimental question | structured-output research | requires CPCS benchmark | **experiment required** |

## §25 Closure matrix (compressed)

Motion state P0 · rotation convention P0 · bilateral P0 · phase grammar P0 ·
force certainty P1 (fail-closed) · interaction lifecycle P0 · camera image
formation P1 · style decomposition P1 · continuity under occlusion P0 ·
causal event structure P0 · evidence taxonomy P0 · complexity P2 (calibrate) ·
carrier choice P2 (experiment) · provider capability P0 (continuous) ·
verification P0.

## Retained from §26 build packet

Fixtures (30) and tests (25) lists are retained here as the seed of
`tests/fixtures/` and `tests/semantic/` rather than as knowledge routes:
right/left reach, asymmetric/symmetric bilateral, punch contact/near-miss,
kick, grab/hold/release, throw, jump/land, turn, recoil, camera locked/pan/
tilt/dolly/orbit/handheld/rack-focus, unsupported focal-length request,
unknown/estimated force, occluded contact, multi-actor identity burden, style
forbidden drift, splash occlusion reentry, object continuity through occlusion,
causal miss without contact, identity-preserving partial occlusion,
contradictory identity evidence.

## File coverage result

```yaml
distillation_status:
  sections_discovered: 29
  sections_assessed: 29
  sections_dispositioned: 29
  semantic_findings: 19
  numerical_findings: 8
  representation_findings: 2
  interface_findings: 5
  contradictions: 0
  gaps: 14
  existing_objects_reused: 0
  existing_objects_extended: 0
  new_objects_proposed: 25
  unresolved_items:
    - KB zip package claims not verifiable from supplied files
    - Pasted markdown(9).md critique not present in repository
  coverage: full (every meaningful section explicitly dispositioned)
```
