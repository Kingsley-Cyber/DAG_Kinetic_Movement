# CPCS Canonical Layer Stack

The stack separates **why**, **what**, **how**, **where**, **when**, **with whom/what**, **how it is photographed**, **how it is stylized**, and **what a particular model can actually accept**. This separation prevents common prompt failures such as treating “powerful” as a force value, using a camera move to hide a contact failure, or allowing style to change the action predicate.

| Order | Layer | Primary question | Output |
|---:|---|---|---|
| 1 | Creative intent | Why is the action performed? | intent distribution, goals, exclusions |
| 2 | Narrative beats | What changes and in what order? | beats, state transitions, causality |
| 3 | Affect trajectory | How does affect evolve? | VAD+CCE tracks, channel timing |
| 4 | Actor and identity | Who/what performs? | actor, skeleton, assets, capabilities |
| 5 | Body organization | Which parts initiate/connect? | connectivity, sequencing, support |
| 6 | Laban BESS | What qualitative dynamics/form/space? | Body/Effort/Shape/Space |
| 7 | Motion primitives | What reusable units compose the action? | primitive graph |
| 8 | Phase grammar | How is each action phased? | phase state machine/events |
| 9 | Kinematics | What measurable trajectory/derivatives? | pose, velocity, acceleration, contact |
| 10 | Interaction topology | Who acts on whom/what? | predicates, contact graph, object state |
| 11 | Force dynamics | What physical/perceived force? | dynamics, kinetic chain, cues |
| 12 | Rhythm | How are events patterned in time? | clocks, cadence, accents, microtiming |
| 13 | Camera | How is action observed? | shots, trajectories, continuity |
| 14 | Style transform | How is choreography stylized? | transforms plus locked invariants |
| 15 | Model adapter | What can the target model accept? | request, prompt, references, loss report |
| 16 | Evaluation | Did output satisfy constraints? | immutable scores/annotations |

## Precedence

Safety and explicit interaction constraints override style. Contact topology overrides decorative trajectories. Measured data override estimates, while estimates override prompt priors without deleting provenance. Native/reference model controls outrank prose. Derived weights can tune compilation but cannot rewrite curated definitions.
