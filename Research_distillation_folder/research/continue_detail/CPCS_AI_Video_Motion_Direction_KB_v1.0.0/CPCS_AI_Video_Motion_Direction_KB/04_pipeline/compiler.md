# CPCS Compiler

## Inputs

- creative brief and exclusions;
- actors, objects, environment, duration, aspect ratio, and target model(s);
- optional reference images/video/audio;
- selected culture/context/style profiles;
- safety, continuity, identity, and product constraints.

## Passes

### Pass 1 — Intent planning

Generate an intent distribution and 2–5 candidate realizations. Reject actions that violate scene constraints. Record ambiguity rather than prematurely collapsing it.

### Pass 2 — Narrative and affect

Build ordered beats, causal state changes, and per-channel VAD+confidence/certainty/engagement trajectories.

### Pass 3 — Body/BESS and primitives

Select body organization, Bartenieff connectivity, BESS factors, primitives, and actor-specific ranges.

### Pass 4 — Phase and interaction

Instantiate phase state machines and bind contacts, grasps, support, releases, impacts, and reactions. Solve interaction causality before camera/style.

### Pass 5 — Kinematics/force priors

Attach metric trajectories when supplied; otherwise use actor-relative priors. Mark every value as measured, estimated, visual proxy, or prompt prior.

### Pass 6 — Rhythm/camera/style

Align phases to clocks/beats; establish action axis, shot coverage, impact sync, and style transforms while locking invariants.

### Pass 7 — Validation

Run schema and semantic checks. Produce errors, warnings, and waivers.

### Pass 8 — Adapter downcast

For each target adapter, choose native controls, references, prose, or postprocess. Produce request payload, prompt, negative constraints, and loss report.

## Conflict resolution

Priority order:

1. safety/legal/rights constraints;
2. explicit interaction/contact and object-state constraints;
3. actor capability/joint limits;
4. narrative causality and identity;
5. timing/camera continuity;
6. style and decorative effects;
7. model-specific optimization.

## Outputs

- canonical JSON;
- YAML creative-intent view;
- XML ordered-beat view;
- human-readable prose brief;
- per-model request/prompt/reference plan;
- validation report;
- control-loss report;
- experiment template.

## Determinism

Given the same canonical scene, adapter snapshot, compiler version, and derived-weight version, compilation should be deterministic. Stochastic idea generation belongs upstream and must materialize a selected canonical plan before downcasting.
