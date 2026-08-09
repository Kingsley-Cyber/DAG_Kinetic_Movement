---
id: cpcs.found.exactness_taxonomy
kind: vocabulary
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §1.2]
primary_route: cpcs/knowledge/00_foundations/epistemology/
secondary_routes:
  - cpcs/verification/
interfaces:
  - cpcs.found.evidence_two_axis_model
  - cpcs.runtime.canonical_schema
---

# Exactness Taxonomy

> **Source:** SRC-005 §1.2 — "What 'exact' can mean"

## Problem

The word *exact* is used without specifying the reference space. A prompt can
claim "exact motion" while leaving ambiguous whether the target is temporal
precision, screen-space trajectory, rig-space kinematics, world-space
placement, physical dynamics, or audience perception.

## Six dimensions of exactness

| Dimension | Meaning | Example |
| --- | --- | --- |
| `clock_exact` | Events occur on the intended frame or source timestamp | contact at frame 72 |
| `screen_space_exact` | Visible landmarks, silhouettes, contacts follow intended image-plane paths | fist arc follows screen-space curve |
| `rig_space_exact` | A defined skeleton follows intended root transforms and joint rotations | elbow flexion at 1.42 rad |
| `world_space_exact` | Actors and props follow intended 3D trajectories relative to scene frame | root displacement 0.8 m along +Z |
| `dynamic_exact` | Masses, forces, torques, impulses, contact responses, momentum match a defined physical model | virtual impulse 18 Ns |
| `perceptual_exact` | The audience reads the intended action, emotion, weight, and causal event even when geometric paths differ | "looks like a heavy hit" |

## Key distinction

A single monocular video can strongly constrain clock and screen-space
behavior while leaving depth, hidden limbs, forces, and torques ambiguous.
Conversely, a motion-capture file may provide rig-space trajectories but
omit facial behavior, camera presentation, or visual exaggerations.

## Design rule

Exactness is a **vector of compliance dimensions**, not a single score.
Every target field must declare which exactness class it claims. A
verification metric must measure the dimension the target declares, not a
substitute dimension. A `screen_space_exact` target is not verified by a
`rig_space_exact` metric.

## Boundary

Perceptual exactness does not override geometric exactness. A clip that reads
as "a punch" while reversing the action order fails `clock_exact` even if it
passes `perceptual_exact`. The dimensions are complementary, not
hierarchical.
