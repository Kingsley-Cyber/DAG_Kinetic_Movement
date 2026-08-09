---
distillation_id: DIST-004
source_id: SRC-004
status: complete
coverage: full
---

# Distillation Ledger — SRC-004

`04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE_COMPLETE.md` → CPCS knowledge tree.
Distilled 2026-08-08. All objects below were written into their primary routes;
this ledger is the audit trail.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-004_...md`. CPCS-internal research
closure (v1.0), authored, citing 14 source units (U01–U14): 5 ADRG package
files + 9 external primary sources. Self-declared limitation: ADRG does NOT
justify adding another framework; representations are CPCS proposals
(`PROPOSED_CPCS`), not externally established facts. Architecture rule: do NOT
create agent framework, graph database, scene ontology, canonical score,
provider compiler, or second reasoning authority (§18, §29).

## PASS 1 — Structural map

Single-layer source (2,208 lines, 30 sections):

§0 Executive result (BLUF: no new framework; 5 additions) · §1 Evidence basis
(5 classes) · §2 Gap closure (Gaps A–F: decision semantics, candidate
comparison, decision-aware routing, state contraction, causal design chain,
failure-to-decision linkage) · §3 Primary-source verification (CoT/ToT/GoT/
ReAct/Self-Refine/Self-Consistency/Least-to-Most, PROV, JSON Patch, JSON
Schema, 4-level verification) · §4 Semantic representation (ownership table)
· §5 Decision IR (DecisionRecord JSON schema) · §6 Decision graph (21
execution-only edges; design_causes vs causal_claim) · §7 Routing (5 features
+ routing matrix) · §8 State contraction (5 memory types; discard rules) · §9
Invariants/variant axes (hard/soft/controlled; variant deltas) · §10 Causal
reasoning contract (problem→treatment→decision→control→effect→verification;
7 claim classes) · §11 Reasoning trace (14-element without CoT) · §12
Research-to-decision examples (6) · §13 Format/compiler effect (ownership table)
· §14 Structured-output caution (parse ≠ schema ≠ decision ≠ render) · §15
Failure-directed reasoning (repair object; algorithm; escalation) · §16
Verification model (12 planner metrics; video metrics) · §17 Measurement form
(14 fields) · §18 Implementation placement (do NOT create; ADD to existing)
· §19 Minimal schemas (Candidate, Invariant, Consequence, Repair) · §20
Canonical ADRG graph example · §21 Canonical mapping (bridge to existing
compiler) · §22 Compiler semantics (realization statuses; loss records) · §23
State of implementation (comparison table) · §24 Controlled experiments
(E-ADRG-001 through 006) · §25 Promotion rules · §26 CPCS_CLOSURE_MATRIX (16
gaps × 7 columns) · §27 Build packet (concepts, fields, relations, ops,
validators, fixtures, tests, open questions) · §28 Implementation order (6
phases) · §29 Final determination · §30 Primary sources.

## PASS 2 — Existing-knowledge search

Repository authority was non-empty (SRC-001 + SRC-002 + SRC-003 populated ~95
canonical owners). REUSE candidates identified: existing reasoning policies,
canonical score, control translation, knowledge graph, provenance, validators,
carrier roles, generative realization, control envelopes/scope. EXTEND
candidates identified for 8 existing owners. Remaining objects placed as new
canonical owners. Dedup obligation: all later sources MUST check against objects
registered by SRC-001 through SRC-004.

## PASS 3–7 — Extraction summary

### New objects written (primary route → file)

| # | Object | kind | route |
| --- | --- | --- | --- |
| 1 | DecisionRecord + Candidate + Consequence | schema_draft | `runtime/04_synthesis/` |
| 2 | Director invariant + variant axes | schema_draft | `runtime/05_strategy/constraints/` |
| 3 | Execution edge vocabulary (21 edges) + causal distinction | vocabulary | `runtime/04_synthesis/` |
| 4 | Decision-aware routing (5 features + matrix) | schema_draft | `runtime/04_synthesis/` |
| 5 | State contraction (5 memory types) | schema_draft | `runtime/04_synthesis/` |
| 6 | Causal design chain (7 claim classes) | contract | `runtime/04_synthesis/` |
| 7 | Reasoning trace (14-element without CoT) | contract | `runtime/04_synthesis/` |
| 8 | Format ownership + structured-output caution | doctrine | `runtime/07_compiler/` |
| 9 | Measurement form (14 fields) | contract | `verification/` |
| 10 | Verification metrics (12 planner + video) | metric_contract | `verification/` |
| 11 | ADRG experiments (E-ADRG-001 through 006) + fixtures | experiment_design | `research/sources/experiments/` |
| 12 | Promotion rules + implementation order | policy | `00_governance/policies/` |

### Existing objects EXTENDED (SRC-001/SRC-002/SRC-003 owners)

| # | Object | Existing route | SRC-004 additions |
| --- | --- | --- | --- |
| E1 | Director decision procedure | `runtime/04_synthesis/` | DecisionRecord provenance; abstention outcomes (select/degrade/decompose/fallback/abstain/reject) |
| E2 | Repair strategy | `verification/` | JSON Patch repair (RFC 6902); base_digest; cause_candidates; repair algorithm; escalation policy; repair bound |
| E3 | Verification layers | `verification/` | 4-level verification separation (structural/semantic/perceptual/empirical); planner metrics cross-ref |
| E4 | Causal event semantics | `knowledge/00_foundations/causality/` | design_causes vs causal_claim distinction; causal design chain; decision-level vs event-level causality |
| E5 | Epistemic firewall | `knowledge/00_foundations/invariants/` | Structured-output caution (parse ≠ schema ≠ decision ≠ render) |
| E6 | Evidence two-axis model | `knowledge/00_foundations/uncertainty/` | ADRG evidence classes (PACKAGE_ESTABLISHED/REPO_OBSERVED/EXTERNAL_ESTABLISHED/PROPOSED_CPCS/EXPERIMENTAL) |
| E7 | Capability classes + loss records | `runtime/07_compiler/semantic_mapping/` | Realization statuses (8: native_exact through unsupported_error); compile loss → decision linkage |
| E8 | Control priority + attention budget | `runtime/07_compiler/salience_budgeting/` | Decision-aware routing features (impact/uncertainty/coupling/irreversibility/validator_strength) flowing into budget |

## PASS 4 — Numerical findings (all dispositioned)

| Finding | Class | Value | Disposition |
| --- | --- | --- | --- |
| Decision confidence | PROPOSED_CPCS | 0.81 (§5) | example value; not a universal threshold |
| Cause candidate confidence | PROPOSED_CPCS | 0.41, 0.37, 0.22 (§15) | example repair attribution; not calibrated |
| Routing features | EXPERIMENTAL | 0.0 default (§7) | proposed operational variables; all start at 0.0 |

No precision was invented. All routing features are explicitly proposed
operational variables, not universal scientific scales. No threshold was
calibrated.

## PASS 5 — Representation/compiler findings

- **21 execution-only edges**: separate namespace from knowledge-graph edges;
  projected into union graph for retrieval but authorities remain separate.
- **Design causality vs empirical causality**: design_causes (authored intent)
  ≠ causal_claim (requires controlled comparison).
- **Format ownership table**: NL (creative), YAML (canonical), JSON (execution),
  XML (exchange), JSONL (observation/audit), Media (evidence).
- **Structured-output caution**: parse validity ≠ schema validity ≠ decision
  correctness ≠ render success; reason/decide in compact semantic IR, then
  serialize as late as practical.
- **Realization statuses**: 8 statuses (native_exact, native_approximate,
  baked_into_reference, compressed_to_text, postprocess_only, evaluation_only,
  dropped_with_warning, unsupported_error).
- **State contraction**: 5 memory types with deterministic sha256 digest.
- **4-level verification**: structural → semantic → perceptual → empirical.
- **Minimal schemas**: Candidate, Invariant, Consequence, Repair — all JSON.
- **Canonical ADRG graph**: 4 planes (scene_intent_control, reasoning_execution,
  verification_experiment) with typed edges.
- **Compiler operations**: 13 (resolve_decision through revalidate).
- **Validators**: 10 ADRG-specific.
- **Fixtures**: 12 minimum.
- **Tests**: 15.
- **Implementation order**: 6 phases (semantic bridge → routing → compiler
  linkage → bounded repair → state contraction → experiments).

## PASS 6 — Cross-department interfaces

DecisionRecord × director_decision_procedure; DecisionRecord ×
director_control_ir; DecisionRecord × capability_classes_loss_records;
DirectorInvariant × constraint_feasibility; ExecutionEdges ×
causal_event_semantics; Routing × control_priority_attention_budget;
StateContraction × long_form_scheduler; StateContraction ×
observation_provenance; CausalDesignChain × causal_event_semantics;
ReasoningTrace × director_decision_procedure; FormatOwnership ×
epistemic_firewall; FormatOwnership × capability_classes_loss_records;
MeasurementForm × verification_contract; MeasurementForm ×
evidence_two_axis_model; VerificationMetrics × verification_layers;
RepairStrategy × failure_mode_catalog; PromotionRules ×
distillation_implementation_priority; ADRGExperiments ×
carrier_effect_experiment.

## PASS 7 — Contradictions / limitations

- No internal contradictions detected within SRC-004.
- Boundary: ADRG does NOT justify adding another reasoning/orchestration
  framework (§0, §18, §29).
- Boundary: do NOT create agent framework, graph database, scene ontology,
  canonical score, provider compiler, ADRGEngine, or second reasoning authority
  (§18).
- Boundary: do NOT move canonical control resolution into the LLM planner (§18).
- Boundary: ADRG should FEED the existing compiler, not replace it (§21).
- Boundary: execution edges are separate from knowledge-graph edges; do not
  inject all ADRG edges into authored edge policy (§6.1).
- Boundary: confidence is not probability of objective correctness (§5).
- Boundary: design_causes ≠ scientific causation; causal_claim requires
  controlled comparison (§6.2).
- Boundary: routing features are proposed operational variables, not universal
  scientific scales (§7.1).
- Boundary: self-consistency and critique do not require new top-level reasoning
  frameworks — they are operators inside the existing policy runtime (§7.2).
- Boundary: no universal claim that any single format or reasoning operator is
  globally superior (§30).

## PASS 8–10 — Placement, dedup, operationalization

All placements listed in PASS 3 table. EXTEND applied to 8 existing
SRC-001/SRC-002/SRC-003 owners (E1–E8); remaining 12 objects placed as new
canonical owners. All decision-level objects placed in existing
runtime/04_synthesis/ route — no parallel "ADRG runtime" created (forbidden by
§18). Director invariant placed in existing runtime/05_strategy/constraints/.
Format/ownership placed in existing runtime/07_compiler/. Verification objects
placed in existing verification/ route. Experiments placed in existing
research/sources/experiments/ route. Promotion rules placed in existing
00_governance/policies/ route. No duplicates found. SRC-003's ControlDecision
(control-level: select/degrade/decompose/fallback/abstain/reject) and SRC-004's
DecisionRecord (reasoning-level: question/candidates/criteria/decision) are
different layers and cross-reference each other.

## PASS 11 — Coverage audit (section dispositions)

| § | Content | Disposition |
| --- | --- | --- |
| 0 | Executive result | DISTILLED (objects 1–12 overview + E1–E8) |
| 1 | Evidence basis | DISTILLED (E6 evidence classes) |
| 2 | Executive gap closure | DISTILLED (registration Gaps A–F) |
| 3 | Primary-source verification | DISTILLED (registration U06–U14 + E3 4-level verification) |
| 4 | Semantic representation | DISTILLED (E1 ownership table) |
| 5 | Director Decision IR | DISTILLED (object 1) |
| 6 | Decision graph | DISTILLED (object 3 + E4) |
| 7 | Reasoning-method routing | DISTILLED (object 4 + E8) |
| 8 | State contraction | DISTILLED (object 5) |
| 9 | Invariants/variant axes | DISTILLED (object 2) |
| 10 | Causal reasoning contract | DISTILLED (object 6) |
| 11 | Reasoning trace | DISTILLED (object 7) |
| 12 | Research-to-decision examples | DISTILLED (object 1 examples) |
| 13 | Format/compiler effect | DISTILLED (object 8) |
| 14 | Structured-output caution | DISTILLED (E5 + object 8) |
| 15 | Failure-directed reasoning | DISTILLED (E2 + object 1 repair schema) |
| 16 | Verification model | DISTILLED (object 10) |
| 17 | Measurement form | DISTILLED (object 9) |
| 18 | Implementation placement | DISTILLED (§7 boundary) |
| 19 | Proposed minimal schemas | DISTILLED (objects 1, 2, E2) |
| 20 | Canonical ADRG graph | DISTILLED (PASS 5 representation) |
| 21 | Canonical mapping | DISTILLED (PASS 6 interface) |
| 22 | Compiler semantics | DISTILLED (E7) |
| 23 | State of implementation | DISTILLED (E1–E8 overview) |
| 24 | Controlled experiments | DISTILLED (object 11) |
| 25 | Promotion rules | DISTILLED (object 12) |
| 26 | CPCS_CLOSURE_MATRIX | DISTILLED (ledger) |
| 27 | Build packet | DISTILLED (PASS 5) |
| 28 | Implementation order | DISTILLED (object 12) |
| 29 | Final determination | DISTILLED (§7 boundary) |
| 30 | Primary sources | DISTILLED (registration) |

No section remains undispositioned.

## File coverage result

```yaml
distillation_status:
  sections_discovered: 30
  sections_assessed: 30
  sections_dispositioned: 30
  semantic_findings: 20
  numerical_findings: 3
  representation_findings: 14
  interface_findings: 18
  contradictions: 0
  gaps: 10
  existing_objects_reused: 0
  existing_objects_extended: 8
  new_objects_proposed: 12
  coverage: full
```
