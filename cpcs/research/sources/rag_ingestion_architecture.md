---
id: cpcs.research.rag_ingestion
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §29]
primary_route: cpcs/research/sources/
secondary_routes:
  - cpcs/runtime/04_synthesis/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.text_compilation
  - cpcs.found.evidence_two_axis_model
---

# Agent Architecture and RAG Ingestion

> **Source:** SRC-005 §29 — "Agent architecture and RAG ingestion"

## Principle

The package supports research and production agents without forcing them to
ingest one enormous document as an undifferentiated context window. The paper,
schema, examples, and sources are separate but cross-linked artifacts.

## Agent roles

| Agent | Responsibility | Prohibited behavior |
| --- | --- | --- |
| Research agent | retrieve theory and source records | invent unsupported standards |
| Director agent | author intent, beats, performance, camera | modify locked measurements silently |
| Motion compiler | map actions to tracks and constraints | infer rights or safety approval |
| Biomechanics reviewer | check kinematic/dynamic feasibility | treat monocular estimates as measured force |
| Laban/performance agent | author qualitative phrasing | redefine Laban concepts through proxies |
| Face agent | construct AU/gaze/breath tracks | infer concealed mental state as fact |
| Style agent | apply typed transforms | violate invariants without report |
| Target adapter | emit model/engine controls | claim unsupported native control |
| Verification agent | re-extract and compare | change acceptance thresholds after seeing results |
| Rights/safety agent | enforce transfer and use policy | provide real-world harmful combat coaching |

## RAG record types

The JSONL corpus uses one object per line. Recommended record types:

```text
document
research_chunk
schema_definition
field_guide
worked_example
source
prompt_template
validation_rule
migration_note
```

Each record contains stable identifiers, heading paths, concepts, evidence
labels, source links, and a content hash.

## Chunking strategy

Chunk boundaries follow semantic sections, not a fixed character count. Long
sections are divided at subheadings with a small context header. Each chunk
should be independently interpretable but retain: document title, section
number and heading path, definition scope, evidence labels, source IDs,
neighboring chunk IDs, and schema fields discussed. Do not split a JSON or
YAML example across records.

## Retrieval strategy

Queries combine semantic similarity with metadata filters. An agent should
retrieve source records for claims, field definitions for syntax, and examples
for composition. Retrieving only the nearest prose chunk can omit required units
or safety constraints.

## JSONL parser requirements

1. stream one line at a time
2. ignore blank lines but not malformed nonblank lines
3. report filename and line number
4. validate each object against the record schema
5. reject duplicate `record_id` values unless byte-identical and explicitly deduplicated
6. verify hashes when present
7. quarantine invalid records rather than dropping them silently
8. support compressed input where scale requires it
9. checkpoint offsets for resumable ingestion
10. preserve source order only as metadata, not semantic hierarchy

## Knowledge graph relationships

Records can expose edges:

```text
section DEFINES field
field COMPILES_TO control
example USES field
metric VERIFIES field
source SUPPORTS claim
style_transform PRESERVES invariant
migration REPLACES field
```

This improves retrieval for questions such as "Which metrics verify a
bound-flow staged contact?" or "Which target controls can carry a local wrist
trajectory?"

## Agent output discipline

An agent generating a score should provide: canonical JSON or authoring YAML,
schema-validation result, assumptions and defaults, source IDs for research
claims, unresolved ambiguities, capability coverage report, verification plan,
and safety and rights scope. It should not claim deterministic video output
merely because the score validates. Schema validity establishes structure, not
model compliance.

## RAG freshness and source status

Platform documentation and emerging model interfaces can change. Source records
include retrieval or publication dates and status labels. Agents should prefer
normative standards and peer-reviewed research for stable concepts, and current
official documentation for platform-specific behavior. An adapter based on a
deprecated API should be treated as historical even if its conceptual discussion
remains useful.

## RAG record schema (SRC-008 EXTEND)

The frozen package defines a JSONL RAG record schema
(`CPCS_MX_RAG_Record_Schema.json`, `$id: urn:cpcs-mx:rag-record-schema:1.0`):

### Required fields

| Field | Type | Notes |
| --- | --- | --- |
| `record_id` | string | unique within corpus |
| `record_type` | enum (10 values) | see below |
| `document_id` | string | source document |
| `title` | string | chunk/record title |
| `content` | string | the chunk text |
| `sha256` | hex64 | hash of `content` |

### Record types (10)

`document` · `research_chunk` · `schema_definition` · `field_guide` ·
`worked_example` · `source` · `prompt_template` · `validation_rule` ·
`migration_note` · `package_document`

### Key optional fields

- `heading_path`: array of strings preserving section hierarchy
- `concepts`: unique array of concept tags for retrieval filtering
- `evidence_labels`: unique array (ESTABLISHED, CURRENT_PLATFORM, etc.)
- `source_ids`: array matching `^S[0-9]{3}$` (e.g., S008)
- `schema_fields`: array of field names referenced by the chunk
- `safety_scope`: string
- `context_before` / `context_after`: adjacent text for disambiguation

### Ingestion rules

1. Validate each record against the RAG schema.
2. Require unique `record_id` values.
3. Verify `sha256` against the `content` string.
4. Quarantine malformed records, never silently drop.
5. Retain `record_type` and `evidence_labels` as metadata.
6. Do not use line order as document hierarchy.
7. Do not embed only `content` and discard evidence labels.

### Embedding fields (recommended)

`title` + `heading_path` + `concepts` + `content`

## v1.2 RAG corpus structure (SRC-009 EXTEND)

The v1.2 package provides a 179-record JSONL corpus
(`CPCS_RAG_Corpus.jsonl`) with two record types:

### `document` record

Contains: `document_id`, `document_version`, `title`, `subtitle`,
`date`, `status`, `knowledge_domains` (array), `chunking_config`
(preferred size range, rules).

### `paper_chunk` record

Contains: `record_id`, `record_type`, `document_id`,
`document_version`, `title`, `heading_path` (array of strings),
`text`, `concepts` (unique array), `aliases`, `source_ids`
(matching `^S[0-9]{2,3}[A-Z]?$`), `evidence_labels`
(ESTABLISHED, CURRENT_PLATFORM, CURRENT_RESEARCH, EMERGING, PROPOSED,
OPERATIONALIZATION), `entities`, `applicability`, `limitations`,
`license_tags`, `anchors`, `language`, `word_count`, `content_hash`.

### v1.2 record types (10)

The information transfer protocol defines 10 record types:
`document`, `paper_chunk`, `concept_card`, `movement_atom`,
`performance_template`, `shot_template`, `calibration_profile`,
`source_record`, `failure_record`, `experiment_record`.

This extends the SRC-008 RAG record types with 4 new types:
`concept_card`, `calibration_profile`, `failure_record`,
`experiment_record`.

See `cpcs.runtime.information_transfer_protocol` for the full RAG
type catalog and `cpcs.runtime.cross_format_compiler_reference` for
the RAG evaluation metrics (9 quality dimensions).
