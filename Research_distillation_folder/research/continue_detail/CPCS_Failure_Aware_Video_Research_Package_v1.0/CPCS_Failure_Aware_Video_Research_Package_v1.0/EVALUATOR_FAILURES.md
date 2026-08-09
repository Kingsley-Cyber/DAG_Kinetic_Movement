# Evaluator Failures

## Principle

A generated artifact is not correct because one VLM, tracker, pose estimator, shot detector, or aggregate metric says it is. Evaluation is itself a perception and reasoning problem. CPCS must preserve direct, semantic, measured, and human-review lanes without averaging away disagreement.

## Six primary evaluator failures

### P.91 — VLM misses or reorders fast action

**Failure ID:** `failure://p/vlm_misses_fast_action/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B007], [B008], [B017], [B025], [B029], [B030], [B031], [B033], [B034]

**Trigger.** Contact, flashes, smears, or events occupy very few frames.

**Observable symptom.** The evaluator omits the event or reports the wrong order.

**Likely cause.** Sparse frame sampling and static visual shortcuts fail to capture temporal logic. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Use high-rate interval extraction, atomic questions, detector evidence, and human review for fast decisive events.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_evaluator_calibration` is the primary metric; companion checks: `metric_false_negative_rate`, `metric_false_positive_rate`, `metric_human_agreement`.

**Compiler/score impact.** `verification_requirements`, `provenance`, `warnings`, `unresolved`.

**Prompt risks.** accepts one VLM verdict as ground truth; averages conflicting semantic and measured evidence; uses a detector outside its calibrated domain without uncertainty.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### P.92 — VLM invents contact from screen overlap

**Failure ID:** `failure://p/vlm_invents_contact/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B007], [B008], [B017], [B025], [B029], [B030], [B031], [B033], [B034]

**Trigger.** Perspective or blur makes actors overlap without physical contact.

**Observable symptom.** Evaluator marks a hit/grasp that did not occur.

**Likely cause.** Semantic priors and 2D overlap substitute for geometric evidence. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L4 (pose, mask, depth, trajectory, or control video).** Require pose/depth/distance evidence and human calibration; do not let semantic verdict alone decide contact.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_evaluator_calibration` is the primary metric; companion checks: `metric_false_negative_rate`, `metric_false_positive_rate`, `metric_human_agreement`.

**Compiler/score impact.** `verification_requirements`, `provenance`, `warnings`, `unresolved`.

**Prompt risks.** accepts one VLM verdict as ground truth; averages conflicting semantic and measured evidence; uses a detector outside its calibrated domain without uncertainty.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### P.93 — Tracker or segmenter swaps actor identity

**Failure ID:** `failure://p/tracker_identity_swap/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B007], [B008], [B013], [B017], [B018], [B019], [B020], [B025], [B029], [B030], [B031], [B033], [B034]

**Trigger.** Actors overlap, cross, wear similar clothing, or become occluded.

**Observable symptom.** Continuity metric reports a false teleport, duplicate, or role swap.

**Likely cause.** Perception tracker loses identity under ambiguity. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Calibrate on the exact domain, combine appearance/trajectory/role cues, expose uncertainty, and require human review on swaps.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_evaluator_calibration` is the primary metric; companion checks: `metric_false_negative_rate`, `metric_false_positive_rate`, `metric_human_agreement`.

**Compiler/score impact.** `verification_requirements`, `provenance`, `warnings`, `unresolved`.

**Prompt risks.** accepts one VLM verdict as ground truth; averages conflicting semantic and measured evidence; uses a detector outside its calibrated domain without uncertainty.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### P.94 — Shot detector mistakes flash or smear for cut

**Failure ID:** `failure://p/shot_detector_flash_false_positive/1`  
**Empirical confidence:** moderate  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B007], [B008], [B017], [B025], [B029], [B030], [B031], [B033], [B034]

**Trigger.** Full-frame graphic effects produce abrupt histogram changes.

**Observable symptom.** Evaluator reports a cut and state discontinuity that were not authored.

**Likely cause.** Low-level shot detection treats graphic discontinuity as edit discontinuity. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Classify cut, flash, hold, blur, and occlusion separately and calibrate with authored effect fixtures.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_cut_flash_classification` is the primary metric; companion checks: `metric_evaluator_calibration`, `metric_false_negative_rate`, `metric_false_positive_rate`, `metric_human_agreement`.

**Compiler/score impact.** `verification_requirements`, `provenance`, `warnings`, `unresolved`.

**Prompt risks.** accepts one VLM verdict as ground truth; averages conflicting semantic and measured evidence; uses a detector outside its calibrated domain without uncertainty.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### P.95 — Pose/anatomy metric fails on anime or stylization

**Failure ID:** `failure://p/pose_metric_stylization_failure/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B007], [B008], [B017], [B025], [B029], [B030], [B031], [B032], [B033], [B034]

**Trigger.** Bodies use smears, holds, foreshortening, nonhuman proportions, or partial visibility.

**Observable symptom.** Evaluator flags intentional style or misses real anatomy breakage.

**Likely cause.** Pose models are out of distribution and confidence is not propagated. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Use style-specific calibration, silhouette and temporal recovery metrics, plus human review; never treat one pose model as truth.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_evaluator_calibration` is the primary metric; companion checks: `metric_false_negative_rate`, `metric_false_positive_rate`, `metric_human_agreement`.

**Compiler/score impact.** `verification_requirements`, `provenance`, `warnings`, `unresolved`.

**Prompt risks.** accepts one VLM verdict as ground truth; averages conflicting semantic and measured evidence; uses a detector outside its calibrated domain without uncertainty.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

### P.96 — Aggregate score hides a decisive localized failure

**Failure ID:** `failure://p/aggregate_metric_hides_local_failure/1`  
**Empirical confidence:** high  
**CPCS render evidence:** `not_run_no_authorized_provider_credentials_or_budget_in_session`  
**Sources:** [B001], [B007], [B008], [B009], [B017], [B025], [B029], [B030], [B031], [B033], [B034]

**Trigger.** Most frames look good but one contact, identity, count, or causal event is wrong.

**Observable symptom.** High average quality score passes an unusable render.

**Likely cause.** Global metrics dilute sparse but production-critical failures. This is recorded as `cross_provider_mechanistic_inference` rather than as a verified closed-model internal mechanism.

**Primary intervention — L2 (canonical event/state contract).** Evaluate canonical assertions per interval and hard-lock dimension; block on any critical assertion regardless of aggregate score.

**Fallback — L6 (postproduction/compositing).** Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing.

**Verification.** `metric_evaluator_calibration` is the primary metric; companion checks: `metric_false_negative_rate`, `metric_false_positive_rate`, `metric_human_agreement`.

**Compiler/score impact.** `verification_requirements`, `provenance`, `warnings`, `unresolved`.

**Prompt risks.** accepts one VLM verdict as ground truth; averages conflicting semantic and measured evidence; uses a detector outside its calibrated domain without uncertainty.

**Falsification checkpoint.** Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.

## Calibration policy

An evaluator can block or promote a provider/model/version only after:

- exact evaluator/version/configuration are pinned;
- the artifact hash and analyzed interval are bound;
- in-domain positive and negative fixtures are labeled by humans;
- false-positive and false-negative rates are reported by failure family;
- hard cases include fast events, full occlusion, reflections, actor crossings, camera zoom/translation, anime smears, and partial visibility;
- confidence and unobservable states are preserved;
- conflicts invoke human review instead of confidence averaging.

## Recommended lanes

| Dimension | Primary lane | Secondary lane | Known hazard |
| --- | --- | --- | --- |
| actor/object count | tracking + segmentation | human | reflection, occlusion, fusion, small objects |
| identity/role | appearance + trajectory + event assignment | human | similar actors, cuts, effects |
| event order/causality | atomic temporal semantic questions | frame/timecode human review | sparse frame sampling and plausible priors |
| contact/penetration | pose/depth/distance measurement | human | 2D overlap is not 3D contact |
| support/foot slip | pose + optical flow + contact state | human | camera motion, stylization, occlusion |
| camera motion | geometric estimator | semantic estimator + human | zoom versus translation, weak parallax |
| flash/cut/smear | effect-aware shot classifier | human | full-frame histogram discontinuity |
| material response | effect origin/segmentation + temporal questions | human | fluid topology and transparency |
| audio sync | event onset/cross-modal model | human | semantic match can hide temporal offset |
| human readability | human rubric | multi-evaluator support | rater disagreement and cultural/style preference |

## Aggregation rule

Critical assertions are conjunctive: one failure blocks the artifact even when the aggregate score is high. Advisory dimensions may be summarized, but the report must retain per-assertion raw values, failed intervals, evaluator provenance, conflicts, and human overrides.
