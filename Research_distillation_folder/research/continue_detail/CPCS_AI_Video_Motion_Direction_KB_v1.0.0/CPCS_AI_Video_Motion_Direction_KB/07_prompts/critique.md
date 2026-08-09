# Prompt — Output Critic

Evaluate a generated output against the canonical scene without rewarding style that breaks action or causality.

Score 0–4 with evidence timestamps for:

- intent readability;
- predicate/action correctness;
- contact topology and reaction order;
- identity/appearance stability;
- body/BESS realization;
- phase timing/rhythm;
- FACS/gaze/head behavior;
- camera/continuity/contact visibility;
- style success and invariant preservation;
- physics/foot skate/joint plausibility;
- audio/dialogue synchronization;
- overall production usefulness.

Return `not_observable` where the shot cannot show a criterion. Distinguish canonical failure, adapter loss, model failure, and evaluator uncertainty.
