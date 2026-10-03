# Owner inputs (2026-10-02), in full

The implementer must read these as intent, not as suggestions. Where an input conflicts with an
older file in the tree, the input wins and `DECISIONS.md` records the override.

## 1. Purpose

"I do AI video deep research workflows trying to find meta ways to prompt and communicate with an
AI video model to bypass the weak prompt outputs. I do the research and the intent of the repo is
to cannibalize it and make the nuances part of prompt creation, and it must know how users'
language maps to the deep latent knowledge."

## 2. What the kitchen must become

An elite "kitchen" that is a strong, accurate compiler using research to create a proper prompt,
plus a reasoning control layer so any LLM understands how to use the research: the abstract layer
(why a technique works) and the semantic layer (what the model actually reads).

## 3. Model architecture awareness

The compiler should understand how video models read a prompt: rewriters, caption-style training
text, token limits and negation, temporal compression, reference images (out of scope for now),
and priors. Per-model profiles with every fact tagged documented / measured / guess.

## 4. Reasoning and friction points

Modular prompting; motion, movement and hands as friction points; an overall logical pass on what
the prompt is actually prompting; layered reasoning that is granular but coherent; compile to
natural language or a structured format; research-grounded motion and Laban prompting (the
hardest to compile); mathematical calculations, science scales, thinking types and creative
lenses.

## 5. Dynamics and ingest

Diversity so the compiler varies prompts for different users and their ideas; a research-ingest
control layer that knows how to expand and integrate itself for future prompting. Layers grow:
color, world, and more.

## 6. Layer taxonomy (owner's A–F, now sub-modules of the passes)

A Narrative intent (action, objective, obstacle, relationship, subtext, beat changes, audience
information) · B Dimensional affect (valence, arousal, dominance) · C Visible performance (FACS
and timing; head, gaze, blink, speech; body actions and postures; Laban Body, Effort, Shape,
Space; gesture and asymmetry) · D Motion realization (root path and facing, joint motion, phase,
contact, support and balance, speed/acceleration/force, constraints between people, props, set) ·
E Cinematic presentation (camera, lens, focus, framing, shot length, cuts) · F Generative
conditioning (text, control signals, pose or depth, camera data, reference images, audio).

"Laban is missing weights": the Weight factor must be listed; each quality needs a strength
number; each layer needs an importance weight.

## 7. The 14 passes + synthesis (owner's pasted design, adopted by name)

Intent & Narrative · World & Environment · Entity & Identity · Action & Motion · Interaction &
Contact · Performance & Expression · Space & Staging · Time & Rhythm · Physics & Causality ·
Camera & Composition · Attention & Information · Continuity & State · Style & Presentation ·
Audio & Dialogue · Cross-Domain Director Synthesis. Plus Light & Color (owner: "light and color").

Each pass: knowledge mode research-backed / reasoning-backed / mixed; origin tags on every
decision; the same eight-step pattern; a pass planner (mandatory / conditional / optional);
provider adaptation and formatting are downstream, never passes. World answers "how should the
surrounding world respond to what happens" (pool example: trajectory → surface contact →
displacement → splash → ripples → wet clothing → resistance → sound → persistent wetness).

## 8. Router, not DAG

"Your current architecture is a retrieval and relay system: understand intent → identify
domain/section → open the article by id → hand the LLM exactly the material it needs… Claude Code
already is the reasoning graph." Adopt declared dependency as data (interfaces in frontmatter, one
machine map, flat decision/loss records), not a graph executor. Adopt a graph mechanism only when
query logs show a failure class the router cannot fix.

## 9. Shot stack and tiers

Shot stack: 01 shot intent · 02 composition/blocking · 03 camera · 04 character motion ·
05 contact/physics · 06 performance · 07 environment motion · VFX …

Three output tiers: Reason (beat graph + action integrity), Style (sref-tinted priorities per beat,
e.g. silhouette 0.8, anticipation 0.7, impact 0.9), Render (UGC texture + continuity locks). Ship
Reason first. "Order beats first, then apply UGC texture to the rendering — not the other way
around." Each tier independently testable: valid beat orders; readable silhouettes; non-morphing
objects.

Logical action pathway (R3 in the owner's text): grip contact → force transfer → state change →
continuity check; the engine refuses a prompt where a beat jumps directly to the completed state;
reusable per object type; pose-to-pose (decide the end state first); minimum anticipation → action
→ aftermath; "play one action at a time".

Sakuga: design for perceptual motion (held cels, key poses, smears, impact flashes, rhythm
breaks); the prompt says which frames matter and in what order; silhouette and simplicity first;
prompt for motion grammar, not anatomy; short motion-focused clips.

## 10. Time and beats ("the big one")

Steerable beat production with diversity; no single formula; never squeeze a 30 s idea into 10 s.
Master clock in seconds; frame and musical clocks derived. Hierarchy sequence → scene → phrase →
exchange → action → phase → micro-event → frame. Independent rhythm fields (tempo, tempo curve,
cadence, meter, beat phase, syncopation, micro-pauses, anticipation beats, accent strength, event
density, swing, rubato, entrainment, phase lock). Timing profiles snappy_24fps, floaty_24fps,
anime_limited (conventions). `impact_frames = anticipation + strike + hold + settle`. Emotional
formula: slow onset 6–12 f + long key-pose hold 2–12 f + minimal smear + long settle 8–18 f + wide
establishing shot before the apex + rest periods; slow element inside a fast context. Fight
granularity: superhero low density, kung fu maximal, boxing metered. The six questions: register,
directorial beats, tempo curve, micro-pauses and anticipation, apex density, variation.

## 11. Text-only, calculations, structured modes

"Right now mocap isn't being used; we are strictly talking text generation, and some calculations
will be in research papers that can be used to reason and generate prompts." Mode C compiler
(parses, validates, rejects unsupported or unverified controls) emitting Mode A text; the existing
reasoning-policy layer stays as thinking modes; what was missing is the decision-semantic bridge
problem → treatment → decision → control → expected visual effect → verification. Reasoning
decides; the control layer emits and validates. Control surfaces: native, reference_conditioned,
prompt_only, postprocess, unsupported, unknown, legacy; levels L0–L5 (text reaches L0–L1). No
format or reasoning operator is globally superior; thresholds need experiments.

## 12. Movement text control: Laban, Bartenieff, film grammar

Three layers with independent dials: Laban (quality), Bartenieff (origination and connectivity),
film grammar / cinematography (camera, mandatory). Laban output is Bayesian and scaled, never
absolute terms. Laban has a cause-and-effect sub-layer, "impact and physics language", producing a
contact-and-recoil layer with explicit stated reactions rather than assumptions.

World bundle (gravity, terrain, mass, camera distance, momentum source, frame discipline) →
Effort (4 factors) × Shape (Door, Table, Wheel planes) × Body (Bartenieff six patterns) →
constraint compiler → strength-scaled emitter (strong: full constraint set; weak: 3–5 core lines +
camera/continuity compensation). Anti-arcade signatures: single-plane motion, zero anticipation,
momentumless impact, unbroken bound flow. Priority: Effort quantification → anti-arcade detectors
→ Bartenieff pathways → strength-adaptive emitter → world bundle.

Relative prompting: always use anchors; one escalating unit relative to the anchor, never two
absolutes.

## 13. Semantic core and dialects

A model-agnostic semantic core with a dialect per model: Hailuo ("h3"), Seedance, Kling,
Gemini/Veo, Wan. Seedance first.

## 14. References supplied

LaMoGen (arXiv 2509.24469), Guo et al. 2022 Laban-based motion classification, bodily expressed
emotion via LMA (S2666389923001854); Bartenieff Fundamentals overviews (Wikipedia; Academia
"Using LMA Effort to Enhance Body Connectivity"; laban-analyses.org). Laban has AI-side evidence;
Bartenieff is untested vocabulary; Laban AI label sets: byebye_dab/glide/flick/float; Effort
Space direct/indirect, Time sudden/sustained, plus Weight and Flow.

## 15. FACS and BESS

FACS specifies which muscles are active (the action units); laterality (bilateral or one-sided);
intensity on an A-through-E scale; the temporal phases onset, apex, offset (the timing of the
movement rising and falling); co-occurrence (which action units fire together, since real
expressions are combinations, not one isolated unit); plus head pose, gaze direction, and
visibility or occlusion of the action. "FACS is genuinely a spatiotemporal event description, much
closer to the richness of a motion-capture log than a simple label."

Laban has four Effort controls (Weight, Time, Space, Flow) inside the BESS framework: Body,
Effort, Shape, Space.

Requested detail (2026-10-02): Bartenieff's six patterns, Shape planes, FACS, and valence–arousal
each specified in the plan (ARCHITECTURE §3.5.2, §3.5.4–3.5.6; CONTROL_LAYER R-34…R-40;
TASKS T27–T29).

## 16. Specialized physics layer (cause and effect)

Its own layer because models render plausible footage and do not simulate physics; action and
reaction come out as loosely associated visuals (a splash that does not happen, a stomp that lands
in front of the face, a zipper that moves but never opens). Every causal event has the same parts
in order: trigger → contact → force quality (Laban weight and time, anchored to a baseline) →
primary reaction → secondary reactions → settle. Writing rules: state the contact point; order
the sentence cause, reaction, settle with connectors; one causal event per beat; name the end pose
when it matters; anchor force relatively. Capability check tags contact types by risk (low:
splashes, debris, cloth, hair; medium: body-on-body strikes, awkward falls; high: fine mechanisms,
graphic contact, exact choreography) and degrades unreliable cases (wind-up then cut, reaction
shot, hiding angle) instead of failing, logging the downgrade. Adopt `contact_state`
(physical_contact_confirmed, near_contact, occluded_contact, editorial_impact, unknown),
`depends_on`, `must_not_imply`, an edge-admission rule (no effect without a named cause), and
upstream repair. Eval log with three yes/no scores (contact happened, reaction followed, end pose
sane), three or more seeds per prompt. Failures registry seeded with the A/B/C stomp test. Defer
the full typed graph, five sub-compilers, trajectory splines, newtons and biomechanics; test
"one causal event per clip" before making it a rule. Treat every rule as a hypothesis until runs
confirm it; automatic physical-commonsense checking is unsolved (VideoPhy-2).

## 17. Agnostic first, dialects as lenses; the Hailuo ("h3") emphasis levers

"It's agnostic first and then we add model dialects as lenses to be used." Dialect knowledge is
stored per model as intent → lever with evidence. Owner's Hailuo observations (not extensively
tested, relative merit unknown): words can be stressed with `<i></i>` or `<emphasis></emphasis>`
around the word, or with asterisks around *key words*, though the model sometimes reads asterisks
as a bleep for a swear word. Stored in `director/profiles/hailuo.yaml` as `owner_observed`.

The reasoning control layer must say how to think per pass (modes, router features, the six time
questions, anchors) and how to use the dialect lens during model fit without writing model syntax
into the IR (`director/protocol.md` §4b–4c).

## 18. Why knowledge is thin, and the fix

"The reason knowledge is thin is because the coding model must know how to take a deep research
and add upon or refactor upon the compiler with rules." The owner's deep-research prompts (e.g.
the DMR Gap Closure prompt) already demand the right shape: for every gap, a decision path from
scene condition to emitted control to observed result, each step labelled by kind, with the exact
runtime owner and smallest executable consumer; definitions without a decision path are
insufficient; statuses closed / implementable_now / requires_experiment / unknown / deferred /
rejected; a shared fixture traced end to end; acceptance and falsification. `plan/INGEST.md` makes
that the compiler's intake procedure.

## 19. Camera movements

"All of these camera movements must be known to the models for decision-making prompts":
aicameramovements.com (46 moves, 7 categories, one prompt each in a Movement / Speed / Framing /
End grammar). Stored as `director/vocab/camera_moves.yaml` with layer (motion vs optics vs
special), the research's motion kind, and a function hint per move; used by the camera pass via
`camera.move_from_catalog`.

## 20. On old plans

"Be careful with any old plans being integrated as it can misalign the current plan." Audit in
`DECISIONS.md` (admission ledger, overrides, not-doing list).
