---
distillation_id: DIST-008
source_id: SRC-008
status: complete
coverage: full
---

# Distillation Ledger — SRC-008

`CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0` → CPCS knowledge
tree. Distilled 2026-08-09. The paper inside the package is SRC-005 (already
distilled). This ledger covers only the implementation artifacts (schemas,
scripts, profiles, prompts, examples, docs, references).

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-008_cpcs_mx_research_package_v1.md`.
Frozen research package (50+ files, ~11,000 lines across all files). 28 source
units U01–U28. The 3,241-line paper is a duplicate of SRC-005 and was not
re-distilled.

## PASS 1 — Structural map

8 directories: schemas (4 JSON), scripts (5 Python), profiles (8 YAML), examples
(4 YAML + compiled + observations), prompts (4), references (80 sources), rag
(JSONL), docs (5 Markdown). Pipeline: authoring YAML → profile resolution →
deep merge → import verification → candidate compilation → schema validation →
report.

## PASS 2 — Existing-knowledge search

SRC-005 already distilled the paper into 14 cards + 6 EXTENDs. The package
provides concrete implementations of what the paper described. 4 EXTENDs
identified: canonical_schema_design (field catalog), constraint_resolution_compilation
(reference implementation), rag_ingestion_architecture (RAG record schema),
text_to_score_compilation (agent prompt contract). 6 CREATEs for new concepts
that don't exist as cards.

## PASS 3 — Semantic map

6 new objects: `mx_compiler` (reference compiler contract), `agent_prompts`
(4 agent prompt contracts), `mx_workflow_recipes` (10 operational recipes),
`mx_roadmap` (8-phase implementation roadmap), `observation_contract`
(JSONL observation schema), `mx_profiles` (profile URI resolution system).

## PASS 4 — Numerical/formal map

Canonical schema: 20 top-level fields, 4 authority values, 3 constraint
priorities, 3 required fields. Observation schema: 7 evidence classes, 4 review
statuses, anyOf temporal anchoring. RAG schema: 10 record types, sha256
verification. Compiler: 3 append-path suffixes, 6 ID keys, 4 exit codes,
5 import types, deterministic serialization.

## PASS 5 — Representation/compiler map

Deep merge with ID-based list matching; profile URI resolution with path
traversal protection; SHA-256 asset verification; deterministic typed
constraint compilation; evidence class labeling on every extracted value;
unresolved items wrapped in namespaced extension rather than discarded.

## PASS 6 — Interface map

New cards interface with canonical_schema, constraint_compilation,
text_compilation, rag_ingestion, measurement_record_form, interchange_manifests,
anime_sakuga, superhuman_transform, combat_coding, evidence_two_axis_model.

## PASS 7 — Contradiction scan

No contradictions. Observation schema's 7 evidence classes are consistent with
SRC-005 E1 EXTEND to evidence_two_axis_model. RAG record types extend
rag_ingestion_architecture without conflict. Compiler merge rules are a concrete
implementation of constraint_resolution_compilation's abstract description.

## PASS 8 — Placement decisions

6 CREATEs across runtime/06_canonical (3), runtime/07_compiler (1),
runtime/04_synthesis (1), verification (1). 4 EXTENDs (see PASS 2). No
REUSE/MERGE.

## PASS 9 — Dedup audit

mx_compiler vs constraint_resolution_compilation: abstract pipeline description
vs concrete implementation contract — complementary, not duplicative.
observation_contract vs measurement_record_form: raw JSONL evidence schema vs
evaluation form — different layers of the verification stack.
agent_prompts vs rag_ingestion: RAG system design vs operational prompt templates.

## PASS 10 — Operationalization

Compiler exit codes, schema required fields, observation review_status lifecycle,
profile URI scheme, and JSONL validation rules are all testable contracts.
Reference scripts are executable with Python 3.10+, PyYAML, jsonschema.

## PASS 11 — Coverage audit

All 28 source units dispositioned: U01–U09 → cards/EXTENDs; U10–U14 →
EXTENDs/CREATEs; U15–U18 → agent_prompt_contracts; U19–U22 →
mx_profiles/observation_contract; U23–U28 → registration reference.

## Objects written

- `cpcs/research/source_registry/identities/SRC-008_cpcs_mx_research_package_v1.md`
- `cpcs/runtime/06_canonical/mx_compiler_implementation.md`
- `cpcs/runtime/07_compiler/agent_prompt_contracts.md`
- `cpcs/runtime/04_synthesis/mx_workflow_recipes.md`
- `cpcs/runtime/06_canonical/mx_implementation_roadmap.md`
- `cpcs/verification/observation_record_contract.md`
- `cpcs/runtime/06_canonical/mx_profile_system.md`
- `cpcs/research/gaps/src008_open_research_questions.md`
- EXTEND: `cpcs/runtime/06_canonical/canonical_schema_design.md`
- EXTEND: `cpcs/runtime/06_canonical/constraint_resolution_compilation.md`
- EXTEND: `cpcs/research/sources/rag_ingestion_architecture.md`
- EXTEND: `cpcs/runtime/04_synthesis/text_to_score_compilation.md`
