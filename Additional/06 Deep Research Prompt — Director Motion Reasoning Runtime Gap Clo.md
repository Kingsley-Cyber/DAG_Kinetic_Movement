# Deep Research Prompt — Director Motion Reasoning Runtime Gap Closure

## Attached research

Use both:

- `director_motion_reasoning_complete_package.zip`
- `director_motion_reasoning_execution_kit.zip`

## Mission

Perform a deep research pass specifically on the remaining gaps identified by the DMR gap register and determine which gaps require additional research before implementation.

Do not redesign CPCS. Treat DMR as execution/runtime research that must integrate behind the existing CPCS semantic authority.

The result must teach a coding agent **how the Director applies the research at
runtime**. Definitions and schemas without a decision path are insufficient.
For every gap, connect:

```text
scene condition
→ evidence or authored intent
→ Director decision
→ ScenePlan/Canonical Score field
→ solver or validator
→ provider capability decision
→ emitted control
→ observed measurement
→ accept, repair, degrade, or fail closed
```

Label each step as deterministic, constraint-solved, model-mediated,
human-authored, observed, measured, or experimental. Identify the exact runtime
owner and the smallest executable consumer for every new field.

Before answering individual gaps, reproduce the authoritative DMR gap register
as a coverage table. This prompt names G001–G009, G011–G017, and G019–G021 but
does not define G010, G018, or G022. Recover those definitions from the attached
register; do not infer them from numbering. Every register entry must end as
`closed`, `implementable_now`, `requires_experiment`, `unknown`, `deferred`, or
`rejected` with a reason.

## Highest-priority research

### G001 — Canonical ScenePlan

Determine the exact reconciliation between:

```text
CPCS Universal Score
CPCS-MX
Video Observation Graph
DMR ScenePlan
```

Define one executable ScenePlan without creating a competing semantic authority.

Resolve:

- IDs;
- units;
- coordinate frames;
- authority;
- authored vs solved vs observed values;
- source/evidence;
- versioning;
- serialization.

#### Application deliverable

Produce an authority and lifecycle table for every overlapping field in the
four structures. State whether DMR references it without copying, materializes
a resolved execution value, derives a temporary solver value, records an
observation link, or is forbidden from owning it.

Define `ScenePlan` as an execution projection with creation, resolution,
validation, compilation, evaluation, and retirement stages. Show replanning
after an authored score change, an observation mismatch, and a provider
capability change. Include one conflict where an observed VOG value differs
from an authored target and demonstrate why observation does not silently
overwrite intent.

Required artifacts:

- a normative field-ownership matrix;
- identity/reference rules for scene, shot, actor, object, event, control, and
  evidence IDs;
- a units and frame registry;
- an origin/value-status model (`authored`, `solved`, `derived`, `observed`,
  `measured`, `unknown`);
- a ScenePlan state machine;
- minimal, realistic, and invalid ScenePlan instances;
- an invariant proving ScenePlan cannot become a second semantic authority.

### G002 — Temporal solver

Research executable temporal semantics for:

- interval;
- instant;
- duration;
- onset;
- deadline;
- overlap;
- before/after;
- during;
- meets;
- starts/finishes;
- equality;
- latency.

Research Allen interval relations, OWL-Time, STN/STNU boundaries, negative-cycle explanations, underconstraint detection, and uncertainty.

Provide exact JSON/YAML/XML representations.

#### Application deliverable

Define compilation from authored temporal language into solver variables and
constraints. Show at least one fully specified schedule, one satisfiable but
underconstrained schedule, one inconsistent schedule with a minimal conflict
explanation, one uncertain-duration case that must not become falsely precise,
and one deadline/latency violation that triggers repair.

Specify when CPCS should use interval algebra, a Simple Temporal Network, an
uncertainty-aware extension, or no solver. Define numeric tolerance,
clock/timebase, boundary rules, unit conversion, rounding, and the policy for
choosing among multiple valid schedules. Record whether a chosen schedule came
from authored timing, deterministic optimization, or creative selection.

### G003/G004 — Action and persistent state

Research executable action preconditions/effects and persistent state.

Required state examples:

```text
actor position
orientation
stance
gaze
held object
injury
wetness
fatigue display
wardrobe
lighting
object ownership
damage
environmental residue
```

Show:

```text
STATE(t) + EVENT → STATE(t+1)
```

and define invariant checking.

#### Application deliverable

Create a state-variable catalog separating identity invariants, persistent
fluents, continuous measured state, ephemeral execution state, derived state,
visual-only display cues, and epistemic state.

For each exemplar field, define identity scope, value type, units/frame,
initialization, write authority, update rule, persistence, reversibility,
observability, uncertainty, and termination. Show event application as an
atomic state patch with precondition evaluation, effect commit, invariant
validation, and rollback/failure behavior. Include competing events that write
the same state, a missing initial state, and an effect known only after observing
the generated video. Show the exact continuity error prevented by consulting
state.

### G005 — Contact graph

Research typed contact lifecycle:

```text
approach
near_contact
contact
impact
support
grasp
release
separation
reaction
```

Include:

- actor;
- target;
- site;
- normal;
- support;
- visibility;
- confidence;
- occlusion;
- reaction link;
- time interval.

#### Application deliverable

Define which lifecycle stages are events, which are relations, and which are
derived classifications. Specify legal and illegal transitions, cardinality,
side and anatomical-site semantics, contact identity across frames, multi-surface
contact, and how occlusion changes confidence without fabricating continuity.
Connect contact to action preconditions, support/balance validation, held-object
state, causal effects, provider projection, and post-generation measurement.

Include a grasp/release trace, impact/reaction trace, sustained-support trace,
and unobservable contact. For each, give the exact runtime decision enabled by
the contact object.

### G006 — Feasibility validator

Research bounded checks for:

- support;
- reach;
- joint limits;
- root/foot coherence;
- penetration;
- impossible timing;
- ownership;
- contact;
- balance.

Explicitly distinguish deterministic checks from estimates and unknowns.

#### Application deliverable

Every check must return a typed outcome:

```text
pass | fail | indeterminate | not_applicable | unobservable
```

Define inputs, assumptions, algorithm, tolerance source, confidence
propagation, evidence, false-positive risk, and repair scope. Establish which
failures block compilation, warn, cause re-solving, or require review. Include
a case where 2D video is insufficient to assert 3D penetration or a joint-limit
failure. Order validation so an unknown prerequisite cannot be treated as a
pass by downstream checks.

### G007/G008 — Provider contracts and adapters

Research exact provider capability contracts for the first implementation targets.

Use official documentation.

For each provider/model/version determine:

```text
native controls
reference/control media
duration
fps
camera controls
image conditioning
motion conditioning
pose controls
negative prompting
structured input
carrier support
API version
limits
unknowns
evidence date
expiry/reprobe condition
```

Do not treat an old provider snapshot as current truth.

#### Application deliverable

Represent each provider contract as a versioned, dated capability snapshot,
not as code constants or prose. Distinguish documented capability,
experimentally observed behavior, adapter support, and unverified assumption.
Define capability identity/granularity, evidence locator and retrieval date,
model/API version and scope, native parameter domain, approximation strategy,
prohibited transformations, expiry, smoke test, drift signal, reprobe trigger,
and the exact pre-compilation negotiation rule.

For one canonical scene, show how two providers produce different
`RepresentationPlan` and loss ledgers while preserving canonical meaning.
Never claim a current capability without official documentation or a dated
experiment.

### G009 — Complete compilation-loss report

Define an exactly-once accounting model:

```text
canonical requested control
→ carrier
→ transformation
→ provider field
→ result
```

Every field must be:

```text
native
approximated
semantic
omitted
unsupported
unknown
```

with residual risk.

#### Application deliverable

Define exactly-once coverage over canonical control IDs and field paths. A
control has one terminal disposition per provider request; transformations may
add ordered intermediate records but may not erase or duplicate that terminal
entry. Specify composite controls, partial field support, conflicts, provider
defaults, and information lost before versus after request submission.

Required invariants:

```text
no requested control without a terminal disposition
no unexplained emitted provider field
no unsupported required control silently omitted
no approximation without method and residual risk
no semantic prose claim treated as native control
```

### G011/G012/G013 — Measurement and evaluator

Research a modular measurement stack covering:

- actor tracking;
- 2D/3D pose;
- face;
- hands;
- gaze;
- contact;
- phase;
- optical flow;
- camera motion;
- world motion;
- lens/crop/edit effects.

Define measurement error and confidence.

Research camera/body motion disentanglement.

Then define evaluator inputs:

```text
target canonical record
observed VOG
measured tracks
semantic observations
human review
```

and output:

```text
metric
score
confidence
evidence locator
failure class
```

#### Application deliverable

Define a target/observation join contract: how target actor, object, event,
interval, side, coordinate frame, and field IDs match VOG tracks and
measurements. Separate detector confidence, measurement uncertainty, semantic
interpretation confidence, and final metric confidence.

For every metric specify target field paths, observed inputs, alignment,
camera/body disentanglement, formula, unit, tolerance provenance,
missing/occluded behavior, aggregation, decision threshold, failure class, and
repairable owner. Give one valid 2D metric, one requiring calibrated 3D, one
semantic human-review metric, and one that must return `unobservable`. Show how
the evaluator result causes acceptance or a minimal repair.

### G014/G015 — Failure and repair

Research a causal failure taxonomy and minimal patch model.

Required:

```text
failure symptom
→ evidence
→ likely responsible layer
→ confidence
→ candidate patch
→ protected invariants
→ re-solve
→ recompile
```

#### Application deliverable

Define diagnosis as ranked, evidence-linked hypotheses; do not equate symptom
with root cause. Every patch must name its authority layer, exact field paths,
protected invariants, downstream invalidations, and required rechecks.
Demonstrate a temporal repair that preserves identity/style, a contact repair
that forces temporal re-solving, a carrier repair that does not mutate canonical
meaning, and an ambiguous observation failure that escalates instead of being
patched speculatively. Include loop termination and rollback rules.

### G016/G017 — Benchmark and experiment harness

Research benchmark construction:

- gold scenes;
- temporal annotations;
- state annotations;
- contacts;
- causal graphs;
- provider outputs;
- human ratings;
- repeated A/B;
- confidence intervals;
- effect sizes;
- negative-result retention.

#### Application deliverable

Define the evaluation unit, split policy, annotation schema, annotator agreement,
provider/version snapshot, seed/repeat policy, and leakage controls. Each gold
fixture must link canonical target, provider request, output artifact,
observations, metrics, human judgments, and failure labels.

Provide a minimal benchmark slice that can falsify at least one ScenePlan,
temporal, state, contact, compiler-loss, and evaluator claim. State which result
blocks implementation versus only recalibrates a threshold.

### G019 — Format doctrine

Research controlled semantic-equivalence experiments for:

- NL;
- YAML;
- JSON;
- XML;
- hybrid.

Measure adherence, token overhead, syntax validity, variance, and failure modes.

#### Application deliverable

Use the same canonical `meaning_id` for every generated format variant. State
which boundary is under test: authoring, internal interchange, model reasoning
context, provider request, or audit log. Do not generalize a result across
boundaries. Produce a provider-specific selection rule and fallback rule driven
by versioned capability evidence and experiment results.

### G020 — FACS/Laban calibration

Determine exactly which numeric scales are defensible and which must remain qualitative/project-specific.

#### Application deliverable

For each numeric or ordinal field, identify scale type, anchors, permitted
operations, calibration source, rater/instrument, reliability evidence,
cross-subject comparability, provider mapping, and invalid transformations.
Show behavior when a provider accepts prose but not the canonical numeric
scale. Do not average ordinal categories or translate between FACS, Laban, and
provider controls without an evidenced mapping.

### G021 — Provider lifecycle

Research contract drift detection, expiration, smoke tests and reprobe policy.

#### Application deliverable

Define `unverified → verified → stale → reprobe_due → invalidated`, including
when compilation may proceed in each state. Specify what a smoke test can
establish, what requires official documentation, and how changed behavior is
quarantined without rewriting historical evidence.

## Shared application fixture

Use one stable fixture throughout the packet:

```text
Actor A rotates toward a table and accidentally strikes a drinking glass with
the right forearm. The glass leaves the table, breaks on the floor, and the
shards persist. Actor B notices the impact after a constrained reaction latency.
The camera reframes to Actor B, then reveals the broken glass. At least one
requested control is unsupported natively by the selected provider.
```

Bounded details may be added, but the causal spine may not change. Assign stable
IDs, time intervals, pre/post state, contact stages, side-specific anatomy,
causal edges, attention/edit motivation, provider dispositions, and evaluation
results. Label every introduced value by origin. The fixture must appear in the
canonical JSON, an authoring format, a provider request, compilation-loss
report, and evaluator output.

## Required "how to apply" output

Include these packet-specific sections in addition to the master protocol:

1. `DMR_RUNTIME_DECISION_TABLE` — condition, consulted object, rule, output,
   failure path, and owner.
2. `SCENEPLAN_AUTHORITY_MATRIX` — field ownership/reference behavior across the
   Universal Score, CPCS-MX, VOG, and DMR.
3. `END_TO_END_SCENE_TRACE` — shared fixture from intent through acceptance or
   repair.
4. `MINIMAL_DMR_VERTICAL_SLICE` — smallest build proving state + time + contact
   + capability negotiation + evaluation.
5. `DEFERRED_SCOPE` — excluded fields/subsystems and evidence needed to add them.
6. `ACCEPTANCE_AND_FALSIFICATION` — observable tests and rejection conditions.

## Standards and research anchors

Investigate authoritative temporal, provenance, affect, multimodal-behavior, and movement-analysis standards where relevant. Do not import their ontologies wholesale; determine which concepts are useful as interoperability references.

## Final requirement

Return a prioritized research closure plan for G001–G022, with exact fields, schemas, metrics, fixtures, tests, and provider evidence requirements.

End with `CPCS_CLOSURE_MATRIX` and `PROPOSED_AGENT_BUILD_PACKET`.


## Research execution rules

Use the attached frozen package as the primary corpus, but independently verify important claims with primary sources. Do not silently "fix" the package. Explicitly distinguish package-derived claims, external-source findings, proposed CPCS representations, and experimental hypotheses.

The objective is not a literature review. The objective is to close implementation-relevant semantic gaps with enough precision that a coding agent can extend the existing CPCS tree without inventing a competing authority.

You MUST apply the output contract in `00_MASTER_DEEP_RESEARCH_PROTOCOL.md`.
