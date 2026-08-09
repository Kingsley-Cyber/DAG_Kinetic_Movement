---
id: cpcs.mx.motor_synergy
kind: mechanism
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-003 §61, §62, §63]
primary_route: cpcs/knowledge/06_body_motion/coarticulation/
secondary_routes:
  - cpcs/knowledge/06_body_motion/biomechanics/
interfaces: [cpcs.mx.action_template, cpcs.mx.motion_realization]
---

# Motor Synergy, Proximal-Distal Sequencing, and Postural Strategy

Human movement is often coordinated through multi-joint patterns rather than
independent joint commands. Motor synergies describe hierarchical coordination
across levels and task-dependent combinations.

## Coordination pattern

```yaml
coordination_pattern:
  id: strike_chain
  purpose: transfer movement through body
  components:
    - pelvis_rotation
    - trunk_rotation
    - shoulder_rotation
    - elbow_extension
    - wrist_alignment
  coupling:
    type: proximal_to_distal
  task_invariant:
    hand_velocity_at_contact: required
```

This is far more useful than independently selecting six joint actions.

## Proximal-distal sequencing

Distinguish research-supported coordination principle from CPCS stylistic
realization. Not every movement is best described by one universal
proximal-distal chain.

```yaml
coordination_rule:
  id: proximal_distal_transfer
  applicability:
    action_classes:
      - strike
      - throw
  status:
    evidence: source_supported
    universality: conditional
```

This prevents an illustrative choreography pattern from becoming a false
universal law.

## Postural strategy

Anticipatory postural adjustments (APAs) occur before predictable perturbations
and help prepare or initiate movement; compensatory adjustments respond after
perturbation.

```text
PosturalStrategy: anticipatory · reactive · mixed
```

```yaml
postural_strategy:
  type: anticipatory
  trigger: upcoming_strike
  objective:
    - preserve_balance
    - prepare_weight_transfer
```

`anticipation` as a narrative phase is not equivalent to `APA` as a motor-control
concept.

## Verification

`test_synergy_components_coordinated`,
`test_proximal_distal_applicability_checked`,
`test_postural_strategy_type_present`.
