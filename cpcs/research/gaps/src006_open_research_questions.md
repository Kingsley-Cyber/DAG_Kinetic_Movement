---
id: cpcs.gaps.src006_open_research_questions
kind: gap_register
epistemic_status: SOURCE_EVIDENCE
acquisition: authored
sources: [SRC-006 §1.5, §1.6, §13.5, build packet §"Open research questions"]
primary_route: cpcs/research/gaps/
---

# SRC-006 Open Research Questions

SRC-006's build packet closes with ten open research questions, plus
seven future-research items. None has a verified CPCS answer yet; each
requires fixtures and measured outcomes before any policy becomes a default.

## Build-packet open research questions

1. Which existing CPCS files own these semantics (executor state, capsule,
   branches, graph, failures, repair, budget, equivalence)?
2. Which current executors are genuinely distinct policies versus duplicated
   prompt wrappers?
3. What minimal capsule passes long-horizon continuation-equivalence tests?
4. Which CPCS task features predict benefit from branching, graph
   aggregation, or repair?
5. Which provider controls are exact, approximate, semantic, or unsupported
   by version?
6. Which automatic verifiers are calibrated against CPCS human judgments?
7. What materiality tolerances are valid for time, camera, motion, space,
   and audio?
8. When does verifier uncertainty make further search wasteful?
9. Does any format advantage replicate for each model/provider profile?
10. Can repair improve the failed requirement without increasing
    protected-invariant regressions?

## Future research (§13.5)

- calibrated CPCS difficulty and solvability models;
- provider-specific control reliability, not only capability presence;
- causal and physical verification beyond semantic VLM judgment;
- uncertainty propagation from VOG observations into repair decisions;
- long-horizon capsule sufficiency across scenes/edits;
- human preference models that preserve domain/cultural specificity;
- active selection of when human review is worth its cost.

## Experiment-only hypotheses (§13.3)

AoT prompting improves CPCS planning at lower call count · graph aggregation
outperforms a single structured Director pass · a specific carrier improves a
specific model/provider profile · viewer-guidance modeling improves
camera/edit adherence · learned complexity estimates outperform
deterministic triggers · more test-time video renders monotonically improve
CPCS outcomes.

## Closure-matrix gaps (11)

Executor-relative atoms (P0) · continuity compression (P0) · selective
branching (P1) · cross-view reasoning (P1) · AoT/local-search confusion (P1)
· failure-directed repair (P0) · adaptive reasoning budget (P1) · state
equivalence (P0) · carrier interaction (P1) · video verification (P0) ·
provider exactness (P0).

## Build order (8 phases)

```text
P0 repository mapping and duplicate-authority audit
P1 schemas + immutable state + audit + budget instrumentation
P2 normalization/equivalence profiles + adversarial fixtures
P3 failure/repair contract + protected-invariant tests
P4 direct baseline + planning-only experiment harness
P5 selective tree and typed graph policies behind flags
P6 provider render experiments and verifier/human calibration
P7 adaptive router only after held-out evidence
```

No production default should change merely because the schema exists. Each
research policy graduates only through the six adoption criteria in §10.6.
