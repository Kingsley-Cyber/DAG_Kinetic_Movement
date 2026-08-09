import json
from pathlib import Path

from dmr_runtime.models import Action, ScenePlan, Severity, TemporalConstraint
from dmr_runtime.temporal import STNSolver
from dmr_runtime.validation import validate_scene


ROOT = Path(__file__).parents[1]


def load_scene() -> ScenePlan:
    return ScenePlan.model_validate(json.loads((ROOT / "examples/blocked_turning_kick.scene.json").read_text()))


def test_valid_example_has_no_error_severity():
    scene = load_scene()
    solution = STNSolver(scene.temporal_constraints, origin=scene.origin_point).solve()
    issues = validate_scene(scene, solution)
    assert not [i for i in issues if i.severity == Severity.ERROR]


def test_overlapping_same_effector_is_detected():
    scene = load_scene()
    duplicate = scene.actions[2].model_copy(update={
        "action_id": "a.second_right_leg_action",
        "verb": "simultaneously extends the same right leg",
    }, deep=True)
    scene.actions.append(duplicate)
    solution = STNSolver(scene.temporal_constraints, origin=scene.origin_point).solve()
    issues = validate_scene(scene, solution)
    assert any(i.code == "RESOURCE_LOCK_CONFLICT" for i in issues)


def test_reaction_before_contact_is_detected():
    scene = load_scene()
    scene.temporal_constraints = [
        c for c in scene.temporal_constraints
        if c.constraint_id not in {"t.reaction.start", "t.reaction.after_contact"}
    ]
    scene.temporal_constraints.append(TemporalConstraint(
        constraint_id="t.reaction.too_early",
        left_point="scene:start",
        right_point="b.reaction:start",
        min_delta_s=1.9,
        max_delta_s=1.9,
    ))
    solution = STNSolver(scene.temporal_constraints, origin=scene.origin_point).solve()
    issues = validate_scene(scene, solution)
    assert any(i.code == "REACTION_BEFORE_CONTACT" for i in issues)
