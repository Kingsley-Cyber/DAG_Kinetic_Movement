---
id: cpcs.mx.risk_profile
kind: metric_contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §29, §38]
primary_route: cpcs/runtime/07_compiler/
secondary_routes:
  - cpcs/knowledge/19_generation_complexity/
interfaces: [cpcs.compiler.control_priority_attention_budget, cpcs.mx.action_template]
---

# RiskProfile and Shot Decomposition

Use a complexity/risk vector rather than an unexplained scalar.

## Risk vector

```json
{
  "risk_profile": {
    "actor_count": 3,
    "simultaneous_primitives": 5,
    "causal_depth": 4,
    "contact_count": 3,
    "occlusion_burden": "high",
    "camera_complexity": "high",
    "identity_burden": "high",
    "retargeting_complexity": "medium",
    "secondary_motion_complexity": "low"
  }
}
```

## Risk drives strategy

```text
high contact + high camera     → simplify camera
high identity + high occlusion  → stronger reference/conditioning
high action density             → shot decomposition
high retarget complexity        → stronger target constraints / pre-solve
```

## Shot decomposition

The compiler should split a request when control complexity exceeds reliable
provider capacity. Preferred split boundaries:

```text
stable state · interaction outcome · camera reset · identity/visibility bridge
```

## Verification

`test_risk_vector_present_for_complex_shots`,
`test_decomposition_at_valid_boundaries`,
`test_decomposition_preserves_continuity`.
