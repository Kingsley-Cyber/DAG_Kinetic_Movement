---
id: cpcs.canonical.temporal_coupling
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§25]
primary_route: cpcs/runtime/06_canonical/temporal_tracks/
secondary_routes:
  - cpcs/knowledge/00_foundations/causality/
interfaces: []
---

# Temporal Coupling

A `performance_expression_event` is **coordinated, not merely simultaneous**.
It supports temporal relations distinct from causal ones:

```text
precedes · lags · synchronizes_with · peaks_with · holds_during ·
releases_after · triggered_by
```

## Example

```yaml
coordination:
  - { relation: precedes, source: gaze_shift, target: head_orientation }
  - { relation: holds_during, source: breath_hold, target: anticipation }
  - { relation: synchronizes_with, source: exhale, target: action_release }
  - { relation: peaks_with, source: facs.au4, target: action_apex }
```

The exact causal status must be **separate** from temporal status (see
`knowledge/00_foundations/causality/causal_event_semantics.md`).

## Coupled timing and relative phase (SRC-012 EXTEND — fulfills SRC-003 E16)

> **Source:** SRC-012 topics 3 + 10 — motion phase grammar and rhythm layer

### Master clock doctrine

A **master clock in seconds is authoritative**; the frame clock and an
optional musical grid are **derived** from it. Continuous times are retained
and quantized to frames only for a render target. Repeated intermediate
rounding causes drift, especially across long sequences or variable frame
rates, and is prohibited.

### Timing profiles are distinct from durations

Tempo, tempo curve, cadence, meter, beat phase, syncopation, micro-pauses,
anticipation beats, accent strength, event density, swing, rubato,
entrainment, and phase lock are **independent fields** — a fast tempo can
contain a long micro-pause, and a slow scene can contain a sudden
high-acceleration accent. Phase-ratio presets (`cpcs.motion.phase.timing_presets`,
`cpcs.rhythm.metrics_contract`) are initialization priors, not laws; the two
preset families are both CPCS conventions and are reconciled by the compiler
as a recorded decision, never silently overriding one another.

### Relative phase and phase lock

Coupling between events is expressed with a declared offset (authored `s`
or `measured` + timebase):

```text
phase_lock       (accents/apexes locked to beats or other events, offset declared)
sync_offset      (authored s / measured + timebase; never conflated with causality)
```

Only **one of** movement initiation, kinetic accent/apex, or settle aligns to
a musical beat (AIST++); "before the beat" means initiation leads while the
apex lands on the beat, "after the beat" means the body accent is
intentionally delayed. DAG edges carry the coupling vocabulary:

```text
event →(synchronizes_with)→ event        (coordination, not causality)
event →(peaks_with)→ event               (apex/beat/contact alignment)
event →(phase_locks_to)→ beat|event      (offset as edge attribute)
event →(precedes|lags)→ event            (offset declared; see causal semantics)
```

The seven relations above remain the canonical vocabulary; the rhythm cards
(`beat_syncpoint_alignment`, `camera_impact_sync`) attach them to beats,
accents, and contact events, and the interaction layer's causal bundle adds
`binds` edges with per-event offsets (reaction onset ≥ contact).

## Verification

`test_master_clock_seconds_authoritative`,
`test_frame_clock_derived_not_intermediate_rounding`,
`test_phase_lock_offset_declared`,
`test_sync_offset_not_conflated_with_causality`.
