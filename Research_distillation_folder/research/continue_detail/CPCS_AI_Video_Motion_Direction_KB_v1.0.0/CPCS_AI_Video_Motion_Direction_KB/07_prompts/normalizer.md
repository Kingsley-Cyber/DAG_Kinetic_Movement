# Prompt — CPCS Concept Normalizer

Given candidate source concepts and the CPCS ontology, propose mappings without changing the original record.

Output each proposal with:

```json
{
  "source_term": "",
  "canonical_id": "",
  "relation": "SAME_AS|SOURCE_TERM_FOR|NARROWER_THAN|BROADER_THAN|RELATED_TO|APPROXIMATES|CONFLICTS_WITH|UNRESOLVED",
  "confidence": 0.0,
  "rationale": "",
  "required_review": true
}
```

Use `SAME_AS` only for genuine semantic identity. Examples that are **not** same-as: Effort Space versus the Space category; LMA Weight versus physical force; Basic Six versus connectivity patterns; FACS letter intensity versus OpenFace detector score; web UI capability versus API capability.
