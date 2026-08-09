---
id: cpcs.bartenieff.six_patterns
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-002 §14, §15, SRC-002-U12, SRC-002-U13]
primary_route: cpcs/knowledge/06_body_motion/bartenieff/
secondary_routes:
  - cpcs/knowledge/06_body_motion/kinematics/
interfaces: [style_x_motion]
---

# Bartenieff Six Connectivity Patterns

The six patterns required by the closure packet are modeled as
**connectivity relationships/patterns**, not six universal scalar dimensions.
The research literature distinguishes the broader Bartenieff Fundamentals
practice (U13) from the individual connectivity patterns (U12).

## The six patterns

| Pattern | Semantic meaning | Side rule | Proxy candidates |
|---|---|---|---|
| Breath | whole-body connectivity around breath-related expansion/contraction | bilateral | ribcage width/depth · torso volume proxy · vertical torso movement · respiratory audio |
| Core-Distal | core↔distal-limb connectivity | — | `distal_distance_from_core(t)` + temporal direction |
| Head-Tail | longitudinal head/spine/tail axis | — | head-to-pelvis phase lag · spinal curvature propagation · COM changes |
| Upper-Lower | upper↔lower body grounding/support | — | upper/lower segment phase · foot-ground contact timing · COM/limb coordination |
| Body-Half | ipsilateral organization | **side: left/right** (do not collapse) | one side stabilizing while the other mobilizes |
| Cross-Lateral | contralateral cross-body coordination | contralateral | `cross_lateral_index = coord(left_upper,right_lower)+coord(right_upper,left_lower)` |

## Representation (SRC-002 §15)

```json
{
  "type": "bartenieff_connectivity",
  "pattern": "cross_lateral",
  "side_relationship": "contralateral",
  "regions": ["left_arm", "right_leg"],
  "phase": { "start_s": 2.0, "end_s": 3.1 },
  "evidence_class": "interpreted",
  "confidence": 0.78,
  "measurement": { "type": "kinematic_proxy", "status": "uncalibrated" }
}
```

The object stores the **semantic classification** and separately stores the
**measurement basis**. The exact numeric formula (e.g. cross_lateral_index)
is a project-specific derived metric, not a Bartenieff standard.

## Verification

`test_bartenieff_side_preserved`, `test_cross_lateral_not_collapsed`,
`test_bartenieff_pattern_does_not_collapse_to_generic_crossing`.

## Basic Six vs patterns and primitive encoding (SRC-012 EXTEND)

> **Source:** SRC-012 topic 2 — "Bartenieff Fundamentals: Connectivity and
> Motion Primitives"

The KB separates the **Basic Six exercises** (Thigh Lift, Forward Pelvic
Shift, Lateral Pelvic Shift, Body Half, Knee Drop, Arm Circle — Bartenieff
& Lewis practical material) from the **Six Patterns of Total Body
Connectivity** (Hackney developmental sequence: Breath, Core–Distal,
Head–Tail, Upper–Lower, Body-Half, Cross-Lateral). They are **different
inventories**; merging them corrupts both annotation and generation. The
pattern order is pedagogical, not a prohibition on concurrent use — one
cross punch can combine upper–lower grounding, cross-lateral rotation,
core-distal reach, and proximal-to-distal arm sequencing.

### Primitive encoding (KB `motion_primitive` schema)

```json
{
  "primitive_id": "cpcs:primitive/cross_lateral_reach/1",
  "connectivity_pattern": "cross_lateral",
  "initiator": "right_rear_foot",
  "receiver_sequence": ["pelvis", "thorax", "left_shoulder", "left_hand"],
  "intensity": 0.72,
  "range": 0.68,
  "sequencing_delay_ms": 55,
  "grounding": 0.84,
  "breath_phase": "exhale",
  "support_contacts": ["right_foot", "left_foot"],
  "phase_profile": "cpcs:phase/explosive",
  "provenance_class": "CPCS_CONVENTION"
}
```

- `initiator` + `receiver_sequence` make the proximal-to-distal chain
  explicit; `sequencing_delay_ms` (worked cross-punch value 55 ms) is the
  lag between segment onsets — a quantifiable complement to the head–tail
  phase-lag proxy in this card.
- `breath_phase` (worked: `exhale`) binds breathing to action release
  (`temporal_coupling`: exhale synchronizes_with action_release).
- `support_contacts` ties the pattern to the interaction layer's contact
  records (grounding 0.84–0.86 worked).
- `intensity`/`range` are engineering controls, not Bartenieff certification
  scores; use m/s or rad/s when calibrated capture is available.

### Composition and compiler operations

| Compound motion | Primitive chain |
|---|---|
| walking_step | breath → upper_lower → cross_lateral |
| cross_punch | lower-body push → cross-lateral pelvis/trunk → proximal-to-distal arm → recoil |
| comforting_reach | breath → core_distal → head_tail orientation → distal hand contact |
| dance_turn | upper_lower support → head_tail spotting → cross_lateral initiation → sequential arm shaping |

Five compiler operations (KB): **sequence** (end-to-start or controlled
overlap) · **blend** (compatible patterns after phase normalization) ·
**condition** (target/end-state adaptation, ProMP-style) · **mirror**
(reflect laterality and spatial path — must also mirror contact targets and
camera screen direction) · **scale** (time/amplitude warp, then re-run
contact, joint-limit, and balance checks). A blend is invalid when it
violates a support contact, creates foot skating, or asks one joint to
satisfy incompatible constraints — the compiler must not simply interpolate
joint angles. A compound primitive should expose which sub-pattern caused
each segment onset, so learned weights stay auditable.

## Verification

`test_basic_six_not_merged_into_patterns`,
`test_sequencing_delay_matches_segment_onsets`,
`test_blend_preserves_support_contacts`,
`test_mirror_reflects_contacts_and_screen_direction`.
