---
id: time.beat_schedule_ugc
pass: time
triggers: ["seconds", "short clip", "UGC", "selfie", "one action", "opens and drinks"]
not_when: ["music-driven or choreographed timing", "combat"]
backs: [cpcs.rhythm.metrics_contract, cpcs.motion.phase.timing_presets]
from: "Additional/LIVING_PERFORMANCE_REALISM.md §4 (convert lists to a schedule), §11 (8 s models: one clip per beat); cpcs/knowledge/10_time_rhythm/rhythm_metrics_contract.md (master clock in seconds; rhythm fields are independent axes); Additional/Granular Motion Control for AI Video Generation.md (motion budget per shot: one dominant action, one camera move, one or two secondary actions)"
origin: PROJECT_DERIVED
importance: 0.6
---
# UGC beat schedule

One dominant action per clip, in explicit order, each beat given room to read. Minimum readable
seconds per beat type are project conventions until renders measure them (origin on each beat).
The master clock is seconds; the model reads order words, not timestamps, so the prompt states
order and pace, and the schedule stays in the IR.

## Wording
```prompt core
Pace: {pace}. One action at a time, each given its own moment; the clip ends on a held settle, not mid-motion.
```

```prompt core short
Pace: {pace}; one action at a time; end on a held settle.
```

## Failure signs
- Actions overlap or the model rushes the sequence to fit.
- The clip ends mid-action or jumps a stage.
- Too many beats for the clip length (OVERLOADED in check).

## Effects
- claim: ordered beats with explicit pace reduce rushed or merged actions · evidence_status: unverified · model: seedance · runs: —
