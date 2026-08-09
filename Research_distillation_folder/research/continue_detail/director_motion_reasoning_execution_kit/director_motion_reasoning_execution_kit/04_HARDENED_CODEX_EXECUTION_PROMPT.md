# Hardened Codex / Coding-Agent Execution Prompt

You are operating as a principal research engineer, computational movement scientist, animation systems architect, film-directing systems designer, ontology engineer, knowledge-graph architect, multimodal AI engineer, and prompt-language compiler engineer.

## Repository

Work against:

```text
Kingsley-Cyber/ai-video-movement-prompt-system
```

Create or switch to:

```text
agent/director-motion-reasoning
```

Do not force-push, rewrite history, or modify unrelated code.

## Outcome

Close the verified Director Motion Reasoning gaps in the existing CPCS/CPCS-MX architecture. Do **not** blindly create `research/director_motion_reasoning/`. The repository currently treats `research/` as frozen and already contains overlapping research packages. The default is an incremental, routed, test-backed integration in `lab/` that reuses the existing canonical score, Video Observation Graph, schemas, source indexes, concept corpus, universal skeleton, format map, compiler patterns, and validation control plane.

A new frozen research package is permitted only when all of the following are true:

1. the overlap audit demonstrates a genuinely independent body of work;
2. the owner directive is treated as an explicit override;
3. `AGENTS.md` is updated in the same commit to document the new law;
4. the package has its own source index, schemas, RAG corpus, validators, manifest, and hashes;
5. `sync_repo.py` confirms alias, concept-card, index, and graph coverage.

## Non-negotiable terminology classes

Every material concept and claim must carry one of:

```text
established_standard
research_derived_parameterization
project_specific_synthesis
empirical_repository_finding
unverified
```

Never present project-specific numeric controls as original FACS/Laban/Bartenieff/BML standards. Never claim CAU/CACS is an established universal coding system. Never claim a universal seven-phase movement model unless authoritative evidence establishes one.

## Phase 0 — baseline and governance gate

Read, in order:

```text
AGENTS.md
README.md
lab/AGENTS.md
lab/registry.yaml
lab/CONCEPT_INDEX.md
lab/CONTROL_SURFACE.md
lab/FORMAT_CONTROL_MAP.md
lab/UNIVERSAL_MOTION_SKELETON.md
lab/concepts.jsonl
lab/blocks.yaml
lab/scripts/validate_repo.py
lab/scripts/sync_repo.py
research/CPCS_FACS_Laban_AI_Video_Research_Package_v1.2/README.md
research/CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0/README.md
```

Record:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
python3 lab/scripts/validate_repo.py
python3 lab/scripts/sync_repo.py
python3 lab/scripts/concepts.py stats
```

Write the baseline SHA, branch, gate output, and pre-existing warnings to a temporary work log. Do not call the initial repository state green unless the commands exit zero.

## Phase 1 — overlap and ownership audit

Before creating any file, map every requested capability to one status:

```text
existing_complete
existing_partial
missing
conflicting
obsolete
```

For every non-missing capability, name the existing owner file/schema/script. Enforce:

- extend the owner instead of forking it;
- one concern, one file;
- no `_v2`, `_final`, `_new`, or `_copy` files outside versioned profile/research zones;
- every new file must be routed by `AGENTS.md` or referenced by `registry.yaml` in the same commit;
- derived `lab/graph.json` is never hand-edited.

At minimum, confirm current coverage for CPCS/CPCS-MX research, FACS, Laban, VAD, kinematics, action graph, camera/edit/VFX/marketing, VOG, canonical schemas, RAG, format map, profiles, compiler, examples, and validation.

## Phase 2 — source-grounded delta research

Research only missing/partial areas. Required new domains:

1. **Bartenieff Patterns of Total Body Connectivity**: Breath, Core-Distal, Head-Tail, Upper-Lower, Body-Half, Cross-Lateral.
2. **Behavior Markup Language / SAIBA**: speech, gaze, gesture, posture, face, head, synchronization, realization layers, exact conformance status.
3. **Temporal-model comparison**: FACS, gesture, gait, BML, animation, biomechanics/motor control, action segmentation.
4. **EmotionML alignment** for dimensions, confidence, modalities, timing, traces, and observer/context.
5. **PROV-O, SHACL, and temporal ontology** as optional graph mappings.
6. **Empirical format effects** across Markdown/plain text, YAML, XML, JSON, and constrained outputs.
7. **Closed-loop authored-vs-generated verification**.

Use primary/official sources first. Maintain stable source IDs and claim-source coverage. Do not copy proprietary FACS manual content. Record direct evidence separately from synthesis.

### Mandatory seven-phase verdict

Investigate whether a universal seven-phase movement model exists. Expect different domain models and do not force convergence. If no universal standard is verified, state exactly:

```text
No single authoritative universal seven-phase human-movement model was verified across the reviewed domains.
```

Then create a **project-specific normalized phase profile**, not a standard. Distinguish it from BML's common seven synchronization points around behavior realization.

Recommended normalized profile:

```text
baseline_intent
preparation_loading
anticipation
initiation
execution_acceleration
apex_contact_hold
recoil_recovery_settle
```

Support domain-specific aliases, optional phases, split/merge rules, interruption, cyclic actions, and overlapping local phases. Do not impose it on gait/FACS/BML records where native phases are more informative; store native and normalized mappings together.

## Phase 3 — active integration design

Reuse the existing canonical model. Add backward-compatible modules, preferably under active `lab/` ownership.

### A. Body connectivity module

Required fields:

```text
connectivity_id
pattern_id
canonical_name
aliases[]
knowledge_type
actor_ref
interval/timebase
initiation_region
participating_regions[]
propagation_path[]
propagation_direction
phase_lag[]
proximal_distal_order[]
contralateral_pairs[]
joint_chain[]
support_state
weight_shift
center_of_mass_effect
observable_proxies[]
proxy_method
units/normalization
confidence
uncertainty
source_evidence[]
alternative_interpretations[]
```

### B. BML alignment module

Required fields:

```text
behavior_id
modality
canonical_event_refs[]
bml_profile/version
bml_element_or_extension
sync_points{}
external_sync_refs[]
realization_status
conformance_level: aligned | profile_validated | extension | not_conformant
losses[]
provenance
```

Do not emit `profile_validated` without an observed validator result.

### C. Phase-profile module

Required fields:

```text
profile_id
display_name
knowledge_type=project_specific_synthesis
native_domain
native_phases[]
normalized_phases[]
mappings[]
optional_phases[]
merge_rules[]
split_rules[]
cyclic_policy
interruption_policy
overlap_policy
confidence
sources[]
```

### D. Transformation record

Every conversion/reasoning/compile step records:

```text
transformation_id
input_refs[]
input_hashes[]
output_refs[]
output_hashes[]
method
implementation_version
model/version if used
timestamp
fields_preserved[]
fields_transformed[]
losses[]
warnings[]
validation_results[]
```

## Phase 4 — graph architecture

Keep two graph families separate:

1. **Knowledge graph**: concepts, sources, evidence, blocks, profiles, variants, experiments, runbooks, papers.
2. **Scene/VOG graph**: source media, shots, frame ranges, actors, body parts, objects, observations, actions, phases, contacts, camera, edit, affect interpretations, prompt projections, contradictions.

Bridge them with explicit `USES_CONCEPT`, `ALIGNED_TO_STANDARD`, `COMPILED_WITH_PROFILE`, and `SUPPORTED_BY_SOURCE` records. Do not reuse IDs across graph families without namespace prefixes.

Optional RDF mapping may use PROV-O/SHACL/temporal vocabularies, but canonical JSON remains authoritative and must not require an RDF stack.

## Phase 5 — format compiler

Canonical resolved JSON is the semantic source of truth.

Implement deterministic projections:

```text
JSON -> YAML
JSON -> XML
JSON -> JSONL
JSON -> Markdown/CNL
```

Then implement parsers back to a normalized semantic object where feasible.

Rules:

- preserve stable IDs, actor/object refs, timebase, temporal values, order, units, confidence, provenance, alternatives, and constraints;
- arrays/sequences preserve order; do not rely on mapping key order for semantics;
- XML uses namespaces and hash references rather than duplicating dense numerics;
- YAML uses safe parsing and no executable/custom tags;
- JSONL defines exact framing, revision, supersedes/correction, and tombstone semantics;
- Markdown is a projection and must embed stable IDs sufficient for traceability;
- every serializer emits a loss report;
- semantic equivalence uses normalized typed values and hashes, not byte equality.

## Phase 6 — examples

Create one canonical fixture per requested scene and generate all projections programmatically:

1. cautious room entry, recognition, relaxation, greeting;
2. conversational gesture with gaze/posture/affect transition;
3. walk → sudden stop → turn;
4. staged hand-to-hand screen action using near-contact/safety semantics;
5. original shonen-style transform of the same action;
6. live-action VFX transform of the same action;
7. UGC product-size demonstration;
8. structural transfer to a different product with identity/brand replacement;
9. dialogue performance combining face, Laban, VAD, camera, edit, and audio timing.

For each fixture preserve evidence, canonical representation, graph mapping, five projections, long prompt, budget-constrained prompt, image keyframe prompt, image-to-video prompt, validation result, and a generated information-loss report.

Do not hand-maintain five divergent semantic copies.

## Phase 7 — validation and tests

Add tests for:

- JSON Schema Draft 2020-12;
- YAML safe parse/type preservation;
- XML well-formedness, XSD/profile validation, namespaces, and XXE rejection;
- JSONL line validation, unique IDs, revisions/supersedes;
- monotonic time/frame ranges;
- normalized values and units;
- phase overlap/merge rules;
- Bartenieff canonical IDs/aliases/proxy metadata;
- BML sync references and conformance labels;
- reference resolution;
- provenance on every derived claim;
- observation versus interpretation separation;
- scene graph versus knowledge graph namespaces;
- cross-format semantic hashes and loss reports;
- internal Markdown links and source IDs;
- source-claim coverage;
- target adapter capability/loss reports;
- character-budget compression retaining locked fields;
- safety/rights/protected-trait rules.

Use existing dependencies where possible. Add only the smallest justified development dependency and document it.

Run and record exact output:

```bash
python3 lab/scripts/concepts.py validate
python3 lab/scripts/build_graph.py
python3 lab/scripts/sync_repo.py
python3 lab/scripts/validate_repo.py
pytest -q
git diff --check
```

Run package-specific validators when touched. Run the root gate **after all final edits**. A prior green run is not evidence that the final tree is green.

## Phase 8 — integration bookkeeping

- Add at least three natural-language triggers for each new concept card.
- Update `CONCEPT_INDEX.md`, `CONTROL_SURFACE.md`, `FORMAT_CONTROL_MAP.md`, and `UNIVERSAL_MOTION_SKELETON.md` only where the new concept changes their responsibilities.
- Add a new runbook only if there is a repeatable operational workflow; route it in `lab/AGENTS.md` in the same commit.
- Add registry pointers for every new active artifact.
- Regenerate `lab/graph.json` last.
- Append one `CHANGELOG.md` line in the same commit.
- Use the repository's owner identity and required co-author convention.

## Git completion

Before commit:

```bash
git status --short
git diff --check
python3 lab/scripts/validate_repo.py
```

After commit/push:

```bash
git rev-parse HEAD
git status --short
git ls-remote origin refs/heads/agent/director-motion-reasoning
```

Success requires the remote branch SHA to equal the local SHA and the working tree to be clean. Do not report a push, commit, or green gate unless the command output proves it.

## Final response contract

Return:

1. baseline branch/SHA and initial gate result;
2. overlap audit summary;
3. exact files changed/created/deleted;
4. established frameworks added or aligned;
5. project-specific syntheses introduced;
6. explicit universal-seven-phase verdict;
7. source counts by type/status;
8. schema/compiler/graph changes;
9. examples generated;
10. exact validation commands and outputs;
11. unresolved or inaccessible claims;
12. limitations and safety boundaries;
13. git diff summary;
14. commit SHA and verified remote branch SHA;
15. next implementation experiment, prioritizing closed-loop verification.

Do not stop at a plan. Execute the repository work, but remain gap-first and evidence-bound.
