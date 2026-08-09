from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from .models import ScenePlan, Severity, StateCondition, ValidationIssue
from .temporal import TemporalSolution


@dataclass
class RuntimeActorState:
    support: set[str]
    held: dict[str, str]
    screen_side: str
    grounded: bool = True


def _interval(action, schedule: dict[str, float]) -> tuple[float, float] | None:
    if action.start_point not in schedule or action.end_point not in schedule:
        return None
    return schedule[action.start_point], schedule[action.end_point]


def _overlap(a: tuple[float, float], b: tuple[float, float]) -> bool:
    return max(a[0], b[0]) < min(a[1], b[1]) - 1e-9


def validate_scene(scene: ScenePlan, temporal: TemporalSolution) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not temporal.consistent:
        conflict = temporal.conflict
        issues.append(ValidationIssue(
            issue_id="temporal.inconsistent",
            severity=Severity.ERROR,
            code="TEMPORAL_NEGATIVE_CYCLE",
            message=conflict.message if conflict else "Temporal network is inconsistent",
            responsible_paths=[f"temporal_constraints:{x}" for x in (conflict.constraint_ids if conflict else [])],
            earliest_causal_layer="temporal_graph",
            suggested_patch={"operation": "review_or_relax_conflicting_constraints"},
        ))
        return issues

    for point in temporal.underconstrained_points:
        issues.append(ValidationIssue(
            issue_id=f"temporal.underconstrained.{point}",
            severity=Severity.WARNING,
            code="TEMPORAL_UNDERCONSTRAINED",
            message=f"Time point {point!r} has no finite two-sided bound relative to the scene origin",
            responsible_paths=[point],
            earliest_causal_layer="temporal_graph",
            suggested_patch={"operation": "add_bound_to_origin_or_neighbor", "point": point},
        ))

    schedule = temporal.schedule_s
    actor_ids = {a.actor_id for a in scene.actors}
    action_by_id = {a.action_id: a for a in scene.actions}
    contact_by_id = {c.contact_id: c for c in scene.contacts}

    # Basic interval validity and scene bounds.
    for action in scene.actions:
        iv = _interval(action, schedule)
        if iv is None:
            issues.append(ValidationIssue(
                issue_id=f"action.unscheduled.{action.action_id}", severity=Severity.ERROR,
                code="ACTION_UNSCHEDULED", message=f"Action {action.action_id} has unresolved endpoints",
                responsible_paths=[action.start_point, action.end_point], earliest_causal_layer="temporal_graph"))
            continue
        if iv[1] < iv[0] - 1e-9:
            issues.append(ValidationIssue(
                issue_id=f"action.negative.{action.action_id}", severity=Severity.ERROR,
                code="ACTION_NEGATIVE_DURATION", message=f"Action {action.action_id} ends before it starts",
                responsible_paths=[action.start_point, action.end_point], earliest_causal_layer="temporal_graph"))
        if iv[0] < -1e-9 or iv[1] > scene.duration_s + 1e-9:
            issues.append(ValidationIssue(
                issue_id=f"action.outside_scene.{action.action_id}", severity=Severity.ERROR,
                code="ACTION_OUTSIDE_SCENE", message=f"Action {action.action_id} lies outside scene bounds",
                responsible_paths=[action.start_point, action.end_point], earliest_causal_layer="temporal_graph"))

    # Mutually exclusive body/effector resources.
    by_actor_resource: dict[tuple[str, str], list] = defaultdict(list)
    for action in scene.actions:
        for resource in action.resource_locks:
            by_actor_resource[(action.actor_id, resource)].append(action)
    for (actor_id, resource), actions in by_actor_resource.items():
        for i, a in enumerate(actions):
            ai = _interval(a, schedule)
            if ai is None:
                continue
            for b in actions[i + 1:]:
                bi = _interval(b, schedule)
                if bi and _overlap(ai, bi):
                    issues.append(ValidationIssue(
                        issue_id=f"resource.{actor_id}.{resource}.{a.action_id}.{b.action_id}",
                        severity=Severity.ERROR,
                        code="RESOURCE_LOCK_CONFLICT",
                        message=f"{actor_id} uses {resource} in overlapping actions {a.action_id} and {b.action_id}",
                        responsible_paths=[f"actions:{a.action_id}", f"actions:{b.action_id}"],
                        earliest_causal_layer="action_state",
                        suggested_patch={"operation": "serialize_or_change_effector", "resource": resource},
                    ))

    # Contact/reaction/recovery ordering.
    for action in scene.actions:
        iv = _interval(action, schedule)
        if iv is None:
            continue
        if action.reacts_to_contact_id:
            contact = contact_by_id[action.reacts_to_contact_id]
            c_start = schedule.get(contact.start_point)
            if c_start is None or iv[0] < c_start - 1e-9:
                issues.append(ValidationIssue(
                    issue_id=f"reaction.premature.{action.action_id}", severity=Severity.ERROR,
                    code="REACTION_BEFORE_CONTACT",
                    message=f"Reaction {action.action_id} begins before contact {contact.contact_id}",
                    responsible_paths=[f"actions:{action.action_id}", f"contacts:{contact.contact_id}"],
                    earliest_causal_layer="temporal_graph",
                    suggested_patch={"operation": "constrain_reaction_after_contact", "contact_id": contact.contact_id},
                ))
        if action.recovers_from_action_id:
            source = action_by_id[action.recovers_from_action_id]
            src_iv = _interval(source, schedule)
            if src_iv and iv[0] < src_iv[1] - 1e-9:
                issues.append(ValidationIssue(
                    issue_id=f"recovery.premature.{action.action_id}", severity=Severity.ERROR,
                    code="RECOVERY_BEFORE_ACTION_END",
                    message=f"Recovery {action.action_id} begins before {source.action_id} completes",
                    responsible_paths=[f"actions:{action.action_id}", f"actions:{source.action_id}"],
                    earliest_causal_layer="temporal_graph",
                    suggested_patch={"operation": "constrain_recovery_after_source_end"},
                ))

    # Deterministic state-machine simulation at action start/end boundaries.
    states = {
        actor.actor_id: RuntimeActorState(
            support=set(actor.initial_support_effectors),
            held=dict(actor.initial_held_objects),
            screen_side=actor.initial_screen_side,
        )
        for actor in scene.actors
    }
    timeline = []
    for action in scene.actions:
        iv = _interval(action, schedule)
        if iv:
            timeline.append((iv[0], 1, "start", action))
            timeline.append((iv[1], 0, "end", action))  # end effects before same-time starts
    timeline.sort(key=lambda x: (x[0], x[1], x[3].action_id))
    for _, _, kind, action in timeline:
        if action.actor_id not in actor_ids:
            continue
        state = states[action.actor_id]
        if kind == "start":
            for condition in action.preconditions:
                if not _condition_holds(condition, state):
                    issues.append(ValidationIssue(
                        issue_id=f"precondition.{action.action_id}.{condition.kind}.{condition.key}",
                        severity=Severity.ERROR,
                        code="ACTION_PRECONDITION_FAILED",
                        message=f"Precondition {condition.kind} failed for action {action.action_id}",
                        responsible_paths=[f"actions:{action.action_id}.preconditions"],
                        earliest_causal_layer="action_state",
                        suggested_patch={"operation": "insert_state_transition_or_change_action", "condition": condition.model_dump()},
                    ))
        else:
            for effect in action.effects:
                if effect.actor_id != action.actor_id:
                    issues.append(ValidationIssue(
                        issue_id=f"effect.cross_actor.{action.action_id}", severity=Severity.WARNING,
                        code="CROSS_ACTOR_EFFECT", message="Cross-actor effects require an explicit interaction protocol",
                        responsible_paths=[f"actions:{action.action_id}.effects"], earliest_causal_layer="action_state"))
                    continue
                if effect.kind == "add_support" and effect.key:
                    state.support.add(effect.key)
                elif effect.kind == "remove_support" and effect.key:
                    state.support.discard(effect.key)
                elif effect.kind == "acquire_object" and effect.key and isinstance(effect.value, str):
                    state.held[effect.key] = effect.value
                elif effect.kind == "release_object" and effect.key:
                    state.held.pop(effect.key, None)
                elif effect.kind == "set_screen_side" and isinstance(effect.value, str):
                    state.screen_side = effect.value
                elif effect.kind == "set_grounded":
                    state.grounded = True
                elif effect.kind == "set_airborne":
                    state.grounded = False

    for contact in scene.contacts:
        start = schedule.get(contact.start_point)
        end = schedule.get(contact.end_point)
        if start is None or end is None:
            issues.append(ValidationIssue(
                issue_id=f"contact.unscheduled.{contact.contact_id}", severity=Severity.ERROR,
                code="CONTACT_UNSCHEDULED", message=f"Contact {contact.contact_id} has unresolved endpoints",
                responsible_paths=[contact.start_point, contact.end_point], earliest_causal_layer="temporal_graph"))
        elif end < start - 1e-9:
            issues.append(ValidationIssue(
                issue_id=f"contact.negative.{contact.contact_id}", severity=Severity.ERROR,
                code="CONTACT_NEGATIVE_DURATION", message=f"Contact {contact.contact_id} ends before it starts",
                responsible_paths=[contact.start_point, contact.end_point], earliest_causal_layer="temporal_graph"))
        if contact.minimum_distance_m is None and contact.contact_type.value in {"impact", "touch", "grasp", "support"}:
            issues.append(ValidationIssue(
                issue_id=f"contact.unverified_distance.{contact.contact_id}", severity=Severity.UNKNOWN,
                code="CONTACT_GEOMETRY_UNKNOWN",
                message=f"Contact {contact.contact_id} has no geometric minimum-distance evidence",
                responsible_paths=[f"contacts:{contact.contact_id}.minimum_distance_m"],
                earliest_causal_layer="contact_geometry",
                suggested_patch={"operation": "measure_or_mark_cinematic_cheat"},
            ))

    return issues


def _condition_holds(condition: StateCondition, state: RuntimeActorState) -> bool:
    if condition.kind == "support_present":
        return bool(condition.key and condition.key in state.support)
    if condition.kind == "support_absent":
        return bool(condition.key and condition.key not in state.support)
    if condition.kind == "object_held":
        return bool(condition.key and state.held.get(condition.key) == condition.value)
    if condition.kind == "object_not_held":
        return bool(condition.key and condition.key not in state.held)
    if condition.kind == "screen_side":
        return state.screen_side == condition.value
    if condition.kind == "grounded":
        return state.grounded
    if condition.kind == "airborne":
        return not state.grounded
    if condition.kind == "region_free":
        # Region occupancy is enforced by resource locks; no stateful occupancy is retained here.
        return True
    return False
