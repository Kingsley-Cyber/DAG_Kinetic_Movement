---
id: cpcs.schema.world_model.universal_kernel_family
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
curation_status: proposal (research/curation path; not yet promoted to governance)
sources: [SRC-001 §10.7, §19, §21, §26, §28, SRC-002 §16, L2.§38, L2.§52]
primary_route: cpcs/schemas/world_model/
---

# Universal Semantic Kernel — Object Family (DRAFT)

> Status: representation proposal from SRC-001 (v1.1). Not an externally
> established ontology. Production authority must be established by CPCS
> fixtures, provider evaluations, and verification metrics before promotion
> via `research/curation/`.

One universal semantic kernel — no separate motion/interaction/camera
ontologies:

```text
Scene
 ├── Actor
 ├── Object
 ├── Relation
 ├── ContinuityState
 ├── StateTransition
 │    └── OcclusionInterval
 ├── PersistenceConstraint
 ├── MotionEvent
 │    ├── trajectory
 │    ├── kinematics
 │    ├── phase_graph
 │    └── effort
 ├── CausalEvent
 ├── InteractionEvent
 │    ├── lifecycle
 │    ├── contact
 │    └── reaction
 ├── CameraState
 │    ├── pose
 │    ├── motion
 │    ├── optics
 │    └── image_formation
 ├── StyleConstraint
 │    ├── invariants
 │    ├── allowed_variation
 │    └── forbidden_drift
 ├── EvidenceRecord
 └── ComplexityWindow
```

## Required fields per object (SRC-001 §26)

```text
MotionEvent: actor_id effector reference_frame temporal action trajectory
             kinematics phases evidence provenance
Phase: role start end boundary_basis confidence preconditions postconditions
InteractionEvent: actor_a actor_b type lifecycle contact visibility evidence
CameraState: pose motion optics focus image_formation
StyleConstraint: domain invariants allowed_variation forbidden_drift
                 priority evidence
Measurement: quantity value unit frame timebase sampling_rate method
             confidence uncertainty missing_data occlusion
ContinuityState: entity_id visibility existence identity actor_count
                 trajectory_continuity pose_continuity action_generation
                 evidence provenance
StateTransition: entity_id type onset offset path pre_state_ref
                 post_state_ref continuity_ref evidence
OcclusionInterval: entity_id start end cause visibility identity_preserved
                 trajectory_preserved hidden_state_status forbidden_generation
                 evidence
PersistenceConstraint: entity_id identity count wardrobe topology existence
                 visibility position priority
CausalEvent: event_id cause produces depends_on must_not_imply
                 temporal_relation evidence provenance
```

## MotionEvent schema sketch (SRC-001 §21)

```yaml
MotionEvent:
  required: [motion_id, actor_id, temporal, reference_frame, semantics]
  fields:
    motion_id: string
    actor_id: string
    temporal: { start: number, end: number, unit: seconds }
    reference_frame:
      position: world | camera | actor_local | object_local
      orientation: world | camera | actor_local | object_local
    semantics:
      action: string
      direction: optional
      amplitude: optional
      speed: optional
      acceleration_profile: optional
      effort: optional
    trajectory: { type: optional, points: optional }
    joints: { side_indexed: boolean, values: optional }
    phases: { items: Phase }
    evidence:
      class: authored | observed | measured | detected | inferred
           | interpreted | derived | unknown | unobservable
      confidence: number
      provenance: optional
```

## Concept mappings (SRC-001 §26)

```text
Laban/BESS → expressive movement attributes
FACS → facial movement events
Kinematics → measurable/derived motion quantities
Phase grammar → temporal action graph
Interaction grammar → contact/reaction graph
Camera grammar → camera semantic object
Style labels → style constraints
Provider adapters → capability matches
```

## Related knowledge cards

- Epistemic firewall: `knowledge/00_foundations/invariants/`
- Evidence two-axis model: `knowledge/00_foundations/uncertainty/`
- Continuity semantics: `knowledge/18_sequence_continuity/occluded_hidden_state/`
- Causal events: `knowledge/00_foundations/causality/`
- Capability classes: `runtime/07_compiler/semantic_mapping/`

## SRC-002 additions (FACS/Laban/Bartenieff/operational)

The kernel is extended, not duplicated. SRC-002 §16/§26 add typed values
inside the universal family rather than competing ontologies:

```text
MotionEvent ── adds facial[] (FACS AU events), laban{}, bartenieff[],
              affect_target{}, gaze{}, head_orientation{}
             = performance_expression_event (SRC-002 §16, L2.§38)
```

Operational layer objects (SRC-002 L2.§52, curation_status: proposal) own
runtime concerns, not new domain predicates: `ApplicabilityRule`,
`ContraindicationRule`, `RealizationPrimitive`, `ControlScope`,
`ControlEnvelope`, `TemporalCoupling`, `ControlPriority`,
`ControlComposition`, `SupportState`, `BodyTopology`,
`FallbackStrategy`, `SemanticGuardrail`, `VerificationExpectation`.
These are placed into existing runtime owners (strategy/canonical/compiler)
per L2.§52, never a parallel FACS runtime.
