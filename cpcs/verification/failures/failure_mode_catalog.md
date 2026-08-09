---
id: cpcs.verification.failure_mode_catalog
kind: catalog
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§55]
primary_route: cpcs/verification/failures/
secondary_routes:
  - cpcs/runtime/04_synthesis/
  - cpcs/verification/repair/
interfaces: []
---

# Failure-Mode Catalog

Predictable failure modes the reasoning system should classify. This table
should become a **test taxonomy**, not merely documentation.

| Failure | Meaning | Correct response |
|---|---|---|
| semantic_invention | unsupported meaning added | remove / mark unknown |
| private_state_inference | visible movement converted to internal state | downgrade interpretation |
| scope_leak | local control becomes global | restore scope |
| temporal_flattening | phrase reduced to static label | restore envelope |
| framework_collapse | Laban/Bartenieff/FACS treated as the same thing | restore typed semantics |
| realization_overclaim | proxy treated as framework measurement | relabel proxy |
| provider_overtranslation | abstract concept exaggerated | use guardrail |
| control_saturation | too many redundant controls | rank/suppress |
| observability_mismatch | invisible control prioritized | suppress projection with loss |
| continuity_break | hidden state changes without cause | preserve persistence |
| causal_confusion | succession treated as causation | separate relations |
| interaction_desync | actors act independently when coupled | add coordination |
| fallback_loss | unsupported control silently dropped | emit loss record |
| verification_ambiguity | no observable success criterion | add expectation |
