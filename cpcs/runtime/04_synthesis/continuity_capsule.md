---
id: cpcs.runtime.continuity_capsule
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.2, §11.3]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/knowledge/18_sequence_continuity/
  - cpcs/runtime/06_canonical/
interfaces:
  - cpcs.adrg.state_contraction
  - cpcs.mx.continuity_state
  - cpcs.runtime.reasoning_atom
  - cpcs.runtime.execution_reasoning_state_schema
---

# Continuity Capsule

> **Source:** SRC-006 §4.2 — "Continuity capsule and external audit memory"

## Definition

A `continuity_capsule` is a versioned active projection of distilled world
plus execution state, sufficient for a scoped task. It is not the full audit
log and not raw VOG history. It keeps active context small while retaining
digests and pointers to external audit records.

## Active content (minimum partitions)

```text
capsule_id · sufficiency_status · validation_profile · timebase_id
identity_register · world_state · character_state · open_events
camera_state · style_invariants · narrative_state · viewer_guidance
audio_state · active_constraints · unresolved_obligations · beliefs
provider_context · audit_refs
```

Open event transactions retain phase and ownership. Every active hard
constraint must be reconstructible from the projection.

## External audit memory (kept out of active context)

- full prompt and response history;
- closed events whose postconditions are already projected;
- rejected branches and verbose rationales;
- raw frame observations and full VOG history;
- superseded capsule revisions;
- all prior compiler projections;
- complete metric traces after the accepted aggregate is recorded;
- token-level reasoning text;
- source documents already distilled into accepted constraints.

The capsule retains only digests and pointers to these records.

## Sufficiency status

```text
unvalidated  = fields selected by design only
provisional  = passes a declared fixture suite
validated    = passes full-history equivalence and ablation criteria
               for a named task/provider profile
invalidated  = a counterexample shows omitted history changes a
               required decision
```

Sufficiency is scoped by `executor_id`, task family, provider capability
version, schema version, and tolerance profile. It is never universal.
`validated` is rejected without a matching validation profile/version.

## Verification

`test_projection_reconstructs_all_active_hard_constraints`,
`test_capsule_continuation_equals_full_history_on_certification_fixtures`,
`test_field_ablation_identifies_decision_changing_omissions`,
`test_validated_requires_matching_profile` (SRC-006 §11.3).
