# CPCS Integration Recommendations

## Architectural verdict

The repository already has the correct top-level control plane: one canonical universal score, one compiler/provider-build boundary, one render-verification owner, one immutable experiment/evidence path, and a human-curated second brain. The failure research should **extend those owners**, not add a failure compiler, separate ontology, or second canonical score.

The inspected architecture explicitly treats the fully resolved JSON score as semantic authority. Provider prompts and requests are projections; research and derived evidence cannot silently mutate curated truth. These laws should remain unchanged.

## Minimal candidate extensions

| Candidate extension | Existing owner | Purpose | Classification | Promotion gate |
| --- | --- | --- | --- | --- |
| continuity.state_ledger | universal score continuity | Persistent existence, visibility, count, possession, material/object state, irreversible deltas, terminal state | contract_affecting | schema review + compiler fixture + verifier |
| continuity.visibility_intervals | universal score continuity | Occlusion start/end, hidden path, reappearance region, visibility bridge, permitted/forbidden state changes | contract_affecting | occlusion ablation + artifact-bound verification |
| continuity.identity_ledger | entities + continuity | Identity signatures, role, voice, costume, body proportions, screen/depth lane history | contract_affecting | identity fixtures + human-calibrated metric |
| continuity.spatial_state | scenes/shots/camera | Coordinate frames, world/screen/depth transitions, axis and eyeline state | contract_affecting | spatial fixtures + camera calibration |
| actions.event_graph | beats/actions | Ordered events, dependencies, cause/effect, onset/apex/reaction/recovery | contract_affecting | topological validation + temporal evaluator |
| interactions.contact_support | interactions/motion | Contact type, target region, distance/separation, support foot, base of support, permitted near-contact cheat | contract_affecting | measured + human lane |
| interactions.material_response | interactions/style/continuity | Material type, impact origin, displacement, topology invariants, effect lifetime | contract_affecting | material-specific fixtures |
| camera.explicit_tracks | camera + motion | Separate camera translation/rotation/lens from actor world/screen motion | implementation_affecting | camera/actor ablation + estimator calibration |
| editing.discontinuity_contract | editing + continuity | Distinguish cut, flash, smear, hold, blur, wipe, occlusion, and world-state reset | contract_affecting | effect-vs-cut fixtures |
| style.deformation_recovery | style + motion + continuity | Authored deformation interval, silhouette anchors, maximum exposure, required anatomy recovery frame | contract_affecting | anime-specific human calibration |
| audio.event_anchors | audio + actions/beats | Bind sound/speech/music events to visual event IDs and time windows | contract_affecting | AV-sync fixtures |
| verification.failure_assertions | lab/verification | Failure ID, interval, observable lane, metric/version, threshold, conflicts, human requirement | verification_affecting | evaluator qualification |
| provider capability generalization | lab/compiler/providers | Version-scoped modes, references, controls, prompt limits, seed/rewrite behavior, audio, edit modes | provider_version_affecting | official docs + one live canary + replay evidence |
| failure/mitigation evidence objects | lab/second_brain | Curated failure concepts, immutable provider observations, derived mitigation ranking | knowledge_only then implementation_affecting | distill + human curation + isolated comparisons |

## Repository overlap result

`REPOSITORY_OVERLAP_MATRIX.csv` maps every one of the 96 failure records to an existing owner. All rows are currently `partial`: the repository has a location for the meaning, but not complete versioned failure contracts, metrics, repeated-seed evidence, and provider-specific mitigation distributions.

The missing requested root `REPO_CONTINUITY_IMPLEMENTATION_PLAN.md` is recorded as an unresolved repository gap. This package does not create a replacement because doing so could establish a parallel or obsolete plan without owner confirmation.

## Integration sequence

### Phase 0 — Ingest as non-authoritative research

- Register `SOURCE_CATALOG.csv`, `CLAIM_SOURCE_MATRIX.csv`, and selected Markdown passages through the existing source-extraction/distillation path.
- Stage failure concepts, mechanism claims, metric methods, and provider capability candidates.
- Preserve source IDs, dates, locators, confidence, and limitations.
- Do not promote machine-generated records automatically.

### Phase 1 — Add typed candidate fields behind the universal score

- Extend only existing score objects.
- Add closed JSON Schema definitions and field-specific merge operators.
- Add migration/adaptation only where existing fixtures require it.
- Fail on unknown/conflicting fields; never generic-recursive-merge continuity state.
- Keep provider strings and prompts out of the score.

### Phase 2 — Compile and report loss

- Add one provider at a time through the existing capability-profile owner.
- For every canonical field, emit `supported_native`, `compressed_to_text`, `delegated_to_asset`, `evaluation_only`, or `unsupported`.
- Make prompt overflow and hard-lock loss fatal.
- Capture provider-side prompt enhancement/rewrite settings.

### Phase 3 — Implement the minimum verifier set

Start with the highest-value deterministic or human-calibratable checks:

1. actor/object count and existence;
2. identity/role checkpoints around cuts and occlusions;
3. event order and effect origin;
4. screen side, reappearance region, and target region;
5. object possession/state transitions;
6. contact/penetration with explicit human review;
7. flash-vs-cut and recovery-frame assertions;
8. audio-event onset offsets.

Each metric must record evaluator/version/configuration, artifact hash, lane, blind spots, threshold policy, and human-calibration status.

### Phase 4 — Run sealed repeated-seed experiments

- Use the YAML fixtures in `experiments/`.
- Prepare exact canonical builds before sealing.
- Isolate one control difference per causal comparison.
- Record every candidate, failed output, cost, latency, and verdict.
- Reflect provider/model-conditioned mitigation weights only after immutable evidence exists.

### Phase 5 — Learn bounded routing, never truth

Derived evidence may recommend:

```text
failure family + provider/model/version + task complexity
→ cheapest mitigation level with acceptable success distribution
```

It may not rewrite canonical truth, override hard locks, or promote a provider marketing claim. Human authority remains the promotion gate.

## Acceptance checks for implementation

```bash
python3 -m lab.compiler.score validate
python3 -m lab.compiler.build validate
python3 -m lab.verification.verify validate
python3 -m lab.second_brain.src.validate schemas
python3 -m lab.second_brain.src.validate control-plane
python3 -m unittest discover -s lab/compiler/tests -p "test_*.py"
python3 -m unittest discover -s lab/verification/tests -p "test_*.py"
python3 -m unittest discover -s lab/second_brain/tests -p "test_*.py"
```

New tests should prove that the same canonical target produces stable semantic projections, hard locks cannot be dropped, unknown provider controls become explicit loss, evaluator conflicts remain unresolved, and `rm -rf lab/second_brain/derived` rebuilds byte-identically.
