# Prompt — Immutable Experiment Summarizer

Summarize only the supplied experiment record and evaluations. Preserve model/adapter/version, canonical hash, request hash, output hashes, seed, repetitions, evaluator count, and uncertainty.

Produce:

- hypothesis/result;
- statistically or descriptively supported findings;
- failures by CPCS layer;
- contradictions between automatic and human metrics;
- applicability scope;
- proposed derived feature updates;
- evidence needed before promotion to Curated.

Do not delete failed runs, average across incompatible adapter versions, or claim deterministic seed behavior from one repetition.
