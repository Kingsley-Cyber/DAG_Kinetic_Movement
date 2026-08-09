---
id: cpcs.found.layer_architecture
kind: schema_draft
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-005 §3]
primary_route: cpcs/knowledge/00_foundations/architecture/
secondary_routes:
  - cpcs/knowledge/00_foundations/
interfaces:
  - cpcs.found.motion_field_separation
  - cpcs.found.exactness_taxonomy
  - cpcs.runtime.canonical_schema
---

# CPCS-MX Layer Architecture

> **Source:** SRC-005 §3 — "The CPCS-MX layered architecture"

## Design principle

CPCS-MX models performance as a hierarchy of coupled but independently
inspectable layers. The architecture answers a diagnostic question: when a
generated clip fails, was the failure semantic, temporal, kinematic,
dynamic, expressive, stylistic, or presentational?

## 14-layer stack

| Layer | Primary question | Representative controls |
| --- | --- | --- |
| Intent | Why is the character moving? | objective, tactic, obstacle, subtext |
| Action graph | What causal actions occur? | step, pivot, reach, dodge, recoil, fall, recover |
| Phase | When is each component active? | preparation, initiation, contact, follow-through, reset |
| Root and balance | Where is the body as a whole? | pelvis trajectory, facing, support polygon, COM proxy |
| Joint kinematics | How do segments articulate? | rotations, positions, velocities, accelerations |
| Contact and interaction | What touches or constrains what? | support, grasp, near-contact, prop contact, impact event |
| Dynamics | What virtual physical explanation is used? | mass, impulse, torque estimate, gravity, damping |
| Laban/BESS | What movement quality and shaping are perceived? | Weight, Time, Space, Flow, Shape change |
| Face and affect | What visible and internal performance cues evolve? | FACS-like AU curves, VAD/VAC, gaze, head, blink |
| Mannerism | What makes the movement character-specific? | guard preference, asymmetry, fidget, habitual timing |
| Secondary motion | What follows the primary skeleton? | hair, cloth, soft tissue, accessories, debris |
| Stylization | How is motion transformed by genre? | holds, smears, exaggeration, time warp, deformation |
| Presentation | How does the audience see it? | camera, lens, framing, edit, slow motion, impact frame |
| Verification | How is compliance tested? | contact error, trajectory error, foot slip, readability |

## Modular composition

A movement module is not a finished clip. It is a reusable partial
specification with declared inputs, outputs, preconditions, postconditions,
and editable parameters. Modules are composed through event and constraint
edges rather than by concatenating prose.

## Primary versus derived tracks

CPCS-MX differentiates **authoritative tracks** from **derived tracks**. If
root position is authoritative, velocity and acceleration are calculated
from it under a specified filter. Maintaining two incompatible authoritative
versions of the same quantity creates an overconstrained system.

Recommended authority order:

```text
locked event timing
→ locked contacts and support
→ locked root trajectory
→ locked key joint targets
→ style and expressive fields
→ generated in-betweens
→ secondary simulation
```

This order is configurable. A physics-first workflow may instead lock masses
and contacts and allow the root path to emerge.

## Control versus presentation

CPCS-MX deliberately separates **staged-world motion** from
**rendered-image motion**. Camera shake, zoom, motion blur, speed lines, and
smear drawings can make an action appear faster or stronger without changing
the underlying joint trajectory. The compiler emits both a performance
package and a presentation package, with explicit dependencies between them.

## Relationship to existing cards

- Extends `motion_field_separation` with the full 14-layer stack.
- Authority order extends the `control_scope` concept from SRC-003.
- Presentation separation aligns with `format_ownership` (SRC-004).
