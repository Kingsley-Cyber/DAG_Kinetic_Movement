---
id: cpcs.rhythm.metrics_contract
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-012]
primary_route: cpcs/knowledge/10_time_rhythm/
secondary_routes:
  - cpcs/runtime/06_canonical/temporal_tracks/
  - cpcs/knowledge/00_foundations/time/synchronization/
interfaces:
  - cpcs.canonical.temporal_coupling
  - cpcs.motion.phase.evidence_vs_engineering
  - cpcs.runtime.temporal_solver_semantics
---

# Rhythm Metrics Contract

> **Source:** SRC-012 topic 10 — "Rhythm" (KB v1.0.0)

## Principle

Rhythm is not merely BPM. CPCS represents a hierarchy of sequence, scene,
phrase, exchange, action, phase, micro-event, and frame. A **master clock in
seconds is authoritative**; a frame clock and an optional musical grid are
**derived**. This makes combat, dance, dialogue, editing, and UGC timing
comparable without forcing every motion to music.

## Master clock doctrine

```text
master_clock_s (authoritative)  →  frame_clock (derived: fps)
                                →  musical_grid (derived: bpm, meter, beat phase)
```

- The system retains **continuous times** and quantizes to frames only for a
  render/export target.
- Repeated rounding causes drift, especially across long sequences or
  variable frame rates. Never round intermediate timeline values.
- Musical-grid derived fields must be re-derived, not stored as truth:
  `tempo · tempo curve · cadence · meter · beat phase · syncopation ·
  micro-pauses · anticipation beats · accent strength · event density ·
  swing · rubato · entrainment · phase lock`.
- A fast tempo can still contain a long micro-pause; a slow scene can contain
  a sudden high-acceleration accent. These fields are independent axes.

## Rhythm presets (production profiles)

| Preset | Normalized phase ratios | Status |
|---|---|---|
| explosive | initiation:0.05 / preparation:0.22 / acceleration:0.18 / stroke:0.10 / overshoot:0.10 / recovery:0.20 / settle:0.15 | CPCS_CONVENTION |
| ballistic | initiation:0.04 / preparation:0.14 / acceleration:0.22 / stroke:0.12 / overshoot:0.20 / recovery:0.18 / settle:0.10 | CPCS_CONVENTION |
| controlled | initiation:0.08 / preparation:0.18 / acceleration:0.18 / stroke:0.18 / overshoot:0.06 / recovery:0.20 / settle:0.12 | CPCS_CONVENTION |
| sustained | initiation:0.08 / preparation:0.12 / acceleration:0.16 / stroke:0.28 / overshoot:0.06 / recovery:0.18 / settle:0.12 | CPCS_CONVENTION |
| hesitant | initiation:0.12 / preparation:0.27 / acceleration:0.10 / stroke:0.12 / overshoot:0.04 / recovery:0.18 / settle:0.17 | CPCS_CONVENTION |

> **Delta (documented, do not merge):** these presets differ from the
> phase-grammar presets in `phase_timing_presets.md` because they are
> rhythm-oriented production profiles. Both are CPCS conventions and must be
> **reconciled by the compiler** rather than silently overriding one another.
> Reconciliation is a recorded decision (see
> `cpcs.runtime.decision_record`), not an automatic preference.

## Frame-level profiles

| Profile | Parameters (frames @24fps) | Status |
|---|---|---|
| snappy_24fps | onset [2,4] · acceleration [2,4] · impact_hold [0,2] · settle [3,7] | CPCS_CONVENTION |
| floaty_24fps | onset [6,12] · acceleration [6,14] · impact_hold [0,1] · settle [8,18] | CPCS_CONVENTION |
| anime_limited | key_pose_hold [2,12] · smear [1,2] · impact [1,3] | PRACTICE/CPCS_CONVENTION |

"Snappy" = compressed onset, rapid time-to-peak, localized jerk, decisive
settle. "Floaty" = long ramps, distributed acceleration/deceleration,
insufficient contact/weight cues. These are perceptual descriptions; CPCS
stores **measurable proxies and human ratings together**, never one alone.

## Metrics (formulas)

Let \(t_e\) be an event's aligned time and \(t_b\) the target beat time.

- **Beat-alignment error:** \(\frac{1}{N}\sum_e |t_e - t_b|\) over aligned
  events; the aligned event (initiation vs apex vs settle) must be declared.
- **Inter-onset-interval CV:** \(\sigma_{IOI}/\mu_{IOI}\) — pulse regularity.
- **Phase-ratio error:** \(\sum_p |r_{p,actual} - r_{p,preset}|\) over the
  seven normalized ratios (presets above).
- **Contact-causality error:** fraction of reaction/defense onsets that
  precede their causal contact onset (target response must begin at or after
  contact).
- **Snappiness proxy (actor-scale-normalized):** compressed onset, rapid
  time-to-peak, localized jerk, decisive settle — normalized by actor scale.
- **Floatiness proxy:** low-frequency motion plus long deceleration.
- **Cut-rhythm divergence:** divergence of realized shot durations from the
  intended shot-duration distribution.

Automatic metrics are **diagnostic**; they do not replace blinded human
evaluation until validated against it (weighted kappa / ICC / Krippendorff's
alpha / Brier / ECE).

## Combat rhythm

A feint works through expectation:

1. establish a pulse;
2. show a **partial preparation** on the expected beat;
3. insert a **micro-pause**;
4. place the **true stroke off-beat**.

A counter window can overlap the attacker's overshoot/recovery, but
defense/evasion **causality must occur first**. A reset beat lowers event
density so the viewer can re-establish geography and threat. Performer
safety, spacing, and contact control **override** the desired beat in staged
choreography.

## Dance and music

Only one of movement initiation, kinetic accent/apex, or settle aligns to the
musical beat (AIST++ beat-alignment evaluation):

- **"before the beat"** = initiation leads while the apex lands on beat;
- **"after the beat"** = the body accent is intentionally delayed.

## Dialogue and UGC

Gesture stroke often aligns with semantically prominent speech, but exact
timing varies with language, gesture type, and speaker. BEAT is a prior, not
a universal template. A UGC phrase
(`hook → problem → reveal → proof → reaction → CTA`) is a marketing template;
CPCS additionally reserves a **product legibility hold**, measured by whether
target viewers can identify the product/claim — not by an arbitrary fixed
frame count.

## Editing rhythm

Cut candidates: acceleration, contact, gaze shift, directional wipe, phrase
boundary, audio transient, reaction onset. Match-on-action is strongest when
source and destination shots share **action phase, pose, screen trajectory,
and contact state**. Cutting before causality is readable creates apparent
teleportation or premature reaction.

## DAG representation

Rhythm maps to graph edges with the temporal-coupling vocabulary
(`cpcs.canonical.temporal_coupling`):

```text
phase_locks_to   (actor/limb phase → master clock or beat)
synchronizes_with (two events coordinated on the same clock)
peaks_with       (accent/apex → beat or contact)
precedes · lags  (offset relations with declared offset_s or beat)
```

Example timeline (from the KB rhythm topic):

```yaml
fps: 24
music_bpm: 120
phrase:
  start_s: 0.0
  end_s: 4.0
  events:
    - {id: feint, apex_s: 0.92, beat: "1:2:3", accent: 0.35}
    - {id: true_strike, contact_s: 1.25, beat: "1:3:1", accent: 0.95}
    - {id: reaction, onset_s: 1.25, apex_s: 1.46, accent: 0.78}
    - {id: reset_gaze, start_s: 1.80, end_s: 2.20, accent: 0.20}
```

## Verification

`test_master_clock_seconds_authoritative`,
`test_frame_clock_derived_not_stored`,
`test_rhythm_preset_ratios_sum_to_one`,
`test_reaction_onset_at_or_after_contact`,
`test_cut_rhythm_divergence_reportable`.
