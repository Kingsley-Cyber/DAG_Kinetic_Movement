# Research and Knowledge Ingestion

## Inputs

- primary papers, books, manuals, standards, datasets, and official documentation;
- expert notes with author/credential/context;
- code repositories and release metadata;
- model documentation snapshots and live capability probes;
- project experiments and annotation guidelines.

## Deterministic flow

1. **Register source.** Create a stable `source_id`, title, authors, date, type, URL/DOI, rights, retrieval date, content hash, and authority class.
2. **Acquire content.** Save permitted text/metadata or a citation-only record when redistribution is restricted. Preserve original bytes and hash if legally stored.
3. **Parse structure.** Retain headings, page/section locators, tables, figures, code blocks, and bibliographic references.
4. **Chunk semantically.** Prefer section/subsection boundaries. Keep page/section ranges and parent relationships.
5. **Extract claims.** Separate factual statement, definition, measured result, limitation, and CPCS inference.
6. **Normalize concepts.** Map terms to canonical entities without deleting source wording.
7. **Link evidence.** `Claim —SUPPORTED_BY→ SourceLocator`; contradictions become explicit edges.
8. **Review/promote.** Only reviewed records enter Curated.

## Source record

```json
{
  "source_id": "S024",
  "title": "OpenCap: Human Movement Dynamics from Smartphone Videos",
  "authority": "peer_reviewed",
  "retrieved_at": "2026-07-30T00:00:00Z",
  "rights": "citation_and_summary_only",
  "locators": ["Methods", "Validation", "Limitations"],
  "content_sha256": "..."
}
```

## Claim classes

- `DEFINITION`: source-defined meaning;
- `MEASUREMENT`: observed value and protocol;
- `METHOD`: reproducible procedure;
- `LIMITATION`: boundary/failure condition;
- `RELATION`: association or causal claim;
- `PRACTICE_RULE`: professional convention;
- `CPCS_INFERENCE`: explicit synthesis;
- `PRODUCT_CAPABILITY`: dated official model control.

## Rights and licensing

Do not ingest a proprietary FACS manual or licensed NRC lexicon into a redistributable repository. Store citation, allowed metadata, locators, and internally licensed references. The pipeline must expose `rights` and block downstream export when an asset is restricted.

## Verification checkpoints

- source hash and locator exist;
- author/title/date/DOI match at least one authoritative record;
- extracted numeric claims retain units, sample/protocol, and uncertainty;
- current product claims have `verified_at` and official source;
- unsupported aliases are quarantined, not normalized into real systems;
- every Curated claim has an accountable reviewer.
