---
id: cpcs.found.numeric_scale_calibration
kind: doctrine
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007 G020]
primary_route: cpcs/knowledge/00_foundations/epistemology/
secondary_routes:
  - cpcs/knowledge/00_foundations/
  - cpcs/verification/
interfaces:
  - cpcs.found.evidence_two_axis_model
  - cpcs.found.exactness_taxonomy
  - cpcs.verification.measurement_record_form
---

# Numeric Scale Calibration Doctrine

> **Source:** SRC-007 G020 — "FACS/Laban calibration"

## Principle

Determine exactly which numeric scales are defensible and which must remain
qualitative or project-specific. Every numeric or ordinal field declares:

```text
scale type · anchors · permitted operations · calibration source
rater/instrument · reliability evidence · cross-subject comparability
provider mapping · invalid transformations
```

## Rules

- Do **not** average ordinal categories.
- Do **not** translate between FACS, Laban, and provider controls without an
  evidenced mapping.
- Show behavior when a provider accepts prose but not the canonical numeric
  scale (semantic projection with loss record, never false precision).
- A numeric field without a declared calibration source is a project
  constant, not a measured quantity.

## Scale types

nominal (labels only) · ordinal (ordering, no arithmetic) · interval
(equal steps, arbitrary zero) · ratio (true zero, full arithmetic). The
permitted operations follow from the scale type.

## Verification

`test_no_averaging_of_ordinals`,
`test_facs_laban_provider_translation_requires_evidence`,
`test_prose_only_provider_gets_semantic_loss_record`,
`test_scale_type_declared_per_numeric_field`.
