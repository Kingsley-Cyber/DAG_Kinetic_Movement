# Localized Repair Playbook

## Preconditions

Localized repair is permitted only after the exact original build, provider request, result, artifact, evaluator evidence, and first-divergence interval are hash-bound. The repair planner may reassert existing canonical controls; it may not invent new directing knowledge or mutate the accepted canonical target.

## Procedure

1. **Freeze accepted evidence.** Record the original artifact hash, accepted intervals, failed interval, hard-lock verdicts, and human review.
2. **Find first divergence.** Diagnose the earliest frame where actor/object identity, count, state, event order, spatial relation, contact, material response, camera, anatomy, or audio departs from target.
3. **Challenge evaluator.** If the failure involves fast motion, occlusion, stylization, reflections, screen-overlap contact, or camera ambiguity, require a second lane and human review.
4. **Classify the cause.** Missing canonical state; compiler loss; provider realization; asset/control error; edit seam; or evaluator failure.
5. **Choose a repair carrier.** Wording, canonical contract, reference/keyframe, mask/pose/depth/trajectory/control video, shot split, V2V edit, deterministic compositing, audio replacement, or provider substitution.
6. **Define the preservation envelope.** List every field and interval outside the target change that must remain unchanged.
7. **Create boundary frames.** Prefer accepted in/out frames around the failed interval; include pose, velocity, state, camera, and material continuity.
8. **Execute one isolated change.** Do not bundle prompt rewrite, provider change, new reference, and shot split in one causal experiment.
9. **Verify the repair and collateral state.** Re-run every critical assertion across the entire artifact, not only the repaired interval.
10. **Record outcome immutably.** Retain failed and successful attempts, cost, latency, request/settings, seeds/retries, evaluator disagreement, and human verdict.

## Failure-specific routes

| Failure class | First repair | Escalation | Required recheck |
| --- | --- | --- | --- |
| Occlusion/hidden state | L2 visibility/state contract | L4 tracked control or L5 split | identity, count, path, reappearance, world state |
| Identity/role | L2 persistent IDs and event binding | L3 references or L4 per-actor controls | face/costume/body/role/screen lane/voice |
| Object state/possession | L2 ledger transition | L4 object track or V2V | count, holder, contact, dimensions, material state |
| Spatial/geography | L2 coordinate frame and transition | L3 storyboard or L4 trajectory/depth | screen direction, depth, target region, camera transform |
| Order/causality | L2 event graph | L5 event-per-shot decomposition | onset, apex, only-after, consequence, recovery |
| Contact/physics | L2 interaction/support contract | L4 source/control motion or L6 deterministic finishing | distance, penetration, support, reaction latency |
| Fluid/VFX | L2 effect origin/lifetime | L6 separate plate/composite | impact origin, topology, persistence, identity/count |
| Camera entanglement | separate camera and actor tracks | L4 camera/source control | world trajectory, zoom vs translation, direction |
| Anime deformation | L2 deformation/recovery interval | L3 recovery keyframe or L6 authored effect | silhouette, limb count, recovery frame |
| Audio sync | L2 shared event anchor | L6 replace/mix audio | onset offset, semantic cause, speaker/voice |

## Rollback

A repair never overwrites the original. Rollback means selecting the previous accepted build/artifact and preserving the failed repair attempt as evidence. If an edit produces collateral hard-lock failures, it is rejected even when the target interval improves.
