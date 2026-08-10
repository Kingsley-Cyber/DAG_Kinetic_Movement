# CPCS Failure-Aware Video Generation Research Package

**Version:** 1.0  
**Research date:** 2026-08-05  
**Repository inspected:** `Kingsley-Cyber/ai-video-movement-prompt-system` at `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Status:** professional source/repository synthesis complete; provider render campaigns designed but not executed.

## Mission

This package answers the operational question:

> Given a requested video event, what conditions cause a generative video model to invent, merge, omit, reverse, deform, teleport, duplicate, obscure, or incorrectly resolve information, and what is the most reliable intervention at each failure boundary?

The central answer is that visually ambiguous intervals must be modeled as **persistent hidden state**, not merely discouraged with negative prompts. CPCS needs enough state, event, spatial, identity, causal, visibility, interaction, camera/edit, audio, and verification structure to remove avoidable ambiguity—and must escalate to references, control media, decomposition, postproduction, localized repair, or provider substitution when prompt text cannot carry or verify the hard requirement.

## Package facts

| Artifact | Count | Meaning |
| --- | --- | --- |
| failure records | 96 | 16 families, each with trigger/cause/mitigation/verification/ownership |
| evaluation metrics | 60 | lane, method, blind spots, calibration, threshold policy |
| provider rows | 21 | official capability separated from reliability |
| source records | 81 | repository, official docs/repos, papers, benchmarks, tools |
| claims | 35 | load-bearing conclusions with source and scope |
| experiment fixtures | 8 | paired repeated-seed plans, status designed_not_run |
| candidate contract schemas | 5 | minimal nested extensions for owner review |

## Start here

1. `EXECUTIVE_SYNTHESIS.md` — decisive findings and the water-splash analysis.
2. `MINIMUM_SUFFICIENT_REPRESENTATION.md` — the final design answer and escalation boundary.
3. `FAILURE_TAXONOMY.md` — all 96 failure records and IDs.
4. `FAILURE_CAUSE_MODEL.md` — target, provider, and evaluator failure model.
5. `MITIGATION_HIERARCHY.md` — L0 through L9 selection and exit checkpoints.
6. `CPCS_INTEGRATION_RECOMMENDATIONS.md` — exact owner-preserving implementation route.
7. `EXPERIMENT_AND_ABLATION_PLAN.md` — how to obtain provider-specific evidence.
8. `EMPIRICAL_EXECUTION_STATUS.md` — completed versus not run.

## Domain reports

- `OCCLUSION_AND_HIDDEN_STATE_FAILURES.md`
- `IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md`
- `SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md`
- `TEMPORAL_ACTION_CAUSALITY_FAILURES.md`
- `CONTACT_BALANCE_AND_PHYSICS_FAILURES.md`
- `FLUID_MATERIAL_AND_VFX_FAILURES.md`
- `CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md`
- `PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md`
- `AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md`
- `EVALUATOR_FAILURES.md`

## Machine-readable outputs

- `FAILURE_RECORDS.jsonl` and `FAILURE_RECORD.schema.json`
- `EVALUATION_METRICS.jsonl` and `EVALUATION_METRICS.schema.json`
- `PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv`
- `FAILURE_MITIGATION_MATRIX.csv`
- `SOURCE_CATALOG.csv`
- `CLAIM_SOURCE_MATRIX.csv`
- `REPOSITORY_OVERLAP_MATRIX.csv`
- `schemas/*.schema.json`
- `examples/*.json`
- `experiments/*.yaml`

## Evidence classes

The package distinguishes repository fact, official capability, peer-reviewed/preprint benchmark result, controlled research method, engineering inference, anecdote, and unverified claim. Source IDs such as `[M001]`, `[B004]`, and `[R006]` resolve in `SOURCE_CATALOG.csv`. Recent preprints and provider-authored claims are explicitly limited.

## Empirical limitation

No commercial or local provider renders were executed because no authorized credentials, generation budget, model weights/workflow, or human rating panel were supplied. The package does not report fabricated success rates. Every failure record carries `cpcs_render_campaign_status=not_run_no_authorized_provider_credentials_or_budget_in_session`.

## Validation

Run:

```bash
python3 scripts/validate_package.py .
```

The generated `VALIDATION_REPORT.json` records the validation result, and `SHA256SUMS.txt` provides file integrity hashes.
