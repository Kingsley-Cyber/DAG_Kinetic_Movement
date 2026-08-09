# Validation System

## Layers

### Structural

JSON Schema, YAML/XML parse, required fields, data types, enums, and closed objects.

### Temporal

Start ≤ end; contained intervals; phase order; coverage/overlap rules; events within scene duration; frame quantization; synchronized bindings.

### Kinematic

Units/frames, finite values, bone lengths, joint ranges, derivative spikes, COM/support consistency, and contact drift.

### Interaction

Predicate preconditions/effects; contact onset before reaction; grasp before carry/throw; release before flight; handoff shared-support interval; no illegal penetration.

### Affect/FACS

AU time order; visibility; laterality; channel conflicts explicitly marked; no inner-state/deception assertion from visible codes.

### Camera/editing

action-axis and screen-direction continuity; subject visibility; contact/readability coverage; shot times; camera/subject separation.

### Adapter

fresh capability snapshot; valid combinations; reference file constraints; model status; no unsupported field represented as native.

### Provenance

empirical claims have sources/scope; CPCS conventions have versions/tests; derived weights have immutable inputs; unverified aliases remain quarantined.

## Severity

- `ERROR`: invalid or unsafe; block compile/generation.
- `WARNING`: plausible loss/ambiguity; generation allowed only by policy.
- `INFO`: optimization or review note.
- `WAIVED`: explicit reviewer decision with identity, reason, and expiry.

## Verification checkpoints

Every pipeline stage produces observable outputs: schema validation report; semantic error list; adapter freshness report; request hash; provider response; output hash; evaluation report. “It probably worked” is not a valid state.
