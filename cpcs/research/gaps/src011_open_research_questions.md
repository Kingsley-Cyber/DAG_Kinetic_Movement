---
id: cpcs.gaps.src011_open_research_questions
kind: gap_register
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-011]
primary_route: cpcs/research/gaps/
---

# SRC-011 Open Research Questions

SRC-011 (ADRG Research Package v1.0) is the primary research package behind
the ADRG line, but its evidence boundary is explicit: engineering defaults
(profiles, thresholds, budgets, weights) are **proposed until the package's
own experiments run**. The package's E-ADRG experiments are renamed
ADRG-PKG-E1..E5 in the tree (collision with SRC-004 E-ADRG-001..006).

## Implementation gaps

1. No ADRG-PKG experiment has been executed. Run ADRG-PKG-E1 (mini fixed
   graph vs one-shot JSON) with the package fixtures — it is the cheapest and
   gates every mini-profile default (top_k 4, branch 2×1, repairs 1).
2. ADRG-PKG-E2 (decision ledger vs verbose rationale) must quantify the
   three CoT risks on CPCS tasks: false provenance rate, retrieval
   contamination, token overhead — before the "no raw CoT as canonical"
   doctrine is treated as more than a design principle.
3. ADRG-PKG-E3 (dense vs graph-bundle retrieval) must validate the graph
   expansion bounds (depth 2, max 24 nodes) and the coverage contract;
   the package's retrieval_queries.json (q001–q005) provides acceptance
   queries but no corpus beyond its own 78 records.
4. ADRG-PKG-E4 (dual-format ownership) overlaps the tree's E-ADRG-006
   (carrier effect). Design one shared protocol so both experiments feed
   the same carrier-evidence table instead of running twice.
5. The weighted router D = w_I·I + w_U·U + w_C·C + w_R·R − w_V·V has no
   calibrated weights. Until calibrated, D is a ranking aid; the budget
   ledger (100 units) must record the raw vector (SRC-006 doctrine).
6. Model-scaled profile numbers (top_k, branch widths, repairs) are
   defaults from reasoning_policy.yaml with `proposed_defaults_require_
   local_calibration`. Calibrate each against the CPCS model stack.
7. The 11 planner metrics are defined but only the tree's SRC-004 §16.1
   definitions exist; no metric has a tooled measurement (e.g.,
   decision_trace_faithfulness has no operationalization).
8. The package's concept cards (15 proposed, `concept_cards.proposed.jsonl`)
   and graph-builder extension (6 node kinds, 12 edges) target the lab repo
   (concepts.jsonl, build_graph.py). Adoption there is unstarted; the
   package's 5-stage migration plan has no owner.
9. Checkpoints A–I are enumerated but checkpoint H (post-generation
   adherence) depends on the verification loop's post-render half, which
   the lab has not closed (SRC-010 gap #4). A–G are runnable now.
10. Teacher-student decision distillation (§9) has no training or
    exemplar dataset; the pattern is documented, not built.

## Cross-source questions

11. **E-ADRG naming collision:** tree E-ADRG-001..006 (SRC-004) vs package
    ADRG-PKG-E1..E5 (SRC-011). Mapping documented in adrg_experiments.md;
    decide whether a future merged program renumbers to a single namespace
    or keeps both registries.
12. **Evidence-label vocabulary:** package RAG schema uses 6 labels
    (ESTABLISHED/EMERGING/PROPOSED/OPERATIONALIZATION/PROJECT-OBSERVED/
    CAUTION); evidence_two_axis_model.md ADRG section uses SRC-004's 5
    classes (PACKAGE_ESTABLISHED/REPO_OBSERVED/EXTERNAL_ESTABLISHED/
    PROPOSED_CPCS/EXPERIMENTAL). Reconcile into one vocabulary with a
    mapping table, or declare them intentionally parallel.
13. The package's 8 realization statuses match the tree's
    capability_classes_and_loss_records (SRC-004 §22) exactly — good. But
    the package's compiled_to edge constraint makes statuses schema-enforced;
    the tree's compile_key (SRC-006 §8) is not in the ADRG schema. Decide
    whether schema gains adapter-version fields.
14. Weighted router D vs reasoning_budget_router.md's "no universal weighted
    scalar" doctrine (SRC-006 §4.7): resolved as routing default vs vector
    record, but the resolution needs an experiment (ADRG-PKG-E1 can provide
    it) before it is stable.
15. The package's 5 promotion criteria vs the tree's 6 adoption criteria:
    tree criteria remain the strict superset. Keep both, or unify when the
    first ADRG-PKG results arrive.
16. Package §20 integration (concept_cards.proposed.jsonl) proposes 15 cards
    including c_reasoning_control_plane, c_decision_ledger, c_variant_lattice
    — several map to tree cards distilled here (adrg_reasoning_graph_schema,
    decision_record, director_invariant). Build the crosswalk before
    importing into the lab repo.

## Empirical unknowns

17. Small-model limits (§22): the mini profile (fixed DAG, 1 responsibility
    per call, top_k 4) is CAUTION-grade until ADRG-PKG-E1 measures failure
    rates vs standard/large on the same tasks.
18. Self-critique limits (§22): intrinsic critique passes (standard 1,
    large 1) are proposed; S013-class evidence says self-correction without
    external feedback is unreliable. The tree's external-validation-over-
    self-critique doctrine already covers this; quantify the residual.
19. Graph complexity costs (§22): large-profile graphs (5×3 branches,
    specialist critics, self-consistency) may exceed the 24-node expansion
    bound. Measure actual graph sizes under the profile before trusting the
    bound.
20. Creative homogenization (§22): variant lattices with maximum_simultaneous_
    deltas 2 and J(S) selection may narrow creative range. No experiment
    measures diversity quality (human-judged) vs J(S) ranking.
21. Prompt injection / format security (§22): the XML/JSON/YAML security
    rules are enumerable but untested against adversarial authoring inputs.
    Build the adversarial test set.

## Governance notes

- All profile numbers, weights, bounds (depth 2, 24 nodes), and the 100-unit
  ledger are proposed defaults from one research package — not calibrated
  constants. Replace only with held-out CPCS evidence.
- The package self-declares its evidence boundary; the tree must not
  silently promote PACKAGE_ESTABLISHED defaults to validated rules.
- References [S001]–[S042] index 42 sources; S036–S042 are repo documents
  (including CPCS paper v1.2 [S041]) — the package is the ADRG family's
  primary artifact and SRC-004's U01; keep the two distillations linked.
