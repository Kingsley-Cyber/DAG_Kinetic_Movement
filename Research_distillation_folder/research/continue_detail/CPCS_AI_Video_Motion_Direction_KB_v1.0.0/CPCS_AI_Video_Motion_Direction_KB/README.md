# CPCS AI Video Motion Direction Knowledge Base

**Package version:** `1.0.0`  
**Research snapshot:** `2026-07-30`  
**Validation as-of date:** `2026-07-31`

This repository is a research and implementation seed for the **Canonical Prompt Control System (CPCS)**: a capability-aware intermediate representation that compiles creative intent into structured motion direction, model-specific prompts, references, and validation criteria.

## What is included

- Fourteen standalone research notes and fourteen machine-readable topic references.
- Complete BESS-oriented Laban layer, Bartenieff connectivity, phase grammar, public FACS reference, kinematics, intent, interaction, force, camera, rhythm, VAD, style transfer, computational-Laban survey, and current AI-video control snapshots.
- A three-tier graph design: **Curated**, **Immutable**, and **Derived**.
- Ten JSON Schemas for canonical scenes, actors, phases, motion primitives, affect, FACS, interactions, camera, experiments, and model adapters.
- Five end-to-end examples in YAML, canonical JSON, XML beat ordering, prose/model prompt compilation, and expected checks.
- Eight dated adapter snapshots for Veo, Kling, Runway, Luma, Adobe Firefly, and legacy Sora.
- Source registry, claim records, evidence matrix, contradictions, known gaps, source-quality notes, and graph-ingestion seed.
- Offline validation, example-compilation, and Neo4j-export scripts.

## Repository map

| Path | Purpose |
|---|---|
| `00_scope/` | Mission, methodology, evidence classes, corrections, terminology |
| `01_topics/` | Fourteen Markdown research notes and paired JSON references |
| `02_canonical_model/` | Layer stack, ontology, vocabulary, mappings, units, graph tiers |
| `03_schemas/` | Draft 2020-12 JSON Schemas |
| `04_pipeline/` | Ingestion, extraction, compiler, adapters, validation, experiments, retrieval |
| `05_examples/` | Five cross-format canonical scenes |
| `06_evidence/` | Sources, claims, evidence matrix, contradictions, gaps, search record |
| `07_prompts/` | Extraction, normalization, planning, compilation, critique prompts |
| `08_evaluation/` | Benchmarks, metrics, acceptance criteria, annotation protocol, test cases |
| `09_source_notes/` | Topic-specific source and locator notes |
| `10_scripts/` | Offline validation, compiler demonstration, graph exporter |
| `11_graph_seed/` | Entities, relations, concepts, Neo4j ingestion guidance |
| `12_adapters/` | Dated vendor capability snapshots |

## Start here

1. Read `00_scope/corrections_and_scope_gaps.md` before treating any normalized value as a standard.
2. Read `02_canonical_model/layer_stack.md` and `04_pipeline/architecture.md` for system design.
3. Inspect `05_examples/01_cross_punch/canonical.json` as the most complete scene record.
4. Run the validator:

```bash
python 10_scripts/validate_package.py --root . --as-of 2026-07-31
```

Success is observable when the command exits `0` and `validation_report.json` reports zero errors.

## Non-negotiable research boundaries

- The seven-phase action sequence is a **CPCS synthesis**, not a universally recognized scientific standard.
- Bartenieff's Basic Six exercises and the Six Patterns of Total Body Connectivity are different taxonomies.
- FACS codes visible facial movement; it does not prove emotion, deception, or intent.
- Video-derived kinematics do not uniquely determine physical force.
- Intent, emotion, and culture mappings are probabilistic priors and require contextual evaluation.
- Vendor controls are dated snapshots. An adapter must be re-probed when its TTL expires or its model/version changes.
- Proprietary FACS manual scoring rules and restricted VAD lexicons are cited, not redistributed.

## Recommended local deployment

- Git: curated definitions, schemas, prompts, adapter snapshots.
- MongoDB: source notes, documents, immutable experiment metadata.
- Neo4j: concepts, claims, mappings, evidence, dependencies.
- Qdrant: searchable summaries, claims, examples, failed-experiment representations.
- Object storage: source snapshots permitted by license, videos, frames, pose tracks, evaluation assets.
- Redis/queue: extraction, compilation, generation, and evaluation jobs.

The architecture is described in `04_pipeline/architecture.md`; store authority and write paths are defined in `02_canonical_model/graph_tiers.md`.
