# 02 — Bartenieff Fundamentals: Connectivity and Motion Primitives

## Executive finding

The original query combined two different Bartenieff inventories. CPCS must keep them separate. The **Basic Six** are exercises; the **Patterns of Total Body Connectivity** are developmental/organizational patterns. Treating them as one list would corrupt both annotation and generation. Bartenieff and Lewis place the Basic Six in their practical material, while Hackney organizes Breath, Core–Distal, Head–Tail, Upper–Lower, Body-Half, and Cross-Lateral as a developmental sequence. [S002, Appendix B; S003, pp.54–219]

## Basic Six exercises

| Exercise | Primary organization | Prompt cues |
|---|---|---|
| Thigh Lift | femoral flexion with pelvic organization | release femur in hip socket; maintain pelvic support |
| Forward Pelvic Shift | sagittal pelvic translation with lower-body support | pelvis glides forward without lumbar collapse |
| Lateral Pelvic Shift | side translation with countertension | pelvis shifts laterally while ribs counterbalance |
| Body Half | ipsilateral organization | same-side arm and leg organize as a unit |
| Knee Drop | diagonal lower-body rotation/reach | knee releases across diagonal while pelvis spirals |
| Arm Circle | scapular-humeral sequencing with torso | circle begins at scapula then shoulder–elbow–wrist |

The Basic Six should not be used as universal motor “atoms” in a strict neurological sense. They are useful **training and observation templates**. CPCS represents each as a reusable primitive profile with explicit initiation, body-part sequencing, range, support, breath, and phase timing.

## Six connectivity patterns

| Order | Pattern | Organization | Locator |
|---|---|---|---|
| 1 | breath | whole-body expansion/condensation through respiratory support | S003, from p.54 |
| 2 | core_distal | radiation from center to limbs and return | S003, from p.71 |
| 3 | head_tail | axial connection between cranial and coccygeal poles | S003, from p.90 |
| 4 | upper_lower | differentiation/integration of upper and lower body | S003, from p.121 |
| 5 | body_half | ipsilateral integration | S003, from p.181 |
| 6 | cross_lateral | contralateral diagonal integration | S003, from p.193 |

**Breath** establishes expansion/condensation support. **Core–Distal** organizes radiation between center and limbs. **Head–Tail** coordinates the axial system. **Upper–Lower** differentiates and integrates grounding with upper-body mobility. **Body-Half** organizes ipsilateral relations. **Cross-Lateral** supports contralateral diagonals used in locomotion, spirals, and many striking/throwing actions.

The “order” is a pedagogical/developmental sequence, not a prohibition against using patterns concurrently. A single cinematic action often contains several patterns: a cross punch can combine upper–lower grounding, cross-lateral rotation, core-distal reach, and proximal-to-distal arm sequencing.

## Motion-primitive encoding

A primitive instance should contain:

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

`intensity` and `range` are engineering controls. They are not Bartenieff certification scores. When calibrated capture is available, speed should use m/s or rad/s; otherwise use normalized, actor-relative values.

## Composition

| Compound motion | Primitive chain | Domains |
|---|---|---|
| walking_step | breath → upper_lower → cross_lateral | everyday, dance, combat footwork |
| cross_punch | lower-body push → cross-lateral pelvis/trunk → proximal-to-distal arm → recoil | boxing, cinematic combat |
| comforting_reach | breath → core_distal → head_tail orientation → distal hand contact | conversation, caregiving |
| dance_turn | upper_lower support → head_tail spotting → cross_lateral initiation → sequential arm shaping | dance |

A useful compiler supports five operations:

1. **Sequence:** connect primitives end-to-start or with controlled overlap.
2. **Blend:** combine compatible patterns after phase normalization.
3. **Condition:** adapt a primitive to a target/end state, similar to conditioning in probabilistic movement primitives. [S068]
4. **Mirror:** reflect laterality and spatial path.
5. **Scale:** time- or amplitude-warp, then re-run contact, joint-limit, and balance checks.

The compiler must not simply interpolate joint angles. A blend is invalid when it violates a support contact, creates foot skating, or asks one joint to satisfy incompatible constraints.

## Domain mappings

### Combat choreography

- **Upper–Lower:** ground-to-strike transfer, level change, sprawl, stand-up.
- **Cross-Lateral:** crosses, rotational kicks, diagonal throws, evasive locomotion.
- **Body-Half:** same-side shield, frame, lateral drive.
- **Head–Tail:** slips, ducks, head movement, axial integrity.
- **Core–Distal:** guard expansion, reach, withdrawal, whole-body commitment.

### Dance

Breath becomes phrasing; Core–Distal becomes extension/return; Head–Tail supports spinal articulation and spotting; Upper–Lower supports grounded legs with a mobile torso; Body-Half supports lateral phrasing; Cross-Lateral supports spirals and turns.

### Everyday action

Reaching, standing, sitting, rolling, walking, and carrying can be described using the same organization without forcing them into dance or combat labels.

## Practical prompt examples

**Cross punch:** “Drive from the floor through upper–lower connection, rotate cross-laterally through pelvis and ribs, then sequence shoulder–elbow–fist; recoil through the reverse chain without losing the two-foot support base.”

**Comforting touch:** “Begin on the exhale, expand core-distally through the sternum and hand, orient head–tail toward the receiver, slow before contact, and let the hand yield to the receiver’s surface.”

**Walk cycle:** “Alternate cross-lateral arm/leg organization over a stable upper–lower support pattern; preserve head–tail continuity and allow breath to modulate the phrase.”

## Validation rules

- Connectivity patterns are organization concepts, not direct muscle-synergy measurements.
- Actor comfort, joint limits, and support state override a preset.
- Mirror operations must also mirror contact targets and camera screen direction where required.
- A compound primitive should expose which sub-pattern caused each segment onset; otherwise learned weights cannot be audited.

## References and locators

- **[S002]** Irmgard Bartenieff; Dori Lewis (1980), *Body Movement: Coping with the Environment*. **Locator:** Ch.3 pp.23–48; Ch.4 pp.49–68; Ch.5 pp.69–82; Ch.6 pp.83–100; Appendix B from p.229  
- **[S003]** Peggy Hackney (2002), *Making Connections: Total Body Integration Through Bartenieff Fundamentals*. **Locator:** Ch.5 p.41; Breath p.54; Core–Distal p.71; Head–Tail p.90; Upper–Lower p.121; Body-Half p.181; Cross-Lateral p.193; Integration p.219  
- **[S039]** Selected peer-reviewed sports-biomechanics sources (2020), *Kinetic-Chain Evidence for Overarm Striking*. **Locator:** Segment sequencing, proximal-to-distal transfer, effective mass  
- **[S068]** Alexandros Paraschos et al. (2013), *ProMPs: Probabilistic Movement Primitives*. **Locator:** Representation, conditioning, blending
