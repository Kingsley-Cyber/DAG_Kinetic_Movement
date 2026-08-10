---
id: cpcs.found.uncertainty.evidence_two_axis_model
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §8.1, §22, §28, SRC-004 §1]
primary_route: cpcs/knowledge/00_foundations/uncertainty/
secondary_routes:
  - cpcs/knowledge/00_foundations/epistemic_classes/
  - cpcs/knowledge/00_foundations/confidence/
interfaces: [state_x_continuity]
---

# Evidence Model: Acquisition Class × Epistemic State

## Principle

Evidence has two independent axes. A flat evidence class list conflates them;
CPCS must keep them separate.

**Acquisition class** — how the value entered the system:

```text
authored · observed · detected · measured · estimated · inferred · derived
```

**Epistemic state** — how strongly the system may claim the value is
established:

```text
known · uncertain · unknown · unobservable · contradictory
```

## Class semantics

- `measured` — requires an actual physical measurement source (force plate,
  inertial sensor, calibrated mocap). Pose-tracker output is `detected`, not
  `measured`.
- `estimated` — algorithmically inferred from observations under a declared
  model; the model assumptions must be recorded.
- `inferred` — semantic conclusion supported by evidence, not directly
  measured.
- `derived` — deterministic computation from other evidence; must carry
  `source_acquisition` (e.g. wrist velocity derived from detected keypoints).
- `unknown` — no sufficiently supported value exists.
- `unobservable` — available media cannot establish the value with acceptable
  uncertainty.
- `contradictory` — accepted sources materially disagree, unresolved.

Any acquisition class may carry any epistemic state.

## Canonical shape

```json
{
  "evidence": {
    "acquisition": "derived",
    "source_acquisition": "detected",
    "epistemic_state": "uncertain",
    "confidence": 0.84
  }
}
```

## Worked example (source §22)

A pose-tracker keypoint stream is `detected`; a velocity computed from it is
`derived` (source_acquisition `detected`) and must not claim `measured`
status in JSONL observation/audit records.

## ADRG evidence classes (SRC-004 §1)

SRC-004 introduces five evidence classes for reasoning-layer provenance:

```text
PACKAGE_ESTABLISHED  — directly established by the supplied research package
REPO_OBSERVED         — directly observed in the current CPCS repository
EXTERNAL_ESTABLISHED  — supported by an external primary/authoritative source
PROPOSED_CPCS         — recommended representation for CPCS
EXPERIMENTAL          — must be calibrated in the target repository/model stack
```

These are orthogonal to the acquisition × epistemic-state axes above. A
PACKAGE_ESTABLISHED claim may still be `uncertain` in epistemic state; an
EXPERIMENTAL claim is `unknown` until calibrated.

## Failure mode

Silently promoting `detected`/`derived` values to `measured` status inflates
downstream certainty and corrupts verification gating. Silently promoting
`PROPOSED_CPCS` to `EXTERNAL_ESTABLISHED` inflates evidence authority.

## CPCS-MX evidence classes (SRC-005 §2)

SRC-005 defines seven evidence classes that align with and extend the
acquisition axis above:

| Class | Meaning |
| --- | --- |
| `measured` | directly computed from a calibrated sensor or source clock under a declared method |
| `detected` | output of a detector operating on observed media |
| `inferred` | estimate derived by a model from incomplete evidence |
| `interpreted` | semantic or expressive reading |
| `authored` | deliberate creative value |
| `simulated` | result of a declared virtual model |
| `derived` | deterministic calculation from other records |

Confidence does not replace evidence class. A measured but poorly calibrated
sensor can be wrong; an interpreted label can be useful without being ground
truth.

## Research-status labels (SRC-005 §2.2)

A second taxonomy for claims in the paper:

```text
ESTABLISHED       — mature scientific, technical, or professional practice
CURRENT_PLATFORM  — documented by a current engine or tool (version-dependent)
CURRENT_RESEARCH  — recent peer-reviewed work, not yet production-standard
EMERGING          — preprint or early research, requires replication
PROPOSED          — CPCS-MX schema or conceptual contribution
OPERATIONALIZATION — engineering mapping from qualitative concept to data/metrics
```

For example, Laban Effort categories are ESTABLISHED movement-analysis
concepts. Mapping `direct Space` to a normalized path-curvature threshold is an
OPERATIONALIZATION. The mapping may be calibrated for a project but should not
be presented as the universal definition of directness.

## Provenance and conflict resolution (SRC-005 §2.3)

Each value retains a provenance chain. When sources conflict, CPCS-MX does
not silently average them. It applies declared authority and locks. A
reviewed frame-level contact can supersede a multimodal interpretation. A
director can author a different contact frame, but the change is recorded as a
creative override rather than rewriting the source observation.

## VOG evidence classes (SRC-009 EXTEND)

The Video Observation Graph (VOG) uses 5 evidence classes for the extraction
pipeline, a subset of the 7 CPCS-MX classes above:

| Class | VOG meaning |
| --- | --- |
| `measured` | Derived from media timing or numeric signal with a reproducible operation |
| `detected` | Output of a trained detector or classifier |
| `inferred` | Computed from multiple measurements under assumptions |
| `interpreted` | Semantic or expressive reading by a model or human |
| `authored` | Deliberate creative value or human-reviewed lock |

The VOG omits `defaulted` and `derived` from the graph layer. Confidence
fusion follows 5 rules: (1) do not average unlike evidence, (2) preserve
confidence type and calibration scope, (3) precedence for geometric facts:
source timestamps > calibrated geometry > uncalibrated detector > multimodal
semantic > free-form description, (4) precedence for narrative: human-approved
> multiple analyses > single analysis > geometry-only, (5) contradictions are
first-class outputs.

See `cpcs.evaluation.video_observation_graph` for the full VOG contract.
