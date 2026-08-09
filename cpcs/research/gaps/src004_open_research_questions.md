---
id: cpcs.gaps.src004_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-004 §27]
primary_route: cpcs/research/gaps/
---

# SRC-004 Open Research Questions

SRC-004 §27 identifies ten research questions that remain genuinely empirical.
None should be filled with invented constants. Each should have a controlled
experiment and measurable outcome before becoming a hard CPCS rule.

1. What numeric thresholds for impact/uncertainty/coupling are useful on actual
   CPCS tasks?
2. How much state contraction can occur before decision quality degrades?
3. Does DecisionRecord output improve downstream compile success enough to
   justify its token cost?
4. Which target providers preserve which controls natively?
5. Which variant-distance metric correlates with human-perceived creative
   diversity?
6. When does self-consistency outperform a deterministic validator?
7. Which carrier produces the best semantic preservation under equal token
   budgets?
8. Which failures can be reliably attributed to planning versus compilation
   versus provider realization?
9. What evidence threshold should promote a reasoning pattern into durable
   knowledge?
10. How should human overrides interact with soft scores while preserving
    reproducibility?

## Governance note

- These questions are operationalized by the ADRG controlled experiments
  (E-ADRG-001 through E-ADRG-006) in `cpcs/research/sources/experiments/
  adrg_experiments.md`.
- Q1/Q2 relate to decision-aware routing (`cpcs.adrg.decision_aware_routing`)
  and state contraction (`cpcs.adrg.state_contraction`).
- Q3 relates to DecisionRecord cost/benefit (E-ADRG-001).
- Q7 relates to carrier effect (E-ADRG-006, also SRC-001 carrier-effect
  experiment).
- Q9 relates to promotion rules (`cpcs.gov.promotion_rules`).
- All routing thresholds remain `EXPERIMENTAL` / proposed operational variables
  until calibrated.
