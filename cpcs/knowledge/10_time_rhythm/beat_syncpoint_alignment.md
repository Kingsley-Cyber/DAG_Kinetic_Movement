---
id: cpcs.rhythm.beat_syncpoint_alignment
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-012]
primary_route: cpcs/knowledge/10_time_rhythm/
secondary_routes:
  - cpcs/knowledge/06_body_motion/phase_grammar/
  - cpcs/knowledge/00_foundations/causality/
interfaces:
  - cpcs.motion.phase.timing_presets
  - cpcs.canonical.temporal_coupling
  - cpcs.rhythm.metrics_contract
---

# Beat and Sync-Point Alignment

> **Source:** SRC-012 topics 3 + 10 — phase grammar and rhythm; mapping
> `map_phase_bml_v1` from the KB canonical model.

## Principle: two different taxonomies

The CPCS seven-phase sequence and the BML sync points are **different
taxonomies** and must never be relabeled as one another:

- **CPCS seven-phase grammar** (production synthesis):
  `initiation → preparation → acceleration → stroke → overshoot → recovery →
  settle`. CPCS_CONVENTION; permits skip/merge/interruption.
- **BML 1.0 sync points** (SAIBA interoperability standard):
  `start · ready · stroke_start · stroke · stroke_end · relax · end`.
  These are behavior-synchronization anchors, not a universal movement law.
- **Gesture research** (McNeill/Kendon): `preparation → prestroke hold →
  stroke → poststroke hold → retraction`.

## Canonical mapping (map_phase_bml_v1)

| CPCS phase | BML sync point(s) |
|---|---|
| initiation | start |
| preparation | ready / stroke_start |
| stroke | stroke |
| overshoot | stroke_end |
| recovery | relax |
| settle | end |

Status: `CPCS_CONVENTION`; source S013 (BML 1.0 spec). The mapping is a
**compile-time projection target**, not an identity: a CPCS `stroke` may be
contact, maximum extension, or grasp onset depending on action class, while
BML `stroke` is defined by the behavior's meaning-bearing phase.

## Alignment semantics

- **Only one of** movement initiation, kinetic accent/apex, or settle aligns
  to a musical beat (AIST++).
- **"Before the beat":** initiation leads; the apex lands on the beat.
- **"After the beat":** the body accent is intentionally delayed.
- **Feint rhythm** (expectation mechanics): establish a pulse → partial
  preparation on the expected beat → micro-pause → true stroke off-beat.
- A counter window may overlap the attacker's overshoot/recovery, but
  defense/evasion causality must occur first.

## Semantic apex vs contact

`action_apex` is **not automatically** contact (near-miss has an apex without
contact). CPCS keeps semantic apex and physical contact as separately
addressable events; compilers must not emit `contact=true` for near-misses.

## Dialogue and gesture sync

Gesture stroke often aligns with semantically prominent speech; exact timing
varies with language, gesture type, and speaker. BEAT is a prior for priors,
not a universal template. Phase-boundary provenance remains
`observed / authored / derived / provider-oriented` per phase.

## DAG representation

```text
phase →(mapped_to)→ sync_point   (BML projection, CPCS_CONVENTION)
phase →(aligned_to)→ beat        (musical grid; declare initiation|apex|settle)
apex →(peaks_with)→ beat|contact (semantic apex edge, distinct from contact)
reaction →(precedes/lags)→ contact (causality preserved; offset declared)
```

Alignment errors attach to the edge as attributes (see
`cpcs.rhythm.metrics_contract` — beat-alignment error).

## Worked binding (ex_cross_punch_01, scene-clock)

- primitive phase timeline is action-local (0–1.1 s), anchored to the scene
  at beat b2 start (0.7 s);
- contact event `contact_01` binds stroke (0.43–0.5) and overshoot (0.5–0.61)
  → scene 1.13–1.31 s;
- interaction `int_block` window 1.13–1.25 s (duration 0.12 s);
- rhythm block: profile `explosive`, `contact_s: 1.18`,
  `setup_strike_recovery: [0.4, 0.18, 0.42]`;
- expected checks: target reaction starts at or after contact; fist recoils
  to guard by 2.3 s; camera impulse decays within six frames.

## Verification

`test_bml_syncpoint_not_relabeled_as_phase_law`,
`test_alignment_event_declared_initiation_apex_settle`,
`test_semantic_apex_distinct_from_contact`,
`test_phase_timeline_action_local_anchored_by_event`.
