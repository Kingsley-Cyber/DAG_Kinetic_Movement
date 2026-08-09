---
id: cpcs.mx.simulation_provenance
kind: contract
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-003 §36]
primary_route: cpcs/knowledge/00_foundations/
secondary_routes:
  - cpcs/knowledge/09_force_physics/
interfaces: [cpcs.mx.observation_provenance]
---

# Simulation Provenance

If a quantity is simulated, reproducibility metadata must remain accessible.

## Provenance record

```json
{
  "simulation_ref": {
    "solver": "solver_id",
    "timestep": 0.008333,
    "mass_model": "mass_profile_01",
    "contact_model": "contact_model_02",
    "gravity": [0, -9.81, 0],
    "friction_model": "model_03",
    "initial_conditions_ref": "ic_01"
  }
}
```

Exact simulation parameters need not all live in canonical motion IR, but
reproducibility metadata must remain accessible.

## Verification

`test_simulation_ref_present_when_simulated`,
`test_solver_and_timestep_recorded`.
