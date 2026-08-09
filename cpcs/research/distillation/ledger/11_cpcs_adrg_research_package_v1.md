---
distillation_id: DIST-011
source_id: SRC-011
status: complete
coverage: full
---

# Distillation Ledger — SRC-011

`CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0` (22 files;
paper 2611 lines / 24 sections; RAG corpus 78 records) → CPCS knowledge tree.
Distilled 2026-08-09.

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-011_cpcs_adrg_research_package_v1.md`.
The ADRG Research Package v1.0 (`CPCS-ADRG-RP-2026-01`, 2026-07-23) is the
**primary research package** that SRC-004 cited as its U01; SRC-004 distilled
the internal closure analysis, SRC-011 distills the package itself. 22 source
units U01–U22. Epistemic class: research_package with an explicit evidence
boundary — engineering defaults are proposed until E-ADRG experiments run.

## PASS 1 — Structural map

**Paper (24 sections):** §1 executive thesis (5 principles: routing not fixed;
model-scaled policy; no raw CoT as canonical; one ontology multiple
serializations; every compilation step has a loss account) · §2 repository
baseline (ASL → CIR → TEP → VER) · §3 reasoning methods as operators (CoT
local decomposition, least-to-most default, ToT selective, GoT orchestration,
ReAct, self-consistency, Chain-of-Draft) · §4 decision ledger contract
(decision_id/question/alternatives/criteria/scores/selected/evidence_refs/
confidence/unresolved/loss; 3 risks of raw CoT: false provenance, retrieval
contamination, token/privacy overhead) · §5 G_R = (V_R, E_R, P, B, A); input
contract (hard_invariants + variation_axes); output contract (4 artifacts);
11 execution phases Phase 0–10 · §6 five graph planes (knowledge/evidence,
scene intent/control, reasoning execution, compilation/realization,
verification/experiments) + 6 cross-plane invariants · §7 node ontology (18
types) + status vocabulary (planned→ready→running→resolved/blocked/failed→
repaired→revalidated/superseded) · §8 edge ontology (~42 edges in 5 groups)
+ 8 edge constraints · §9 model-scaled policy (mini/standard/large) +
escalation record · §10 reasoning router D = w_I·I + w_U·U + w_C·C + w_R·R −
w_V·V; operator selection table; 5 branch-admission conditions; 6 early
pruning conditions; 100-unit reasoning budget ledger · §11 variant lattice
(invariants/axes/deltas; incompatibilities; maximum_simultaneous_deltas;
J(S) diversity) · §12 graph-aware RAG (bundle not chunk; 12 retrieval object
types; 10-step hybrid pipeline; R(o|q); expansion bounds depth 2 / 24 nodes;
coverage contract) · §13 NL contract (director-language pattern
[SHOT AND DURATION]/[SUBJECT AND ACTION]/[PERFORMANCE]/[TIMING]/[CAMERA AND
PRESENTATION]/[NEGATIVES]; observable-not-affect; 8-step compression) · §14
YAML contract (9 safety rules) · §15 JSON contract (4 validation levels;
constrained generation) · §16 XML contract (director envelope, namespaces
urn:cpcs:adrg:1.0, security) · §17 polyglot compiler (carrier ownership;
one authority per semantic path; 15 cross-format compile passes; direct
multi-format prompting = text_interpretation_only) · §18 worked example
(6s shot, mini policy A–G, XML envelope, compiled NL prompt, loss report) ·
§19 verifier (3 role separation; checkpoints A–I; bounded repair; compile-loss
ledger) · §20 repo integration (15 concept cards; 6 node kinds; 12 edges;
5-stage migration) · §21 experimental program (7 RQs; factors; 11 planner
metrics; video metrics; causal discipline; E-ADRG-001..005; promotion
criteria) · §22 security/limitations · §23 implementation blueprint (9
service boundaries) · §24 conclusion. References [S001]–[S042].

**Schemas:** `CPCS_ADRG_Reasoning_Graph_Schema.json` (schema_version const
"cpcs-adrg/1.0"; node 18-type/5-plane/9-status enums; edge 42-type enum +
realization_status 8-enum + allOf constraints: selected_over requires
decision_id, compiled_to requires target_adapter + realization_status;
decisionRecord required fields) · `CPCS_ADRG_RAG_Record_Schema.json` (6
evidence labels) · `CPCS_ADRG_Source_Index_Schema.json` (42 sources with
evidence_tier).

**Examples:** canonical_reasoning_graph.json (mini-policy worked graph),
director_request.yaml (hard_invariants + variation_axes +
maximum_simultaneous_deltas 2), director_envelope.xml (beat/recognition/
recovery), compiled_natural_language_prompt.txt (1-shot NL output),
planner_prompt_templates.md (8 templates: NL director planner, mini JSON
decision node, large ADRG graph planner, YAML+JSON / XML+JSON / YAML+XML
compiler prompts, NL target compiler, validator repair), reasoning_policy.yaml
(3 profiles with exact budgets + 6 operator rules + 5 hard policies),
dual_format_patterns.md (3 valid + 1 invalid dual authority).

**Tests:** retrieval_queries.json (q001–q005 mapping queries → expected
concepts/operators/terms). **Integration:** REPO_INTEGRATION_PLAN.md
(6-step staged rollout, 8 verification checkpoints), CONCEPT_INDEX_ADDITION.md
(Part ADRG, 6 sections), concept_cards.proposed.jsonl (15 cards, layer tags),
BUILD_GRAPH_EXTENSION.md (6 node kinds, 12 edges). **Scripts:**
build_adrg_rag.py (corpus builder: 1 doc + 35 chunks + 42 sources = 78),
validate_package.py (package integrity checks).

## PASS 2 — Existing-knowledge search

SRC-004 already distilled the closure analysis of this same package family:
decision_record.md (DecisionRecord/Candidate/Consequence schema),
decision_aware_routing.md (5 routing features + operator matrix),
reasoning_budget_router.md (budget vectors), typed_reasoning_graph.md
(department-aware graph 9 node / 14 edge types), director_invariant.md
(3 tiers, axes, deltas), format_ownership.md (ownership table + structured
output caution), cross_format_compiler_reference.md (representation roles,
14-pass YAML→JSON, 14-item checklist), capability_classes_and_loss_records.md
(8 realization statuses, loss taxonomy, decision linkage), repair_strategy.md
(bounded repair + JSON Patch test op — package §19 repair protocol already
covered), verification_layers.md (4-level separation + 11 planner metrics),
adrg_experiments.md (E-ADRG-001..006, F1–F14, B0–B3), evidence_two_axis_model.md
(ADRG evidence classes).

**Major gaps found:**
1. Decision-ledger doctrine (3 risks of raw CoT, retention rules) — schema exists, doctrine does not
2. Reasoning router weighted formula D + branch admission (5) + early pruning (6) + 100-unit budget ledger — features exist, formula/rules do not
3. Model-scaled policy profiles (mini/standard/large with exact budgets) + escalation record + teacher-student distillation — not in tree
4. ADRG graph schema v1.0 (5 planes, 18 nodes, 42 edges, 8 constraints, status vocabulary, 11 phases) — tree has the smaller SRC-006 department graph only
5. Variant lattice (incompatibilities, maximum_simultaneous_deltas, J(S) diversity selection, prompt-vs-shot optimization) — invariants/axes exist, lattice rules do not
6. Graph-aware RAG bundle (bundle-not-chunk, 12 object types, 10-step pipeline, R(o|q), expansion bounds, coverage contract) — not in tree
7. Per-format contracts (NL director-language pattern, YAML safety rules, JSON validation levels, XML envelope/security) — ownership table exists, contract details do not
8. Polyglot compiler (15 cross-format passes, one-authority rule, dual-format patterns) — 14-pass YAML→JSON exists, cross-format passes do not
9. Compile-loss ledger JSON + verifier checkpoints A–I + 3-role separation — 8 statuses exist, ledger/checkpoints do not
10. Package experimental program (7 RQs, factors, causal discipline, ADRG-PKG-E1..E5) — tree has SRC-004's E-ADRG-001..006 (different experiments; collision documented)

## PASS 3 — Semantic map

3 new objects:
- `model_scaled_reasoning_policy` — mini/standard/large profiles (top_k 4/6/10, branch 2×1/3×2/5×3, repairs 1/2/2, specialist critics, self-consistency), escalation record, teacher-student distillation, variant counts by model class
- `adrg_reasoning_graph_schema` — G_R definition, input/output contracts, 11 phases, 5 planes + 6 cross-plane invariants, 18 node types + status vocabulary, ~42 edge types + 8 constraints, worked example (mini policy A–G)
- `graph_aware_rag_bundle` — bundle-not-chunk, 12 retrieval object types, 10-step hybrid pipeline, R(o|q) formula, graph expansion bounds (depth 2 / 24 nodes), context packing order, coverage contract

## PASS 4 — Numerical/formal map

Router: D = w_I·I + w_U·U + w_C·C + w_R·R − w_V·V (weights default, not law).
Budgets: mini top_k 4 / graph_depth 1 / branch 2×1 / repairs 1 / intrinsic
critique 0; standard top_k 6 / depth 2 / 3×2 / repairs 2 / intrinsic 1;
large top_k 10 / depth 2 / 5×3 / repairs 2 / specialist critics 4 /
self-consistency on high-impact ambiguous. Variant counts: mini 1+1,
standard 3 / 2 deltas, large 4–8 → 2–4. maximum_simultaneous_deltas 2.
Diversity J(S) = mean pairwise semantic delta (not wording). Graph expansion
bounds: depth 2, max 24 nodes. Reasoning budget ledger: 100 units.
Realization statuses: 8 (native_exact … unsupported_error). Edge constraints:
8 (selected_over requires decision_id; compiled_to requires
target_adapter + realization_status; depends_on acyclic; etc.). Node types 18;
edge types ~42; planes 5; phases 11 (Phase 0–10); checkpoints A–I (9);
concept cards 15; operator rules 6; hard policies 5; RQ count 7; promotion
criteria 5 (package) vs 6 (SRC-004); planner metrics 11 (already in tree).

## PASS 5 — Representation/compiler map

Package §13–17 formalizes per-format contracts and the polyglot compiler:
NL owns intent/audience effect/observable behavior (director-language pattern
with 6 bracketed clause classes); YAML owns authoring/policy/profiles/imports/
variants/invariants (9 safety rules); JSON owns canonical resolved data
(2020-12 schema, 4 validation levels: parse/schema/semantic/cross-field;
constrained generation 5 rules); XML owns ordered narrative + namespaced
events (urn:cpcs:adrg:1.0, urn:cpcs:core:1.1, perf/cam namespaces); JSONL
owns append-only evidence. One authority per semantic path; dual-format
patterns (YAML+JSON, XML+JSON, YAML+XML) valid only with typed ownership;
embedded duplicate authority rejected. Direct multi-format prompting =
text_interpretation_only (matches structured_prompting_architecture Mode A).
15 cross-format compile passes extend the existing 14-pass YAML→JSON
reference. Compile-loss ledger per canonical control × adapter with
8 realization statuses (already in tree via SRC-004 §22) + decision_id
linkage (already present) + checkpoints A–I + bounded repair (JSON Patch,
test op first — already in repair_strategy.md).

## PASS 6 — Interface map

New cards interface with: typed_reasoning_graph (department graph vs ADRG
execution graph — relationship documented), decision_record, decision_aware_routing,
reasoning_budget_router, director_invariant, format_ownership,
cross_format_compiler_reference, capability_classes_and_loss_records,
repair_strategy, verification_layers, adrg_experiments, agent_retrieval_contract,
rag_ingestion_architecture, structured_prompting_architecture,
evidence_two_axis_model, director_decision_procedure, agent_prompt_contracts.

## PASS 7 — Contradiction scan

- **E-ADRG naming collision:** package §21 E-ADRG-001..005 ≠ SRC-004
  E-ADRG-001..006. Package: E1 mini fixed graph vs one-shot; E2 decision
  ledger vs verbose rationale; E3 dense vs graph-bundle retrieval; E4
  dual-format semantic ownership; E5 selective ToT camera. SRC-004: E1
  Decision IR; E2 router features; E3 state contraction; E4 selective ToT;
  E5 failure-directed repair; E6 carrier effect. Partial correspondence:
  PKG-E5 ↔ tree E-ADRG-004 (ToT); PKG-E4 ↔ tree E-ADRG-006 (carrier).
  Resolution: tree keeps E-ADRG-001..006; package experiments registered as
  ADRG-PKG-E1..E5 with mapping table in adrg_experiments.md EXTEND.
- **Evidence-label vocabulary:** package RAG schema uses 6 labels
  (ESTABLISHED/EMERGING/PROPOSED/OPERATIONALIZATION/PROJECT-OBSERVED/CAUTION);
  tree's evidence_two_axis_model ADRG section uses SRC-004's 5 classes
  (PACKAGE_ESTABLISHED/REPO_OBSERVED/EXTERNAL_ESTABLISHED/PROPOSED_CPCS/
  EXPERIMENTAL). Related but not identical; noted in gaps, no tree change.
- **Weighted router vs budget vectors:** package §10 weighted scalar D vs
  reasoning_budget_router.md "do not begin with a universal weighted scalar"
  (SRC-006 §4.7). Consistent reading: D is a routing default for operator
  selection; budget ledger (100 units) remains a vector record. Documented
  in decision_aware_routing EXTEND.
- **Repair protocol:** package §19 bounded repair (smallest valid change,
  test op first, empty patch → needs_escalation) matches repair_strategy.md
  (SRC-004 §15) — consistent, no new card.
- **No contradictions** between package and SRC-004 closure on the boundary
  rule: ADRG feeds the existing compiler, never replaces it (SRC-004 §21;
  package §5/§20).

## PASS 8 — Placement decisions

3 CREATEs: runtime/04_synthesis/model_scaled_reasoning_policy.md,
runtime/04_synthesis/adrg_reasoning_graph_schema.md,
runtime/03_retrieval/graph_aware_rag_bundle.md. 7 EXTENDs:
decision_record, decision_aware_routing, director_invariant, format_ownership,
cross_format_compiler_reference, capability_classes_and_loss_records,
adrg_experiments. No REUSE/MERGE/SPECIALIZE beyond the above.

## PASS 9 — Dedup audit

- adrg_reasoning_graph_schema vs typed_reasoning_graph.md: SRC-006 graph is
  the department-view aggregation graph (9/14 types); the package schema is
  the ADRG execution-graph control-plane schema (18/42) with a concrete JSON
  Schema artifact. Distinct artifacts; cross-referenced, SRC-004 boundary
  (no second graph authority) preserved.
- model_scaled_reasoning_policy vs reasoning_budget_router.md: budget router
  is resource vectors; model-scaled policy is per-model-class reasoning
  profiles. Complementary layers; interfaced.
- graph_aware_rag_bundle vs agent_retrieval_contract / rag_ingestion_architecture:
  the former is the ADRG graph-expansion retrieval procedure; the latter are
  the paper's record schemas and ingestion. Complementary; interfaced.
- format_ownership EXTEND vs cross_format_compiler_reference EXTEND:
  ownership card gets per-format contracts (NL/YAML/JSON/XML); compiler card
  gets cross-format passes and dual-format patterns. No overlap between the
  two EXTEND sections.
- adrg_experiments EXTEND vs existing E-ADRG-001..006: package program
  registered under ADRG-PKG-E1..E5; both tables kept distinct with mapping.

## PASS 10 — Operationalization

All profiles, thresholds, admission/pruning conditions, ledger fields, edge
constraints, RAG pipeline steps, and checkpoints are enumerable and testable.
The package ships validate_package.py and retrieval_queries.json (q001–q005
with expected concepts/operators/terms). canonical_reasoning_graph.json is a
valid instance of CPCS_ADRG_Reasoning_Graph_Schema.json. The 100-unit budget
ledger, J(S) diversity, and R(o|q) are computable formulas with declared
inputs.

## PASS 11 — Coverage audit

All 22 source units dispositioned: U01 → ledger/identity/gaps; U02, U05–U08,
U18 → CREATE adrg_reasoning_graph_schema; U03, U10 → EXTEND
decision_aware_routing; U04 → EXTEND decision_record; U09 → CREATE
model_scaled_reasoning_policy; U11 → EXTEND director_invariant; U12 → CREATE
graph_aware_rag_bundle; U13–U16 → EXTEND format_ownership; U17 → EXTEND
cross_format_compiler_reference; U19 → EXTEND capability_classes_and_loss_records;
U20, U22 → DIST ledger + gaps; U21 → EXTEND adrg_experiments.

## Objects written

- `cpcs/research/source_registry/identities/SRC-011_cpcs_adrg_research_package_v1.md`
- `cpcs/research/distillation/ledger/11_cpcs_adrg_research_package_v1.md`
- `cpcs/research/gaps/src011_open_research_questions.md`
- `cpcs/runtime/04_synthesis/model_scaled_reasoning_policy.md`
- `cpcs/runtime/04_synthesis/adrg_reasoning_graph_schema.md`
- `cpcs/runtime/03_retrieval/graph_aware_rag_bundle.md`
- EXTEND: `cpcs/runtime/04_synthesis/decision_record.md`
- EXTEND: `cpcs/runtime/04_synthesis/decision_aware_routing.md`
- EXTEND: `cpcs/runtime/05_strategy/constraints/director_invariant.md`
- EXTEND: `cpcs/runtime/07_compiler/format_ownership.md`
- EXTEND: `cpcs/runtime/07_compiler/cross_format_compiler_reference.md`
- EXTEND: `cpcs/runtime/07_compiler/semantic_mapping/capability_classes_and_loss_records.md`
- EXTEND: `cpcs/research/sources/experiments/adrg_experiments.md`
