# Confidence and Provenance Model

Each factual or prescriptive record may carry:

```json
{
  "provenance_class": "ESTABLISHED | EMPIRICAL | PRACTICE | CPCS_CONVENTION | UNVERIFIED",
  "source_ids": ["S007"],
  "confidence": 0.72,
  "scope": {"population": "hand/arm study", "capture": "mocap", "context": "constrained affective paths"},
  "uncertainty_note": "Do not generalize to unconstrained full-body video.",
  "verified_at": "2026-07-30"
}
```

- `0.90–1.00`: directly stated by a definitive source or current official documentation.
- `0.70–0.89`: strongly supported but context-dependent.
- `0.40–0.69`: plausible empirical/practice prior requiring local evaluation.
- `0.10–0.39`: hypothesis or weakly evidenced mapping.
- `0.00`: unsupported, disproven, or unusable.

Confidence is confidence in applicability under the stated scope, not a probability that a character or real person “truly feels” an emotion.
