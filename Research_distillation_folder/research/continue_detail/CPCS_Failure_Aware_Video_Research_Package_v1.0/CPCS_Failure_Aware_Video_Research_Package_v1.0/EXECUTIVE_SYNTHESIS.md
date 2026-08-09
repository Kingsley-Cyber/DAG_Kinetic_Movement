# Executive Synthesis

**Research date:** 2026-08-05  
**Repository:** `Kingsley-Cyber/ai-video-movement-prompt-system` at `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`  
**Package status:** source/repository research complete; live repeated-seed provider qualification not run.

## BLUF

The dominant control problem in current generative video is not merely visual quality. It is **state underdetermination across time**. A prompt can describe what is visible, but it usually does not carry a persistent, machine-checkable representation of who and what exists, which state changes are legal, how hidden subjects continue moving, which event causes which effect, how camera coordinates relate to world coordinates, and which exact interval must be verified. When visibility drops or multiple constraints compete, the model is free to resolve missing information with a statistically plausible continuation. That is the gap the user observed when a fighter disappears behind a water splash.

The correct CPCS response is therefore a mitigation ladder, not a larger negative prompt:

1. **Represent the missing state** in the canonical score: persistent IDs, state ledger, event graph, spatial frame, visibility interval, causal edges, terminal state, and hard invariants.
2. **Compile only the provider-relevant subset** into one native request representation; do not duplicate identical semantics across XML, YAML, and JSON.
3. **Escalate conditioning** when text cannot carry the missing information: reference frames, identity sheets, masks, point/pose/depth tracks, control video, or source-video editing.
4. **Split the shot** before a long opaque interval, dense interaction, role crossing, or causal chain exceeds the empirically qualified provider/task envelope.
5. **Move deterministic effects to postproduction** when exact topology, timing, count, contact, or audio synchronization matters more than generative spontaneity.
6. **Verify interval-level assertions** and retain failures. Aggregate aesthetic scores cannot overrule one production-critical identity, count, event-order, or contact failure.

## What the research package establishes

- **96 distinct failure records** across 16 families, each with triggers, symptoms, causes, mitigations, verification metrics, CPCS owners, confidence, and unresolved questions.
- **60 evaluator definitions** with explicit lanes, blind spots, human-calibration requirements, and threshold policy.
- **21 provider/interface rows** separating official capability from unmeasured reliability.
- **81 source records** spanning repository authority, official provider documentation/model repositories, peer-reviewed work, benchmarks, control methods, tracking/measurement tools, and recent preprints.
- **Candidate contracts** for occlusion continuity, persistent state, spatial transitions, causal events, and evaluator provenance.
- **Repeated-seed experiment fixtures** for occlusion, serialization, action density, spatial control, causality, repair, identity/state, and evaluator calibration.

## Ten load-bearing findings

1. **Opaque occlusion changes the information problem.** The model no longer observes the subject; unless state and trajectory survive outside the pixels, reappearance is reconstruction rather than continuation. [B012] [B013] [B014] [B027] [B028]
2. **Endpoint images are constraints, not proofs of the path.** First/last-frame modes can anchor endpoints, but current official documentation does not guarantee correct intermediate order, hidden trajectory, contact, or causality. [M001] [M014] [M024]
3. **Compositional binding remains fragile.** Attribute, count, role, action, motion, spatial relation, and interaction bindings all degrade as scenes become denser. [B002] [B041] [B043]
4. **Visual plausibility and physical correctness are separable.** Benchmarks continue to expose failures in mass, momentum, support, collisions, fluids, and causality even when a clip looks coherent at a glance. [B004] [B005] [B025] [B027] [B044] [B045]
5. **Prompt detail has diminishing returns.** When the missing variable is a trajectory, mask, contact geometry, source motion, or deterministic effect, more prose competes for attention without becoming an executable control. [B005] [B035] [B036] [B037] [B038]
6. **Camera and world motion require separate tracks.** Screen-space flow alone cannot reliably identify whether the camera, actor, or background moved; zoom and translation are especially confusable. [B031] [B035] [B037]
7. **Graphic discontinuity is not world-state discontinuity.** Flashes, smears, wipes, speed lines, and full-frame effects need explicit recovery frames and continuity locks or they can become scene-reset opportunities.
8. **Structured serialization is a compiler discipline, not model intelligence.** JSON is CPCS authority because it is deterministic and validated; XML/YAML can be useful authoring envelopes, but no evidence supports universal provider-side superiority. [R005] [M001] [M002] [M007]
9. **Evaluators fail in systematic ways.** Fast temporal events, occlusion, stylization, camera geometry, screen-overlap contact, and sparse localized failures require calibrated multi-lane evidence and human review. [B029] [B030] [B031] [B032] [B033] [B034]
10. **The cheapest reliable intervention is provider/task specific.** CPCS should learn a failure-to-mitigation policy from immutable paired runs; it should never hard-code a universal action-per-second or prompt-length threshold from one provider or showcase.

## Water-splash case: why the model fills the gap

For the two-fighter water sequence, the splash simultaneously creates several high-risk conditions: a complete opaque occlusion, a solid-fluid transition, overlapping cause/effect timing, one actor's hidden dive trajectory, another actor's kick and recovery, actor-count continuity, screen-side continuity, and a full-frame high-frequency effect. A text model can satisfy the surface concept—“kick, splash, fighter submerged”—without preserving the exact latent state. The splash is therefore a **permission boundary** unless CPCS represents:

```text
B remains the same existing actor while invisible
B's hidden dive path continues from entry state to a bounded reappearance region
A's kick misses B and contacts only the water
water displacement starts only at A's impact point
actor count stays exactly two
costumes, roles, screen sides, water topology, and world layout do not change
```

Even that canonical contract does not guarantee prompt-only compliance. When the subject is fully hidden and the result must be exact, CPCS should choose at least one of: a visible bridge, tracked control media, first/last/reference frames plus path control, a shot split, clean-plate compositing, or source-video modification.

## Decision boundary

Prompt-only generation should be abandoned when any of the following is both **hard** and **not directly observable throughout the generated interval**:

- exact identity/count through complete occlusion;
- exact hidden trajectory or reappearance region;
- precise hand-object or body-body contact;
- collision-free geometry or support mechanics;
- causal material response from a specific impact point;
- multi-actor crossings with persistent role assignment;
- deterministic graphic/anatomy recovery after a full-frame effect;
- frame-accurate audio-event synchronization;
- exact product geometry, logos, dimensions, or state transitions.

The escalation target is not always the most expensive control. CPCS should select the lowest mitigation level whose repeated-seed distribution clears the pre-registered acceptance threshold without adding a new critical failure.
