# Research Method

## Scope and evidence model

This package executes the uploaded research brief as a **Phase 1 professional evidence and implementation study**. It covers text-to-video, image-to-video, first-frame, first-and-last-frame, reference-conditioned, reference-video, video-to-video, multi-shot, joint audio-video, and pose/depth/mask/trajectory/control-video workflows. It covers realistic, cinematic, UGC, product, dialogue, anime, stylized action, VFX, and multi-actor scenes.

The evidence hierarchy is:

1. repository authority and controlled repository observation;
2. official model papers, technical reports, documentation, API references, model cards, and model repositories;
3. peer-reviewed benchmarks and publications;
4. official benchmark code and disclosed evaluation protocols;
5. recent preprints and controlled independent research, explicitly marked as such;
6. engineering inference with a falsification test;
7. community anecdotes only as experiment hypotheses.

Official documentation is used only for **capability**: accepted inputs, endpoint IDs, durations, resolutions, prompt limits, audio, references, seeds, and documented controls. It is not used as proof of adherence or reliability. Provider showcases and marketing rankings are not counted as reliability evidence.

## Repository-first procedure

The inspected repository is `Kingsley-Cyber/ai-video-movement-prompt-system` at revision `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`. The review mapped ownership before proposing fields. The canonical JSON score, compiler, provider profiles, verification, immutable experiment evidence, and second-brain curation remain the existing authorities. Candidate schemas in this package are research proposals only.

Reviewed files include:

- `AGENTS.md`
- `ARCHITECTURE.md`
- `lab/AGENTS.md`
- `lab/CONTROL_SURFACE.md`
- `lab/FORMAT_CONTROL_MAP.md`
- `lab/UNIVERSAL_MOTION_SKELETON.md`
- `lab/compiler/AGENTS.md`
- `lab/compiler/schemas/universal_score.schema.json`
- `lab/compiler/providers/veo_3_1.yaml`
- `lab/verification/AGENTS.md`
- `lab/verification/schemas/compliance_report.schema.json`
- `lab/second_brain/AGENTS.md`
- `lab/second_brain/IMPLEMENTATION_PLAN.md`

The root `REPO_CONTINUITY_IMPLEMENTATION_PLAN.md` requested by the brief was not found in the inspected tree. The package uses `ARCHITECTURE.md` and `lab/second_brain/IMPLEMENTATION_PLAN.md` as the nearest current owners and records this as an unresolved repository gap rather than silently inventing the missing file.

## Literature and capability procedure

For each model-specific row, the research records provider, model/endpoint, date scope, input modes, durations, output properties, prompt limits, seed semantics, source IDs, and unresolved caveats. The package does not claim 100% verification where an official interface was inaccessible, region-specific, product-only, adapter-mediated, or internally contradictory.

For each failure record, the synthesis records:

```text
trigger conditions
observable symptoms
likely causes and inference status
canonical fields affected
prompt risk patterns
mitigation levels
verification metrics
provider-specific caveats
repository owner
empirical confidence
unresolved questions
```

## What was and was not executed

Executed in this session:

- repository ownership audit;
- primary-source and benchmark synthesis;
- 96-record failure taxonomy;
- provider capability matrix;
- source and claim traceability matrices;
- JSON Schema design and validation;
- repeated-seed experiment designs;
- CPCS compiler, decomposition, verification, and repair recommendations;
- package integrity validation and ZIP generation.

Not executed in this session:

- paid or credentialed commercial provider generation;
- local open-model inference requiring model weights/GPU workflows not supplied to this environment;
- human rating panels;
- seed-level success distributions;
- live CPCS ingestion, curation, promotion, or production-authority changes.

Therefore, provider-specific failure rates, action-density limits, prompt-length sweet spots, mitigation effect sizes, and evaluator thresholds remain **not measured by CPCS**. The experiment fixtures are designed to produce those measurements without changing production authority.

## Statistical design principles

- Use paired arms and identical canonical meaning.
- Use the same seed where the provider exposes a seed, while recognizing that seeds do not guarantee identical artifacts.
- Use at least 20 completed candidates per arm for an initial provider screen and 30+ for open/local models when affordable; expand near decision boundaries.
- Report successes and failures per seed, Wilson intervals for binary criteria, medians and bootstrap intervals for continuous error, and human/evaluator disagreement.
- Pre-register critical assertions and stop conditions before generation.
- Apply correction for multiple comparisons within an ablation family.
- Never discard failed outputs or select only the best render.
- Bind every artifact to the exact request, model/version, provider, seed/retry identifier, assets, evaluator versions, and human verdict.

## Reproducibility boundary

The package is reproducible as a research artifact: schemas, JSONL, CSV, YAML, manifest, checksums, and validation report are generated deterministically from this script. Generative-video outputs remain stochastic and provider-dependent. Reproducibility means preserving the complete attempt and its evidence, not claiming byte-identical regeneration.
