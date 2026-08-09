---
id: SRC-009
title: CPCS FACS/Laban Directorial Control Paper v1.2, Pegasus Atomic Video Deconstruction v1.0, Video-to-CPCS Extraction Guide v1.2
version: 1.2
epistemic_class: authored
status: COMPLETE
lines: 12891
file: research/continue_detail/ai-video-movement-prompt-system - Copy/ai-video-movement-prompt-system - Copy/research/
kind: vocabulary
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-009 — CPCS Directorial Control Paper v1.2 + Pegasus Paper + Extraction Guide

- **Package:** `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2` + `Pegasus_Atomic_Video_Deconstruction_and_Modular_AI_Recreation_v1.0`
- **Date:** 2026-07-18
- **Relationship:** These three documents + the v1.2 operational package massively expand the CPCS framework distilled in SRC-001 through SRC-008. The paper (8,731 lines) is the definitive CPCS reference with 31 sections + appendices A-H and 90 bibliography sources. The Pegasus paper (2,782 lines) provides the fight-analysis and information-transfer companion. The extraction guide (1,378 lines) operationalizes reference-video distillation.

## Source identity

Three major research documents plus a v1.2 operational package (33 files: configs, schemas, scripts, prompts, RAG corpus, reference indexes, examples, manifests). Together they define the complete CPCS framework: structured prompting, compiler architecture, reference-video distillation, and reverse directorial compilation.

## Source units

| Unit | Component | Lines | Distilled to |
| --- | --- | --- | --- |
| U01 | CPCS paper §1-17 (foundations through conditioning) | ~2,400 | Already in SRC-001–SRC-005 cards; EXTEND where gaps found |
| U02 | CPCS paper §18 (schema design + worked YAML) | ~100 | EXTEND canonical_schema_design |
| U03 | CPCS paper §19 (structured prompting, ~1,900 lines) | ~1,900 | CREATE structured_prompting_architecture, CREATE capability_negotiation_protocol, CREATE typed_merge_algebra, CREATE backend_adapter_pattern |
| U04 | CPCS paper §20-23 (worked examples) | ~800 | CREATE worked_example_registry |
| U05 | CPCS paper §24 (evaluation framework) | ~400 | CREATE evaluation_framework |
| U06 | CPCS paper §25 (experimental program) | ~200 | CREATE cpcs_experimental_program |
| U07 | CPCS paper §26 (failure modes) | ~300 | EXTEND failure taxonomy |
| U08 | CPCS paper §27-29 (ethics, limitations, future) | ~400 | CREATE cpcs_ethics_and_governance, CREATE cpcs_research_agenda |
| U09 | CPCS paper §30 (reference-video distillation) | ~1,200 | CREATE reference_video_distillation, CREATE video_observation_graph |
| U10 | CPCS paper appendices A-H | ~930 | EXTEND canonical_schema_design, CREATE cross_format_compiler_reference |
| U11 | CPCS paper full reference list (S01-S92) | ~300 | Registration reference |
| U12 | Pegasus paper Part I-II (foundations) | ~600 | Already in SRC-001–SRC-005; EXTEND combat/action cards |
| U13 | Pegasus paper Part III (fight layers + passes) | ~500 | CREATE pegasus_fight_analysis |
| U14 | Pegasus paper Part IV (information transfer) | ~700 | CREATE information_transfer_protocol |
| U15 | Pegasus paper appendices A-E | ~500 | EXTEND pegasus_fight_analysis |
| U16 | Extraction guide §1-15 (stages 0-8) | ~700 | CREATE extraction_pipeline_stages |
| U17 | Extraction guide §16-30 (stages 9-15, fusion, VOG, workflows) | ~678 | CREATE extraction_pipeline_stages, EXTEND video_observation_graph |
| U18 | `configs/video_to_cpcs_pipeline.yaml` | 262 | CREATE extraction_pipeline_config |
| U19 | `schemas/CPCS_Video_Observation_Graph_Schema.json` | 236 | CREATE video_observation_graph |
| U20 | `schemas/CPCS_Video_Observation_Record_Schema.json` | ~200 | EXTEND observation_record_contract |
| U21 | `schemas/CPCS_Video_Extraction_Record_Schema.json` | ~400 | CREATE extraction_record_contract |
| U22 | `schemas/CPCS_RAG_Record_Schema.json` | ~100 | EXTEND rag_ingestion_architecture |
| U23 | `scripts/video_to_cpcs_reference_pipeline.py` | 859 | CREATE extraction_pipeline_scripts |
| U24 | `scripts/extract_video_manifest.py` | 398 | CREATE extraction_pipeline_scripts |
| U25 | `scripts/merge_video_observations.py` | 227 | CREATE extraction_pipeline_scripts |
| U26 | `scripts/validate_video_observation_graph.py` | 191 | CREATE extraction_pipeline_scripts |
| U27 | `prompts/` (5 prompt files) | ~600 | CREATE extraction_prompt_templates |
| U28 | `rag/CPCS_RAG_Corpus.jsonl` (179 records) | ~660K chars | EXTEND rag_ingestion_architecture |
| U29 | `examples/source_video_extraction_example.json` | 615 | CREATE extraction_record_contract |
| U30 | `references/` (4 index files) | ~400 | Registration reference |
| U31 | `manifests/` (2 files) | ~100 | Registration reference |

## Self-declared limitations

- The CPCS paper explicitly marks many components as [PROPOSED] — they are not established standards.
- The extraction pipeline scripts are reference implementations, not production systems.
- All examples are synthetic/fictional — no real performer identity or copyrighted material.
- The VOG schema is a draft 2020-12 JSON Schema, not an international standard.
- The paper's evaluation framework (§24) is a proposal, not validated against running systems.
- Capability negotiation examples (Sora 2, Veo, Runway) are based on publicly available API documentation as of July 2026 and may become outdated.
- Sora 2 and the Videos API are marked deprecated with shutdown scheduled for September 24, 2026.

## Distilled object count

12 new cards + 6 EXTENDs + 1 gaps file + DIST-009 ledger + source identity registration.
