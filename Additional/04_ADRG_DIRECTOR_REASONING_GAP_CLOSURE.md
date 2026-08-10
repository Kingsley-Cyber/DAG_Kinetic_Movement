# 04_ADRG_DIRECTOR_REASONING_GAP_CLOSURE — Research-to-Runtime Closure

**Status:** Research closure complete  
**Scope:** CPCS Adaptive Director Reasoning Graph (ADRG)  
**Target:** `Kingsley-Cyber/ai-video-movement-prompt-system`  
**Primary research corpus:** `CPCS-ADRG-RP-2026-01` + `CPCS_ADRG_RAG_Corpus.jsonl`  
**External verification cutoff:** 2026-08-08  
**Repository changes:** None

---

## 0. Executive result

### BLUF

ADRG does **not** justify adding another reasoning/orchestration framework to CPCS.

The current CPCS already has a governed reasoning-policy layer and six registered reasoning policies/executors. The actual remaining gap is one layer above those executors:

> **CPCS has reasoning methods; it does not yet have a compact, first-class semantic representation of the director decisions those methods are supposed to resolve.**

The highest-value closure is therefore:

```text
existing reasoning policy
        ↓
ADRG Decision IR / execution graph
        ↓
decision records + alternatives + invariants
        ↓
existing compiled_directing_strategy
        ↓
existing universal score/compiler
        ↓
provider capability negotiation
        ↓
existing verification / render evidence
```

Do **not** build a second agent framework, second scene ontology, second compiler, or second durable knowledge graph.

### Five concrete additions

1. **DirectorProblem / DecisionRecord / DecisionOutcome / Candidate / DecisionConstraintSet / Criterion / EvaluationRecord / ExpectedEffect objects** at reasoning-runtime level.
2. **Typed execution edges and append-only ExecutionEvents** for support, contradiction, proposal, selection, rejection, dependency, invalidation, verification, compilation, supersession, and repair — without polluting the existing authored knowledge-edge ontology.
3. **Decision-aware routing features** represented as typed/decomposed impact, uncertainty, coupling, reversal-cost, validator-capability, and budget features rather than uncalibrated 0–1 scores.
4. **Explicit active/compressed/decision/failure state projections** derived from immutable execution history, with semantic-equivalence contraction and dependency invalidation rules.
5. **DecisionProjection + bounded repair + compile-loss + verification linkage** so ADRG selects governed concepts/mappings for the existing compiler, while failures are attributed before any semantic mutation and repair may patch, regenerate, recarrier, split, switch provider, escalate, or accept loss.

The existing compiler, translation registry, provenance, graph builder, policy registry, and validator infrastructure should remain the authorities.

---

# 1. Evidence basis and classification

The master protocol requires a research-to-representation closure rather than a literature summary. It explicitly requires:

```text
frozen research
→ primary-source verification
→ missing semantic detail
→ measurement definition
→ representation design
→ JSON/YAML/XML/NL examples
→ canonical CPCS mapping
→ compiler behavior
→ provider-facing meaning
→ verification metrics
```

This closure follows that structure.

The ADRG prompt defines the target gap as the representation of decisions, alternatives, evidence, constraints, causal structure, and compiler consequences, while explicitly saying not to create another orchestration framework if the current reasoning-policy infrastructure already covers that role.

The ADRG research package is available in the project library. Its README identifies the package contents as including the reasoning-graph schema, policy examples, canonical graph examples, compiler examples, concept cards, integration plan, and validation scripts. The package explicitly says raw chain-of-thought is not a canonical artifact and instead uses typed task/evidence/candidate/decision/compilation/validation/failure/repair records.

### Evidence classes used here

| Label | Meaning |
|---|---|
| `PACKAGE_ESTABLISHED` | Directly established by the supplied ADRG research package. |
| `REPO_OBSERVED` | Directly observed in the current CPCS repository. |
| `EXTERNAL_ESTABLISHED` | Supported by an external primary/authoritative source. |
| `PROPOSED_CPCS` | Recommended representation for CPCS. |
| `EXPERIMENTAL` | Must be calibrated in the target repository/model stack. |

---

# 2. Executive gap closure

## 2.1 What the ADRG research already establishes

The package already establishes the architectural direction:

- ADRG is above the scene-control/compiler layer.
- It represents planning as typed nodes and edges.
- It separates knowledge/evidence, scene intent/control, reasoning execution, compilation/realization, and verification/experiments.
- Branching is selective rather than global.
- Mini models should use narrow fixed graphs and external validation.
- Larger models can use selective branching and graph aggregation.
- Raw chain-of-thought should not become canonical evidence.
- Natural language, YAML, JSON, XML, and JSONL have distinct semantic ownership.
- Compilation must produce explicit loss records.
- Render evidence is required before promoting a reasoning policy as causally useful.
- The research package already contains a JSON Schema for ADRG.

The package's conclusion is that the important question is not whether CPCS should use CoT, ToT, or GoT globally, but which operator should resolve a given decision under the current model, budget, evidence, and verification regime.

## 2.2 What CPCS already implements

The current repository already has:

- six reasoning policies and a registered executor for each;
- deterministic policy selection and replay tests;
- ephemeral reasoning execution rather than mutation of canonical authority;
- a live derived graph and Neo4j projection;
- a canonical score compiler;
- deterministic control-translation records;
- provenance/hashing;
- profile/constraint/merge handling;
- capability-aware control translation;
- schema validation;
- compile-loss dispositions;
- knowledge-lens binding;
- candidate concept/mapping admission;
- a separate compiler/verifier boundary.

The current tests explicitly require six reasoning policies and executor-registry alignment, and verify deterministic replay without authority mutation.

The compiler already validates that a directing strategy admits only concepts and mappings present in the selected context, and it binds the strategy to normalized intent/context hashes and knowledge-lens hashes.

## 2.3 What is still missing

### Gap A — Decision semantics

Current policy execution can produce a strategy, but the reasoning layer does not yet have a sufficiently rich first-class representation of:

```text
problem
evidence
inference
creative choice
candidate treatment
constraints
invariants
alternatives
decision
consequences
verification
```

The ADRG schema contains these concepts indirectly, but the current CPCS runtime needs a clean bridge into its existing strategy contract.

### Gap B — Candidate comparison

The current method layer can execute ToT/GoT-style operations, but the durable semantic unit is not yet:

```text
question
→ candidates
→ criteria
→ constraints
→ selected
→ rejected reasons
→ expected consequences
```

That is the missing decision IR.

### Gap C — Decision-aware routing

The existing policy layer routes by task complexity/type. ADRG requires routing based on the properties of the **decision itself**:

```text
impact
uncertainty (decomposed)
coupling
reversal_cost / dependency_commitment
validator_capability
budget
```

These should be typed/decomposed routing features, not uncalibrated scalar scores and not a replacement policy framework.

### Gap D — Explicit state contraction

CPCS has atomic/dependency-style reasoning execution, but does not yet expose a durable contract separating:

```text
active_state
compressed_state
source_memory
decision_memory
failure_memory
```

This matters because context can be contracted without losing the ability to audit why a decision was made.

### Gap E — Causal design chain

CPCS has controls and mappings, but ADRG needs an explicit design-causality chain:

```text
problem
→ treatment
→ decision
→ control
→ expected visual effect
→ observable verification
```

This must not be confused with an empirical scientific causal claim.

### Gap F — Failure-to-decision linkage

The compiler already has deterministic validation and loss handling. ADRG needs to connect:

```text
failure
→ likely responsible layer
→ affected decision/control
→ minimal repair
→ recompile
→ reverify
```

This should reuse the existing validator/compiler rather than creating a new repair subsystem.

---

# 3. Primary-source verification

The package's reasoning-method claims were independently checked against foundational sources.

## 3.1 Reasoning operators

- Chain-of-Thought: Wei et al., 2022.
- Least-to-Most: Zhou et al., 2022/ICLR 2023.
- Self-Consistency: Wang et al., 2022.
- Tree-of-Thoughts: Yao et al., 2023.
- Graph-of-Thoughts: Besta et al., 2023.
- ReAct: Yao et al., 2022.
- Self-Refine: Madaan et al., 2023.
- Unfaithful CoT: Turpin et al., 2023.

The external evidence supports the narrow architectural conclusion:

- reasoning methods are useful operators with different costs;
- decomposition, branch search, aggregation, tool use, and iterative refinement are distinct capabilities;
- self-generated explanation is not reliable evidence of the true causal basis of a model output;
- external validation is therefore required for hard structural/semantic claims.

## 3.2 Provenance

W3C PROV provides a useful conceptual basis for keeping entities, activities, agents, derivations, and provenance distinct. CPCS does not need to implement PROV wholesale; the relevant lesson is to preserve provenance as a first-class relationship rather than treating a generated explanation as causal evidence.

## 3.3 JSON Pointer / JSON Patch

RFC 6901 defines JSON Pointer for precise addressing into JSON documents. RFC 6902 defines JSON Patch and includes the `test` operation, which is directly suitable for base-state protection before applying a repair.

Therefore:

```text
repair proposal
→ JSON Patch
→ test expected base
→ apply
→ validate
```

is standards-aligned.

## 3.4 JSON Schema

JSON Schema is appropriate for structural validity:

```text
types
required fields
enums
ranges
conditional structure
references
```

It cannot establish that a directorial decision is aesthetically correct, causally effective, or perceptually successful.

CPCS should therefore retain the package's four-level verification separation:

```text
structural → schema
semantic    → graph/domain rules
perceptual  → metrics/human review
empirical   → controlled render comparison
```

---

# 4. Semantic representation specification

## 4.1 Recommended ownership

| Concept | Recommended form | Authority |
|---|---|---|
| problem | node/record | ADRG execution |
| evidence | reference to evidence/source record | knowledge/evidence |
| inference | decision-local record | ADRG execution |
| creative_choice | candidate/decision payload | ADRG execution |
| candidate_treatment | node | ADRG execution |
| constraint | existing CPCS constraint + ADRG reference | compiler/constraint authority |
| invariant | typed invariant record | ADRG execution + compiler |
| alternative | candidate node | ADRG execution |
| decision | `DecisionRecord` + decision node | ADRG execution |
| consequence | typed edge/record | ADRG execution |
| verification | validation/metric node | verification plane |
| compilation | existing compiler artifacts | compiler |
| provider capability | existing adapter/profile authority | provider adapter |
| evidence provenance | source IDs/digests | provenance layer |

### Key rule

Do not make every item a Neo4j node merely because it can be represented as a node.

The durable knowledge graph should contain only reusable knowledge. Per-request decision state belongs in the execution graph/state and may be persisted as an audit record.

---

# 5. Proposed Director Decision IR

The minimum semantic decision family is no longer a single record with an unexplained score matrix. The hardened contract separates the decision, its scope, constraints, candidate evaluations, assumptions/gaps, outcome, and projection. Section 26 defines the normative full contract.

A compact decision instance is:

```json
{
  "decision_id": "dec.camera.treatment",
  "problem_id": "problem.action_readability",
  "mode": "branched_creative",
  "decision_type": "semantic_directorial",
  "decision_domain": "camera",
  "scope": {
    "scene_id": "scene_07",
    "shot_id": "shot_03"
  },
  "constraint_set_ref": "constraints.camera.001",
  "candidate_ids": [
    "cand.low_tracking",
    "cand.telephoto",
    "cand.handheld"
  ],
  "criterion_ids": [
    "criterion.action_readability",
    "criterion.subject_visibility",
    "criterion.continuity",
    "criterion.generation_reliability"
  ],
  "evaluation_ids": [
    "eval.low_tracking.readability",
    "eval.low_tracking.visibility",
    "eval.low_tracking.continuity"
  ],
  "assumption_ids": [
    "asm.single_actor_visibility"
  ],
  "unresolved_gap_ids": [
    "gap.target_specific_camera_adherence"
  ],
  "outcome_ref": "outcome.camera.001",
  "expected_effect_ids": [
    "effect.camera.action_readability"
  ],
  "provenance": {
    "procedure": "bounded_candidate_search",
    "executor": "tree_of_thoughts",
    "source_event_ids": ["evt://..."]
  }
}
```

The selected disposition lives in `DecisionOutcome`, not an overloaded `selected` field:

```json
{
  "outcome_id": "outcome.camera.001",
  "decision_id": "dec.camera.treatment",
  "status": "selected",
  "selected_candidate_id": "cand.low_tracking",
  "selection_basis": [
    "eval.low_tracking.readability",
    "eval.low_tracking.visibility"
  ],
  "unresolved_refs": [
    "gap.target_specific_camera_adherence"
  ],
  "strategy_projection_ref": "projection.camera.001"
}
```

### What it does not mean

A selected candidate does not mean rendered success.

Evidence references establish provenance and scoped support; they do not become truth merely by being cited.

A numeric evaluation is not permitted unless its scale, evaluator, basis, and calibration are explicit. Until then use typed/categorical results such as `high`, `medium`, `low`, or `unknown`.

A provider-realization decision may approximate the selected creative intent but may not overwrite the semantic-directorial decision.

Raw chain-of-thought is not part of the canonical Decision IR.

---

# 6. Decision graph

## 6.1 Execution-only edge vocabulary

Use a separate execution-edge namespace rather than expanding the current authored knowledge-edge policy indiscriminately.

Recommended:

```text
supports
contradicts
requires
depends_on
proposes
alternative_to
selected_over
rejected_because
refines
replaces
motivates
expected_to_affect
prevents
verifies
derived_from
compiled_to
realized_as
fails
repaired_by
revalidated_by
measured_by
```

### Important distinction

The current authored graph already has its own typed edge policy. Do not inject all ADRG execution edges into that policy.

Use:

```text
knowledge graph edges
    = durable reusable semantic relationships

reasoning execution edges
    = per-decision dependencies and audit relationships
```

The two may be projected into a derived union graph for retrieval/visualization, but their authorities remain separate.

## 6.2 Causal vocabulary

Use design-intent relations such as:

```text
expected_to_affect
intended_to_improve
design_hypothesis
```

for claims such as:

> this treatment is intended or expected to affect this observable outcome.

Reserve stronger empirical causal language for relationships supported by controlled evidence under a declared scope. Those are not the same. Empirical causal promotion should require a controlled comparison.

---

# 7. Reasoning-method routing

## 7.1 Deterministic routing features

Add a typed routing record. Do not use arbitrary 0–1 pseudo-precision until a calibrated scale exists.

```json
{
  "impact": {
    "level": "high",
    "basis": ["affects_primary_action"]
  },
  "uncertainty": {
    "evidence": "low",
    "decision_ambiguity": "medium",
    "provider": "high",
    "measurement": "medium"
  },
  "coupling": {
    "level": "high",
    "dependencies": ["camera", "blocking", "action_timing"]
  },
  "reversal_cost": {
    "level": "low",
    "dependency_commitment": "medium"
  },
  "validator_capability": {
    "coverage": "partial",
    "applicable_dimensions": ["subject_visibility", "timing"],
    "weak_dimensions": ["taste"]
  },
  "budget": {
    "context_tokens": 0,
    "generation_cost": 0,
    "latency_ms": 0
  }
}
```

The operational features are:

- impact — effect on audience meaning, hard compliance, or dependent decisions;
- uncertainty — decomposed evidence, decision, provider, and measurement uncertainty;
- coupling — explicit cross-domain dependencies;
- reversal cost / dependency commitment — operational cost of revisiting the choice;
- validator capability — dimension-specific coverage and limitations rather than one scalar strength;
- budget — bounded context, generation, latency, and where relevant render cost.

These are proposed operational variables, not universal scientific scales.

## 7.2 Routing matrix

| Signal | Preferred operator | Reason |
|---|---|---|
| low complexity + strong validator | Direct | No need for search |
| decomposable dependency chain | AoT / least-to-most | Sequential local resolution |
| high impact + independent alternatives | ToT | Compare bounded candidates |
| high coupling | GoT | Aggregate dependent decisions |
| external state/tool needed | ReAct-style tool action | Retrieve/measure/validate externally |
| deterministic computation | CoC/program-aided | Move arithmetic/validation to code |
| ambiguous high-impact decision | Self-consistency | Sample alternatives/paths where objective rubric exists |
| validator failure | bounded repair | Patch the earliest responsible layer |
| deterministic compiler can decide | no extra reasoning | Avoid unnecessary model calls |

### Critical finding

**Critique, self-consistency, and repair do not require new top-level reasoning frameworks.**

They should be operators inside the existing policy runtime.

---

# 8. State contraction

## 8.1 Proposed state model

```text
active_state
compressed_state
source_memory
decision_memory
failure_memory
```

### active_state

Only what the next operation needs:

```json
{
  "current_question": "...",
  "hard_invariants": [],
  "selected_evidence_refs": [],
  "candidate_ids": [],
  "relevant_capabilities": [],
  "unresolved": []
}
```

### compressed_state

A deterministic digest of completed work:

```json
{
  "intent_hash": "...",
  "decision_ids": [],
  "selected_candidate_ids": [],
  "invariant_status": {},
  "coverage": {},
  "loss_status": {},
  "state_digest": "sha256:..."
}
```

### source_memory

Never silently discard:

- source ID;
- locator;
- source digest;
- evidence class;
- provenance;
- retrieval timestamp/version;
- capability profile version.

### decision_memory

Retain:

- selected candidate;
- rejected candidate IDs;
- rejection reason codes;
- decision criteria;
- decision confidence;
- assumptions;
- unresolved items.

### failure_memory

Retain:

- validator ID;
- failure code;
- responsible layer;
- affected object/path;
- repair ID;
- patch digest;
- result;
- recurrence count.

## 8.2 What may be discarded

After a decision is resolved, active context may discard:

- raw retrieved prose;
- duplicate evidence text;
- rejected candidate payloads after their semantic disposition is recorded;
- scratch reasoning;
- intermediate formatting;
- tool chatter.

It must not discard:

- stable IDs;
- evidence provenance;
- decision outcome;
- rejection reason;
- invariant status;
- compile loss;
- failure/repair history;
- hashes needed for reproducibility.

This gives CPCS non-Markovian auditability without keeping the entire context window alive.

---

# 9. Invariants and variant axes

The correct model is:

```text
hard_invariant
soft_preference
controlled_degree_of_freedom
```

## 9.1 Hard invariant

Must not change.

Examples:

```text
identity
subject
action_identity
duration
safety_class
required product visibility
contact topology
continuity lock
```

Violation:

```text
reject candidate
```

## 9.2 Soft preference

Optimization target rather than prohibition.

Examples:

```text
cinematic intimacy
camera participation
emotional subtlety
visual dynamism
```

Violation:

```text
score penalty
```

## 9.3 Controlled degree of freedom

An explicit axis:

```json
{
  "axis": "camera_treatment",
  "allowed_values": [
    "low_tracking_medium",
    "telephoto_observer"
  ],
  "preserved_invariants": [
    "action_identity",
    "duration",
    "subject_visibility"
  ]
}
```

A variant should record only deltas:

```json
{
  "variant_id": "v2",
  "parent_id": "v1",
  "deltas": [
    {
      "axis": "camera_treatment",
      "from": "low_tracking_medium",
      "to": "telephoto_observer"
    }
  ]
}
```

This makes semantic diversity measurable and prevents lexical paraphrase from being mistaken for creative variation.

---

# 10. Causal reasoning contract

Use the following chain:

```text
problem
→ treatment
→ directorial decision
→ canonical control
→ expected visual effect
→ verification target
```

Example:

```text
problem:
  strike reads as instantaneous

treatment:
  visible preparation before strike

decision:
  add anticipation phase

control:
  phase.anticipation

expected_effect:
  increased action readability

verification:
  measure preparation-to-action timing and reviewer readability
```

## Causal claim classes

```text
observed_cooccurrence
correlation
temporal_succession
narrative_motivation
design_dependency
creative_hypothesis
empirical_causal_claim
```

Do not promote:

```text
research says X correlates with Y
```

into:

```text
X causes Y
```

without a controlled experiment.

---

# 11. Reasoning trace without chain-of-thought

The minimum production trace is:

```text
policy_id
policy_version
router_features
operations
selected evidence IDs
candidate IDs
decision IDs
rejected candidate reason codes
admitted concepts
admitted mappings
compiler transformations
realization statuses
verification results
repair records
final hashes
```

No private chain-of-thought is required.

This is stronger operationally because the trace is directly testable.

---

# 12. Research-to-decision examples

## Example 1 — Anticipation

```text
research:
  anticipation prepares the audience for significant action

problem:
  strike appears instantaneous

decision:
  introduce visible preparation phase

canonical:
  phase.anticipation

provider projection:
  explicit preparatory movement before strike

verification:
  preparation/action temporal separation + human readability
```

The animation literature describes anticipation as a setup/preparatory movement. This supports the semantic bridge, but the exact numeric threshold for CPCS must be calibrated.

## Example 2 — Laban effort

```text
research:
  movement qualities can be described through effort dimensions

problem:
  action reads as uncontrolled rather than deliberate

decision:
  reduce uncontrolled movement quality and preserve bound/sustained treatment

canonical:
  performance.movement_quality

provider projection:
  concise observable movement instructions

verification:
  reviewer rating + movement metric where available
```

Do not encode a psychological claim such as “bound flow means confidence.” Encode the observable movement quality and separately encode any intended audience interpretation.

## Example 3 — Gaze timing

```text
research:
  gaze can be used as a temporal directing signal

problem:
  recognition is not legible

decision:
  hold eye contact until recognition event, then briefly redirect gaze

canonical:
  gaze.target_event

provider projection:
  explicit gaze sequence in prompt / reference asset

verification:
  gaze event timing and recognition readability
```

The operational object is the event sequence, not an inferred internal emotion.

## Example 4 — Product visibility

```text
research:
  product visibility is affected by framing, blocking, and occlusion

problem:
  product reveal is intermittently obscured

decision:
  choose camera/blocking treatment that preserves product visibility

canonical:
  invariant.product_visibility
  + control.camera.framing

provider projection:
  explicit framing and visibility requirement

verification:
  visibility percentage / occlusion metric
```

This is a coupled decision and therefore a candidate for GoT-style subgraph aggregation.

## Example 5 — Camera treatment

```text
research:
  camera participation changes perceived emphasis and action readability

problem:
  the action is readable but the intended controlled tone is weak

candidates:
  handheld_close
  low_tracking_medium
  telephoto_observer

decision:
  select one candidate using explicit criteria

canonical:
  camera.treatment

provider projection:
  native camera controls if supported,
  otherwise prompt semantics,
  otherwise reference asset

verification:
  camera adherence + action readability + continuity
```

This is the canonical ToT use case: branch only because the decision has meaningful alternatives.

## Example 6 — Reference choreography

```text
research:
  exact choreography/contact topology must survive style transfer

problem:
  style transformation changes action semantics

decision:
  preserve action/contact invariants while allowing style axis to vary

canonical:
  action_identity
  contact_topology
  style.variant_axis

provider projection:
  reference-motion asset + style instructions

verification:
  action order, contact topology, identity consistency
```

---

# 13. Format/compiler effect

## 13.1 Canonical conclusion

**Format should not influence canonical reasoning.**

It should influence:

- parsing;
- validation;
- ordering;
- verbosity;
- carrier-specific conditioning;
- provider realization.

The semantic object should be resolved before provider serialization.

## 13.2 Ownership

```text
Natural language
  → intent, audience effect, observable description, provider prose

YAML
  → authored policy, profiles, imports, variants, constraints

JSON
  → canonical resolved graph, exact arrays, patches, schemas, manifests

XML
  → ordered narrative, mixed content, namespaced event envelope

JSONL
  → append-only evidence, decisions, compiler events, experiments

Media/arrays
  → dense measured/generated controls
```

## 13.3 Representation equivalence

### Same meaning

```text
"Recognition precedes the pivot."
```

### YAML

```yaml
shot:
  events:
    - id: recognition
      order: 1
    - id: pivot
      order: 2
```

### Resolved JSON

```json
{
  "events": [
    {"id": "recognition", "order": 1},
    {"id": "pivot", "order": 2}
  ]
}
```

### XML

```xml
<beat id="recognition"/>
<beat id="pivot"/>
```

### Natural-language provider projection

```text
Recognition occurs before the pivot.
```

### Compact provider form

```text
recognition → pivot
```

The last form is a lossy projection unless the provider explicitly interprets the notation.

## 13.4 Important verification

There is no sufficiently strong external evidence to claim that JSON, YAML, or XML is universally better for reasoning quality.

Therefore the package's controlled experiment is the correct approach:

```text
same canonical meaning
same model
same task
same token budget
same semantic evaluator
different carrier
```

Measure:

```text
instruction adherence
semantic preservation
omission
contradiction
schema validity
token cost
latency
```

---

# 14. Structured-output caution

Schema validity is not semantic correctness.

A model can return:

```json
{
  "selected": "candidate_3"
}
```

that is perfectly valid JSON and still select a candidate that violates a hard invariant.

Therefore:

```text
parse validity
≠
schema validity
≠
decision correctness
≠
render success
```

The system must report these separately.

Recent structured-output research also reinforces that hard output constraints can alter semantic accuracy in some small-model settings. This strengthens the design principle:

> reason/decide in a compact semantic IR, then constrain/serialize as late as practical.

This is an experimental finding to be calibrated against the CPCS model stack, not a universal provider claim.

---

# 15. Failure-directed reasoning

## 15.1 Required repair object

```json
{
  "repair_id": "repair.001",
  "failure_id": "failure.camera.001",
  "validator_id": "validator.camera_continuity",
  "base_digest": "sha256:...",
  "attribution": {
    "status": "hypothesized",
    "candidates": [
      {
        "layer": "decision",
        "confidence": "medium"
      },
      {
        "layer": "compiler",
        "confidence": "medium"
      },
      {
        "layer": "provider",
        "confidence": "low"
      }
    ]
  },
  "semantic_targets": [
    "camera.event.orbit_02"
  ],
  "resolved_paths": [
    "/camera/events/by-id/orbit_02"
  ],
  "protected_invariants": [
    "action_identity",
    "duration",
    "subject_identity"
  ],
  "patch": [],
  "status": "proposed"
}
```

## 15.2 Repair algorithm

```text
observed failure
→ classify failure
→ locate earliest responsible layer
→ load only affected object slice
→ propose smallest patch
→ test expected base
→ apply patch
→ rerun failed validator
→ rerun dependent validators
→ recompile
→ reverify
```

Use JSON Patch for canonical changes.

The `test` operation should protect the expected base before mutation.

## 15.3 Escalation

```text
repair 1 fails
→ second bounded repair if policy permits

repair limit reached
→ blocked / needs_escalation
```

Never:

```text
validator failure
→ silently rewrite canonical data
```

---

# 16. Verification model

## 16.1 Planner metrics

Required:

| Metric | Definition |
|---|---|
| evidence_selection_precision | Relevant selected evidence / selected evidence |
| evidence_resolution | Cited evidence IDs that resolve |
| decision_trace_faithfulness | Decision record matches actual selected candidate and compiler result |
| constraint_preservation | Hard invariants retained after compilation |
| alternative_diversity | Meaningful typed semantic delta between candidates |
| unnecessary_branching | Branches that produce no meaningful semantic delta |
| strategy_stability | Same fixed inputs produce same decision under deterministic policy |
| token_cost | Input + output inference cost |
| decision_latency | Planner wall-clock latency |
| repair_efficiency | Successful repairs / repair attempts |
| regression_rate | Previously passing fixtures that fail after change |
| compile_loss_severity | Weighted loss introduced by target adapter |

## 16.2 Video metrics

Use existing CPCS metrics plus:

```text
action_order
action_count
beat_timing_error
contact_timing_error
identity_consistency
camera_adherence
facial/gaze event visibility
product visibility
continuity
variant diversity
audience-meaning judgment
```

---

# 17. Measurement form

For every measurable control:

```text
what:
  exact phenomenon

source:
  measured / detected / observed / inferred

timebase:
  seconds / frames / presentation timestamp / sample timestamp

sampling:
  Hz or frame rate

coordinates:
  declared frame/world/camera coordinates

normalization:
  raw / normalized / calibrated

side:
  left / right / bilateral / side-indexed event

confidence:
  [0,1] operational confidence

tolerance:
  explicit error threshold

missing:
  unknown / unobservable / unavailable

occlusion:
  flag + confidence degradation

camera contamination:
  flag if measurement is camera-motion dependent

aggregation:
  min/max/mean/median/percentile/event rule

provenance:
  source ID + digest
```

Do not turn semantic labels into fake measurements.

For example:

```text
"controlled performance"
```

is an interpretation/creative target, not a directly measured physical quantity.

---

# 18. Implementation placement

## 18.1 Do not create

Do not create:

- another agent framework;
- another graph database;
- another scene ontology;
- another canonical score;
- another provider compiler;
- a generic `ADRGEngine` that duplicates the existing policy runtime;
- a second persistent reasoning authority.

## 18.2 Add to existing components

### Existing reasoning policy module

Extend with:

```text
router_features
decision_record creation
candidate admission
branch budget
operator metadata
state contraction
repair routing
```

### Existing graph module

Keep the existing authored edge policy intact.

Add an execution projection/record layer rather than redefining the knowledge graph.

### Existing score compiler

Consume selected ADRG decision outputs.

Do not move canonical control resolution into the LLM planner.

### Existing translation registry

Continue to own:

```text
concept/mapping
→ canonical field
→ merge operator
→ preconditions
→ loss
```

### Existing provenance

Add:

```text
decision_id
source_refs
source_digests
policy_id
policy_version
model_profile
prompt_digest
compiler_version
base_digest
result_digest
```

### Existing validators

Add ADRG-specific validators:

```text
decision_integrity
candidate_integrity
invariant_preservation
decision_reference_integrity
execution_graph_acyclicity
repair_bound
causal-edge-type validity
compile-loss completeness
```

---

# 19. Proposed minimal schemas

These are compact illustrations of the hardened contract. Section 26 is normative.

## 19.1 Candidate

```json
{
  "candidate_id": "cand.camera.tracking",
  "problem_id": "problem.action_readability",
  "status": "admitted",
  "semantic_deltas": [
    {
      "axis_id": "axis.camera.treatment",
      "from": "baseline_medium",
      "to": "low_tracking_medium"
    }
  ],
  "semantic_hash": "sha256:...",
  "preserves": [
    "inv.action_identity",
    "inv.duration"
  ],
  "requires": [
    "cap.camera_tracking"
  ],
  "expected_effect_refs": [
    "effect.action_readability"
  ],
  "evidence_refs": []
}
```

## 19.2 Decision constraint set

```json
{
  "constraint_set_id": "constraints.action.001",
  "hard_invariants": [
    {
      "id": "inv.action_identity",
      "semantic_target": {
        "object_id": "action_strike_01",
        "field": "identity"
      },
      "operator": "equals",
      "expected_value": "single_near_contact_strike",
      "violation_policy": "reject_candidate"
    }
  ],
  "soft_preferences": [],
  "variant_axes": []
}
```

## 19.3 Criterion + evaluation

```json
{
  "criterion": {
    "criterion_id": "criterion.action_readability",
    "objective": "maximize",
    "importance": "required",
    "evaluation_contract": {
      "evaluator_type": "human_rubric",
      "scale_ref": "scale://ordinal/low-medium-high",
      "calibration_status": "experimental"
    }
  },
  "evaluation": {
    "evaluation_id": "eval.camera.tracking.readability",
    "candidate_id": "cand.camera.tracking",
    "criterion_id": "criterion.action_readability",
    "result": {
      "value": "high",
      "scale_ref": "scale://ordinal/low-medium-high"
    },
    "evaluator": {
      "type": "human_rubric",
      "version": "1.0"
    },
    "basis": "human"
  }
}
```

## 19.4 Expected effect

```json
{
  "effect_id": "effect.action_readability",
  "decision_id": "dec.camera",
  "target": "action_readability",
  "direction": "increase",
  "magnitude": "unknown",
  "epistemic_status": "design_hypothesis",
  "verification_ref": "metric.action_readability"
}
```

## 19.5 Decision projection

```json
{
  "projection_id": "projection.camera.001",
  "decision_id": "dec.camera",
  "selected_candidate_id": "cand.camera.tracking",
  "admitted_concepts": ["concept.camera.tracking"],
  "admitted_mappings": ["mapping.camera.low_tracking"],
  "strategy_targets": ["camera.treatment"],
  "canonical_mutation": {"allowed": false}
}
```

## 19.6 Repair

```json
{
  "repair_id": "repair.001",
  "failure_id": "failure.001",
  "action_type": "recompile_same_semantics",
  "base_digest": "sha256:...",
  "semantic_targets": ["camera.event.orbit_02"],
  "resolved_paths": ["/camera/events/by-id/orbit_02"],
  "protected_invariants": ["inv.action_identity"],
  "patch_optional": [],
  "budget": {"max_attempts": 1},
  "status": "proposed"
}
```

---

# 20. Minimal canonical ADRG graph example

The graph is a projection of authoritative records/events. It must be rebuildable.

```json
{
  "schema_version": "cpcs-adrg/1.1",
  "document_id": "shot07",
  "nodes": [
    {
      "id": "problem.action_readability",
      "type": "goal",
      "plane": "reasoning_execution",
      "title": "Make the strike readable"
    },
    {
      "id": "cand.anticipation",
      "type": "candidate",
      "plane": "reasoning_execution",
      "title": "Visible anticipation before strike"
    },
    {
      "id": "dec.anticipation",
      "type": "decision",
      "plane": "reasoning_execution",
      "outcome_ref": "outcome.anticipation"
    },
    {
      "id": "projection.anticipation",
      "type": "decision_projection",
      "plane": "compilation_realization",
      "admitted_mappings": ["mapping.phase.anticipation"]
    },
    {
      "id": "verify.action_readability",
      "type": "validation",
      "plane": "verification_experiment",
      "title": "Verify action readability"
    }
  ],
  "edges": [
    {
      "id": "e1",
      "type": "proposes",
      "from": "problem.action_readability",
      "to": "cand.anticipation"
    },
    {
      "id": "e2",
      "type": "selected_over",
      "from": "dec.anticipation",
      "to": "cand.anticipation",
      "decision_id": "dec.anticipation"
    },
    {
      "id": "e3",
      "type": "compiled_to",
      "from": "dec.anticipation",
      "to": "projection.anticipation"
    },
    {
      "id": "e4",
      "type": "verifies",
      "from": "verify.action_readability",
      "to": "dec.anticipation"
    }
  ]
}
```

The projected graph may be used for traversal/visualization, but the durable execution-event/record layer remains authoritative.

---

# 21. Canonical mapping to current CPCS

The bridge should be:

```text
ADRG
  DecisionOutcome:selected
       ↓
DecisionProjection
       ↓
admitted concept IDs
admitted mapping IDs
       ↓
existing directing_strategy
       ↓
existing score request
       ↓
existing control translation registry
       ↓
existing universal score
       ↓
existing provider adapter
```

The current compiler already verifies that admitted concepts and mappings are present in the context and that control mapping IDs agree with the strategy's admitted mappings.

Therefore ADRG should **feed** the existing compiler, not replace it.

---

# 22. Compiler semantics

For every selected decision:

```text
research concept
→ evidence bundle
→ decision
→ canonical field/control
→ capability check
→ realization status
→ provider projection
→ loss record
→ verification
```

Realization statuses should remain:

```text
native_exact
native_approximate
baked_into_reference
compressed_to_text
postprocess_only
evaluation_only
dropped_with_warning
unsupported_error
```

A provider that cannot express a canonical control exactly must not be treated as exact merely because the natural-language prompt mentions it.

Example:

```text
canonical:
  face.AU04 peak = 0.71 at 2.73s

prompt-only provider:
  "subtle brow tension at recognition"

realization:
  compressed_to_text

lost:
  exact spline
  calibrated peak
  apex tolerance

verification:
  post-generation facial estimate
```

---

# 23. State of the current implementation vs ADRG

| Area | Current CPCS | ADRG closure |
|---|---|---|
| Reasoning policies | Present | Reuse |
| Policy execution | Present | Reuse |
| Deterministic replay | Present | Reuse |
| Canonical score | Present | Reuse |
| Control translation | Present | Reuse |
| Provenance | Present | Extend with decision refs |
| Decision IR | Partial/implicit | **Add** |
| Candidate semantics | Partial | **Add** |
| Rejection reasons | Limited | **Add** |
| Invariant/axis lattice | Partial in compiler constraints | **Add decision-level contract** |
| Impact/uncertainty routing | Not first-class | **Add** |
| State contraction | Partial | **Add explicit state contract** |
| Causal design chain | Partial | **Add execution edges/records** |
| Compile loss | Present | **Link to decision** |
| Verification | Present | **Link to decision/control** |
| Repair | Present at validator/compiler level | **Link to decision and failure** |
| Self-consistency | Not required as a new executor | **Optional operator** |
| Critique | Existing policy/validator capability | **Operator/validator stage** |
| Failure-directed refinement | Partial | **Decision-aware bounded repair** |
| New graph database | Not needed | **Do not add** |
| New orchestration framework | Not needed | **Do not add** |

---

# 24. Controlled experiments

## E-ADRG-001 — Decision IR vs current strategy-only output

**Question:** Does explicit DecisionRecord improve trace completeness without reducing compile success?

Compare:

```text
A: current reasoning strategy only
B: strategy + ADRG DecisionRecord
```

Measure:

- decision completeness;
- evidence resolution;
- constraint recall;
- compile success;
- token cost;
- latency.

## E-ADRG-002 — Router features

Compare:

```text
A: current task-class policy routing
B: task-class + typed impact/uncertainty/coupling/reversal-cost/validator-capability features
```

Measure:

- unnecessary branching;
- decision quality;
- cost;
- latency;
- hard-constraint violations.

## E-ADRG-003 — State contraction

Compare:

```text
A: full retrieved context
B: active_state + source/decision/failure memory
```

Measure:

- decision accuracy;
- evidence resolution;
- token cost;
- omission rate;
- recovery after multi-step repair.

## E-ADRG-004 — Selective ToT

Branch only on one high-impact camera decision.

Measure:

- selected-plan quality;
- semantic diversity;
- cost;
- render adherence.

## E-ADRG-005 — Failure-directed repair

Compare:

```text
A: regenerate full strategy
B: identify earliest responsible layer + JSON Patch
```

Measure:

- repair success;
- tokens;
- latency;
- collateral changes;
- invariant violations;
- regression rate.

## E-ADRG-006 — Carrier effect

Hold canonical meaning constant.

Compare:

```text
NL
YAML
JSON
XML
YAML+JSON
YAML+XML
```

Measure:

- semantic preservation;
- omission;
- contradiction;
- parse/schema validity;
- token cost;
- latency.

Do not promote a carrier as intrinsically better without this experiment.

---

# 25. Promotion rules

A new ADRG policy/operator should remain:

```text
unexplored
```

until:

1. an isolated experiment supports it;
2. it repeats across multiple tasks or is explicitly scoped;
3. cost and failure cases are recorded;
4. no rights/safety issue remains;
5. the concept/policy record is updated with evidence and calibrated confidence.

This is consistent with the existing repository integration plan.

---

# 26. ADRG Decision IR contract hardening — 04B

## 26.1 Freeze decision

The ADRG research program is sufficiently complete for implementation. The remaining work is not another broad reasoning-method survey. It is a contract-hardening pass that makes director decisions precise enough to survive routing, compilation, provider realization, verification, invalidation, replay, and repair without introducing a second orchestration or canonical-control authority.

Freeze the following laws:

```text
reasoning procedure ≠ reasoning decision
reasoning decision ≠ canonical control
canonical control ≠ provider realization
provider realization ≠ observed result
observed result ≠ empirical causal truth
```

The runtime bridge is therefore:

```text
normalized CPCS intent
→ bounded research retrieval
→ DirectorProblem
→ ReasoningRoute / DecisionProcedure
→ candidate generation
→ semantic normalization + deduplication
→ hard-constraint admission
→ criterion evaluation
→ DecisionOutcome
→ DecisionProjection
→ existing Compiled Directing Strategy
→ existing universal CPCS score/compiler
→ provider realization
→ render / VOG / verification
→ outcome, invalidation, or bounded repair
```

No additional orchestration framework is justified by this closure.

---

## 26.2 Authority planes

Every ADRG field must have one owning authority plane. No plane may silently overwrite another.

| Plane | Owns | Must not own |
|---|---|---|
| Research authority | reusable evidence, methods, scoped application knowledge | per-request selections |
| Reasoning-policy authority | allowed decision procedures, routing rules, operator contracts | canonical video controls |
| ADRG execution authority | per-request problems, candidates, evaluations, decisions, assumptions, gaps, events | research truth or provider truth |
| Directing-strategy authority | accepted semantic directing treatment | provider-specific compromises |
| Canonical score authority | exact resolved provider-neutral control state | reasoning history |
| Provider realization | carrier choice, target-specific approximation, capability loss | canonical creative truth |
| VOG | observed render evidence | intended meaning |
| Verification | expected-vs-observed verdict | canonical intent mutation |
| Experiment authority | empirical performance and promotion evidence | immediate runtime selection |

Required precedence principle:

```text
semantic_directorial decision
→ accepted directing intent
→ provider_realization decision
→ adapter projection
```

Example:

```text
semantic intent:
    low tracking medium shot

provider evidence:
    exact tracking control unreliable

provider realization:
    approximate with simplified subject-relative motion

canonical intent:
    remains low tracking medium

loss:
    exact camera path not faithfully realized
```

Provider compromise must never overwrite the underlying semantic-directorial decision.

---

## 26.3 Canonical ADRG object family

The implementation family should remain intentionally small:

```text
DirectorProblem

DecisionRecord
├── DecisionScope
├── DecisionConstraintSet
│   ├── HardInvariant
│   ├── SoftPreference
│   └── VariantAxis
├── Candidate[]
│   └── CandidateDelta[]
├── Criterion[]
├── EvaluationRecord[]
├── Assumption[]
├── UnresolvedGap[]
├── ExpectedEffect[]
└── DecisionOutcome

DecisionProjection

ReasoningRoute
DecisionProcedure
OperatorExecution

ExecutionEvent

FailureRecord
RepairRecord
VerificationRef

Optional only for genuinely coupled decisions:
DecisionBundle
```

The execution graph is a rebuildable projection of these records/events, not a parallel runtime authority.

---

## 26.4 `DirectorProblem`

`DirectorProblem` defines the decision boundary. It must ask what needs to be resolved without prematurely embedding the answer.

```json
{
  "problem_id": "problem_camera_readability_001",
  "problem_type": "creative_tradeoff",
  "question": "How should the strike be framed so anticipation and near-contact remain readable?",
  "scope": {
    "project_id": "proj_01",
    "scene_id": "scene_07",
    "shot_id": "shot_03",
    "beat_id": "beat_strike",
    "action_id": "action_strike_01",
    "actor_ids": ["actor_astra"],
    "interval_ref": "interval_strike_execution"
  },
  "decision_domain": "camera",
  "blocking": true,
  "created_from": [
    "normalized_intent://...",
    "evidence_bundle://..."
  ]
}
```

`problem_type` may include:

```text
deterministic_constraint
creative_tradeoff
provider_realization
verification_choice
failure_diagnosis
repair_choice
```

---

## 26.5 `DecisionScope`

A valid decision applied at the wrong hierarchy level is still wrong. Scope must therefore be first-class.

```json
{
  "scope": {
    "project_id": null,
    "sequence_id": null,
    "scene_id": "scene_07",
    "shot_id": "shot_03",
    "beat_id": null,
    "action_id": null,
    "actor_ids": [],
    "object_ids": [],
    "interval_ref": null
  }
}
```

Normative rules:

```text
scope ≠ inheritance
shot decision does not silently become scene policy
scene decision does not silently become project policy
scope promotion must be explicit and auditable
```

Recommended decision domains:

```text
creative
performance
camera
motion
interaction
continuity
style
editing
execution_strategy
provider_realization
verification
repair
```

---

## 26.6 Decision type and authority

At minimum, type decisions as:

```text
semantic_directorial
execution_strategy
provider_realization
verification
repair
human_override
```

Examples:

```text
semantic_directorial:
    use restrained low tracking to preserve action readability

execution_strategy:
    realize the treatment through governed camera and timing mappings

provider_realization:
    provider lacks exact path control; use reference composition + simplified motion text

verification:
    test action readability and subject visibility

repair:
    retain semantic intent and change carrier
```

A provider-realization or repair decision may supersede an earlier realization choice without superseding semantic-directorial intent unless the failure is explicitly attributed to the semantic decision itself.

---

## 26.7 `DecisionConstraintSet`

The broader container must not call every constraint an invariant. Use:

```text
DecisionConstraintSet
├── HardInvariant
├── SoftPreference
└── VariantAxis
```

Example:

```json
{
  "constraint_set_id": "constraints_camera_001",
  "hard_invariants": [
    {
      "id": "inv_action_identity",
      "semantic_target": {
        "object_id": "action_strike_01",
        "field": "identity"
      },
      "operator": "equals",
      "expected_value": "single_near_contact_strike",
      "violation_policy": "reject_candidate"
    }
  ],
  "soft_preferences": [
    {
      "id": "pref_camera_intimacy",
      "target": "camera.intimacy",
      "preference": "moderate"
    }
  ],
  "variant_axes": [
    {
      "id": "axis_camera_treatment",
      "allowed_values": [
        "low_tracking_medium",
        "telephoto_observer",
        "static_medium"
      ]
    }
  ]
}
```

Hard invariants are admission gates. Soft preferences are optimization targets. Variant axes identify what is deliberately allowed to change.

---

## 26.8 Stable semantic targeting

Raw array-index JSON Pointers are execution addresses, not semantic identity.

Use:

```text
semantic object ID
→ resolver
→ current canonical JSON Pointer
```

Example:

```json
{
  "semantic_target": {
    "object_id": "action_strike_01",
    "field": "identity"
  },
  "resolved_pointer": "/actions/by-id/action_strike_01/identity",
  "resolution_hash": "sha256:..."
}
```

This targeting law applies to:

- hard invariants;
- decision projections;
- verification targets;
- repair targets;
- human overrides.

JSON Pointer and JSON Patch remain transport/mutation mechanisms. They are not semantic identity systems.

---

## 26.9 Candidate contract

A candidate is a possible semantic treatment, not a prompt string.

```json
{
  "candidate_id": "cand_camera_low_track",
  "problem_id": "problem_camera_readability_001",
  "status": "admitted",
  "semantic_deltas": [
    {
      "axis_id": "axis_camera_treatment",
      "from": "baseline_medium",
      "to": "low_tracking_medium"
    }
  ],
  "preserves": [
    "inv_action_identity",
    "inv_actor_identity",
    "inv_product_visibility"
  ],
  "generation": {
    "procedure": "bounded_candidate_search",
    "executor": "tree_of_thoughts",
    "model_ref": "model://...",
    "prompt_hash": "sha256:...",
    "temperature": 0.8,
    "seed": 18274,
    "response_hash": "sha256:..."
  }
}
```

### Candidate lifecycle

```text
generated
→ normalized
→ duplicate? ── yes → duplicate/rejected
→ hard-invariant admission
→ admitted or invalid
→ evaluated
→ dominated or retained
→ selected / rejected
→ verified / failed / superseded
```

Recommended states:

```text
generated
normalized
admitted
invalid
duplicate
evaluated
dominated
selected
rejected
verified
failed
superseded
```

Rejection is typed:

```json
{
  "rejection": {
    "code": "violates_hard_invariant",
    "reference": "inv_product_visibility"
  }
}
```

or:

```json
{
  "rejection": {
    "code": "semantic_duplicate",
    "equivalent_to": "cand_camera_low_track"
  }
}
```

---

## 26.10 Candidate semantic equivalence

Creative diversity must be measured from normalized semantic deltas rather than lexical variation.

Example:

```text
"low tracking camera"

and

"camera moves alongside the actor from a low angle"
```

may normalize to the same treatment:

```json
{
  "camera.treatment": "tracking",
  "camera.height": "low",
  "camera.subject_relation": "follows_subject"
}
```

A useful deterministic identity is:

```text
candidate_semantic_hash =
SHA256(
    normalized_deltas
    + preserved_invariants
    + scope
)
```

Prompt wording must not participate in semantic candidate identity.

Admission test:

```text
normalize candidate deltas
→ compute semantic identity
→ compare admitted candidate identities
→ reject semantic duplicate
```

This prevents branch-based methods from reporting several paraphrases as several distinct creative treatments.

---

## 26.11 Separate candidate generation and evaluation

Candidate generation, admission, and evaluation are distinct stages:

```text
CandidateGenerator
→ candidate set
→ SemanticNormalizer
→ Deduplicator
→ InvariantGate
→ Evaluator
→ DecisionProcedure
```

The generator must not silently score and discard its own candidates before they enter the auditable execution set.

A valid trace can therefore state:

```text
generated: 5
semantic duplicates: 2
hard-invariant failures: 1
admitted: 2
evaluated: 2
selected: 1
```

---

## 26.12 `Criterion`

Criteria must be first-class semantic objects.

```json
{
  "criterion_id": "criterion_action_readability",
  "name": "action_readability",
  "objective": "maximize",
  "importance": "required",
  "evaluation_contract": {
    "evaluator_type": "human_rubric",
    "evaluator_ref": "rubric://action_readability/v1",
    "scale_ref": "scale://ordinal/low-medium-high",
    "calibration_status": "experimental"
  },
  "missing_value_policy": "unknown",
  "evidence_refs": [
    "concept://anticipation_readability"
  ]
}
```

Initial objective modes:

```text
must_pass
maximize
minimize
prefer
avoid
```

Weighted-sum optimization is not the default decision law.

---

## 26.13 `EvaluationRecord`

Naked values such as `readability = 0.91` or `confidence = 0.81` are forbidden unless the scale, evaluator, basis, and calibration are explicit.

Prefer:

```json
{
  "evaluation_id": "eval_001",
  "decision_id": "decision_camera_001",
  "candidate_id": "cand_camera_low_track",
  "criterion_id": "criterion_action_readability",
  "result": {
    "value": "high",
    "scale_ref": "scale://ordinal/low-medium-high"
  },
  "evaluator": {
    "type": "human_rubric",
    "ref": "rubric://action_readability/v1",
    "version": "1.0"
  },
  "basis": "human",
  "calibration": {
    "status": "unvalidated"
  },
  "evidence_refs": [
    "evidence://..."
  ]
}
```

A numeric value becomes valid only when its measurement semantics are established:

```json
{
  "result": {
    "value": 0.83,
    "scale_ref": "scale://action_readability_calibrated_v3"
  }
}
```

Recommended evaluator classes:

```text
deterministic
measurement
computer_vision
vlm
llm
expert_human
general_human
project_owner
experiment
```

Creative/taste criteria must explicitly identify who or what judges them. Until trustworthy proxies are calibrated, project-owner verdict should dominate claims such as better taste, stronger emotional effect, or better visual storytelling.

---

## 26.14 Decision selection semantics

Do not allow weighted scoring to compensate for a hard-invariant violation.

Required ordering:

```text
1. hard-invariant filtering
2. mandatory-threshold filtering
3. candidate dominance checks
4. soft-criterion comparison
5. selection or abstention
```

Initial decision procedures:

```text
deterministic_rule
constraint_then_rank
human_choice
```

Potential later procedures, only if fixtures/experiments justify them:

```text
pareto_frontier
lexicographic
satisficing
```

A candidate that violates identity, event topology, safety, or another hard invariant is invalid regardless of its soft score.

---

## 26.15 `DecisionOutcome`

Downstream components should consume one explicit final disposition object.

```json
{
  "outcome_id": "outcome_camera_001",
  "decision_id": "decision_camera_001",
  "status": "selected",
  "selected_candidate_id": "cand_camera_low_track",
  "selection_basis": [
    "eval_readability_001",
    "eval_visibility_001"
  ],
  "unresolved_refs": [
    "gap_provider_camera_reliability"
  ],
  "strategy_projection_ref": "projection_camera_001"
}
```

Allowed outcome states:

```text
selected
abstained
deferred
needs_evidence
needs_human_decision
blocked
superseded
invalidated
```

Normative rule:

```text
no defensible candidate
≠ automatically select the least bad candidate
```

The correct result may be `needs_evidence`, `needs_human_decision`, or `blocked`.

---

## 26.16 Confidence decomposition

Do not use a single unqualified `confidence: 0.81` field.

Prefer typed confidence dimensions:

```json
{
  "confidence": {
    "evidence_support": "medium",
    "candidate_separation": "high",
    "evaluation_reliability": "medium",
    "provider_realization": "low"
  }
}
```

These dimensions are not automatically probabilities. They become numeric only after calibration defines the scale and measurement process.

---

## 26.17 Assumptions and invalidation

Assumptions are records, not strings.

```json
{
  "assumption_id": "asm_single_actor_visibility",
  "statement": "The principal actor remains unobstructed during the strike.",
  "scope": {
    "shot_id": "shot_03"
  },
  "status": "assumed",
  "blocking_if_false": true,
  "verification_ref": null
}
```

States:

```text
assumed
verified
falsified
unknown
superseded
```

Dependency law:

```text
Decision A
DEPENDS_ON
Assumption X
```

If X is falsified:

```text
X falsified
→ Decision A stale/invalidated
→ dependent decisions stale
→ associated projection no longer effective
→ reroute only affected dependency region
```

This invalidation mechanism is required for correct non-Markovian decision state.

---

## 26.18 `UnresolvedGap`

Open questions must also be typed.

```json
{
  "gap_id": "gap_provider_tracking_reliability",
  "kind": "provider_capability_uncertainty",
  "severity": "medium",
  "blocking": false,
  "owner": "provider_adapter",
  "evidence_needed": [
    "provider_capability_test"
  ],
  "status": "open"
}
```

Routing rule:

```text
blocking unresolved gap
→ selection forbidden or human escalation required

non-blocking unresolved gap
→ selection may proceed only with explicit uncertainty/loss state
```

---

## 26.19 Evidence roles and contradictions

Evidence references should state their semantic role.

```json
{
  "evidence": [
    {
      "ref": "evidence_001",
      "role": "supports"
    },
    {
      "ref": "evidence_002",
      "role": "contradicts"
    },
    {
      "ref": "evidence_003",
      "role": "limits_scope"
    },
    {
      "ref": "provider_profile_001",
      "role": "provider_capability"
    }
  ]
}
```

Recommended roles:

```text
supports
contradicts
limits_scope
defines
motivates
provider_capability
failure_history
verification_history
```

Contradiction must remain visible:

```json
{
  "evidence_state": {
    "status": "conflicting",
    "supporting_refs": ["research_general_01"],
    "contradicting_refs": ["provider_eval_ltx23_08"]
  }
}
```

Do not resolve conflict by deleting one source. A scoped provider result may legitimately outweigh a generic recommendation for one realization decision while leaving the general research statement intact.

---

## 26.20 Universal decision precedence and human authority

CPCS needs an explicit conflict law. Recommended default precedence:

```text
1. explicit human/user hard lock
2. safety / rights / identity invariant
3. canonical action/event semantics
4. explicit scene/shot direction
5. approved project policy/profile
6. experimentally qualified scoped knowledge
7. general research recommendation
8. provider optimization
9. system default
10. stylistic embellishment
```

Exact project-specific policy may refine this order, but unresolved LLM arbitration must not be the default.

Human override is append-only and superseding:

```json
{
  "override_id": "override_001",
  "decision_id": "decision_camera_001",
  "previous_outcome": "cand_camera_low_track",
  "new_outcome": "cand_telephoto",
  "authority": {
    "type": "project_owner",
    "actor_ref": "user://..."
  },
  "reason_code": "creative_preference",
  "hard_invariants_preserved": true,
  "supersedes_event": "event_decision_selected_001"
}
```

The original model recommendation remains in history for reproducibility.

---

## 26.21 `ExpectedEffect` and causal discipline

Do not use `design_causes` for an untested creative mechanism. Prefer:

```text
expected_to_affect
intended_to_improve
design_hypothesis
```

Example:

```json
{
  "effect_id": "effect_readability_01",
  "decision_id": "decision_camera_001",
  "target": "action_readability",
  "direction": "increase",
  "magnitude": "unknown",
  "epistemic_status": "design_hypothesis",
  "evidence_basis": "research_supported",
  "verification_ref": "metric://action_readability"
}
```

Only controlled evidence may later promote a relationship toward a stronger empirical causal class, with scope preserved.

Recommended epistemic classes:

```text
observed_cooccurrence
correlation
temporal_succession
narrative_motivation
design_dependency
design_hypothesis
empirical_causal_claim
```

---

## 26.22 `DecisionProjection` — the only bridge into the existing strategy compiler

ADRG must not directly author canonical score fields.

It selects governed concepts and mappings:

```json
{
  "projection_id": "projection_camera_001",
  "decision_id": "decision_camera_001",
  "selected_candidate_id": "cand_camera_low_track",
  "admitted_concepts": [
    "c_camera_tracking",
    "c_action_readability"
  ],
  "admitted_mappings": [
    "mapping_camera_tracking_medium"
  ],
  "strategy_targets": [
    "camera.treatment"
  ],
  "canonical_mutation": {
    "allowed": false
  }
}
```

The authoritative bridge is:

```text
DecisionProjection
→ existing directing-strategy compiler
→ existing mapping authority
→ existing canonical score
```

This contract is a release gate. ADRG must never become a second canonical-score writer.

---

## 26.23 Decision procedure vs reasoning executor

The router should select a semantic decision procedure, not a research-brand name.

```text
DecisionProcedure
→ Executor implementation
```

Recommended procedure vocabulary:

```text
direct_rule
dependency_contraction
bounded_candidate_search
coupled_decision_resolution
deterministic_computation
evidence_acquisition
consensus_evaluation
failure_directed_refinement
```

Example implementation binding:

```json
{
  "procedure": "bounded_candidate_search",
  "executor": "tree_of_thoughts",
  "executor_version": "1.0"
}
```

Today `bounded_candidate_search` may resolve to the existing ToT executor. The semantic Decision IR must remain unchanged if another executor implements that procedure later.

Maintain hard ID disambiguation:

```text
rp_algorithm_of_thoughts
rp_atom_of_thoughts
```

Do not use ambiguous bare `AoT` in persisted runtime records.

---

## 26.24 Typed routing features

Do not persist arbitrary routing pseudo-precision such as:

```text
impact = 0.82
coupling = 0.73
uncertainty = 0.46
validator_strength = 0.81
```

until calibration defines those numbers.

Prefer decomposed features:

```json
{
  "routing_features": {
    "impact": {
      "level": "high",
      "basis": [
        "affects_primary_action",
        "affects_hard_visibility_requirement"
      ]
    },
    "coupling": {
      "level": "high",
      "dependencies": [
        "camera",
        "blocking",
        "action_timing"
      ]
    },
    "uncertainty": {
      "evidence": "low",
      "decision_ambiguity": "medium",
      "provider": "high",
      "measurement": "medium"
    },
    "reversal_cost": {
      "level": "low",
      "dependency_commitment": "medium"
    },
    "validator_capability": {
      "coverage": "partial",
      "applicable_dimensions": [
        "subject_visibility",
        "timing"
      ],
      "weak_dimensions": [
        "taste"
      ]
    }
  }
}
```

`irreversibility` should be interpreted operationally as reversal/commitment cost, not metaphysical irreversibility.

Example routing rules:

```text
IF single candidate
AND all hard requirements deterministically verifiable
THEN direct_rule
```

```text
IF several materially distinct candidates
AND high impact
AND weak deterministic validator
THEN bounded_candidate_search
```

```text
IF decision affects multiple coupled domains
AND local selections may conflict
THEN coupled_decision_resolution
```

```text
IF missing external factual/capability evidence
THEN evidence_acquisition
```

```text
IF arithmetic / timing / geometry is decisive
THEN deterministic_computation
```

```text
IF verification failure is attributable to a prior decision
THEN failure_directed_refinement
```

---

## 26.25 Operator contract

Critique, self-consistency, evidence acquisition, repair, and similar behaviors are operators/stages, not new top-level orchestration frameworks.

A minimal operator interface is:

```json
{
  "operator_id": "op_self_consistency",
  "procedure": "consensus_evaluation",
  "consumes": [
    "candidate_set",
    "criterion_set"
  ],
  "produces": [
    "evaluation_records"
  ],
  "side_effects": "none",
  "budget": {
    "max_samples": 3
  },
  "requires": [
    "objective_or_semiobjective_rubric"
  ],
  "stop_conditions": [
    "stable_majority",
    "budget_exhausted"
  ]
}
```

Every operator must declare input/output contracts, budget, side-effect permission, validator requirements, stop conditions, and replay metadata.

---

## 26.26 Coupled decisions and `DecisionBundle`

GoT-style reasoning is justified only when decisions interact.

Example:

```text
camera candidate A + blocking candidate B = compatible
camera candidate C + blocking candidate B = degraded
```

Represent cross-decision compatibility explicitly:

```json
{
  "bundle_id": "bundle_action_camera_001",
  "member_decisions": [
    "decision_camera_001",
    "decision_blocking_001",
    "decision_timing_001"
  ],
  "compatibility_constraints": [
    {
      "candidate_ids": [
        "cand_camera_track",
        "cand_block_forward"
      ],
      "status": "compatible"
    },
    {
      "candidate_ids": [
        "cand_camera_telephoto",
        "cand_block_forward"
      ],
      "status": "degraded"
    }
  ]
}
```

Compatibility states:

```text
compatible
conflicting
degraded
requires_revision
mergeable
dominates
```

This supplies actual merge semantics to coupled graph reasoning.

---

## 26.27 Event-sourced execution authority

Use an append-only execution history as the temporal authority.

```text
ExecutionEvent log
        │
        ├── problem_created
        ├── candidate_generated
        ├── candidate_normalized
        ├── candidate_rejected
        ├── candidate_admitted
        ├── criterion_evaluated
        ├── decision_selected
        ├── decision_abstained
        ├── assumption_verified
        ├── assumption_falsified
        ├── decision_invalidated
        ├── human_override
        ├── projection_emitted
        ├── provider_projection_created
        ├── verification_received
        ├── failure_classified
        ├── repair_requested
        ├── repair_applied
        └── decision_superseded
                ↓
        deterministic projections
        ├── current DecisionRecord
        ├── active_state
        ├── compressed_state
        ├── decision_memory
        ├── failure_memory
        └── execution graph
```

Example:

```json
{
  "event_id": "evt_000142",
  "event_type": "decision_selected",
  "decision_id": "decision_camera_001",
  "payload": {
    "selected_candidate_id": "cand_camera_low_track",
    "evaluation_refs": [
      "eval_readability_001",
      "eval_visibility_001"
    ]
  },
  "caused_by": [
    "evt_eval_000138",
    "evt_eval_000139"
  ],
  "base_state_hash": "sha256:...",
  "created_at": "..."
}
```

A later override or repair appends another event. It does not mutate history.

---

## 26.28 State contraction

`active_state`, `compressed_state`, `decision_memory`, and `failure_memory` are projections, not independent authorities.

```text
immutable execution history
→ state projector
    ├── active context
    ├── compressed context
    ├── decision memory
    └── failure memory
```

### Active state

Contains only facts that can affect the next decision:

```text
open problems
effective hard invariants
current accepted decisions
blocking gaps
live assumptions
relevant provider capability state
recent relevant failures
```

### Compressed state

Contains minimal summaries of resolved history, stable IDs, hashes, and dependency state.

### Source memory

Contains stable evidence references/provenance rather than duplicated source prose.

### Decision memory

Contains selected/rejected outcomes, supersession chain, criteria/evaluation refs, assumptions, and unresolved gaps.

### Failure memory

Contains mechanism-class signatures, recurrence state, provider/model scope, prior repair outcomes, and escalation state.

---

## 26.29 State-contraction correctness invariant

State contraction is valid only if it preserves downstream semantic behavior.

Test:

```text
full state
→ next deterministic decision eligibility

contracted state
→ same deterministic decision eligibility
```

Required preservation:

```text
hard invariants
blocking gaps
admitted evidence identities
assumption states
candidate eligibility
decision dependencies
authority precedence
```

Validator:

```text
state_contraction_semantic_equivalence
```

Token savings alone are not sufficient.

---

## 26.30 Graph-cycle semantics

Do not require the entire historical ADRG graph to be acyclic.

Require acyclicity only where it is semantically necessary, such as:

```text
current strict decision-dependency graph
canonical compilation dependency graph
```

Allow cycles/history through:

```text
revision
repair
revalidation
supersession
recurrence
```

Example:

```text
decision
→ verification
→ repair
→ revised decision
→ verification
```

A bounded strongly connected decision group may be legal for genuine coupled optimization, provided the procedure has explicit convergence/stop criteria.

---

## 26.31 Failure attribution

Verification failure must be classified before mutation.

Recommended classes:

```text
decision_defect
strategy_projection_defect
compiler_defect
provider_capability_failure
provider_stochastic_failure
reference_control_failure
verification_failure
unknown
```

Critical law:

```text
provider failure
≠ automatic semantic-plan mutation
```

If canonical choreography is correct but the provider failed, valid remedies include regeneration, carrier change, reference strengthening, shot split, provider switch, or accepted loss before reopening the semantic-directorial decision.

---

## 26.32 Responsibility is an attribution hypothesis

Do not record an uncertain responsible layer as fact.

```json
{
  "attribution": {
    "status": "hypothesized",
    "candidates": [
      {
        "layer": "provider",
        "confidence": "high",
        "evidence_refs": ["..."]
      },
      {
        "layer": "compiler",
        "confidence": "low",
        "evidence_refs": ["..."]
      }
    ]
  }
}
```

Upstream semantic mutation should require stronger attribution than a local realization repair. Unknown attribution must fail safely.

---

## 26.33 Repair action family

JSON Patch is one repair primitive, not the definition of repair.

Allowed repair dispositions should include:

```text
patch_strategy
recompile_same_semantics
regenerate_same_build
change_control_carrier
add_reference_control
split_shot
switch_provider
postprocess
human_review
accept_loss
no_safe_repair
```

Example authority matrix:

| Failure | Typical permitted repair |
|---|---|
| schema invalid | patch structural object |
| mapping stale | recompile |
| provider stochastic failure | regenerate |
| provider cannot express control | change carrier/provider |
| shot exceeds provider limit | split realization |
| verification false positive | repair verifier |
| semantic decision demonstrably defective | reopen decision |
| unknown cause | no upstream mutation |

Most provider failures should stop below the semantic decision layer.

---

## 26.34 Repair budget and stop rules

```json
{
  "repair_budget": {
    "max_attempts": 2,
    "max_token_cost": 12000,
    "max_render_attempts": 2,
    "max_latency_ms": null,
    "max_collateral_delta": "local",
    "on_diagnostic_uncertainty": "escalate",
    "on_invariant_threat": "stop"
  }
}
```

A repair must stop early if:

- a hard invariant becomes threatened;
- attribution confidence becomes insufficient for the proposed mutation;
- the same mechanism-class failure recurs beyond the policy threshold;
- cost/latency/render budget is exhausted.

Failure records should support:

```text
signature
mechanism_class
recurrence_count
provider/model scope
root-cause hypothesis
previous successful repair
```

---

## 26.35 Replay semantics

Distinguish three replay contracts:

```text
record replay
execution replay
generation replay
```

### Record replay

```text
same sealed candidates
+ same evaluations
+ same criteria
+ same policy version
→ same decision outcome
```

Must be deterministic.

### Execution replay

```text
same sealed decision/event records
→ same projection
→ same deterministic compile result
```

Must be deterministic.

### Generation replay

```text
same live external model request
→ byte-identical candidates
```

is not guaranteed unless the provider/model explicitly supports deterministic generation.

Therefore seal:

```text
model identity/version
prompt/version/hash
request parameters
temperature
seed when supported
raw response hash
normalized candidate outputs
```

The sealed output, not an assumption of external model reproducibility, is the replay authority.

---

## 26.36 Controlled stochastic candidate generation

Deterministic selection and stochastic creative generation are compatible.

```text
candidate generation = optionally stochastic and fully logged
selection over sealed candidate set = deterministic where the procedure/evaluations are deterministic
```

Example generation metadata:

```json
{
  "generation": {
    "generator": "model://...",
    "prompt_version": "...",
    "temperature": 0.8,
    "seed": 1234,
    "branch_request": 4,
    "response_hash": "sha256:..."
  }
}
```

---

## 26.37 Decision completeness modes

Do not force the full ADRG object onto trivial deterministic decisions.

### Deterministic decision

Required:

```text
problem
scope
rule_ref
inputs
outcome
```

### Evaluated decision

Required:

```text
problem
scope
candidate set
constraint set
criteria
evaluations
outcome
```

### Branched creative decision

Required:

```text
problem
scope
candidate set
semantic deltas
hard invariants
criteria
evaluations
rejection records
outcome
expected effects
```

### Coupled graph decision

Additionally requires:

```text
DecisionBundle
cross-candidate compatibility
merge disposition
```

This prevents ADRG from adding unnecessary branching, token cost, and ceremony to deterministic provider limits or simple rule enforcement.

---

## 26.38 Minimal hardened `DecisionRecord`

```json
{
  "decision_id": "decision_camera_001",
  "problem_id": "problem_camera_readability_001",
  "mode": "branched_creative",
  "decision_type": "semantic_directorial",
  "decision_domain": "camera",
  "scope": {
    "scene_id": "scene_07",
    "shot_id": "shot_03"
  },
  "constraint_set_ref": "constraints_camera_001",
  "candidate_ids": [
    "cand_low_tracking",
    "cand_telephoto",
    "cand_locked_medium"
  ],
  "criterion_ids": [
    "criterion_readability",
    "criterion_subject_visibility",
    "criterion_continuity"
  ],
  "evaluation_ids": [
    "eval_001",
    "eval_002",
    "eval_003"
  ],
  "assumption_ids": [
    "asm_single_actor_visibility"
  ],
  "unresolved_gap_ids": [
    "gap_provider_camera_reliability"
  ],
  "outcome_ref": "outcome_camera_001",
  "expected_effect_ids": [
    "effect_action_readability_001"
  ],
  "provenance": {
    "procedure": "bounded_candidate_search",
    "executor": "tree_of_thoughts",
    "source_event_ids": ["..."]
  }
}
```

Deliberately excluded:

```text
raw chain-of-thought
unqualified score matrix
single arbitrary confidence number
provider-specific canonical override
direct canonical-score mutation
```

---

## 26.39 End-to-end hardened example

User intent:

```text
Make the strike feel deliberate and dangerous,
but do not make the character look enraged.
Keep the gauntlet visible.
```

### Problem

```text
How should performance + camera communicate controlled danger
without breaking gauntlet visibility?
```

### Constraints

```text
HARD
- actor identity
- single strike
- gauntlet visibility

SOFT
- dangerous
- restrained

VARIANT AXES
- camera treatment
- performance leakage
```

### Generated candidates

```text
A: low tracking medium + restrained displayed affect
B: handheld close + stronger facial leakage
C: telephoto observer + minimal leakage
D: low tracking medium phrased differently
```

### Normalize/deduplicate

```text
D semantically equals A
→ duplicate rejection
```

### Hard-invariant admission

```text
B obscures gauntlet
→ invalid
```

Remaining candidates:

```text
A
C
```

### Evaluations

```text
A
- action readability: high
- gauntlet visibility: high
- emotional restraint: high
- provider realization reliability: medium

C
- action readability: medium
- gauntlet visibility: high
- emotional restraint: high
- provider realization reliability: high
```

### Outcome

```text
selected: A
basis: required action-readability criterion while preserving all hard invariants
```

### Projection

```text
admitted concepts:
- camera tracking
- restrained displayed affect
- action readability

admitted mappings:
- camera.low_tracking_medium
- performance.restraint

→ existing CPCS directing-strategy compiler
```

### Provider realization

If the target provider cannot reliably reproduce the tracking path:

```text
provider_realization decision:
    approximate A using simplified subject-relative movement

canonical semantic-directorial decision:
    remains A

loss:
    exact camera trajectory unavailable/unreliable
```

### Verification

Observed:

```text
gauntlet visible ✓
single strike ✓
identity ✓
restraint ✓
camera tracking ✗
```

### Failure attribution

```text
semantic decision defect: low
governed strategy defect: low
compiler defect: low
provider capability/stochastic failure: high
```

### Repair

```text
do not reopen semantic_directorial decision

preferred actions:
- regenerate same semantic build
- strengthen/change carrier
- switch provider if required
```

This example captures the core ADRG authority law: failed realization is not automatically failed intent.

---

## 26.40 Format/compiler implications after hardening

The prior carrier conclusion remains valid:

```text
YAML  → authoring/policy/variant surface
JSON  → canonical resolved structures and schema enforcement
XML   → ordered/namespaced narrative/event envelope where needed
NL    → human-facing and provider-facing semantic projection
JSONL → append-only evidence/execution/decision/experiment events
```

Two experiment families must remain separate:

```text
reasoning carrier experiment:
    NL vs YAML vs JSON vs XML vs hybrid context presentation

provider realization carrier experiment:
    text vs reference image vs first frame vs pose/control video/mask/depth/etc.
```

Schema validity is not semantic correctness:

```text
parse validity
≠ schema validity
≠ decision correctness
≠ provider realization success
≠ render verification success
```

---

# 27. `CPCS_CLOSURE_MATRIX`

| Gap | Existing CPCS support | Hardened representation | Governing rule / measurement | Compiler effect | Experiment needed | Priority |
|---|---|---|---|---|---|---|
| Decision semantics | strategy/executor layer | `DirectorProblem` + `DecisionRecord` + `DecisionOutcome` | decision completeness by mode | feeds projection only | E-ADRG-001 | P0 |
| Decision scope | implicit task/scene context | `DecisionScope` + `decision_domain` | scope resolution + no implicit promotion | limits projection target | fixture first | P0 |
| Decision authority | existing canonical/compiler separation | `decision_type` + authority planes | semantic intent cannot be overwritten by realization | preserves canonical truth | fixture first | P0 |
| Alternatives | ToT/GoT execution | `Candidate` + `CandidateDelta` | semantic-delta diversity | only selected/admitted candidate projects | E-ADRG-001/004 | P0 |
| Candidate equivalence | no formal contract | semantic normalization + candidate hash | duplicate branch rate | prevents duplicate projections | E-ADRG-004 | P0 |
| Candidate lifecycle | implicit pruning | typed candidate states + rejection codes | lifecycle completeness | no direct compiler mutation | fixture first | P0 |
| Constraints | locks/compiler constraints | `DecisionConstraintSet` | hard invariant admission before soft scoring | protects strategy projection | E-ADRG-002 | P0 |
| Criteria | string list | `Criterion` | explicit objective/evaluator/scale | no direct mutation | E-ADRG-001 | P0 |
| Evaluation | ad hoc scores possible | `EvaluationRecord` | reject unqualified numeric pseudo-precision | selected candidate basis becomes auditable | E-ADRG-001 | P0 |
| Abstention | not first-class | `DecisionOutcome` states | selected/deferred/needs_evidence/blocked | no projection when unresolved | fixture first | P0 |
| Confidence | scalar risk | decomposed confidence dimensions | scale/calibration required for numeric form | no direct compiler effect | calibration later | P0 |
| Assumptions | string metadata | `Assumption` | falsification invalidates dependents | stale projections disabled | fixture first | P0 |
| Unresolved gaps | free text | `UnresolvedGap` | blocking vs non-blocking | may block projection | fixture first | P0 |
| Evidence roles | evidence refs | typed evidence roles | contradiction preservation | no authority change | fixture first | P0 |
| Precedence | partly implicit governance | explicit decision precedence | deterministic conflict law | protects user/identity/scene authority | fixture first | P0 |
| Human override | open/implicit | superseding override event | preserve original recommendation/history | may replace effective projection if valid | fixture first | P0 |
| Routing | six existing executors | `DecisionProcedure` + typed `ReasoningRoute` | decision features, not arbitrary 0–1 values | selects existing executor | E-ADRG-002 | P0 |
| Operator semantics | methods/stages exist | `OperatorExecution` | declared I/O, budget, side effects, stop | no new compiler | E-ADRG-004 | P1 |
| Coupled reasoning | GoT executor exists | `DecisionBundle` + compatibility | merge/conflict semantics | bundle may gate projections | E-ADRG-004 | P1 |
| Execution authority | runtime traces | append-only `ExecutionEvent` | deterministic event projection | graph/state rebuildable | fixture first | P0 |
| State contraction | atom/dependency execution | active/compressed/decision/failure projections | semantic-equivalence validator | no canonical semantic change | E-ADRG-003 | P1 |
| Invalidation | partial dependency logic | assumption/decision dependency events | local stale/invalidated propagation | disables affected projection | fixture first | P0 |
| Causal design chain | controls + experiments | `ExpectedEffect` | design hypothesis distinct from empirical causality | links decision→verification | E-ADRG-001/005 | P0 |
| Decision→strategy bridge | selected concepts/mappings | `DecisionProjection` | ADRG cannot mutate canonical score directly | existing compiler remains authority | E-ADRG-001 | P0 |
| Compile loss | existing | decision/projection/loss refs | exact vs semantic vs approximated status | existing adapter behavior | E-ADRG-001 | P0 |
| Provider capability | existing profiles | provider realization decision + empirical reliability refs | expressibility ≠ reliability | adapter/capability negotiation only | provider experiments | P1 |
| Verification | existing validators/VOG | verification refs back to decision/effect | expected-vs-observed completeness | may trigger failure event | E-ADRG-005 | P0 |
| Failure attribution | basic validator failure | typed `FailureRecord` + attribution hypothesis | uncertain cause cannot justify unsafe upstream mutation | selects repair layer | E-ADRG-005 | P0 |
| Repair | compiler/validator repair | `RepairRecord` + action family | patch is one action; bounded budgets | recompile/regenerate/recareer/etc. | E-ADRG-005 | P0 |
| Replay | deterministic policy replay | record/execution/generation replay distinction | sealed external outputs | deterministic projection/compile | fixture first | P0 |
| Format effect | polyglot compiler | carrier experiment records | semantic preservation under equal meaning/budget | serialization/projection only | E-ADRG-006 | P1 |
| Empirical causality | experiment infrastructure | scoped experiment records | one-lever controlled comparisons | promotion only | E-ADRG-006+ | P1 |

---

# 28. `PROPOSED_AGENT_BUILD_PACKET`

## 28.1 Concepts to add

```text
director_problem
decision_scope
director_decision
director_candidate
candidate_delta
decision_constraint_set
hard_invariant
soft_preference
variant_axis
criterion
evaluation_record
assumption
unresolved_gap
expected_effect
decision_outcome
decision_projection
reasoning_route
decision_procedure
operator_execution
execution_event
failure_record
repair_record
verification_ref
```

Optional, only when coupled reasoning requires it:

```text
decision_bundle
candidate_compatibility
```

Do not add a second canonical control schema or persistent execution graph authority.

---

## 28.2 Core fields

### `director_problem`

```text
problem_id
problem_type
question
scope
decision_domain
blocking
created_from
```

### `director_decision`

```text
decision_id
problem_id
mode
decision_type
decision_domain
scope
constraint_set_ref
candidate_ids
criterion_ids
evaluation_ids
assumption_ids
unresolved_gap_ids
outcome_ref
expected_effect_ids
provenance
```

Explicitly remove unexplained fields such as a naked `scores` matrix or single unqualified `confidence` scalar.

### `director_candidate`

```text
candidate_id
problem_id
status
semantic_deltas
semantic_hash
preserves
requires
expected_effect_refs
evidence_refs
generation_metadata
rejection
```

### `decision_constraint_set`

```text
constraint_set_id
hard_invariants
soft_preferences
variant_axes
```

### `criterion`

```text
criterion_id
name
objective
importance
evaluation_contract
missing_value_policy
evidence_refs
```

### `evaluation_record`

```text
evaluation_id
decision_id
candidate_id
criterion_id
result.value
result.scale_ref
evaluator.type
evaluator.ref
evaluator.version
basis
calibration
evidence_refs
```

### `assumption`

```text
assumption_id
statement
scope
status
blocking_if_false
verification_ref
```

### `unresolved_gap`

```text
gap_id
kind
severity
blocking
owner
evidence_needed
status
```

### `expected_effect`

```text
effect_id
decision_id
target
direction
magnitude
epistemic_status
evidence_basis
verification_ref
```

### `decision_outcome`

```text
outcome_id
decision_id
status
selected_candidate_id
selection_basis
unresolved_refs
strategy_projection_ref
```

### `decision_projection`

```text
projection_id
decision_id
selected_candidate_id
admitted_concepts
admitted_mappings
strategy_targets
canonical_mutation.allowed=false
```

### `reasoning_route`

```text
procedure
executor
executor_version
routing_features.impact
routing_features.coupling
routing_features.uncertainty
routing_features.reversal_cost
routing_features.validator_capability
budget
```

### `execution_event`

```text
event_id
event_type
entity_refs
payload
caused_by
base_state_hash
created_at
provenance
```

### `failure_record`

```text
failure_id
verification_ref
failure_class
signature
mechanism_class
recurrence_count
provider_scope
model_scope
attribution.status
attribution.candidates
protected_invariants
```

### `repair_record`

```text
repair_id
failure_id
action_type
base_digest
semantic_targets
resolved_paths
protected_invariants
patch_optional
budget
status
result
```

---

## 28.3 Relations / execution edges

Keep execution edges separate from the authored reusable knowledge-edge ontology.

Recommended execution-only relations:

```text
supports
contradicts
limits_scope
defines
motivates
requires
depends_on
proposes
alternative_to
selected_over
rejected_because
refines
replaces
supersedes
expected_to_affect
prevents
verifies
derived_from
compiled_to
realized_as
fails
repaired_by
revalidated_by
measured_by
invalidates
```

Reserve stronger causal predicates for empirically qualified claims.

---

## 28.4 Compiler/runtime operations

```text
create_problem
classify_decision_mode
resolve_decision_scope
resolve_precedence
route_decision_procedure
generate_candidates
normalize_candidate
compute_candidate_semantic_hash
deduplicate_candidates
enforce_hard_invariants
admit_candidate
evaluate_candidate
resolve_decision
abstain_or_defer
record_human_override
emit_decision_projection
compile_existing_strategy
resolve_capability
emit_realization_status
emit_loss
emit_verification_ref
append_execution_event
project_active_state
contract_state
invalidate_dependents
classify_failure
attribute_failure
propose_repair
resolve_semantic_target_to_pointer
apply_json_patch_when_applicable
regenerate_or_recarrier_when_applicable
revalidate
```

---

## 28.5 Validators

```text
director_problem_schema
decision_schema
decision_scope_integrity
decision_mode_completeness
decision_reference_integrity
decision_authority_plane_integrity
candidate_schema
candidate_semantic_identity
candidate_lifecycle_integrity
candidate_generation_evaluation_separation
hard_invariant_preservation
variant_axis_integrity
criterion_schema
evaluation_record_schema
numeric_evaluation_requires_scale
evaluator_role_required
abstention_projection_guard
assumption_dependency_integrity
unresolved_gap_blocking_rule
evidence_role_integrity
contradiction_preservation
decision_precedence_integrity
human_override_supersession_integrity
decision_projection_no_canonical_mutation
current_dependency_acyclicity
historical_revision_cycles_allowed
state_contraction_semantic_equivalence
execution_event_replay_integrity
execution_graph_rebuildability
compile_loss_completeness
provider_failure_semantic_mutation_guard
failure_attribution_required
repair_bound
repair_base_digest
repair_invariant_preservation
provenance_resolution
capability_profile_freshness
```

---

## 28.6 Minimum fixtures

```text
fixture_direct_deterministic_limit
fixture_evaluated_single_domain
fixture_tot_camera_choice
fixture_got_performance_camera_coupling
fixture_hard_invariant_rejection
fixture_semantically_duplicate_variants
fixture_conflicting_evidence
fixture_blocking_unresolved_gap
fixture_abstained_decision
fixture_human_override
fixture_assumption_falsification
fixture_local_decision_invalidation
fixture_missing_capability
fixture_provider_realization_approximation
fixture_compile_loss
fixture_validator_failure
fixture_provider_stochastic_failure
fixture_patch_repair
fixture_recarrier_repair
fixture_no_safe_repair
fixture_second_repair_escalation
fixture_event_replay
fixture_state_contraction_equivalence
fixture_carrier_equivalence
```

---

## 28.7 Release tests

The minimum ADRG release suite should include:

```text
ADRG-001 trivial deterministic decision does not branch
ADRG-002 lexical paraphrases that normalize identically become one candidate
ADRG-003 candidate violating hard invariant cannot win through scoring
ADRG-004 unqualified numeric evaluation fails schema
ADRG-005 missing evidence may produce needs_evidence instead of forced selection
ADRG-006 abstained/blocked decision emits no strategy projection
ADRG-007 human override supersedes but does not delete machine recommendation
ADRG-008 provider realization cannot overwrite semantic_directorial decision
ADRG-009 DecisionProjection cannot directly mutate canonical score
ADRG-010 selected decision projects governed concepts/mappings only
ADRG-011 candidate generation and candidate evaluation are independently recorded
ADRG-012 candidate rejection requires typed reason code
ADRG-013 falsified blocking assumption invalidates dependent decision
ADRG-014 unrelated decisions remain valid after local invalidation
ADRG-015 current dependency graph remains acyclic where required
ADRG-016 revision/repair history may contain bounded cycles
ADRG-017 coupled candidate incompatibility blocks bundle selection
ADRG-018 event replay reconstructs identical effective ADRG state
ADRG-019 execution graph can be deleted and rebuilt from execution records/events
ADRG-020 state contraction preserves deterministic eligibility and authority state
ADRG-021 provider_stochastic failure cannot patch semantic intent
ADRG-022 unknown attribution forbids unsafe upstream mutation
ADRG-023 schema failure may use structural JSON Patch with base digest
ADRG-024 repair can choose regenerate/recareer/provider-switch/no-patch outcomes
ADRG-025 repair budget exhaustion escalates/blocks
ADRG-026 repair preserves protected hard invariants
ADRG-027 exact/non-exact provider realization always has realization status
ADRG-028 non-exact realization emits loss record
ADRG-029 existing six reasoning executors remain replay-stable behind procedure bindings
ADRG-030 existing CPCS compiler remains the sole canonical-score writer
```

---

## 28.8 Explicit non-goals / deletion guard

Do not build:

```text
another orchestration framework
LangGraph as a new runtime authority
a second canonical score
a parallel ADRG canonical-control schema
an independently authoritative ADRG Neo4j state
a generic weighted-scoring engine without need
a system that treats LLM confidence numbers as measured truth
a system that mutates creative intent automatically after provider failure
raw chain-of-thought persistence
unbounded repair loops
a graph search for every trivial deterministic decision
```

Any future ADRG concept must earn admission through a failing fixture, measured experiment, or demonstrated production failure class.

---

## 28.9 Remaining empirical questions — not design blockers

These move to implementation/experiments rather than more conceptual ADRG research:

1. provider empirical reliability for each control and carrier;
2. numeric router thresholds, if numeric calibration proves useful;
3. state-contraction thresholds;
4. candidate semantic-diversity metrics beyond exact normalized equivalence;
5. repair-attribution calibration from real failures;
6. human/project-owner taste evaluator calibration;
7. self-consistency cost/benefit defaults;
8. reasoning-carrier effects under equal canonical meaning;
9. provider-carrier effects under equal semantic target;
10. failure recurrence/escalation thresholds.

---

# 29. Recommended implementation order

## Phase 1 — Decision IR foundation

Implement:

```text
DirectorProblem
DecisionScope
DecisionRecord
DecisionOutcome
```

Fixtures:

```text
deterministic
evaluated
branched
abstained
blocked
```

Release gate: decision mode completeness and scope integrity.

---

## Phase 2 — constraints and candidates

Implement:

```text
DecisionConstraintSet
HardInvariant
SoftPreference
VariantAxis
Candidate
CandidateDelta
semantic candidate identity
candidate lifecycle
```

Tests:

```text
semantic paraphrase dedup
hard invariant rejection
soft preference never acts as hard rejection
variant outside declared axis rejected
```

---

## Phase 3 — criteria and evaluation

Implement:

```text
Criterion
EvaluationRecord
evaluator classes
typed confidence dimensions
```

Hard rule:

```text
numeric score without scale/evaluator/calibration metadata
→ reject
```

---

## Phase 4 — decision procedure routing

Implement:

```text
DecisionProcedure
ReasoningRoute
OperatorExecution
```

Bind existing executors behind procedure names. Do not rewrite the six current executors merely to rename them.

Initial procedures:

```text
direct_rule
constraint_then_rank
bounded_candidate_search
coupled_decision_resolution
deterministic_computation
evidence_acquisition
failure_directed_refinement
```

---

## Phase 5 — projection into existing CPCS compiler

Implement:

```text
DecisionProjection
```

Acceptance canary:

```text
DecisionOutcome:selected
→ DecisionProjection
→ exact existing Compiled Directing Strategy path
→ existing universal score
```

Hard gate:

```text
ADRG cannot directly mutate canonical score
```

---

## Phase 6 — event history, override, and invalidation

Implement:

```text
ExecutionEvent
state projection
Assumption
UnresolvedGap
decision dependency invalidation
human override
```

Tests:

```text
falsified assumption invalidates only dependents
event replay reconstructs effective state
execution graph rebuilds from event records
human override preserves prior recommendation
```

---

## Phase 7 — verification and bounded repair

Implement:

```text
ExpectedEffect
VerificationRef
FailureRecord
attribution hypothesis
RepairRecord
repair action family
```

Tests:

```text
provider failure cannot automatically mutate semantic intent
schema failure may patch structure
unknown attribution → no unsafe upstream patch
repair budget exhausted → escalate/block
recurrence can stop repeating ineffective repair
```

---

## Phase 8 — controlled experiments

Run the existing E-ADRG experiments with the hardened objects:

```text
E-ADRG-001 Decision IR vs strategy-only output
E-ADRG-002 typed router features
E-ADRG-003 state contraction
E-ADRG-004 bounded candidate/coupled reasoning
E-ADRG-005 failure-directed repair
E-ADRG-006 carrier effect
```

Add provider-specific reliability experiments separately from reasoning-carrier experiments.

Only measured results may justify numeric calibration, stronger causal claims, or new default routing policy.

---

# 30. Final determination

## 30.1 What ADRG is

ADRG is the semantic decision layer that makes the existing CPCS reasoning-policy system explicit, auditable, replayable, compiler-connected, and verification-linked.

It represents:

```text
problem
→ alternatives
→ constraints
→ evidence
→ evaluations
→ decision disposition
→ expected effects
→ governed strategy projection
→ realization/loss
→ verification
→ invalidation/repair when required
```

## 30.2 What ADRG is not

ADRG is not a replacement for:

- the existing reasoning policies/executors;
- the curated research knowledge graph;
- the existing scene/control ontology;
- the existing Compiled Directing Strategy;
- the universal canonical score;
- the provider compiler/adapters;
- VOG;
- the existing validation framework.

It also does not require a new orchestration framework.

## 30.3 Final frozen runtime

```text
                 REUSABLE KNOWLEDGE
                        │
                        ▼
              CPCS knowledge authority
                        │
                        ▼
                  DirectorProblem
                        │
                        ▼
                  ReasoningRoute
                        │
                        ▼
                DecisionProcedure
                        │
                        ▼
       ┌──── Candidate generation ────┐
       │                              │
       ▼                              │
normalize → dedup → invariant gate    │
       │                              │
       ▼                              │
  EvaluationRecord[]                  │
       │                              │
       ▼                              │
   DecisionOutcome ◄──────────────────┘
       │
       ▼
 DecisionProjection
       │
       ▼
 EXISTING COMPILED DIRECTING STRATEGY
       │
       ▼
 EXISTING UNIVERSAL CPCS SCORE
       │
       ▼
 provider realization
       │
       ▼
 render / VOG / verification
       │
       ▼
 failure or success event
       │
       ├── evidence update
       ├── provider-profile evidence
       ├── bounded repair
       └── selective decision invalidation
```

Orthogonal temporal authority:

```text
EVERY EXECUTION TRANSITION
        ↓
append-only ExecutionEvent
        ↓
rebuildable projections
├── effective decisions
├── active reasoning state
├── compressed state
├── execution graph
├── decision memory
└── failure memory
```

## 30.4 Closure state

```text
ADRG RESEARCH COVERAGE              PASS
CORE ARCHITECTURE                   PASS
NO-NEW-ORCHESTRATOR DECISION        PASS
REASONING OPERATOR LAYER            PASS
DIRECTOR DECISION IR                HARDENED CONTRACT DEFINED
DECISION SCOPE/AUTHORITY             CLOSED AT DESIGN LEVEL
EVALUATION SEMANTICS                 CLOSED AT DESIGN LEVEL; CALIBRATION EMPIRICAL
ABSTENTION / INVALIDATION            CLOSED AT DESIGN LEVEL
STRATEGY PROJECTION                  CLOSED AT DESIGN LEVEL
EVENT / REPLAY AUTHORITY             CLOSED AT DESIGN LEVEL
REPAIR ATTRIBUTION                   CONTRACT DEFINED; CALIBRATION EMPIRICAL
PROVIDER RELIABILITY                 EXPERIMENTAL
NUMERIC ROUTER THRESHOLDS            EXPERIMENTAL / NOT REQUIRED FOR V1
IMPLEMENTATION READINESS             READY FOR FIXTURES + SLICED IMPLEMENTATION
READY FOR MORE BROAD ADRG RESEARCH   NO
```

## 30.5 Stopping rule

This 04B hardening pass is the final conceptual ADRG design pass.

From this point forward, a new ADRG abstraction should be added only when one of the following occurs:

1. a release fixture cannot express a legitimate decision/failure state;
2. a production failure exposes a genuinely new mechanism class;
3. a controlled experiment demonstrates that the existing representation loses necessary semantics;
4. an existing CPCS authority boundary cannot represent the required behavior without contradiction.

Otherwise, do not add more ADRG concepts. Implement, measure, and repair the smallest failing layer.

The final architectural insight remains:

```text
CPCS already knows how to reason in several ways.
ADRG makes explicit what was decided, under what authority,
from which evidence and constraints, with which unresolved uncertainty,
and how that decision is projected into the existing compiler without becoming a second compiler.
```

That is the closure.

---

# 31. Primary sources / source locators

## ADRG package

- `CPCS-ADRG-RP-2026-01`, *From Prompt Chains to Director Graphs*, version 1.0.
- `CPCS_ADRG_Reasoning_Graph_Schema.json`.
- `reasoning_policy.yaml`.
- `planner_prompt_templates.md`.
- `REPO_INTEGRATION_PLAN.md`.

## External primary sources

- Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*, arXiv:2201.11903.
- Wang et al., *Self-Consistency Improves Chain of Thought Reasoning in Language Models*, arXiv:2203.11171.
- Zhou et al., *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models*, arXiv:2205.10625.
- Yao et al., *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*, arXiv:2305.10601.
- Besta et al., *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*, arXiv:2308.09687.
- Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, arXiv:2210.03629.
- Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback*, arXiv:2303.17651.
- Turpin et al., *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*, arXiv:2305.04388.
- W3C PROV Overview / PROV-DM.
- RFC 6901 — JSON Pointer.
- RFC 6902 — JSON Patch.
- JSON Schema Draft 2020-12.
- Ray, *The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models*, arXiv:2605.26128 (2026).
- YAML 1.2 specification.
- XML 1.0 specification.

---

## Confidence

**High confidence:** the principal architectural gap is the missing decision-semantic bridge, not a missing reasoning framework.

**Medium confidence:** exact routing thresholds, state-contraction thresholds, semantic diversity weights, and provider-specific format effects require controlled experiments.

**Not established:** no universal claim that JSON/YAML/XML or any single reasoning operator is globally superior for AI-video directing.
