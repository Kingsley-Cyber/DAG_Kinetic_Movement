#!/usr/bin/env python3
"""Deterministic, offline demonstration compiler from a canonical CPCS example to an adapter plan.

This does not call a vendor API. It creates a capability-aware compilation report and request draft.
"""
from __future__ import annotations
import argparse, hashlib, json, pathlib
from typing import Any


def load(path): return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))

def compact_prompt(scene: dict, adapter: dict) -> str:
    intent = scene.get("intent", {}).get("primary", "perform the described action")
    beats = "; ".join(b.get("label", b.get("id", "beat")) for b in scene.get("beats", []))
    motion = []
    for p in scene.get("motion_primitives", []):
        lab = p.get("laban", {})
        motion.append(f"{p.get('name')}: {lab.get('effort', {})}, shape {lab.get('shape', {})}")
    camera = []
    for c in scene.get("camera_tracks", []):
        camera.append(f"{c.get('shot_size','shot')} at {c.get('focal_length_equiv_mm','?')}mm; " + ", ".join(m.get("type", "move") for m in c.get("motion_primitives", [])))
    return (f"Intent: {intent}. Beat order: {beats}. Motion: {' | '.join(motion)}. "
            f"Camera: {' | '.join(camera)}. Preserve actor identity, contact causality, support contacts, "
            "screen direction, and the final settle. Do not add unrequested actions.")

def set_template_value(value: Any, variables: dict[str, Any]):
    if isinstance(value, str):
        if value.startswith("${") and value.endswith("}"):
            return variables.get(value[2:-1], None)
        out=value
        for k,v in variables.items(): out=out.replace("${"+k+"}", str(v))
        return out
    if isinstance(value, dict): return {k:set_template_value(v,variables) for k,v in value.items()}
    if isinstance(value, list): return [set_template_value(v,variables) for v in value]
    return value

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("example", type=pathlib.Path, help="Example directory or canonical.json")
    ap.add_argument("adapter", type=pathlib.Path, help="Adapter JSON")
    ap.add_argument("--output", type=pathlib.Path)
    a=ap.parse_args()
    scene_path=a.example/"canonical.json" if a.example.is_dir() else a.example
    scene=load(scene_path); adapter=load(a.adapter)
    prompt=compact_prompt(scene,adapter)
    variables={
      "prompt":prompt,"duration":scene.get("duration_s"),"aspect":"16:9","aspect_ratio":"16:9",
      "model_id":adapter.get("model_id"),"live_model_id":adapter.get("model_id"),"surface":adapter.get("surface"),
      "native_config":{"duration":scene.get("duration_s"),"fps":scene.get("fps")},"shot_plan":scene.get("beats"),
      "shot_plan_optional":scene.get("beats"),"elements":None,"elements_optional":None,"audio_options":None,
      "audio_options_optional":None,"input_image":None,"start_image_optional":None,"reference_images_optional":None,
      "video":None,"source_video":None,"faces":"default","setting":"default","poses_or_blocking":"Poses",
      "0_to_9_or_off":5,"image_or_video":None,"image_mode_or_video_mode":"image","resolution":"1280x720",
      "driving_performance":None,"character":None,"optional":None
    }
    draft=set_template_value(adapter.get("request_template",{}),variables)
    scene_hash=hashlib.sha256(scene_path.read_bytes()).hexdigest()
    preserved=["intent","beat_order","actor_roles","duration"]
    if adapter.get("reference_capabilities"): preserved.append("reference-conditioned channels when supplied")
    lossy=sorted(set(adapter.get("prompt_only",[])+adapter.get("unsupported",[])))
    out={
      "compiler":"cpcs_offline_demo/1.0.0","scene_id":scene.get("scene_id"),"scene_sha256":scene_hash,
      "adapter_id":adapter.get("adapter_id"),"adapter_verified_at":adapter.get("verified_at"),
      "status":adapter.get("status"),"compiled_prompt":prompt,"request_draft":draft,
      "preserved_or_native":preserved,"lossy_or_prompt_only":lossy,
      "loss_risk":adapter.get("loss_risk",{}),
      "verification_required":adapter.get("validation_rules",[]),
      "not_executed":True
    }
    text=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
    if a.output: a.output.write_text(text,encoding="utf-8")
    else: print(text,end="")
if __name__=="__main__": main()
