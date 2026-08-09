---
id: cpcs.request.intent_to_control_mapping
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§33]
primary_route: cpcs/runtime/00_request/intent/
secondary_routes:
  - cpcs/runtime/03_retrieval/
  - cpcs/runtime/04_synthesis/
interfaces: []
---

# Intent → Framework Control Mapping

## Avoid fixed semantic lookup

Do **not** implement universal lookups like
`restrained confidence → AU12 + Bound + Direct`. Instead:

```text
creative intent → context interpretation → candidate realizations
    → framework candidate controls → selection based on shot/action/interaction
```

## Candidate mapping object

```yaml
intent_mapping:
  source_intent: restrained_confidence
  context: { scene_type: dialogue, shot_scale: close_up, actor_role: speaker }
  candidates:
    - { control: facs.au12, rationale: restrained_smile_candidate, confidence: medium }
    - { control: gaze.stable_target, rationale: sustained_attention_candidate, confidence: high }
    - { control: laban.effort.flow.bound, rationale: movement_restraint_candidate, confidence: medium }
  forbidden_inference: [private_confidence_state]
  evidence_class: cpcs_proposed
```

The candidate list is **not** an instruction to use every item. The director
selects after considering context and salience. No automatic mapping to a
private emotional state is permitted (see director decision procedure).
