---
id: cpcs.synthesis.director_decision_procedure
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-002 L2.§42, SRC-004 §5, §42]
primary_route: cpcs/runtime/04_synthesis/
secondary_routes:
  - cpcs/runtime/05_strategy/
interfaces: []
---

# Director Decision Procedure

The reasoning layer follows a bounded 12-step procedure.

1. **Characterize intent** — what/how-feel/what-not/who acts/who reacts/where/when/shot scale/style. Do not infer private mental state as fact.
2. **Identify observable targets** — attention · facial display · posture · weight transfer · movement timing · trajectory · shape · connectivity · breath · interaction.
3. **Retrieve candidate framework controls** — FACS/Laban/Bartenieff with application rules.
4. **Filter by applicability** — reject contraindicated / unobservable / redundant / conflicting / insufficient-evidence concepts.
5. **Scope controls** — attach actor · body region · action · phase · shot · interaction.
6. **Compose** — resolve reinforcement · conflict · sequence · causal dependency · priority.
7. **Generate realizations** — translate semantic controls into observable realization candidates.
8. **Negotiate provider capability** — native / semantic / behavioral / reference / unsupported.
9. **Apply attention budget** — keep the minimal sufficient set of provider instructions.
10. **Compile** — produce provider-specific projection and loss record.
11. **Verify** — compare rendered video against the original canonical target.
12. **Localize failure** — never rewrite the entire intent because one control failed; classify failure (identity/action/spatial/temporal/performance_quality/facial/connectivity/camera/continuity/provider_translation) and correct the smallest responsible layer.

See worked examples in SRC-002 L2.§43–§45 (restrained dialogue, explosive action, stylized/anime).

## ADRG DecisionRecord provenance (SRC-004 §5, §42)

Each step should produce an auditable DecisionRecord with: question, candidate
IDs, criteria, constraint_refs, evidence_refs, scores, selected, rejected
(with reason_codes), assumptions, confidence, unresolved, consequences, loss.

`confidence` is confidence in the decision under the declared evidence and
rubric — not the probability that the director is objectively correct. `selected`
does not mean rendered success.

## Abstention outcomes

When no candidate satisfies the invariants, the decision procedure may:

```text
select  — choose the best admissible candidate
degrade — relax a soft preference and re-evaluate
decompose — split the decision into sub-decisions
fallback — use a simpler, more reliable treatment
abstain — explicitly decline to decide (requires human escalation)
reject   — reject the entire intent as infeasible
```

Abstention is a valid outcome, not a failure. It must be recorded with the
reason and the unresolved items.
