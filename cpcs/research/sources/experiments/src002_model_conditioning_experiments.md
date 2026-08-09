---
id: cpcs.experiment.src002_model_conditioning
kind: experiment_design
epistemic_status: PROJECT_DERIVED
acquisition: authored
status: designed, not executed
sources: [SRC-002 §23, L2.§49]
primary_route: cpcs/research/sources/experiments/
---

# SRC-002 Model-Conditioning Experiments

## Carrier experiment (SRC-002 §23)

No evidence justifies declaring JSON/YAML/XML/NL universally superior for
FACS/Laban/Bartenieff providers. Create 100 scenes with identical canonical
JSON meaning; generate into JSON · YAML · XML · structured Markdown · NL ·
hybrid structured+NL. Randomize order.

Measure: schema adherence · control preservation · AU preservation · bilateral
preservation · temporal-order preservation · Laban-factor preservation ·
Bartenieff-pattern preservation · omission rate · contradiction rate ·
provider adherence · token count · latency · regeneration rate. Use paired
scene-level comparisons; report mean/median/95% CI/omission/contradiction/
token/latency. Do not infer superiority from one provider.

## Operational-layer experiments (SRC-002 L2.§49)

| Exp | A vs B | Measure |
|---|---|---|
| A — dictionary vs application packet | concept-definition only vs +applicability+guardrails vs +realization | concept-selection accuracy · incorrect framework selection · unsupported inference rate · provider adherence · prompt length · latency |
| B — generic vs action-conditioned | `Strong→generic` vs `Strong×action→realization` | action preservation · quality adherence |
| C — static vs temporal envelope | `Flow=Bound` vs `Bound→Free→Bound` | temporal performance · phase localization |
| D — full graph vs compact packet | retrieve all vs compact application bundle | decision accuracy · contradiction · unsupported invention · token · latency |
| E — minimal-pair reasoning | give controlled pairs, ask expected visible change | whether research became operational knowledge |

## Disposition

P1–P2 per `00_governance/policies/distillation_implementation_priority.md`.
Output is a **CPCS empirical profile**, never a universal claim.
