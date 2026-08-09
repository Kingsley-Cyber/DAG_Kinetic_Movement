---
id: cpcs.runtime.capability_negotiation_protocol
kind: contract
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §19.19-19.22]
primary_route: cpcs/runtime/07_compiler/
interfaces:
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.runtime.canonical_schema
  - cpcs.runtime.typed_merge_algebra
---

# Capability Negotiation Protocol

> Distilled from CPCS paper §19.19-19.22. Defines how the compiler discovers what
> a target model can accept and degrades gracefully when controls are unsupported.

## 8 capability statuses

For each control field, the adapter reports one of:

| Status | Meaning |
| --- | --- |
| `native_exact` | Field maps directly to a documented API parameter or control channel |
| `native_approximate` | Field maps to a supported channel but with known fidelity loss |
| `baked_into_reference` | Control is rendered into a reference image, landmark sequence, or appearance asset |
| `compressed_to_text` | Control is compressed into a natural-language prompt clause |
| `postprocess_only` | Control is applied as a post-production operation (compositor, retime, crop) |
| `evaluation_only` | Control is retained only as a verification target, not enforced during generation |
| `dropped_with_warning` | Control is unsupported; a warning is emitted and the field is not forwarded |
| `unsupported_error` | Control is a hard requirement that the target cannot satisfy; compilation fails |

## Loss budget

Every compilation declares what it is willing to lose:

```yaml
loss_budget:
  hard_domains:          # these must not degrade
    - safety
    - asset_identity
  maximum_text_compression: 0.3  # max fraction of control info lost to prose
  permitted_approximations:
    - au_intensity_mae: 0.15
    - camera_position_rmse_m: 0.5
  forbidden_drops:       # these controls must not be dropped
    - contact_policy
    - identity_lock
```

## Degradation ladder

When a control cannot be natively accepted, the compiler walks down:

1. **Native channel** — direct API parameter or control asset
2. **Baked reference** — render AU curve into facial landmarks or expression image
3. **Control media** — convert to pose video, depth map, mask, or camera path
4. **Text compression** — compress into timed language clause in prompt
5. **Evaluation only** — retain as verification target, not enforced
6. **Drop with warning** — report in compile report, do not pretend enforcement
7. **Error** — hard requirement not satisfiable, fail compilation

## Backend adapter examples (July 2026)

### Sora 2 (deprecated, shutdown September 2026)

- Accepts: prompt text, duration, aspect ratio, first/last frames
- Does not accept: AU curves, Laban vectors, camera 6DoF paths
- AU handling: `compressed_to_text` or `baked_into_reference` (expression landmarks)
- Camera: `compressed_to_text` (prose description of movement)

### Veo (Vertex AI)

- Accepts: prompt text, first/last frames, duration
- Does not accept: AU curves, phase tracks, contact constraints
- AU handling: `baked_into_reference` (landmark sequence as control image)
- Camera: `compressed_to_text`

### Runway

- Accepts: prompt text, reference images, camera motion presets
- Does not accept: AU curves, Laban vectors, contact constraints
- AU handling: `compressed_to_text`
- Camera: limited presets (pan, zoom, orbit) — `native_approximate` for presets, `compressed_to_text` for custom paths

## Compile report structure

Every compilation produces a report recording what each control became:

```json
{
  "control_mappings": [
    {
      "control_id": "shot014.mara.au04",
      "source_path": "/tracks/face/0",
      "importance": "hard_target_soft_tolerance",
      "status": "baked_into_reference",
      "outputs": [
        "control/face_landmarks_000060.json",
        "control/expression_apex_000066.png"
      ],
      "losses": [
        "continuous AU curve reduced to landmark sequence and one appearance reference"
      ],
      "verification": [
        "au04_apex_time_error_s",
        "au04_intensity_mae"
      ]
    }
  ]
}
```

## 3 compilation tiers

| Tier | Controls available | Use case |
| --- | --- | --- |
| 1 — Prompt only | Text description, duration, aspect ratio | Ideation, rapid exploration |
| 2 — Multimodal control | + first/last frames, pose video, depth, masks, camera path, reference images | Production with control media |
| 3 — Render-assisted | + simulation, physics, IK, compositor, post-production | Full pipeline with render assistance |

## Provider adapter contract

Every adapter must declare:

```json
{
  "id": "adapter.generic.prompt-video/1",
  "model_id": "model-name",
  "api_version": "2026-07",
  "verified_on": "2026-07-18",
  "accepts": {
    "duration_s": {"support": "native"},
    "aspect_ratio": {"support": "native"},
    "first_frame": {"support": "native"},
    "last_frame": {"support": "native"},
    "prompt_text": {"support": "native"},
    "au_curve": {"support": "none"},
    "laban_vector": {"support": "none"},
    "camera_path_6dof": {"support": "none"},
    "pose_video": {"support": "none"}
  }
}
```

The `accepts` map is at the granularity of control fields, not the whole model.
A model may natively accept duration but not AU curves.
