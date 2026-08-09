---
id: cpcs.adrg.experiments
kind: experiment_design
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-004 §24, §25, §27]
primary_route: cpcs/research/sources/experiments/
secondary_routes:
  - cpcs/00_governance/policies/
  - cpcs/runtime/04_synthesis/
interfaces: [cpcs.adrg.decision_record, cpcs.adrg.decision_aware_routing, cpcs.adrg.state_contraction]
---

# ADRG Controlled Experiments

Six controlled experiments are required before any ADRG policy/operator is
promoted from `unexplored` to verified (SRC-004 §24, §25).

## E-ADRG-001 — Decision IR vs current strategy-only output

**Question:** Does explicit DecisionRecord improve trace completeness without
reducing compile success?

Compare: A (current reasoning strategy only) vs B (strategy + ADRG
DecisionRecord).

Measure: decision completeness, evidence resolution, constraint recall, compile
success, token cost, latency.

## E-ADRG-002 — Router features

Compare: A (current task-class policy routing) vs B (task-class +
impact/uncertainty/coupling/irreversibility/validator strength).

Measure: unnecessary branching, decision quality, cost, latency,
hard-constraint violations.

## E-ADRG-003 — State contraction

Compare: A (full retrieved context) vs B (active_state +
source/decision/failure memory).

Measure: decision accuracy, evidence resolution, token cost, omission rate,
recovery after multi-step repair.

## E-ADRG-004 — Selective ToT

Branch only on one high-impact camera decision.

Measure: selected-plan quality, semantic diversity, cost, render adherence.

## E-ADRG-005 — Failure-directed repair

Compare: A (regenerate full strategy) vs B (identify earliest responsible layer
+ JSON Patch).

Measure: repair success, tokens, latency, collateral changes, invariant
violations, regression rate.

## E-ADRG-006 — Carrier effect

Hold canonical meaning constant. Compare: NL, YAML, JSON, XML, YAML+JSON,
YAML+XML.

Measure: semantic preservation, omission, contradiction, parse/schema
validity, token cost, latency.

Do not promote a carrier as intrinsically better without this experiment.

## Fixtures (minimum)

```text
fixture_direct_selection
fixture_tot_camera_choice
fixture_got_performance_camera_coupling
fixture_hard_invariant_rejection
fixture_conflicting_evidence
fixture_missing_capability
fixture_compile_loss
fixture_validator_failure
fixture_one_patch_repair
fixture_second_repair_escalation
fixture_semantically_duplicate_variants
fixture_carrier_equivalence
```

## Promotion rules

A new ADRG policy/operator remains `unexplored` until:

1. an isolated experiment supports it;
2. it repeats across multiple tasks or is explicitly scoped;
3. cost and failure cases are recorded;
4. no rights/safety issue remains;
5. the concept/policy record is updated with evidence and calibrated confidence.

## Package experimental program (SRC-011 EXTEND)

> **Source:** SRC-011 §21 — "Experimental program". The package defines its
> own E-ADRG-001..005. These are **different experiments** from the tree's
> E-ADRG-001..006 above; to avoid collision, package experiments are
> registered as **ADRG-PKG-E1..E5**.

### Naming-collision mapping

| Package (§21) | Tree (SRC-004 §24) | Relation |
| --- | --- | --- |
| PKG-E1 mini fixed graph vs one-shot | — | new (subset of reasoning-mode eval) |
| PKG-E2 decision ledger vs verbose rationale | — | new (ledger doctrine) |
| PKG-E3 dense vs graph-bundle retrieval | — | new (graph-aware RAG) |
| PKG-E4 dual-format semantic ownership | E-ADRG-006 carrier effect | overlapping (carrier × ownership) |
| PKG-E5 selective ToT for camera | E-ADRG-004 selective ToT | overlapping (ToT camera) |
| — | E-ADRG-001/002/003/005 | package has no equivalents |

### Core research questions (7)

RQ1 Does a fixed mini graph beat one-shot JSON for small models? · RQ2 Does
the decision ledger preserve trace quality without verbose rationale? · RQ3
Does graph-bundle retrieval beat dense-only retrieval? · RQ4 Does declared
format ownership beat raw concatenation? · RQ5 Does selective ToT improve
camera decisions at bounded cost? · RQ6 How does each result scale across
model classes (mini/standard/large)? · RQ7 Which planner metrics predict
video-level adherence?

### Factors

`planner_model_class · reasoning_mode · retrieval_mode · output_carrier ·
candidate_policy · verifier` — all crossed with the task set and frozen
adapter/verifier versions.

### Planner metrics (11)

evidence_selection_precision · evidence_resolution · decision_trace_faithfulness ·
constraint_preservation · alternative_diversity · unnecessary_branching ·
strategy_stability · token_cost · decision_latency · repair_efficiency ·
regression_rate (definitions in verification_layers.md SRC-004 §16.1). Video
metrics follow the existing verification metric vectors.

### Causal discipline (6 conditions)

Promote a claim only when: isolated comparison; control variables frozen;
predeclared primary outcomes; cost accounting complete; automatic-judge
gains corroborated by blinded human or executable checks; replication across
the intended model profile.

### Promotion criteria (5, package)

1. repeatable, isolated gain on a predeclared outcome; 2. no hard-constraint
regression beyond the declared bound; 3. improvement persists under full
cost accounting; 4. verified by external checks, not self-critique; 5.
replicates across model classes or is explicitly scoped. (Tree's 6 adoption
criteria above remain the strict superset for becoming a default.)

## Reasoning-mode evaluation (SRC-006 §10)

### Two-stage design

- **Stage A — planning and compiler isolation:** no video generation; each
  mode must produce valid, semantically correct, non-contradictory canonical
  state and provider projection.
- **Stage B — generation and repair:** provider outputs from accepted plans;
  evaluate adherence, failure localization, repair scope, regression, renders,
  cost. The same accepted canonical task is used across modes.

### Fixture families F1–F14

| Fixture | Required stress |
| --- | --- |
| F1 simple direct | one actor, one action, no material branch |
| F2 laterality | left/right action where reversal is a hard failure |
| F3 contact phases | approach → contact → transfer/release → effect |
| F4 two-actor binding | each actor has a distinct action/attribute |
| F5 spatial topology | relative placement changes across time |
| F6 causal consequence | effect must follow and depend on contact/action |
| F7 camera-performance conflict | desired framing conflicts with visibility of required action |
| F8 narrative reveal | viewer and character knowledge must remain distinct |
| F9 audio sync | dialogue or sound must align to a visible event |
| F10 provider gap | one required control is semantic/unsupported |
| F11 localized failure | injected or observed single-path failure suitable for patch |
| F12 ambiguous failure | evidence supports multiple diagnoses |
| F13 equivalent carriers | multiple serializations of identical meaning |
| F14 misleading similarity | similar wording but materially different actor/order/control |

### Reasoning modes (exact implementations)

`direct` = one generation, deterministic validation, no revision;
`aot_prompting` = one/few calls with a frozen algorithmic search exemplar;
`selective_tree_search` = material branch generator + evaluator + bounded
search; `typed_graph_aggregation` = independent typed proposals merged through
graph rules; `bounded_local_search` = fixed operation registry and immutable
state transitions; `failure_directed_repair` = render/observation → localized
patch → recompile; `hybrid` = predeclared router, never a hand-selected best
result after the fact. Do not use `AoT` as a synonym for local search.

### Budget levels (vectors, not token counts)

```text
B0 direct: 1 model call, 0 extra verifier calls, 1 render
B1 light:  up to 3 model calls, 2 candidates, 1–2 renders
B2 medium: up to 8 model calls, 4 candidates, 3–4 renders
B3 high:   predeclared upper bound, used only on hard/solvable fixtures
```

### Randomization and replication

Multiple independent runs per stochastic cell (count from pilot variance, not
an arbitrary number); block by canonical task and provider/model; preserve all
failed and invalid runs; blind human pairwise comparisons; keep `direct` as a
champion in iterative comparisons; freeze verifier/adapter versions; separate
development fixtures from held-out certification fixtures.

### Adoption criteria (6)

A reasoning policy may become a default only if, on held-out tasks: (1) it
improves at least one predeclared primary quality/adherence outcome; (2) it
does not worsen hard-constraint violations beyond the declared
non-inferiority bound; (3) its improvement persists under complete cost
accounting; (4) verifier gains correlate with blinded human evaluation where
judgments are subjective; (5) failures, malformed states, and unsupported
controls remain visible; (6) the result replicates across the intended
provider/model profile. If a mode improves an automatic judge but not human
or executable checks, it is not validated.

## Verification

`test_experiment_has_control_group`,
`test_promotion_requires_experiment_evidence`,
`test_unexplored_status_before_calibration`,
`test_fixture_family_stress_declared`,
`test_mode_label_matches_exact_implementation`,
`test_adoption_requires_held_out_replication`.
