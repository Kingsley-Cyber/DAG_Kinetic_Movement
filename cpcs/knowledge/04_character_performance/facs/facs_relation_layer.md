---
id: cpcs.facs.relation_layer
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §5, SRC-002-U03]
primary_route: cpcs/knowledge/04_character_performance/facs/
interfaces: []
---

# FACS Coactivation, Nonadditivity, and Confusion

Three **distinct** relations — must not be collapsed.

## `coactivates_with`

Two AUs observed simultaneously. Says nothing by itself about emotion.

```json
{ "relation": "coactivates_with", "source": "AU6", "target": "AU12", "evidence_class": "observed" }
```

## `nonadditive_with`

The visual appearance of one AU **changes** when another is present. The FACS
literature documents non-additive combinations, so this must remain a distinct
relation.

## `confusable_with`

A **measurement/reliability** relation, not an incompatibility. Published
psychometric work (U03) identifies AU7/AU6 and AU23/AU24 as difficult
distinctions.

```json
{
  "relation": "confusable_with",
  "source": "AU7", "target": "AU6",
  "reason": "subtle lower-lid appearance difference and frequent co-occurrence",
  "evidence_class": "empirical_reliability"
}
```

## Prohibited

Do **not** convert `confusable_with` into `incompatible_with`. Confusion is a
coder/detector limitation; incompatibility is a semantic constraint.
