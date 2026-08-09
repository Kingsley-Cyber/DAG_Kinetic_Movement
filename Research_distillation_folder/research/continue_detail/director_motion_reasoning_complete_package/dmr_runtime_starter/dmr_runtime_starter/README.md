# DMR Runtime Starter

**Version:** 0.1.0  
**Purpose:** Minimum technically defensible control-plane runtime for the `Kingsley-Cyber/ai-video-movement-prompt-system` repository.  
**Scope:** deterministic authoring validation, temporal solving, provider capability negotiation, and compilation-loss reporting.  
**Non-goals:** full biomechanics simulation, dense motion synthesis, claiming hidden controls, or autonomously judging generated video.

## Why this package exists

The repository already contains a large movement/directing knowledge base, canonical-schema research, extraction utilities, runbooks, and a reference YAML-to-JSON compiler. What it does not yet contain is one executable path that can answer all of the following before a generation call:

1. Is the authored timeline internally consistent?
2. Are actor, object, contact, and body-region states compatible?
3. Which controls does the exact provider/model/API surface actually accept?
4. Which requested controls are converted to semantic text, approximated, unsupported, or unknown?
5. Did compilation silently discard anything?

This starter implements that path without claiming that a video model natively consumes joint tracks, contact constraints, FACS curves, Laban vectors, or an STN.

## Included components

```text
src/dmr_runtime/
├── models.py          strict Pydantic canonical objects and result types
├── temporal.py        deterministic Simple Temporal Network solver
├── validation.py      state/resource/contact/causal validators
├── capabilities.py    pinned provider-contract loader
├── compiler.py        prompt/request compiler with complete loss accounting
└── cli.py             solve, validate, and compile commands

contracts/
├── veo-3.1-generate-001.vertex.json
├── runway-gen4.5.api.json
├── seedance-2.0-modelark.api.json
├── ltx-video-0.9.8.local.json
└── kling-video-3.0-omni.product.json

examples/
├── blocked_turning_kick.scene.json
├── blocked_turning_kick.solved.json
└── blocked_turning_kick.veo.compilation.json

schemas/
├── scene-plan.schema.json
├── provider-capability-contract.schema.json
└── compilation-result.schema.json

tests/
├── test_temporal.py
├── test_validation.py
└── test_compiler.py
```

The Kling file is intentionally labeled `product_profile`, not `api`: accessible official documentation verifies product-level capability, but the exact public API request schema could not be verified with 100% certainty. The compiler rejects product profiles as non-executable.

## Install and verify

```bash
cd dmr_runtime_starter
python3 -m venv .venv
source .venv/bin/activate       # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[test]'
pytest -q
```

Expected checkpoint:

```text
12 passed
```

A nonzero test exit code means the package is not safe to integrate.

## Solve a timeline

```bash
dmr-runtime solve examples/blocked_turning_kick.scene.json \
  > work/blocked_turning_kick.solved.json
```

Verification checkpoints:

- `consistent` must be `true`.
- `conflict` must be `null`.
- `underconstrained_points` should be empty for a fully pinned benchmark scene.
- Contact and reaction times should satisfy the authored bounds.

The STN accepts constraints of the form:

```text
min_delta_s <= time(right_point) - time(left_point) <= max_delta_s
```

It detects contradictions as negative cycles and returns the responsible constraint IDs. It reports points lacking finite two-sided bounds relative to the scene origin.

## Validate action and state coherence

```bash
dmr-runtime validate examples/blocked_turning_kick.scene.json
```

The current validator checks:

- action intervals and scene bounds;
- overlapping body/effector resource locks;
- reaction-after-contact ordering;
- recovery-after-source-action ordering;
- support, held-object, grounded/airborne, and screen-side preconditions;
- deterministic end effects such as support changes and object acquisition/release;
- contact interval validity and whether geometric evidence is absent.

It returns `error`, `warning`, or `unknown` rather than turning missing evidence into a fabricated pass.

## Compile against a pinned capability contract

```bash
dmr-runtime compile \
  examples/blocked_turning_kick.scene.json \
  contracts/veo-3.1-generate-001.vertex.json \
  --output work/blocked_turning_kick.veo.json
```

Verification checkpoints:

- Every `control_requests[]` entry must appear exactly once in `loss_report`.
- Native controls must land in an explicit provider request field, unless the contract identifies a fixed model setting.
- Media-conditioned controls must identify their asset carrier.
- Semantic-only or approximated controls must retain a residual-risk statement.
- A required `unsupported` or `unknown` control must fail closed.

To inspect a failure report without hiding its severity:

```bash
dmr-runtime compile SCENE CONTRACT --allow-required-loss
```

The result still has `hard_failure: true`; this option is for diagnostics, not production execution.

## Capability classification

Each canonical control is classified as exactly one of:

```text
native
media-conditioned
semantic-text-only
approximated
unsupported
unknown
```

A contract is valid only for the exact tuple:

```text
provider + API surface + model ID/checkpoint + version/date + region/workflow
```

Do not merge capabilities across different surfaces. For example, Google’s exact Vertex/Agent Platform `veo-3.1-generate-001` page marks sound generation unsupported, while the Gemini API preview page documents video with audio. Those require separate contracts.

## Integration into the repository

Respect the repository rule that `research/` is frozen. Promote implementation into `lab/`:

```text
lab/
├── runtime/
│   ├── models/
│   ├── solvers/
│   ├── validators/
│   ├── compiler/
│   ├── adapters/
│   └── provenance/
├── schema/
│   ├── scene_plan.schema.json
│   ├── provider_capability_contract.schema.json
│   └── compilation_result.schema.json
├── benchmarks/dmr_bench/
├── experiments/
└── tests/runtime/
```

Recommended promotion sequence:

1. Copy the tested modules into `lab/runtime/`.
2. Reconcile names with the frozen CPCS-MX schema; do not fork equivalent concepts.
3. Add `lab/scripts/dmr_runtime.py` as the stable CLI entry point.
4. Register new runtime files in `lab/registry.yaml` and routing documentation.
5. Extend `validate_repo.py` to run the runtime unit tests and provider-contract schema checks.
6. Run `python3 lab/scripts/sync_repo.py --fix`.
7. Run `python3 lab/scripts/validate_repo.py` after all edits; only a final green exit code is acceptable.

## Deliberate limitations

This package does not yet:

- infer 3D pose, camera motion, contact, gaze, FACS, or Laban features;
- solve inverse kinematics, dynamics, center of mass, or ground-reaction force;
- invoke any generation provider;
- compare a generated video to the canonical target;
- calibrate confidence or human-rater agreement;
- perform minimal causal repair after output evaluation;
- implement vector/graph retrieval.

Those are Phase 2–4 work. Adding placeholder class names for them would not make the system operational.

## Reproducibility record

Generated and tested on Python 3.13.5 with Pydantic 2.13.4 and pytest 9.0.2. Provider contracts were researched on July 31, 2026 and must be reverified before production use because video-model APIs change rapidly.
