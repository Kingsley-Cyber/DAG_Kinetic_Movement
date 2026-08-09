# 10 — Rhythm Layer for Motion Sequencing

## Executive finding

Rhythm is not merely BPM. CPCS represents a hierarchy of sequence, scene, phrase, exchange, action, phase, micro-event, and frame. A master clock in seconds is authoritative; a frame clock and optional musical grid are derived. This makes combat, dance, dialogue, editing, and UGC timing comparable without forcing every motion to music. [S013; S041; S045]

## Core parameters

Tempo, tempo curve, cadence, meter, beat phase, syncopation, micro-pauses, anticipation beats, accent strength, event density, swing, rubato, entrainment, and phase lock are distinct fields. A fast tempo can still contain a long micro-pause; a slow scene can contain a sudden high-acceleration accent.

The system retains continuous times and quantizes to frames only for a render target. Repeated rounding causes drift, especially across long sequences or variable frame rates.

## Action presets

| Preset | Normalized phase ratios | Status |
|---|---|---|
| explosive | initiation:0.05 / preparation:0.22 / acceleration:0.18 / stroke:0.10 / overshoot:0.10 / recovery:0.20 / settle:0.15 | CPCS_CONVENTION |
| ballistic | initiation:0.04 / preparation:0.14 / acceleration:0.22 / stroke:0.12 / overshoot:0.20 / recovery:0.18 / settle:0.10 | CPCS_CONVENTION |
| controlled | initiation:0.08 / preparation:0.18 / acceleration:0.18 / stroke:0.18 / overshoot:0.06 / recovery:0.20 / settle:0.12 | CPCS_CONVENTION |
| sustained | initiation:0.08 / preparation:0.12 / acceleration:0.16 / stroke:0.28 / overshoot:0.06 / recovery:0.18 / settle:0.12 | CPCS_CONVENTION |
| hesitant | initiation:0.12 / preparation:0.27 / acceleration:0.10 / stroke:0.12 / overshoot:0.04 / recovery:0.18 / settle:0.17 | CPCS_CONVENTION |

These presets differ from Topic 3’s general phase profiles because they are rhythm-oriented production profiles. Both are CPCS conventions and must be reconciled by the compiler rather than silently overriding one another.

## Combat rhythm

A feint works through expectation: establish a pulse, show a partial preparation on the expected beat, insert a micro-pause, then place the true stroke off-beat. A counter window can overlap the attacker’s overshoot/recovery, but defense/evasion causality must occur first. A reset beat lowers event density so the viewer can re-establish geography and threat.

CPCS timing is for staged choreography and animation. Performer safety, spacing, and contact control override the desired beat.

## Dance and music

AIST++ formalizes music-conditioned dance data and beat-alignment evaluation. CPCS distinguishes movement initiation, kinetic accent/apex, and settle, because only one of them may align to the musical beat. “Before the beat” often means initiation leads while the apex lands on beat; “after the beat” means the body accent is intentionally delayed. [S045]

## Dialogue and UGC

Gesture stroke often aligns with semantically prominent speech, but exact timing varies with language, gesture type, and speaker. BEAT offers large-scale multimodal data; it should inform priors rather than become a universal template. [S030]

A practical UGC phrase may be `hook → problem → reveal → proof → reaction → CTA`. CPCS treats this as a marketing template. It should additionally reserve a **product legibility hold**, measured by whether target viewers can identify the product/claim, not by an arbitrary fixed frame count.

## Editing rhythm

Cut candidates include acceleration, contact, gaze shift, directional wipe, phrase boundary, audio transient, and reaction onset. Match-on-action is strongest when the source and destination shots share action phase, pose, screen trajectory, and contact state. Cutting before causality is readable creates apparent teleportation or premature reaction.

## Frame-level profiles

| Profile | Parameters | Status |
|---|---|---|
| snappy_24fps | {'onset_frames': [2, 4], 'acceleration_frames': [2, 4], 'impact_hold_frames': [0, 2], 'settle_frames': [3, 7]} | CPCS_CONVENTION |
| floaty_24fps | {'onset_frames': [6, 12], 'acceleration_frames': [6, 14], 'impact_hold_frames': [0, 1], 'settle_frames': [8, 18]} | CPCS_CONVENTION |
| anime_limited | {'key_pose_hold_frames': [2, 12], 'smear_frames': [1, 2], 'impact_frames': [1, 3]} | PRACTICE/CPCS_CONVENTION |

“Snappy” is associated with compressed onset, rapid time-to-peak, localized jerk, and decisive settle. “Floaty” often includes long ramps, distributed acceleration/deceleration, and insufficient contact/weight cues. These are perceptual descriptions, so CPCS stores measurable proxies and human ratings together.

## Example timeline

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

## Metrics

- beat-alignment error;
- inter-onset-interval coefficient of variation;
- phase-ratio error;
- contact-causality error;
- actor-scale-normalized snappiness proxy;
- floatiness proxy from low-frequency motion and long deceleration;
- cut-rhythm divergence from intended shot-duration distribution.

## References and locators

- **[S013]** SAIBA community (2011), *Behavior Markup Language 1.0 Specification*. **Locator:** Behavior phases, sync points, and synchronization  
- **[S014]** McNeill Lab, University of Chicago (2026), *Gesture Phases*. **Locator:** Preparation, prestroke hold, stroke, poststroke hold, retraction  
- **[S015]** Adam Kendon (2004), *Gesture: Visible Action as Utterance*. **Locator:** Chapters on gesture units, phrases, and movement phases  
- **[S016]** Frank Thomas; Ollie Johnston (1981), *The Illusion of Life: Disney Animation*. **Locator:** Chapters on anticipation, follow-through, timing, arcs, exaggeration  
- **[S030]** Haiyang Liu et al. (2022), *BEAT: A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis*. **Locator:** ECCV 2022; dataset statistics and §§3–5  
- **[S040]** David Bordwell; Kristin Thompson; Jeff Smith (2020), *Film Art: An Introduction*. **Locator:** Cinematography, editing, continuity, temporal relations  
- **[S041]** Karen Pearlman (2016), *Cutting Rhythms: Intuitive Film Editing, 2nd ed.*. **Locator:** Timing, pacing, trajectory phrasing, tension/release  
- **[S044]** Li Siyao et al. (2021), *AnimeInterp: Open-Domain Interpolation for 2D Animation*. **Locator:** CVPR 2021; formulation and occlusion-aware interpolation  
- **[S045]** Ruilong Li et al. (2021), *AIST++ Dance Motion Dataset*. **Locator:** ICCV 2021; dataset, beat alignment, evaluation
