---
id: cpcs.experiment.carrier_effect_design
kind: experiment_design
epistemic_status: PROJECT_DERIVED
acquisition: authored
status: designed, not executed
sources: [SRC-001 §16, SRC-001-U15, SRC-001-U16]
primary_route: cpcs/research/sources/experiments/
---

# Carrier-Effect Experiment Design

## Question

Does structured carrier choice (JSON/YAML/XML/NL/hybrids) materially change
motion adherence when semantic content is held constant? No universal
superiority claim is evidence-supported; structured-output research (U15,
U16) shows schema compliance and semantic correctness are separate
dimensions and that format effects vary across tasks.

## Dataset (minimum)

- 100 motion intents
- 50 interaction intents
- 50 camera intents
- 25 style intents
- 25 mixed scenes

## Renderings per intent

1. JSON
2. YAML
3. XML
4. Markdown table
5. plain NL
6. hybrid JSON + NL
7. hybrid YAML + NL

## Held constant

model · seed (where supported) · token budget · temperature · retrieved
evidence · semantic meaning · provider · number of generation attempts

## Metrics

schema validity · field preservation · action adherence · temporal-order
preservation · actor identity consistency · left/right preservation · camera
adherence · interaction/contact adherence · contradiction rate · omission
rate · token count · latency · retry count

## Output

A **CPCS empirical carrier profile** — never a universal claim.

## CPCS representation policy (SRC-006 §9.2)

- YAML: authored intent, inheritance, profiles, comments, human editing.
- JSON: resolved canonical meaning, validation, hashing, diffing, API contracts.
- XML: only for ordered/namespaced/mixed-content envelopes or provider
  interfaces that demonstrate a benefit.
- Natural language: reasoning scratch output where allowed and provider-facing
  compilation.
- Hybrid: concise natural-language task plus machine-readable canonical
  references/constraints; test rather than assume.

Do not force private reasoning traces into canonical schemas. Require
structured decisions, evidence, uncertainty, and verification records — the
products of reasoning — not hidden token-level rationales.

## Controlled carrier experiment (SRC-006 §9.3)

### Independent variables

1. Carrier: `NL`, `YAML`, `JSON`, `XML`, `hybrid`.
2. Reasoning mode: `direct`, `aot_prompting`, `selective_tree_search`,
   `typed_graph_aggregation`, `failure_directed_repair`.
3. Task block: simple, temporal, causal, multi-actor, cross-view conflict,
   provider-loss, repair.
4. Model/provider family, analyzed separately.

### Controls (10)

one frozen canonical semantic task per fixture · mechanically generated
carrier projections from the same task · identical field order where the
carrier permits · identical instructions and examples except syntax-required
changes · fixed decoding settings and seeds when supported · same context
evidence · same output schema and verifier versions · same compute budget
per comparison · no format-specific extra semantic hints · randomized
presentation order · separate planning-only tests from video-render tests.

### Outcomes (13)

```text
schema validity · semantic field preservation · hard-constraint pass rate
left/right preservation · temporal-order preservation · causal-edge preservation
omission rate · contradiction rate · malformed syntax rate
input/output tokens · latency · model calls · provider adherence after render
```

### Analysis

Report cell-level results, confidence intervals, effect sizes, and carrier ×
reasoning-mode × model interactions. Do not pool models into a universal
winner. Use a predeclared missing/failure policy. A carrier becomes a
provider/profile default only after held-out replication.

## Boundary doctrine (SRC-007 G019)

Use the same canonical `meaning_id` for every generated format variant.
State which boundary is under test before comparing:

```text
authoring · internal interchange · model reasoning context
· provider request · audit log
```

Do not generalize a result across boundaries. Produce a provider-specific
selection rule and fallback rule driven by versioned capability evidence and
experiment results, not by preference.

`test_same_meaning_id_across_variants`,
`test_boundary_under_test_declared`,
`test_no_cross_boundary_generalization`,
`test_selection_rule_driven_by_capability_evidence`.

## Disposition

P2 per `00_governance/policies/distillation_implementation_priority.md`.
