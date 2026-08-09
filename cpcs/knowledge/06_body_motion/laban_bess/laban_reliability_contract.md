---
id: cpcs.laban.reliability_contract
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §13, SRC-002-U09]
primary_route: cpcs/knowledge/06_body_motion/laban_bess/
secondary_routes:
  - cpcs/research/numerical/calibration/
interfaces: []
---

# Laban Reliability Contract

The empirical literature supports **reliability testing** rather than assuming
all LMA categories are equally objective. A 2019 CMA-rater study (U09) found
only **weak-to-acceptable** overall reliability; Effort/Shape carry greater
subjective inference than spatially explicit dimensions.

## Recommended metrics

```text
categorical/multi-rater : Krippendorff's alpha
two-coder categorical   : Cohen's kappa
continuous proxy         : ICC · MAE · rank correlation · calibration error
categorical Laban       : per-category precision/recall
```

## Implication

An apparently formal movement vocabulary does **not** automatically imply high
agreement across expert observers. CPCS must attach confidence/reliability
metadata to Laban values and apply confidence-aware compilation rather than
treating authored Laban labels as mechanically objective.

## Verification

`Laban Krippendorff alpha` metric; per-category precision/recall.
