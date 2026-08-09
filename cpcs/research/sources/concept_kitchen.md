---
id: cpcs.lab.concept_kitchen
kind: mechanism
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U07, SRC-010-U08, SRC-010-U09, SRC-010-U15]
primary_route: cpcs/research/sources/
secondary_routes:
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.lab.architecture
  - cpcs.lab.pattern_registry
  - cpcs.research.rag_ingestion_architecture
  - cpcs.evaluation.cpcs_evaluation_framework
---

# Concept Kitchen (semantic retrieval + paper crosswalk)

> **Source:** SRC-010 `lab/concepts.jsonl`, `lab/CONCEPT_INDEX.md`,
> `lab/profiles/`, `lab/scripts/{concepts,build_graph,graph,sync_repo}.py`.
> The lab's retrieval corpus and its bridge to all 3 CPCS papers.

## concepts.jsonl — semantic cards

One card per concept with `nl_triggers`: natural-language phrases that should
surface the concept. Operated by `concepts.py` (query / card / stats /
validate). This is the lab-scale version of the paper's RAG record schema
(`cpcs.research.rag_ingestion_architecture`): same idea, smaller scale,
working today.

## CONCEPT_INDEX.md — paper crosswalk (17 sections)

Every concept from all 3 papers is cataloged and mapped to a lab status:

- **3-paper cross-validation:** concepts independently derived from multiple
  papers are marked as such.
- **Session discoveries ↔ paper crosswalk:** what the authoring session found
  vs what the papers predict.
- **Lab-original findings** (in the lab, not named in the papers):
  anti-AI-skin rule · device-signature realism · 30 fps cadence ·
  < 2000-char prompt packaging · format-as-diversity · owner kinematic detail
  layers.

## Profiles (8)

`natural_human_v3` · `staged_action_base_v2` · `authentic_ugc_v2` ·
`impact_readability_v1` · `observational_medium_wide_v1` · `confident_direct_v1`
· `staged_near_contact_v2` · `anime_sakuga_action_v3`.

All are `production_example` / `safety_scoped_example`: **structurally sound,
not yet lab-render-validated** — the honest bound every profile carries.

## Graph

`build_graph.py` + `graph.py` derive `graph.json` from the corpus (concepts,
blocks, patterns, variants) for dependency/coverage queries. `sync_repo.py`
is the control plane: checks S1–S4 (schema validity, graph consistency,
concept coverage, ledger integrity) gate every promotion.

## Growth protocol (cannibalize flow)

7 steps: spot a one-off prompt that worked → extract the reusable pattern →
promote to a block in `blocks.yaml` → write the concept card with nl_triggers
→ update CONCEPT_INDEX → regenerate the graph → gate with `sync_repo.py`.
Composition fallback: when no block covers a capability, look up
CONCEPT_INDEX first (paper § refs), compose from the paper's definition,
mark unproven, and propose the isolated A/B.

## Boundary

The kitchen is the lab's memory, not its evidence: cards and profiles are
retrieval aids; only patterns with run evidence carry confidence. The
crosswalk maps paper theory → lab status, it does not validate the theory.
