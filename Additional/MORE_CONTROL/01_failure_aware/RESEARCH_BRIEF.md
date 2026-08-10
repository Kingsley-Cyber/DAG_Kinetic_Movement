# Deep Research Prompt — Failure-Aware Control and Mitigation for AI Video Generation

Act as a principal generative-video researcher, diffusion-model engineer, computational animator, movement scientist, cinematography systems designer, multimodal evaluation researcher, prompt-language compiler engineer, and ontology architect.

## Mission

Produce a source-grounded, experimentally actionable research package on:

> **Failure modes in current text-to-video, image-to-video, reference-to-video, and multimodal video-generation systems, with emphasis on why the failures occur and how they can be prevented, reduced, detected, isolated, or repaired through prompting, structured compilation, reference conditioning, shot decomposition, control media, postproduction, and closed-loop verification.**

The research must support the CPCS universal video-intent compiler and its provider-specific adapters.

Do not produce a generic list of AI artifacts. Build a detailed failure taxonomy connected to:

* triggering scene conditions;
* likely model or representation causes;
* observable symptoms;
* prompt-level mitigation;
* canonical-score requirements;
* provider-adapter behavior;
* reference or control-media strategies;
* clip decomposition strategies;
* verification metrics;
* localized repair procedures;
* empirical confidence;
* remaining limitations.

The goal is to answer:

> Given a requested video event, what situations are likely to cause a video model to invent, merge, omit, reverse, deform, teleport, duplicate, obscure, or incorrectly resolve visual information, and what is the most reliable intervention for each failure?

---

## Mandatory repository context

Before external research, inspect the current repository and map existing ownership.

Read at minimum:

```text
AGENTS.md
ARCHITECTURE.md
REPO_CONTINUITY_IMPLEMENTATION_PLAN.md
lab/AGENTS.md
lab/CONTROL_SURFACE.md
lab/FORMAT_CONTROL_MAP.md
lab/UNIVERSAL_MOTION_SKELETON.md
lab/blocks.yaml
lab/concepts.jsonl
CPCS-MX research paper and RAG package
CPCS FACS–Laban research paper and RAG package
Pegasus atomic video deconstruction research
ontology-driven multimodal direction manual
kinetic motion direction manual
```

Search existing materials for:

```text
failure
hallucination
occlusion
identity drift
object permanence
temporal consistency
spatial reasoning
axis reversal
contact
penetration
foot skating
camera entanglement
motion blur
splash
smoke
flash
transformation
multi-actor
action order
prompt overload
overconstraint
underconstraint
verification
repair
```

Create an overlap matrix:

```text
failure_id
existing_owner
existing_coverage: complete | partial | absent | conflicting
missing_evidence
missing_mitigation
missing_test
recommended_owner
```

Do not create a parallel CPCS schema, second compiler, or separate ontology when an existing owner can be extended.

---

## Scope

Cover at least these generation modes:

```text
text-to-video
image-to-video
first-frame-conditioned video
first-and-last-frame video
reference-image-conditioned video
reference-video-conditioned generation
video-to-video transformation
multi-shot generation
audio-video joint generation
pose/depth/mask/control-video-conditioned generation
```

Cover realistic, cinematic, UGC, product-demonstration, dialogue, anime, stylized action, VFX, and multi-actor scenes.

Model families must include currently available or documented versions of, where access or reliable evidence exists:

```text
Seedance
LTX Video
Kling
Veo
Runway
Hailuo/MiniMax
Wan
CogVideoX
HunyuanVideo
Mochi
other relevant open or commercial systems
```

Verify exact model names, versions, dates, interfaces, limits, and supported inputs from official sources. Do not infer capabilities from marketing language or community anecdotes.

Separate:

```text
officially documented capability
peer-reviewed or preprint experimental result
independent benchmark result
controlled repository observation
community anecdote
unverified claim
```

---

# Research Area A — Occlusion and Hidden-State Hallucination

Study failures caused when an actor or object becomes hidden by:

```text
water splash
smoke
dust
fire
debris
cloth
hair
another actor
foreground object
motion blur
camera whip
impact flash
darkness
lens flare
cut
frame exit
submersion
transformation effect
```

Investigate:

1. Why do models treat temporary occlusion as permission to reconstruct the scene?
2. Under what conditions do they:

   * duplicate the hidden subject;
   * change identity or clothing;
   * alter pose;
   * teleport;
   * introduce an extra action;
   * remove the subject;
   * make the subject reappear at an incorrect location;
   * merge the subject with the occluder?
3. How should a prompt encode:

   * pre-occlusion state;
   * entry trajectory;
   * hidden interval;
   * continued latent path;
   * reappearance state;
   * actor count;
   * identity continuity;
   * spatial continuity?
4. Compare:

   * complete versus partial occlusion;
   * short versus long occlusion;
   * static versus moving occluder;
   * transparent versus opaque effects;
   * text-only versus image/reference conditioning.
5. Determine whether continuity improves when the hidden subject remains visible as:

   * silhouette;
   * mask;
   * shadow;
   * bubble trail;
   * partially visible limb;
   * tracked control signal.

Define an **Occlusion Continuity Contract** with fields such as:

```text
subject_id
pre_occlusion_state
occluder
occlusion_start
occlusion_end
hidden_motion_path
expected_reappearance_region
identity_lock
actor_count_lock
state_change_allowed
state_change_forbidden
visibility_bridge
```

---

# Research Area B — Object Permanence and State Persistence

Study whether models retain:

```text
same actor
same prop
same clothing
same injury state
same object count
same object dimensions
same water level
same destruction state
same open/closed state
same held item
same environmental layout
```

Investigate failures involving:

* object disappearance;
* duplicate objects;
* spontaneous object creation;
* object replacement;
* object-state reset;
* size drift;
* color or material drift;
* hand-object detachment;
* products changing shape during use;
* weapons or props changing hands;
* reflections becoming physical duplicates.

Determine how persistence should be represented across:

```text
frames
beats
shots
cuts
occlusions
transformations
multi-shot clips
separately generated clips
```

Design a **State Ledger** and measurable object-permanence tests.

---

# Research Area C — Identity, Role, and Actor-Assignment Failures

Study:

```text
face drift
hair drift
costume drift
body-proportion drift
actor duplication
actor fusion
role swapping
attacker/defender reversal
left/right actor confusion
target confusion
voice identity drift
character mannerism drift
```

Investigate why multi-actor scenes are especially vulnerable during:

* close contact;
* crossed limbs;
* grapples;
* rapid cuts;
* motion blur;
* similar clothing;
* camera rotation;
* actor crossing;
* off-screen exits and re-entry.

Compare mitigation through:

```text
distinct wardrobe/color coding
stable actor IDs
screen-side locks
depth lanes
reference sheets
separate actor references
face references
start-pose images
explicit role labels
shot decomposition
avoiding actor crossings
```

Define identity and role verification metrics that do not rely only on facial similarity.

---

# Research Area D — Spatial Reasoning and Screen Geography

Study failures in:

```text
left/right relationships
front/behind
above/below
near/far
screen side
world position
depth ordering
camera-relative versus world-relative direction
axis of action
eyelines
entrances and exits
target regions
actor distance
```

Investigate:

1. Why does “A attacks left-to-right” often fail after a cut or camera move?
2. When does the model confuse:

   * actor-relative left;
   * viewer-relative left;
   * world direction;
   * camera direction?
3. How should spatial constraints survive:

   * pans;
   * orbits;
   * reverse angles;
   * tracking shots;
   * close-ups;
   * sky-to-ground tilts?
4. Compare natural-language spatial instructions with:

   * normalized screen coordinates;
   * lane descriptions;
   * bounding boxes;
   * masks;
   * keyframes;
   * depth maps;
   * pose tracks.

Define a **Spatial State Transition Contract**, not merely a list of positions.

---

# Research Area E — Temporal Order and Action-Graph Collapse

Study failures where models:

```text
omit actions
merge multiple actions
repeat actions
reverse event order
begin reaction before cause
skip recovery
fill unused time with invented action
compress a long sequence into one gesture
perform simultaneous actions that should be sequential
```

Analyze:

* action density per second;
* number of actors;
* number of dependent events;
* clip duration;
* event similarity;
* prompt length;
* exact timestamps versus relative ordering;
* single-shot versus multi-shot generation;
* effect of words such as “then,” “only after,” “before,” and “while.”

Test whether the strongest representation is:

```text
ordered prose
flat YAML timeline
JSON event array
XML event graph
reference storyboard
pose/control sequence
separate clip generation
```

Define limits such as:

```text
maximum primary actions per second
maximum sequential dependencies per clip
maximum simultaneous actor actions
minimum visible setup and recovery duration
```

Do not invent universal limits. Establish provider- and task-specific empirical ranges.

---

# Research Area F — Causality and Reaction Failures

Study failures where visual consequences do not follow their causes:

```text
recoil before near-contact
splash before water entry
debris without collision
fall without loss of balance
water column from the wrong location
camera shake without impact
sound before action
object moves before being touched
character reacts to the wrong attacker
```

For every event, distinguish:

```text
cause
initiator
target
onset
apex
consequence
reaction delay
recovery
secondary effects
```

Develop a causal-event graph and determine when explicit statements such as:

> B dives first; A’s kick misses B; the kick hits only the water; the water strike creates the column.

outperform compressed statements such as:

> Axe kick, splash, B submerged.

---

# Research Area G — Contact, Penetration, and Interaction Geometry

Study:

```text
false contact
missing contact
body penetration
limb intersection
floating hands
grip drift
contact without reaction
reaction without contact
incorrect target body part
inconsistent interaction distance
```

Separate:

```text
physical contact
simulated virtual impact
staged near-contact
camera-cheated contact
effect-obscured near-contact
grasp/support contact
surface contact
```

Investigate prompt and control strategies for:

* minimum separation;
* contact frame;
* target region;
* actor reaction delay;
* projected screen overlap versus world-space distance;
* camera placement;
* occlusion used to conceal safe near-contact.

Design verification for:

```text
minimum actor distance
penetration duration
contact-target accuracy
reaction latency
limb separability
silhouette readability
```

---

# Research Area H — Balance, Support, Weight, and Momentum

Study:

```text
foot skating
floating
weightless landings
instant direction changes
unmotivated launches
incorrect center of mass
missing support foot
impossible recovery
constant-speed motion
rubber-body deformation
momentum disappearing between frames
```

Investigate how to express or approximate:

```text
support state
base of support
weight transfer
takeoff
flight
landing
deceleration
recoil
follow-through
settle
```

Distinguish real physical simulation from cinematic or anime perceptual physics.

Research when stylized scenes should retain:

```text
causal skeleton
contact timing
screen trajectory
landing target
action order
```

while permitting:

```text
smears
holds
perspective distortion
time suspension
deformation
exaggerated environmental response
```

---

# Research Area I — Fluid, Cloth, Hair, Debris, and Material Interaction

Study model behavior for:

```text
water entry
surface displacement
splash generation
submersion
buoyancy
ripples
water columns
wet clothing
smoke
dust
cloth follow-through
hair overlap
debris trajectories
glass
mud
snow
fire
```

Focus especially on solid–fluid transitions.

Determine common failures:

* fluid treated as a solid surface;
* actor standing on water unintentionally;
* splash appearing without displacement;
* water column following the actor rather than impact point;
* submerged actor disappearing;
* fluid effects spawning duplicate limbs or faces;
* water plane changing height or topology;
* ripples not centered at contact;
* effects persisting longer than their cause.

Design material-specific prompt primitives and verification fields.

---

# Research Area J — Camera and Actor-Motion Entanglement

Study failures where:

```text
camera pan becomes actor movement
tracking shot freezes actor locomotion
camera orbit reverses screen direction
impact shake deforms subjects
zoom changes subject size inconsistently
tilt causes actors to teleport vertically
motion blur destroys identity
```

Determine how to separate:

```text
world-space actor motion
screen-space actor motion
camera translation
camera rotation
lens or zoom
edit
impact impulse
background motion
```

Research which camera instructions can safely coexist with complex choreography and which should be split into separate shots.

---

# Research Area K — Cuts, Flashes, Smears, and Scene-Reset Failures

Study how models interpret:

```text
hard cut
impact flash
one-frame monochrome frame
smear drawing
speed-line background
whip pan
full-frame splash
smoke wipe
transformation burst
black frame
```

Investigate when effects are interpreted as:

* new shot;
* new scene;
* identity reset;
* costume transformation;
* character duplication;
* change of art style;
* spatial teleport.

Define a distinction between:

```text
graphic discontinuity
camera cut
world-state discontinuity
temporal hold
motion-blur interval
occlusion interval
```

Design syntax and reference strategies that permit anime deformation while restoring correct anatomy immediately afterward.

---

# Research Area L — Anatomy and Stylization Recovery

Study:

```text
extra limbs
missing limbs
joint inversion
face melting
permanent smear anatomy
changing body proportions
limbs reconnecting incorrectly
perspective enlargement persisting
```

Investigate controlled deformation contracts:

```text
affected body region
deformation onset
source pose
destination pose
maximum deformation
one-frame or multi-frame exposure
silhouette anchors
required anatomy recovery frame
```

Determine how to preserve action readability without forcing continuous realistic anatomy during authored anime accents.

---

# Research Area M — Prompt and Serialization Failure

Research how failures vary with:

```text
natural language
Markdown
flat YAML
nested YAML
XML
JSON
XML containing JSON
XML containing YAML
duplicate semantic representations
negative prompts
long prompts
short prompts
provider character limits
```

Separate:

* whether the provider officially supports structured input;
* whether structure merely improves semantic boundaries;
* whether duplicated formats overload attention;
* whether nesting consumes useful token budget;
* whether exact numeric values are ignored;
* whether contradictory fields trigger improvisation;
* whether negative instructions introduce the forbidden concept.

Study:

```text
semantic density
attention competition
priority dilution
instruction conflict
field omission
order sensitivity
format token overhead
provider-specific parsing behavior
```

Build controlled A/B tests with identical semantics across formats.

Do not claim that XML, YAML, or JSON universally improves model intelligence.

---

# Research Area N — Constraint Overload and Under-Specification

Study two opposing failure modes.

## Overconstraint

Symptoms:

```text
stiff motion
ignored instructions
averaged behavior
broken anatomy
failure to complete the scene
random selection among constraints
```

Causes may include too many:

```text
exact events
hard constraints
camera moves
actors
effects
negative conditions
spatial locks
format repetitions
```

## Under-specification

Symptoms:

```text
hallucinated filler
new attacks
random gestures
teleportation
scene changes
unmotivated effects
unwanted dialogue
```

Determine the minimum sufficient specification for:

```text
identity
start state
event order
causal links
hidden transitions
end state
allowed variation
forbidden variation
```

Develop an attention-budget compiler that decides when to:

* compress;
* simplify;
* split the clip;
* bake information into a reference;
* move an effect to postproduction;
* retain a field only for verification.

---

# Research Area O — Audio and Cross-Modal Synchronization

Study:

```text
impact sound timing
speech/lip mismatch
voice identity drift
music accent misalignment
breath timing
water sound without splash
sound generated for nonexistent action
visual event with no corresponding audio
```

Separate audio-generation failure from visual-generation failure and define cross-modal event anchors.

---

# Research Area P — Verification and Evaluator Failure

Do not assume the evaluator is correct.

Study:

```text
VLM misses fast action
VLM invents contact
actor tracker swaps identities
shot detector mistakes flash for cut
pose detector fails on anime
segmentation treats reflection as actor
physics metric rewards visually wrong output
human raters disagree
```

For every metric, define:

```text
observable dimension
measurement method
evaluator/version
confidence
known blind spots
human calibration requirement
failure threshold
```

Compare:

```text
action-graph agreement
temporal event error
actor-count consistency
identity continuity
screen-direction consistency
contact-distance error
foot-slip distance
object permanence
camera agreement
material-response consistency
human readability
```

Require raw generated videos, failed samples, prompts, seeds where available, model versions, and exact evaluation methods.

---

## Mitigation hierarchy

For every failure, classify the best mitigation level:

```text
L0 wording repair
L1 structured prompt repair
L2 canonical event/state contract
L3 reference image or storyboard
L4 pose, mask, depth, trajectory, or control video
L5 shot decomposition
L6 postproduction/compositing
L7 regenerate only failing interval
L8 provider/model substitution
L9 unsupported—cannot be controlled reliably
```

Do not recommend “add more prompt detail” by default.

For each mitigation report:

```text
expected benefit
token or character cost
generation-cost impact
risk of new failure
provider dependency
evidence strength
verification method
rollback
```

---

## Required empirical program

Design controlled experiments rather than relying only on literature.

### Core variables

```text
provider/model/version
text-to-video versus image-to-video
prompt format
prompt length
action count
actor count
occlusion type
occlusion duration
camera complexity
effect density
reference availability
seed
clip duration
aspect ratio
```

### Minimum ablation families

1. **Occlusion continuity**

   * no splash;
   * narrow partial splash;
   * complete splash;
   * complete splash plus visible silhouette;
   * complete splash plus explicit hidden path.

2. **Format**

   * natural language;
   * flat YAML;
   * XML;
   * JSON;
   * XML+JSON;
   * XML+JSON+YAML.

3. **Action density**

   * one action;
   * three actions;
   * five actions;
   * full sequence.

4. **Spatial control**

   * verbal left/right;
   * explicit lanes;
   * normalized coordinates;
   * reference storyboard.

5. **Causality**

   * compressed event description;
   * ordered cause-and-effect statement;
   * action graph.

6. **Repair**

   * full regeneration;
   * localized repair prompt;
   * shot split and edit;
   * postproduction effect replacement.

Use repeated seeds. Report success distributions, not one selected render.

---

## Required failure record schema

Design a machine-readable record similar to:

```json
{
  "failure_id": "failure://occlusion/hidden_state_reconstruction/1",
  "name": "Hidden-state reconstruction hallucination",
  "scope": {
    "provider": null,
    "model": null,
    "workflow": ["text_to_video", "image_to_video"]
  },
  "trigger_conditions": [],
  "observed_symptoms": [],
  "suspected_causes": [],
  "evidence_class": "benchmark | paper | controlled_test | anecdote",
  "source_refs": [],
  "canonical_fields_affected": [],
  "prompt_risk_patterns": [],
  "mitigations": [
    {
      "level": "L3",
      "method": "",
      "evidence_strength": "",
      "limitations": []
    }
  ],
  "verification_metrics": [],
  "regression_fixtures": [],
  "provider_specific_notes": [],
  "unresolved_questions": []
}
```

---

## Source policy

Prioritize:

1. official model papers, technical reports, documentation, model cards, and API documentation;
2. peer-reviewed papers and benchmark publications;
3. official benchmark repositories and evaluation code;
4. controlled independent evaluations with disclosed prompts, seeds, versions, and samples;
5. qualified animation, cinematography, graphics, biomechanics, and HCI research;
6. community observations only as hypotheses for controlled tests.

Do not use promotional reels as proof of reliability.

Do not use search snippets as final evidence.

For every model-specific claim, record:

```text
provider
model
version
release date
workflow
documented input modes
documented duration/resolution limits
source
access date
confidence
```

Mark conclusions that cannot be verified with 100% certainty.

---

## Required outputs

Produce:

```text
README.md
FAILURE_TAXONOMY.md
FAILURE_CAUSE_MODEL.md
OCCLUSION_AND_HIDDEN_STATE_FAILURES.md
IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md
SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md
TEMPORAL_ACTION_CAUSALITY_FAILURES.md
CONTACT_BALANCE_AND_PHYSICS_FAILURES.md
FLUID_MATERIAL_AND_VFX_FAILURES.md
CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md
PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md
AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md
MITIGATION_HIERARCHY.md
PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv
FAILURE_MITIGATION_MATRIX.csv
SOURCE_CATALOG.csv
CLAIM_SOURCE_MATRIX.csv
FAILURE_RECORDS.jsonl
FAILURE_RECORD.schema.json
EVALUATION_METRICS.schema.json
EXPERIMENT_AND_ABLATION_PLAN.md
PROMPT_COMPILER_RULES.md
SHOT_DECOMPOSITION_RULES.md
LOCALIZED_REPAIR_PLAYBOOK.md
CPCS_INTEGRATION_RECOMMENDATIONS.md
UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL.md
```

---

## CPCS integration requirements

For every verified failure, identify effects on:

```text
intent normalization
profile routing
canonical score
event graph
spatial state
identity ledger
continuity ledger
provider capability profile
serialization strategy
prompt compression
loss report
verification plan
repair planner
experiment registry
```

Determine whether each finding is:

```text
knowledge_only
contract_affecting
implementation_affecting
provider_version_affecting
verification_affecting
policy_affecting
unverified
```

Research may generate implementation proposals but must not directly change production authority.

---

## Acceptance criteria

The research is complete only when:

1. Occlusion is modeled as a hidden-state continuity problem, not only a negative-prompt problem.
2. At least 30 distinct failure modes are documented.
3. Every failure has trigger conditions, observable symptoms, causes, mitigations, and verification methods.
4. Object permanence, actor identity, role assignment, spatial relations, event order, causality, contact, support, camera, materials, VFX, anime deformation, and audio are covered separately.
5. Prompt-level mitigation is distinguished from reference/control-media and shot-decomposition mitigation.
6. Provider-specific behavior is version scoped.
7. Official capability claims are separated from empirical reliability.
8. Structured formats are tested without assuming universal superiority.
9. At least one repeated-seed ablation is designed for each major failure family.
10. Failed outputs are retained as evidence.
11. Exact model compliance is never inferred from a successful showcase.
12. Every proposed CPCS field or compiler rule has an existing owner or justified minimal extension.
13. A closed-loop workflow is specified:

```text
canonical target
→ provider-specific compile
→ generation
→ re-extraction
→ failure classification
→ localized repair
→ re-verification
→ immutable experiment record
```

14. The final report explicitly distinguishes:

```text
preventable by prompting
partially mitigated by prompting
requires visual/control conditioning
requires shot decomposition
requires postproduction
currently unreliable or unsupported
```

## Final research question

Conclude with an evidence-backed answer to:

> What is the minimum sufficient state, event, spatial, identity, causal, and visibility representation needed to stop a generative video model from inventing information during visually ambiguous transitions, and when must the system abandon prompt-only generation in favor of references, control media, shot decomposition, or postproduction?
