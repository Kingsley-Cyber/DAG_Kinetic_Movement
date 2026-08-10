# Deep Research Prompt — CPCS World Model / Causal State / Attention Gap Closure

## Attached research

Use:

- `mISSIN_Distill.txt`
- `Research-Grounded Video Prompt.txt`
- `CPCS_AI_Video_Motion_Direction_KB_v1.0.0.zip`
- `CPCS_FACS_Laban_AI_Video_Research_Package_v1.2.zip`
- `CPCS_MX_Hierarchical_Motion_Grammar_Research_Package_v1.0.zip`
- DMR packages if available

## Mission

This is the cross-cutting gap-closure pass.

The missing-distillation document identifies a major architectural opportunity: a **sparse persistent World Model between dense observation and directorial reasoning**.

Research exactly what this model should contain, what it should not contain, and how it should compile into CPCS.

The key distinction is:

```text
Pegasus/VOG observes densely
        ↓
World Model Distiller summarizes sparsely
        ↓
Director reasons causally
        ↓
Canonical Score encodes controls
        ↓
Provider compiler translates
```

Do not turn the World Model into another giant knowledge graph.

The closure document must show **how a fact enters, changes, affects a decision,
and leaves the sparse World Model**. A catalog of possible fields is not enough.
For every proposed object, connect:

```text
dense observation / authored intent / retrieved research
→ inclusion or exclusion decision
→ sparse world-state object
→ Director causal or continuity decision
→ Canonical Score control or constraint
→ provider projection
→ observed result
→ persistence, correction, retirement, or unknown
```

Label every arrow as deterministic, model-mediated, measured, detected,
interpreted, authored, creative, or experimental. Define the runtime owner,
write authority, consumer, invalidation rule, and smallest observable benefit.

The World Model is a disposable/rebuildable execution projection. It may refer
to evidence, VOG observations, research claims, and Canonical Score objects, but
must not silently promote interpreted scene state into reusable knowledge or
overwrite authored intent. The researcher must prove this boundary with field
ownership rules and conflict examples.

## 0. Sparse distillation policy

Before the domain sections, research the selection policy that keeps the World
Model small. Define:

```text
candidate fact
salience and continuity need
causal/constraint relevance
persistence horizon
observability/confidence
redundancy check
include | reference | summarize | defer | discard | unknown
```

Specify budgets by object/event/time window only if evidence supports them;
otherwise define a parameterized budget requiring calibration. Explain how
facts are deduplicated, merged, aged, invalidated, and re-expanded from source
evidence. Produce a `distillation_decision` audit record for every retained,
compressed, or discarded candidate that could materially affect continuity,
causality, feasibility, or evaluation.

Include adversarial cases: a visually salient but causally irrelevant detail,
a visually subtle continuity-critical fact, conflicting observations, an
unobservable state, and a fact that becomes important only after a later event.

## 1. Persistent environment

Research a world-state representation containing:

```text
location
topology
floor planes
walls
exits
obstacles
vertical levels
atmosphere
weather
environmental motion
damage
persistent changes
```

Define:

```text
state_at(t)
event_delta
persistence
reversibility
owner
evidence
```

Example:

```text
wall_crack_01
appears at frame 388
persists through frame 500
caused by impact_07
```

### Application deliverable

Define environment identity, coordinate frame, containment/topology, state
variable type, initialization, update authority, persistence, reversibility,
expiry, and evidence linkage. Show how CPCS distinguishes "not observed",
"absent", "unknown", "occluded", and "ceased to exist". Give one delta that
updates state, one delta rejected by an invariant, and one retroactive correction
that preserves the prior observation history.

Demonstrate the exact continuity/directing decision caused by retaining the wall
crack or residue, and show when that fact is no longer needed by the runtime.

## 2. Physics and affordance model

Research object-level representation:

```text
material
rigid/deformable
mass class
inertia class
support
affordances
grip
push
pull
break
bend
roll
slide
```

Then connect object affordance to action feasibility.

Do not build a full physics engine. Determine the smallest semantic model that improves director reasoning and validation.

### Application deliverable

Separate authored/known physical properties from qualitative classes,
measurements, detected behavior, inferred affordances, and simulation outputs.
For each affordance define actor/object roles, prerequisites, enabling and
blocking conditions, confidence, evidence, and the feasibility check that
consumes it. Do not infer `breakable`, `grippable`, or mass/inertia class merely
from an object label without evidence or an explicit prior.

Show three branches: affordance enables an action candidate; a known property
rejects it; evidence is insufficient and the validator returns `indeterminate`.
State which representation is enough to improve planning without pretending to
predict dynamics.

## 3. Causal Event Graph

This is a mandatory focus.

Research a typed graph where:

```text
hip rotation
→ causes
arm acceleration
→ causes
contact
→ causes
recoil
→ causes
table collision
→ causes
glass displacement
→ causes
glass break
→ motivates
camera reframe
```

Distinguish:

```text
causes
temporally_precedes
enables
motivates
reacts_to
results_in
observed_with
correlated_with
```

Do not collapse all into `related_to`.

Define:

- event identity;
- actor/object;
- precondition;
- action;
- contact;
- effect;
- state transition;
- camera/edit consequence;
- confidence;
- evidence.

### Application deliverable

Give truth conditions and non-meaning for every edge type. Define direction,
cardinality, whether cycles are legal, confidence propagation, temporal
requirements, provenance, and allowed inference. `causes` must require more
than precedence; `motivates` must identify the directing/narrative decision
owner; `observed_with` and `correlated_with` must not be promoted to causation.

Provide a causal-chain construction procedure, an edge-admission decision table,
and a contradiction/repair rule. Show how the graph is traversed to choose a
camera/edit response, diagnose a failed effect, and compute the minimal upstream
repair set. Include one tempting but invalid causal edge and reject it.

## 4. Character state

Research a persistent character state:

```text
identity invariants
appearance
wardrobe
body proportions
location
orientation
pose
gaze target
held objects
injury
wetness
cleanliness
fatigue display
breath
visible affect
knowledge state
social state
```

Define state transitions and invariants.

### Application deliverable

Classify each character field as identity invariant, authored continuity
constraint, persistent fluent, continuous measurement, visible display cue,
epistemic state, social interpretation, or provider-facing control. Define who
may write each class and what evidence can revise it. `Fatigue display` and
`visible affect` must not become claims about private internal state.

Show atomic state transitions for movement, grasp/release, wardrobe/wetness or
injury continuity, and a knowledge change. Include simultaneous conflicting
writes, identity drift, occlusion, and re-identification uncertainty. Then show
one Director decision and one evaluator check that consume the resulting state.

## 5. Viewer attention model

Research how directing can represent:

```text
primary attention target
secondary target
withheld information
reveal
attention shift
attention transition mechanism
```

Potential mechanisms:

```text
gaze
camera pan
rack focus
blocking
lighting
sound
edit
contrast
motion
depth
```

The key model is:

```text
narrative objective
→ viewer attention
→ composition
→ camera/performance/editing/lighting
```

Research whether this can be represented as a time-varying attention curve or event sequence.

### Application deliverable

Do not assume a numeric attention curve is valid. Compare event targets,
piecewise priority, ordinal salience, probabilistic gaze/attention estimates,
and continuous curves. Define which are authored directing intent, which are
measured viewer responses, and which are experimental predictions.

For each attention transition, specify narrative objective, target identity,
onset/window, priority, withholding/reveal condition, mechanism candidates,
selected mechanism, protected continuity constraints, provider controls, and
verification. Show how CPCS chooses among gaze, camera, focus, blocking,
lighting, sound, edit, contrast, motion, and depth based on capability and scene
constraints rather than duplicating every mechanism in the prompt.

## 6. Character/audience knowledge state

Research a safe distinction between:

```text
authored knowledge state
observed behavior
inferred mental state
```

Represent:

```text
audience knows threat
actor_A does not
actor_B does
```

Then:

```text
actor_A notices threat
```

causes a knowledge-state transition which motivates:

- gaze;
- head turn;
- facial response;
- posture;
- camera;
- edit;
- audio;
- dialogue.

Do not claim private mental-state observation from video.

### Application deliverable

Define separate ledgers for authored story truth, character knowledge, audience
knowledge, observed behavior, and interpreted mental-state hypotheses. Specify
subject, proposition, polarity, valid interval, source, confidence, and
transition event. An observed gaze or facial action may support but must not
prove that a character knows a proposition.

Show the complete application of `actor_A notices threat`: precondition,
knowledge-state delta, performance/camera/audio candidates, Canonical Score
fields, provider projection, and observable verification. Include a scene where
the same behavior admits two interpretations and CPCS preserves uncertainty.

## 7. Performer interaction

Research:

- proxemics;
- turn-taking;
- reaction latency;
- eye contact;
- gaze avoidance;
- mirroring;
- dominance/submission;
- interruption;
- gesture response;
- synchrony;
- social distance;
- touch;
- shared attention;
- leader/follower.

Represent interaction as a state/causal sequence rather than independent actor descriptions.

### Application deliverable

Define interaction identity and participant roles for dyads and groups. Separate
measurable timing/distance/gaze/touch from social interpretations such as
dominance or submission. For turn-taking, interruption, shared attention,
mirroring, reaction, and synchrony, define event boundaries, timebase,
side/actor ownership, confidence, and the next directing decision.

Provide one coordinated two-actor sequence with explicit latency and causal
links, one ambiguous social interpretation, and one occluded interaction that
must remain unobservable.

## 8. Audio world model

Research:

```text
word timestamps
WPM
syllables/sec
pauses
emphasis
prosody
voice position
distance
occlusion
room size
reverb
ambience
music beats
impact synchronization
```

Determine how sound participates in the spatial/causal world model.

### Application deliverable

Separate audio evidence, authored audio intent, detected events, measured
timing, inferred spatial properties, and provider controls. Define a shared
audio/video timebase, synchronization tolerance source, speaker/source identity,
diegetic status, location/frame, occlusion, propagation/reverb descriptors,
and uncertainty.

Show how an impact sound causes or motivates a reaction/attention/edit event,
how word timing constrains shot duration, and how missing or unsynchronized
audio changes the plan. Do not infer physical room dimensions from reverb
without a calibrated method and assumptions.

## 9. Editing motivation

Represent a cut as:

```text
from
to
time
motivation
narrative function
continuity requirements
eyeline
movement
screen direction
information reveal
```

Distinguish "cut at 3.4 seconds" from "cut because the reaction/reveal becomes the primary information."

### Application deliverable

Define cut identity, source/target shot, feasible time window, selected time,
motivation type, motivating event/evidence, narrative function, transition type,
continuity constraints, and evaluator expectation. Motivation is not a substitute
for executable timing, and timing alone is not a motivation.

Show selection among no cut, reframe, rack focus, and cut; capability negotiation;
and how eyeline, motion, screen direction, identity, or information-release
constraints veto an otherwise motivated edit. Include one cut whose selected
time changes after temporal re-solving without changing its motivation.

## 10. Complexity and information density

Research a windowed complexity representation:

```text
actors
simultaneous actions
contacts
camera complexity
physics complexity
style/VFX complexity
dialogue density
identity burden
spatial complexity
temporal density
```

Determine whether a generation-risk score is meaningful, and how to validate it.

### Application deliverable

Treat complexity features as observable/derived descriptors and any aggregate
generation-risk score as an experimental, provider-versioned prediction. Define
the window, feature formulas, normalization, missing values, interactions,
training/calibration data, outcome label, confidence interval, and drift/reprobe
rule. Do not assign intuitive universal weights.

Show how the result changes planning: split a shot, reduce simultaneous contacts,
defer an effect, select a different provider, or request review. Include a case
where high complexity succeeds and a low-complexity scene fails, demonstrating
why the score is not a deterministic feasibility fact.

## 11. Style invariants/freedoms

Research:

```text
invariants
allowed_variation
forbidden_drift
```

for:

- visual style;
- motion style;
- camera style;
- editing style;
- performance style;
- audio style;
- narrative style.

The objective is to preserve a style manifold rather than exact pixels.

### Application deliverable

Define each invariant or freedom at a named scope: project, scene, sequence,
shot, actor, object, camera, edit, performance, or audio. Specify whether it is
an authored hard constraint, soft preference, retrieved style principle,
creative choice, measured reference property, or experimental embedding-space
region. Define conflicts, precedence, allowed variation, drift detection, and
repair ownership.

Provide one allowed variation, one forbidden drift, and one ambiguous case that
requires human review. Explain what the provider receives and what the evaluator
can actually verify; do not equate embedding similarity with full style
preservation.

## 12. Salience-weighted representation

Research whether each world/control fact should carry:

```text
semantic salience
continuity salience
visual salience
temporal salience
provider importance
```

and whether this can support controlled prompt compression without semantic loss.

### Application deliverable

Define each salience axis independently and specify its author/estimator,
scale type, calibration, scope, and consumer. Do not collapse semantic,
continuity, visual, temporal, and provider importance into one unexplained
number.

Produce a compression algorithm or decision procedure with protected fields,
dependency closure, token/length budget, provider constraints, and a complete
loss ledger. Compare an uncompressed and compressed representation with a
semantic-equivalence report. Include a low-visual-salience fact that cannot be
dropped because it is continuity- or causality-critical.

## 13. World Model schema

Produce a complete schema sketch covering:

```text
intent
world
entities
relationships
style
space
time
performance
motion
camera
editing
audio
causality
continuity
verification
```

Then show how it maps into the existing CPCS score without creating a new semantic authority.

### Application deliverable

For every top-level field, state whether the World Model owns an execution-state
value, references another CPCS authority, carries a hypothesis, or caches a
derived value. Provide stable identity/reference rules, origin status,
observability, schema version, update/merge semantics, and cross-field
invariants. Define what is intentionally absent from the minimal World Model.

Show three mappings:

```text
World Model fact → Director decision → existing Canonical Score field
World Model fact → runtime-only validator input (no score field)
World Model hypothesis → no canonical write until resolved
```

Include minimal, realistic, invalid, and stale/conflicted instances plus exact
failure codes.

## Shared application fixture

Use one stable fixture throughout the packet:

```text
Actor A rotates toward a table and strikes a drinking glass with the right
forearm. The glass falls, breaks, and its shards remain on the floor. The impact
sound draws Actor B's attention after a constrained latency. The camera first
reframes to Actor B's reaction and then reveals the shards. The audience sees a
hazard that Actor A has not yet noticed.
```

Keep the causal spine unchanged. Use it to exercise persistent environment,
affordance/feasibility, contact, causal edges, actor and audience knowledge,
attention, audio synchronization, edit motivation, complexity, style
constraints, and salience compression. Assign stable IDs and label every value
by origin. Show at least one `unknown`, one `unobservable`, one rejected causal
edge, one fact protected from compression, and one post-generation correction.

## Required "how to apply" output

Include these packet-specific sections in addition to the master protocol:

1. `WORLD_MODEL_INCLUSION_POLICY` — admission, compression, retention,
   invalidation, and discard decision table.
2. `WORLD_MODEL_AUTHORITY_MATRIX` — owner/writer/consumer and conflict rules for
   VOG, World Model, Director, Canonical Score, KG, and provider adapter.
3. `WORLD_MODEL_RUNTIME_DECISION_TABLE` — condition, consulted state/edge,
   decision, canonical effect, verification, and failure behavior.
4. `END_TO_END_CAUSAL_SCENE_TRACE` — the shared fixture from dense candidates to
   acceptance or repair.
5. `MINIMAL_WORLD_MODEL_VERTICAL_SLICE` — smallest build proving persistence +
   causal decision + attention/edit consequence + verification.
6. `COMPRESSION_EQUIVALENCE_REPORT` — retained/dropped facts, dependency closure,
   and measured semantic loss.
7. `DEFERRED_SCOPE_AND_FALSIFICATION` — excluded features and evidence that
   would justify or reject them.

## Final requirement

This research should answer:

> What is the smallest persistent world representation that lets CPCS reason causally about a scene instead of merely retrieving prompt concepts?

End with `CPCS_CLOSURE_MATRIX` and `PROPOSED_AGENT_BUILD_PACKET`.


## Research execution rules

Use the attached frozen package as the primary corpus, but independently verify important claims with primary sources. Do not silently "fix" the package. Explicitly distinguish package-derived claims, external-source findings, proposed CPCS representations, and experimental hypotheses.

The objective is not a literature review. The objective is to close implementation-relevant semantic gaps with enough precision that a coding agent can extend the existing CPCS tree without inventing a competing authority.

You MUST apply the output contract in `00_MASTER_DEEP_RESEARCH_PROTOCOL.md`.
