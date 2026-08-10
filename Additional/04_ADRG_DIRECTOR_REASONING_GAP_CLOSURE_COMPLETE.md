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

1. **DecisionRecord / Candidate / Invariant / Consequence objects** at reasoning-runtime level.
2. **Typed execution edges** for support, contradiction, proposal, selection, rejection, causal dependency, verification, compilation, and repair — without polluting the existing authored knowledge-edge ontology.
3. **Decision-aware routing features**: impact, uncertainty, coupling, irreversibility, validator strength, plus budget.
4. **Explicit active/compressed/source/decision/failure memory** with deterministic contraction rules.
5. **Bounded repair + compile-loss + verification linkage** so a render failure can identify the earliest responsible layer and generate a minimal patch.

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
uncertainty
coupling
irreversibility
validator_strength
budget
```

These should be features of routing, not a replacement policy framework.

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

The minimum semantic object should be:

```json
{
  "decision_id": "dec.camera.treatment",
  "question": "Which camera treatment best preserves action readability?",
  "problem_ref": "problem.action_readability",
  "candidate_ids": [
    "cand.low_tracking",
    "cand.telephoto",
    "cand.handheld"
  ],
  "criteria": [
    "action_readability",
    "subject_visibility",
    "continuity",
    "generation_reliability"
  ],
  "constraint_refs": [
    "inv.action_identity",
    "inv.subject_identity"
  ],
  "evidence_refs": [
    "evidence.anticipation_readability",
    "profile.camera.capability.v3"
  ],
  "scores": {
    "cand.low_tracking": {
      "action_readability": 0.90,
      "subject_visibility": 0.88,
      "continuity": 0.86,
      "generation_reliability": 0.81
    }
  },
  "selected": "cand.low_tracking",
  "rejected": [
    {
      "candidate_id": "cand.handheld",
      "reason_codes": ["continuity_risk"]
    }
  ],
  "assumptions": [
    "single_actor_visibility"
  ],
  "confidence": 0.81,
  "unresolved": [
    "target_specific_camera_adherence"
  ],
  "consequences": [
    "control.camera.low_tracking",
    "verification.camera.adherence"
  ],
  "loss": []
}
```

### What it does not mean

`confidence` is not probability that the director is objectively correct.

It is confidence in the decision under the declared evidence, rubric, and unresolved assumptions.

`causes` does not automatically mean scientifically demonstrated causation.

`selected` does not mean rendered success.

`evidence_refs` establish provenance, not truth by themselves.

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
design_causes
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

Use:

```text
design_causes
```

for:

> this treatment is intended to cause this control/effect.

Use:

```text
causal_claim
```

for:

> empirical evidence supports that changing X causes Y.

Those are not the same.

Empirical causal promotion should require a controlled comparison.

---

# 7. Reasoning-method routing

## 7.1 Deterministic routing features

Add a routing record:

```json
{
  "impact": 0.0,
  "uncertainty": 0.0,
  "coupling": 0.0,
  "irreversibility": 0.0,
  "validator_strength": 0.0,
  "budget": {
    "context_tokens": 0,
    "generation_cost": 0,
    "latency_ms": 0
  }
}
```

The first five ADRG features are:

- impact — effect on audience meaning or hard compliance;
- uncertainty — unresolved uncertainty after retrieval;
- coupling — cross-domain dependencies;
- irreversibility — cost of choosing incorrectly;
- validator_strength — availability of deterministic verification.

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
  "responsible_layer": "scene_control",
  "affected_paths": [
    "/camera/events/2"
  ],
  "cause_candidates": [
    {
      "layer": "decision",
      "confidence": 0.41
    },
    {
      "layer": "compiler",
      "confidence": 0.37
    },
    {
      "layer": "provider",
      "confidence": 0.22
    }
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

## 19.1 Candidate

```json
{
  "candidate_id": "cand.camera.tracking",
  "parent_id": null,
  "type": "candidate_treatment",
  "decision_id": "dec.camera",
  "deltas": [],
  "preserves": [
    "inv.action_identity",
    "inv.duration"
  ],
  "requires": [
    "cap.camera_tracking"
  ],
  "expected_effects": [
    "higher_action_readability"
  ],
  "risks": [],
  "evidence_refs": [],
  "status": "proposed"
}
```

## 19.2 Invariant

```json
{
  "invariant_id": "inv.action_identity",
  "kind": "hard_invariant",
  "path": "/actions/0/identity",
  "value": "single_near_contact_strike",
  "source": "authored",
  "enforcement": "reject_candidate"
}
```

## 19.3 Consequence

```json
{
  "consequence_id": "cons.camera_tracking",
  "decision_id": "dec.camera",
  "target": "control.camera.treatment",
  "type": "derived",
  "expected_effect": "higher_action_readability",
  "verification_refs": [
    "metric.action_readability"
  ]
}
```

## 19.4 Repair

```json
{
  "repair_id": "repair.001",
  "failure_id": "failure.001",
  "base_digest": "sha256:...",
  "patch": [],
  "protected_invariants": [],
  "max_attempts": 1,
  "status": "proposed"
}
```

---

# 20. Minimal canonical ADRG graph example

```json
{
  "schema_version": "cpcs-adrg/1.0",
  "document_id": "shot07",
  "planner_profile": "planner.standard.modular.v1",
  "nodes": [
    {
      "id": "problem.action_readability",
      "type": "goal",
      "plane": "scene_intent_control",
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
      "title": "Select anticipation treatment",
      "selected_candidate": "cand.anticipation"
    },
    {
      "id": "control.phase.anticipation",
      "type": "transform",
      "plane": "scene_intent_control",
      "title": "Canonical anticipation phase"
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
      "to": "control.phase.anticipation",
      "target_adapter": "cpcs.universal_score",
      "realization_status": "native_exact"
    },
    {
      "id": "e4",
      "type": "validated_by",
      "from": "control.phase.anticipation",
      "to": "verify.action_readability"
    }
  ]
}
```

---

# 21. Canonical mapping to current CPCS

The bridge should be:

```text
ADRG
  DecisionRecord.selected
       ↓
selected concept IDs
selected mapping IDs
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
B: task-class + impact/uncertainty/coupling/irreversibility/validator strength
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

# 26. `CPCS_CLOSURE_MATRIX`

| Gap | Existing CPCS support | New knowledge required | New representation | Measurement | Compiler effect | Experiment needed | Priority |
|---|---|---|---|---|---|---|---|
| Decision IR | strategy/executor layer | decision semantics | DecisionRecord | completeness, evidence resolution | feeds existing strategy | E-ADRG-001 | P0 |
| Alternatives | ToT/GoT execution | candidate semantics | Candidate + deltas | semantic diversity | selected candidate only compiles | E-ADRG-001/004 | P0 |
| Rejection reasons | implicit pruning | auditable rejection taxonomy | `rejected_because` | reason coverage | no direct effect | E-ADRG-001 | P0 |
| Invariants | compiler constraints/locks | decision-level invariant contract | hard/soft/axis | preservation | controls inherit protected paths | E-ADRG-002 | P0 |
| Routing | existing policy selection | decision-level signals | routing_features | unnecessary branching/cost | selects existing executor | E-ADRG-002 | P0 |
| State contraction | atom/dependency execution | memory contract | active/compressed/source/decision/failure | token savings + recovery | no canonical semantic change | E-ADRG-003 | P1 |
| Causal design chain | controls + experiments | explicit design causality | consequence + design edges | trace completeness | links decision to control | E-ADRG-001/005 | P0 |
| Empirical causality | A/B infrastructure | causal claim contract | experiment_record | one-lever effect | policy promotion only | E-ADRG-006 | P1 |
| Compile loss | existing | decision linkage | loss refs | loss severity | existing adapter behavior | E-ADRG-001 | P0 |
| Verification | existing validators | decision linkage | validation refs | verification completeness | revalidation | E-ADRG-005 | P0 |
| Repair | existing validator/compiler repair | earliest-layer attribution | RepairRecord | repair efficiency | JSON Patch/recompile | E-ADRG-005 | P0 |
| Self-consistency | method research | optional operator metadata | bounded branch set | quality/cost | no new compiler | E-ADRG-004 | P2 |
| Critique | existing critique/validation mechanisms | stage semantics | critic node | critique usefulness | no direct authority | E-ADRG-002 | P2 |
| Format effect | existing polyglot compiler | controlled evidence | carrier experiment record | semantic preservation | serialization only | E-ADRG-006 | P1 |
| Provider capability | existing adapter profiles | decision-aware capability penalty | capability evidence ref | realization accuracy | existing loss statuses | E-ADRG-001 | P0 |
| Provenance | existing provenance | decision-level links | source/decision hashes | evidence resolution | no authority change | E-ADRG-001 | P0 |

---

# 27. `PROPOSED_AGENT_BUILD_PACKET`

## Concepts to add

```text
director_problem
director_candidate
director_decision
director_invariant
director_axis
director_consequence
director_verification_ref
director_failure
director_repair
reasoning_route_features
state_snapshot
```

## Fields

### `director_decision`

```text
decision_id
question
problem_ref
candidate_ids
criteria
scores
constraint_refs
evidence_refs
selected
rejected
assumptions
confidence
unresolved
consequences
loss
```

### `director_candidate`

```text
candidate_id
decision_id
parent_id
deltas
preserves
requires
expected_effects
risks
evidence_refs
status
```

### `director_invariant`

```text
invariant_id
kind
path
value
source
enforcement
```

### `reasoning_route_features`

```text
impact
uncertainty
coupling
irreversibility
validator_strength
budget
```

### `repair`

```text
repair_id
failure_id
validator_id
base_digest
responsible_layer
affected_paths
protected_invariants
patch
max_attempts
status
```

## Relations

```text
proposes
supports
contradicts
requires
depends_on
alternative_to
selected_over
rejected_because
refines
replaces
motivates
design_causes
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

## Compiler operations

```text
resolve_decision
admit_candidate
enforce_invariants
apply_variant_delta
route_operator
contract_state
resolve_capability
compile_existing_strategy
emit_loss
emit_verification_ref
propose_repair
apply_json_patch
revalidate
```

## Validators

```text
decision_schema
candidate_schema
decision_reference_integrity
invariant_preservation
alternative_delta_integrity
execution_dependency_acyclicity
repair_bound
compile_loss_completeness
provenance_resolution
capability_profile_freshness
```

## Fixtures

Minimum fixtures:

```text
fixture_direct_selection
fixture_tot_camera_choice
fixture_got_performance_camera_coupling
fixture_hard_invariant_rejection
fixture_conflicting_evidence
fixture_missing_capability
fixture_compile_loss
fixture_validator_failure
fixture_one_patch_repair
fixture_second_repair_escalation
fixture_semantically_duplicate_variants
fixture_carrier_equivalence
```

## Tests

```text
test_decision_selected_candidate_exists
test_rejection_reason_required
test_hard_invariant_blocks_candidate
test_variant_changes_only_declared_axes
test_no_duplicate_semantic_variant
test_decision_evidence_ids_resolve
test_design_causal_edge_not_empirical_causal_claim
test_compiled_control_has_realization_status
test_loss_record_required_for_non_exact_realization
test_repair_requires_base_test
test_repair_preserves_invariants
test_repair_bound_escalates
test_state_contraction_preserves_audit_refs
test_router_is_deterministic
test_existing_policies_remain_replay_stable
```

## Open research questions

1. What numeric thresholds for impact/uncertainty/coupling are useful on actual CPCS tasks?
2. How much state contraction can occur before decision quality degrades?
3. Does DecisionRecord output improve downstream compile success enough to justify its token cost?
4. Which target providers preserve which controls natively?
5. Which variant-distance metric correlates with human-perceived creative diversity?
6. When does self-consistency outperform a deterministic validator?
7. Which carrier produces the best semantic preservation under equal token budgets?
8. Which failures can be reliably attributed to planning versus compilation versus provider realization?
9. What evidence threshold should promote a reasoning pattern into durable knowledge?
10. How should human overrides interact with soft scores while preserving reproducibility?

---

# 28. Recommended implementation order

### Phase 1 — semantic bridge

Implement:

```text
DecisionRecord
Candidate
Invariant
Consequence
```

and emit them from the existing reasoning runtime.

### Phase 2 — decision-aware routing

Add:

```text
impact
uncertainty
coupling
irreversibility
validator_strength
```

to routing state.

Do not remove the existing six executors.

### Phase 3 — compiler linkage

Attach:

```text
decision_id
candidate_id
loss_id
verification_id
```

to the existing directing strategy / compiler result.

### Phase 4 — bounded repair

Connect existing validator failures to:

```text
FailureRecord
→ RepairRecord
→ JSON Patch
→ recompile
→ revalidate
```

### Phase 5 — state contraction

Introduce explicit active/compressed/source/decision/failure memory.

### Phase 6 — experiments

Run E-ADRG-001 through E-ADRG-006.

Only after measurement should new routing defaults become verified policy.

---

# 29. Final determination

## What ADRG is

A semantic decision/control layer that makes the existing reasoning-policy system auditable and compiler-connected.

## What ADRG is not

A replacement for:

- CPCS reasoning policies;
- the existing knowledge graph;
- the existing scene-control ontology;
- the existing canonical score;
- the existing provider compiler;
- the existing validation framework.

## The central implementation insight

The missing abstraction is:

```text
reasoning method
    ≠
reasoning decision
```

CPCS already has the first.

ADRG should add the second.

The resulting architecture is:

```text
                    RESEARCH / KNOWLEDGE
                           │
                           ▼
                    evidence bundle
                           │
                           ▼
                 ┌─────────────────────┐
                 │ ADRG Decision IR    │
                 │                     │
                 │ problem             │
                 │ candidates          │
                 │ invariants          │
                 │ criteria            │
                 │ decision            │
                 │ consequences        │
                 │ verification        │
                 └──────────┬──────────┘
                            │
                   existing policy router
                            │
            ┌───────────────┼────────────────┐
            ▼               ▼                ▼
          Direct          AoT/AOT          ToT/GoT
            │               │                │
            └───────────────┼────────────────┘
                            ▼
                  existing strategy IR
                            │
                            ▼
                  existing CPCS compiler
                            │
                  capability negotiation
                            │
                            ▼
                  provider realization
                            │
                            ▼
                      verification
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
              success               failure
                                      │
                                      ▼
                              bounded repair
                                      │
                                      ▼
                                  recompile
                                      │
                                      ▼
                                  reverify
```

That is the closure.

No new orchestration framework is justified by the current evidence. The implementation gap is semantic: **make the existing reasoning operators resolve explicit, auditable director decisions and connect those decisions to the existing compiler and verification authority.**

---

# 30. Primary sources / source locators

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
