---
id: SRC-008
title: CPCS-MX Hierarchical Motion Grammar Research Package v1.0
version: 1.0
epistemic_class: authored
status: COMPLETE
lines: 11000
file: research - Copy/CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0/
kind: vocabulary
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-008 — CPCS-MX Hierarchical Motion Grammar Research Package v1.0

- **Package:** `CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0`
- **Date:** 2026-07-19
- **Relationship:** Frozen implementation package for SRC-005 (the research paper). The
  paper was distilled as SRC-005 (28 units, 14 new cards + 6 EXTENDs). This package
  provides the concrete schemas, compiler, scripts, profiles, prompts, references, and
  worked examples that operationalize the paper's proposals.

## Source identity

A frozen research artifact containing 50+ files across schemas, scripts, profiles,
examples, prompts, references, RAG corpus, and documentation. The paper inside the
package (3,241 lines) is identical to SRC-005. Everything else is new evidence.

## Source units

| Unit | Component | Lines | Distilled to |
| --- | --- | --- | --- |
| U01 | `schemas/CPCS_MX_Schema.json` | 1,610 | EXTEND canonical_schema_design |
| U02 | `schemas/CPCS_MX_Authoring_Schema.json` | 164 | EXTEND canonical_schema_design |
| U03 | `schemas/CPCS_MX_Observation_Record_Schema.json` | 146 | CREATE observation_record_contract |
| U04 | `schemas/CPCS_MX_RAG_Record_Schema.json` | 108 | EXTEND rag_ingestion_architecture |
| U05 | `scripts/compile_authoring_yaml.py` | 437 | CREATE mx_compiler_implementation |
| U06 | `scripts/validate_cpcs_mx_package.py` | 311 | CREATE mx_compiler_implementation |
| U07 | `scripts/build_cpcs_mx_rag.py` | 293 | EXTEND rag_ingestion_architecture |
| U08 | `scripts/merge_cpcs_mx_observations.py` | 119 | CREATE observation_record_contract |
| U09 | `scripts/validate_jsonl_stream.py` | 98 | CREATE observation_record_contract |
| U10 | `docs/SCHEMA_FIELD_GUIDE.md` | 109 | EXTEND canonical_schema_design |
| U11 | `docs/AGENT_INGESTION_GUIDE.md` | 190 | EXTEND rag_ingestion_architecture |
| U12 | `docs/AGENT_WORKFLOW_RECIPES.md` | 405 | CREATE mx_workflow_recipes |
| U13 | `docs/IMPLEMENTATION_ROADMAP.md` | 156 | CREATE mx_implementation_roadmap |
| U14 | `docs/PACKAGE_STRUCTURE.md` | 95 | registration reference |
| U15 | `prompts/TEXT_TO_CPCS_MX_AGENT_PROMPT.md` | 97 | CREATE agent_prompt_contracts |
| U16 | `prompts/CPCS_MX_VERIFIER_AGENT_PROMPT.md` | 64 | CREATE agent_prompt_contracts |
| U17 | `prompts/CPCS_MX_STYLE_TRANSFER_AGENT_PROMPT.md` | 43 | CREATE agent_prompt_contracts |
| U18 | `prompts/cpcs_mx_agent_request.xml` | 20 | CREATE agent_prompt_contracts |
| U19 | `profiles/` (8 YAML files) | 120 | CREATE mx_profile_system |
| U20 | `examples/` (4 YAML + canonical JSON + cross-style) | 1,300 | CREATE mx_profile_system, mx_workflow_recipes |
| U21 | `examples/compiled/` (4 compiled JSONs + 4 reports) | 2,531 | CREATE mx_compiler_implementation |
| U22 | `examples/observations/` (4 JSONL/JSON) | 50 | CREATE observation_record_contract |
| U23 | `references/CPCS_MX_Reference_Index.json` | 1,850 | registration reference |
| U24 | `references/CPCS_MX_Source_Annotations.jsonl` | — | registration reference |
| U25 | `rag/CPCS_MX_RAG_Corpus.jsonl` | — | EXTEND rag_ingestion_architecture |
| U26 | `manifests/CPCS_MX_Package_Manifest.json` | 38 | registration reference |
| U27 | `README.md` | 215 | registration reference |
| U28 | `NOTICE.md`, `CHANGELOG.md`, `SHA256SUMS.txt` | 94 | registration reference |

## Self-declared limitations

- The reference compiler intentionally does **not** synthesize dense skeletal motion.
  It resolves profiles, merges, normalizes, and validates — but does not generate
  animation.
- All examples are fictional synthetic data, not motion capture.
- Package schemas are proposed engineering conventions, not international standards.
- Provider capabilities referenced in compiled reports are placeholders.

## Distilled object count

6 new cards + 4 EXTENDs + 1 gaps file + DIST-008 ledger.
