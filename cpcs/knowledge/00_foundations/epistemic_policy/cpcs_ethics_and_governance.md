---
id: cpcs.found.epistemic_policy.cpcs_ethics_governance
kind: principle
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-009 §27-29]
primary_route: cpcs/knowledge/00_foundations/epistemic_policy/
interfaces:
  - cpcs.found.uncertainty.evidence_two_axis_model
  - cpcs.runtime.structured_prompting_architecture
  - cpcs.evaluation.reference_video_distillation
---

# CPCS Ethics, Rights, and Governance

> Distilled from CPCS paper §27-29. Defines 8 governance areas, 8 acknowledged
> limitations, and 11 research agenda items. CPCS is a proposal, not a
> validated standard.

## 8 governance areas

### 1. Identity and performance rights

Consent must specify: identity use, voice/facial use, body/motion use,
training/inference/editing/distribution rights, project and duration scope,
derivative/transferable rights, revocation/retention policy, compensation
and credit. Motion and expressive style are distinctive even when the face
is changed — motion capture is not ownerless technical data.

### 2. Deepfake and deception risk

Systems should support: consent verification, visible/machine-readable
provenance, content credentials where available, audit logs, restricted
identity models, disclosure policies, detection and incident response.
Technical provenance improves accountability but does not eliminate social harm.

### 3. Emotional inference and pseudoscience

FACS and VAD should NOT claim knowledge of real people's internal emotions,
honesty, intent, or mental health. CPCS uses these systems to author
**intended portrayals** and measure **visible features**. It rejects the
inference that one facial or body pattern proves a private state.

### 4. Cultural and individual variation

Gesture, gaze, interpersonal distance, emotional display, and movement quality
vary across cultures, communities, contexts, and individuals. A retrieval
system trained on narrow film conventions can reproduce stereotypes.
Templates should record population and context; prefer performer-specific
direction over demographic assumptions.

### 5. Disability and non-normative movement

Metrics such as symmetry, gait regularity, or "physical normality" can
penalize authentic disabled movement. Evaluate against the intended performer
profile and action, not a single normative body model. Requires: configurable
body topology and assistive devices, mobility-aid contacts, performer-specific
ranges, nonpathologizing language, evaluation distinguishing artifact from
intentional movement.

### 6. Stunt and violence governance

Fight generation is for fictional choreography, previsualization, safe
performance design. Templates distinguish cinematic illusion from real impact
and should NOT be presented as instructions for harming people. Human stunt
professionals remain essential for real production safety.

### 7. Labor and creative attribution

A directorial model may retrieve or emulate patterns from actors, animators,
choreographers, cinematographers. Production systems should retain source and
contributor attribution, honor labor agreements, avoid representing generated
performance as a substitute for consented creative work without terms.

### 8. Dataset and RAG governance

The knowledge store must support: provenance and source hashes, consent and
license scopes, access control, deletion and revocation, versioning and audit
trails, separation of public research from private production assets, bias
and coverage reports, restrictions on biometric export.

## 8 acknowledged limitations

| Limitation | Core issue |
| --- | --- |
| Representation burden | Detailed scores can be expensive to author; depends on good defaults and retrieval |
| Estimator error | AU, gaze, pose, camera, contact, affect estimators are imperfect; verification must include uncertainty |
| Laban operationalization | No small kinematic set fully captures Laban practice; requires trained analyst collaboration |
| Physics–cinema mismatch | Cinematic motion intentionally violates strict physics; plausibility serves the shot |
| Model capacity | A score can specify controls a generator cannot follow; compiler must report unsupported features |
| Long-horizon consistency | Identity, props, affect, performance continuity across shots remains difficult |
| Ambiguity | Directorial language benefits from interpretive openness; overformalization narrows discovery |
| Evaluation validity | Automatic metrics may not reflect dramatic effectiveness; expert/audience studies necessary |

## Research agenda (11 items)

1. **Open performance-score standard** — extensible tracks, typed constraints,
   provenance, rig/model conversion (CPCS schema as proposed starting point)
2. **Learned compiler** — compare direct LLM generation, RAG, symbolic
   planning, multimodal planning, interactive correction
3. **Joint face–body–voice modeling** — synchronized multi-modal behavior with
   independent controls; masking and leakage as test
4. **Body-part local phase as editable interface** — "hips lead shoulders by
   four frames" → phase constraints
5. **Differentiable cinematography** — optimize visibility, composition,
   emphasis, continuity under director constraints
6. **Physics-aware video diffusion** — integrate 3D bodies, geometry, contacts,
   dynamics directly; hybrid world models
7. **Retrieval of performance, not stereotype** — compositional, context-aware
   retrieval; template diversity and bias evaluation
8. **Causal evaluation** — vary only Laban Weight → should alter perceived
   weight without changing action identity or camera
9. **Director-in-the-loop learning** — edits as preference data with consent;
   learn individual grammars
10. **Cross-shot performance continuity** — track unresolved affect, fatigue,
    injury, prop state, costume, gaze across cuts
11. **Benchmarks for reference-video distillation** — verified shot boundaries,
    actor tracks, AUs, pose, contacts, camera, dialogue; distinguish
    observation accuracy from interpretive agreement
