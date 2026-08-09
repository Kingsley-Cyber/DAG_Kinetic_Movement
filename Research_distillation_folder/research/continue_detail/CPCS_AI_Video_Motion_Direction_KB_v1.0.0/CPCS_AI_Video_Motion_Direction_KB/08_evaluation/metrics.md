# Metrics

## Human ordinal scores (0–4)

0 absent/wrong; 1 major failure; 2 partial/ambiguous; 3 good with minor errors; 4 fully satisfies observable criterion.

## Automatic metrics

- **Pose/trajectory:** MPJPE/PCK or task-relative trajectory error when reference exists.
- **Contact:** contact precision/recall, onset error, drift, penetration, reaction-order violations.
- **Identity:** face/appearance embedding stability with consent and appropriate model limitations.
- **Camera:** homography/pose/flow fit to reference; shot-size/path error.
- **Rhythm:** beat alignment, phase landmark timing, inter-onset intervals.
- **FACS:** AU agreement only for visible supported AUs with calibrated detector/manual annotations.
- **Style:** style classifier/similarity plus invariant-preservation score.
- **Physics:** foot-skate distance, bone-length variance, joint-limit violations, COM/support proxy.
- **Temporal coherence:** track fragmentation, object/actor identity swaps, flicker.

## Reliability/calibration

Use weighted kappa for ordinal labels, ICC for continuous ratings, Krippendorff’s alpha where missingness/coders vary, Brier/ECE for probabilistic outputs, and calibration plots by domain.

Automatic metrics are diagnostic. They do not replace blinded human evaluation until validated against it.
