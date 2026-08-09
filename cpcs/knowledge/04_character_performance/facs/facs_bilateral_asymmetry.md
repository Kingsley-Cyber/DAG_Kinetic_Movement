---
id: cpcs.facs.bilateral_asymmetry
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §3.2, SRC-002-U01]
primary_route: cpcs/knowledge/04_character_performance/facs/
secondary_routes:
  - cpcs/knowledge/00_foundations/numerical_representation/
interfaces: []
---

# FACS Bilateral / Asymmetric Representation

Do **not** average left/right AU activation. Cross-ref general doctrine:
`knowledge/00_foundations/numerical_representation/bilateral_side_semantics.md`.

## Side-indexed activation

```json
{
  "au_id": "AU12",
  "activation": {
    "left": { "intensity": "C" },
    "right": { "intensity": "B" },
    "bilateral": false
  },
  "asymmetry": { "kind": "left_dominant", "basis": "ordinal_comparison" }
}
```

## Bilateral equivalent

```json
{
  "au_id": "AU12",
  "activation": {
    "left": { "intensity": "C" },
    "right": { "intensity": "C" },
    "bilateral": true
  }
}
```

## Authority boundary

The exact FACS coding rules for asymmetry remain governed by the licensed
manual; this JSON is a **CPCS representation**, not a reproduction of
proprietary scoring notation.

## Verification

`test_left_right_not_averaged`, `test_bilateral_preserved`.
