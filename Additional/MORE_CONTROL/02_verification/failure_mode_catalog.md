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

## Causal hand–object failure taxonomy (SRC-013 EXTEND)

> **Source:** SRC-013 (user research return, staged) — gap_answer_02
> §failure taxonomy + §action-specific verification; evidence E9 (VBench),
> E10 (PhyGenBench).

| Code | Failure | Meaning | Correct response |
|---|---|---|---|
| FAIL-01 | ghost_contact | hand-to-part transfer without established surface contact (empty reach) | require contact-preserving path |
| FAIL-02 | effect_before_contact | state change precedes the causal hand contact | enforce causal order |
| FAIL-03 | identity_break | hand/part identity lost or swapped across cuts or occlusion | track ownership graph |
| FAIL-04 | unobserved_interpolation | model invents mechanism for a cut-hidden transition | declare or forbid the cut |
| FAIL-05 | closure_state_error | teeth/closure state contradicts slider passage direction | verify slider-relative state |

Staged metrics (SRC-013 evidence only; experiments required before
promotion): penetration ≤ 2 mm / ≤ 5 mm bounds; cavity visibility
V_cavity ≥ 0.70; contact speed S_contact ≤ 0.05 m/s; contact-detection
head CD_h ≤ 11.3 mm².

## Hand-identity failure drivers (SRC-016 EXTEND)

> **Source:** SRC-016 (user research return, staged) — gap_answer_05;
> corroborates FAIL-01/FAIL-03 and adds three catalog rows.

| Code | Failure | Meaning | Correct response |
|---|---|---|---|
| role_renaming | hand identity labels change with the job (zipper_hand → lip_hand) | model treats labels as separate agents | keep left/right labels stable |
| hand_spawn | extra hand/arm appears during an ambiguous transfer | identity burden too high at the handoff | continuous contact + endpoint anchors |
| reentry_reset | hand identity lost on frame exit/re-entry | identity not re-affirmed at the boundary | restate same-hand reentry |

## Verification

`test_fail_01_ghost_contact_classified`,
`test_fail_02_effect_before_contact_classified`,
`test_fail_03_identity_break_classified`,
`test_role_renaming_classified`,
`test_hand_spawn_classified`.
