import json
from pathlib import Path

import pytest

from dmr_runtime.capabilities import load_contract
from dmr_runtime.compiler import CompilationError, CompileOptions, compile_scene
from dmr_runtime.models import ControlRequest, ScenePlan


ROOT = Path(__file__).parents[1]


def load_scene() -> ScenePlan:
    return ScenePlan.model_validate(json.loads((ROOT / "examples/blocked_turning_kick.scene.json").read_text()))


def test_compiler_accounts_for_every_requested_control():
    scene = load_scene()
    contract = load_contract(ROOT / "contracts/veo-3.1-generate-001.vertex.json")
    result = compile_scene(scene, contract)
    assert not result.hard_failure
    assert len(result.loss_report) == len(scene.control_requests)
    assert {x.control_id for x in result.loss_report} == {x.control_id for x in scene.control_requests}
    assert result.provider_request["parameters"]["durationSeconds"] == 8
    assert result.provider_request["parameters"]["aspectRatio"] == "16:9"
    assert result.provider_request["instances"][0]["image"]["mimeType"] == "image/png"
    assert result.provider_request["instances"][0]["prompt"] == result.prompt
    assert "a.turning_kick" not in result.prompt  # prompt uses readable action text, not IDs
    assert "executes a right turning kick" in result.prompt


def test_required_unsupported_control_fails_closed():
    scene = load_scene()
    scene.control_requests.append(ControlRequest(
        control_id="ctrl.required_joint_track",
        canonical_path="motion.joint_tracks",
        value={"right_ankle": [[0.0, 0.0, 0.0]]},
        required=True,
    ))
    contract = load_contract(ROOT / "contracts/veo-3.1-generate-001.vertex.json")
    with pytest.raises(CompilationError, match="failed closed"):
        compile_scene(scene, contract)


def test_required_loss_can_be_rendered_for_inspection_without_hiding_failure():
    scene = load_scene()
    scene.control_requests.append(ControlRequest(
        control_id="ctrl.required_joint_track",
        canonical_path="motion.joint_tracks",
        value={"right_ankle": [[0.0, 0.0, 0.0]]},
        required=True,
    ))
    contract = load_contract(ROOT / "contracts/veo-3.1-generate-001.vertex.json")
    result = compile_scene(scene, contract, options=CompileOptions(allow_required_loss=True))
    assert result.hard_failure
    item = next(x for x in result.loss_report if x.control_id == "ctrl.required_joint_track")
    assert item.classification.value == "unsupported"


def test_required_value_outside_contract_limits_fails_closed():
    scene = load_scene()
    duration = next(c for c in scene.control_requests if c.control_id == "ctrl.duration")
    duration.value = 7
    contract = load_contract(ROOT / "contracts/veo-3.1-generate-001.vertex.json")
    with pytest.raises(CompilationError, match="outside contract limits"):
        compile_scene(scene, contract)


def test_limit_failure_is_explicit_in_diagnostic_result():
    scene = load_scene()
    duration = next(c for c in scene.control_requests if c.control_id == "ctrl.duration")
    duration.value = 7
    contract = load_contract(ROOT / "contracts/veo-3.1-generate-001.vertex.json")
    result = compile_scene(scene, contract, options=CompileOptions(allow_required_loss=True))
    item = next(x for x in result.loss_report if x.control_id == "ctrl.duration")
    assert result.hard_failure
    assert item.classification.value == "unsupported"
    assert "allowed values" in (item.residual_risk or "")
    assert "durationSeconds" not in result.provider_request.get("parameters", {})


def test_product_profile_is_not_executable():
    scene = load_scene()
    profile = load_contract(ROOT / "contracts/kling-video-3.0-omni.product.json")
    with pytest.raises(CompilationError, match="product profile"):
        compile_scene(scene, profile)
