# Acceptance Criteria

## Package/repository

- 100% JSON/YAML/XML parse success;
- all source IDs resolve;
- all topic pairs present;
- all examples pass structural schemas;
- no adapter older than policy TTL in an active release;
- no `UNVERIFIED` claim promoted to Curated.

## Compiler

- deterministic output for fixed inputs/version;
- no temporal interval outside scene;
- no invalid phase order without interruption;
- every unsupported/unknown adapter field appears in loss report;
- measured/estimated/prior values distinguishable.

## Generated output pilot gate

For each supported scene family/model pair, predeclare thresholds. Recommended initial gate:

- median human predicate/action score ≥ 3/4;
- median contact causality ≥ 3/4 for contact scenes;
- identity stability ≥ 3/4;
- zero critical safety/rights violations;
- inter-rater weighted κ or ICC reported and targeted ≥ 0.60 before fully automated promotion;
- CPCS condition improves at least one co-primary outcome without a material decline in the other.

Thresholds are project gates, not scientific universals.
