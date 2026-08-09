---
id: cpcs.combat.math_metrics_layer
kind: mechanism
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U21]
primary_route: cpcs/knowledge/05_action/combat/
secondary_routes:
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.body.combat_coding
  - cpcs.lab.architecture
  - cpcs.runtime.kinematic_validation
  - cpcs.camera.three_layer_semantics
  - cpcs.style.anime_sakuga
---

# Combat Math Metrics Layer

> **Source:** SRC-010 `references/combat_choreography.md`. Adds the quantitative
> layer (units, budgets, tolerances) on top of the combat ontology in
> `cpcs.body.combat_coding`. Empirically exercised by v005/v006 (SRC-010).

## Two-document architecture

Combat is authored as **two linked documents**:

1. **YAML authoring doc** — intent, beats, style, character profiles.
2. **JSON kinematic doc** — the measured truth: keyframes, vectors, contacts,
   tolerances. JSON ⊂ YAML by convention; the kinematic doc is the executable
   canon (v005 proved it sufficient alone).

**Laban float encoding** (authoring-side proxies, see the numeric calibration
contract): weight / time / space ∈ [0, 1], flow ∈ [−1, 1]; 9 named Effort
float signatures (e.g., punch = strong/fast/direct with bound flow). These are
**typed proxies for authoring** — v005's `lab_control` effort vectors proved
as a working control channel — not universal measurements (SRC-002 §1.6).

## Contacts (5 types)

`impact` · `near_miss` · `block` · `grasp` · `grasp_and_shove` — each with
timing, distance tolerance, and normal/impulse fields in the kinematic doc.

## Frame timing

- **Frame budget identity:** `beat_frames = (end − start) × fps` — every beat
  budget must satisfy it exactly (TOL_FRAME 0, checked by tooling).
- **4-phase strike ratios** (% of beat duration):
  anticipation 25–35% · contact 10–15% · follow-through 25–35% · recovery 15–30%.
- Exposure patterns: 1s / 2s / 3s holds; **held impact frames 1–8** at contact.

## Kinematics required per beat

`closing_speed_ms` · `screen_velocity_pct_s` · `strike_velocity_ms` ·
`torso_rotation_per_strike_deg` · `recoil_distance_m` · `weight_transfer_time_ms`.

Strike velocity references: jab 6–8 m/s typical / 10–14 elite; **anime scale
1.5–3×** human values.

## Spatial geometry

6 engagement ranges by style, 0.3–2.5 m (e.g., MMA clinch ~0.3–0.5 m; wuxia
loose ~1.5–2.5 m). Contact geometry must satisfy `separation ≤ combined reach
+ TOL_REACH` (0.35 m) — the check that caught v005's 0.18 m deficit.

## Tempo and power

- **BPM table:** 6 beat types, 40–220 BPM (build 40–70, exchange 80–120,
  impact cluster 140–220, …); rest beats last 2–6 frames.
- **Power curves:** normalized by beat (e.g., 0.30 → 1.00 escalation);
  `power_escalation_monotonic` constraint — power never dips once escalated.

## Combat FACS (intensity B–E)

- Combat runs intensity **C–E** vs UGC **B–C**; E = mugging only at impact.
- 8 AU combos for fight faces (brows, lids, jaw); 3 rules (AU4+AU7 before
  contact, AU12 suppressed during threat, asymmetric AU43/AU45 blinks for
  impact).

## Combat Laban

7 strike → Effort mappings (punch = strong/sudden/direct…); 6 shape values;
bound → free transition as the strike lands (relaxation after contact).

## Required constraints (10) with tolerances

Identity lock, no slow-mo, no VFX, continuous unbroken coverage, reach
verified (TOL_REACH 0.35 m), contact time error ≤ 50 ms, contact distance
≤ 0.05 m, foot-contact consistency, monotonic time, near-miss clearance —
all machine-checkable by `validate_kinematics.py` (v006: 0 failures).

## Camera math (7 parameters)

`focal_length_mm` · `angle_deg` · `tracking_speed_match` (camera matches
subject speed) · `shake_amplitude_px` · `shake_frequency_hz` (8–15) ·
`shake_decay_frames` · `whip_pan_speed_deg_s` (120–240). Patterns by beat
type: wide establishing for anticipation, tight + shake on impact, release
on recovery.

## Archetypes and style notes

5 fighting archetypes → Laban baselines (brawler = heavy/direct; acrobat =
light/indirect; …). Style notes: **shonen** (anime scale 1.5–3×, held impact
frames, impact grammar per `cpcs.style.anime_sakuga`) · **wuxia** (loose
ranges, floaty weight) · **MMA** (tight ranges, real velocities) · **superhero**
(superhuman physics split, staged near-contact kept honest).

## Boundary

This is the math layer for **virtual/animated** combat authoring — staged
near-contact and screen craft, not real-world combat instruction. Tolerance
values are authored lab controls (calibrated in v006), not universal constants.

## KB force and phase alignment (SRC-012 EXTEND)

> **Source:** SRC-012 topics 3, 8, 10 — phase grammar, force dynamics, rhythm

### Impact decomposition (four stages; contact instant is the causal anchor)

1. **Pre-impact:** support loading, alignment, pre-tension proxies, slack
   removal, visual/audio anticipation.
2. **Contact:** relative-velocity change, deformation, impulse, impact
   sound, graphic impact cue.
3. **Post-impact:** target motion, recoil, follow-through, secondary
   vibration, debris/cloth response.
4. **Resolution:** balance recovery, guard return, object rest state,
   reaction beat.

A target that moves **before** contact fails physical causality even if it
looks energetic.

### Force production priors (cinematic starting points — never claims about real athletes)

| Profile | Preparation | Peak speed | Recoil | Follow-through | Commitment |
|---|---|---|---|---|---|
| boxing_snap | 0.25 | 0.85 | 0.8 | 0.35 | 0.65 |
| muay_thai_commitment | 0.45 | 0.8 | 0.45 | 0.8 | 0.9 |
| tai_chi_redirection | 0.25 | 0.35 | 0.25 | 0.55 | 0.55 |
| mma_mixed | — | — | — | — | not one force style; compile by technique/range/context |

### Measurement-status precedence

`measured > inverse_dynamics_estimate > visual_proxy > prompt_prior`.
Physical values require units and measurement status; no inferred force
without mass/contact assumptions; style priors never overwrite measured
dynamics.

### Phase-grammar mapping (third granularity — compatible, do not merge)

| SRC-010 4-phase | SRC-012 7-phase | 10-step engineering grammar |
|---|---|---|
| anticipation 25–35% | initiation + preparation | precondition → anticipation → initiation |
| contact 10–15% | acceleration → stroke (contact as bin) | acceleration → action_apex → contact |
| follow-through 25–35% | overshoot | deceleration → follow-through |
| recovery 15–30% | recovery → settle | recovery → postcondition |

Contact stays the anchor bin. Details in `phase_timing_presets` and
`evidence_vs_engineering_phases` (SRC-012 EXTEND).

### Rhythm alignment of a strike

`setup_strike_recovery` (worked `ex_cross_punch_01`: [0.4, 0.18, 0.42]) is
the KB's beat-relative distribution of setup/strike/recovery phases;
`contact_s` anchors the strike to the musical grid. KB metrics compatible
with the tolerances above: beat-alignment error, inter-onset-interval
coefficient of variation, phase-ratio error, contact-causality error
(contact time error ≤ 50 ms, contact distance ≤ 0.05 m; reaction onset ≥
contact).

### Perceived-force controls (amplify force without changing the kinematic doc)

Visual: anticipation contrast · sharp spacing change near contact · target
deformation/displacement · restrained damped camera impulse (amplitude 0.22,
decay ≤ 6 frames) · impact hold/freeze (1–8 frames, matching the held-impact
budget above) · secondary motion. Audio: pre-impact silence/drop · sharp
high-frequency transient · low-frequency body · delayed reverb. Editing:
cut on or just before impact · reaction shot · time ramp/replay that
reframes rather than physically changes the action.

## Verification

`test_contact_instant_causal_anchor`,
`test_force_profile_measurement_status_declared`,
`test_target_reaction_at_or_after_contact`,
`test_style_prior_does_not_overwrite_measured_dynamics`.
