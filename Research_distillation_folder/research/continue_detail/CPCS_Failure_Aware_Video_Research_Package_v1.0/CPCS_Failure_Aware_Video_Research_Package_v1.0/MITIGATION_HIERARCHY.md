# Mitigation Hierarchy

## Governing rule

Use the **lowest-cost intervention that carries the missing information in a form the selected provider can actually receive and that clears a pre-registered verification threshold across repeated seeds**. Do not default to “add more detail.” More detail can worsen attention competition, conflict, and temporal overload.

## L0 — wording repair

**Use when:** The canonical target is complete and the failure is caused by an ambiguous or provider-hostile phrase.

**Exit checkpoint:** Paired wording arm improves the same critical assertion without changing the canonical target.

## L1 — structured prompt repair

**Use when:** The provider receives a prompt string, but deterministic compiler structure is needed to prioritize identities, events, hard locks, and end state.

**Exit checkpoint:** The adapter retains every hard lock and produces no semantic conflict or overflow loss.

## L2 — canonical event/state contract

**Use when:** The missing information is a persistent state, event dependency, spatial frame, causal edge, visibility interval, support/contact state, or terminal invariant.

**Exit checkpoint:** The score validates and every required state/event/spatial/causal obligation has an explicit verification assertion.

## L3 — reference image or storyboard

**Use when:** Appearance, identity, layout, start/end pose, product geometry, or reappearance state needs a visual anchor.

**Exit checkpoint:** Reference identity, role, rights, and binding are verified; conflicts with text are resolved before submission.

## L4 — pose, mask, depth, trajectory, or control video

**Use when:** The missing information is time-varying and cannot be represented reliably by text: mask, pose, point, depth, trajectory, camera, audio, or source-motion control.

**Exit checkpoint:** Control assets are hash-bound, aligned to the exact timebase/coordinate frame, and validated before generation.

## L5 — shot decomposition

**Use when:** One clip contains too many dependencies, actors, crossings, camera moves, effects, or opaque intervals for the qualified provider/task envelope.

**Exit checkpoint:** Each shot has a complete handoff state, no hidden dependency across the edit, and a deterministic assembly plan.

## L6 — postproduction/compositing

**Use when:** The required behavior is deterministic finishing: splash, flash, smoke, shake, sound, logo, count, geometry, topology, or exact effect timing.

**Exit checkpoint:** The generated plate preserves required clean geometry/identity and the composite passes all continuity assertions.

## L7 — regenerate only the failing interval

**Use when:** Most of the artifact is accepted and the first divergence can be bounded with stable in/out frames and preservation checks.

**Exit checkpoint:** The repaired interval and both seams pass; all non-target hard locks are rechecked across the entire artifact.

## L8 — provider/model substitution

**Use when:** The selected provider lacks a documented carrier or repeatedly fails despite a complete target and appropriate controls.

**Exit checkpoint:** The substitute provider profile is officially verified and the same sealed experiment is rerun without changing acceptance criteria.

## L9 — unsupported or not reliably controllable

**Use when:** No available workflow can satisfy the hard requirement with an acceptable success distribution or verification confidence.

**Exit checkpoint:** The system returns an explicit unsupported result and does not fabricate a controllability claim.

## Escalation algorithm

```text
validate canonical target
→ identify first divergence
→ challenge evaluator
→ determine missing carrier
→ choose lowest compatible level
→ compile with explicit loss report
→ generate paired candidates
→ verify interval and all hard locks
→ retain failed evidence
→ escalate only if pre-registered threshold is not met
```

## Cost and risk accounting

Every mitigation record in `FAILURE_RECORDS.jsonl` includes expected benefit, prompt/character cost, generation cost, risk of a new failure, provider dependency, evidence strength, verification, and rollback. CPCS should learn provider/model/version-conditioned mitigation ordering from immutable isolated comparisons; learned weights may rank admissible choices but cannot override hard constraints or authored policy.
