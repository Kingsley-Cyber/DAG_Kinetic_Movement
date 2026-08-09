---
id: SRC-011
title: CPCS ADRG Research Package v1.0 (paper + schemas + examples)
version: 1.0
epistemic_class: research_package
status: COMPLETE
lines: paper 2611 (24 sections) + 21 package files
file: research/continue_detail/CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0/CPCS_Adaptive_Director_Reasoning_Graph_Research_Package_v1.0/
kind: research_package
epistemic_status: PACKAGE_ESTABLISHED
acquisition: authored
sources: [SRC-011]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-011 — CPCS ADRG Research Package v1.0

## Source identity

The **Adaptive Director Reasoning Graph (ADRG) Research Package v1.0** — the
primary research package behind SRC-004's gap closure (SRC-004 listed it as
U01). Document id `CPCS-ADRG-RP-2026-01`, dated 2026-07-23, 22 files:
paper (2611 lines, 24 sections), 3 JSON schemas, RAG corpus (78 records:
1 document + 35 paper chunks + 42 external sources), 8 example files,
3 integration files, 2 scripts, tests, manifests, SHA256SUMS.

The paper defines a **model-scaled reasoning control plane** above the CPCS
compiler (ASL → CIR → TEP → VER): a typed directed multigraph
\(G_R = (V_R, E_R, P, B, A)\) whose nodes are goals/questions/candidates/
decisions/validators and whose edges are typed reasoning, scene, compilation,
and validation relations. Its primary design decision: **no raw chain-of-thought
as canonical artifact** — replace it with a decision ledger.

References [S001]–[S042]: 35 external primary sources (CoT, Self-Consistency,
Least-to-Most, ToT, GoT, ReAct, Self-Refine, PAL, Chain-of-Draft, RAG papers,
JSON Schema 2020-12, RFC 6901/6902, PROV, XML/YAML specs) + 7 repo documents
(AGENTS.md, concepts.jsonl, build_graph.py, CONTROL_SURFACE.md,
FORMAT_CONTROL_MAP.md, CPCS paper v1.2 [S041], lab AGENTS.md [S042]).

## Source structure (single paper, 24 sections)

§1 Executive thesis (5 principles) · §2 Repository baseline · §3 Reasoning
methods as operators · §4 Raw CoT not production artifact (decision ledger) ·
§5 ADRG architecture (input/output contracts, 11 phases) · §6 Five graph
planes + 6 cross-plane invariants · §7 Typed node ontology (18 types, status
vocabulary) · §8 Typed edge ontology (~42 edges, 8 constraints) · §9
Model-scaled policy (mini/standard/large) · §10 Reasoning router (weighted
score, branch admission, pruning, 100-unit budget ledger) · §11 Variant
lattice · §12 Graph-aware RAG (bundle retrieval, 10-step pipeline) · §13 NL
contract · §14 YAML contract · §15 JSON contract · §16 XML contract · §17
Polyglot compiler (15 cross-format passes) · §18 Worked example (6s shot) ·
§19 Compiler/verifier (checkpoints A–I, bounded repair) · §20 Repo
integration · §21 Experimental program (E-ADRG-001..005) · §22 Security and
limitations · §23 Implementation blueprint · §24 Conclusion.

## Source units

| Unit | Component | Distilled to |
| --- | --- | --- |
| U01 | README.md + package_manifest.json + manifests/rag_manifest.json | DIST ledger, identity, gaps |
| U02 | paper §1–2 (thesis, 5 principles, ASL→CIR→TEP→VER baseline) | CREATE adrg_reasoning_graph_schema |
| U03 | paper §3 (reasoning methods as operators) | EXTEND decision_aware_routing |
| U04 | paper §4 (decision ledger, 3 CoT risks) | EXTEND decision_record |
| U05 | paper §5 (G_R, input/output contracts, 11 phases) | CREATE adrg_reasoning_graph_schema |
| U06 | paper §6 (five planes, 6 cross-plane invariants) | CREATE adrg_reasoning_graph_schema |
| U07 | paper §7 (18 node types, status vocabulary) | CREATE adrg_reasoning_graph_schema |
| U08 | paper §8 (~42 edge types, 8 constraints) | CREATE adrg_reasoning_graph_schema |
| U09 | paper §9 (model-scaled policy, escalation record) | CREATE model_scaled_reasoning_policy |
| U10 | paper §10 (router D, admission, pruning, budget ledger) | EXTEND decision_aware_routing |
| U11 | paper §11 (variant lattice, J(S), simultaneous deltas) | EXTEND director_invariant |
| U12 | paper §12 (graph-aware RAG bundle) | CREATE graph_aware_rag_bundle |
| U13 | paper §13 (NL contract, director-language pattern) | EXTEND format_ownership |
| U14 | paper §14 (YAML contract, 9 safety rules) | EXTEND format_ownership |
| U15 | paper §15 (JSON contract, 4 validation levels) | EXTEND format_ownership |
| U16 | paper §16 (XML contract, namespaces, security) | EXTEND format_ownership |
| U17 | paper §17 (polyglot compiler, 15 passes) | EXTEND cross_format_compiler_reference |
| U18 | paper §18 (worked example, mini policy A–G) | CREATE adrg_reasoning_graph_schema |
| U19 | paper §19 (verifier, checkpoints A–I, repair, loss ledger) | EXTEND capability_classes_and_loss_records |
| U20 | paper §20 (repo integration, 6 node kinds, 12 edges) | DIST ledger, gaps |
| U21 | paper §21 (experimental program, E-ADRG-001..005) | EXTEND adrg_experiments |
| U22 | paper §22–24 (security, blueprint, conclusion) + schemas + examples + tests + scripts + references + RAG corpus | DIST ledger, gaps |

## Self-declared limitations

- **Evidence boundary:** engineering defaults (profiles, thresholds, budgets)
  are "proposed defaults" that "cannot be verified with 100% certainty until
  the supplied experiments are run" (README). All policies remain
  `unexplored` until E-ADRG experiments are executed.
- 6 evidence labels (ESTABLISHED, EMERGING, PROPOSED, OPERATIONALIZATION,
  PROJECT-OBSERVED, CAUTION) are attached per record in the RAG corpus.
- Routing features are proposed operational variables, not universal
  scientific scales; the weighted router formula is a default, not a law.
- Small-model limits, self-critique limits, graph complexity costs, and
  creative homogenization risks are CAUTION-grade claims.
- The package's E-ADRG-001..005 names collide with SRC-004's E-ADRG-001..006
  (different experiments); this ledger renames package experiments
  ADRG-PKG-E1..E5 and documents the mapping.

## Distilled object count

3 new cards + 7 EXTENDs + 1 gaps file + DIST-011 ledger + source identity
registration + sync.
