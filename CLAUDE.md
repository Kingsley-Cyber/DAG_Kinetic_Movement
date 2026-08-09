# CLAUDE.md — CPCS Repository Guide

> This file mirrors [`AGENTS.md`](./AGENTS.md), the canonical agent guide.
> If you change one, update the other in the same change.

## What This Repository Is

This repository contains **CPCS**: a structured, DAG-style knowledge and
runtime architecture for directing, compiling, and verifying kinetic
cinematic performance (live-action, anime, documentary, UGC, etc.).

It is currently in the **skeleton phase**: the full route tree exists under
`cpcs/`, but most routes are still empty directories awaiting content
(knowledge cards, schemas, research artifacts, code).

The architecture has three planes:

1. **Knowledge plane** — a taxonomy of concepts ("routes"): story, audience,
   performance, motion, physics, camera, lighting, editing, audio, style,
   continuity, plus cross-domain interfaces.
2. **Research plane** — sources, distillation, evidence, numerics, and
   coverage tracking that feed the knowledge plane.
3. **Runtime plane** — a pipeline from request → world model → routing →
   retrieval → synthesis → strategy → canonical score → compiler →
   provider negotiation → execution, with verification, evaluation, and
   maintenance loops around it.

## Repository Layout (top level under `cpcs/`)

| Route | Purpose |
| --- | --- |
| `00_governance/` | Authority, policies, naming, versioning, change control, release/deprecation policy |
| `knowledge/` | The taxonomy itself: `00_foundations` … `20_interfaces` |
| `research/` | Sources, source registry, distillation, curation, evidence, numerics, representation, coverage |
| `observation/` | Measurement from reference video/pegasus: detection, tracking, pose, gaze, contact, reverse compiler |
| `profiles/` | Reusable domain and department profiles (cinematic, anime, camera, audio, …) |
| `runtime/` | The pipeline: `00_request` … `09_execution` |
| `providers/` | Capability registry and per-provider adapters (seedance, kling, veo, runway, luma, ltx, sora, …) |
| `verification/` | Post-generation checks, failure diagnosis, and repair strategies |
| `evaluation/` | Golden cases, benchmarks, ablations, human ratings, calibration |
| `maintenance/` | Health checks, migrations, deprecations, archives for every subsystem |
| `schemas/` | Formal schemas for every subsystem |
| `generated/` | Machine-generated artifacts (repository maps, indexes, snapshots) — never hand-edit |
| `tests/` | Unit, integration, semantic, retrieval, regression, canaries, fixtures |
| `examples/` | Worked examples per domain and per pipeline stage |
| `archive/` | Frozen, superseded, or deprecated material |

The complete, always-current list of every route lives in
[`DIRECTORY.md`](./DIRECTORY.md).

## MANDATORY Rule: DIRECTORY.md Sync

`DIRECTORY.md` at the repo root is a **generated, live index of every route**
in `cpcs/`. Whenever a directory (route) under `cpcs/` is **added, removed,
renamed, or moved**, you MUST regenerate it in the same change:

```pwsh
pwsh -NoProfile -File .\update_directory_md.ps1
```

- Run it from the repo root after the filesystem change succeeds.
- Confirm the route count in its output reflects your change.
- Never hand-edit `DIRECTORY.md`; the generator script owns its content.
- A task that touches `cpcs/` routes is **not complete** until `DIRECTORY.md`
  has been regenerated.

## Conventions

- **Route naming**: lowercase `snake_case`, singular nouns preferred
  (`weight_transfer`, not `weightTransfers`). Cross-domain interfaces use the
  `domain_x_domain` pattern (`motion_x_physics`).
- **Numbered prefixes** encode order/stage and must be preserved:
  `knowledge/00_foundations` … `knowledge/20_interfaces`,
  `runtime/00_request` … `runtime/09_execution`.
- **Never put content in `generated/`** by hand; it is rebuilt by tooling.
- **Deprecation over deletion**: obsolete material moves to `archive/`
  following `00_governance/deprecation_policy/` — do not silently delete
  routes that may be referenced elsewhere.
- **Epistemic discipline**: knowledge content respects the classes in
  `knowledge/00_foundations/epistemic_classes/` (observed, detected,
  measured, interpreted, inferred, authored, creative_choice). Label claims
  with their class; do not present inference as observation.
- New routes should sit at the correct place in the taxonomy DAG; when in
  doubt, prefer a leaf under the closest existing route over inventing a new
  top-level branch.

## Scripts

| Script | Purpose |
| --- | --- |
| `update_directory_md.ps1` | Regenerate `DIRECTORY.md` from the filesystem (mandatory after route changes) |

## Current Status

- Skeleton only: directories exist, content is pending.
- No git repository initialized yet; once one is, a pre-commit hook should
  enforce the `DIRECTORY.md` sync rule.
- Do not create throwaway/test directories inside `cpcs/`; route additions
  are deliberate and must be registered via `DIRECTORY.md`.
