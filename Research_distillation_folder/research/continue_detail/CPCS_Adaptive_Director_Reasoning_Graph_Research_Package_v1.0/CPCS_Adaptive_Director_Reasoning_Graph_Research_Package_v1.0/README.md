# CPCS Adaptive Director Reasoning Graph Research Package v1.0

This package extends the Cinematic Performance Control Score (CPCS) architecture with an **Adaptive Director Reasoning Graph (ADRG)**. ADRG is a model-scaled reasoning control plane for retrieving concepts, decomposing directing problems, selectively exploring treatments, recording auditable decisions, compiling across natural language/YAML/JSON/XML, negotiating target-model capabilities, and validating the result.

## Primary design decision

The package does **not** make raw chain-of-thought text a canonical artifact. It stores typed task, evidence, candidate, decision, compilation, validation, failure, and repair records. This supports auditing and experiments without treating a model-generated explanation as verified causal provenance.

## Package contents

```text
README.md
paper/
  CPCS_Adaptive_Director_Reasoning_Graph_and_Polyglot_Prompt_Compiler.md
rag/
  CPCS_ADRG_RAG_Corpus.jsonl
schemas/
  CPCS_ADRG_RAG_Record_Schema.json
  CPCS_ADRG_Reasoning_Graph_Schema.json
  CPCS_ADRG_Source_Index_Schema.json
references/
  ADRG_Reference_Index.json
examples/
  reasoning_policy.yaml
  director_request.yaml
  director_envelope.xml
  canonical_reasoning_graph.json
  compiled_natural_language_prompt.txt
  dual_format_patterns.md
  planner_prompt_templates.md
tests/
  retrieval_queries.json
integration/
  concept_cards.proposed.jsonl
  CONCEPT_INDEX_ADDITION.md
  BUILD_GRAPH_EXTENSION.md
  REPO_INTEGRATION_PLAN.md
scripts/
  build_adrg_rag.py
  validate_package.py
manifests/
  rag_manifest.json
  package_manifest.json
SHA256SUMS.txt
```

## Main paper

The 14,000-word paper covers:

- CoT, least-to-most, ToT, GoT, ReAct, self-consistency, program-aided reasoning, critique, and concise-reasoning research;
- why those methods should be routed per decision rather than used as one global prompt instruction;
- mini, standard, and large planner policies;
- five graph planes and typed node/edge vocabularies;
- a decision ledger that replaces raw reasoning transcripts;
- a constrained invariant-and-axis variant lattice;
- graph-aware RAG with coverage and conflict reporting;
- natural-language, YAML, JSON, XML, and JSONL ownership contracts;
- dual-format and three-format compiler patterns;
- deterministic validation and compilation-loss reporting;
- a staged integration plan for the target repository;
- an experimental program for causal promotion of reasoning policies.

## RAG corpus

The corpus is generated from explicit `RAG_CHUNK` markers and the structured source index. The current build contains:

- 1 document record;
- 35 paper-chunk records;
- 42 source records;
- 78 total JSONL records.

Each record contains a stable ID, heading path, text, context overlap, concepts, source IDs, evidence labels, anchors, word count, token estimate, and SHA-256 digest.

Rebuild it with:

```bash
python3 scripts/build_adrg_rag.py
```

Observable success is a JSON result with `"status": "ok"`; the corpus and `manifests/rag_manifest.json` are regenerated.

## Validate the package

```bash
python3 scripts/validate_package.py
```

The validator checks:

- Markdown front matter and unique RAG markers;
- source-index schema and unique source IDs;
- YAML, XML, and JSON example parsing;
- reasoning-graph JSON Schema validation;
- graph endpoints, decision references, and dependency acyclicity;
- RAG-record schema, unique record IDs, chunk bounds, and source resolution;
- proposed concept-card structure and unique IDs;
- package manifest and SHA-256 checksums.

Observable success is:

```text
PACKAGE VALIDATION: PASS
```

## Use in a planner

1. Normalize the user request into `examples/director_request.yaml`-style fields.
2. Select a model profile from `examples/reasoning_policy.yaml`.
3. Retrieve concept bundles from the package and repository graph.
4. Emit a schema-valid ADRG graph using `schemas/CPCS_ADRG_Reasoning_Graph_Schema.json`.
5. Compile the selected treatment into CPCS authoring and canonical formats.
6. Record target realization status and loss for every control.
7. Validate before generation, then attach render metrics as evidence.

## Repository integration

The target repository treats research packages as frozen inputs and `lab/graph.json` as derived. Do not edit the existing CPCS v1.2 package or hand-edit the graph. Follow `integration/REPO_INTEGRATION_PLAN.md` and run the repository’s own validation gates before committing.

## Evidence boundary

The research literature supports the component methods, standards, and known limitations. The ADRG directing architecture, routing thresholds, model budgets, variant counts, and graph extensions are proposed engineering defaults. They cannot be verified with 100% certainty for every model or video backend until the supplied experiments are run against the target stack.
