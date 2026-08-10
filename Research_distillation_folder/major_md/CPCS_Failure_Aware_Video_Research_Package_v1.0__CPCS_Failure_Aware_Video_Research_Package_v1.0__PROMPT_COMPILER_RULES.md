# Prompt Compiler Rules

## Authority rule

The fully resolved `cpcs.universal_score/1.0` JSON remains the only semantic authority. Natural language, Markdown, YAML, XML, JSON prompt text, hybrid envelopes, references, and control media are projections or inputs. No serialization may become a second truth source.

## Deterministic compile sequence

1. **Normalize entities.** Assign stable IDs and distinguish identity, role, screen lane, world position, voice, prop ownership, and material state.
2. **Resolve state.** Materialize initial state, state deltas, visibility intervals, irreversible transitions, and terminal state.
3. **Topologically order events.** Compile dependencies before timestamps: `before`, `only_after`, `causes`, `while`, `prevents`, `terminates`.
4. **Declare coordinate frames.** Never emit unqualified left/right when camera motion or cuts can change screen projection.
5. **Separate actor, camera, effect, edit, and audio tracks.** Do not rely on one prose clause to distinguish these motions.
6. **Classify controls.** Each field is hard, soft, evaluation-only, unsupported, or delegated to a reference/control asset.
7. **Resolve conflicts before provider submission.** Contradictory fields must fail closed or require explicit selection; the provider must not arbitrate canonical conflicts.
8. **Select one provider-native representation.** Do not duplicate the same meaning as XML+JSON+YAML inside a prompt unless a controlled experiment proves a version-scoped benefit.
9. **Compress by information value.** Preserve identities, event order, causal links, hidden transitions, terminal state, and hard locks before style adjectives, redundant negatives, or verifier-only fields.
10. **Emit a loss report.** Every canonical field receives a capability disposition; unsupported or evaluation-only controls remain visible.
11. **Disable or record prompt rewriting.** Provider-side enhancement/rewrite changes the experiment arm and can alter semantics. If it cannot be disabled, capture the setting and returned/expanded prompt where available.
12. **Bind assets and timebases.** References, masks, pose tracks, depth, trajectories, audio, and source video require content hashes, roles, coordinate frames, intervals, and rights basis.
13. **Predeclare verification.** Hard fields without an observable metric are not ready for provider execution.

## Priority order under prompt limits

```text
safety and legal constraints
> identity, actor/object count, and role locks
> initial and terminal state
> ordered primary events and causal edges
> spatial/visibility/contact invariants
> camera and edit state
> audio anchors
> provider-required syntax
> style and secondary detail
> negative constraints not paired with a positive target
> explanatory prose and evaluator-only notes
```

A hard lock may not be silently truncated. If the prompt budget cannot carry the required subset, the compiler must change carrier, split the shot, or return unsupported loss.

## Positive continuation rule

A forbidden outcome is not a complete instruction. Each critical negative must be paired with the positive state that should persist:

```text
weak: no teleport, no duplicate, no costume change
stronger canonical target:
  actor_B.exists=true throughout
  actor_B follows hidden_path_01
  actor_B reappears in region R_B
  actor_count=2
  actor_B.costume remains costume_B_01
```

## Serialization experiments

The format experiment must hold canonical meaning constant across natural language, flat YAML, XML, JSON, XML+JSON, and XML+JSON+YAML. Compare semantic coverage, hard-lock retention, prompt cost, and failure distributions. Do not compare hand-written prompts with unequal information or provider-specific optimization and call the result a format test.

## Provider adapter rules

- Bind the exact provider, endpoint/model ID, API/product interface, date, region, duration, resolution, frame rate, seed semantics, prompt limit, reference roles, audio behavior, and rewrite policy.
- Third-party adapters are separate provider surfaces; do not assume native limits or behavior.
- A documented seed is an experiment key, not proof of deterministic or compliant output.
- First/last-frame modes are endpoint constraints, not hidden-path, contact, or causal guarantees.
- Source-video edit modes must verify preservation outside the requested change.
- Marketing claims never populate empirical reliability fields.

## Attention-budget decision

The compiler should calculate a version-scoped complexity vector rather than one universal score:

```text
primary_event_count
dependency_depth
simultaneous_actor_actions
actor_similarity
screen_crossings
complete_occlusion_seconds
contact_complexity
camera_motion_complexity
effect_density
audio_anchor_count
prompt_characters
reference_count
```

Provider/task-specific experiment results define warning and split thresholds. Before calibration, CPCS may warn on rising complexity but must not claim universal maximum actions per second.
