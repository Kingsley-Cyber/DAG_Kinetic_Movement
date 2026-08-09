Act as a principal multimodal AI researcher, computational movement scientist, temporal-reasoning architect, animation systems engineer, knowledge-graph engineer, computer-vision researcher, and AI video-model evaluation lead.

Conduct a deep, source-grounded technical investigation into the remaining research, architecture, implementation, and evaluation gaps in the following repository:

**Repository:** `Kingsley-Cyber/ai-video-movement-prompt-system`

## Primary objective

Determine exactly what is still required to transform this repository from a broad movement-research and structured-prompt knowledge base into a reliable end-to-end **Director Motion Reasoning System** that can:

1. Accept a natural-language request, image, or reference video.
2. Retrieve the correct movement, directing, animation, and cinematography knowledge.
3. Decompose behavior into actors, actions, body regions, phases, contacts, reactions, camera events, editing events, and VFX events.
4. Construct a temporally and physically coherent canonical motion plan.
5. Detect contradictory, impossible, underspecified, or unsupported controls before generation.
6. Compile the canonical plan into the controls actually supported by a specific image or video model.
7. Generate model-specific prompts and conditioning assets.
8. Re-extract the resulting video.
9. Measure whether action order, timing, contact, body mechanics, camera, identity, continuity, and style matched the authored plan.
10. Diagnose failures and modify only the responsible fields.
11. Repeat until the result passes defined acceptance thresholds.
12. Preserve provenance, uncertainty, alternative interpretations, and model-capability loss throughout the pipeline.

The final result must identify what is missing for the system to **work operationally**, not merely what additional terminology or documents could be added.

---

# 1. Repository inspection requirements

Inspect the repository before drawing conclusions.

Read at minimum:

* `README.md`
* `AGENTS.md`
* `SKILL.md`
* `lab/AGENTS.md`
* `lab/CONTROL_SURFACE.md`
* `lab/FORMAT_CONTROL_MAP.md`
* `lab/UNIVERSAL_MOTION_SKELETON.md`
* `lab/CONCEPT_INDEX.md`
* `lab/concepts.jsonl`
* `lab/registry.yaml`
* `lab/blocks.yaml`
* `lab/runs/results.csv`
* `lab/graph.json`
* every `lab/RUNBOOK_*.md`
* `lab/variants/v005_combat_kinematic_json.jsonc`
* `lab/variants/v005_combat_full_authoring.md`
* relevant scripts under `lab/scripts/`
* the CPCS, MX, and Reverse Directorial Compilation research packages under `research/`
* existing schemas, examples, tests, profiles, prompts, validation scripts, and extraction utilities

Search the repository for:

* temporal reasoning
* Simple Temporal Networks
* interval algebra
* constraint solving
* action preconditions and postconditions
* contact
* support
* balance
* center of mass
* foot plant
* kinematic chain
* camera-subject separation
* prompt compiler
* capability contract
* provider adapter
* unsupported controls
* loss report
* round-trip verification
* output re-extraction
* failure diagnosis
* benchmark
* inter-rater reliability
* confidence calibration
* Graph-RAG retrieval evaluation
* persistent scene state
* actor identity continuity
* hand-object interaction
* FACS numeric tracks
* Bartenieff computation
* Laban feature proxies

Distinguish clearly between:

1. Concepts that are documented.
2. Concepts that have executable implementations.
3. Concepts that have been tested.
4. Concepts supported only by one qualitative render.
5. Concepts validated through isolated controlled experiments.
6. Concepts that remain speculative or proposed.

Do not treat the existence of a schema, runbook, prompt, or example as proof that the corresponding system works.

---

# 2. Evidence classification

Throughout the report, label every major claim as one of:

### Established standard

A recognized formalism, specification, scientific framework, or established technical method, such as:

* FACS
* Laban/Bartenieff Movement Studies
* Behavior Markup Language
* biomechanical coordinate systems
* Allen interval algebra
* Simple Temporal Networks
* constraint-satisfaction methods
* RDF, OWL, SHACL, or PROV-O
* established evaluation metrics

### Research-derived parameterization

A computational or numerical operationalization proposed in academic research, such as:

* kinematic proxies for Laban Effort
* contact inference from pose
* camera-motion disentanglement
* phase estimation
* motion-text alignment
* learned motion tokenization
* physical-plausibility metrics

### Project-specific synthesis

A repository-created design, including:

* the CPCS canonical control score
* numeric Laban axes in `[-1,1]`
* the universal motion skeleton
* the harmonic YAML/JSON/XML compiler
* a normalized seven-phase abstraction
* a project-specific screen-combat ontology
* provider capability contracts
* project-specific prompt compression rules

Never present project-specific synthesis as an industry standard.

---

# 3. Core research questions

Investigate each of the following areas deeply.

## A. Target-model capability contracts

Research the current officially documented and empirically demonstrated control surfaces of major video-generation systems, prioritizing:

* Google Gemini/Veo
* Kling
* Seedance
* LTX Video
* Runway
* Sora, when publicly documented
* other significant controllable video-generation systems

For each model, determine whether it supports:

* text prompts
* negative prompts
* image-to-video
* first-frame conditioning
* last-frame conditioning
* reference images
* character-reference controls
* video-to-video
* masks
* pose control
* depth control
* optical-flow control
* motion-brush controls
* camera trajectories
* keyframes
* multi-shot prompting
* seed control
* duration control
* frame rate
* aspect ratio
* audio
* native JSON or structured prompting
* exact timestamps
* frame-count instructions
* contact constraints
* joint trajectories
* identity binding
* extension or continuation

Classify every canonical control as:

```text
native
media-conditioned
semantic-text-only
approximated
unsupported
unknown
```

Design a provider capability-contract schema and a compilation-loss report.

The compiler must never silently discard unsupported controls.

## B. Temporal and causal reasoning

Determine the best formal architecture for converting action descriptions into a valid timeline.

Research and compare:

* Allen interval algebra
* Simple Temporal Networks
* Simple Temporal Networks with Uncertainty
* temporal constraint satisfaction
* event calculus
* PDDL or HTN planning
* behavior trees
* state machines
* temporal knowledge graphs
* probabilistic temporal models

The system must represent constraints such as:

```text
attack initiation precedes parry initiation
parry occurs before strike apex
contact coincides with minimum distance
reaction does not begin before contact
local compression precedes root displacement
camera shake does not begin before impact
recovery follows peak displacement
landing follows flight
a grasp must persist until release
```

Recommend a deterministic temporal solver and provide:

* node types
* edge types
* constraint equations
* uncertainty representation
* conflict detection
* underconstraint detection
* cycle detection
* failure explanations
* serialization format
* example solved timeline

## C. Hierarchical action planning

Research how to decompose:

```text
scene
→ shot
→ beat
→ interaction
→ action
→ phase
→ body-region event
→ joint or effector control
```

Determine whether the repository needs:

* HTN planning
* action grammars
* motion graphs
* behavior trees
* action preconditions and postconditions
* actor-state machines
* interaction protocols
* task-and-motion planning
* causal action graphs

Design an action representation that can detect cases such as:

* the same hand attacks and holds an object simultaneously
* a character kicks before the support foot is planted
* recovery occurs before landing
* a defender reacts before contact
* an actor changes screen side without a crossing event
* an object changes ownership without release and acquisition
* a body region occupies incompatible states

## D. Persistent world and scene state

Design a persistent scene-state model covering:

* actor position
* orientation
* velocity
* stance
* support foot
* guard state
* balance
* held objects
* object ownership
* contact state
* gaze target
* fatigue
* injury or movement limitations
* clothing state
* environment changes
* screen side
* camera side of axis
* shot continuity
* lighting continuity
* VFX residue
* sound state

Research suitable state-transition and validation methods.

## E. Biomechanical feasibility

Research what minimum biomechanical reasoning is needed for believable prompting without pretending that a text prompt is a physics simulator.

Investigate:

* support polygons
* center of mass
* foot contact
* ground reaction
* proximal-to-distal sequencing
* joint range of motion
* limb reachability
* kinematic chains
* momentum
* impulse
* reaction direction
* landing mechanics
* balance recovery
* actor-to-actor collision
* self-collision
* penetration
* hand-object contact
* friction and sliding
* body-proportion normalization

Determine which controls can be:

* calculated deterministically
* estimated from reference video
* authored as qualitative intent
* represented as project-normalized values
* impossible to verify from monocular video

Create a practical feasibility validator for AI-video prompting rather than a full biomechanics simulator.

## F. Contact and interaction reasoning

Develop a complete contact model covering:

* support contact
* touch
* impact
* near miss
* guard contact
* grasp
* sustained hold
* release
* slide
* push
* pull
* brace
* actor-object contact
* actor-environment contact
* occluded contact
* uncertain contact

Each contact should support:

* actor and target
* body or object sites
* start and end
* contact normal
* relative velocity
* minimum distance
* visibility
* support status
* confidence
* reaction reference
* camera presentation
* cinematic cheat allowance
* provenance

Research current contact-aware human-motion and interaction-generation literature.

## G. Motion extraction and calibration

Assess the repository’s current reference-video pipeline and identify what is required to make it reliable.

Research:

* multi-person tracking
* actor re-identification
* pose estimation
* hand tracking
* face and gaze tracking
* 3D body reconstruction
* camera solving
* camera-body motion separation
* root trajectory estimation
* world coordinate recovery
* contact inference
* phase-boundary detection
* action segmentation
* optical flow
* occlusion handling
* uncertainty propagation
* smoothing
* identity swaps
* fast-motion failure
* anime and non-photorealistic pose extraction

Define a gold-standard evaluation protocol using:

* mocap-grounded data
* synthetic rendered data
* controlled filmed data
* multi-person interaction data
* human-object interaction data
* anime or stylized data when available

Recommend metrics such as:

* MPJPE
* root trajectory error
* orientation error
* actor-swap count
* foot-contact F1
* hand-object contact F1
* phase-boundary error
* action-order accuracy
* contact-time error
* confidence calibration

## H. Structured motion description

Research the best intermediate representation between:

```text
dense joint arrays
and
high-level natural-language action labels
```

The representation should describe:

* body region
* trajectory
* direction
* magnitude
* timing
* orientation
* support
* contact
* relation to another actor or object
* phase
* confidence
* evidence

Compare:

* structured motion descriptions
* motion tokens
* pose tokens
* body-part captions
* motion-language models
* graph representations
* event streams
* symbolic motion grammars

Determine what should be computed deterministically before an LLM reasons over the motion.

## I. FACS, Laban, Bartenieff, and affect calibration

Identify where the repository currently uses qualitative frameworks as if they were validated numeric controls.

Research:

* FACS AU intensity normalization
* onset, apex, offset estimation
* identity and morphology normalization
* automated AU reliability
* Laban inter-rater reliability
* computational Laban feature extraction
* Bartenieff connectivity proxies
* phase lag between body regions
* body-part initiation detection
* continuous versus categorical movement-quality controls
* dimensional affect inference
* multimodal disagreement
* cultural and individual variation

For every proposed numeric control, specify:

* whether the scale is canonical or project-specific
* feature derivation
* normalization
* calibration data
* uncertainty
* inter-rater reliability
* limitations
* whether it predicts model output adherence

## J. Camera, editing, VFX, and physical-motion disentanglement

Research how to determine whether perceived motion comes from:

* actor movement
* camera movement
* lens change
* crop or digital zoom
* editing
* time remapping
* impact frames
* motion blur
* smear frames
* camera shake
* sound
* particles
* cloth or hair movement
* environmental reaction

Develop a **perceptual compensation compiler** that can decide:

```text
desired effect
+ physical-motion confidence
+ model capabilities
→ best available combination of body, camera, editing, sound, and VFX controls
```

The system must clearly distinguish:

```text
physically correct
perceptually convincing
cinematically concealed
unsupported
```

## K. Serialization and constrained generation

Compare:

* Markdown plus controlled natural language
* YAML
* JSON
* XML
* JSONL
* grammar-constrained decoding
* function calling
* schema-constrained output
* multi-pass generation

Investigate empirical evidence about whether representation format changes:

* reasoning accuracy
* action-order preservation
* schema validity
* prompt adherence
* model output variance
* token overhead
* truncation risk
* error recovery

Do not assume JSON, YAML, or XML is universally superior.

Recommend whether:

* one canonical format should be authoritative
* YAML and XML should be generated views
* the LLM should reason before serialization
* separate agents should perform authoring, solving, compiling, and validation

## L. Graph-RAG reasoning

Assess whether the existing concept graph and graph traversal are sufficient.

Research:

* ontology-guided retrieval
* temporal subgraph retrieval
* graph query planning
* path retrieval
* contradiction retrieval
* multi-hop retrieval
* provenance-preserving context assembly
* query-aware subgraph extraction
* graph reranking
* learned graph retrievers
* hybrid vector, lexical, and graph retrieval

Create an evaluation framework for questions such as:

* Which constraints apply to a blocked turning kick?
* What must occur before a defender’s reaction?
* Which camera controls compensate for uncertain contact?
* How can the same action be rendered realistically and as original shonen animation?
* Which evidence supports a Laban proxy?
* Which interpretations of a gesture are culturally ambiguous?

Specify:

* node recall
* edge recall
* path recall
* unsupported-node rate
* contradiction recall
* citation accuracy
* answer faithfulness
* token cost

## M. Benchmark and evaluation suite

Design a Director Motion Reasoning Benchmark covering:

1. Natural locomotion.
2. Gesture and dialogue.
3. Facial and gaze behavior.
4. Two-person interaction.
5. Screen combat.
6. Product demonstration.
7. Human-object interaction.
8. Camera-subject coordination.
9. Anime action.
10. VFX-enhanced action.
11. Multi-shot continuity.
12. Prompt compression.
13. Model-capability degradation.
14. Failure diagnosis and repair.

For each scene, provide:

* request
* reference assets
* observations
* gold action graph
* gold temporal constraints
* actor state
* contact graph
* canonical representation
* target-model compilation
* expected loss report
* generated outputs
* automatic measurements
* human ratings
* failure labels

Require controlled A/B testing:

* same model
* same seed where possible
* same reference assets
* one changed variable
* multiple generations per condition
* blinded evaluation
* negative results retained
* confidence intervals

## N. Closed-loop verification and repair

Design the full loop:

```text
canonical target
→ compilation
→ generation
→ re-extraction
→ observed canonical record
→ comparison
→ failure classification
→ minimal patch
→ regeneration
```

Research metrics for:

* action order
* actor assignment
* phase timing
* contact timing
* reaction latency
* foot sliding
* joint discontinuity
* penetration
* trajectory similarity
* camera path
* subject scale
* shot continuity
* identity persistence
* prompt adherence
* style realization

Design a minimal-repair system that modifies only the earliest responsible causal layer.

Examples:

```text
foot sliding
→ support/root constraint

weak impact
→ anticipation, contact pose, reaction delay, audiovisual synchronization

identity swap
→ reference binding or shot decomposition

wrong action order
→ temporal graph

ignored numeric fields
→ capability degradation or alternate control carrier
```

---

# 4. Required evidence standards

Prioritize sources in this order:

1. Official model documentation and API documentation.
2. Formal standards and specifications.
3. Peer-reviewed research papers.
4. Official project repositories and technical reports.
5. University or institutional sources.
6. Reputable secondary analysis only when primary evidence is unavailable.

For every significant claim:

* Cite the source.
* Record publication date.
* Record access date.
* Identify whether it is primary, peer-reviewed, official, or secondary.
* Distinguish documentation from empirical evidence.
* Distinguish a model capability from prompt-engineering speculation.
* Do not rely on search snippets.
* Do not fabricate benchmarks, page numbers, APIs, model features, or standards.
* Mark inaccessible or unverified claims.
* State when something cannot be verified with 100% certainty.

For software, APIs, and current model capabilities, verify the current state at the time the research is performed.

---

# 5. Required final deliverable

Produce a detailed technical report with the following structure.

## 1. Executive verdict

Answer:

* What the repository already does well.
* Why it does not yet “just work.”
* The five most important blockers.
* Whether the main problem is missing knowledge, missing implementation, insufficient evidence, or model limitations.

## 2. Repository maturity matrix

For every subsystem, label it:

```text
documented
schema_only
prototype
partially_exercised
tested
controlled_tested
production_ready
```

Include evidence paths from the repository.

## 3. Gap register

For each gap include:

* Gap ID.
* Description.
* Why it matters.
* Existing repository support.
* Missing research.
* Missing implementation.
* Required data.
* Required tests.
* Dependencies.
* Estimated impact.
* Technical risk.
* Priority.
* Completion criteria.

## 4. Recommended end-to-end architecture

Provide:

* system diagram
* component boundaries
* data flow
* canonical objects
* temporal solver
* state manager
* contact validator
* provider adapters
* compiler
* RAG layer
* generation layer
* evaluator
* repair loop
* provenance flow

## 5. Formal temporal-reasoning design

Include schemas, constraints, examples, failure cases, and solver recommendation.

## 6. Provider capability-contract design

Include a complete example for Gemini/Veo and at least two other models.

## 7. Benchmark design

Include scene categories, annotation protocol, metrics, A/B methodology, and acceptance thresholds.

## 8. Round-trip verification design

Specify exact extraction, comparison, scoring, and repair stages.

## 9. Research agenda

Separate into:

* must research immediately
* should research after the runtime exists
* low-value or premature research
* topics already sufficiently covered

## 10. Implementation roadmap

Provide an ordered roadmap divided into:

### Phase 1: Minimum functioning runtime

* canonical scene object
* action/state model
* temporal solver
* basic validator
* one provider adapter
* compiler loss report

### Phase 2: Measurement and verification

* extraction
* contact inference
* output comparison
* benchmark harness

### Phase 3: Closed-loop repair

* failure classification
* minimal patching
* regeneration

### Phase 4: Advanced reasoning

* calibrated FACS/Laban/Bartenieff
* Graph-RAG retrieval planning
* learned motion representations
* multi-model adapters

For every phase, include observable completion tests.

## 11. Exact repository changes recommended

Provide a proposed directory tree under `lab/`, respecting the repository rule that `research/` is frozen.

Recommend files such as:

```text
lab/runtime/compiler/
lab/runtime/adapters/
lab/runtime/solvers/
lab/runtime/evaluators/
lab/benchmarks/dmr_bench/
lab/schema/
lab/experiments/
```

For each file, describe its responsibility and interfaces.

## 12. Experiment queue

Design at least 15 controlled experiments, including:

* prose versus controlled natural language
* JSON versus YAML versus XML
* temporal solver versus unsolved timeline
* contact constraints versus no contact constraints
* support constraints versus no support constraints
* camera compensation versus physical-only prompting
* keyframe conditioning versus text only
* short prompt versus dense prompt
* one-shot versus shot decomposition
* numeric FACS versus descriptive FACS
* Laban vectors versus qualitative words
* provider-adapter compilation versus generic prompt
* round-trip repair versus manual regeneration
* reference image identity binding
* persistent state versus independent beat generation

## 13. Source matrix

Include:

* source ID
* domain
* authors or organization
* title
* year
* source type
* peer-review status
* URL or DOI
* concepts supported
* reliability
* limitations
* report sections citing the source

---

# 6. Non-negotiable conclusions to test rather than assume

Do not begin with these as predetermined truths. Test them:

* JSON improves choreography.
* XML improves timing.
* YAML improves intent adherence.
* More numerical detail improves generation.
* A video model understands joint coordinates.
* Camera tricks can compensate for invalid biomechanics.
* Laban numeric vectors control movement quality.
* FACS AU tracks improve facial performance.
* a seven-phase abstraction generalizes across domains.
* Graph-RAG improves prompt quality.
* one successful render proves a control method.
* an LLM can judge fine-grained motion accurately.
* re-extraction from generated video is sufficiently reliable for automatic repair.

Identify which of these claims are supported, unsupported, model-specific, or require controlled experiments.

---

# 7. Final question

Conclude with a direct answer:

> What is the minimum technically defensible system that should be built next so that this repository moves from a detailed prompt-research framework into a measurable, model-aware, self-correcting Director Motion Reasoning runtime?

Do not merely recommend more research papers or more prompt templates. Produce a source-grounded technical architecture, gap register, experiment program, and implementation roadmap that can be executed directly in the repository.
