# Model Adapter Architecture

## Adapter key

`provider + model_id + surface + account/tier/region when relevant + adapter_version`.

A web UI, first-party API, and third-party wrapper are separate surfaces even when they use the same marketing model name.

## Capability registry

Each canonical field receives one status:

- native;
- reference-conditioned;
- prompt-only;
- postprocess;
- unsupported;
- unknown;
- legacy.

## Compile algorithm

1. Validate adapter freshness (`verified_at + ttl_days`).
2. Validate input combinations and quotas/limits.
3. Prefer native structured controls.
4. Prefer reference conditioning for identity, motion, camera, or expression when available.
5. Translate remaining controls to model-specific natural language.
6. Defer suitable controls to postprocess.
7. Emit unsupported/unknown fields unchanged into the loss report.
8. Hash request, references, canonical scene, adapter, and compiler.

## Prompt rendering

Do not dump the entire canonical JSON into a model prompt. Rank details by model evidence and scene salience. A typical rendering order is subject/identity, action and interaction, temporal order, camera, environment, style, facial cues, physics/negative constraints.

## Live probe

A deterministic probe should submit minimal legal requests to test duration, aspect, resolution, reference count/type, seed behavior, audio, response schema, and error messages. It must not infer a capability from one successful artistic output; it tests whether the surface accepts and reports a control.

## Loss report example

```json
{
  "native": ["duration","aspect_ratio","start_image"],
  "reference_conditioned": ["identity","initial_pose"],
  "prompt_only": ["BESS","contact_sequence","camera_move"],
  "postprocess": ["impact_sound"],
  "unsupported": ["explicit_per_frame_FACS"],
  "unknown": ["deterministic_seed_replay"],
  "risk": {"contact_topology": 0.72, "identity": 0.31}
}
```

## Deprecation

Legacy adapters remain readable for experiment reproducibility. They are removed from new compilation targets, not deleted. Migration records link old and replacement adapters.
