# Prompt — Intent Planner

Translate a creative brief into 2–5 candidate motion realizations. Return strict JSON. Do not infer real-world emotion, culture, disability, or deception from appearance.

Required fields:

- primary and secondary intents with confidence;
- beneficiaries/targets/objects;
- culture/context/relationship conditions explicitly supplied;
- scale: face, gaze/head, gesture, upper body, full body, group;
- candidate predicate chains;
- BESS/body/connectivity priors with provenance `CPCS_CONVENTION`;
- affect trajectory seed;
- exclusions, safety, consent, identity, and continuity constraints;
- ambiguity that must be preserved;
- evidence IDs for any source-backed mapping.

Do not select a single realization when the brief is underdetermined. Return alternatives and explain the discriminating context.
