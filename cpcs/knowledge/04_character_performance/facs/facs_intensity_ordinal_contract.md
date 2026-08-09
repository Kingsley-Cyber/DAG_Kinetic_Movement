---
id: cpcs.facs.intensity_ordinal_contract
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §3.3, §1.2, SRC-002-U01, SRC-002-U03]
primary_route: cpcs/knowledge/04_character_performance/facs/
secondary_routes:
  - cpcs/research/numerical/ordinal_scales/
interfaces: []
---

# FACS Intensity Remains Ordinal

## Canonical ordinal field

```text
A | B | C | D | E
```

is the FACS intensity scale where the underlying observation supports FACS
intensity. It is **ordinal**, not physical force or a universally calibrated
percentage.

## Prohibited

Never define a fixed numeric mapping as physical truth:

```text
A = 0.2  B = 0.4  C = 0.6  D = 0.8  E = 1.0   # FORBIDDEN
```

## Derived control (separate identity)

A project-normalized control may exist but must retain its mapping identity:

```json
{
  "intensity": {
    "value": 0.6,
    "basis": "project_normalized",
    "source_scale": "facs_ordinal",
    "mapping_id": "project:facs_to_control_v1"
  }
}
```

This is a **derived control**, not FACS truth. Cross-subject/cross-camera/
cross-model numeric comparison requires calibration and should not be assumed
(SRC-002 §1.2).

## Verification

`test_facs_intensity_not_numeric_truth`,
`test_project_normalized_intensity_requires_mapping_id`.
