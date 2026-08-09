---
distillation_id: DIST-016
source_id: SRC-016
status: complete
coverage: core
---

# Distillation Ledger — SRC-016

User research return (gap_answer_05, 2026-08-09): why AI video adds extra
or mismatched hands — identity-ambiguity diagnosis, six stacked failure
drivers, fix doctrine (two stable labels, continuous contact, fewer action
changes per clip, endpoint frames) → CPCS knowledge tree. Distilled
2026-08-09. Coverage: core (2 EXTENDs + corroboration).

## PASS 0 — Source identity

See `research/source_registry/identities/SRC-016_mismatched_hands_diagnosis.md`.
Epistemic class: research_package (staged). Short Diagnosis: role-label
ambiguity — two physical hands described with three changing role labels
are inferred as separate visual agents.

## PASS 1 — Structural map

- Short diagnosis + root cause (identity ambiguity)
- Six fragility factors: role renaming → extra actors; empty-hand transfer
  → hallucination; hard cuts re-sample identity; exit/re-entry resets
  continuity; POV forearm competing prior; hand-object contact is hard
- Better/worse prompt pairs per factor
- Research support (HanDiffuser, HandDiffuse, DiffH2O, JointHOI, Video
  Storyboarding, Sora 2 guide, reference-image conditioning)
- Bottom line: stacked failure; highest-leverage fix = reduce identity
  burden

## PASS 2 — Placement (D2)

| Unit | Route | Action |
| --- | --- | --- |
| Hand-identity label stability (role renaming, transfer, cut/exit/re-entry, POV prior, fix doctrine) | `knowledge/07_interaction_contact/actor_object/interaction_lifecycle.md` | EXTEND (SRC-016) |
| role_renaming / hand_spawn / reentry_reset catalog rows | `verification/failures/failure_mode_catalog.md` | EXTEND (SRC-016) |
| Corroboration of SRC-013 FAIL-01/FAIL-03 + SRC-015 role permanence | — | SUPPORT (no new object) |
| Identity + ledger | `research/source_registry/identities/` | CREATE (this batch) |

## PASS 3 — Staged notes

The diagnosis is evidence-linked but the artifact-rate claims are
experience-based; they enter the tree as directing doctrine, not measured
statistics. Experiments (carrier_effect_design / provider runs) are
required before any numeric promotion.

## Housekeeping

DIRECTORY.md regenerated; checker 0 deviations; control plane reference
§2/§8/§9/§14 synced; doctrine register D-2026-08-09-13.
