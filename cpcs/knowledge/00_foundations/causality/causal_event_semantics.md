---
id: cpcs.found.causality.causal_event_semantics
kind: principle
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §10.6, §28, SRC-002 L2.§26, SRC-004 §6.2, §10]
primary_route: cpcs/knowledge/00_foundations/causality/
secondary_routes:
  - cpcs/knowledge/01_story_direction/narrative_causality/
  - cpcs/knowledge/18_sequence_continuity/
interfaces: [causality_x_editing, state_x_continuity]
---

# Causal Event Semantics

## Principle

`phase_graph` provides temporal organization but cannot express **why** a
downstream event occurs. Causality is a separate semantic dimension:

```text
PhaseGraph    = WHEN
CausalEvent   = WHY / BECAUSE
SpatialState  = WHERE
MotionEvent   = HOW
Interaction   = WITH WHAT / WHOM
Continuity    = STILL THE SAME?
Visibility    = WHAT CAN BE OBSERVED?
```

The causal representation must distinguish — they are not interchangeable:

```text
temporal succession · causal dependency · correlation ·
narrative motivation · observed co-occurrence
```

SRC-002 L2.§26 sharpens the predicate vocabulary:

```text
A causes B   A enables B   A prevents B   A motivates B
A precedes B (temporal only)   A correlates with B
```

`A precedes B` and `A causes B` answer different questions and must remain
separate edges. A causal edge for creative authoring may carry
`evidence_class: authored` rather than being empirically established.

## Proposed `CausalEvent` object (PROJECT_DERIVED)

```json
{
  "causal_event": {
    "event_id": "evt_water_impact_01",
    "cause": "A_kick_intersects_water",
    "produces": ["surface_displacement", "vertical_water_column", "splash"],
    "depends_on": ["B_evasive_dive"],
    "must_not_imply": ["A_contacts_B"]
  }
}
```

`must_not_imply` is load-bearing: a causal miss that produces water
displacement must not be read as actor–actor contact.

## Applies when

Any downstream event depends on an upstream event beyond mere temporal
order; runtime owner is world-model `causal_events` / `state_transitions`.

## Verification

`causal_edge_preservation`, `causal_false_positive_rate`
(SRC-001 §10.9/§26 tests).

## Design causality vs empirical causality (SRC-004 §6.2, §10)

`design_causes` means: *this treatment is intended to cause this
control/effect.* It is an authored intent.

`causal_claim` means: *empirical evidence supports that changing X causes Y.*
It requires a controlled comparison to promote.

These are not the same. The causal design chain (SRC-004 §10) operates at the
decision level:

```text
problem → treatment → decision → control → expected_effect → verification
```

This is distinct from event-level causality (A_kick causes water_splash). Both
are causal but at different planes. See `cpcs.adrg.causal_design_chain` and
`cpcs.adrg.execution_edge_vocabulary` for the decision-level contract.

## Open questions

SRC-001 §26 Q13 (causal constraints vs creative variation), Q14
(decomposition vs stronger prompting) — see `research/gaps/`.
SRC-004 §27 Q9 (evidence threshold for promoting reasoning pattern into durable
knowledge) — see `research/gaps/src004_open_research_questions`.

## Action graph edges (SRC-005 §10.4)

SRC-005 defines an action graph whose edges can mean `before`, `overlaps`,
`causes`, `requires`, `targets`, or `interrupts`. This allows the same
movement content to be rephrased: a sudden style compresses preparation and
increases acceleration; a sustained style lengthens transitions; a feint
interrupts before contact and redirects the action graph. These edges extend
the causal vocabulary without introducing new fundamental relation types —
they are composites of the existing `precedes`, `causes`, `enables`, and
`motivates` relations.

## Typed contact taxonomy (SRC-005 §10.2)

SRC-005 defines eight contact types that complement the interaction lifecycle:

```text
support · grasp · surface_touch · staged_near_contact ·
simulated_impact · environmental_collision · attachment · break_contact
```

A contact record stores participants, local points, surface normal, start/end,
confidence, friction/compliance where simulated, and whether the event is hard
or soft. Contacts are among the strongest anchors for believable motion; foot
skating occurs when a foot expected to be planted moves relative to the ground.
