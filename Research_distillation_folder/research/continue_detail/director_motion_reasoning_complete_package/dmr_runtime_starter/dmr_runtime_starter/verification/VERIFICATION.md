# Verification record

Audit and package date: **2026-07-31**  
Repository baseline: `Kingsley-Cyber/ai-video-movement-prompt-system@3db5dcef5f4902ac7343b79a3d9bdae7dc17fc7e`  
Repository writes: **none**

## Recorded checks

```bash
PYTHONPATH=src pytest -q
```

Expected and recorded result: `12 passed`.

```bash
PYTHONPATH=src python3 -m compileall -q src
```

Expected and recorded result: exit code `0`.

```bash
PYTHONPATH=src python3 -m dmr_runtime.cli solve examples/blocked_turning_kick.scene.json
PYTHONPATH=src python3 -m dmr_runtime.cli validate examples/blocked_turning_kick.scene.json
PYTHONPATH=src python3 -m dmr_runtime.cli compile \
  examples/blocked_turning_kick.scene.json \
  contracts/veo-3.1-generate-001.vertex.json
```

Recorded checkpoints:

- STN consistency: `true`.
- Validation errors: `0`.
- Provider contracts parsed by the strict Pydantic model: `5`.
- Example compilation parsed by the strict result model: `true`.
- Veo request candidate uses `instances[0]`, matching the documented array-shaped REST body.
- Required unsupported, unknown, or out-of-limit controls fail closed.
- `product_profile` contracts are rejected as non-executable.
- Source wheel builds successfully with `--no-build-isolation --no-deps`.

## Important boundary

No live video-provider generation call or generated-video round-trip evaluation was performed. The files prove the deterministic Phase-1 control plane only: typed data, temporal consistency, action/state checks, capability classification, request compilation and explicit loss accounting.
