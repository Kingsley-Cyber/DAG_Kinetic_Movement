---
distillation_id: DIST-002
source_id: SRC-002
status: complete
coverage: full
---

# Distillation Ledger — SRC-002

`02_FACS_LABAN_BARTENIEFF_GAP_CLOSURE_COMPLETED.md` → CPCS knowledge tree.
Distilled 2026-08-08. All objects below were written into their primary routes;
this ledger is the audit trail.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-002_...md`. CPCS-internal research
closure (v1.2), authored, citing 13 external primary sources (U01–U13).
Self-declared limitation: the frozen KB package it closes gaps against was not
supplied, so package-level coverage claims are **not verifiable from the
supplied files**. FACS 2002 scoring rules are proprietary/licensed — must not
be reconstructed from secondary lists. Layer-2 operational objects are largely
CPCS proposals, not externally established facts.

## PASS 1 — Structural map

Two-layer source (4,937 lines, 61 numbered sections):

**Layer 1 — semantic/measurement closure** (§1–§32): (1) scope, (2) evidence
ledger, (3) FACS event model, (4) AU catalog + version rule, (5) AU relation
layer, (6) autodetection contract, (7) measurement contract, (8) affect
boundary AU12≠happy, (9) VAD trajectory, (10) Laban five-category structure,
(11) proxy measurement, (12) numeric calibration contract, (13) reliability
contract, (14) Bartenieff six patterns, (15) bilateral asymmetry, (16)
combined performance event, (17) integration principles, (18) compiler
semantics, (19) representation equivalence, (20) carrier experiment, (21)
verification suite, (22) fixtures, (23) closure matrix, (24) build packet,
(25) conclusion, (26–32) revision/cited sources.

**Layer 2 — operational/application closure** (second §18–§61): (L2.18)
operational knowledge model, (L2.19–20) applicability/contraindication,
(L2.21–22) generative realization + action-conditioned mapping, (L2.23)
control scope, (L2.24) control envelopes, (L2.25) temporal coupling,
(L2.26) causal graph, (L2.27) continuity/persistence/occlusion, (L2.28)
observability-conditioned selection, (L2.29) priority/attention budget,
(L2.30) cross-framework composition, (L2.31) body topology, (L2.32)
multi-actor coordination, (L2.33) intent→control mapping, (L2.34) semantic
guardrails, (L2.35) minimal-pair corpus, (L2.36) provider fallback ladder,
(L2.37) verification expectation model, (L2.38) revised performance event,
(L2.39) graph relations, (L2.40) universal relation vocabulary, (L2.41)
retrieval requirements, (L2.42) director decision procedure, (L2.43–45)
worked examples, (L2.46) measurement extension, (L2.47) FACS automation
boundary, (L2.48) LMA numeric encoding, (L2.49) model-conditioning
experiments, (L2.50) reasoning completeness score, (L2.51) agent retrieval
contract, (L2.52) implementation placement, (L2.53) test fixtures,
(L2.54) director control IR, (L2.55) failure-mode catalog, (L2.56) open
questions, (L2.57) closure criteria, (L2.58) closure matrix, (L2.59–61)
operational build packet, final verdict.

> Source defect: the operational layer restarts section numbering at §18,
> colliding with Layer 1's §18–§32. Ledger uses L1.§N / L2.§N notation.
> No content lost.

## PASS 2 — Existing-knowledge search

Repository authority was non-empty (SRC-001 populated 25 canonical owners +
governance + experiments + gaps + fixtures). REUSE/EXTEND candidates identified
for 9 existing SRC-001 owners; remaining objects placed as new canonical
owners. Dedup obligation: all later sources MUST check against objects
registered by SRC-001 and SRC-002.

## PASS 3–7 — Extraction summary

### New objects written (primary route → file)

| # | Object | kind | route |
| --- | --- | --- | --- |
| 1 | FACS descriptive not emotion | boundary | `knowledge/04_character_performance/facs/` |
| 2 | FACS intensity ordinal A–E | contract | `knowledge/04_character_performance/facs/` |
| 3 | FACS versioning rule (2002) | rule | `knowledge/04_character_performance/facs/` |
| 4 | FACS AU catalog (version-aware) | vocabulary | `knowledge/04_character_performance/facs/` |
| 5 | FACS relation layer | vocabulary | `knowledge/04_character_performance/facs/` |
| 6 | FACS autodetection contract | contract | `knowledge/04_character_performance/facs/` |
| 7 | FACS bilateral asymmetry | principle | `knowledge/04_character_performance/facs/` |
| 8 | FACS temporal event | model | `knowledge/04_character_performance/facs/` |
| 9 | Affect VAD trajectory | model | `knowledge/04_character_performance/affect/` |
| 10 | Laban proxy measurement contract | contract | `knowledge/06_body_motion/laban_bess/` |
| 11 | Laban numeric calibration contract | contract | `knowledge/06_body_motion/laban_bess/` |
| 12 | Laban reliability contract (Krippendorff α) | contract | `knowledge/06_body_motion/laban_bess/` |
| 13 | Bartenieff six patterns | vocabulary | `knowledge/06_body_motion/bartenieff/` |
| 14 | Body topology + support/bridge | principle | `knowledge/06_body_motion/biomechanics/` |
| 15 | Universal relation vocabulary | vocabulary | `knowledge/00_foundations/causality/` |
| 16 | Performance expression event | schema | `schemas/world_model/` |
| 17 | Applicability + contraindication rules | ruleset | `runtime/05_strategy/constraints/` |
| 18 | Observability-conditioned selection | ruleset | `runtime/05_strategy/constraints/` |
| 19 | Semantic guardrails | ruleset | `runtime/05_strategy/constraints/` |
| 20 | Control envelopes (state/transition/apex/recovery) | model | `runtime/06_canonical/` |
| 21 | Director control IR | schema | `runtime/06_canonical/control_registry/` |
| 22 | Generative realization layer | schema | `runtime/06_canonical/control_registry/` |
| 23 | Control scope (mandatory + inheritance) | policy | `runtime/06_canonical/field_policies/` |
| 24 | Temporal coupling | model | `runtime/06_canonical/temporal_tracks/` |
| 25 | Director decision procedure (12-step) | procedure | `runtime/04_synthesis/` |
| 26 | Cross-framework composition | ruleset | `runtime/04_synthesis/performance/` |
| 27 | Control priority + attention budget | policy | `runtime/07_compiler/salience_budgeting/` |
| 28 | Provider fallback ladder (5-rung) | ladder | `runtime/08_provider_negotiation/text_fallback/` |
| 29 | Intent→control mapping | mapping | `runtime/00_request/intent/` |
| 30 | Agent retrieval contract | contract | `runtime/03_retrieval/` |
| 31 | Verification expectation model | method | `verification/semantic/` |
| 32 | Failure-mode catalog (14 rows) | taxonomy | `verification/failures/` |
| 33 | Operational knowledge model (6 strata) | policy | `00_governance/policies/` |
| 34 | Reasoning completeness score (RCS) | policy | `00_governance/policies/` |
| 35 | SRC-002 open research questions (25) | gap | `research/gaps/` |
| 36 | SRC-002 model-conditioning experiments | experiment | `research/sources/experiments/` |
| 37 | SRC-002 fixture & minimal-pair corpus | fixture_set | `research/sources/experiments/` |

### Existing objects EXTENDED (SRC-001 owners)

| # | Object | SRC-001 route | SRC-002 additions |
| --- | --- | --- | --- |
| E1 | Capability classes + loss records | `runtime/07_compiler/semantic_mapping/` | `unknown` fifth state; FACS loss example; 12-type loss taxonomy |
| E2 | Verification contract | `verification/semantic/` | FACS verification (8 rules); Laban/Bartenieff/Affect verification |
| E3 | Causal event semantics | `knowledge/00_foundations/causality/` | Predicate vocabulary (causes/enables/prevents/motivates); temporal≠causal |
| E4 | Visibility ≠ existence | `knowledge/18_sequence_continuity/occluded_hidden_state/` | Six-state visibility vocabulary; persistence lifetimes |
| E5 | Interaction lifecycle | `knowledge/07_interaction_contact/actor_object/` | 13 multi-actor coordination primitives; phase-offset |
| E6 | Universal kernel family | `schemas/world_model/` | MotionEvent extended: facial[]/laban{}/bartenieff[]/affect_target{}; 13 operational objects |
| E7 | Laban layering doctrine | `knowledge/06_body_motion/laban_bess/` | Five-category LMA structure table; reliability note |
| E8 | Epistemic firewall | `knowledge/00_foundations/invariants/` | Operational qualitative-to-numeric collapses (Sudden≠fast etc.) |
| E9 | Carrier role semantics | `runtime/07_compiler/carrier_planner/` | SRC-002 §22 confirmation (XML ordered/namespaced; NL is projection) |

## PASS 4 — Numerical findings (all dispositioned)

| Finding | Class | Value | Disposition |
| --- | --- | --- | --- |
| FACS intensity ordinal | STANDARDIZED_CODING_SCALE | A–E (U02) | canonical `A|B|C|D|E`; fixed numeric mapping prohibited |
| FACS detector output | DETECTOR_SCORE | [0,1] continuous (U05) | kept separate from A–E ordinal; `detected ≠ measured` |
| Laban effort factors | QUALITATIVE_POLARITY | Strong/Light · Sudden/Sustained · Direct/Indirect · Bound/Free | no numeric mapping; proxy only with `validation_status: uncalibrated` |
| Laban shape modes | QUALITATIVE_POLARITY | Spreading/Retreating · Rising/Sinking · Advancing/Retreating | same policy as effort |
| Krippendorff α (LMA) | EXPERIMENTAL_RESULT | weak-to-acceptable range (U09) | recorded as reliability boundary; no universal threshold claimed |
| VAD circumplex | COORDINATE_MODEL | valence/arousal (U08) | affect as separate layer; project-defined coordinates only |
| OpenFace AU intensity | DETECTOR_SCORE | [0,1] (U05) | observation-layer only; promotion to A–E requires coder-equivalence |
| Carrier experiment sizes | PROJECT_DERIVED_SCALE | 100 scenes × 6 carriers × 13 metrics | experiment design, not executed |
| RCS scoring | PROJECT_DERIVED_SCALE | 0–100 (10 questions × 10) | policy formula; not a validated psychometric instrument |

No precision was invented. Qualitative source terms (`Strong`, `Sudden`,
`Bound`, `Cross-Lateral`) were NOT mapped to numbers; source forbids it
(§12, L2.§48, L2.§44). Detector-continuous [0,1] scores kept separate from
A–E ordinal; no silent mapping.

## PASS 5 — Representation/compiler findings

- **Carrier roles**: JSON canonical / YAML authored / XML ordered-projection /
  NL lossy projection — EXTENDED existing owner (E9) with SRC-002 §22
  confirmation (XML for ordered/namespaced, NL is projection).
- **Capability classes**: `native`/`approximate`/`semantic`/`unsupported` +
  `unknown` (fifth state added in E1) + compilation-loss record + fail-closed.
- **Performance expression event**: combined canonical form with
  `controls[]` array (framework: facs/laban/bartenieff) — new schema (object 16).
- **Director control IR**: universal operational envelope YAML — new schema
  (object 21).
- **Generative realization layer**: `RealizationPrimitive` + action-conditioned
  mapping — new schema (object 22).
- Round-trip tests must target resolved JSON, not textual equality (inherited
  from SRC-001, confirmed by SRC-002 §19/L2.§22).

## PASS 6 — Cross-department interfaces

FACS×Laban (performance_expression_event combines both); FACS×Affect (AU12≠happy
boundary); Laban×Bartenieff (body topology bridges both); Bartenieff×Biomechanics
(support/bridge patterns); Control×Verification (envelopes→expectation model);
Intent×Control (mapping object); Retrieval×Director (retrieval contract feeds
decision procedure); Composition×Provider (fallback ladder);
Observability×Strategy (shot-scale→selection). Active interfaces recorded in
card front-matter of objects 16, 17, 20, 25, 26, 31.

## PASS 7 — Contradictions / limitations

- No internal contradictions detected within SRC-002.
- Boundary: Layer-2 operational objects are CPCS proposals
  (`cpcs_proposed` / `source_supported_interpretation`), not externally
  established facts (L2.§18, L2.§57).
- Boundary: FACS 2002 manual scoring rules are proprietary — secondary AU lists
  must not be treated as the manual (U02, §4).
- Boundary: no carrier superiority claim is supported (§20) — experiment required.
- Boundary: detector-continuous [0,1] ≠ A–E ordinal; `detected ≠ measured`
  (§6, U05).
- Boundary: LMA reliability is weak-to-acceptable (U09) — CMA proxy without
  calibration forbidden (§13, §12).
- Missing referenced artifacts: frozen ZIP package
  (`CPCS_FACS_Laban_AI_Video_Research_Package_v1.2.zip`) not attached.

## PASS 8–10 — Placement, dedup, operationalization

All placements listed in PASS 3 table. REUSE applied to 9 existing SRC-001
owners (E1–E9); remaining 37 objects placed as new canonical owners. Retrieval
role: route cards are the discovery surface; secondary routes declared in
front-matter rather than duplicated files. Operational-layer objects placed
into existing runtime routes (05_strategy, 06_canonical, 07_compiler,
08_provider_negotiation, 04_synthesis, 00_request, 03_retrieval) — no parallel
"FACS runtime" created (forbidden by L2.§52). Verification implications
consolidated in `verification/semantic/verification_contract.md` (E2) and
new `verification_expectation_model.md` (object 31).

## PASS 11 — Coverage audit (section dispositions)

### Layer 1

| § | Content | Disposition |
| --- | --- | --- |
| 1 | Scope | DISTILLED (objects 1–8, 16) |
| 2 | Evidence ledger | DISTILLED — reproduced below |
| 3 | FACS event model | DISTILLED (object 8) |
| 4 | AU catalog + version rule | DISTILLED (objects 3, 4) |
| 5 | AU relation layer | DISTILLED (object 5) |
| 6 | Autodetection contract | DISTILLED (object 6) |
| 7 | Measurement contract | DISTILLED (object 6 + PASS 4) |
| 8 | Affect boundary AU12≠happy | DISTILLED (object 1) |
| 9 | VAD trajectory | DISTILLED (object 9) |
| 10 | Laban five-category structure | DISTILLED (E7 + object 10) |
| 11 | Proxy measurement | DISTILLED (object 10) |
| 12 | Numeric calibration contract | DISTILLED (object 11) |
| 13 | Reliability contract | DISTILLED (object 12) |
| 14 | Bartenieff six patterns | DISTILLED (object 13) |
| 15 | Bilateral asymmetry | DISTILLED (object 7) |
| 16 | Combined performance event | DISTILLED (object 16 + E6) |
| 17 | Integration principles | DISTILLED (objects 16, 26) |
| 18 | Compiler semantics | DISTILLED (E1, E9) |
| 19 | Representation equivalence | DISTILLED (E9 + PASS 5) |
| 20 | Carrier experiment | EXPERIMENT_ONLY (object 36) |
| 21 | Verification suite | DISTILLED (E2 + object 31) |
| 22 | Fixtures | DISTILLED (object 37) |
| 23 | Closure matrix | DISTILLED — reproduced below |
| 24 | Build packet | SUPPORTS_EXISTING (placement honored by this distillation) |
| 25–32 | Conclusion / revision / cited sources | DISTILLED (source registration) |

### Layer 2

| § | Content | Disposition |
| --- | --- | --- |
| L2.18 | Operational knowledge model | DISTILLED (object 33) |
| L2.19–20 | Applicability / contraindication | DISTILLED (object 17) |
| L2.21–22 | Generative realization + action-conditioned | DISTILLED (objects 22, 29) |
| L2.23 | Control scope | DISTILLED (object 23) |
| L2.24 | Control envelopes | DISTILLED (object 20) |
| L2.25 | Temporal coupling | DISTILLED (object 24) |
| L2.26 | Causal graph | DISTILLED (E3 + object 15) |
| L2.27 | Continuity/persistence/occlusion | DISTILLED (E4) |
| L2.28 | Observability-conditioned selection | DISTILLED (object 18) |
| L2.29 | Priority/attention budget | DISTILLED (object 27) |
| L2.30 | Cross-framework composition | DISTILLED (object 26) |
| L2.31 | Body topology | DISTILLED (object 14) |
| L2.32 | Multi-actor coordination | DISTILLED (E5) |
| L2.33 | Intent→control mapping | DISTILLED (object 29) |
| L2.34 | Semantic guardrails | DISTILLED (object 19) |
| L2.35 | Minimal-pair corpus | DISTILLED (object 37) |
| L2.36 | Provider fallback ladder | DISTILLED (object 28 + E1 loss taxonomy) |
| L2.37 | Verification expectation | DISTILLED (object 31) |
| L2.38 | Revised performance event | DISTILLED (object 16 + E6) |
| L2.39 | Graph relations | DISTILLED (object 15) |
| L2.40 | Universal relation vocabulary | DISTILLED (object 15) |
| L2.41 | Retrieval requirements | DISTILLED (object 30) |
| L2.42 | Director decision procedure | DISTILLED (object 25) |
| L2.43–45 | Worked examples | EXAMPLE_ONLY (retained in cards as YAML examples) |
| L2.46 | Measurement extension | DISTILLED (objects 6, 10, 11 + E8) |
| L2.47 | FACS automation boundary | DISTILLED (object 6) |
| L2.48 | LMA numeric encoding | DISTILLED (object 11 + PASS 4) |
| L2.49 | Model-conditioning experiments | EXPERIMENT_ONLY (object 36) |
| L2.50 | Reasoning completeness score | DISTILLED (object 34) |
| L2.51 | Agent retrieval contract | DISTILLED (object 30) |
| L2.52 | Implementation placement | SUPPORTS_EXISTING (placement honored) |
| L2.53 | Test fixtures | DISTILLED (object 37) |
| L2.54 | Director control IR | DISTILLED (object 21) |
| L2.55 | Failure-mode catalog | DISTILLED (object 32) |
| L2.56 | Open questions | DISTILLED (object 35) |
| L2.57 | Closure criteria | DISTILLED (object 33) |
| L2.58 | Closure matrix | DISTILLED — reproduced below |
| L2.59–61 | Build packet / final verdict | DISTILLED (object 16 + E6) |

No meaningful section remains undispositioned.

## §2 Evidence ledger (Layer 1, verbatim semantics preserved)

| Field | Meaning | Evidence class | Source | Measurement status | CPCS status |
| --- | --- | --- | --- | --- | --- |
| facial.action_unit | FACS AU activation (side-indexed) | established (U01, U02) | FACS 2002 | coded by trained coder; detector presence/intensity separate | implementable |
| facial.intensity | A–E ordinal intensity | standardized scale (U02) | FACS 2002 | coded; detector-continuous [0,1] separate | implementable (no numeric mapping) |
| facial.onset/apex/offset | temporal event phases | proposed (U04) | CPCS extension | inferred from coded frames | implementable |
| facial.laterality | L/R bilateral designation | established | FACS 2002 | coded; asymmetry = semantic | implementable |
| laban.effort | Strong/Light · Sudden/Sustained · Direct/Indirect · Bound/Free | supported (U09, U10) | LMA literature | authored; proxy uncalibrated | implementable (proxy only) |
| laban.shape | Spreading/Retreating · Rising/Sinking · Advancing/Retreating | supported (U09) | LMA literature | authored; proxy uncalibrated | implementable (proxy only) |
| laban.phrasing | beginning/middle/end segmentation | proposed | LMA practice | authored | implementable |
| bartenieff.pattern | connectivity pattern (6 types) | supported (U12) | Bartenieff & Lewis | authored/observed | implementable |
| affect.valence | pleasantness axis | established (U08) | circumplex model | authored; project-defined | implementable (separate layer) |
| affect.arousal | activation axis | established (U08) | circumplex model | authored; project-defined | implementable (separate layer) |
| affect.dominance | control axis | supported | circumplex extensions | authored; project-defined | implementable (separate layer) |

## §23 / L2.58 Closure matrix (compressed)

Layer 1: FACS event model P0 · intensity ordinal P0 · versioning P0 · AU
catalog P0 · relation layer P0 · autodetection contract P0 · affect boundary
P0 · Laban structure P0 · proxy measurement P0 (uncalibrated) · numeric
calibration P2 (calibrate) · reliability P1 · Bartenieff P0 · performance event
P0 · compiler P0 · verification P0.

Layer 2: operational model P0 · applicability P0 · realization P0 · control
scope P0 · envelopes P0 · temporal coupling P0 · causal graph P0 · continuity
P0 · observability P0 · priority/budget P0 · composition P0 · body topology P0
· multi-actor P0 · intent→control P0 · guardrails P0 · minimal-pair P1 (corpus
to be built) · provider fallback P0 · verification expectation P0 · retrieval
P0 · director procedure P0 · RCS P1 (validate) · director IR P0 · failure modes
P0 · open questions P1 (research) · closure criteria P0.

## File coverage result

```yaml
distillation_status:
  sections_discovered: 61
  sections_assessed: 61
  sections_dispositioned: 61
  semantic_findings: 37
  numerical_findings: 9
  representation_findings: 6
  interface_findings: 9
  contradictions: 0
  gaps: 25
  existing_objects_reused: 0
  existing_objects_extended: 9
  new_objects_proposed: 37
  unresolved_items:
    - frozen ZIP package claims not verifiable from supplied files
    - FACS 2002 manual scoring rules proprietary (not reconstructable)
    - Layer-2 operational objects are CPCS proposals not externally established
  coverage: full (every meaningful section explicitly dispositioned)
```
