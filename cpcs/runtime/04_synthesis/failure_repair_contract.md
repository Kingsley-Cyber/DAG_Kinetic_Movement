---
id: cpcs.runtime.failure_repair_contract
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §4.6, §11.5]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/verification/
  - cpcs/runtime/07_compiler/
interfaces:
  - cpcs.compiler.capability_classes_loss_records
  - cpcs.runtime.reasoning_atom
  - cpcs.runtime.execution_reasoning_state_schema
  - cpcs.verification.measurement_record_form
---

# Failure-Directed Refinement

> **Source:** SRC-006 §4.6 — "Failure-directed refinement"

## Contract

```text
generated output
→ observation records
→ verification results
→ localized failure claim
→ diagnosis with uncertainty
→ responsible canonical/execution paths
→ minimal preconditioned patch
→ invariant checks
→ recompile
→ A/B verification against preserved champion
```

## Failure classes

```text
missing_required_element · unexpected_element · identity_drift
attribute_binding_error · actor_action_binding_error
spatial_relation_error · temporal_order_error · timing_window_error
contact_error · causal_consequence_error · camera_error
edit_continuity_error · audio_presence_error · audio_sync_error
style_invariant_error · physical_commonsense_error
provider_unsupported_control · compiler_loss · evaluation_inconclusive
```

## Localization rule

A repair may be automatic only when:

1. a failure is supported by accepted observation/evaluation evidence;
2. at least one responsible canonical or execution path is identified;
3. the diagnosis confidence meets a calibrated threshold;
4. the patch touches only permitted paths;
5. all protected invariants have executable tests;
6. the original champion remains available for comparison.

If localization is ambiguous, create competing diagnoses or request review.
Do **not** rewrite the full prompt and call it repair.

## Patch semantics

Use ordered, versioned patch operations equivalent to RFC 6902. Start
patches with `test` operations against the source revision and protected
values. A failed `test` aborts the patch; it must not silently target a
newer state. RFC 6902 operation requirements are mandatory: `add`,
`replace`, `test` require `value`; `move`, `copy` require `from`; every
`path`/`from` is a valid JSON Pointer.

The canonical target is not changed merely because the generated video
missed it. Repairs normally adjust execution controls, decomposition,
emphasis, provider routing, or adapter strategy. Changing authored intent
requires separate authorization.

## Diagnosis as ranked hypotheses (SRC-007 G014/G015)

Diagnosis is a set of **ranked, evidence-linked hypotheses**; a symptom is
not a root cause. Every patch must name:

- its authority layer;
- exact field paths;
- protected invariants;
- downstream invalidations;
- required rechecks.

Required demonstrations: a temporal repair that preserves identity/style; a
contact repair that forces temporal re-solving; a carrier repair that does
not mutate canonical meaning; an ambiguous observation failure that
escalates instead of being patched speculatively. Loop termination and
rollback rules apply to every repair chain.

`test_diagnosis_ranked_evidence_linked_hypotheses`,
`test_patch_declares_authority_layer_and_invalidations`,
`test_ambiguous_failure_escalates_not_speculative_patch`,
`test_repair_loop_terminates`.

## Verification

`test_failure_requires_observation_evidence`,
`test_automatic_repair_requires_localization`,
`test_patch_starts_with_protected_value_tests`,
`test_patch_touches_only_allowed_paths`,
`test_canonical_intent_unchanged_without_authorization`,
`test_rollback_restores_exact_parent_state`,
`test_repeated_equivalent_repair_stops_loop` (SRC-006 §11.5).
