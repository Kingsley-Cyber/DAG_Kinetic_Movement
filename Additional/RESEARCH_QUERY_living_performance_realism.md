---
id: cpcs.research.query.living_performance_realism
kind: deep_research_prompt
epistemic_status: AUTHORED
primary_route: cpcs/research/gaps/
enhances: cpcs.reference.living_performance_realism
---

# Deep Research Prompt — Living Performance & Capture Realism gap closure

## Mission

Turn the **Living Performance & Capture Realism** spec (`LIVING_PERFORMANCE_REALISM.md`, layers
L1–L7 + capture + voice) from **qualitative direction into measured, source-cited control**. The
goal is that a director/coding agent can, at generation time, place *time-indexed, quantified*
realism behavior for **any gender and any living thing** and know which encoding actually conditions
each provider.

Do **not** redesign CPCS. This is knowledge that must integrate behind the existing semantic
authority as promotable concepts + mappings (concept → control, with format projections), so each
result should be shaped for the `distill → curate → promote` path into `lab/concepts.jsonl` and
`lab/second_brain/curated/mappings.jsonl`.

For every gap, connect the runtime chain and **label each step** as `deterministic`,
`constraint_solved`, `model_mediated`, `human_authored`, `observed`, `measured`, or `experimental`:

```
subject/scene condition
→ evidence or authored intent
→ Director decision (which lever, what value, at what time)
→ Canonical Score field (timeline event)
→ solver/validator (physics/continuity/anatomy check)
→ provider capability decision (can this model express it?)
→ emitted control (the prose/param the model reads)
→ observed measurement (how you verify it in the render)
→ accept / repair / degrade / fail-closed
```

Name the exact **runtime owner** and the **smallest executable consumer** for every new field.

## Coverage table (reproduce and complete)

Answer each gap and end it as `closed | implementable_now | requires_experiment | unknown | deferred | rejected` with a one-line reason.

| Gap | Layer | Question type | Scope |
|---|---|---|---|
| LPR-001 | L1 aliveness/autonomic | WHAT/HOW | breath cadence, blink rate, resting micro-sway amplitude & frequency — by species, age, arousal |
| LPR-002 | L2 attention/gaze | WHAT/HOW | saccade durations, eyes→head→torso **lead-times (ms)**, blink–gaze coupling; predator/prey scan patterns |
| LPR-003 | L3 affect display | WHAT/WHEN | FACS AU onset/apex/offset durations; Duchenne markers; cross-species affect signal catalog (ears/tail/gular/pupil); VAD→signal map |
| LPR-004 | L4 motor initiation | WHY/HOW | proximal-to-distal lead-times; anticipation:action:recovery ratios; gait phase; body-wave propagation (fish/reptile) |
| LPR-005 | L5 emphasis dynamics | HOW/APPLY | prosodic stress → Laban effort accent magnitude + lean displacement + timing offset; audio-visual accent sync window |
| LPR-006 | L6 asymmetry/noise | WHAT/WHY | bilateral asymmetry magnitudes; **correlated (1/f) vs white** micro-noise spectra; the "not random jitter" bound |
| LPR-007 | L7 surface realism | WHAT/WHEN | measurable descriptors separating real skin/fur/scale/feather from waxy/plastic; uncanny-valley thresholds |
| LPR-008 | capture | WHAT/HOW | autofocus hunt durations, exposure adaptation time-constants, handheld shake spectra, wide-lens distortion by focal length — the "real device" signature |
| LPR-009 | voice/vocalization | HOW/APPLY | speech pace ranges, pre-line breath timing, filler/pause rates, audio-visual lip-sync tolerance; animal vocalization–motion sync |
| LPR-010 | gender invariance | WHY/BLEND | which realism levers are gender-invariant; where perceptual/annotation bias enters; how to keep direction neutral without losing realism |
| LPR-011 | cross-species map | BLEND | validate the function→signal mapping per species class; where a human lever has no valid animal analog (and what replaces it) |
| LPR-012 | provider conditioning | APPLY | which **prose encoding** of each measured lever actually moves which model (Veo/Sora/Kling/Runway); minimal-token phrasing that survives |

## Required output shape (per lever, directly promotable)

For each measured lever, return a record that maps cleanly onto the CPCS concept + mapping schema so
it can be promoted without reshaping:

- **concept**: `id (c_*)`, `kind` (use registered kinds: `technique`/`doctrine`/`structure`),
  `layer` (registered), `name`, `what` (the measured principle), `use_when`, `nl_triggers` (≥3),
  `query_term_gate.any`, `source[]` (exact citations), `status`.
- **mapping**: `concept_id` → `target_type: control`, `target_id` in a registered
  `control_namespace` (e.g. `motion.*`, `performance.*`, `camera.*`), with a
  `representation_strategy.projections[]` **per format** (`natural_language`, `yaml`, `json`, `xml`)
  giving the exact prose/param the model reads.
- **conditioning_effect** (one or more): `claim`, `effect_type`, `direction`
  (positive/negative/neutral/mixed/unknown), `epistemic_class`
  (measured/detected/inferred/interpreted/authored/simulated/derived), `evidence_status`
  (unverified/supported/contradicted/qualified/deprecated), `confidence` [0–1],
  `confidence_basis`, `scope { provider, model_version, task_class, duration_seconds,
  prompt_budget_chars }`, `evidence_refs[]`, `limitations[]`.

## Source demands

- Draw from: **FACS** (Ekman/Friesen action units + timing), **Laban/Bartenieff** effort & shape,
  **ethology / animal behavior** (species affect and locomotion signals), **biomechanics** (motor
  sequencing, gait, wave propagation), **oculomotor & psychophysics** (saccade/blink/gaze, uncanny
  valley thresholds), **cinematography & camera forensics** (AF/AE behavior, handheld shake spectra,
  lens distortion), **speech science / prosody** (stress, breath, disfluency, AV sync).
- Prefer **numeric ranges with citations** over prose. Where a value is population-dependent, give
  the range + the moderator (species, age, arousal, culture) — do **not** collapse to one number.
- **Every gender claim must be justified or marked invariant** — do not encode gendered performance
  defaults; if a lever differs by perceived gender, cite the source and mark it as perceptual bias
  to be neutralized, not a directing rule.
- Flag `requires_experiment` where the effect on a *generative model* (not on humans/animals) is
  unproven — those become CPCS ablation candidates, not asserted facts.

## Anti-scope (do not do)

- Do not invent packaging, identities, or claims. Do not produce gendered or species stereotypes.
- Do not return definitions without a runtime decision path. Do not collapse the four format
  projections into one. Do not assert model-conditioning effects without either a citation or a
  `requires_experiment` flag.

## Deliverable

1. Completed coverage table (every gap terminated with a status + reason).
2. Per-lever promotable records (concept + mapping + conditioning_effect) as above.
3. A short **measurement→control→verification** appendix: for each lever, how to *check it in a
   render* (the observed-measurement step), so verification is possible, not just direction.
