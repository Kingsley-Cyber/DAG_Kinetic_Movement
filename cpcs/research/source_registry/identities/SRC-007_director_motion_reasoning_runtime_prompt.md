---
id: SRC-007
title: Director Motion Reasoning Runtime Gap Closure (Deep Research Prompt)
version: 1.0
epistemic_class: authored
status: COMPLETE
lines: 539
file: Research_distillation_folder/06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md
kind: vocabulary
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-007]
primary_route: cpcs/research/source_registry/identities/
---

# SRC-007 — Director Motion Reasoning Runtime Gap Closure (Deep Research Prompt)

- **File:** `Research_distillation_folder/06 Deep Research Prompt — Director Motion Reasoning Runtime Gap Clo.md`
- **Lines:** 539
- **Artifact type:** Deep-research prompt / brief (not a completed report)

## Source identity

A research prompt instructing a deep-research pass on the DMR (Director
Motion Reasoning) gap register. Names G001–G009, G011–G017, and G019–G021
(19 defined gaps) and explicitly does **not** define G010, G018, or G022 —
those must be recovered from an attached register, never inferred from
numbering. Every register entry must end as `closed`,
`implementable_now`, `requires_experiment`, `unknown`, `deferred`, or
`rejected` with a reason. The prompt mandates a decision-path output for
every gap and six packet-specific sections.

Because this is a prompt, distilled objects are **research requirements**,
not verified findings. All implementation claims remain pending research.

## Source units

| Unit | Gap | Domain | New objects | EXTENDs |
| --- | --- | --- | --- | --- |
| U01 | G001 | Canonical ScenePlan reconciliation (Universal Score / CPCS-MX / VOG / DMR) | 1 (sceneplan_authority_projection) | 0 |
| U02 | G002 | Temporal solver (Allen, OWL-Time, STN/STNU) | 1 (temporal_solver_semantics) | 0 |
| U03 | G003/G004 | Action preconditions/effects, persistent state catalog | 1 (state_variable_catalog) | 0 |
| U04 | G005 | Typed contact lifecycle stages | 0 | E2 (interaction_lifecycle) |
| U05 | G006 | Feasibility validator with typed outcomes | 0 | E1 (constraint_feasibility) |
| U06 | G007/G008 | Provider capability contracts and adapters | 1 (provider_capability_snapshots) | 0 |
| U07 | G009 | Exactly-once compilation-loss report | 0 | E3 (capability_classes_and_loss_records) |
| U08 | G011/G012/G013 | Measurement stack, evaluator, target/observation join | 0 | E4 (measurement_record_form) |
| U09 | G014/G015 | Causal failure taxonomy, minimal patch model | 0 | E5 (failure_repair_contract) |
| U10 | G016/G017 | Benchmark and experiment harness | 1 (benchmark_harness_contract) | 0 |
| U11 | G019 | Format doctrine with meaning_id | 0 | E6 (carrier_effect_experiment_design) |
| U12 | G020 | FACS/Laban numeric scale calibration | 1 (numeric_scale_calibration) | 0 |
| U13 | G021 | Provider lifecycle (unverified → invalidated) | 0 | merged into provider_capability_snapshots |
| U14 | Shared fixture | Glass-break fixture with stable causal spine | 0 | 0 (gaps file) |
| U15 | Required outputs | 6 packet sections (decision table, authority matrix, trace, slice, deferred scope, acceptance) | 0 | 0 (gaps file) |
| U16 | Standards anchors | Temporal/provenance/affect/movement standards as references, not wholesale imports | 0 | 0 |
| U17 | Execution rules | Frozen package primary corpus; distinguish package/external/proposed/hypothesis | 0 | 0 (registration) |

## Self-declared limitations

- G010, G018, G022 are undefined in this prompt; recovery from the attached
  register is mandatory and must not be inferred from numbering.
- Do not redesign CPCS; DMR is execution/runtime research behind the
  existing CPCS semantic authority.
- Do not treat an old provider snapshot as current truth.
- Never claim a current provider capability without official documentation
  or a dated experiment.
- The attached frozen packages were not available to this distillation.

## Distilled object count

- **6 new knowledge cards**
- **6 EXTENDs to existing cards**
- **19 defined gaps + 3 undefined (G010/G018/G022) tracked in gaps file**
