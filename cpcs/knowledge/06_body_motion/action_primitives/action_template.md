---
id: cpcs.mx.action_template
kind: schema_draft
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §3, §6]
primary_route: cpcs/knowledge/06_body_motion/action_primitives/
secondary_routes:
  - cpcs/runtime/04_synthesis/
interfaces: [cpcs.mx.typed_primitive_taxonomy, cpcs.mx.motion_realization, cpcs.canonical.control_scope]
---

# ActionTemplate

A primitive is too low-level to answer what should happen when the director asks
for a particular action. `ActionTemplate` is the missing decision layer between
director intent and motion primitives.

## Definition

```text
ActionTemplate =
    action identity
    + preconditions
    + applicability
    + phases
    + primitive composition
    + modifiers
    + spatial requirements
    + support requirements
    + interaction requirements
    + outcome branches
    + invariants
    + realization candidates
    + verification expectations
```

## Example: strike

```yaml
action_template:
  id: strike
  preconditions:
    actor_present: true
    target:
      required: true
  phases:
    - anticipation
    - execution
    - interaction
    - follow_through
    - recovery
  composition:
    anticipation:
      - primitive: shift_weight
      - primitive: retract
    execution:
      - primitive: reach
      - modifier: accelerate
    interaction:
      - event: contact
    follow_through:
      - modifier: continue
    recovery:
      - primitive: stabilize
  outcomes:
    - contact
    - blocked_contact
    - near_miss
    - complete_miss
    - interrupted
    - deflected
  invariants:
    - actor_identity
    - side
    - action_identity
```

## Action branching

A motion plan cannot assume the desired interaction succeeds. Each template
must declare outcome branches with contracts.

```json
{
  "action_template": "strike",
  "selected_branch": "near_miss",
  "branch_contract": {
    "requires": ["visible_separation", "no_impact_deformation"],
    "produces": ["evasive_reaction"],
    "forbids": ["impact_recoil_as_collision"]
  }
}
```

This prevents a generator from converting "near miss" into an accidental hit.

## Canonical branch model

```text
Action
 ├── intended path
 └── outcome
       ├── success
       ├── blocked
       ├── near_miss
       ├── miss
       ├── interrupted
       ├── deflected
       ├── caught
       └── cancelled
```

## Verification

`test_action_template_resolves_to_branch`,
`test_branch_contract_enforced`,
`test_invariants_preserved_across_branches`.
