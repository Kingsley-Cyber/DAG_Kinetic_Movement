---
id: cpcs.runtime.mx_profiles
kind: catalog
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-008 §profiles/, SRC-008 §examples/]
primary_route: cpcs/runtime/06_canonical/
secondary_routes:
  - cpcs/runtime/07_compiler/
  - cpcs/knowledge/16_style_visual_language/
interfaces:
  - cpcs.runtime.mx_compiler
  - cpcs.style.anime_sakuga
  - cpcs.body.superhuman_transform
  - cpcs.body.combat_coding
---

# CPCS-MX Profile System

> Distilled from the frozen package's 8 reusable YAML profiles and 4 worked
> authoring examples. Profiles provide typed defaults that authoring documents
> inherit through `profile://` URIs.

## Profile URI scheme

```text
profile://<category>/<name>
```

Maps to `<profiles_root>/<category>/<name>.yaml`. Each profile contributes a
`defaults` dict that the compiler deep-merges before the authoring body.

## Profile catalog (8)

| Category | Profile | Key defaults |
| --- | --- | --- |
| movement | `natural_human_v3` | Natural locomotion: moderate step variation, breath-coupled torso, relaxed arm swing |
| movement | `staged_action_base_v2` | Stage-combat base: wide stance, controlled weight transfer, proximal-to-distal initiation |
| capture | `authentic_ugc_v2` | UGC camera: handheld micro-motion, lens-address gaze cycle, natural imperfection bounds |
| camera | `impact_readability_v1` | Combat camera: flat depth at contact, frame hold on impact, shake on recoil |
| camera | `observational_medium_wide_v1` | Observation camera: static medium-wide, minimal parallax, full-body visibility |
| screen_action | `staged_near_contact_v2` | Near-contact safety: default `staged_near_contact`, minimum screen distance, recoil latency window |
| style | `anime_sakuga_action_v3` | Anime timing: anticipation expansion, key-pose holds, smear geometry, impact frames |
| performance | `confident_direct_v1` | Performance: direct gaze, controlled mannerism, steady breath |

## Inheritance model

Authoring documents declare `extends:` with one or more profile URIs. The compiler
applies profiles left-to-right, then overlays the authoring body:

```yaml
extends:
  - profile://movement/staged_action_base_v2
  - profile://style/anime_sakuga_action_v3
```

Later profiles override earlier ones. The authoring body overrides all profiles.
This is deterministic: the same profiles + authoring always produce the same merge.

## Authoring document structure

```yaml
cpcs_mx:
  schema: "urn:cpcs-mx:schema:1.0"
  document_id: "..."
  extends:
    - "profile://..."
  scope:
    safety: "..."
    rights: "..."
  shot:
    id: "..."
    duration_s: 4.0
    fps: 24
  characters: [...]
  action_graph: [...]
  performance:
    laban: {...}
    face: {...}
    breath: [...]
  style_transform: {...}
  virtual_physics: {...}
  secondary_motion: [...]
  hard_constraints: [...]
  soft_constraints: [...]
  verification:
    gates: [...]
```

## Worked examples

| Example | Profiles used | Key features |
| --- | --- | --- |
| `natural_walk.yaml` | `natural_human_v3` | Support-aware locomotion, breath, mannerism |
| `realistic_ugc_gesture.yaml` | `authentic_ugc_v2` | Imperfect camera-aware creator, no random instability |
| `staged_combat_exchange.yaml` | `staged_near_contact_v2`, `impact_readability_v1` | Two-actor near-contact, reaction latency, recovery |
| `anime_superhuman_action.yaml` | `staged_action_base_v2`, `anime_sakuga_action_v3` | Virtual physics, phase transforms, rig-safe limits |

## Cross-style transform example

A typed transform from `natural_human` to `anime_sakuga_action` with 10 named
dimensions (timing_compression, anticipation_expansion, key_pose_hold_frames,
arc_exaggeration, silhouette_separation, secondary_overlap, microvariation,
graphic_smear, impact_frame, camera_emphasis) and 5 protected invariants
(action_order, support_contact_sequence, target_identity, screen_direction,
recovery_completion).
