---
id: cpcs.mx.transition_compatibility
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §82, §83, §84]
primary_route: cpcs/knowledge/06_body_motion/
secondary_routes:
  - cpcs/knowledge/06_body_motion/kinetic_phrases/
interfaces: [cpcs.mx.action_template, cpcs.body_motion.phase.evidence_vs_engineering]
---

# Transition Compatibility, Blending, and Loop Closure

Every action should specify allowed predecessors, successors, transition cost,
and required bridge. This prevents impossible concatenations.

## Transition compatibility

```yaml
transition:
  from: run
  to: strike
  compatibility:
    status: valid
  bridge:
    required:
      - deceleration
      - support_adjustment
```

Prevents: `airborne spin → instantaneous planted strike` without a transition
state.

## Blending vs semantic transition

A numerical blend can produce a visually smooth interpolation while
semantically destroying the action. Distinguish:

```text
geometric blend ≠ semantic transition
```

A valid transition needs: identity continuity, support continuity, contact
continuity, action phase compatibility, trajectory continuity.

## Loop closure

For repeated actions (walk, run, idle, breathing, gestures, cyclic dance), the
compiler needs:

```text
cycle_start · cycle_end · phase_alignment · state_equivalence · closure_error
```

```yaml
cycle:
  mode: loop
  closure:
    required:
      - root_continuity
      - phase_continuity
      - support_continuity
```

## Verification

`test_transition_compatibility_checked`,
`test_bridge_required_when_incompatible`,
`test_loop_closure_state_equivalence`.
