# Extraction and Normalization Pipeline

## Principle

Use deterministic parsing and schemas first; use language models for bounded extraction and synthesis with evidence spans. The extractor may propose a claim but cannot silently promote it.

## Stages

### 1. Structural extraction

Parse title, headings, paragraphs, lists, tables, equations, captions, references, and page/section locators. Preserve order and parent hierarchy.

### 2. Candidate concepts

Run controlled-vocabulary matching, NER, and relation candidates for LMA, FACS, biomechanics, camera, emotion, datasets, models, and software. Keep the literal source term and normalized candidate.

### 3. Claim extraction

Require a strict record:

```json
{
  "claim_text": "...",
  "claim_type": "MEASUREMENT",
  "subject": "trained_boxer_straight_punch",
  "predicate": "has_reported_fist_speed",
  "object": {"range": [7,12], "unit": "m/s"},
  "evidence_quote": "short allowed span",
  "locator": "Results/Table ...",
  "scope": {"population": "...", "protocol": "..."},
  "confidence": 0.82
}
```

### 4. Validation

Pydantic/JSON Schema validation, unit checking, source-locator existence, numeric-range sanity, and contradiction search. Invalid records enter a review queue.

### 5. Ontology alignment

Resolve source concepts to canonical entities. Use `SAME_AS` only for genuine equivalence; prefer `RELATED_TO`, `NARROWER_THAN`, `SOURCE_TERM_FOR`, or `APPROXIMATES` when meanings differ.

### 6. Human review

Reviewer accepts, revises, rejects, or marks uncertain. The original proposal and decision remain auditable.

## Avoided shortcuts

- no force value inferred from “strong”;
- no emotion inferred as fact from an AU combination;
- no universal timing rule extracted from one animation guide;
- no current model capability copied from an aggregator when official documentation exists;
- no automatic merge of Bartenieff Basic Six and connectivity patterns.

## Batch behavior

Run source parsing and candidate extraction in parallel. Keep source-local writes independent, then perform global entity resolution and contradiction analysis in a second pass. This prevents one failed document from blocking the corpus and supports reproducible reprocessing by source hash.
