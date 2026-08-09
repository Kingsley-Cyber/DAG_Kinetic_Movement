---
id: SRC-004
title: ADRG Director Reasoning Gap Closure
version: 1.0
epistemic_class: research_closure
status: COMPLETE
lines: 2208
sections: 30
file: Research_distillation_folder/04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE_COMPLETE.md
primary_route: cpcs/research/source_registry/identities/
---

# SRC-004 — ADRG Director Reasoning Gap Closure

## Source identity

A CPCS-internal research closure (v1.0) that investigates whether the Adaptive
Director Reasoning Graph (ADRG) justifies adding a new reasoning/orchestration
framework to CPCS. The source's central finding is negative: **ADRG does not
justify another framework.** The actual gap is a compact, first-class semantic
representation of director decisions — not a missing reasoning method.

The source establishes five concrete additions:

1. DecisionRecord / Candidate / Invariant / Consequence objects.
2. Typed execution edges (21) without polluting the knowledge-graph edge policy.
3. Decision-aware routing features (impact/uncertainty/coupling/irreversibility/
   validator_strength/budget).
4. Explicit active/compressed/source/decision/failure memory with deterministic
   contraction rules.
5. Bounded repair + compile-loss + verification linkage.

## Source structure (single layer, 30 sections)

§0 Executive result · §1 Evidence basis · §2 Gap closure (A–F) · §3 Primary-
source verification · §4 Semantic representation · §5 Decision IR · §6 Decision
graph (21 edges) · §7 Routing · §8 State contraction · §9 Invariants/variant
axes · §10 Causal reasoning contract · §11 Reasoning trace · §12 Research-to-
decision examples · §13 Format/compiler effect · §14 Structured-output caution ·
§15 Failure-directed reasoning · §16 Verification model · §17 Measurement form ·
§18 Implementation placement · §19 Minimal schemas · §20 Canonical ADRG graph ·
§21 Canonical mapping · §22 Compiler semantics · §23 State of implementation ·
§24 Controlled experiments · §25 Promotion rules · §26 Closure matrix · §27
Build packet · §28 Implementation order · §29 Final determination · §30 Primary
sources.

## Source units

| Unit | Source | Evidence class | Key contribution |
| --- | --- | --- | --- |
| U01 | CPCS-ADRG-RP-2026-01, *From Prompt Chains to Director Graphs*, v1.0 | PACKAGE_ESTABLISHED | ADRG research package; reasoning-graph schema, policy examples |
| U02 | CPCS_ADRG_Reasoning_Graph_Schema.json | PACKAGE_ESTABLISHED | JSON Schema for ADRG decision graph |
| U03 | reasoning_policy.yaml | PACKAGE_ESTABLISHED | Reasoning policy definitions |
| U04 | planner_prompt_templates.md | PACKAGE_ESTABLISHED | Prompt templates for planner |
| U05 | REPO_INTEGRATION_PLAN.md | PACKAGE_ESTABLISHED | Repository integration plan |
| U06 | Wei et al., CoT, arXiv:2201.11903 | EXTERNAL_ESTABLISHED | Chain-of-Thought prompting |
| U07 | Wang et al., Self-Consistency, arXiv:2203.11171 | EXTERNAL_ESTABLISHED | Self-consistency sampling |
| U08 | Zhou et al., Least-to-Most, arXiv:2205.10625 | EXTERNAL_ESTABLISHED | Decomposition prompting |
| U09 | Yao et al., Tree-of-Thoughts, arXiv:2305.10601 | EXTERNAL_ESTABLISHED | Deliberate problem solving |
| U10 | Besta et al., Graph-of-Thoughts, arXiv:2308.09687 | EXTERNAL_ESTABLISHED | Graph aggregation |
| U11 | Yao et al., ReAct, arXiv:2210.03629 | EXTERNAL_ESTABLISHED | Reasoning + acting |
| U12 | Madaan et al., Self-Refine, arXiv:2303.17651 | EXTERNAL_ESTABLISHED | Iterative refinement |
| U13 | Turpin et al., Unfaithful CoT, arXiv:2305.04388 | EXTERNAL_ESTABLISHED | CoT explanations ≠ causal basis |
| U14 | W3C PROV / RFC 6901 / RFC 6902 / JSON Schema 2020-12 / YAML 1.2 / XML 1.0 / Ray 2026 (Constraint Tax, arXiv:2605.26128) | EXTERNAL_ESTABLISHED | Standards alignment: provenance, JSON Pointer/Patch, schema, formats, constraint tax |

## Self-declared limitations

- Architecture rule: do NOT create another agent framework, graph database, scene
  ontology, canonical score, provider compiler, or second persistent reasoning
  authority (§18, §29).
- Many representations are CPCS proposals (`PROPOSED_CPCS`), not externally
  established facts.
- Routing features are proposed operational variables, not universal scientific
  scales (§7.1).
- Realization statuses, state contraction thresholds, and format effects require
  controlled experiments (§24, §30).
- No universal claim that any single format or reasoning operator is globally
  superior (§30).

## Distilled objects

12 new canonical owners written + 8 existing owners extended. See DIST-004
ledger at `research/distillation/ledger/04_adrg_director_reasoning_gap_closure.md`.
