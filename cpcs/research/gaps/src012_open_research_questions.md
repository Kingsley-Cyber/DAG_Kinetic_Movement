---
id: cpcs.gaps.src012
kind: gap_register
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-012]
primary_route: cpcs/research/gaps/
---

# SRC-012 Open Research Questions and Gap Notes

Source: `CPCS_AI_Video_Motion_Direction_KB_v1.0.0` (frozen KB). Distilled
2026-08-09. Questions and deltas that did not close against the tree.

## Open questions

| # | Question | Priority | Cross-source link |
| --- | --- | --- | --- |
| 1 | Which phase boundaries are reproducible across annotators well enough to become canonical? (KB 00_scope + SRC-001 §26 Q1) | P0 | SRC-003 E18 |
| 2 | Which rhythm metrics (beat-alignment error, IOI CV, phase-ratio error, contact-causality error, snappiness/floatiness proxies, cut-rhythm divergence) correlate with expert judgment on real video-model outputs? | P0 | SRC-010 (only empirical source) |
| 3 | Should the KB `rhythm` object (profile + contact_s + setup_strike_recovery 3-split) become a canonical scene field, or remain an authoring convenience reconciled by the compiler? | P1 | canonical_schema_design |
| 4 | Do the KB's 5 evidence classes (ESTABLISHED/EMPIRICAL/PRACTICE/CPCS_CONVENTION/UNVERIFIED) warrant adoption as a tree-wide vocabulary, or stay package-local? (Compare SRC-005 7, SRC-009 VOG 5, SRC-011 6) | P1 | evidence_two_axis_model |
| 5 | Which provider surfaces natively carry timing/phase/contact controls? (KB downcasting says phase_timing/FACS/BESS are high-loss in prose; needs live probing) | P1 | provider_capability_snapshots |
| 6 | Can a real-time BESS detector reach production confidence for Weight/Flow using target-response + contact evidence? (KB proposes assisted inference first) | P2 | laban_proxy_measurement_contract |
| 7 | Should `sequencing_delay_ms`-style per-pattern lag values be calibrated per actor/technique via immutable experiments? (KB value 55 ms is a single CPCS_CONVENTION sample) | P2 | bartenieff_six_patterns |
| 8 | Do the KB 5 phase presets or SRC-010 4-phase strike ratios predict viewer readability better? (Both CPCS conventions; benchmark design in KB 08_evaluation) | P1 | combat_math_metrics_layer |

## Deltas and nuances (noted, no tree change)

- **Preset families differ by design:** KB rhythm presets (production
  profiles) ≠ KB phase-grammar presets (normalized execution profiles) —
  the KB explicitly requires compiler reconciliation, never silent override.
  Distilled into rhythm_metrics_contract + phase_timing_presets.
- **7-phase vs 4-phase vs 10-step grammars:** KB seven-phase (contact as
  event), SRC-010 combat 4-phase (contact as bin), tree 10-step engineering
  grammar (contact explicit step) are three compatible granularities; a
  mapping table exists in combat_math_metrics_layer EXTEND; do not equate.
- **Evidence-class vocabularies** differ across packages (5 vs 7 vs 5 vs 6
  labels); the KB's measurement_status precedence (measured > annotated >
  inverse_dynamics_estimate > model_inference > visual_proxy > prompt_prior >
  generated) is the most granular and is captured as reference.
- **Unit conventions consistent:** KB bipolar [-1,1] with u=(x+1)/2 matches
  SRC-010 laban float encoding (weight/time/space [0,1], flow [-1,1]).
- **UNVERIFIED aliases quarantined:** LabanWRML, ChoosenMove, MoveScape,
  and the ambiguous `CMD` dataset remain UNVERIFIED — never promoted to
  curated entities.
- **Adapter snapshot dated 2026-07-30:** Veo 3.1 (duration 4/6/8; reference
  images ⇒ duration=8), Kling 3.0/Omni (3–15 s, multi-shot, element_voice),
  Runway Gen-4.5 (2–10 s, 24/25 fps) + Act-Two (3–30 s, gesture_control),
  Luma Ray 3.2 (Motion/Structure 1–9; Poses vs Blocking), Firefly (camera
  reference 5–10 s <200 MB, first 5 s used), Sora 2 legacy (web ended
  2026-04-26, API ends 2026-09-24). TTL 21–30 days; reprobe required before
  use.
- **Topic 14 reconstruction:** the KB itself rebuilt topic 14 from a
  truncated query and labeled it a dated snapshot, not a ranking.

## Carried from KB gaps (research agenda)

1. Large open full-BESS dataset with multi-rater expert annotations,
   calibrated motion, contacts, diverse domains/cultures.
2. Reliable visual inference of LMA Weight/Flow with uncertainty.
3. Cross-cultural intent-to-motion benchmark (production vs audience culture).
4. Standard continuous contact topology for multi-human/human-object
   generation evaluation.
5. Open FACS-compatible expression-timing data (masked/asymmetric/nuanced).
6. Provider structured controls for phase timing, trajectories, contacts,
   facial tracks.
7. Causal evaluation metric for contact/reaction order correlating with
   expert judgment.
8. Style-transfer benchmarks scoring invariant action/contact preservation
   separately from stylistic similarity.
9. Verification of aliases LabanWRML / ChoosenMove / intended `CMD` dataset.
