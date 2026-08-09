# Repository Audit and Ownership Map

## Inspected target

- Repository: `Kingsley-Cyber/ai-video-movement-prompt-system`
- Revision: `eb0fc359de4bb61075db49ca0dad08d4d6ed5114`
- Inspection date: `2026-08-05`
- Branch observed: `main`

## Architectural findings

1. The repository defines one universal provider-neutral score as semantic authority.
2. Prompt serializations and provider requests are authoring/execution projections, not competing authority.
3. The compiler owns score resolution and non-submitting provider builds.
4. Verification owns artifact compliance, diagnosis, conflicts, and bounded repair planning.
5. The second brain separates curated truth, immutable occurrence evidence, and rebuildable derived inference.
6. Research may propose but cannot promote itself or directly change production authority.
7. The current architecture remains not production-qualified without live-provider, calibration, held-out, and other external gates.

## Files reviewed

- `AGENTS.md`
- `ARCHITECTURE.md`
- `lab/AGENTS.md`
- `lab/CONTROL_SURFACE.md`
- `lab/FORMAT_CONTROL_MAP.md`
- `lab/UNIVERSAL_MOTION_SKELETON.md`
- `lab/compiler/AGENTS.md`
- `lab/compiler/schemas/universal_score.schema.json`
- `lab/compiler/providers/veo_3_1.yaml`
- `lab/verification/AGENTS.md`
- `lab/verification/schemas/compliance_report.schema.json`
- `lab/second_brain/AGENTS.md`
- `lab/second_brain/IMPLEMENTATION_PLAN.md`

## Ownership matrix

| Failure family | Current owner | Coverage | Required extension |
| --- | --- | --- | --- |
| A | lab/compiler universal score continuity/actions; lab/verification assertions; lab/second_brain evidence | partial | continuity + actions + verification |
| B | lab/compiler entities/continuity/assets; lab/verification state checks | partial | entities + continuity + verification |
| C | lab/compiler entities/interactions/continuity; lab/verification identity-role checks | partial | entities + interactions + continuity + verification |
| D | lab/compiler scenes/shots/actions/camera; lab/verification geography checks | partial | scenes + shots + actions + camera + verification |
| E | lab/compiler beats/actions/editing; lab/verification event-graph checks | partial | beats + actions + editing + verification |
| F | lab/compiler actions/interactions/audio; lab/verification causal assertions | partial | actions + interactions + effects + verification |
| G | lab/compiler interactions/motion/camera; lab/verification measured/human lanes | partial | interactions + motion + camera + verification |
| H | lab/compiler motion/interactions; lab/verification support/momentum metrics | partial | motion + interactions + verification |
| I | lab/compiler interactions/style/continuity; lab/verification material-response checks | partial | interactions + style + continuity + verification |
| J | lab/compiler camera/motion/shots; lab/verification camera/actor separation | partial | camera + motion + shots + verification |
| K | lab/compiler editing/continuity/style; lab/verification cut/effect classification | partial | editing + continuity + style + verification |
| L | lab/compiler motion/style/performance; lab/verification recovery assertions | partial | motion + style + performance + verification |
| M | lab/compiler provider build and adapter; lab/experiments format arms | partial | compiler + provider adapter + experiment registry |
| N | lab/compiler constraints/warnings/loss report; shot planner; lab/experiments capacity staircases | partial | compiler + loss report + shot planner |
| O | lab/compiler audio/actions/beats; lab/verification AV anchors | partial | audio + actions + verification |
| P | lab/verification; lab/second_brain immutable evidence and human calibration | partial | verification + immutable evidence + human calibration |

## Repository gaps

### repo_gap_001

**Finding:** The requested root REPO_CONTINUITY_IMPLEMENTATION_PLAN.md was not found in the inspected tree.

**Impact:** The research uses ARCHITECTURE.md plus lab/second_brain/IMPLEMENTATION_PLAN.md as the nearest current architecture/continuity owners; this substitution must be reviewed by the repository owner.

**Action:** Do not create a duplicate plan. Confirm whether the root file was renamed, moved, or never committed.

### repo_gap_002

**Finding:** Only Veo 3.1 is represented as a versioned compiler provider capability profile in the inspected repository.

**Impact:** Seedance, Kling, Runway, MiniMax, Wan, LTX, and other rows in this research remain knowledge records, not executable adapters.

**Action:** Add provider profiles one at a time through the existing compiler provider schema after official-interface and live-request qualification.

### repo_gap_003

**Finding:** The universal score has existing top-level owners but several relevant objects remain structurally open rather than typed for hidden state, state transitions, and causal events.

**Impact:** Prompt adapters can serialize intent, but cannot deterministically prove that all continuity obligations were represented.

**Action:** Review the candidate schemas in this package as minimal nested extensions under existing owners; do not add a second root score.

### repo_gap_004

**Finding:** Current verification supports artifact identity/basic media properties and a small number of closed measurements, but not the complete failure metric catalog.

**Impact:** Most new failure assertions require new calibrated measured/semantic/human lanes before they can block or promote a run.

**Action:** Implement metrics incrementally behind lab/verification, starting with actor/object count, event order, screen side, effect origin, and occlusion reappearance region.

### repo_gap_005

**Finding:** No authorized provider render campaign or human calibration bundle was available in this session.

**Impact:** The package cannot report provider-specific success rates or universal complexity thresholds.

**Action:** Execute the pre-registered repeated-seed fixtures and record raw prompts, requests, seeds, outputs, evaluator versions, and human verdicts.

## No-parallel-schema decision

The candidate contract schemas in `schemas/` are research review artifacts. If accepted, their fields should become typed nested definitions beneath existing universal-score owners and existing verification/evidence records. They must not become a new root score, alternate compiler, or independent failure ontology.

## Detailed overlap

`REPOSITORY_OVERLAP_MATRIX.csv` contains one row per failure record with current owner, coverage status, missing evidence, missing mitigation, missing test, and recommended owner.
