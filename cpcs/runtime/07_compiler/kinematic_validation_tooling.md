---
id: cpcs.runtime.kinematic_validation
kind: method
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010-U13, SRC-010-U14, SRC-010-U18]
primary_route: cpcs/runtime/07_compiler/
secondary_routes:
  - cpcs/evaluation/benchmark_runs/
interfaces:
  - cpcs.lab.variant_lineage
  - cpcs.lab.runbooks
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.evaluation.video_observation_graph
---

# Kinematic Validation Tooling

> **Source:** SRC-010 `lab/scripts/validate_kinematics.py`, `extract_pose_tier2.py`,
> `RUNBOOK_reference_to_kinematic_truth.md`. The **pre-render self-consistency
> gate** for numeric canonical truth — the half of the verification loop the
> lab actually tooled. The post-render half (measuring an output) is open.

## validate_kinematics.py — 8 check families

Checks a kinematic canon document for internal consistency **before** rendering.
Exit code 0 = pass. Per-check verdicts: `ok` / `warn` / `fail` / `skip`.

| # | Family | What it guards | Tolerance |
|---|---|---|---|
| 1 | Frame math | beat budget identity: `beat_frames = (end − start) × fps` | TOL_FRAME 0 |
| 2 | Velocity vectors | authored speeds are physically self-consistent | TOL_SPEED 0.05 m/s |
| 3 | Position/velocity coherence | positions integrate consistently with velocities | — |
| 4 | **Contact geometry** | separation vs combined reach (the family that caught v005) | TOL_REACH 0.35 m |
| 5 | Closing speed | approach speed matches contact timing | — |
| 6 | Foot contacts | foot-contact track agrees with root motion | — |
| 7 | Monotonic time | no time travel: times strictly increasing | — |
| 8 | Near-miss clearance | near-miss events keep honest clearance | — |

## The lesson it exists for (v005 → v006)

v005 authored fighters 1.60 m apart at first contact with 1.42 m combined
reach — a **0.18 m deficit** the canon could not execute. Family 4 (contact
geometry) caught it; watching the render did not. A numeric canon that is not
self-consistent will fail silently, so **every numeric canon passes this gate
before it is rendered** (0 failures for v006).

## extract_pose_tier2.py — the Tier-2 pose lane

MediaPipe-based multi-person 2D pose extraction feeding schema-valid
observation records:

- `JOINTS`: 13 landmark vocabulary; `EXTRACTOR_VERSION: lab-pose-tier2/1.0`
- multi-person: `num-poses 2`, keyframe every 0.5 s, greedy nearest-centroid
  tracking across keyframes
- output: schema-valid observation records (`detected` evidence class)

**Honest bounds (never violated):**

- Output is 2D image-space `detected` evidence — never relabeled `measured`.
- Camera motion is not separated from subject motion.
- Tier 2 cannot claim world-space truth; it can only feed it.

## Tier ladder (evidence quality)

```text
Tier 1  semantic lane      — Pegasus prose extraction (~1 fps, intent, not measurement)
Tier 2  pose lane          — 2D detected keypoints (extract_pose_tier2)
Tier 3  calibrated lane    — stereo / camera-calibrated 3D
Tier 4  measurement lane   — mocap / ground truth
```

Merge rule between lanes: when a semantic value (e.g., strike at 1.4 s) and a
pose value (1.55 s) disagree, the **measured lane wins, the semantic label is
retained** as provenance.

## Round-trip verification

After generating a clip from a canon: re-extract, re-measure, and compare —
thresholds 50 ms time / 0.05 m position. This closes the loop the lab has
tooled only halfway (pre-render gate yes; post-render measurement still open).

## Integration

- `validate_repo.py`: pre-commit gate over the lab repository itself.
- `sync_repo.py`: E2E sync control plane, checks S1–S4 (schema, graph,
  concepts, ledger consistency) before any promotion.
- Canon documents: `hard_constraints` + `verification` blocks in v005/v006
  encode the expected tolerances (e.g., contact_time_error_ms ≤ 50,
  contact_distance_m ≤ 0.05) for the post-render half.

## Boundary

Tooling proves internal consistency of a canon — it does **not** prove a
provider will honor the canon. That remains the open post-render half.
