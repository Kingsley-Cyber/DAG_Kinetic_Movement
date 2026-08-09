---
distillation_id: DIST-005
source_id: SRC-005
status: complete
coverage: full
---

# Distillation Ledger — SRC-005

`04.5-CPCS_MX_Hierarchical_Motion_Grammar_Research_Paper.md` → CPCS knowledge tree.
Distilled 2026-08-09. All objects below were written into their primary routes;
this ledger is the audit trail.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-005_...md`. CPCS-MX hierarchical
motion grammar research paper (v1.0, 4,182 lines, 32 sections + 5 appendices,
28 source units U01–U28). Authored research monograph. Self-declared
limitations: CPCS-MX is a PROPOSED synthesis and schema, not an international
standard; biomechanical fields are not medical diagnosis; a validated score
does not guarantee generative model compliance; combat examples are virtual or
professionally staged screen action; monocular video cannot uniquely determine
hidden depth, forces, torques, or off-camera motion.

## PASS 1 — Structural map

Multi-layer source (32 sections + 5 appendices):

§1 Research problem, contributions, exactness taxonomy · §2 Evidence and claim
taxonomy (7 evidence classes, 6 research-status labels) · §3 Layered
architecture (14 layers) · §4 Time, clocks, units, coordinate systems (8
frames) · §5 Skeleton topology, DoF, joint limits (3 limit domains) · §6–§8
Root motion, joint tracks, kinematics/kinetics · §9 IK, retargeting,
morphology · §10 Motion phases, contacts, action graphs (8 contact types, 6
edge meanings) · §11 Hard/soft/perceptual constraints · §12–§15 Laban, Effort
phrasing, FACS/face/gaze/breath, mannerisms · §16 Natural movement and
high-fidelity UGC · §17 Staged combat and multi-actor action coding · §18
Anime, sakuga, limited animation, cartoon physics · §19 Superhuman motion as
constrained transformation · §20 Secondary and overlapping motion · §21 BVH,
FBX, dense arrays, canonical interchange · §22 Procedural animation, motion
matching, engine execution (4 root modes) · §23 AI motion synthesis and
controllable video generation · §24 Text-to-CPCS-MX compilation (10 stages) ·
§25 Canonical schema design (JSON Schema 2020-12) · §26 Constraint resolution
and compilation (15 passes) · §27 Verification and perceptual evaluation ·
§28 Cross-style modular switching (5 profiles) · §29 Agent architecture and
RAG ingestion (10 agent roles, 9 record types) · §30 Experimental program
(7 questions, ablation A–G) · §31 Limitations, rights, safety, ethics · §32
Conclusions · App A–E Field dictionary, JSON example, YAML example, validation
checklist, glossary.

## PASS 2 — Existing-knowledge search

Repository authority was non-empty (SRC-001 through SRC-004 populated ~113
canonical owners). REUSE candidates identified: SRC-003 covers joint tracks,
root motion, constraints, Laban, retargeting, secondary motion; SRC-002 covers
FACS/face/gaze/breath and Laban doctrine; SRC-001 covers video observation and
carrier semantics. EXTEND candidates identified for 6 existing owners.
Remaining objects placed as new canonical owners. Dedup obligation: later
sources MUST check against objects registered by SRC-001 through SRC-005.

## PASS 3–7 — Extraction summary

### New objects written (primary route → file)

| # | Object | kind | route |
| --- | --- | --- | --- |
| 1 | Exactness taxonomy (6 dimensions) | vocabulary | `knowledge/00_foundations/epistemology/` |
| 2 | Layer architecture (14 layers) | schema_draft | `knowledge/00_foundations/architecture/` |
| 3 | Timebase and coordinate systems (8 frames) | contract | `knowledge/00_foundations/numerical_representation/` |
| 4 | Skeleton topology, DoF, joint limits (3 domains) | schema_draft | `knowledge/06_body_motion/biomechanics/` |
| 5 | Superhuman motion transform vector | schema_draft | `knowledge/06_body_motion/root_motion/` |
| 6 | Staged combat and multi-actor action coding | mechanism | `knowledge/06_body_motion/action_primitives/` |
| 7 | Anime, sakuga, limited animation representation | schema_draft | `knowledge/16_style_visual_language/` |
| 8 | BVH/FBX interchange manifests + loss accounting | contract | `runtime/07_compiler/` |
| 9 | Motion matching and engine execution | mechanism | `runtime/07_compiler/` |
| 10 | Text-to-CPCS-MX compilation | mechanism | `runtime/04_synthesis/` |
| 11 | Canonical schema design | schema_draft | `runtime/06_canonical/` |
| 12 | Constraint resolution and compilation | mechanism | `runtime/06_canonical/` |
| 13 | Agent architecture and RAG ingestion | mechanism | `research/sources/` |
| 14 | CPCS-MX experimental program | mechanism | `research/sources/experiments/` |

### Existing objects EXTENDED (SRC-001/SRC-002/SRC-003 owners)

| # | Object | Existing route | SRC-005 additions |
| --- | --- | --- | --- |
| E1 | Evidence two-axis model | `knowledge/00_foundations/uncertainty/` | 7 CPCS-MX evidence classes (measured/detected/inferred/interpreted/authored/simulated/derived); 6 research-status labels; provenance/conflict resolution (authority + locks, creative override) |
| E2 | Motion field separation | `knowledge/00_foundations/numerical_representation/` | Primary vs derived tracks; authority order (locked event timing → secondary simulation) |
| E3 | Causal event semantics | `knowledge/00_foundations/causality/` | Action graph edges (before/overlaps/causes/requires/targets/interrupts); typed contact taxonomy |
| E4 | Style mechanics | `knowledge/16_style_visual_language/` | Style transform vector with named dimensions; 5 profiles (natural/UGC/feature/anime/superhuman); cross-style invariants; style ablation |
| E5 | Verification layers | `verification/` | 8 verification metric vectors; layer-localized error diagnosis |
| E6 | Interaction lifecycle | `knowledge/07_interaction_contact/actor_object/` | 8-type contact taxonomy; contact record fields; fight-shot causal bundle |

## PASS 4 — Numerical findings (all dispositioned)

| Finding | Class | Value | Disposition |
| --- | --- | --- | --- |
| Rational fps example | PROPOSED | 24000/1001 (§4.1) | example timebase; not universal |
| Contact tolerance example | PROPOSED | 0.0417 s (§25.5) | example tolerance; threshold remains null until calibrated |
| Freeze duration default | PROPOSED | 0.45 s (§24.6) | named default profile `cinematic_human_v2`; versioned, not universal |
| Superhuman scale values | PROPOSED | gravity 0.68, impulse 1.9 etc. (§19.2) | project controls, not standardized units |
| Style transform values | PROPOSED | timing 1.35, smear 0.80 (§28.2) | project controls, not standardized perceptual units |
| Joint limit range example | PROPOSED | elbow [-0.05, 2.62] rad (§5.1) | illustrative, not a universal clinical range |

No precision was invented. All numeric examples are explicitly labeled as
illustrative or project controls, never universal thresholds.

## PASS 5 — Representation/compiler findings

- **14-layer architecture**: Intent → Action graph → Phase → Root → Joint →
  Contact → Dynamics → Laban → Face → Mannerism → Secondary → Stylization →
  Presentation → Verification; primary vs derived tracks with authority order.
- **6 exactness dimensions**: clock/screen-space/rig-space/world-space/
  dynamic/perceptual; vector of compliance dimensions, not a single score.
- **8 coordinate frames**: world, character root, pelvis/body, joint local,
  camera, screen, object, contact.
- **7 evidence classes + 6 research-status labels**: measured/detected/
  inferred/interpreted/authored/simulated/derived; ESTABLISHED through
  OPERATIONALIZATION.
- **3 joint-limit domains**: anatomical_reference, rig_safe,
  virtual_stylized; skeleton solver must not exceed rig_safe via stylized layer.
- **8 contact types**: support/grasp/surface_touch/staged_near_contact/
  simulated_impact/environmental_collision/attachment/break_contact.
- **6 action-graph edge meanings**: before/overlaps/causes/requires/targets/
  interrupts.
- **4 root-motion execution modes**: clip_driven/controller_driven/
  constraint_driven/hybrid_warped.
- **10 text-compilation stages** with provenance at each stage; intent
  separated from implementation; reverse compilation distinguishes lossless
  controls from textual fallbacks.
- **JSON Schema 2020-12**: track/interval/event/Laban/face/breath/constraint
  objects; extension namespacing; explicit migrations.
- **Typed merge table**: 9 value types with distinct merge operations;
  generic deep-merge insufficient.
- **15 compilation passes**; immutable intermediate artifacts with hashes;
  deterministic build identity.
- **10 agent roles with prohibited behaviors; 9 RAG record types; 10 JSONL
  parser requirements; 7 knowledge-graph relationship types.**
- **Style**: scalar style_intensity expands into named dimensions; 5
  profiles; invariants; one-dimension-at-a-time ablation.
- **Verification**: metric vectors never collapsed into one score;
  phase-labeled smoothness (impact discontinuity is not a failure);
  layer-localized error diagnosis.

## PASS 6 — Cross-department interfaces

exactness_taxonomy × evidence_two_axis_model; exactness_taxonomy ×
canonical_schema; layer_architecture × motion_field_separation;
layer_architecture × exactness_taxonomy; timebase_systems × exactness_taxonomy
× canonical_schema; skeleton_topology × retarget_contract × canonical_schema ×
interchange_manifests; superhuman_transform × anime_sakuga × style_mechanics ×
skeleton_topology; combat_coding × interaction_lifecycle ×
causal_event_semantics × relative_motion; anime_sakuga × superhuman_transform
× layer_architecture; interchange_manifests × format_ownership ×
canonical_schema; motion_matching × constraint_compilation × retarget_contract;
text_compilation × canonical_schema × constraint_compilation ×
evidence_two_axis_model; canonical_schema × constraint_compilation ×
interchange_manifests; constraint_compilation × canonical_schema ×
skeleton_topology × motion_matching × format_ownership; rag_ingestion ×
canonical_schema × text_compilation × evidence_two_axis_model;
cpcs_mx_experiments × layer_architecture × constraint_compilation ×
verification_contract.

## PASS 7 — Contradictions / limitations

- No internal contradictions detected within SRC-005.
- Boundary: CPCS-MX is a PROPOSED synthesis and schema, not an international
  standard (§31).
- Boundary: biomechanical fields are not medical diagnosis or individualized
  real-world performance instruction (§31).
- Boundary: a validated score does not guarantee generative model compliance
  (§29.7).
- Boundary: combat examples describe virtual animation or professionally
  staged screen action, not real-world injury optimization (§17.1).
- Boundary: monocular video cannot uniquely determine hidden depth, forces,
  torques, or off-camera motion (§1.2, §4.4).
- Boundary: joint-limit numerical ranges are illustrative, not universal
  clinical ranges (§5.1).
- Boundary: superhuman transformation vector applies to virtual characters
  only; invariants prevent breaking action readability (§19).
- Boundary: Laban descriptor and computational proxy are separate; a proxy
  must not be presented as the universal definition of a concept (§2.2,
  §25.6).

## PASS 8–10 — Placement, dedup, operationalization

All placements listed in PASS 3 table. EXTEND applied to 6 existing
SRC-001/SRC-002/SRC-003 owners (E1–E6); remaining 14 objects placed as new
canonical owners. Knowledge-layer objects placed in existing
00_foundations/, 06_body_motion/, 16_style_visual_language/ routes.
Compiler/runtime objects placed in existing runtime/04_synthesis/,
runtime/06_canonical/, runtime/07_compiler/ routes. Agent/RAG and experiments
placed in existing research/sources/ routes. No duplicates found. Overlap with
SRC-003 (joint tracks, constraints, Laban, retargeting) dispositioned as
REUSE — content covered by existing cards was not re-created. The 14 new
objects cover only concepts absent from the existing tree (exactness
taxonomy, layer architecture, timebase, skeleton topology, superhuman
transform, combat coding, anime representation, interchange manifests, motion
matching, text compilation, canonical schema, constraint compilation, RAG
ingestion, experimental program).

## PASS 11 — Coverage audit (section dispositions)

| § | Content | Disposition |
| --- | --- | --- |
| 1 | Research problem, contributions, exactness | DISTILLED (object 1) |
| 2 | Evidence and claim taxonomy | DISTILLED (E1) |
| 3 | Layered architecture | DISTILLED (object 2 + E2) |
| 4 | Time, clocks, units, coordinate systems | DISTILLED (object 3) |
| 5 | Skeleton topology, DoF, joint limits | DISTILLED (object 4) |
| 6–8 | Root motion, joint tracks, kinematics/kinetics | DISTILLED (REUSE SRC-003 cards) |
| 9 | IK, retargeting, morphology | DISTILLED (REUSE SRC-003 retarget_contract) |
| 10 | Motion phases, contacts, action graphs | DISTILLED (E3 + E6) |
| 11 | Hard, soft, perceptual constraints | DISTILLED (REUSE SRC-003 constraint_model) |
| 12–15 | Laban, Effort phrasing, FACS/face/gaze/breath, mannerisms | DISTILLED (REUSE SRC-002/SRC-003) |
| 16 | Natural movement, high-fidelity UGC | DISTILLED (partial REUSE SRC-003) |
| 17 | Staged combat, multi-actor coding | DISTILLED (object 6) |
| 18 | Anime, sakuga, limited animation | DISTILLED (object 7) |
| 19 | Superhuman motion | DISTILLED (object 5) |
| 20 | Secondary and overlapping motion | DISTILLED (REUSE SRC-003 material_response) |
| 21 | BVH, FBX, dense arrays, interchange | DISTILLED (object 8) |
| 22 | Procedural animation, motion matching, engine | DISTILLED (object 9) |
| 23 | AI motion synthesis, controllable video | DISTILLED (REUSE SRC-001/SRC-003) |
| 24 | Text-to-CPCS-MX compilation | DISTILLED (object 10) |
| 25 | Canonical schema design | DISTILLED (object 11) |
| 26 | Constraint resolution and compilation | DISTILLED (object 12) |
| 27 | Verification and perceptual evaluation | DISTILLED (E5) |
| 28 | Cross-style modular switching | DISTILLED (E4) |
| 29 | Agent architecture and RAG ingestion | DISTILLED (object 13) |
| 30 | Experimental program | DISTILLED (object 14) |
| 31 | Limitations, rights, safety, ethics | DISTILLED (PASS 7 boundaries) |
| 32 | Conclusions | DISTILLED (registration) |
| App A–E | Field dictionary, JSON/YAML examples, checklist, glossary | DISTILLED (registration U28) |

No section remains undispositioned.

## File coverage result

```yaml
distillation_status:
  sections_discovered: 37
  sections_assessed: 37
  sections_dispositioned: 37
  semantic_findings: 22
  numerical_findings: 6
  representation_findings: 18
  interface_findings: 16
  contradictions: 0
  gaps: 10
  existing_objects_reused: 6
  existing_objects_extended: 6
  new_objects_proposed: 14
  coverage: full
```
