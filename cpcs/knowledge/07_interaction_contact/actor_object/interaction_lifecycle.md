---
id: cpcs.contact.interaction_lifecycle
kind: mechanism
epistemic_status: PROJECT_DERIVED
acquisition: authored
sources: [SRC-001 §9, §23, SRC-001-U08, SRC-001-U09, SRC-002 L2.§32]
primary_route: cpcs/knowledge/07_interaction_contact/actor_object/
secondary_routes:
  - cpcs/knowledge/07_interaction_contact/near_contact/
  - cpcs/knowledge/07_interaction_contact/impact/
interfaces: [motion_x_contact, state_x_continuity]
---

# Interaction Lifecycle and Occluded Contact

## Mechanism

Canonical actor–object/actor–actor interaction lifecycle
(not every interaction has every state):

```text
approach → proximity → alignment → contact_candidate → contact_established
→ grasp/support/collision → displacement/transfer → release → separation
→ reaction/recoil
```

Contact is a **temporal interval with state, site, and visibility**, not a
boolean instant. External support: explicit contact position/timing
representation (U08); contact points are often hard to observe because hands
or objects occlude the contact site (U09).

## Canonical interaction object (condensed)

```json
{
  "interaction_id": "int_004",
  "actor_a": "actor_01", "actor_b": "object_07",
  "type": "impact",
  "lifecycle": [
    { "state": "approach", "start": 1.10, "end": 1.24 },
    { "state": "contact_established", "start": 1.24, "end": 1.30,
      "evidence_class": "detected", "confidence": 0.89 },
    { "state": "recoil", "start": 1.30, "end": 1.62,
      "evidence_class": "inferred", "confidence": 0.74 }
  ],
  "contact": { "site_a": "right_fist", "site_b": "torso",
               "visibility": "partially_occluded" }
}
```

## Occluded contact rule

Never encode `{"contact": true}` when the contact point is visually hidden
and merely plausible. Use
`{status: estimated, visibility: occluded, confidence: ...}` or
`{status: unknown}` depending on evidence.

## Near-miss rule

`action_apex` without contact must compile as explicit near-miss description
(fist passing close to target), never as `contact=true`
(worked example: SRC-001 §23 boxer near-miss cross).

## Multi-actor coordination primitives (SRC-002 L2.§32)

Cinematic performance is relational. A small universal interaction set
(not new FACS/Laban predicates):

```text
initiates · reacts_to · attends_to · tracks · mirrors · counters ·
synchronizes_with · leads · follows · turn_takes_with · approaches ·
withdraws_from
```

A phase-offset representation records initiator/reactor, trigger/response,
and an offset (authored `s` or `measured` + timebase) — never conflated
with a causal edge.

## Failure modes

- Proximity inferred as contact (`test_contact_not_inferred_from_proximity`).
- Near-miss compiled as contact.
- Boolean contact erases occlusion visibility, blocking continuity reasoning.

## Typed contact taxonomy (SRC-005 §10.2)

SRC-005 defines eight contact types that complement the lifecycle above:

| Type | Meaning |
| --- | --- |
| `support` | foot, hand, knee, or body supporting weight |
| `grasp` | hand or appendage constrained to an object |
| `surface_touch` | visible touch without substantial support |
| `staged_near_contact` | intentionally appears to connect from the camera without collision |
| `simulated_impact` | virtual dynamic event |
| `environmental_collision` | body or prop meets scene geometry |
| `attachment` | weapon, wearable, harness, or rig constraint |
| `break_contact` | release or takeoff |

A contact record stores participants, local points, surface normal, start/end,
confidence, friction/compliance where simulated, and whether the event is hard
or soft. In a fight shot, contact timing couples multiple systems: attacker
end-effector path, defender target position, near-contact decision, defender
reaction onset, sound onset, VFX accent, camera shake, and edit point. The
event graph preserves that causal bundle while allowing each offset to be
edited.

## Typed lifecycle stages (SRC-007 G005)

SRC-007 defines a nine-stage lifecycle and requires each stage to be
classified as **event**, **relation**, or **derived classification**:

```text
approach · near_contact · contact · impact · support · grasp
· release · separation · reaction
```

- `approach`, `contact`, `impact`, `release`, `separation` are **events**
  (instantaneous or interval facts that change state).
- `near_contact`, `support`, `grasp` are **relations** (enduring typed
  connections between entities).
- `reaction` is a **derived classification** (response causally linked to a
  prior contact event).

Legal/illegal transitions, cardinality, side and anatomical-site semantics,
and contact identity across frames must be declared per stage. Multi-surface
contact is representable. Occlusion lowers confidence without fabricating
continuity: an occluded contact keeps its identity and becomes
`estimated`/`unknown`, it is never deleted or silently interpolated.

Required traces: grasp/release, impact/reaction, sustained support, and an
unobservable contact — each with the exact runtime decision the contact
object enables (e.g. support event gates balance validation; release enables
held-object state update; reaction onset enables causal effect ordering).

`test_contact_identity_preserved_across_frames`,
`test_occlusion_lowers_confidence_not_identity`,
`test_transition_legality_enforced`,
`test_reaction_derived_from_contact_event`.

## Predicate vocabulary and contact topology (SRC-012 EXTEND)

> **Source:** SRC-012 topic 7 — "Interaction Layer: Motion Predicates and
> Contact Topology"

The KB supplies a controlled predicate vocabulary (~40 predicates,
HICO-DET-seeded) with core/optional roles, preconditions, and effects:
`support · touch · contact · grasp · hold · release · push · pull · press ·
slide · roll · carry · lift · lower · throw · catch · place · open · close ·
strike · block · parry · deflect · redirect · trap · pin · evade · dodge ·
intercept · collide · stagger · yield · resist · guide · embrace · shield ·
mount · disarm · handoff · point_at · look_at · approach · retreat · circle`.

Compound predicates carry explicit preconditions/effects: `throw` = grasp →
accelerate object → release → free flight; `catch` = intercept → absorb
relative motion → establish support/grasp; `block` changes/terminates an
incoming path through interposition; `parry` creates brief redirecting
contact; `evade` succeeds without required contact.

Predicate record fields extend the canonical interaction object above and
bind the predicate to the phase grammar:

```json
{
  "predicate_id": "block",
  "agent": "fighter_b",
  "patient": "fighter_a.right_fist",
  "agent_body_parts": ["left_forearm"],
  "t_start_s": 0.42,
  "t_end_s": 0.51,
  "phase_links": ["defense_01.stroke"],
  "contact_ids": ["contact_44"],
  "preconditions": ["fist_on_collision_course"],
  "effects": ["incoming_path_redirected", "head_contact_prevented"],
  "confidence": 0.91
}
```

`phase_links` is the bridge between interaction and phase timing: a
predicate interval is associated with a specific phase (here `stroke`) of
the seven-phase grammar (`cpcs.motion.phase.timing_presets`).

### Contact topology modes

The contact edge stores interval, body/object parts, point or surface patch,
normal and tangent basis, **mode**, relative velocity, force if known,
friction, compliance, and confidence. Modes: `stick · slide · roll · impact
· separate`. Worked values from `ex_cross_punch_01`: `int_block` duration
0.12 s, compliance 0.25, resistance 0.82.

Core invariants (KB, compatible with the rules above):

- stick → near-zero tangential relative velocity within tolerance;
- support → load-bearing/stability contribution;
- grasp → constrains the intended degrees of freedom;
- release closes the active constraint before free flight;
- no mesh penetration beyond configured tolerance;
- a reaction cannot causally precede contact unless it is
  anticipation/evasion.

### Two-person sync patterns

- **Combat exchange:** `attack → defense/interception → counter →
  reaction/recovery`. Actions overlap; the counter may prepare during the
  attacker's overshoot, but its causal effects cannot precede the defense.
- **Handoff:** `giver support/grasp → shared grasp → receiver support/grasp
  → giver release` — no unsupported interval unless dropping is intended.
- **Dance partnering:** shared support, counterbalance, lead/follow —
  silhouettes can look plausible while violating the shared-force relation,
  so contact validation remains necessary.
- **Conversation:** proxemics, gaze, turn-taking, gesture holds, mirroring.

### Timing metrics (KB evaluation, compatible with the combat metrics layer)

Contact precision/recall, contact-time onset error, drift, penetration, and
reaction-order violations. Hard checks: reaction onset ≥ contact; target
response begins at or after contact. These complement the SRC-010 tolerances
(contact time error ≤ 50 ms, contact distance ≤ 0.05 m).

## Verification

`test_predicate_preconditions_effects_declared`,
`test_contact_mode_declared_stick_slide_roll_impact_separate`,
`test_reaction_order_causality_enforced`,
`test_handoff_no_unsupported_interval`.
