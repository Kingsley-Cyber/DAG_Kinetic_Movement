from __future__ import annotations

import csv
import hashlib
import json
import shutil
import textwrap
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ACCESS_DATE = "2026-08-05"
REPO = "Kingsley-Cyber/ai-video-movement-prompt-system"
REPO_SHA = "eb0fc359de4bb61075db49ca0dad08d4d6ed5114"
ROOT = Path("/mnt/data/CPCS_Failure_Aware_Video_Research_Package_v1.0")
ZIP_PATH = Path("/mnt/data/CPCS_Failure_Aware_Video_Research_Package_v1.0.zip")
SRC_BRIEF = Path("/mnt/data/Pasted markdown(7).md")

if ROOT.exists():
    shutil.rmtree(ROOT)
ROOT.mkdir(parents=True)
(ROOT / "experiments").mkdir()
(ROOT / "schemas").mkdir()
(ROOT / "scripts").mkdir()


def write_text(rel: str, text: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(rel: str, obj: Any) -> None:
    write_text(rel, json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=False))


def write_csv(rel: str, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            normalized = {}
            for k in fieldnames:
                v = row.get(k, "")
                if isinstance(v, (list, dict)):
                    v = json.dumps(v, ensure_ascii=False, separators=(",", ":"))
                normalized[k] = v
            w.writerow(normalized)


def source(
    sid: str,
    title: str,
    publisher: str,
    year: str,
    source_type: str,
    evidence_class: str,
    url: str,
    scope: str,
    limitations: str,
) -> dict[str, str]:
    return {
        "source_id": sid,
        "title": title,
        "publisher_or_authors": publisher,
        "year_or_date": year,
        "source_type": source_type,
        "evidence_class": evidence_class,
        "url": url,
        "accessed": ACCESS_DATE,
        "scope_or_key_finding": scope,
        "limitations": limitations,
    }


SOURCES: list[dict[str, str]] = [
    source("R001", "Repository governance", REPO, REPO_SHA, "repository_file", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/AGENTS.md", "Defines repository-wide authority and no-parallel-kernel constraints.", "Repository policy, not empirical model evidence."),
    source("R002", "CPCS architecture", REPO, REPO_SHA, "repository_file", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/ARCHITECTURE.md", "Defines one provider-neutral score and compile-render-verify-repair loop.", "Architecture may exceed currently qualified runtime behavior."),
    source("R003", "Lab governance", REPO, REPO_SHA, "repository_file", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/AGENTS.md", "Requires controlled A/B experiments and exact authority boundaries.", "Policy only."),
    source("R004", "CPCS control surface", REPO, REPO_SHA, "repository_file", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/CONTROL_SURFACE.md", "Maps authored prose, canonical controls, and known unexplored areas.", "Several statements are research hypotheses pending verification."),
    source("R005", "CPCS format control map", REPO, REPO_SHA, "repository_file", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/FORMAT_CONTROL_MAP.md", "Defines YAML authoring, JSON canonical authority, XML event envelopes, JSONL evidence, and media controls.", "Does not prove provider-side structured-format superiority."),
    source("R006", "Universal score schema 1.0", REPO, REPO_SHA, "repository_schema", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/compiler/schemas/universal_score.schema.json", "Existing owners include entities, scenes, shots, beats, actions, interactions, camera, editing, audio, continuity, constraints, provider realization, verification requirements, and loss surfaces.", "Many high-level objects are open objects and need typed minimal extensions."),
    source("R007", "Provider capability schema 1.0", REPO, REPO_SHA, "repository_schema", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/compiler/schemas/provider_capability.schema.json", "Current schema is hard-coded to Google Vertex AI Veo 3.1 and its current adapter assumptions.", "Not yet a universal multi-provider capability contract."),
    source("R008", "Verification plan schema 1.0", REPO, REPO_SHA, "repository_schema", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/compiler/schemas/verification_plan.schema.json", "Supports direct, semantic, measured, and human-review observability plus provider artifact checks.", "Current artifact checks are basic media properties; failure-specific metrics require extension."),
    source("R009", "Compliance report schema 1.0", REPO, REPO_SHA, "repository_schema", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/verification/schemas/compliance_report.schema.json", "Already supports evidence traces, conflicts, interval-scoped failures, and bounded repair actions that reassert canonical controls.", "Does not yet define the failure taxonomy or metric catalog in this package."),
    source("R010", "Second-brain governance", REPO, REPO_SHA, "repository_file", "controlled_repository_observation", f"https://github.com/{REPO}/blob/{REPO_SHA}/lab/second_brain/AGENTS.md", "Separates frozen research, curated knowledge, immutable evidence, and rebuildable derived state.", "Research proposals cannot promote themselves into production authority."),

    source("M001", "Generate videos with Veo using first and last frames", "Google Cloud", "updated 2026-01-02", "official_documentation", "officially_documented_capability", "https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos-from-first-and-last-frames", "Veo 3.1 supports first/last frame conditioning, 4/6/8-second outputs, 720p/1080p, optional negative prompt, and seed in the documented endpoint.", "Capability documentation does not establish adherence reliability."),
    source("M002", "Runway API reference", "Runway", "accessed 2026-08-05", "official_documentation", "officially_documented_capability", "https://docs.dev.runwayml.com/api/", "Documents text-, image-, and video-conditioned endpoints, model identifiers, prompt strings, ratios, durations, seeds, and reference assets.", "Runway can expose third-party models; adapter behavior may differ from original providers."),
    source("M003", "Runway API changelog", "Runway", "through 2026-07-10", "official_documentation", "officially_documented_capability", "https://docs.dev.runwayml.com/api-details/api_changelog/", "Version-scopes Gen-4.5, Seedance 2.0, Veo 3.1, Aleph 2.0, and related API controls.", "Changelog is interface evidence, not quality evidence."),
    source("M004", "Seedance 2.0 official launch", "ByteDance Seed", "2026-02-12", "official_model_announcement", "officially_documented_capability", "https://seed.bytedance.com/blog/seedance-2-0-official-launch", "Documents unified text/image/audio/video inputs, up to 9 images, 3 videos, 3 audio clips, and up to 15-second multi-shot audio-video output.", "Internal benchmark and marketing claims are not independent reliability evidence."),
    source("M005", "Kling VIDEO 3.0 model user guide", "Kling AI", "2026-02-06", "official_documentation", "officially_documented_capability", "https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide", "Documents T2V, I2V, first/last frames, native audio, multi-shot, element references, and flexible 3-15 second generation.", "Official guide contains promotional quality statements; only interface claims are used as capability evidence."),
    source("M006", "MiniMax API release notes", "MiniMax", "2025-10-28", "official_documentation", "officially_documented_capability", "https://platform.minimax.io/docs/release-notes/apis", "Hailuo-2.3 supports T2V and I2V; Hailuo-2.3-Fast supports I2V; documented 768p 6/10s and 1080p 6s outputs.", "No independent failure-rate evidence."),
    source("M007", "MiniMax text-to-video API", "MiniMax", "accessed 2026-08-05", "official_documentation", "officially_documented_capability", "https://platform.minimax.io/docs/api-reference/video-generation-t2v", "Prompt is a text string up to 2000 characters; documented bracketed camera commands provide a provider-specific syntax.", "Camera command support does not guarantee exact choreography."),
    source("M008", "LTX-Video/LTX-2 official repository", "Lightricks", "current through 2026", "official_model_repository", "officially_documented_capability", "https://github.com/Lightricks/LTX-Video", "Documents synchronized audio-video, multiple keyframes, video extension, video-to-video, control models, and up to 10-second LTX-2 outputs.", "Repository claims and demos are not independent reliability measurements."),
    source("M009", "Wan2.2 official repository", "Wan-Video", "2025-07-28 onward", "official_model_repository", "officially_documented_capability", "https://github.com/Wan-Video/Wan2.2", "Documents T2V, I2V, unified TI2V, speech-to-video, pose-video control, character animation/replacement, 480p/720p workflows, and seeds through local inference.", "Open-model performance depends on checkpoint, sampler, hardware, and configuration."),
    source("M010", "HunyuanVideo-1.5 official repository", "Tencent Hunyuan", "2025-11-20 onward", "official_model_repository", "officially_documented_capability", "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5", "Documents 8.3B T2V/I2V models, 480p/720p generation, super-resolution, prompt rewriting, seed control, and compressed spatiotemporal latent architecture.", "Official evaluation is model-authored and not a substitute for CPCS qualification."),
    source("M011", "CogVideo/CogVideoX official repository", "Z.ai/THUDM", "current through 2025", "official_model_repository", "officially_documented_capability", "https://github.com/zai-org/CogVideo", "Documents CogVideoX1.5 T2V/I2V, 10-second generation, resolutions, frames, and local seed-based inference.", "Current commercial QingYing behavior is outside the open repository scope."),
    source("M012", "Mochi 1 official repository", "Genmo", "2024 onward", "official_model_repository", "officially_documented_capability", "https://github.com/genmoai/mochi", "Documents a 10B AsymmDiT and a 128x-compressed causal video latent representation for open T2V generation.", "Repository preview does not document all hosted product controls or current service limits."),
    source("M013", "Veo 3.1 model documentation", "Google Cloud", "updated through 2026", "official_documentation", "officially_documented_capability", "https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate", "Documents Veo 3.1 model IDs, modes, resolutions, durations, and endpoint-specific capability differences.", "Google pages expose conflicting or endpoint-specific sound/reference statements; package marks audio capability as requiring endpoint verification."),

    source("B001", "VBench/VBench++/VBench-2.0", "Vchitect and collaborators", "CVPR 2024; later extensions", "official_benchmark_repository", "benchmark_result", "https://github.com/Vchitect/VBench", "Fine-grained evaluation dimensions include subject/background consistency, temporal flicker, motion smoothness, multiple objects, spatial relations, and semantics; human-alignment annotations are provided.", "Aggregate metrics can hide localized failures and inherit evaluator biases."),
    source("B002", "T2V-CompBench", "Sun et al.", "CVPR 2025", "official_benchmark_repository", "benchmark_result", "https://github.com/KaiyueSun98/T2V-CompBench", "Benchmarks attribute binding, spatial relationships, motion/action binding, object interactions, and generative numeracy; reports compositional generation remains highly challenging.", "Primarily T2V and benchmark-prompt scoped; commercial model versions age quickly."),
    source("B003", "TC-Bench", "Feng et al.", "Findings of ACL 2025", "peer_reviewed_paper", "benchmark_result", "https://aclanthology.org/2025.findings-acl.241/", "Evaluates temporal compositionality using explicit initial/final states and transition completeness; metrics correlate more strongly with humans than prior metrics in the study.", "Does not directly isolate every production failure type."),
    source("B004", "VideoPhy-2", "Bansal et al.; Google Research/UCLA", "ICLR 2026", "peer_reviewed_benchmark", "benchmark_result", "https://research.google/pubs/videophy-2-a-challenging-action-centric-physical-commonsense-evaluation-in-video-generation/", "On the hard subset, the best evaluated model achieved 22% joint semantic-and-physical adherence; conservation of mass and momentum were particularly difficult.", "Results apply to evaluated versions and prompts, not every current provider release."),
    source("B005", "PhyGenBench", "Meng et al.", "ICML 2025", "official_benchmark_repository", "benchmark_result", "https://github.com/OpenGVLab/PhyGenBench", "160 prompts cover 27 physical laws; authors report current models struggle and prompt engineering alone is insufficient for dynamic physical phenomena.", "Automated hierarchical evaluation still needs human calibration."),
    source("B006", "WorldModelBench", "Li et al.", "CVPR 2025 workshop oral", "official_benchmark_repository", "benchmark_result", "https://github.com/WorldModelBench-Team/WorldModelBench", "Evaluates instruction following, common sense, and physical adherence over 350 prompts and seven application domains with a human-aligned VLM judge.", "Judge-based results inherit the judge's model and training distribution."),
    source("B007", "Physics-IQ Verified", "Rädsch et al.", "2026", "research_paper", "benchmark_audit", "https://arxiv.org/abs/2606.18943", "Audits Physics-IQ, revises prompts/ground truth, and reports meaningful ranking changes, demonstrating benchmark construction can materially alter conclusions.", "Recent preprint; not yet peer reviewed at access date."),
    source("B008", "VideoScore", "He et al.", "EMNLP 2024", "official_metric_repository", "benchmark_result", "https://github.com/TIGER-AI-Lab/VideoScore", "Uses 37.6K human-scored generated videos; reports strong but imperfect human correlation, supporting learned evaluators as proxies rather than authorities.", "Domain shift, fast events, and unseen artifact classes remain risks."),
    source("B009", "EvalCrafter", "Liu et al.", "CVPR 2024", "official_benchmark_repository", "benchmark_result", "https://github.com/evalcrafter/EvalCrafter", "Combines 17 objective metrics and human feedback across visual, content, motion, temporal consistency, and alignment dimensions.", "Multiple metrics do not eliminate correlated evaluator failure."),
    source("B010", "ChronoMagic-Bench", "Yuan et al.", "NeurIPS 2024", "official_benchmark_repository", "benchmark_result", "https://github.com/PKU-YuanGroup/ChronoMagic-Bench", "Evaluates metamorphic progression and temporal coherence over long visual transformations.", "Time-lapse focus does not directly cover all interaction/contact failures."),
    source("B011", "WorldBench: How Close are World Models to the Physical World?", "Upadhyay et al.", "2025", "benchmark_project", "benchmark_result", "https://world-bench.github.io/", "Reports degradation with prediction horizon and identifies object permanence as the hardest scenario in its benchmark.", "Synthetic/controlled benchmark; title-level results should not be generalized to every commercial model."),
    source("B012", "Temporally Consistent Transformers for Video Generation", "Yan et al.", "ICML 2023", "peer_reviewed_paper", "experimental_result", "https://proceedings.mlr.press/v202/yan23b.html", "Documents that models can invent different content when a scene leaves view and is revisited; introduces long-range consistency datasets and TECO.", "Video prediction setting differs from prompt-only commercial generation but exposes the same hidden-state problem."),
    source("B013", "Tracking through Containers and Occluders in the Wild", "Van Hoorick et al.", "CVPR 2023", "peer_reviewed_paper", "benchmark_result", "https://tcow.cs.columbia.edu/", "Defines object-permanence tracking under heavy occlusion/containment and finds a substantial remaining performance gap.", "Perception benchmark, not a generator benchmark; used to design verification and visibility bridges."),
    source("B014", "MemoBench", "Chen et al.", "2026", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2606.27537", "Tests disappear-and-reappear memory while hidden objects continue changing state.", "Recent preprint; version and leaderboard may change."),
    source("B015", "EntityBench", "He et al.", "2026", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2605.15199", "Tracks characters, objects, and locations across up to 50 shots; reports consistency degradation with recurrence distance and benefit from explicit entity memory.", "Recent preprint; multi-shot systems and metrics may evolve."),
    source("B016", "GeCo", "Gu et al.", "2025", "research_preprint", "benchmark_and_metric", "https://arxiv.org/abs/2512.22274", "Introduces dense geometry-grounded maps for deformation and occlusion inconsistency and uses them as a training-free guidance signal.", "Static-scene emphasis and learned depth/motion priors limit universal coverage."),
    source("B017", "TOC-Bench", "Chen et al.", "2026", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2605.09904", "Shows video-LLMs remain weak on object identity, state, event ordering, and hallucination-aware verification across occlusion and reappearance.", "Evaluates video understanding, not generation; directly informs evaluator-risk controls."),
    source("B018", "SAM 2", "Meta FAIR", "2024", "official_model_publication", "measurement_tool", "https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/", "Promptable video segmentation with streaming memory; suitable for masks, counts, and continuity traces.", "Segmentation errors under blur, reflections, occlusion, small subjects, and stylized content must be calibrated."),
    source("B019", "CoTracker3", "Karaev et al.", "2024", "official_project", "measurement_tool", "https://cotracker3.github.io/", "Tracks visible and occluded points and supports long trajectories.", "Tracking can swap identities or lose points in severe occlusion, cuts, deformation, and out-of-distribution imagery."),
    source("B020", "TAPIR", "Doersch et al.", "ICCV 2023", "official_publication", "measurement_tool", "https://deepmind.google/research/publications/26336/", "Tracks arbitrary points with per-frame matching and temporal refinement.", "Point tracking is not semantic identity proof and can fail on textureless/blurred/occluded surfaces."),
    source("B021", "RAFT", "Teed and Deng", "ECCV 2020", "official_repository", "measurement_tool", "https://github.com/princeton-vl/RAFT", "Dense optical flow supports foot slip, motion continuity, and camera/actor decomposition diagnostics.", "Known difficult cases include fast motion, occlusion, motion blur, and textureless regions."),
    source("B022", "AV-SyncBench", "Zhou et al.", "2026", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2607.00726", "Separates temporal from semantic audio-visual synchronization across voice, music, and sound events.", "Very recent preprint; model rankings and code may change."),
    source("B023", "VABench", "Hua et al.", "2025", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2512.09299", "Evaluates text-video, text-audio, video-audio, synchronization, lip-speech consistency, and audio/video QA for joint generation.", "Preprint and benchmark design require independent reproduction."),
    source("B024", "AV-HuBERT", "Shi et al.", "ICLR 2022", "official_repository", "measurement_tool", "https://github.com/facebookresearch/av_hubert", "Provides audio-visual speech representations useful for lip-speech agreement checks.", "Speech recognition quality is not identical to generative lip-sync quality; model is archived and domain-limited."),
    source("B025", "PhyGround", "Lin et al.", "2026", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2605.10806", "Uses criteria-grounded physical-law questions and reports evaluator bias differences, supporting auditable, law-specific and human-calibrated scoring.", "Recent preprint; requires independent reproduction."),
    source("B026", "CRONOS", "Begiristain et al.", "2026", "benchmark_project", "benchmark_result", "https://genintel.github.io/CRONOS/", "Uses controlled counterfactual interventions for falls, collisions, and full occlusion/reappearance.", "Controlled simulated setting may not predict cinematic model behavior exactly."),
]

SOURCE_BY_ID = {s["source_id"]: s for s in SOURCES}

# ---------------------------------------------------------------------------
# Research contracts, metrics, providers, mechanisms, and failure records
# ---------------------------------------------------------------------------

MITIGATION_LEVELS = {
    "L0": "wording repair",
    "L1": "structured prompt repair",
    "L2": "canonical event/state contract",
    "L3": "reference image or storyboard",
    "L4": "pose, mask, depth, trajectory, or control video",
    "L5": "shot decomposition",
    "L6": "postproduction/compositing",
    "L7": "regenerate only the failing interval",
    "L8": "provider/model substitution",
    "L9": "unsupported or not reliably controllable",
}

EVIDENCE_RANK = {
    "officially_documented_capability": 5,
    "peer_reviewed_experimental_result": 5,
    "benchmark_result": 4,
    "controlled_repository_observation": 3,
    "research_inference": 2,
    "community_anecdote": 1,
    "unverified_claim": 0,
}

MECHANISMS = [
    {
        "mechanism_id": "mechanism://underdetermined_hidden_state",
        "name": "Underdetermined hidden-state completion",
        "description": "When pixels cease to observe a subject or object, many latent continuations remain compatible with the visible frames and prompt. A generator without an externally enforced state trajectory may sample a plausible replacement rather than preserve the exact hidden state.",
        "evidence_basis": ["B011", "B012", "B013", "B014", "B017"],
        "confidence": "high for the observable phenomenon; medium for closed-model internals",
        "falsifiable_prediction": "Continuity failure should rise with complete occlusion duration and recurrence distance, and fall when masks, point tracks, silhouettes, or explicit reappearance constraints bridge the hidden interval.",
    },
    {
        "mechanism_id": "mechanism://entity_binding_ambiguity",
        "name": "Entity-binding and role ambiguity",
        "description": "Text labels, visual appearance, screen location, and action roles can become competing identifiers. Similar actors, close contact, crossings, and cuts increase the chance that identity and role assignments are rebound.",
        "evidence_basis": ["B002", "B015", "B017", "B019"],
        "confidence": "high for the failure family; medium for any provider-specific causal attribution",
        "falsifiable_prediction": "Identity and role errors should increase with actor similarity and recurrence distance, while distinct identity signatures, stable screen lanes, separate references, and explicit role edges should reduce them.",
    },
    {
        "mechanism_id": "mechanism://state_representation_gap",
        "name": "State representation gap",
        "description": "A prose prompt usually describes desired events but does not carry a queryable ledger of identity, object count, possession, visibility, material state, and allowed transitions. The generator is therefore asked to infer persistence rather than obey an explicit state machine.",
        "evidence_basis": ["B003", "B011", "B014", "B015", "R006"],
        "confidence": "high as a control-system diagnosis; model-internal causality remains unverified",
        "falsifiable_prediction": "A state ledger plus transition assertions should improve state-transition agreement more than adding equivalent descriptive adjectives after controlling for prompt length.",
    },
    {
        "mechanism_id": "mechanism://coordinate_frame_ambiguity",
        "name": "Coordinate-frame ambiguity",
        "description": "Natural-language directions may refer to actor-relative, viewer-relative, camera-relative, or world-relative coordinates. Camera motion and edits change the screen projection without necessarily changing world geometry.",
        "evidence_basis": ["B002", "R005", "R006"],
        "confidence": "high",
        "falsifiable_prediction": "Explicit coordinate-frame declarations and shot-to-shot transforms should reduce left/right and axis errors compared with unqualified directional prose.",
    },
    {
        "mechanism_id": "mechanism://temporal_dependency_collapse",
        "name": "Temporal dependency collapse",
        "description": "Multiple ordered actions, dependencies, and reactions compete for limited duration and conditioning capacity. The output may merge, omit, reorder, or make dependent events simultaneous.",
        "evidence_basis": ["B003", "B010", "B017"],
        "confidence": "high for the observable pattern; provider thresholds require testing",
        "falsifiable_prediction": "Failure should rise with dependency depth and action density, while an explicit event graph or shot split should outperform equivalent compressed prose.",
    },
    {
        "mechanism_id": "mechanism://physical_constraint_absence",
        "name": "No guaranteed physical constraint solver",
        "description": "Current video generators can learn statistical regularities without enforcing conservation, support, collision, fluid response, or rigid-body constraints. Visual plausibility and physical correctness are therefore separable.",
        "evidence_basis": ["B004", "B005", "B006", "B025", "B026"],
        "confidence": "high",
        "falsifiable_prediction": "Prompt elaboration alone will plateau on interactions requiring precise contact, momentum, or material response; control media, decomposition, simulation, or postproduction will produce larger gains.",
    },
    {
        "mechanism_id": "mechanism://conditioning_competition",
        "name": "Conditioning competition and priority dilution",
        "description": "Long, repetitive, contradictory, or multiply serialized instructions compete for influence. Providers may rewrite, truncate, or semantically compress prompts, and exact numerical fields may not map to explicit controllable variables.",
        "evidence_basis": ["R005", "M002", "M007"],
        "confidence": "medium; provider parsing behavior requires controlled tests",
        "falsifiable_prediction": "After matching semantics, concise single-authority prompts should equal or outperform duplicated XML+JSON+YAML bundles on adherence per character, especially under provider prompt limits.",
    },
    {
        "mechanism_id": "mechanism://camera_scene_entanglement",
        "name": "Camera/scene-motion entanglement",
        "description": "Observed optical flow is a mixture of camera motion, actor motion, deforming effects, and edits. A generative model may satisfy a camera instruction by moving the scene or subject instead of reproducing the intended world-space trajectory.",
        "evidence_basis": ["B021", "R004", "R006"],
        "confidence": "medium-high",
        "falsifiable_prediction": "Separating camera and actor tracks, or holding one constant, should reduce trajectory drift and identity deformation compared with combined complex instructions.",
    },
    {
        "mechanism_id": "mechanism://graphic_world_state_conflation",
        "name": "Graphic discontinuity conflated with world-state change",
        "description": "Flashes, smears, wipes, speed lines, and blur are both visual effects and potential shot boundaries. Without an explicit continuity contract, the model may treat a graphic discontinuity as permission to reset identity, anatomy, style, or geography.",
        "evidence_basis": ["B010", "B017", "R005"],
        "confidence": "medium-high",
        "falsifiable_prediction": "A required post-effect recovery frame and explicit 'graphic-only; world state unchanged' assertion should reduce scene-reset errors, with stronger gains from first/last frames or reference keyframes.",
    },
    {
        "mechanism_id": "mechanism://evaluator_observability_gap",
        "name": "Evaluator observability gap",
        "description": "A single VLM or detector may miss fast events, hallucinate contact, swap tracks, misclassify flashes as cuts, or fail on stylized anatomy. Evaluation therefore needs multiple independent lanes plus preserved conflicts and human calibration.",
        "evidence_basis": ["B007", "B008", "B009", "B017", "B018", "B019", "B020", "B021", "B025"],
        "confidence": "high",
        "falsifiable_prediction": "Disagreement will concentrate in short contact intervals, full occlusions, fast motion, reflections, and stylized frames; multi-lane adjudication will reduce false certainty rather than necessarily increase pass rate.",
    },
]


def metric(mid: str, name: str, dimension: str, method: str, unit: str, threshold_policy: str, blind_spots: str, human: str, sources: list[str]) -> dict[str, Any]:
    return {
        "metric_id": mid,
        "name": name,
        "observable_dimension": dimension,
        "measurement_method": method,
        "unit": unit,
        "threshold_policy": threshold_policy,
        "evaluator_or_tool": "version-pinned implementation required",
        "confidence": "calibrate per content domain and provider",
        "known_blind_spots": blind_spots,
        "human_calibration_requirement": human,
        "source_refs": sources,
    }


METRICS = [
    metric("metric_actor_count_consistency", "Actor-count consistency", "Number of distinct intended actors visible or tracked over time", "Segmentation/tracking consensus with reflection suppression and human review at ambiguous intervals", "proportion of frames and event checkpoints with correct count", "Calibrate separately for realistic and stylized content; any duplicate during a hard actor-count lock is a critical failure", "Reflections, silhouettes, occlusion, crowds, and fused bodies", "Required for full occlusion, mirrors, stylized effects, and disagreements", ["B018", "B019", "B017"]),
    metric("metric_identity_continuity", "Identity continuity", "Persistence of face, hair, costume, body proportions, and nonfacial signature", "Fuse face/body/costume embeddings, color/material descriptors, track continuity, and human identity verdicts", "0-1 composite plus component deviations", "Thresholds must be learned from same-character positive pairs and intentionally different negative pairs", "Profile view, blur, masks, anime deformation, lighting, and occlusion", "Required whenever component metrics disagree or identity is plot-critical", ["B015", "B017", "B019"]),
    metric("metric_role_assignment_accuracy", "Role-assignment accuracy", "Correct initiator, target, holder, speaker, attacker, and defender assignment", "Compare extracted event graph roles with canonical role edges at event checkpoints", "role-edge precision/recall/F1", "Critical role swaps fail regardless of aggregate score", "Fast contact, similar actors, off-screen action, and ambiguous pronouns", "Required for critical action and dialogue roles", ["B002", "B003", "B017"]),
    metric("metric_object_count_persistence", "Object-count persistence", "Object number across frames, occlusions, cuts, and reflections", "Class-aware segmentation/tracking with state-ledger checkpoints", "count error and persistence rate", "Zero tolerance for hard-locked product/prop counts; domain-specific tolerance otherwise", "Small objects, reflections, smoke, motion blur", "Review every count change not authorized by an event", ["B011", "B013", "B018"]),
    metric("metric_object_state_transition", "Object-state transition agreement", "Open/closed, intact/damaged, held/released, wet/dry, on/off, and other state transitions", "State classifier or VLM questions anchored to precondition and postcondition frames, plus human adjudication", "transition accuracy and illegal-transition count", "Any state change without a causal event is a failure under a hard state lock", "Subtle states, stylization, hidden changes", "Required for product demos and narrative-critical states", ["B003", "B014", "B017"]),
    metric("metric_reappearance_position_error", "Reappearance-position error", "Spatial continuity through full occlusion", "Predict hidden path from pre-occlusion velocity/trajectory or supplied control track; compare reappearance centroid in normalized screen/world coordinates", "normalized frame diagonal or world units", "Provider/task-specific distribution; hard-region violation always fails", "Camera cuts, nonrigid motion, long hidden intervals", "Review when camera or edit transforms are uncertain", ["B013", "B019", "B020"]),
    metric("metric_occlusion_continuity", "Occlusion continuity score", "Identity, count, state, pose family, trajectory, and allowed-change agreement across an occlusion interval", "Weighted contract checks at pre-entry, hidden interval proxies, and first stable reappearance frame", "0-1 composite and per-check verdicts", "No universal threshold; critical hard locks are conjunctive", "No observable hidden path; evaluator may infer incorrectly", "Required for complete occlusion unless a trusted control track exists", ["B011", "B012", "B013", "B014", "B017"]),
    metric("metric_visibility_bridge_coverage", "Visibility-bridge coverage", "Fraction of hidden interval with a tracked silhouette, mask, shadow, bubble trail, limb, or control signal", "Framewise bridge presence and track continuity", "0-1 interval coverage", "Treat as an input/control diagnostic, not proof of output correctness", "Bridge can attach to the wrong actor", "Review attachment identity on multi-actor scenes", ["B013", "B018", "B019"]),
    metric("metric_spatial_relation_accuracy", "Spatial-relation accuracy", "Left/right, front/behind, above/below, near/far, containment, and depth relations", "Extract relations per beat in declared coordinate frame and compare with canonical transitions", "relation accuracy/F1", "Critical relation hard locks fail conjunctively", "Camera-relative ambiguity and close overlap", "Required after cuts/orbits and for ambiguous depth", ["B002", "B017"]),
    metric("metric_screen_direction_consistency", "Screen-direction consistency", "Sign and lane of actor motion in screen coordinates", "Track actor centroid/pose root and camera transform; compare signed displacement with score", "signed direction accuracy and reversal count", "No unauthorized sign reversal within a shot; cross-shot rules depend on declared axis policy", "Orbiting camera, zoom, cuts, and perspective", "Review if camera transform cannot be recovered", ["B019", "B020", "B021"]),
    metric("metric_axis_crossing_count", "Unauthorized axis crossing count", "Actor or camera crossing the declared axis of action", "Estimate shot geometry and screen-side ordering across checkpoints", "integer count and interval list", "Zero for no-axis-cross hard locks", "Uncertain world geometry from monocular video", "Human review for deliberate reverse angles", ["B002", "R006"]),
    metric("metric_depth_order_accuracy", "Depth-order accuracy", "Correct front/behind ordering and occlusion ownership", "Depth estimation plus segmentation overlap ordering and human adjudication", "pairwise depth-order accuracy", "Calibrate by domain; exact metric is unreliable under stylization", "Transparent materials, flat anime art, reflections", "Required in stylized or transparent scenes", ["B016", "B018"]),
    metric("metric_event_graph_agreement", "Event-graph agreement", "Presence and role assignment of requested events and dependencies", "Extract event graph from output; compare nodes and typed edges with canonical graph", "node/edge precision, recall, F1", "Critical events and dependencies are conjunctive; noncritical events can use weighted score", "Fast or visually implied events may be missed by VLM", "Human calibration on critical intervals", ["B003", "B017"]),
    metric("metric_temporal_event_error", "Temporal event error", "Difference between expected and observed event onset/apex/end", "Frame- or time-indexed event detection with uncertainty intervals", "milliseconds, frames, or normalized clip duration", "Provider/task-specific tolerance; order inversions always fail", "Ambiguous onset, motion blur, low frame rate", "Required for causally linked events and audio sync", ["B003", "B010", "B017"]),
    metric("metric_causal_edge_accuracy", "Causal-edge accuracy", "Whether consequences follow the correct initiator/cause", "Question-answer or event-graph adjudication using explicit cause, target, consequence, and reaction edges", "edge accuracy/F1", "All critical causal edges must pass", "Coincident events can appear causal", "Human review for ambiguous contact/effects", ["B004", "B005", "B017"]),
    metric("metric_reaction_latency_error", "Reaction-latency error", "Delay from cause/contact/near-contact to target reaction", "Compare detected cause apex and reaction onset", "milliseconds or frames", "Calibrate to style; negative latency is a hard failure unless anticipation is authored", "Subtle anticipation and editing conventions", "Review authored anticipation and anime holds", ["B003", "B004"]),
    metric("metric_contact_distance", "Contact-distance error", "Distance or overlap at intended contact/near-contact frame", "Pose/segmentation keypoints, depth proxy, and projected overlap classified by contact type", "pixels normalized by body size; depth proxy where available", "Type-specific: physical contact, staged near-contact, camera-cheated contact, grasp, or surface contact", "Monocular depth and hidden limbs", "Required for safety-critical and ambiguous contact", ["B018", "B019", "B020"]),
    metric("metric_penetration_duration", "Penetration duration", "Duration of impossible body/body, body/object, or limb/surface intersection", "Segmentation/pose/depth overlap persistence with topology rules", "frames or milliseconds", "Zero beyond allowed stylized smear window", "Occlusion can resemble penetration; pose models fail on anime", "Required for stylized or obscured contact", ["B016", "B018"]),
    metric("metric_foot_slip_distance", "Foot-slip distance", "Support-foot movement while intended planted", "Optical flow and point tracking at foot contact, compensated for camera motion", "pixels/body-height or world units per support interval", "Calibrate by shot scale and style; flag nonzero drift beyond tracking uncertainty", "Blur, floor reflections, occlusion, low resolution", "Review when confidence interval overlaps threshold", ["B019", "B020", "B021"]),
    metric("metric_support_plausibility", "Support plausibility", "Base of support, contact state, center-of-mass projection, takeoff, landing, and settle", "Pose/track-derived support phases plus human biomechanics review", "phase agreement and violation count", "No universal physical threshold for stylized content; preserve causal skeleton and authored support phases", "2D pose cannot recover true 3D balance", "Human review required for acrobatics and anime", ["B004", "B005"]),
    metric("metric_momentum_continuity", "Momentum-continuity proxy", "Whether velocity and direction change are causally supported", "Track body/object centroids, estimate camera-compensated velocity, and flag unexplained discontinuities", "normalized velocity/acceleration discontinuity", "Provider/task-specific; use as diagnostic, not literal mass-conservation proof", "Monocular scale, cuts, speed ramps, stylization", "Human review for edits and anime time suspension", ["B004", "B005", "B021"]),
    metric("metric_effect_origin_error", "Effect-origin error", "Distance between causal contact/displacement point and splash/debris/flash/smoke origin", "Segment effect onset and compare centroid with causal event target point", "normalized frame diagonal", "Calibrate by effect spread; origin outside allowed region fails", "Diffuse effects and obscured contact", "Review large stylized effects", ["B004", "B005", "B018"]),
    metric("metric_effect_decay_error", "Effect-decay error", "Effect persistence relative to authored onset, peak, decay, and end", "Temporal segmentation of effect opacity/area with expected envelope", "timing error and residual area", "Task-specific; any effect before cause is a hard causal failure", "Blended particles and camera exposure changes", "Review when effect boundaries are subjective", ["B003", "B010"]),
    metric("metric_material_state_consistency", "Material-state consistency", "Water level/topology, wetness, cloth attachment, hair continuity, debris count, and other material state", "Material-specific segmentation/state questions at checkpoints", "state accuracy and illegal transition count", "Hard locks conjunctive; otherwise domain-calibrated", "Transparent/reflective materials and stylization", "Required for product and fluid-critical scenes", ["B005", "B018"]),
    metric("metric_camera_motion_agreement", "Camera-motion agreement", "Pan, tilt, roll, translation, orbit, zoom/lens, and shake versus canonical camera track", "Estimate homography/flow/background motion and compare with declared camera components", "parameter error and qualitative agreement", "Calibrate per shot; distinguish optical zoom from dolly when observable", "Parallax, moving backgrounds, low texture, cuts", "Human review for complex parallax and virtual cameras", ["B021", "R004"]),
    metric("metric_camera_actor_entanglement", "Camera/actor entanglement ratio", "Unintended covariance between requested camera motion and actor/world displacement", "Decompose background, camera, and actor flow; compare intended independent tracks", "0-1 entanglement index", "Research metric requiring calibration; use primarily for A/B comparisons", "Nonrigid backgrounds, handheld footage, full-frame effects", "Review all high-severity flags", ["B021"]),
    metric("metric_edit_graphic_classification", "Edit/graphic-discontinuity classification", "Correct distinction among cut, flash, smear, blur, wipe, hold, and world-state change", "Shot detector plus effect classifier plus identity/state checks before/after interval", "class accuracy and false-reset count", "Any graphic-only interval causing unauthorized state reset fails", "One-frame effects, black frames, stylized cuts", "Human review required for one-frame ambiguity", ["B010", "B017"]),
    metric("metric_anatomy_recovery_latency", "Anatomy-recovery latency", "Time from permitted deformation end to restored anatomy and identity", "Pose/silhouette/anatomy checks on required recovery frame and following frames", "frames or milliseconds", "Must recover by contract deadline; stylized deformation window excluded", "Pose detectors fail on deliberate smears", "Human animation review required", ["B017", "B018"]),
    metric("metric_lip_sync_offset", "Lip-sync offset", "Temporal alignment of visible speech articulation and audio", "Audio-visual speech model plus phoneme/mouth-event alignment", "milliseconds", "Calibrate language, frame rate, and speaking style; report confidence interval", "Profile view, beard/mask, stylized mouths, singing", "Human review for low-confidence or creative timing", ["B023", "B024"]),
    metric("metric_audio_event_alignment", "Audio-event alignment", "Timing and semantic agreement of impacts, splashes, breaths, music accents, and environmental sounds", "Detect audio events and visual events; compare typed anchors and onset offsets", "milliseconds plus semantic match", "Separate semantic mismatch from temporal mismatch", "Overlapping sounds and off-screen sources", "Human review for ambiguous sources", ["B022", "B023"]),
    metric("metric_human_readability", "Human action readability", "Whether intended actors, action, cause, target, and outcome are understandable", "Blinded human rating with forced-choice event/role questions and confidence", "accuracy, confidence, and inter-rater agreement", "Pre-register acceptance thresholds per use case", "Rater expertise, cultural conventions, fatigue", "At least two calibrated raters for critical scenes", ["B008", "B009"]),
    metric("metric_evaluator_disagreement", "Evaluator disagreement", "Conflict across semantic, measurement, and human lanes", "Preserve lane verdicts and calculate pairwise/overall agreement", "Krippendorff alpha, Cohen kappa, conflict count", "Do not collapse disagreement into a single confident score", "Shared model biases and nonindependent tools", "Adjudication required above pre-registered criticality", ["B007", "B017", "B025", "R009"]),
    metric("metric_observability_coverage", "Observability coverage", "Fraction of hard controls with valid evidence in an appropriate lane", "Map each canonical control to evidence, evaluator version, interval, and confidence", "0-1 coverage plus unobservable count", "All critical hard locks require evidence or explicit unobservable status", "Evaluator gaps and missing raw assets", "Required for any production qualification", ["R008", "R009"]),
    metric("metric_control_retention", "Control retention after repair", "Preservation of already-passing controls during localized repair", "Re-run full verification plan and compare preserved control IDs", "retention rate and regression count", "Zero regression on hard locks; bounded tolerance on soft controls", "Evaluator drift and stochastic variation", "Human review for visually meaningful regressions", ["R009"]),
]
METRIC_BY_ID = {m["metric_id"]: m for m in METRICS}

PROVIDERS = [
    {
        "provider": "Google Vertex AI",
        "model_family": "Veo 3.1",
        "version_or_model_id": "veo-3.1-generate-001 / verify endpoint-specific variant",
        "release_or_doc_date": "documentation updated 2026-01-02",
        "documented_workflows": "text-to-video; image-to-video; first-and-last-frame",
        "documented_reference_inputs": "first frame; last frame; endpoint-dependent reference/extension features must be verified",
        "documented_audio": "conflicting across endpoint/documentation surfaces; do not assume",
        "documented_duration": "4, 6, or 8 seconds on cited first/last endpoint",
        "documented_resolution": "720p or 1080p on cited first/last endpoint",
        "documented_prompt_limit": "not asserted in this package",
        "documented_seed": "yes on cited endpoint",
        "documented_negative_prompt": "yes on cited endpoint",
        "official_source_refs": "M001;M013",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "existing repository adapter/profile; schema currently hard-coded",
        "highest_value_controls": "first/last frames; seed; negative prompt; canonical loss report",
        "known_evidence_gap": "No repeated-seed CPCS failure matrix; endpoint audio/reference behavior requires exact API verification",
    },
    {
        "provider": "Runway",
        "model_family": "Gen-4.5",
        "version_or_model_id": "Gen-4.5 / current API identifier must be pinned at implementation",
        "release_or_doc_date": "API availability 2026-02-10",
        "documented_workflows": "text-to-video; image-to-video through current API surfaces",
        "documented_reference_inputs": "image conditioning and provider endpoint assets",
        "documented_audio": "model/endpoint-specific; not assumed",
        "documented_duration": "2-10 seconds in cited API family documentation",
        "documented_resolution": "endpoint/ratio dependent; pin exact API response",
        "documented_prompt_limit": "up to 1000 characters on cited generation request family",
        "documented_seed": "documented in current API reference",
        "documented_negative_prompt": "model-specific",
        "official_source_refs": "M002;M003",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "reference image; seed; short bounded prompt; provider-specific duration/ratio negotiation",
        "known_evidence_gap": "No official failure taxonomy or CPCS ablation results",
    },
    {
        "provider": "Runway-hosted ByteDance model",
        "model_family": "Seedance 2.0 / Seedance 2.0 Fast",
        "version_or_model_id": "seedance2 / seedance2_fast on cited Runway changelog",
        "release_or_doc_date": "official launch 2026-02-12; Runway API 2026-05-28/2026-06-05",
        "documented_workflows": "text, image, video, and audio conditioned generation; multi-shot",
        "documented_reference_inputs": "up to 9 images, 3 videos, 3 audio clips in ByteDance product description",
        "documented_audio": "joint audio-video documented",
        "documented_duration": "up to 15 seconds in cited official descriptions",
        "documented_resolution": "verify exact hosting endpoint",
        "documented_prompt_limit": "verify exact hosting endpoint",
        "documented_seed": "verify exact hosting endpoint",
        "documented_negative_prompt": "not asserted",
        "official_source_refs": "M003;M004",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "multimodal references; reference video; key images; shot decomposition; audio anchors",
        "known_evidence_gap": "Provider wrapper may transform limits and reference semantics; marketing reliability claims excluded",
    },
    {
        "provider": "Kling AI",
        "model_family": "Kling VIDEO 3.0",
        "version_or_model_id": "Kling VIDEO 3.0",
        "release_or_doc_date": "guide dated 2026-02-06",
        "documented_workflows": "T2V; I2V; start/end frame; multi-shot; native audio",
        "documented_reference_inputs": "element references; multi-character reference/coreference; start/end frames",
        "documented_audio": "native audio documented",
        "documented_duration": "3-15 seconds",
        "documented_resolution": "verify selected product/API tier",
        "documented_prompt_limit": "not asserted",
        "documented_seed": "not asserted",
        "documented_negative_prompt": "not asserted",
        "official_source_refs": "M005",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "element references; start/end frames; multi-shot segmentation; explicit role labels",
        "known_evidence_gap": "Exact regional/API feature availability and parsing behavior require live verification",
    },
    {
        "provider": "MiniMax",
        "model_family": "Hailuo-2.3 / Hailuo-2.3-Fast",
        "version_or_model_id": "Hailuo-2.3; Hailuo-2.3-Fast",
        "release_or_doc_date": "2025-10-28",
        "documented_workflows": "2.3 T2V and I2V; Fast I2V",
        "documented_reference_inputs": "first image for I2V; verify other endpoint controls",
        "documented_audio": "not asserted in cited video endpoints",
        "documented_duration": "768p 6/10 seconds; 1080p 6 seconds in release notes",
        "documented_resolution": "768p or 1080p as documented",
        "documented_prompt_limit": "up to 2000 characters for cited T2V endpoint",
        "documented_seed": "verify endpoint",
        "documented_negative_prompt": "not asserted",
        "official_source_refs": "M006;M007",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "I2V anchoring; provider camera commands; concise prompt; shot split",
        "known_evidence_gap": "No controlled CPCS comparison of bracketed camera syntax versus canonical camera tracks",
    },
    {
        "provider": "Lightricks / open weights",
        "model_family": "LTX-2",
        "version_or_model_id": "pin exact checkpoint and commit",
        "release_or_doc_date": "repository current through 2026",
        "documented_workflows": "T2V; I2V/keyframes; V2V; extension; control models; joint audio-video",
        "documented_reference_inputs": "multiple keyframes; control models; video input",
        "documented_audio": "synchronized audio-video documented",
        "documented_duration": "up to 10 seconds in cited repository",
        "documented_resolution": "up to 4K/50fps claimed by repository; local qualification required",
        "documented_prompt_limit": "local implementation dependent",
        "documented_seed": "local inference should pin seed/config",
        "documented_negative_prompt": "pipeline dependent",
        "official_source_refs": "M008",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "multiple keyframes; control video; local reproducibility; interval regeneration",
        "known_evidence_gap": "Checkpoint/sampler/hardware combinations materially affect behavior",
    },
    {
        "provider": "Wan-Video / open weights",
        "model_family": "Wan2.2",
        "version_or_model_id": "pin checkpoint, task variant, and commit",
        "release_or_doc_date": "2025-07-28 onward",
        "documented_workflows": "T2V; I2V; TI2V; S2V; pose/video control; animation/replacement",
        "documented_reference_inputs": "image; pose/control video; audio/speech for S2V; task-specific inputs",
        "documented_audio": "task-specific speech-to-video; not general native sound assumption",
        "documented_duration": "task/config dependent",
        "documented_resolution": "480p/720p documented workflows",
        "documented_prompt_limit": "local pipeline dependent",
        "documented_seed": "yes through local inference configuration",
        "documented_negative_prompt": "pipeline dependent",
        "official_source_refs": "M009",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "pose/control video; local seed reproducibility; separate task checkpoints",
        "known_evidence_gap": "Cross-checkpoint comparability and local MPS/CUDA behavior require qualification",
    },
    {
        "provider": "Tencent Hunyuan / open weights",
        "model_family": "HunyuanVideo-1.5",
        "version_or_model_id": "pin checkpoint and commit",
        "release_or_doc_date": "2025-11-20 onward",
        "documented_workflows": "T2V; I2V",
        "documented_reference_inputs": "image for I2V",
        "documented_audio": "not documented as joint audio generation in cited repository",
        "documented_duration": "configuration dependent",
        "documented_resolution": "480p/720p generation; 1080p super-resolution workflow",
        "documented_prompt_limit": "local implementation dependent",
        "documented_seed": "documented local configuration",
        "documented_negative_prompt": "pipeline dependent",
        "official_source_refs": "M010",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "I2V start-state anchor; fixed seed/config; local instrumentation",
        "known_evidence_gap": "No external repeated-seed CPCS task matrix",
    },
    {
        "provider": "THUDM / open weights",
        "model_family": "CogVideoX1.5",
        "version_or_model_id": "pin exact T2V/I2V checkpoint and commit",
        "release_or_doc_date": "official repository current through 2025/2026",
        "documented_workflows": "T2V; I2V",
        "documented_reference_inputs": "image for I2V",
        "documented_audio": "not documented as joint audio generation",
        "documented_duration": "approximately 10-second model family output in cited repository",
        "documented_resolution": "checkpoint-specific documented resolutions/frames",
        "documented_prompt_limit": "local implementation dependent",
        "documented_seed": "local inference configuration",
        "documented_negative_prompt": "pipeline dependent",
        "official_source_refs": "M011",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "I2V anchoring; fixed seed; low-action-density prompts; local metrics",
        "known_evidence_gap": "Checkpoint-specific limits must be resolved before compilation",
    },
    {
        "provider": "Genmo / open weights",
        "model_family": "Mochi 1 preview",
        "version_or_model_id": "pin exact checkpoint and commit",
        "release_or_doc_date": "2024 preview; repository current thereafter",
        "documented_workflows": "T2V in cited release",
        "documented_reference_inputs": "not assumed beyond current repository pipeline",
        "documented_audio": "not documented as joint audio generation",
        "documented_duration": "pipeline/checkpoint dependent",
        "documented_resolution": "pipeline/checkpoint dependent",
        "documented_prompt_limit": "local implementation dependent",
        "documented_seed": "local inference configuration",
        "documented_negative_prompt": "pipeline dependent",
        "official_source_refs": "M012",
        "empirical_failure_rate": "not qualified in this package",
        "cpcs_adapter_status": "absent in repository",
        "highest_value_controls": "fixed seed/config; simple shots; postproduction for complex interactions",
        "known_evidence_gap": "Preview model is not evidence of current commercial parity or complex-control reliability",
    },
]

# Additional primary sources verified during the 2026-08-05 research pass.
SOURCES.extend([
    source("M014", "Video generation and editing model overview", "Alibaba Cloud Model Studio", "updated 2026-07-01", "official_documentation", "officially_documented_capability", "https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model", "Version-scopes Wan 2.7 text, image, reference, editing, audio, duration, resolution, frame rate, and character animation interfaces.", "Capability documentation does not establish continuity or physics reliability."),
    source("M015", "Available AI models and API reference", "Runway", "accessed 2026-08-05", "official_documentation", "officially_documented_capability", "https://docs.dev.runwayml.com/guides/models/", "Current Runway API exposes gen4.5, aleph2, Seedance 2 variants, Veo variants, and other models with endpoint-specific inputs.", "Runway-hosted third-party behavior may differ from native-provider interfaces."),
    source("M016", "Creating with Edit Studio (Aleph 2.0)", "Runway", "2026", "official_documentation", "officially_documented_capability", "https://help.runwayml.com/hc/en-us/articles/51683104370451-Creating-with-Edit-Studio", "Documents source-video editing and localized transformations over single- or multi-shot input up to 30 seconds.", "Product documentation describes available operations, not exact edit isolation rates."),
    source("M017", "Ray 3.2 introduction and core concepts", "Luma AI", "2026-05-27", "official_documentation", "officially_documented_capability", "https://lumalabs.ai/learning-center/articles/ray-3-2-introduction-and-core-concepts", "Clarifies Ray 3.2 is source-video modify, not text-to-video, image animation, or extension; supports dense keyframe anchoring and source-duration preservation.", "Product documentation does not establish perfect source preservation."),
    source("M018", "Sora 2 System Card", "OpenAI", "2025-09-30; status note 2026-04-26", "official_system_card", "officially_documented_capability", "https://openai.com/index/sora-2-system-card/", "Documents Sora 2 video/audio claims and states that the consumer Sora product is no longer available as of 2026-04-26.", "No current public production interface was verified in this research pass."),
    source("M019", "Kling AI launches 3.0", "Kuaishou Technology", "2026-02-05", "official_company_release", "officially_documented_capability", "https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be", "Documents Kling Video 3.0 and Video 3.0 Omni with text, image, audio, and video inputs, native audio, reference/editing tasks, and up to 15-second output.", "Quality and consistency language is provider-authored and not independent reliability evidence."),
    source("M020", "MiniMax API overview", "MiniMax", "accessed 2026-08-05", "official_documentation", "officially_documented_capability", "https://platform.minimax.io/docs/api-reference/api-overview", "Lists current video models and text, first-frame, last-frame, and reference-image inputs.", "Exact features vary by model and endpoint."),
    source("M021", "Runway API input parameters", "Runway", "accessed 2026-08-05", "official_documentation", "officially_documented_capability", "https://docs.dev.runwayml.com/assets/inputs/", "Documents current aspect-ratio rules and that Aleph 2.0 preserves source resolution up to 1080p for 2-30 second inputs at 30 fps or lower.", "Resolution preservation is not semantic-state preservation."),
    source("M022", "Gen-4.5 API changelog entry", "Runway", "2026-02-10", "official_documentation", "officially_documented_capability", "https://docs.dev.runwayml.com/api-details/api_changelog/", "Documents Gen-4.5 text-to-video and image-to-video with 2-10 second durations.", "No official failure distribution is provided."),
    source("M023", "Gen-3 Alpha prompting guide", "Runway", "historical; deprecated 2026", "official_documentation", "provider_specific_prompt_guidance", "https://help.runwayml.com/hc/en-us/articles/30586818553107-Gen-3-Alpha-Prompting-Guide", "Historically advises positive phrasing instead of negative phrasing for Gen-3.", "This is deprecated-model guidance and must not be generalized to all providers."),
    source("M024", "Wan 2.7 image-to-video API", "Alibaba Cloud Model Studio", "updated 2026-06-16", "official_documentation", "officially_documented_capability", "https://www.alibabacloud.com/help/en/model-studio/image-to-video-general-api-reference", "Documents first-frame, first/last-frame, video continuation, multimodal input, and region-bound endpoint behavior.", "Endpoint behavior and regional model aliases can change."),
    source("M025", "Wan reference-to-video API", "Alibaba Cloud Model Studio", "updated 2026", "official_documentation", "officially_documented_capability", "https://www.alibabacloud.com/help/en/model-studio/wan-video-to-video-api-reference", "Documents reference inputs, durations, prompt rewriting, seeds, and explicitly states that identical seeds do not guarantee identical output.", "Native provider behavior only; hosted adapters may expose different parameters."),

    source("B027", "WorldReasonBench", "Wu et al.", "2026-05-11", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2605.10434", "436 cases across physical, social, logical, and informational state evolution expose a gap between visual plausibility and dynamics, causality, or information preservation.", "Recent preprint; commercial model versions and rankings can change."),
    source("B028", "MBench", "Zhang et al.", "2026-05-30", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2606.00793", "Decomposes video-world-model memory into entity, environment, and causal consistency and reports systemic long-term state-retention limits.", "Recent preprint and long-horizon scope; not all short commercial clips are represented."),
    source("B029", "TimeBlind", "Li et al.", "2026-01-30", "research_preprint", "evaluator_limitation", "https://arxiv.org/abs/2602.00288", "Minimal temporal pairs show the strongest evaluated MLLM at 48.2% instance accuracy versus 98.2% human performance.", "Evaluates understanding models rather than generators; informs verifier calibration."),
    source("B030", "SLVMEval", "Matsuda et al.", "2026-03-31", "research_preprint", "evaluator_limitation", "https://arxiv.org/abs/2603.29186", "Synthetic degradations show evaluation systems below human accuracy in nine of ten long-video quality aspects.", "Long-video focus; individual evaluator versions may improve."),
    source("B031", "Towards Understanding Camera Motions in Any Video (CameraBench)", "Lin et al.", "NeurIPS 2025", "peer_reviewed_benchmark", "evaluator_limitation", "https://arxiv.org/abs/2504.15376", "Shows semantic and geometric camera-motion estimators have complementary blind spots; zoom and forward translation can be confused without training.", "Camera understanding benchmark, not a direct generator benchmark."),
    source("B032", "HumanScore", "Fang et al.", "2026-04-22", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2604.20157", "Six interpretable human-motion metrics identify temporal jitter, anatomically implausible poses, and motion drift across 13 models.", "Recent preprint; pose and biomechanics estimates remain model-dependent."),
    source("B033", "ETVA", "Guan et al.", "2025-03-21", "research_preprint", "evaluation_method", "https://arxiv.org/abs/2503.16867", "Uses prompt scene graphs and atomic questions; reports 58.47 Spearman correlation with human judgment for alignment.", "Correlation is not perfect; atomic QA can still miss fast or ambiguous events."),
    source("B034", "VideoScore2", "He et al.", "2025-09-26", "research_preprint", "evaluator_limitation", "https://arxiv.org/abs/2509.22799", "Reports around 50% average accuracy on four out-of-domain benchmarks despite improved multi-dimensional reasoning.", "Evaluator performance and benchmark composition may change after publication."),
    source("B035", "MotionCtrl", "Wang et al.", "2023-12-06", "research_preprint", "control_method", "https://arxiv.org/abs/2312.03641", "Separates camera motion from object motion using camera poses and trajectories.", "Model-specific research method; does not prove current commercial support."),
    source("B036", "DragNUWA", "Yin et al.", "2023-08-16", "research_preprint", "control_method", "https://arxiv.org/abs/2308.08089", "Combines text, image, and trajectory conditions for spatial and temporal control.", "Open research method with its own training and domain limits."),
    source("B037", "CameraCtrl", "He et al.", "2024-04-02", "research_preprint", "control_method", "https://arxiv.org/abs/2404.02101", "Uses explicit camera trajectories for precise camera-pose control.", "Requires a compatible trained module; ordinary text prompts do not gain this control automatically."),
    source("B038", "C-Drag", "Li et al.", "2025-02-27", "research_preprint", "control_method", "https://arxiv.org/abs/2502.19868", "Adds reasoning about surrounding-object effects because a controlled object's trajectory alone does not specify interaction consequences.", "VLM reasoning and trajectory prediction can fail; not a universal physics solver."),
    source("B039", "GenMAC", "Huang et al.", "2024-12-05", "research_preprint", "closed_loop_method", "https://arxiv.org/abs/2412.04440", "Iterates design, generation, verification, correction, and structured redesign for compositional video generation.", "Agent judgments and repeated generation add cost and can propagate evaluator errors."),
    source("B040", "VideoDirectorGPT", "Lin et al.", "2023-09-26", "research_preprint", "planning_method", "https://arxiv.org/abs/2309.15091", "Plans scenes, entity layouts, backgrounds, and consistency groups before grounded generation.", "Research framework and backbone-specific results; not a current provider guarantee."),
    source("B041", "VideoTetris", "Tian et al.", "2024-06-06", "research_preprint", "control_method", "https://arxiv.org/abs/2406.04277", "Uses spatiotemporal compositional attention for multiple objects and changing object counts.", "Requires model-level intervention rather than prompt-only access."),
    source("B042", "VBench", "Huang et al.", "2023-11-29", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2311.17982", "Defines 16 dimensions including identity consistency, motion smoothness, flicker, and spatial relationship with human annotations.", "Dimension scores can miss localized causal failures."),
    source("B043", "T2V-CompBench paper", "Sun et al.", "2024-07-19", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2407.14505", "Covers attribute, action, motion, spatial, interaction, and count binding over a large compositional prompt set.", "Benchmark results are model-version scoped."),
    source("B044", "VideoPhy-2 paper", "Bansal et al.", "2025-03-09", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2503.06800", "Reports only 22% joint success for the best evaluated model on the hard subset and difficulty with mass and momentum.", "Applies to tested models and prompts; not a current universal score."),
    source("B045", "PhyGenBench paper", "Meng et al.", "2024-10-07", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2410.05363", "Covers 160 prompts and 27 physical laws and reports that scaling and prompt engineering alone do not solve dynamic physical failures.", "Automated evaluator and prompt set have finite coverage."),
    source("B046", "AV-SyncBench", "Zhou et al.", "2026-07-01", "research_preprint", "benchmark_result", "https://arxiv.org/abs/2607.00726", "Separates temporal offset detection from semantic audio-video matching over 3,269 videos and 38,390 samples.", "Very recent preprint; exact leaderboard status may change."),
])
SOURCE_BY_ID = {s["source_id"]: s for s in SOURCES}


def compact(value: str) -> str:
    return " ".join(value.strip().split())


FAMILY_META: dict[str, dict[str, Any]] = {
    "A": {"name": "Occlusion and hidden-state continuity", "owner": "continuity + actions + verification", "default_sources": ["B012", "B013", "B014", "B017", "B027", "B028"], "canonical_paths": ["continuity.visibility_intervals", "continuity.state_ledger", "actions", "constraints.continuity_locks", "verification_requirements"], "metrics": ["metric_occlusion_reappearance_region_error", "metric_actor_count_consistency", "metric_identity_continuity", "metric_hidden_path_consistency"]},
    "B": {"name": "Object permanence and state persistence", "owner": "entities + continuity + verification", "default_sources": ["B011", "B012", "B015", "B027", "B028", "B042"], "canonical_paths": ["entities", "continuity.state_ledger", "assets", "constraints.continuity_locks", "verification_requirements"], "metrics": ["metric_object_count_consistency", "metric_state_transition_accuracy", "metric_material_attribute_stability", "metric_environment_layout_consistency"]},
    "C": {"name": "Identity, role, and actor assignment", "owner": "entities + interactions + continuity + verification", "default_sources": ["B002", "B015", "B027", "B028", "B041", "B042"], "canonical_paths": ["entities", "interactions", "actions", "continuity.identity_ledger", "constraints.continuity_locks"], "metrics": ["metric_identity_continuity", "metric_role_assignment_accuracy", "metric_screen_side_consistency", "metric_voice_identity_consistency"]},
    "D": {"name": "Spatial reasoning and screen geography", "owner": "scenes + shots + actions + camera + verification", "default_sources": ["B002", "B031", "B035", "B036", "B037", "B040"], "canonical_paths": ["scenes", "shots", "actions", "camera", "continuity.spatial_state", "verification_requirements"], "metrics": ["metric_screen_direction_consistency", "metric_depth_order_accuracy", "metric_trajectory_target_error", "metric_eyeline_consistency"]},
    "E": {"name": "Temporal order and action-graph collapse", "owner": "beats + actions + editing + verification", "default_sources": ["B003", "B017", "B027", "B029", "B033", "B039"], "canonical_paths": ["beats", "actions", "editing", "continuity.event_state", "verification_requirements"], "metrics": ["metric_action_graph_agreement", "metric_temporal_event_error", "metric_action_omission_rate", "metric_recovery_presence"]},
    "F": {"name": "Causality and reaction", "owner": "actions + interactions + effects + verification", "default_sources": ["B004", "B005", "B025", "B027", "B038", "B044"], "canonical_paths": ["actions", "interactions", "motion", "audio", "verification_requirements"], "metrics": ["metric_causal_edge_agreement", "metric_effect_origin_error", "metric_reaction_latency", "metric_target_assignment_accuracy"]},
    "G": {"name": "Contact, penetration, and interaction geometry", "owner": "interactions + motion + camera + verification", "default_sources": ["B002", "B004", "B025", "B032", "B038", "B043"], "canonical_paths": ["interactions", "motion", "camera", "constraints.hard", "verification_requirements"], "metrics": ["metric_contact_distance_error", "metric_penetration_duration", "metric_contact_target_accuracy", "metric_limb_separability"]},
    "H": {"name": "Balance, support, weight, and momentum", "owner": "motion + interactions + verification", "default_sources": ["B004", "B005", "B025", "B032", "B044", "B045"], "canonical_paths": ["motion", "interactions", "actions", "verification_requirements"], "metrics": ["metric_foot_slip_distance", "metric_support_state_consistency", "metric_momentum_discontinuity", "metric_landing_stability"]},
    "I": {"name": "Fluid, cloth, hair, debris, and material interaction", "owner": "interactions + style + continuity + verification", "default_sources": ["B004", "B005", "B010", "B025", "B027", "B045"], "canonical_paths": ["interactions", "style", "continuity.material_state", "actions", "verification_requirements"], "metrics": ["metric_material_response_consistency", "metric_effect_origin_error", "metric_surface_topology_stability", "metric_effect_persistence_error"]},
    "J": {"name": "Camera and actor-motion entanglement", "owner": "camera + motion + shots + verification", "default_sources": ["B031", "B035", "B037", "B040"], "canonical_paths": ["camera", "motion", "shots", "constraints.hard", "verification_requirements"], "metrics": ["metric_camera_motion_agreement", "metric_actor_world_trajectory", "metric_zoom_translation_disambiguation", "metric_screen_direction_consistency"]},
    "K": {"name": "Cuts, flashes, smears, and scene reset", "owner": "editing + continuity + style + verification", "default_sources": ["B003", "B010", "B015", "B027", "B033"], "canonical_paths": ["editing", "continuity", "style", "shots", "verification_requirements"], "metrics": ["metric_cut_flash_classification", "metric_post_cut_state_consistency", "metric_shot_boundary_error", "metric_graphic_discontinuity_recovery"]},
    "L": {"name": "Anatomy and stylization recovery", "owner": "motion + style + performance + verification", "default_sources": ["B001", "B016", "B032", "B042"], "canonical_paths": ["motion", "style", "performance", "continuity.anatomy_state", "verification_requirements"], "metrics": ["metric_anatomical_validity", "metric_deformation_duration", "metric_recovery_frame_accuracy", "metric_silhouette_readability"]},
    "M": {"name": "Prompt and serialization", "owner": "compiler + provider adapter + experiment registry", "default_sources": ["R005", "M001", "M002", "M007", "M023", "M025"], "canonical_paths": ["provider_neutral_controls", "provider_realization", "constraints", "warnings", "provenance"], "metrics": ["metric_field_projection_coverage", "metric_prompt_semantic_equivalence", "metric_hard_lock_retention", "metric_prompt_truncation_loss"]},
    "N": {"name": "Constraint overload and under-specification", "owner": "compiler + loss report + shot planner", "default_sources": ["B002", "B003", "B039", "B040", "B043"], "canonical_paths": ["constraints", "warnings", "unresolved", "provider_realization", "verification_requirements"], "metrics": ["metric_instruction_coverage", "metric_hallucinated_action_rate", "metric_constraint_conflict_count", "metric_primary_action_completion"]},
    "O": {"name": "Audio and cross-modal synchronization", "owner": "audio + actions + verification", "default_sources": ["B022", "B023", "B024", "B046", "M004", "M019"], "canonical_paths": ["audio", "actions", "beats", "continuity.voice_state", "verification_requirements"], "metrics": ["metric_audio_visual_temporal_offset", "metric_audio_visual_semantic_match", "metric_lip_speech_consistency", "metric_voice_identity_consistency"]},
    "P": {"name": "Verification and evaluator failure", "owner": "verification + immutable evidence + human calibration", "default_sources": ["B007", "B008", "B017", "B025", "B029", "B030", "B031", "B033", "B034"], "canonical_paths": ["verification_requirements", "provenance", "warnings", "unresolved"], "metrics": ["metric_evaluator_calibration", "metric_human_agreement", "metric_false_positive_rate", "metric_false_negative_rate"]},
}


def spec(slug: str, name: str, trigger: str, symptom: str, cause: str, level: str, mitigation: str, metric: str, sources: str, confidence: str = "moderate") -> dict[str, Any]:
    return {"slug": slug, "name": name, "trigger": compact(trigger), "symptom": compact(symptom), "cause": compact(cause), "level": level, "mitigation": compact(mitigation), "metric": metric, "sources": [x for x in sources.split() if x], "confidence": confidence}


FAMILY_SPECS: dict[str, list[dict[str, Any]]] = {
    "A": [
        spec("hidden_state_reconstruction", "Hidden-state reconstruction hallucination", "A subject becomes completely hidden by splash, smoke, debris, darkness, blur, or a foreground object.", "The subject returns with an invented pose, action, identity detail, or location.", "The hidden interval is underdetermined and the generator samples a plausible continuation without an explicit persistent state or trajectory constraint.", "L4", "Keep a visibility bridge or supply a tracked mask, silhouette, pose path, depth path, or control video; otherwise split before and after the opaque interval.", "metric_hidden_path_consistency", "B012 B013 B014 B027 B028", "high"),
        spec("duplicate_after_occlusion", "Subject duplication after opaque occlusion", "A full-frame effect hides one actor while a second actor or reflection remains visible.", "The returning actor coexists with an unintended duplicate or the occluder spawns a face or limb.", "Entity binding is re-solved from visible evidence after the occlusion and count constraints are weak.", "L4", "Lock actor count in the canonical state, retain distinct visibility anchors, and verify instance tracks through the effect; move the effect to post when count must be exact.", "metric_actor_count_consistency", "B001 B002 B013 B017 B028", "moderate"),
        spec("identity_rewrite_under_effect", "Identity rewrite under effect cover", "The face, costume, or body is fully hidden by an effect or fast blur.", "Hair, face, costume, or body proportions change on reappearance.", "Reference appearance competes with newly sampled local detail when no visible identity evidence survives.", "L3", "Use reference-conditioned generation plus a partially visible identity anchor; require an identity checkpoint immediately before and after the cover.", "metric_identity_continuity", "B001 B015 B016 B028", "moderate"),
        spec("reappearance_region_error", "Incorrect reappearance region", "A moving subject is fully occluded while continuing to translate or dive.", "The subject reappears too early, too late, or in the wrong screen/depth region.", "The prompt states disappearance and reappearance but not the latent path in a declared coordinate frame.", "L2", "Encode occlusion start/end, hidden trajectory, expected screen/depth region, and velocity continuity; escalate to trajectory control when tolerance is small.", "metric_occlusion_reappearance_region_error", "B013 B014 B019 B020 B027", "high"),
        spec("occluder_subject_fusion", "Occluder-subject fusion", "Hair, cloth, water, smoke, another body, or a foreground prop overlaps the subject for multiple frames.", "Materials merge with anatomy, clothing becomes fluid, or two bodies fuse.", "The model lacks stable layer ownership and boundary evidence during prolonged overlap.", "L4", "Provide masks or layered control media and preserve a readable silhouette; use compositing for dense particulate or fluid covers.", "metric_limb_separability", "B016 B018 B019 B032", "moderate"),
        spec("frame_exit_reentry_reset", "Frame-exit and re-entry state reset", "An actor exits the frame or is hidden by a camera whip and returns later.", "The actor returns with reset state, wrong prop, changed injury, or reversed role.", "Off-screen state is not directly observed and recurrence distance weakens entity memory.", "L5", "Terminate the shot at exit, create an explicit handoff state, and generate re-entry as a new shot from a state/reference keyframe when continuity is hard.", "metric_state_transition_accuracy", "B012 B015 B027 B028", "moderate"),
    ],
    "B": [
        spec("object_disappearance", "Persistent object disappearance", "A prop becomes small, briefly hidden, passed between hands, or de-emphasized by the camera.", "The prop vanishes before the canonical removal event.", "Object memory and salience fall below competing scene content.", "L3", "Use a dedicated reference/asset binding, state-ledger presence invariant, and object-specific verification track.", "metric_object_count_consistency", "B001 B002 B011 B015 B028", "high"),
        spec("spontaneous_object_creation", "Spontaneous object creation", "The prompt implies an interaction but omits the required prop's introduction or exact count.", "A new prop, weapon, product, or environmental element appears without an event.", "The model fills causal or semantic gaps with statistically likely objects.", "L2", "Declare the complete initial inventory and event-scoped creation/destruction permissions; reject undeclared count increases.", "metric_object_count_consistency", "B002 B027 B028 B041", "high"),
        spec("state_reset", "Object-state reset", "An object changes state, then is occluded, cut away from, or revisited.", "Open becomes closed, broken becomes intact, wet becomes dry, or consumed material returns.", "The generator re-samples a prototypical object rather than preserving an irreversible state delta.", "L2", "Represent state transitions as irreversible ledger deltas with validity intervals and post-transition reference frames.", "metric_state_transition_accuracy", "B003 B011 B014 B027 B028", "high"),
        spec("size_material_drift", "Size, color, or material drift", "A product or prop rotates, changes depth, becomes partially hidden, or crosses shots.", "Dimensions, logo placement, color, or material changes.", "Appearance features are not bound to a stable entity representation across viewpoints.", "L3", "Use orthographic/reference views or a product sheet, freeze non-negotiable attributes, and use video-to-video or compositing for exact product geometry.", "metric_material_attribute_stability", "B001 B002 B015 B016", "moderate"),
        spec("hand_object_detachment", "Hand-object detachment", "A hand manipulates, rotates, passes, or rapidly moves a held item.", "The object floats, penetrates the hand, changes hands without a pass, or lags behind the grip.", "Grasp state and contact point are not explicitly represented and fast interaction exceeds local binding stability.", "L4", "Provide pose/trajectory or source-video motion; encode hand, grip region, contact interval, and transfer event; isolate product close-ups.", "metric_contact_distance_error", "B002 B004 B032 B038", "high"),
        spec("environment_layout_drift", "Environmental layout drift", "A camera move, cut, or multi-shot sequence revisits the same room or terrain.", "Doors, cliffs, furniture, waterline, or background geometry move or change count.", "No explicit persistent scene map anchors layout across view changes.", "L3", "Use a scene reference board, depth/layout map, or source-video transform; maintain a scene-state ledger and camera/world transform.", "metric_environment_layout_consistency", "B015 B027 B028 B031 B040", "moderate"),
    ],
    "C": [
        spec("face_costume_drift", "Face and costume drift", "A character turns away, is blurred, changes shot scale, or crosses an edit.", "Facial structure, hair, costume elements, or accessories change.", "Identity features are weakly persistent relative to pose, lighting, and style changes.", "L3", "Use separate character references, stable identity IDs, attribute locks, and post-shot identity checkpoints.", "metric_identity_continuity", "B001 B015 B028 B042", "high"),
        spec("actor_duplication_fusion", "Actor duplication or fusion", "Two similar actors overlap, grapple, cross, or enter a high-effect interval.", "Two actors become one, one becomes two, or limbs are assigned to the wrong body.", "Instance binding collapses when silhouettes and appearance cues overlap.", "L4", "Use distinct wardrobe/color/depth lanes, avoid crossings, supply separate masks or pose tracks, and split grapples into readable contact beats.", "metric_actor_count_consistency", "B002 B018 B019 B041 B043", "high"),
        spec("role_swap", "Attacker-defender or speaker-role swap", "Actors have similar appearance or cross screen positions during a dependent action.", "The wrong actor attacks, reacts, speaks, holds the prop, or receives the effect.", "Role semantics are not anchored to persistent actor IDs and action bindings compete.", "L2", "Bind every event to initiator_id and target_id, preserve role labels through the event graph, and verify action-to-actor assignment.", "metric_role_assignment_accuracy", "B002 B017 B027 B033 B043", "high"),
        spec("screen_side_identity_swap", "Screen-side identity swap", "Actors cross, camera orbits, reverse angles are used, or a shot cuts across the axis.", "The left actor becomes the right actor without a declared crossing, or identities swap at the cut.", "Screen-side labels are confused with world identity and camera transform.", "L5", "Declare world IDs separately from screen lanes, preserve the action axis, and insert a neutral/re-establishing shot before a side reversal.", "metric_screen_side_consistency", "B002 B031 B035 B040", "high"),
        spec("target_confusion", "Action target confusion", "More than one plausible target is visible or interaction lines cross.", "An attack, gaze, handoff, effect, or dialogue response lands on the wrong target.", "Attention binding does not uniquely resolve the event participant graph.", "L2", "Declare target_id, target region, exclusion targets, and temporal isolation; use bounding/layout controls when multiple candidates remain close.", "metric_target_assignment_accuracy", "B002 B033 B038 B043", "high"),
        spec("voice_identity_drift", "Voice identity drift", "Multi-character dialogue spans shots or overlaps with off-screen speech.", "Voice timbre, language, accent, or speaker assignment changes.", "Audio identity is not persistently linked to the visual entity and turn order.", "L3", "Bind voice references and speaker IDs, encode turn order, and separate speech generation/dubbing when exact identity is required.", "metric_voice_identity_consistency", "B022 B023 B046 M004 M019", "moderate"),
    ],
    "D": [
        spec("left_right_frame_confusion", "Viewer-, actor-, and world-left confusion", "A prompt uses left/right without naming the coordinate frame.", "Motion or placement occurs in the opposite direction.", "Natural language under-specifies whether direction is viewer-, camera-, actor-, or world-relative.", "L2", "Normalize every direction to an explicit coordinate frame and compile provider prose from canonical screen/world coordinates.", "metric_screen_direction_consistency", "B002 B031 B035 B037", "high"),
        spec("axis_reversal_after_cut", "Axis reversal after cut", "A reverse angle, orbit, or cut changes camera side during two-actor action.", "Attack direction, gaze, or travel reverses without an authored crossing.", "The 180-degree action axis is not represented as persistent world geometry.", "L5", "Lock the action axis, prohibit unmotivated camera-side crossing, or insert a neutral bridge shot that re-establishes geography.", "metric_screen_direction_consistency", "B031 B035 B037 B040", "high"),
        spec("depth_order_inversion", "Depth-order inversion", "Actors or props overlap, camera parallax is weak, or effects obscure boundaries.", "Foreground/background ordering flips or an actor passes through another layer.", "Depth is inferred ambiguously from 2D appearance without an explicit depth map or lane.", "L4", "Use depth lanes, masks, depth maps, and minimum-separation constraints; verify ordering at overlap frames.", "metric_depth_order_accuracy", "B016 B018 B036 B037", "moderate"),
        spec("trajectory_target_miss", "Trajectory misses target region", "A fast actor/object follows a curved, airborne, or partially hidden path.", "The subject lands, strikes, or exits at the wrong region.", "Text describes intent but not a measurable spatiotemporal path.", "L4", "Provide point/pose trajectory or storyboard keyframes with time-indexed target regions; fail to shot decomposition when tolerance is tight.", "metric_trajectory_target_error", "B019 B020 B036 B038", "high"),
        spec("entrance_exit_mismatch", "Entrance and exit mismatch", "A subject leaves one shot and enters another after a camera change.", "Entry side, direction, scale, or depth lane conflicts with the previous exit.", "Shot-local coordinates are not transformed through a shared world state.", "L2", "Record exit world state and compile the next shot's entrance through the camera transform; verify directional continuity.", "metric_screen_direction_consistency", "B003 B015 B031 B040", "moderate"),
        spec("eyeline_mismatch", "Eyeline and gaze-target mismatch", "Dialogue or reaction shots isolate actors in close-up.", "Actors look to the wrong side or at the wrong height/depth.", "Gaze target is omitted or screen geometry is reconstructed independently per shot.", "L3", "Bind gaze_target_id and screen target, use matching reference frames, and verify gaze ray/target intersection with human calibration.", "metric_eyeline_consistency", "B031 B033 B040", "moderate"),
    ],
    "E": [
        spec("action_omission", "Primary action omission", "The clip contains many requested events or dependent beats.", "One or more required actions never occur.", "Finite temporal/attention capacity causes lower-priority actions to be dropped.", "L5", "Reduce to one primary event chain per shot, preserve hard events, and generate separate clips when a provider-specific density staircase fails.", "metric_action_omission_rate", "B002 B003 B027 B039 B043", "high"),
        spec("action_merge", "Sequential actions merged into one gesture", "Two or more similar actions occur close together or share actors/effect language.", "Setup, action, consequence, or recovery collapse into a single ambiguous movement.", "The generator compresses semantically related tokens into one visual event.", "L2", "Use explicit event nodes with non-overlapping intervals and prerequisite edges; include visible setup and settle beats.", "metric_action_graph_agreement", "B003 B017 B027 B029 B033", "high"),
        spec("action_repeat", "Unrequested action repetition", "Unused duration remains after the main action or a cyclic motion prior is strong.", "A strike, gesture, step, or camera move repeats.", "The model fills time with locally plausible motion and lacks an explicit terminal hold/state.", "L1", "Specify the end state and hold duration positively; shorten the generation or freeze the terminal interval in editing.", "metric_primary_action_completion", "B003 B027 B033", "moderate"),
        spec("event_order_reversal", "Event-order reversal", "The prompt uses compressed clauses or several dependent events.", "Reaction precedes cause, impact precedes approach, or recovery precedes landing.", "Text order is not a guaranteed executable temporal graph and evaluator models may also miss the reversal.", "L2", "Topologically sort an explicit event graph and compile causal phrases; verify event timestamps with human calibration for fast actions.", "metric_temporal_event_error", "B003 B027 B029 B033 B039", "high"),
        spec("recovery_omission", "Recovery or settle omission", "A dynamic action consumes most clip duration.", "The actor never lands, regains balance, lowers the arm, or reaches the requested end state.", "The model allocates duration to salient apex motion and truncates low-salience recovery.", "L5", "Reserve an explicit recovery interval or separate recovery shot; use first/last frames only when the path remains plausible.", "metric_recovery_presence", "B003 B004 B032", "high"),
        spec("simultaneity_collapse", "Sequential events become simultaneous", "Multiple actors act concurrently with causal dependencies.", "Mutually dependent actions happen at once or turn order disappears.", "The generation conditions do not enforce partial order under dense multi-actor motion.", "L5", "Serialize actor turns into separate beats or shots; keep only genuinely simultaneous actions in one interval.", "metric_action_graph_agreement", "B002 B003 B027 B039 B043", "high"),
    ],
    "F": [
        spec("effect_before_cause", "Effect occurs before cause", "A splash, recoil, debris burst, sound, or camera shake accompanies a fast action.", "The effect begins before contact or near-contact.", "The effect token is strongly associated with the action but not anchored to its causal frame.", "L2", "Declare cause, contact/near-contact frame, effect onset, reaction delay, and recovery as separate event nodes.", "metric_reaction_latency", "B004 B005 B027 B033 B045", "high"),
        spec("effect_without_cause", "Effect without a valid cause", "The prompt contains effect imagery but omits the generating interaction or permits filler.", "Debris, water, recoil, shake, or damage appears spontaneously.", "The model satisfies salient effect semantics independently of physical preconditions.", "L2", "Gate every effect by a named causal event and reject effects whose preconditions are absent; move ornamental effects to post.", "metric_causal_edge_agreement", "B004 B005 B025 B027 B045", "high"),
        spec("wrong_effect_origin", "Effect originates at the wrong location", "The cause and effect are spatially separated or one actor is occluded.", "Splash, dust, sparks, or debris emit from the actor instead of the impact point.", "The event graph lacks a persistent origin anchor or the model binds effect to the salient subject.", "L4", "Bind effect_origin to a world/screen region or mask; composite the effect at a tracked point when exact origin matters.", "metric_effect_origin_error", "B005 B019 B020 B038", "high"),
        spec("wrong_reactor", "Wrong actor reacts", "Several actors are nearby, roles cross, or impact is partly hidden.", "A non-target recoils, falls, or speaks.", "Target binding is ambiguous and reaction semantics are generated independently.", "L2", "Bind initiator, target, reaction actor, and excluded reactors in the causal graph; isolate the reaction shot if needed.", "metric_target_assignment_accuracy", "B002 B027 B033 B038", "high"),
        spec("reaction_latency_error", "Reaction latency error", "Contact is fast, stylized, obscured, or audio-linked.", "Reaction is anticipatory, excessively delayed, or temporally disconnected.", "No explicit causal latency interval constrains the generated motion.", "L2", "Encode onset, apex, consequence onset, acceptable latency range, and recovery; verify at frame level.", "metric_reaction_latency", "B004 B029 B032 B046", "moderate"),
        spec("secondary_effect_chain_break", "Secondary-effect chain break", "One impact should create several ordered consequences.", "Primary contact occurs but fluid, debris, sound, camera impulse, or environmental response is missing or unordered.", "Long causal chains exceed reliable event binding and secondary effects compete for attention.", "L5", "Split the primary interaction from secondary VFX/audio or composite them from tracked anchors; verify each causal edge independently.", "metric_causal_edge_agreement", "B005 B025 B027 B038 B045", "high"),
    ],
    "G": [
        spec("false_contact", "False contact", "Two actors approach rapidly or projected silhouettes overlap.", "A hit or grasp is implied although world-space separation remains large.", "Screen overlap is mistaken for physical contact and perspective masks depth.", "L4", "Specify near-contact versus contact, target region, minimum/maximum distance, and camera-cheated overlap; use pose/depth controls for exact interaction.", "metric_contact_distance_error", "B004 B016 B032 B038", "high"),
        spec("missing_contact", "Missing required contact", "A handoff, grasp, support, strike, or landing is partly occluded or fast.", "Bodies or objects stop short, float apart, or pass without touching.", "Contact is a short low-duration constraint with weak frame-level supervision.", "L4", "Provide a contact keyframe/pose, reserve readable approach and consequence frames, and verify the target region at the declared contact interval.", "metric_contact_target_accuracy", "B004 B032 B036 B038", "high"),
        spec("body_penetration", "Body or limb penetration", "Close combat, grapples, crossed limbs, or rapid camera motion reduce silhouette separation.", "Limbs pass through torsos, actors interpenetrate, or body ownership becomes ambiguous.", "The 2D generator lacks hard 3D collision constraints and instance boundaries overlap.", "L4", "Use pose/depth/mask controls, maintain silhouette readability, or stage camera-cheated near-contact and add impact effects in post.", "metric_penetration_duration", "B016 B018 B019 B032", "high"),
        spec("grip_drift", "Grip and support drift", "A hand carries, turns, or supports a prop across motion.", "Grip point slides, fingers detach, or the object changes orientation independently.", "Grasp/contact is not modeled as a persistent constraint across frames.", "L4", "Track grip anchor and object transform, use source-video/pose guidance, and isolate the manipulation shot.", "metric_contact_distance_error", "B019 B020 B032 B038", "high"),
        spec("wrong_contact_target", "Incorrect contact body part or region", "A prompt states a general hit/grab without a spatial target.", "Contact lands on the wrong limb, side, or object region.", "Language describes event category but not target geometry.", "L2", "Encode target_region in actor-local coordinates plus allowed screen tolerance; use a contact keyframe for precise choreography.", "metric_contact_target_accuracy", "B002 B033 B038", "moderate"),
        spec("interaction_distance_drift", "Interaction-distance drift", "Dialogue, handoffs, dances, or combat continue during dolly/zoom/orbit motion.", "Actors become too close/far or collision distance changes without locomotion.", "Camera-scale changes are entangled with inferred world-space spacing.", "L4", "Separate world distance from screen size, constrain actor trajectories, and verify with depth/pose estimates plus human review.", "metric_contact_distance_error", "B031 B035 B037", "moderate"),
    ],
    "H": [
        spec("foot_skating", "Foot skating", "Walking, pivots, landings, or stance holds occur while the camera or background moves.", "A planted foot slides relative to the surface.", "Generated limb motion and global translation are not constrained by a persistent contact point.", "L4", "Use pose/source-video guidance, encode planted-foot intervals, and measure foot-to-ground optical-flow residual.", "metric_foot_slip_distance", "B021 B032", "high"),
        spec("missing_support", "Missing support foot or base of support", "A body leans, kicks, carries weight, or changes direction.", "The body floats or remains stable without a supporting foot/hand/contact.", "Support state and center-of-mass relation are absent from the condition.", "L2", "Encode support contacts and transfer order; require a readable base of support or use source-motion control.", "metric_support_state_consistency", "B004 B025 B032 B044", "high"),
        spec("weightless_takeoff_landing", "Weightless takeoff or landing", "Jumping, diving, falling, or anime launches involve large vertical motion.", "No compression/push-off, acceleration, impact, deceleration, or settle is visible.", "The model prioritizes trajectory appearance over force-bearing phases.", "L5", "Separate anticipation, takeoff, flight, contact, deceleration, and settle; retain a causal skeleton even under stylization.", "metric_landing_stability", "B004 B005 B032 B044 B045", "high"),
        spec("momentum_discontinuity", "Momentum disappearance or reversal", "A fast actor/object changes direction, collides, or crosses an edit.", "Velocity changes instantly or momentum vanishes between frames.", "No explicit velocity/impulse state persists across the event or cut.", "L4", "Use trajectory/control video and encode pre/post velocity plus impulse event; split at impact for compositing when needed.", "metric_momentum_discontinuity", "B004 B005 B025 B044 B045", "high"),
        spec("constant_speed_motion", "Constant-speed motion without acceleration profile", "A fall, swing, throw, or recoil is described only by endpoints.", "Motion traverses the path at visually uniform speed.", "Endpoint or semantic conditioning lacks an authored timing/easing profile.", "L2", "Encode anticipation, acceleration, apex, deceleration, overshoot, and settle timing; verify phase durations.", "metric_momentum_discontinuity", "B003 B032", "moderate"),
        spec("impossible_recovery", "Impossible recovery or balance regain", "An actor lands off-center, is struck, or changes direction sharply.", "The actor instantly returns to a stable pose without corrective steps or support transfer.", "Recovery is low-salience and the model samples a canonical stable pose.", "L5", "Reserve recovery time, specify corrective support steps, or end the shot at impact and generate recovery separately.", "metric_landing_stability", "B004 B032 B044", "high"),
    ],
    "I": [
        spec("solid_fluid_boundary_error", "Solid-fluid boundary error", "An actor enters, strikes, stands on, or emerges from water/mud/snow.", "Fluid behaves as a rigid plane or fails to admit/displace the body.", "The model lacks explicit material-state and boundary-condition constraints.", "L5", "Separate pre-contact, contact/effect, and submerged/post-contact shots; use source/control media or composite the fluid interaction.", "metric_material_response_consistency", "B004 B005 B025 B027 B045", "high"),
        spec("splash_before_displacement", "Splash before displacement", "A fast body or object approaches water and the splash is salient in the prompt.", "The splash begins before surface contact.", "Effect semantics are associated with entry but not tied to a contact frame.", "L2", "Bind surface contact, displacement onset, splash onset, and ripple onset to ordered causal events.", "metric_reaction_latency", "B004 B005 B027 B045", "high"),
        spec("splash_origin_drift", "Splash or water column follows the actor", "An actor dives away while another impact creates a water column.", "The effect follows the hidden actor or originates from the wrong point.", "The effect is bound to the most salient subject rather than the causal impact anchor.", "L4", "Track the impact point with a mask/point and composite or regenerate the localized effect independently.", "metric_effect_origin_error", "B019 B020 B027 B038", "high"),
        spec("submerged_subject_disappearance", "Submerged subject disappearance", "A character passes below an opaque or reflective surface.", "The subject vanishes permanently, duplicates, or returns without a continuous path.", "Complete occlusion removes all identity and trajectory evidence.", "L4", "Keep bubbles, silhouette, refraction cue, mask, or trajectory control; otherwise cut on entry and establish the underwater shot from a reference state.", "metric_hidden_path_consistency", "B013 B014 B017 B027", "high"),
        spec("material_effect_anatomy_spawn", "Material effect spawns anatomy or duplicate faces", "Dense splash, smoke, cloth, hair, or debris overlaps a face/body.", "Faces, hands, limbs, or bodies appear inside the effect.", "Texture and anatomy priors become entangled in ambiguous high-frequency regions.", "L6", "Render the effect as a separate layer or add it in post; preserve actor masks and verify actor count before compositing.", "metric_actor_count_consistency", "B016 B018 B032", "moderate"),
        spec("environment_material_state_drift", "Material topology or persistence drift", "Waterline, mud, snow, debris, cloth damage, or wetness persists across time/cuts.", "Surface height, ripple center, wetness, tear, or debris state resets or moves.", "Material state is not carried in a persistent ledger and effects outlive or detach from causes.", "L3", "Record material state deltas, anchor effect regions, and use continuity plates or postproduction for persistent damage/wetness.", "metric_surface_topology_stability", "B003 B010 B027 B028", "moderate"),
    ],
    "J": [
        spec("pan_becomes_actor_motion", "Camera pan becomes actor translation", "The prompt combines a pan with actor locomotion or static blocking.", "The actor slides across the world or background instead of the camera rotating.", "Camera and object motion are entangled in the learned representation.", "L4", "Represent camera pose and actor world trajectory separately; use camera-control media or source-video motion.", "metric_camera_motion_agreement", "B031 B035 B037", "high"),
        spec("tracking_freezes_locomotion", "Tracking shot freezes actor locomotion", "A camera should follow a moving actor at stable framing.", "The actor appears stationary while the background moves, or gait collapses.", "Screen-space constancy is mistaken for world-space immobility.", "L4", "Encode world locomotion and camera follow as separate tracks; verify foot motion and background parallax.", "metric_actor_world_trajectory", "B021 B031 B035", "high"),
        spec("orbit_reverses_screen_direction", "Orbit reverses screen direction", "The camera orbits around two actors during directional action.", "Left-to-right action flips or roles swap.", "Camera-side crossing changes projection while the canonical action axis is not preserved.", "L5", "Do not combine an orbit with exact two-actor choreography unless camera-pose control is available; split or re-establish the axis.", "metric_screen_direction_consistency", "B031 B035 B037", "high"),
        spec("zoom_dolly_confusion", "Zoom and dolly confusion", "The prompt asks for zoom, push-in, dolly, or Hitchcock-style motion.", "Perspective/parallax and subject scale change incorrectly.", "Intrinsic lens change and extrinsic camera translation are visually confusable and evaluators also have blind spots.", "L4", "Use explicit camera intrinsics/extrinsics or a source/control video; validate parallax, subject scale, and background expansion separately.", "metric_zoom_translation_disambiguation", "B031 B037", "high"),
        spec("impact_shake_deforms_subject", "Impact shake deforms or teleports subjects", "Handheld shake or impact impulse coincides with contact/effect.", "Bodies warp, location jumps, or motion blur rewrites identity.", "Global frame perturbation is entangled with object deformation and the contact interval is already ambiguous.", "L6", "Generate a stable plate and add camera shake in post, or apply controlled V2V to the final shot.", "metric_identity_continuity", "B016 B031 B032", "high"),
        spec("motion_blur_identity_loss", "Motion blur destroys identity and geometry", "Whip pans, fast limbs, smears, or low shutter cues cover key frames.", "Faces/limbs melt, duplicate, or reconnect incorrectly.", "Blur removes high-frequency identity and boundary cues during high motion.", "L5", "Keep the decisive contact/recovery readable, shorten blur intervals, add authored blur/smears in post, or provide source motion.", "metric_identity_continuity", "B016 B019 B032", "high"),
    ],
    "K": [
        spec("flash_misread_as_cut", "Impact flash misread as a camera cut", "A full-frame white/black/monochrome flash interrupts action.", "The model resets scene, identity, pose, or location after the flash.", "A graphic discontinuity resembles a shot boundary in training data.", "L6", "Generate continuous action without the flash and insert a one-frame graphic flash in post; verify pre/post state identity.", "metric_cut_flash_classification", "B003 B015 B033", "high"),
        spec("smoke_splash_wipe_scene_reset", "Effect wipe causes scene reset", "Smoke, splash, speed lines, or transformation effects cover the whole frame.", "A new background, costume, pose, or actor arrangement appears.", "Opaque effect interval is interpreted as permission for a new scene sample.", "L5", "Treat the wipe as an edit boundary with explicit outgoing/incoming state or composite it between separately verified plates.", "metric_post_cut_state_consistency", "B012 B015 B027", "high"),
        spec("hard_cut_state_reset", "Hard cut resets world state", "A multi-shot prompt revisits actors/objects after a cut.", "Object, injury, wardrobe, direction, or environment state regresses.", "Shots are generated with insufficient shared entity/world memory.", "L3", "Use shot-level state snapshots, shared references, and explicit continuity inheritance; generate shots separately when provider multi-shot control is weak.", "metric_post_cut_state_consistency", "B015 B027 B028 B040", "high"),
        spec("whip_pan_teleport", "Whip-pan teleport", "A whip pan bridges positions or shots.", "Actors teleport, swap sides, or disappear during the blur.", "The hidden interval combines camera ambiguity and subject occlusion.", "L6", "Create outgoing and incoming plates with matched motion direction, then add the whip blur/edit in post.", "metric_screen_direction_consistency", "B012 B031", "high"),
        spec("transformation_burst_unintended_redesign", "Transformation burst redesigns forbidden attributes", "A transformation or energy burst permits only a specific state change.", "Identity, costume, body, or environment changes beyond the authorized delta.", "The effect activates broad transformation priors without a constrained change set.", "L2", "Declare allowed and forbidden state deltas and provide the required post-transform reference frame; verify every locked attribute.", "metric_state_transition_accuracy", "B003 B010 B015", "moderate"),
        spec("multi_shot_temporal_jump", "Multi-shot temporal jump or duplicate beat", "A model generates several shots inside one clip.", "Events repeat, time skips, or a shot shows a contradictory phase.", "Shot segmentation and event graph are not explicitly aligned.", "L5", "Assign each shot a closed event interval and handoff state; compile/generate separately if the provider cannot expose shot-level control.", "metric_action_graph_agreement", "B003 B015 B027 B040", "high"),
    ],
    "L": [
        spec("extra_missing_limbs", "Extra or missing limbs", "Fast action, overlap, blur, cloth, hair, or foreshortening hides joints.", "An extra limb appears, a limb disappears, or ownership changes.", "Ambiguous silhouettes and compressed spatiotemporal representation weaken anatomical correspondence.", "L4", "Use pose/source-video guidance, maintain limb separability, and reserve anatomy recovery checkpoints.", "metric_anatomical_validity", "B016 B018 B032 B042", "high"),
        spec("joint_inversion", "Joint inversion or impossible articulation", "Extreme pose, rapid rotation, or stylized perspective challenges joint geometry.", "Elbows, knees, wrists, or spine bend incorrectly.", "The generator prioritizes local appearance and motion over biomechanical constraints.", "L4", "Use pose constraints or source motion and verify joint-angle plausibility; simplify the pose when detectors and humans disagree.", "metric_anatomical_validity", "B032", "high"),
        spec("persistent_smear_anatomy", "Smear deformation persists beyond the accent", "Anime smear frames or motion trails are requested.", "Elongated limbs, duplicated features, or distorted body shapes remain after the intended smear.", "The model lacks an explicit recovery frame and treats stylization as a continuing state.", "L3", "Define deformation onset/end and a required anatomy recovery keyframe; add one-frame smears in post when exact duration is required.", "metric_recovery_frame_accuracy", "B010 B016 B032", "moderate"),
        spec("perspective_deformation_persists", "Perspective enlargement persists", "A fist, foot, or face moves close to lens for a stylized accent.", "The enlarged body part stays disproportionate after moving away.", "Perspective effect is absorbed into entity appearance rather than a transient camera-relative deformation.", "L3", "Bind deformation to camera distance and interval, then require a normal-proportion recovery state.", "metric_deformation_duration", "B016 B031 B032", "moderate"),
        spec("failed_anatomy_reconnection", "Failed anatomy reconnection after occlusion", "Limbs cross behind body/cloth/effects and re-emerge.", "A limb reconnects to the wrong side or body.", "Occluded joints lose persistent identity and local correspondence.", "L4", "Use joint/pose tracks, partial visibility anchors, and a post-occlusion anatomy checkpoint.", "metric_anatomical_validity", "B013 B019 B032", "high"),
        spec("stylization_readability_loss", "Stylization destroys action readability", "Smears, holds, speed lines, flashes, and deformation stack in the same interval.", "The primary pose, target, direction, or contact cannot be read.", "Multiple graphic accents compete with the causal skeleton and silhouette.", "L5", "Retain one readable setup, contact/apex, and recovery pose; distribute accents across shots or post layers.", "metric_silhouette_readability", "B001 B010 B032", "moderate"),
    ],
    "M": [
        spec("structured_format_not_parsed", "Structured serialization treated as ordinary text", "XML, YAML, or JSON is submitted to an endpoint that documents only a prompt string.", "Field boundaries, nesting, keys, or numeric values are ignored inconsistently.", "The provider has no documented schema parser; structure only changes token sequence and semantic emphasis.", "L1", "Keep JSON as CPCS authority, compile one concise provider-native prose prompt, and treat structured serialization as an experiment unless officially supported.", "metric_prompt_semantic_equivalence", "R005 M001 M002 M007", "high"),
        spec("duplicate_representation_attention_collision", "Duplicate-format attention collision", "The same semantics are repeated in prose, XML, JSON, and YAML.", "Instructions conflict, fields are omitted, or motion becomes stiff/averaged.", "Redundant tokens consume prompt budget and introduce slight semantic differences and priority competition.", "L1", "Compile exactly one provider-facing representation plus non-submitted verification metadata; A/B-test hybrids instead of assuming benefit.", "metric_instruction_coverage", "R005 B002 B039", "moderate"),
        spec("numeric_control_ignored", "Exact numeric values ignored or approximated", "Timestamps, angles, speeds, coordinates, or distances are placed only in text.", "The output follows qualitative intent but not the requested numbers.", "Prompt-string conditioning is semantic, not an executable trajectory or simulation constraint.", "L4", "Project numbers to provider controls when documented; otherwise retain them for verification and use control media or postproduction.", "metric_field_projection_coverage", "R004 R006 M001 B035 B037", "high"),
        spec("negative_prompt_concept_priming", "Negative instruction introduces or preserves forbidden content", "The prompt repeatedly names forbidden objects/actions/effects.", "The forbidden concept appears or attention is diverted from positive target behavior.", "Negation handling is provider-specific and the named concept remains present in the condition.", "L0", "Prefer a positive replacement state and provider-specific negative field only when documented; do not generalize deprecated-model guidance.", "metric_hard_lock_retention", "M001 M023", "low"),
        spec("prompt_rewrite_semantic_loss", "Provider prompt rewriting changes canonical intent", "The endpoint silently enhances or rewrites a short prompt.", "New actions/details appear, priorities shift, or hard locks weaken.", "An opaque secondary model transforms the submitted semantics before generation.", "L1", "Disable rewriting where possible, record the setting, hash the exact request, and reject providers that cannot preserve hard-lock meaning for critical shots.", "metric_prompt_semantic_equivalence", "M025 R006 R007", "moderate"),
        spec("prompt_budget_truncation", "Prompt-budget overflow or truncation", "Long nested prompts exceed provider or aggregator limits.", "Late constraints, end state, or forbidden variation disappear.", "Transport or adapter truncation loses low-position fields and no canonical loss report is enforced.", "L1", "Compile by priority, never drop hard locks, emit an explicit loss report, and split the shot when minimum sufficient semantics do not fit.", "metric_prompt_truncation_loss", "M002 M007 R006 R008", "high"),
    ],
    "N": [
        spec("overconstraint_priority_dilution", "Overconstraint and priority dilution", "Too many exact actions, camera moves, effects, spatial locks, and negatives share one clip.", "Motion stiffens, instructions are randomly ignored, or the scene fails to complete.", "Competing conditions exceed practical attention and temporal capacity.", "L5", "Classify hard/soft/evaluation-only controls, remove duplicated semantics, and decompose the shot when calibrated complexity limits are exceeded.", "metric_instruction_coverage", "B002 B003 B039 B043", "high"),
        spec("under_specified_filler", "Under-specified filler action", "The prompt defines a start and one action but leaves duration/end state open.", "The model adds gestures, attacks, dialogue, effects, or scene changes.", "Stochastic generation fills unassigned time with likely motion.", "L1", "Declare terminal state, hold behavior, allowed variation, and forbidden new primary actions; shorten duration.", "metric_hallucinated_action_rate", "B003 B027 B033", "high"),
        spec("contradictory_constraints", "Contradictory canonical constraints", "Two profiles or representations demand incompatible positions, motion, camera, or timing.", "The model averages, selects randomly, or produces broken geometry.", "Conflict is passed to the provider instead of resolved by the compiler.", "L2", "Fail closed at compile time, expose the conflict, and require one explicit resolution before provider submission.", "metric_constraint_conflict_count", "R006 R007 B039", "high"),
        spec("action_density_overflow", "Action-density overflow", "Many dependent events are packed into a short clip.", "Actions merge, omit, reverse, or lose recovery.", "Required event duration exceeds provider/task capacity.", "L5", "Run a provider-specific staircase to estimate capacity; split before the first statistically reliable failure point instead of using a universal actions-per-second rule.", "metric_primary_action_completion", "B003 B027 B039", "high"),
        spec("multi_actor_complexity_overflow", "Multi-actor interaction overload", "Several actors have simultaneous, crossing, or contact-heavy actions.", "Role swaps, count drift, fusion, and target confusion increase together.", "Entity, role, spatial, and temporal bindings compete in the same interval.", "L5", "Reduce simultaneous actors/actions, enforce lanes, and use separate shots or source/control video for dense choreography.", "metric_role_assignment_accuracy", "B002 B041 B043", "high"),
        spec("camera_effect_choreography_overflow", "Camera, VFX, and choreography overload", "Complex camera motion, actor interaction, material effects, and edits coincide.", "The system sacrifices motion, identity, geography, or effect causality.", "Multiple high-variance generators are entangled without independent control channels.", "L6", "Generate stable choreography first, then apply camera/VFX/edit layers through controlled V2V or postproduction.", "metric_instruction_coverage", "B031 B035 B037 B038", "high"),
    ],
    "O": [
        spec("impact_sound_offset", "Impact sound temporal offset", "A fast contact or near-contact should trigger a sound.", "Sound precedes or lags the visual event beyond tolerance.", "Joint generation or later audio synthesis lacks a shared event anchor.", "L2", "Use canonical audio event anchors tied to visual event IDs and verify onset offset; replace sound in post when timing is critical.", "metric_audio_visual_temporal_offset", "B022 B023 B046", "high"),
        spec("lip_speech_mismatch", "Lip-speech mismatch", "Dialogue contains phonetic complexity, profile view, fast cuts, or multiple speakers.", "Mouth motion does not match speech timing/content.", "Audio and facial motion are weakly aligned or speaker assignment changes.", "L4", "Use a driving performance/dedicated lip-sync system or generate clean visuals and dub; measure temporal and phonetic agreement separately.", "metric_lip_speech_consistency", "B023 B024 M004 M019", "high"),
        spec("sound_without_visual_cause", "Sound without visual cause", "Joint generation is asked for ambience/effects while actions are ambiguous.", "An impact, splash, step, or mechanical sound occurs without the event.", "Audio semantics are generated independently from visual causal satisfaction.", "L2", "Bind every foreground sound to a visual event or explicitly classify it as off-screen/ambient.", "metric_audio_visual_semantic_match", "B022 B023 B046", "high"),
        spec("visual_event_without_sound", "Visual event lacks required sound", "A salient impact, splash, door, or speech event occurs.", "Expected audio is absent or masked.", "The model satisfies visual semantics but omits a lower-salience audio consequence.", "L6", "Retain event metadata and synthesize/mix deterministic sound in post; verify presence and onset.", "metric_audio_visual_semantic_match", "B022 B023 B046", "moderate"),
        spec("speaker_voice_drift", "Speaker or voice drift", "Multi-shot or multi-speaker dialogue changes camera view or scene.", "Voice identity, language, accent, or turn assignment changes.", "Voice embeddings/identity are not persistently bound across shots.", "L3", "Use speaker-specific voice references and turn IDs; separate dialogue production from video generation when exact casting matters.", "metric_voice_identity_consistency", "B023 M004 M019", "moderate"),
        spec("music_action_accent_misalignment", "Music or beat accent misalignment", "Choreography, cuts, or impacts must land on musical beats.", "Visual apex/cut occurs off beat.", "Textual BPM/beat instructions do not create an executable shared timeline.", "L4", "Use a timecoded beat map/control track and edit generated clips to the beat; verify event-to-beat offset.", "metric_audio_visual_temporal_offset", "B022 B023 B046", "high"),
    ],
    "P": [
        spec("vlm_misses_fast_action", "VLM misses or reorders fast action", "Contact, flashes, smears, or events occupy very few frames.", "The evaluator omits the event or reports the wrong order.", "Sparse frame sampling and static visual shortcuts fail to capture temporal logic.", "L2", "Use high-rate interval extraction, atomic questions, detector evidence, and human review for fast decisive events.", "metric_false_negative_rate", "B017 B029 B033", "high"),
        spec("vlm_invents_contact", "VLM invents contact from screen overlap", "Perspective or blur makes actors overlap without physical contact.", "Evaluator marks a hit/grasp that did not occur.", "Semantic priors and 2D overlap substitute for geometric evidence.", "L4", "Require pose/depth/distance evidence and human calibration; do not let semantic verdict alone decide contact.", "metric_false_positive_rate", "B017 B025 B029 B033", "high"),
        spec("tracker_identity_swap", "Tracker or segmenter swaps actor identity", "Actors overlap, cross, wear similar clothing, or become occluded.", "Continuity metric reports a false teleport, duplicate, or role swap.", "Perception tracker loses identity under ambiguity.", "L2", "Calibrate on the exact domain, combine appearance/trajectory/role cues, expose uncertainty, and require human review on swaps.", "metric_evaluator_calibration", "B013 B018 B019 B020", "high"),
        spec("shot_detector_flash_false_positive", "Shot detector mistakes flash or smear for cut", "Full-frame graphic effects produce abrupt histogram changes.", "Evaluator reports a cut and state discontinuity that were not authored.", "Low-level shot detection treats graphic discontinuity as edit discontinuity.", "L2", "Classify cut, flash, hold, blur, and occlusion separately and calibrate with authored effect fixtures.", "metric_cut_flash_classification", "B030 B033", "moderate"),
        spec("pose_metric_stylization_failure", "Pose/anatomy metric fails on anime or stylization", "Bodies use smears, holds, foreshortening, nonhuman proportions, or partial visibility.", "Evaluator flags intentional style or misses real anatomy breakage.", "Pose models are out of distribution and confidence is not propagated.", "L2", "Use style-specific calibration, silhouette and temporal recovery metrics, plus human review; never treat one pose model as truth.", "metric_evaluator_calibration", "B032 B034", "high"),
        spec("aggregate_metric_hides_local_failure", "Aggregate score hides a decisive localized failure", "Most frames look good but one contact, identity, count, or causal event is wrong.", "High average quality score passes an unusable render.", "Global metrics dilute sparse but production-critical failures.", "L2", "Evaluate canonical assertions per interval and hard-lock dimension; block on any critical assertion regardless of aggregate score.", "metric_human_agreement", "B001 B008 B009 B030 B034", "high"),
    ],
}


def mitigation_record(
    level: str,
    method: str,
    expected_benefit: str,
    verification_metric_ids: list[str],
    evidence_strength: str,
    limitations: list[str] | None = None,
    token_cost: str = "low-to-medium",
    generation_cost: str = "none-to-one additional candidate",
    new_failure_risk: str = "May dilute other controls if added without compression.",
    provider_dependency: str = "provider capability and adapter dependent",
    rollback: str = "Restore the prior canonical score/build and preserve the failed candidate as immutable evidence.",
) -> dict[str, Any]:
    return {
        "level": level,
        "level_name": MITIGATION_LEVELS[level],
        "method": method,
        "expected_benefit": expected_benefit,
        "token_or_character_cost": token_cost,
        "generation_cost_impact": generation_cost,
        "risk_of_new_failure": new_failure_risk,
        "provider_dependency": provider_dependency,
        "evidence_strength": evidence_strength,
        "verification_method": f"Re-run {', '.join(verification_metric_ids)} on paired seeds and retain per-seed outcomes.",
        "verification_metric_ids": verification_metric_ids,
        "rollback": rollback,
        "limitations": limitations or ["No intervention guarantees compliance on stochastic generators."],
    }


FAILURES: list[dict[str, Any]] = []


def add_failure(
    code: str,
    category: str,
    name: str,
    definition: str,
    triggers: list[str],
    symptoms: list[str],
    mechanisms: list[str],
    sources: list[str],
    canonical_paths: list[str],
    risk_patterns: list[str],
    primary: tuple[str, str, str],
    escalation: tuple[str, str, str],
    metrics: list[str],
    controllability: str,
    provider_notes: list[str] | None = None,
    unresolved: list[str] | None = None,
    severity: str = "high",
    likelihood_when_triggered: str = "unknown until provider-specific repeated-seed qualification",
    additional_mitigation: tuple[str, str, str] | None = None,
) -> None:
    slug = name.lower().replace("/", "_").replace("–", "_").replace("—", "_")
    slug = "_".join("".join(ch if ch.isalnum() or ch == "_" else " " for ch in slug).split())
    cause_names = {m["mechanism_id"]: m["name"] for m in MECHANISMS}
    evidence_class = "benchmark_result" if any(s.startswith("B") for s in sources) else "research_inference"
    mitigation_list = [
        mitigation_record(
            primary[0], primary[1], primary[2], metrics,
            "moderate-to-strong where supported by cited benchmark/control literature; provider-specific effect size unqualified",
        ),
        mitigation_record(
            escalation[0], escalation[1], escalation[2], metrics,
            "mechanistically strong control escalation; exact benefit requires live provider tests",
            token_cost="low prompt cost; medium asset preparation cost" if escalation[0] in {"L3", "L4"} else "low",
            generation_cost="additional asset preparation and/or multiple generated clips" if escalation[0] in {"L3", "L4", "L5", "L6"} else "one additional candidate",
            new_failure_risk="Can introduce boundary, compositing, reference-transfer, or motion-stiffness artifacts; verify all preserved controls.",
        ),
    ]
    if additional_mitigation:
        mitigation_list.append(
            mitigation_record(
                additional_mitigation[0], additional_mitigation[1], additional_mitigation[2], metrics,
                "fallback intervention; use only after the lower level fails its paired-seed gate",
                token_cost="minimal prompt cost; workflow cost may be high",
                generation_cost="localized regeneration, substitution, or postproduction",
                new_failure_risk="May change style, timing, or already-passing regions; full regression verification required.",
            )
        )
    record = {
        "failure_id": f"failure://{category.lower()}/{slug}/{code.lower()}",
        "failure_code": code,
        "name": name,
        "category": category,
        "definition": definition,
        "scope": {
            "providers": ["any stochastic generative-video system unless version-qualified otherwise"],
            "models": [],
            "workflows": ["text_to_video", "image_to_video", "reference_conditioned", "multi_shot"],
            "version_scope": "generic failure hypothesis; provider-specific incidence is unqualified",
        },
        "trigger_conditions": triggers,
        "observed_symptoms": symptoms,
        "suspected_causes": [
            {
                "mechanism_id": mid,
                "mechanism": cause_names[mid],
                "causal_status": "evidence-backed system inference; closed-model internals not directly verified",
            }
            for mid in mechanisms
        ],
        "evidence_class": evidence_class,
        "source_refs": sources,
        "empirical_confidence": "high that the failure class exists; provider/version frequency cannot be verified with 100% certainty without live repeated-seed trials",
        "severity": severity,
        "likelihood_when_triggered": likelihood_when_triggered,
        "canonical_fields_affected": canonical_paths,
        "prompt_risk_patterns": risk_patterns,
        "mitigations": mitigation_list,
        "verification_metrics": metrics,
        "regression_fixtures": [
            f"fixture://{code.lower()}/minimal_trigger",
            f"fixture://{code.lower()}/paired_control",
            f"fixture://{code.lower()}/escalated_control",
        ],
        "provider_specific_notes": provider_notes or [
            "Do not infer relative provider reliability from documented input capability.",
            "Pin provider, model/version, endpoint, prompt transformation settings, seed where exposed, duration, aspect ratio, and all reference assets.",
        ],
        "unresolved_questions": unresolved or [
            "What is the per-provider success distribution under matched prompts and paired seeds?",
            "Which intervention gives the largest adherence gain per generation dollar without regressing other hard locks?",
        ],
        "cpcs_impact": {
            "intent_normalization": "Preserve the requested invariant and classify ambiguity before compilation.",
            "profile_routing": f"Route to the {category} risk profile and provider capability filter.",
            "canonical_score": canonical_paths,
            "event_graph": "Add typed nodes/edges only when the failure involves event, causal, role, or transition semantics.",
            "spatial_state": "Carry declared coordinate frame and transition constraints when relevant.",
            "identity_ledger": "Use stable entity IDs and signatures whenever actors, voices, products, or props can be rebound.",
            "continuity_ledger": "Record precondition, allowed transition, postcondition, visibility interval, and forbidden changes.",
            "provider_capability_profile": "Record whether the provider can carry text, reference, keyframe, control-media, seed, repair, and audio requirements without silent loss.",
            "serialization_strategy": "Emit one provider-native authority representation; do not duplicate semantic authorities.",
            "prompt_compression": "Protect hard locks, causal edges, identities, start/end states, and visibility bridges before style adjectives.",
            "loss_report": "Report every unsupported, evaluation-only, compressed, or omitted control.",
            "verification_plan": metrics,
            "repair_planner": "Repair only the smallest failing interval/shot while preserving passing control IDs.",
            "experiment_registry": f"Register matched ablations for {code} with raw artifacts and immutable manifests.",
        },
        "finding_classification": ["contract_affecting", "implementation_affecting", "verification_affecting"],
        "controllability": controllability,
        "research_status": "literature-and-repository-grounded; live provider qualification pending",
    }
    FAILURES.append(record)


# A — Occlusion and hidden-state hallucination (7)
add_failure(
    "A01", "Occlusion and hidden state", "Hidden-state reconstruction hallucination",
    "A temporarily invisible subject is reconstructed into a different pose, state, or action rather than continued along the intended hidden path.",
    ["complete splash, smoke, flash, cloth, foreground, blur, darkness, submersion, or frame-exit occlusion", "hidden interval longer than a brief transient", "no visible bridge or control trajectory", "complex action occurs immediately before or after occlusion"],
    ["pose changes behind the occluder", "unrequested action appears", "subject exits or reappears inconsistently", "continuity looks plausible locally but violates the requested event"],
    ["mechanism://underdetermined_hidden_state", "mechanism://state_representation_gap"],
    ["B011", "B012", "B013", "B014", "B017"],
    ["continuity.visibility_intervals", "continuity.state_ledger", "actions", "constraints.continuity_locks", "verification_requirements"],
    ["'disappears in a splash' with no hidden trajectory", "effect name substitutes for explicit precondition/hidden path/postcondition", "long opaque interval followed by a dense action"],
    ("L2", "Compile an Occlusion Continuity Contract: subject ID, pre-state, start/end, hidden path, expected reappearance region, identity/count locks, allowed and forbidden state changes, and visibility bridge.", "Removes ambiguity from the canonical target and gives the verifier explicit checkpoints."),
    ("L4", "Provide a mask, point track, silhouette, pose trajectory, depth/trajectory control, or control video spanning the hidden interval.", "Carries information through the interval instead of asking text alone to preserve an unobserved state."),
    ["metric_occlusion_continuity", "metric_reappearance_position_error", "metric_identity_continuity", "metric_event_graph_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Split at a stable visible state before the occlusion and generate the effect/hidden transition as a separate shot or postproduction layer.", "Eliminates the need for one model sample to preserve an unobservable transition."),
)
add_failure(
    "A02", "Occlusion and hidden state", "Duplicate subject on reappearance",
    "The hidden subject reappears while a residual or newly generated copy remains, increasing actor count.",
    ["full-frame splash/smoke", "mirrors or reflections", "multiple similar actors", "occluder itself has face/limb-like texture", "re-entry from a frame edge"],
    ["extra face or limb in the effect", "two versions of the same actor", "reflection becomes independent", "actor count changes after the occlusion"],
    ["mechanism://underdetermined_hidden_state", "mechanism://entity_binding_ambiguity"],
    ["B011", "B013", "B015", "B017", "B018"],
    ["entities", "continuity.state_ledger", "continuity.visibility_intervals", "constraints.continuity_locks"],
    ["negative prompt only: 'no clones'", "unspecified reflection status", "complete occluder with no count checkpoint"],
    ("L2", "Hard-lock actor_count and entity IDs before, during, and after the interval; declare reflections/shadows as non-entity render phenomena.", "Turns actor count and reflection status into explicit invariants rather than prose preferences."),
    ("L3", "Use distinct actor reference sheets and a post-occlusion keyframe/storyboard showing exactly the intended count and layout.", "Anchors the reappearance state and reduces duplicate completion modes."),
    ["metric_actor_count_consistency", "metric_identity_continuity", "metric_occlusion_continuity"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Composite the occluding effect over a clean actor plate or remove duplicate regions with tracked masks.", "Makes count preservation deterministic when generation cannot maintain it."),
)
add_failure(
    "A03", "Occlusion and hidden state", "Identity mutation behind occlusion",
    "A subject preserves approximate role and position but changes face, hair, costume, body proportions, or species after being hidden.",
    ["long or complete occlusion", "weak or single-view reference", "similar cast", "transformation-like VFX", "style changes around the occlusion"],
    ["face/hair/costume drift", "body proportions change", "actor becomes a different character", "identity changes only after the effect"],
    ["mechanism://underdetermined_hidden_state", "mechanism://entity_binding_ambiguity", "mechanism://graphic_world_state_conflation"],
    ["B014", "B015", "B017"],
    ["entities", "continuity.state_ledger", "style", "constraints.continuity_locks", "assets"],
    ["'same character' without a stable entity signature", "transformation vocabulary when no transformation is allowed", "graphic effect and identity reset described together"],
    ("L2", "Compile a multimodal identity signature and forbid identity/costume/body-state transitions during the visibility interval.", "Defines identity from multiple nonfacial attributes and makes the absence of transformation explicit."),
    ("L3", "Supply separate face, full-body, costume, and reappearance references or a first/last-frame pair.", "Provides direct visual anchors before and after the ambiguous interval."),
    ["metric_identity_continuity", "metric_occlusion_continuity", "metric_object_state_transition"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L7", "Regenerate only the occlusion/reappearance interval with fixed boundary frames and composite it into the passing clip.", "Limits identity resampling to the failed interval while preserving accepted regions."),
)
add_failure(
    "A04", "Occlusion and hidden state", "Reappearance-position discontinuity",
    "A subject reappears at a position incompatible with its entry velocity, hidden trajectory, world geometry, or declared screen lane.",
    ["fast entry into smoke/water", "camera motion during occlusion", "long hidden interval", "no expected reappearance region", "off-screen exit and return"],
    ["teleportation", "wrong side of opponent", "depth lane changes", "subject emerges too early, too far, or from the wrong point"],
    ["mechanism://underdetermined_hidden_state", "mechanism://coordinate_frame_ambiguity", "mechanism://camera_scene_entanglement"],
    ["B012", "B013", "B019", "B020", "B021"],
    ["continuity.visibility_intervals", "shots", "camera", "actions", "constraints.continuity_locks"],
    ["'goes under and comes back' without coordinates or trajectory", "camera-relative and world-relative movement mixed", "orbit/whip during complete occlusion"],
    ("L2", "Encode entry point, velocity/trajectory class, hidden path, coordinate frame, expected reappearance region, and allowed camera transform.", "Makes spatial continuity a transition contract rather than two disconnected positions."),
    ("L4", "Use point tracks, pose trajectory, depth path, or a control video through the hidden interval.", "Constrains the missing trajectory directly."),
    ["metric_reappearance_position_error", "metric_screen_direction_consistency", "metric_spatial_relation_accuracy", "metric_camera_motion_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Cut before full disappearance and resume from an authored reappearance keyframe in a second shot.", "Replaces hidden long-range inference with an explicit edit boundary."),
)
add_failure(
    "A05", "Occlusion and hidden state", "Subject–occluder fusion",
    "The hidden subject becomes topologically or semantically fused with water, smoke, cloth, debris, hair, or another actor.",
    ["occluder shares colors/textures with subject", "full-frame effect", "crossed limbs or close contact", "transparent/semtransparent material", "effect contains face-like shapes"],
    ["limbs emerge from splash/smoke", "actor surface becomes liquid/cloth unintentionally", "two actors merge", "occluder retains anatomy"],
    ["mechanism://underdetermined_hidden_state", "mechanism://entity_binding_ambiguity", "mechanism://physical_constraint_absence"],
    ["B013", "B016", "B017", "B018"],
    ["entities", "interactions", "continuity.visibility_intervals", "style", "constraints.continuity_locks"],
    ["effect and subject described as one noun phrase", "no material boundary", "full opacity followed by immediate close-up"],
    ("L2", "Declare distinct entity/material IDs, topology invariants, and whether overlap is occlusion, contact, or transformation; forbid cross-material identity transfer.", "Separates semantic entities and allowed interaction types."),
    ("L4", "Provide separate subject and occluder masks/layers or a control composite with tracked boundaries.", "Enforces separability at the carrier level."),
    ["metric_identity_continuity", "metric_penetration_duration", "metric_material_state_consistency", "metric_actor_count_consistency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Generate clean subject motion and occluder/effect separately, then composite with tracked mattes.", "Avoids asking the generator to solve topology, identity, and VFX simultaneously."),
)
add_failure(
    "A06", "Occlusion and hidden state", "Submerged or hidden subject deletion",
    "A subject fully hidden by water, darkness, smoke, or an object is treated as no longer existing and never returns or loses downstream causal influence.",
    ["complete submersion", "subject leaves frame", "long opaque interval", "no downstream reappearance checkpoint", "another actor becomes the only visible subject"],
    ["subject vanishes permanently", "later action lacks the hidden actor", "held object disappears with actor", "actor count decreases without authored exit"],
    ["mechanism://underdetermined_hidden_state", "mechanism://state_representation_gap"],
    ["B011", "B012", "B013", "B014"],
    ["entities", "continuity.state_ledger", "continuity.visibility_intervals", "actions", "constraints.continuity_locks"],
    ["'disappears' used to mean temporarily obscured", "no explicit persistent-but-hidden state", "reappearance omitted from event graph"],
    ("L0", "Replace ambiguous disappearance language with 'remains present but fully hidden' and name the mandatory reappearance event.", "Removes a high-risk lexical ambiguity at minimal cost."),
    ("L2", "Represent visibility separately from existence: entity.exists=true, entity.visible=false during the interval, with a required reappearance transition.", "Prevents visibility loss from authorizing entity deletion in the canonical score."),
    ["metric_actor_count_consistency", "metric_object_count_persistence", "metric_event_graph_agreement", "metric_occlusion_continuity"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L3", "Provide a reappearance keyframe or storyboard panel and, where possible, a bubble trail/silhouette visibility bridge.", "Anchors existence and downstream position visually."),
)
add_failure(
    "A07", "Occlusion and hidden state", "Visibility-bridge attachment loss",
    "A silhouette, shadow, bubble trail, limb, mask, or point track intended to preserve continuity detaches from the correct hidden subject or attaches to another entity.",
    ["multi-actor occlusion", "overlapping control masks", "similar trajectories", "camera cut during bridge", "low-contrast silhouette"],
    ["bridge moves independently", "trail follows wrong actor", "mask jumps", "reappearance aligns with the wrong track"],
    ["mechanism://entity_binding_ambiguity", "mechanism://evaluator_observability_gap", "mechanism://coordinate_frame_ambiguity"],
    ["B013", "B018", "B019", "B020"],
    ["entities", "continuity.visibility_intervals", "provider_neutral_controls", "verification_requirements"],
    ["unlabeled masks/tracks", "one shared control layer for two actors", "bridge described but not associated by entity ID"],
    ("L2", "Bind every visibility bridge to a stable subject ID, coordinate frame, interval, and expected reappearance state.", "Prevents a bridge from being treated as a generic visual effect."),
    ("L4", "Use per-actor nonoverlapping masks/tracks and validate control assets before generation.", "Makes attachment explicit and machine-checkable."),
    ["metric_visibility_bridge_coverage", "metric_reappearance_position_error", "metric_identity_continuity", "metric_evaluator_disagreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Avoid multi-actor full occlusion in one shot; isolate each hidden trajectory or use a cut.", "Reduces attachment ambiguity at the scene-design level."),
)

# B — Object permanence and state persistence (7)
add_failure(
    "B01", "Object permanence and state", "Object disappearance",
    "A persistent prop, product, body-worn item, or environmental object vanishes without an authored removal event.",
    ["temporary occlusion", "hand-off", "camera cut", "small object", "motion blur", "attention shifts to another actor"],
    ["prop missing in later frames", "held item vanishes", "environmental object disappears after a camera move", "product demo loses the product"],
    ["mechanism://state_representation_gap", "mechanism://underdetermined_hidden_state"],
    ["B011", "B012", "B013", "B017"],
    ["entities", "assets", "continuity.state_ledger", "interactions", "constraints.continuity_locks"],
    ["object mentioned only at scene start", "no possession/state checkpoints", "object too small or visually similar to background"],
    ("L2", "Create a State Ledger entry with stable object ID, count, dimensions, material, holder/location, visibility, and legal transitions at every beat boundary.", "Makes persistence and possession explicit across the clip."),
    ("L3", "Use product/prop references and keyframes at every critical state or shot boundary.", "Anchors appearance and presence where text may be weak."),
    ["metric_object_count_persistence", "metric_object_state_transition", "metric_identity_continuity"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L7", "Regenerate only the first interval where the object is lost, using fixed boundary frames and preservation checks.", "Targets the earliest divergence before downstream errors compound."),
)
add_failure(
    "B02", "Object permanence and state", "Spontaneous object duplication",
    "A single prop, product, weapon, or environmental object becomes multiple objects without a creation event.",
    ["reflection or mirror", "two hands cross", "handoff", "object leaves and re-enters frame", "motion blur or VFX overlap"],
    ["two held items", "duplicate product", "reflection becomes tangible", "object remains in old hand and appears in new hand"],
    ["mechanism://entity_binding_ambiguity", "mechanism://underdetermined_hidden_state"],
    ["B011", "B013", "B017", "B018"],
    ["entities", "continuity.state_ledger", "interactions", "constraints.continuity_locks"],
    ["handoff described without exclusive possession transition", "reflection not typed", "object count omitted"],
    ("L2", "Hard-lock object_count=1 and encode an exclusive possession transition with release preceding acquire.", "Eliminates simultaneous ownership and duplicate interpretations from the target contract."),
    ("L4", "Track the object with a mask/point trajectory or provide handoff control frames.", "Carries one continuous object identity through the interaction."),
    ["metric_object_count_persistence", "metric_object_state_transition", "metric_contact_distance"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Composite or paint out duplicate objects after validating the intended trajectory.", "Provides deterministic count correction when interaction generation remains unstable."),
)
add_failure(
    "B03", "Object permanence and state", "Prop replacement",
    "A prop remains present but changes semantic type, geometry, brand, or function during use.",
    ["complex manipulation", "partial occlusion by hands", "small product details", "long clip", "multiple similar props"],
    ["tool becomes another tool", "product shape or logo changes", "weapon type changes", "functional parts move or disappear"],
    ["mechanism://state_representation_gap", "mechanism://entity_binding_ambiguity", "mechanism://conditioning_competition"],
    ["B002", "B011", "B015", "B017"],
    ["entities", "assets", "continuity.state_ledger", "interactions", "constraints.continuity_locks"],
    ["brand/geometry described only with adjectives", "many product features compete with action instructions", "no multi-view reference"],
    ("L2", "Encode immutable product identity, key dimensions, material, brand-critical marks, and allowed articulation separately from action.", "Distinguishes fixed identity from permitted mechanical state changes."),
    ("L3", "Provide multi-view product references and state-specific keyframes for each manipulation stage.", "Supplies the geometry and appearance that prose cannot reliably specify."),
    ["metric_identity_continuity", "metric_object_state_transition", "metric_human_readability"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Render or composite the product separately with tracked hands/occlusion mattes.", "Protects brand/product geometry when model-native manipulation is unreliable."),
)
add_failure(
    "B04", "Object permanence and state", "Unauthorized object-state reset",
    "An object returns to an earlier state—closed, intact, dry, empty, unlit, or unheld—without a reversing event.",
    ["cut or flash", "object leaves view", "multi-shot generation", "long action sequence", "state change not visually salient"],
    ["opened container closes", "damage repairs itself", "wet clothing becomes dry", "consumed product reappears", "light turns off"],
    ["mechanism://state_representation_gap", "mechanism://graphic_world_state_conflation", "mechanism://underdetermined_hidden_state"],
    ["B003", "B011", "B014", "B017"],
    ["continuity.state_ledger", "editing", "beats", "actions", "constraints.continuity_locks"],
    ["only final visual described, not state transition", "cut treated as a state reset", "separate clips generated without shared ledger"],
    ("L2", "Use monotonic or typed state transitions with preconditions, postconditions, and explicit reversibility; carry the resulting state into every later shot manifest.", "Prevents later shots from defaulting to the initial object state."),
    ("L3", "Condition each shot on the correct prior-state keyframe rather than the pristine reference.", "Transfers the changed state visually across generation boundaries."),
    ["metric_object_state_transition", "metric_object_count_persistence", "metric_event_graph_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Create and reuse a state-specific asset/plate for all later shots.", "Makes state persistence deterministic across separately generated clips."),
)
add_failure(
    "B05", "Object permanence and state", "Dimension, color, or material drift",
    "An object's scale, proportions, color, texture, reflectance, or material changes over time without an authored transformation.",
    ["camera zoom/dolly", "lighting change", "partial occlusion", "nonrigid handling", "stylized rendering", "long duration"],
    ["product grows/shrinks", "colors shift", "metal becomes plastic", "water level changes", "dimensions vary between hands"],
    ["mechanism://state_representation_gap", "mechanism://camera_scene_entanglement", "mechanism://conditioning_competition"],
    ["B011", "B015", "B016"],
    ["entities", "assets", "camera", "continuity.state_ledger", "style"],
    ["exact dimensions stated without a scale reference", "camera change mixed with size lock", "material adjectives repeated inconsistently"],
    ("L2", "Store immutable dimensions/material identifiers plus a visible scale anchor and separate world size from projected screen size.", "Prevents zoom or perspective changes from authorizing geometry drift."),
    ("L3", "Use multi-view reference images with consistent lighting/material capture and start/end state keyframes.", "Provides direct appearance and proportion anchors."),
    ["metric_identity_continuity", "metric_material_state_consistency", "metric_camera_motion_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Use product rendering/compositing for geometry- or brand-critical objects.", "Avoids stochastic re-synthesis of exact geometry and materials."),
)
add_failure(
    "B06", "Object permanence and state", "Hand–object detachment",
    "A held or manipulated object floats, drifts, intersects the hand, or changes grip without a valid release/acquire transition.",
    ["fast hand motion", "small object", "occlusion by fingers", "grip change", "two-hand handoff", "motion blur"],
    ["floating prop", "fingers pass through object", "object moves before contact", "grip slides", "object changes hands instantly"],
    ["mechanism://physical_constraint_absence", "mechanism://entity_binding_ambiguity", "mechanism://underdetermined_hidden_state"],
    ["B004", "B005", "B017", "B019", "B020"],
    ["interactions", "entities", "motion", "continuity.state_ledger", "verification_requirements"],
    ["'holds' without contact points", "handoff as a single compressed verb", "no contact frame or release/acquire order"],
    ("L2", "Compile a grasp/support contact contract with hand, object, contact regions, grip interval, release event, acquire event, and possession exclusivity.", "Defines the interaction geometry and temporal order explicitly."),
    ("L4", "Use hand/object pose or trajectory controls and keyframes at acquire, stable hold, and release.", "Constrains the most failure-prone contact frames."),
    ["metric_contact_distance", "metric_object_state_transition", "metric_penetration_duration", "metric_event_graph_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Separate the handoff into setup, exchange, and post-exchange shots or use a cut on contact.", "Reduces simultaneous hand/prop topology demands."),
)
add_failure(
    "B07", "Object permanence and state", "Reflection becomes a physical duplicate",
    "A mirror, water reflection, polished surface image, or shadow is interpreted as an independent physical entity or object.",
    ["reflective water or mirror", "camera crosses reflection axis", "occlusion hides the original", "low distinction between real and reflected planes"],
    ["reflection walks independently", "extra actor/object appears", "reflection leaves surface", "tracker/evaluator counts reflection as real"],
    ["mechanism://entity_binding_ambiguity", "mechanism://evaluator_observability_gap", "mechanism://underdetermined_hidden_state"],
    ["B013", "B017", "B018"],
    ["entities", "scenes", "continuity.state_ledger", "constraints.continuity_locks", "verification_requirements"],
    ["reflection described as a second visual subject", "no render-phenomenon type", "actor count inferred from segmentation alone"],
    ("L2", "Type reflections and shadows as non-entity render phenomena linked to a source entity and constrained to a surface/lighting relation.", "Prevents them from participating as independent actors in the canonical graph."),
    ("L4", "Provide reflection-plane masks or generate the clean scene and reflection in separate controlled layers.", "Separates physical entities from optical phenomena."),
    ["metric_actor_count_consistency", "metric_object_count_persistence", "metric_evaluator_disagreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Composite or replace reflections in postproduction using the accepted source-entity motion.", "Makes optical duplication deterministic."),
)

# C — Identity, role, and actor assignment (7)
add_failure(
    "C01", "Identity and role", "Face, body, hair, or costume drift",
    "An actor remains in the scene but its identity signature changes progressively or abruptly.",
    ["long duration", "profile/back view", "blur", "occlusion", "lighting/style shift", "multiple similar actors", "close-up after wide shot"],
    ["face morphs", "hair color/style changes", "costume details disappear", "body proportions drift", "mannerisms change"],
    ["mechanism://entity_binding_ambiguity", "mechanism://state_representation_gap", "mechanism://underdetermined_hidden_state"],
    ["B015", "B017", "B019"],
    ["entities", "assets", "continuity.state_ledger", "style", "constraints.continuity_locks"],
    ["single face reference used for full-body action", "identity described only by name", "too many mutable appearance adjectives"],
    ("L2", "Define a multimodal identity ledger with face, body shape, hair, costume, voice, and role signatures; separate immutable from intentionally variable traits.", "Makes identity continuity testable beyond face similarity."),
    ("L3", "Provide multi-view full-body/face/costume references and shot-boundary keyframes.", "Reduces underdetermination across pose and view changes."),
    ["metric_identity_continuity", "metric_actor_count_consistency", "metric_human_readability"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Generate shorter shots within the identity recurrence horizon and edit them using shared boundary frames.", "Limits cumulative identity drift."),
)
add_failure(
    "C02", "Identity and role", "Actor fusion during interaction",
    "Two intended actors merge into one body, exchange limbs, or become an inseparable topology during close interaction.",
    ["grapple", "crossed limbs", "similar clothing", "full overlap", "fast camera", "effect-obscured contact"],
    ["shared torso", "limbs attach to wrong actor", "faces merge", "actor count drops", "separation after contact is anatomically inconsistent"],
    ["mechanism://entity_binding_ambiguity", "mechanism://physical_constraint_absence", "mechanism://underdetermined_hidden_state"],
    ["B002", "B004", "B017", "B018"],
    ["entities", "interactions", "motion", "continuity.state_ledger", "constraints.continuity_locks"],
    ["both actors described in one dense clause", "no depth lanes or silhouette separation", "contact obscured with full-frame effect"],
    ("L2", "Declare stable actor IDs, depth lanes, allowed contact regions, minimum separability, and pre/post-contact poses.", "Defines how actors may overlap without losing identity/topology."),
    ("L4", "Use separate actor masks/poses or control video with readable silhouettes at contact and separation.", "Constrains identity ownership during maximum overlap."),
    ["metric_actor_count_consistency", "metric_identity_continuity", "metric_penetration_duration", "metric_contact_distance"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Cheat contact through camera angle, foreground occlusion, or a cut while keeping actors separately readable before and after.", "Preserves perceived impact without requiring exact two-body topology."),
)
add_failure(
    "C03", "Identity and role", "Actor duplication outside occlusion",
    "An actor is copied during fast motion, a smear, a cut, a crowd/background transition, or multi-shot synthesis even without full occlusion.",
    ["motion smear", "speed lines", "panoramic move", "multi-shot prompt", "background extras", "reflection", "frame exit/re-entry"],
    ["ghost copy persists", "same actor appears on both sides", "extra face/limb becomes a second person", "actor count changes across shot boundary"],
    ["mechanism://entity_binding_ambiguity", "mechanism://graphic_world_state_conflation"],
    ["B015", "B017", "B018"],
    ["entities", "editing", "style", "continuity.state_ledger", "constraints.continuity_locks"],
    ["smear described as duplicate silhouettes without recovery rule", "multi-shot prompt lacks per-shot cast ledger", "crowd language near a two-actor lock"],
    ("L2", "Separate graphic smear instances from persistent entities and carry a per-shot cast/count ledger with mandatory recovery frame.", "Allows temporary graphic duplication without authorizing physical actor duplication."),
    ("L3", "Provide pre-smear and recovery keyframes with exact cast and screen lanes.", "Anchors the physical actor count around the graphic accent."),
    ["metric_actor_count_consistency", "metric_edit_graphic_classification", "metric_anatomy_recovery_latency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Create smear/ghost accents as postproduction layers over a clean single-actor plate.", "Decouples visual stylization from entity generation."),
)
add_failure(
    "C04", "Identity and role", "Initiator/target or attacker/defender role swap",
    "Actors remain visually distinct but the wrong actor performs or receives the requested action.",
    ["similar actors", "pronouns", "crossing screen sides", "rapid cuts", "counterattacks", "mutual contact", "camera reverse"],
    ["defender attacks", "initiator reacts to own action", "wrong actor falls", "roles reverse mid-sequence"],
    ["mechanism://entity_binding_ambiguity", "mechanism://coordinate_frame_ambiguity", "mechanism://temporal_dependency_collapse"],
    ["B002", "B003", "B017"],
    ["entities", "actions", "interactions", "beats", "constraints.continuity_locks"],
    ["A/B labels not tied to visual signatures", "pronoun-heavy action prose", "actor crossings before role-critical event"],
    ("L2", "Encode typed event roles—initiator, target, instrument, contact region, reactor—and bind each role to stable entity IDs at every event.", "Removes role inference from surface grammar and screen position."),
    ("L3", "Use color-coded actor references and a storyboard with role-labeled poses at setup, apex, and reaction.", "Provides visual role anchors at critical times."),
    ["metric_role_assignment_accuracy", "metric_event_graph_agreement", "metric_causal_edge_accuracy", "metric_identity_continuity"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L5", "Avoid actor crossings in the same generated shot or split before the role-critical event.", "Reduces role rebinding pressure."),
)
add_failure(
    "C05", "Identity and role", "Target assignment confusion",
    "An action, gaze, line of dialogue, projectile, camera emphasis, or reaction is directed to the wrong target.",
    ["three or more candidate targets", "shared screen region", "off-screen target", "similar objects", "camera reframing", "pronouns/deictic language"],
    ["gaze misses target", "attack hits wrong actor/object", "speaker addresses wrong person", "camera follows wrong subject", "effect originates at wrong target"],
    ["mechanism://entity_binding_ambiguity", "mechanism://coordinate_frame_ambiguity"],
    ["B002", "B017"],
    ["entities", "actions", "interactions", "camera", "audio"],
    ["'him/it/there' without entity IDs", "target named only by left/right", "multiple objects share color/shape"],
    ("L1", "Resolve every deictic/pronoun reference into an explicit target entity and target region before provider serialization.", "Eliminates avoidable linguistic target ambiguity."),
    ("L2", "Add typed target edges, gaze/trajectory endpoints, and target-region constraints to the canonical event graph.", "Makes target correctness verifiable across modalities."),
    ["metric_role_assignment_accuracy", "metric_spatial_relation_accuracy", "metric_effect_origin_error", "metric_event_graph_agreement"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L4", "Use target masks, trajectory guides, or reference storyboard arrows where the provider supports visual control.", "Carries target geometry directly."),
)
add_failure(
    "C06", "Identity and role", "Screen-side actor swap",
    "Actor identities become associated with the opposite screen lane after crossing, a cut, an orbit, or temporary overlap.",
    ["actors cross", "camera crosses axis", "reverse angle", "full overlap", "similar wardrobe", "off-screen exit/re-entry"],
    ["A appears where B should be", "left/right labels swap", "subsequent actions attach to wrong actor", "continuity feels mirrored"],
    ["mechanism://entity_binding_ambiguity", "mechanism://coordinate_frame_ambiguity", "mechanism://camera_scene_entanglement"],
    ["B002", "B015", "B017", "B019"],
    ["entities", "shots", "camera", "continuity.state_ledger", "constraints.continuity_locks"],
    ["identity defined by screen side only", "camera orbit without world/screen transform", "no crossing event in state graph"],
    ("L2", "Define identity independently from screen side; encode lane transitions and camera transforms as explicit state transitions.", "Prevents screen projection from becoming the identity key."),
    ("L3", "Use distinct wardrobe/reference signatures and shot-boundary panels labeled by entity ID and world position.", "Anchors identities when screen lanes change."),
    ["metric_identity_continuity", "metric_screen_direction_consistency", "metric_spatial_relation_accuracy", "metric_axis_crossing_count"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Keep the axis and screen lanes stable for role-critical choreography; move the camera or actors in separate shots.", "Avoids simultaneous identity and coordinate-frame rebinding."),
)
add_failure(
    "C07", "Identity and role", "Voice or mannerism identity drift",
    "A character's voice, speech rhythm, accent, gesture habits, gaze style, or performance signature changes across time or shots.",
    ["multi-shot audio-video generation", "speaker off-screen", "multiple voices", "long dialogue", "voice not explicitly referenced", "separate clip generation"],
    ["voice changes timbre", "wrong actor speaks", "lip movement belongs to another voice", "mannerisms become generic or swap"],
    ["mechanism://entity_binding_ambiguity", "mechanism://state_representation_gap", "mechanism://conditioning_competition"],
    ["B015", "B022", "B023", "B024"],
    ["entities", "audio", "performance", "continuity.state_ledger", "assets"],
    ["speaker identified only by shot position", "no voice reference/ID", "dialogue and action overload one prompt"],
    ("L2", "Bind each utterance and performance signature to a stable speaker ID; store voice reference/hash, prosody constraints, and gesture/gaze motifs separately.", "Prevents voice and behavior from being inferred from transient screen position."),
    ("L3", "Use approved voice/reference assets and shot-level speaker keyframes; generate dialogue and complex action separately when necessary.", "Provides multimodal identity anchors."),
    ["metric_role_assignment_accuracy", "metric_lip_sync_offset", "metric_audio_event_alignment", "metric_identity_continuity"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Replace or align dialogue in postproduction and preserve accepted visual performance.", "Makes voice identity and timing deterministic when joint generation drifts."),
)

# D — Spatial reasoning and screen geography (6)
add_failure(
    "D01", "Spatial and screen geography", "Screen/world/actor direction confusion",
    "A directional instruction is interpreted in the wrong coordinate frame: viewer-relative, actor-relative, camera-relative, or world-relative.",
    ["unqualified left/right", "camera rotation", "actor turns around", "mirrored reference", "reverse shot", "movement described from multiple perspectives"],
    ["attack travels opposite direction", "actor uses wrong hand/side", "camera pans wrong way", "world direction changes after reframing"],
    ["mechanism://coordinate_frame_ambiguity", "mechanism://camera_scene_entanglement"],
    ["B002", "R005", "R006"],
    ["shots", "camera", "actions", "motion", "constraints.continuity_locks"],
    ["'move left' without frame declaration", "world and screen directions mixed in one sentence", "mirrored image reference not normalized"],
    ("L0", "Qualify every direction with its coordinate frame and subject: screen-left, actor's anatomical left, camera yaw left, or world-west.", "Eliminates a common lexical ambiguity at negligible cost."),
    ("L2", "Compile a Spatial State Transition Contract with coordinate-frame IDs, transforms, source/target regions, and expected signed displacement.", "Makes direction survival through camera and actor orientation changes explicit."),
    ["metric_screen_direction_consistency", "metric_spatial_relation_accuracy", "metric_camera_motion_agreement"],
    "preventable_by_prompting",
    additional_mitigation=("L3", "Use a labeled storyboard or start/end frames showing screen lanes and facing direction.", "Provides direct geometric anchors when text is insufficient."),
)
add_failure(
    "D02", "Spatial and screen geography", "Depth-order inversion",
    "Front/behind, containment, near/far, or occlusion ownership reverses relative to the intended world layout.",
    ["flat/stylized art", "transparent effects", "crossing trajectories", "camera orbit", "low parallax", "similar scale"],
    ["background actor appears in front", "wrong limb occludes", "object exits the wrong side of a container", "near actor shrinks behind target"],
    ["mechanism://coordinate_frame_ambiguity", "mechanism://underdetermined_hidden_state"],
    ["B002", "B013", "B016", "B018"],
    ["scenes", "shots", "camera", "interactions", "continuity.state_ledger"],
    ["depth implied only by prose", "no lane/depth order", "transparent effect obscures ownership"],
    ("L2", "Encode ordered depth lanes, containment relationships, and permitted occlusion ownership per beat.", "Turns depth into explicit pairwise relations rather than inferred composition."),
    ("L4", "Provide depth maps, masks, or a storyboard with clear parallax/overlap cues.", "Carries depth ordering through visual control."),
    ["metric_depth_order_accuracy", "metric_spatial_relation_accuracy", "metric_penetration_duration"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Choose a camera angle with readable silhouettes and unambiguous depth rather than solving the same action under flat overlap.", "Redesigns the shot to reduce ambiguity."),
)
add_failure(
    "D03", "Spatial and screen geography", "Axis reversal after cut or orbit",
    "The 180-degree action axis is crossed or implicitly mirrored so motion, eyelines, or attacker/defender screen direction reverses unintentionally.",
    ["camera orbit", "reverse angle", "hard cut", "whip pan", "actors cross", "no axis declaration"],
    ["A and B swap sides", "motion reverses", "eyelines no longer meet", "entrance/exit continuity breaks"],
    ["mechanism://coordinate_frame_ambiguity", "mechanism://camera_scene_entanglement", "mechanism://graphic_world_state_conflation"],
    ["B002", "R004", "R006"],
    ["shots", "camera", "editing", "continuity.state_ledger", "constraints.continuity_locks"],
    ["camera move and action described without axis policy", "'opposite angle' without intentional side swap", "single-shot orbit plus dense choreography"],
    ("L2", "Declare axis, camera side, actor world positions, screen-side policy, and whether an axis crossing is allowed at each shot transition.", "Makes the continuity rule explicit across edits and camera motion."),
    ("L3", "Provide shot panels or first/last frames for each side of the edit with labeled actor IDs.", "Anchors screen geography around the discontinuity."),
    ["metric_axis_crossing_count", "metric_screen_direction_consistency", "metric_spatial_relation_accuracy", "metric_edit_graphic_classification"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L5", "Split camera orbit and complex action; use a neutral bridge shot when intentionally crossing the axis.", "Prevents a single sample from resolving camera transform and choreography simultaneously."),
)
add_failure(
    "D04", "Spatial and screen geography", "Entrance/exit and off-screen continuity mismatch",
    "An actor or object exits one edge/direction and returns from a region incompatible with the world path or next shot.",
    ["frame exit", "cut during exit", "long off-screen interval", "camera pan", "multiple entrances", "ambiguous set layout"],
    ["actor enters from wrong edge", "teleports across room", "path crosses impossible obstacle", "next shot starts in unrelated position"],
    ["mechanism://underdetermined_hidden_state", "mechanism://coordinate_frame_ambiguity", "mechanism://state_representation_gap"],
    ["B012", "B014", "B015", "B017"],
    ["scenes", "shots", "actions", "continuity.visibility_intervals", "continuity.state_ledger"],
    ["'exits frame' without world destination", "separately generated shots lack shared scene map", "off-screen movement not represented"],
    ("L2", "Record exit edge, world destination, off-screen path, elapsed time, next entrance edge, and scene-layout constraints in the transition contract.", "Links two visible states with an explicit off-screen trajectory."),
    ("L3", "Use a scene map/storyboard and boundary keyframes for both shots.", "Provides consistent geography across separate generation calls."),
    ["metric_reappearance_position_error", "metric_spatial_relation_accuracy", "metric_event_graph_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Insert an establishing/bridge shot or avoid unsupported off-screen traversal.", "Restores observable continuity and reduces hidden-state inference."),
)
add_failure(
    "D05", "Spatial and screen geography", "Actor-distance drift",
    "The separation between actors or actor/object changes without locomotion, camera justification, or authored interaction.",
    ["zoom/dolly", "close contact", "cut from wide to close", "occlusion", "scale drift", "static pose held over time"],
    ["actors slide together/apart", "contact occurs from impossible range", "close-up changes world distance", "staging becomes crowded or empty"],
    ["mechanism://camera_scene_entanglement", "mechanism://coordinate_frame_ambiguity", "mechanism://physical_constraint_absence"],
    ["B002", "B004", "B021"],
    ["shots", "camera", "interactions", "motion", "continuity.state_ledger"],
    ["screen-size change used as world-distance instruction", "camera move and actor approach combined", "no minimum/target distance"],
    ("L2", "Separate world-space actor distance from projected screen distance; specify approach/retreat events and distance bands per beat.", "Prevents camera framing changes from substituting for locomotion."),
    ("L4", "Use pose/root trajectories, depth control, or start/end keyframes with calibrated scale.", "Constrains actual staging rather than appearance alone."),
    ["metric_contact_distance", "metric_spatial_relation_accuracy", "metric_camera_motion_agreement", "metric_camera_actor_entanglement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Separate camera move from actor approach or use a cut at a stable distance state.", "Reduces entanglement between projection and world motion."),
)
add_failure(
    "D06", "Spatial and screen geography", "Target-region miss",
    "An action, contact, gaze, effect, or trajectory reaches the wrong body part, object region, or environmental location.",
    ["small target", "fast action", "multiple nearby targets", "effect obscures contact", "camera angle hides region", "compressed verb"],
    ["strike hits wrong limb", "splash originates away from entry", "gaze misses face", "hand grasps wrong part", "projectile misses marked point"],
    ["mechanism://entity_binding_ambiguity", "mechanism://coordinate_frame_ambiguity", "mechanism://physical_constraint_absence"],
    ["B002", "B004", "B005", "B017"],
    ["actions", "interactions", "entities", "shots", "verification_requirements"],
    ["target is named only by object/actor", "no target region or contact frame", "effect and contact described simultaneously"],
    ("L2", "Attach a typed target region, allowed error band, contact/arrival frame, and consequence origin to the event edge.", "Makes local geometry part of the canonical target."),
    ("L4", "Use target masks, pose keypoints, trajectory guides, or a storyboard close-up.", "Constrains the precise region directly."),
    ["metric_contact_distance", "metric_effect_origin_error", "metric_role_assignment_accuracy", "metric_spatial_relation_accuracy"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Use a camera-cheated near-contact or insert shot rather than demanding exact full-body interaction.", "Improves readability and localizes the geometric problem."),
)

# E — Temporal order and causality (8)
add_failure(
    "E01", "Temporal action and causality", "Action omission",
    "One or more requested events never occur, often because the clip duration or conditioning budget is consumed by other actions.",
    ["many actions", "multiple actors", "dependent sequence", "short clip", "long style/camera prompt", "similar repeated events"],
    ["missing setup, contact, reaction, recovery, or effect", "clip ends before final event", "one actor remains idle"],
    ["mechanism://temporal_dependency_collapse", "mechanism://conditioning_competition"],
    ["B003", "B010", "B017"],
    ["beats", "actions", "interactions", "project.duration_seconds", "verification_requirements"],
    ["unordered action list", "too many primary actions for duration", "style details outrank event nodes"],
    ("L2", "Compile an ordered event graph with criticality, dependencies, minimum visible setup/apex/recovery windows, and a duration-feasibility check.", "Makes omission detectable before and after generation."),
    ("L5", "Split the sequence at stable state boundaries when all critical events cannot receive observable time.", "Reduces event competition and gives every action a complete visual interval."),
    ["metric_event_graph_agreement", "metric_temporal_event_error", "metric_human_readability"],
    "requires_shot_decomposition",
    additional_mitigation=("L7", "Regenerate only the missing event interval using accepted boundary frames.", "Adds the omitted event without resampling the full sequence."),
)
add_failure(
    "E02", "Temporal action and causality", "Action merge or compression",
    "Distinct sequential events collapse into one ambiguous movement or effect, losing setup, causality, or role separation.",
    ["compressed prose", "high action density", "similar actions", "short duration", "multi-actor simultaneity", "effect at contact"],
    ["setup and impact occur together", "dive/kick/splash become one motion", "handoff has no release/acquire phases", "cause and reaction are inseparable"],
    ["mechanism://temporal_dependency_collapse", "mechanism://conditioning_competition"],
    ["B003", "B004", "B005", "B017"],
    ["beats", "actions", "interactions", "editing", "verification_requirements"],
    ["comma-separated action nouns", "one verb phrase encodes cause, effect, and reaction", "no minimum phase duration"],
    ("L1", "Rewrite compressed nouns into ordered, single-subject clauses with explicit 'only after' dependencies.", "Improves semantic separation without adding a new control carrier."),
    ("L2", "Represent each event as a node with onset, apex, end, initiator, target, precondition, postcondition, and causal edges.", "Prevents the canonical plan from accepting a merged event as equivalent."),
    ["metric_event_graph_agreement", "metric_temporal_event_error", "metric_causal_edge_accuracy"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L5", "Allocate separate shots or clips to dependent events that remain merged under repeated seeds.", "Forces visual separation through production structure."),
)
add_failure(
    "E03", "Temporal action and causality", "Action repetition or invented filler",
    "The model repeats an event or invents gestures, attacks, camera moves, dialogue, or effects to fill unused duration.",
    ["under-specified middle interval", "long duration relative to action", "loop-like motion", "generic action genre prompt", "no end-state hold"],
    ["extra attacks", "repeated turn or gesture", "unwanted dialogue", "camera continues moving", "post-action idle becomes new action"],
    ["mechanism://state_representation_gap", "mechanism://conditioning_competition", "mechanism://temporal_dependency_collapse"],
    ["B003", "B010", "B017"],
    ["beats", "actions", "constraints", "project.duration_seconds", "verification_requirements"],
    ["action described without end state", "'dynamic' or genre language permits filler", "negative-only prohibition list"],
    ("L2", "Specify allowed event set, forbidden event classes, terminal state, and explicit hold/settle behavior for remaining duration.", "Closes the unused-time gap without relying on an open-ended negative prompt."),
    ("L5", "Shorten or split the clip so duration matches the intended event graph.", "Removes temporal capacity that the model otherwise fills stochastically."),
    ["metric_event_graph_agreement", "metric_temporal_event_error", "metric_control_retention"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L7", "Replace the filler interval with a regenerated hold, settle, or cutaway while preserving adjacent frames.", "Repairs only the invented content."),
)
add_failure(
    "E04", "Temporal action and causality", "Event-order reversal",
    "Two or more events occur in the opposite order from their causal or narrative specification.",
    ["before/after dependencies", "similar event cues", "short intervals", "audio cue", "multi-shot prompt", "compressed chronology"],
    ["reaction precedes cause", "landing precedes jump", "door closes before opening", "effect precedes contact"],
    ["mechanism://temporal_dependency_collapse", "mechanism://conditioning_competition"],
    ["B003", "B010", "B017"],
    ["beats", "actions", "interactions", "audio", "editing"],
    ["unordered list", "exact timestamps without causal edges", "'while' used for sequential events"],
    ("L1", "Use explicit ordered clauses and dependency language: event B begins only after event A reaches its apex/end.", "Clarifies the temporal relation in the provider prompt."),
    ("L2", "Compile a directed acyclic event graph and reject any schedule that violates preconditions or causal order before serialization.", "Creates a deterministic canonical ordering independent of prose order."),
    ["metric_temporal_event_error", "metric_event_graph_agreement", "metric_causal_edge_accuracy"],
    "preventable_by_prompting",
    additional_mitigation=("L5", "Generate causally dependent events as separate shots with boundary states when order still reverses.", "Makes order an edit-level property rather than a single-sample hope."),
)
add_failure(
    "E05", "Temporal action and causality", "Premature reaction or anticipation",
    "A target recoils, falls, splashes, speaks, or changes state before the initiating event reaches contact or an authored near-contact cue.",
    ["fast action", "impact effects", "audio prompt", "dramatic anticipation", "blur obscures contact", "model learns genre timing"],
    ["recoil before hit", "splash before water entry", "camera shake before impact", "fear reaction before reveal"],
    ["mechanism://temporal_dependency_collapse", "mechanism://physical_constraint_absence"],
    ["B003", "B004", "B005", "B022"],
    ["actions", "interactions", "audio", "camera", "verification_requirements"],
    ["effect listed before cause", "compressed 'hit and recoil' phrase", "dramatic wording without reaction-delay rule"],
    ("L2", "Encode cause apex, target reaction onset, allowed anticipation, minimum nonnegative reaction delay, and effect onset as linked event fields.", "Distinguishes authored anticipation from causal inversion."),
    ("L4", "Use keyframes/control timing for setup, contact/near-contact, and first reaction frame.", "Constrains the critical timing boundary visually."),
    ["metric_reaction_latency_error", "metric_causal_edge_accuracy", "metric_temporal_event_error", "metric_audio_event_alignment"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Time-shift or replace impact audio/VFX/camera shake in postproduction after preserving the accepted body motion.", "Makes secondary consequence timing deterministic."),
)
add_failure(
    "E06", "Temporal action and causality", "Cause–consequence decoupling",
    "A visible consequence occurs without the correct cause, at the wrong location, or in response to the wrong initiator.",
    ["impact VFX", "fluid/debris", "multiple contacts", "camera shake", "off-screen cause", "dense action"],
    ["debris with no collision", "water column from wrong point", "wrong actor reacts", "object moves before touch", "camera shake has no impact"],
    ["mechanism://physical_constraint_absence", "mechanism://entity_binding_ambiguity", "mechanism://temporal_dependency_collapse"],
    ["B004", "B005", "B006", "B017", "B026"],
    ["actions", "interactions", "motion", "camera", "audio", "verification_requirements"],
    ["cause and effect described as adjacent nouns", "no initiator/target/origin edge", "multiple possible causes in same interval"],
    ("L2", "Compile explicit causal edges: initiator → action/contact → target region → consequence onset/origin → reaction/recovery.", "Makes every consequence traceable to one allowed cause."),
    ("L5", "Isolate the causal event and its immediate consequence in one readable shot; move secondary VFX to postproduction if necessary.", "Reduces competing causes and clarifies event ownership."),
    ["metric_causal_edge_accuracy", "metric_effect_origin_error", "metric_reaction_latency_error", "metric_event_graph_agreement"],
    "requires_shot_decomposition",
    additional_mitigation=("L6", "Generate clean action and add debris/splash/shake/sound from the verified contact point in postproduction.", "Guarantees consequence origin and timing once the cause is accepted."),
)
add_failure(
    "E07", "Temporal action and causality", "Recovery or settle omission",
    "The generated action ends at apex/contact/landing without the authored follow-through, deceleration, recovery pose, or settled state.",
    ["short duration", "many earlier actions", "cut at impact", "camera effect consumes end time", "prompt omits recovery"],
    ["instant freeze", "body snaps to neutral", "landing has no compression", "object stops without deceleration", "clip ends mid-action"],
    ["mechanism://temporal_dependency_collapse", "mechanism://physical_constraint_absence"],
    ["B003", "B004", "B005"],
    ["beats", "actions", "motion", "interactions", "project.duration_seconds"],
    ["action noun without phase model", "duration allocated only to setup/apex", "impact used as terminal state"],
    ("L2", "Represent setup, onset, apex, consequence, recovery, and settle as required phases with minimum observable windows.", "Protects the action's terminal dynamics in the canonical schedule."),
    ("L5", "Allocate a separate recovery/settle shot or extend only from an accepted impact/landing frame.", "Gives recovery its own generation budget."),
    ["metric_event_graph_agreement", "metric_temporal_event_error", "metric_support_plausibility", "metric_momentum_continuity"],
    "requires_shot_decomposition",
    additional_mitigation=("L7", "Extend/regenerate the terminal interval from the accepted apex frame.", "Preserves the successful setup and contact while adding the missing recovery."),
)
add_failure(
    "E08", "Temporal action and causality", "Sequential/simultaneous collapse",
    "Events intended to be sequential occur together, or actions intended to overlap are serialized, changing causality and readability.",
    ["'while'/'then' ambiguity", "multiple actors", "short duration", "dependent actions", "audio cue", "parallel camera move"],
    ["both actors attack at once", "camera move waits until action ends", "dialogue and gesture lose sync", "sequential handoff becomes simultaneous"],
    ["mechanism://temporal_dependency_collapse", "mechanism://conditioning_competition"],
    ["B003", "B010", "B017"],
    ["beats", "actions", "camera", "audio", "interactions"],
    ["flat timestamp list", "relative ordering words used inconsistently", "no concurrency groups"],
    ("L2", "Compile concurrency groups, dependency edges, overlap windows, and mutual-exclusion constraints instead of relying on prose conjunctions.", "Makes parallel and sequential structure explicit."),
    ("L5", "Separate independent camera/action complexity or divide mutually dependent actions into adjacent shots.", "Reduces scheduling competition in one sample."),
    ["metric_temporal_event_error", "metric_event_graph_agreement", "metric_camera_motion_agreement", "metric_audio_event_alignment"],
    "requires_shot_decomposition",
    additional_mitigation=("L6", "Align audio, camera impulse, or secondary overlays in postproduction after body events pass.", "Restores precise concurrency without resampling core motion."),
)

FAMILY_PROMPT_RISKS = {
    "A": ["describes disappearance and reappearance but omits the hidden path", "uses a full-frame opaque effect while demanding exact continuity", "relies only on negative phrases such as no teleporting"],
    "B": ["omits the complete initial inventory", "describes an irreversible state change without a persistent end-state lock", "expects exact product geometry from text alone"],
    "C": ["uses only relative labels such as the left fighter", "gives similar actors indistinguishable appearance cues", "omits persistent actor IDs from events"],
    "D": ["uses left or right without a coordinate frame", "combines camera-side crossing with directional action", "specifies endpoints without depth or path"],
    "E": ["packs many dependent verbs into one sentence", "omits terminal hold and recovery", "assumes textual order is an executable timeline"],
    "F": ["compresses cause and consequence into a noun list", "names an effect without its origin and preconditions", "does not identify the reactor"],
    "G": ["uses hit or grab without distinguishing contact from near-contact", "omits target body region and contact interval", "combines close contact with heavy blur or occlusion"],
    "H": ["specifies only motion endpoints", "omits support contacts and recovery", "demands instant stylized direction changes without a causal skeleton"],
    "I": ["treats material effects as decorations rather than causal responses", "omits surface contact and displacement order", "requires opaque fluid effects and exact hidden identity in one pass"],
    "J": ["mixes camera and actor motion in one undifferentiated sentence", "combines orbit, impact shake, blur, and choreography", "uses zoom and dolly interchangeably"],
    "K": ["uses full-frame flash or wipe without declaring continuity semantics", "describes multi-shot events without state handoffs", "uses transformation language without allowed-state deltas"],
    "L": ["requests prolonged smear anatomy without a recovery frame", "stacks blur, cloth, overlap, and extreme foreshortening", "does not distinguish intentional deformation from invalid anatomy"],
    "M": ["submits multiple duplicate serializations", "assumes a prompt-string endpoint parses XML/YAML/JSON as a schema", "places hard locks after low-priority decorative text"],
    "N": ["treats all instructions as equally hard", "leaves unused time and allowed variation undefined", "combines too many high-variance control dimensions"],
    "O": ["does not bind sound events to visual event IDs", "asks a joint model to preserve multiple voices without speaker references", "uses BPM numerals without a shared timecode"],
    "P": ["accepts one VLM verdict as ground truth", "averages conflicting semantic and measured evidence", "uses a detector outside its calibrated domain without uncertainty"],
}

FAMILY_WORKFLOWS = {
    "A": ["text_to_video", "image_to_video", "first_last_frame", "reference_to_video", "video_to_video", "multi_shot"],
    "B": ["text_to_video", "image_to_video", "reference_to_video", "multi_shot", "video_extension"],
    "C": ["text_to_video", "image_to_video", "reference_to_video", "multi_shot", "audio_video_joint"],
    "D": ["text_to_video", "image_to_video", "first_last_frame", "multi_shot", "pose_depth_control"],
    "E": ["text_to_video", "image_to_video", "multi_shot", "audio_video_joint"],
    "F": ["text_to_video", "image_to_video", "audio_video_joint", "multi_shot"],
    "G": ["text_to_video", "image_to_video", "pose_depth_control", "video_to_video"],
    "H": ["text_to_video", "image_to_video", "pose_depth_control", "video_to_video"],
    "I": ["text_to_video", "image_to_video", "video_to_video", "multi_shot"],
    "J": ["text_to_video", "image_to_video", "camera_control", "video_to_video"],
    "K": ["text_to_video", "image_to_video", "multi_shot", "video_to_video"],
    "L": ["text_to_video", "image_to_video", "pose_control", "video_to_video"],
    "M": ["all_prompt_string_workflows"],
    "N": ["all_generation_workflows"],
    "O": ["audio_video_joint", "dialogue", "music_synchronized_video", "post_dubbed_video"],
    "P": ["verification", "repair", "experiment_recording"],
}


def mitigation_entry(level: str, method: str, evidence_strength: str, limitations: list[str], verification: str, rollback: str) -> dict[str, Any]:
    return {
        "level": level,
        "method": method,
        "expected_benefit": "Reduces the named failure by adding the missing state, control signal, decomposition boundary, or deterministic finishing step.",
        "token_or_character_cost": "low" if level in {"L0", "L1", "L2"} else "not primarily a prompt-token cost",
        "generation_cost_impact": {
            "L0": "none",
            "L1": "none to low",
            "L2": "none to low",
            "L3": "low to moderate asset-preparation cost",
            "L4": "moderate control-media and compute cost",
            "L5": "additional generations and edit cost",
            "L6": "postproduction labor or compute cost",
            "L7": "localized regeneration cost",
            "L8": "provider migration and qualification cost",
            "L9": "not controllable in the declared workflow",
        }.get(level, "unknown"),
        "risk_of_new_failure": "Control/reference conflict, overconstraint, evaluator error, or seam discontinuity must be checked.",
        "provider_dependency": "Provider-independent decision level; exact implementation depends on documented provider inputs.",
        "evidence_strength": evidence_strength,
        "verification_method": verification,
        "rollback": rollback,
        "limitations": limitations,
    }


def build_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    ordinal = 0
    for family, specs in FAMILY_SPECS.items():
        meta = FAMILY_META[family]
        for item in specs:
            ordinal += 1
            source_refs = sorted(set(meta["default_sources"] + item["sources"]))
            primary = mitigation_entry(
                item["level"],
                item["mitigation"],
                "supported by cross-model benchmarks/control research; provider-specific effect size not yet measured by CPCS",
                ["No prompt or control guarantees exact compliance.", "Provider/model/version qualification is required."],
                item["metric"],
                "Restore the previous compiler build and retained accepted artifact; never overwrite immutable run evidence.",
            )
            fallback_level = "L6" if item["level"] in {"L0", "L1", "L2", "L3", "L4", "L5"} else "L8"
            fallback_method = (
                "Move the unstable effect, shake, audio event, graphic discontinuity, or exact geometry to deterministic postproduction/compositing."
                if fallback_level == "L6"
                else "Use a provider/model with an officially documented control input matching the missing constraint and rerun qualification."
            )
            fallback = mitigation_entry(
                fallback_level,
                fallback_method,
                "workflow engineering rationale; requires controlled validation",
                ["May add seams, finishing labor, or provider migration cost."],
                item["metric"],
                "Return to the accepted pre-repair artifact and preserve the failed attempt as evidence.",
            )
            record = {
                "schema_version": "cpcs.failure_record/1.0",
                "failure_id": f"failure://{family.lower()}/{item['slug']}/1",
                "ordinal": ordinal,
                "family_id": family,
                "family_name": meta["name"],
                "name": item["name"],
                "definition": f"A generation or evaluation failure in which {item['symptom'][0].lower() + item['symptom'][1:]}",
                "scope": {
                    "provider": None,
                    "model": None,
                    "version": None,
                    "workflows": FAMILY_WORKFLOWS[family],
                    "content_types": ["realistic", "cinematic", "UGC", "product_demo", "dialogue", "anime", "stylized_action", "VFX", "multi_actor"],
                },
                "trigger_conditions": [item["trigger"]],
                "observed_symptoms": [item["symptom"]],
                "suspected_causes": [
                    {
                        "statement": item["cause"],
                        "status": "cross_provider_mechanistic_inference",
                        "confidence": item["confidence"],
                        "falsification_test": "Hold content and seed/retry policy constant; add only the missing state/control representation and compare repeated-seed success distributions.",
                    }
                ],
                "evidence_class": "benchmark_and_literature_synthesis",
                "source_refs": source_refs,
                "canonical_fields_affected": meta["canonical_paths"],
                "prompt_risk_patterns": FAMILY_PROMPT_RISKS[family],
                "mitigations": [primary, fallback],
                "verification_metrics": sorted(set([item["metric"]] + meta["metrics"])),
                "regression_fixtures": [f"fixture://failure/{family.lower()}/{item['slug']}/v1"],
                "provider_specific_notes": [
                    "Official capability documentation establishes available inputs, not reliable compliance with this failure contract.",
                    "Text-only workflows should be presumed unable to guarantee hidden geometry, exact contact, or exact numeric trajectories until qualified.",
                    "First/last frames constrain endpoints but do not by themselves prove the path between them.",
                ],
                "cpcs_ownership": {
                    "existing_owner": meta["owner"],
                    "research_owner": "research package and second-brain candidate evidence",
                    "implementation_owner": "existing compiler/verification/second-brain modules only",
                    "new_parallel_schema_allowed": False,
                },
                "integration_classifications": [
                    "knowledge_only",
                    "verification_affecting",
                    "contract_affecting" if family not in {"P"} else "implementation_affecting",
                ],
                "empirical_confidence": item["confidence"],
                "cpcs_render_campaign_status": "not_run_no_authorized_provider_credentials_or_budget_in_session",
                "unresolved_questions": [
                    "What is the success distribution for each current provider/model/version under a repeated-seed CPCS fixture?",
                    "Which mitigation level is the cheapest intervention that clears the pre-registered threshold without creating a new failure?",
                ],
                "researched_at": ACCESS_DATE,
            }
            records.append(record)
    return records


FAILURE_RECORDS = build_records()


FAILURE_RECORD_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/failure-record/1.0",
    "title": "CPCS failure research record",
    "type": "object",
    "required": [
        "schema_version", "failure_id", "family_id", "family_name", "name", "definition", "scope",
        "trigger_conditions", "observed_symptoms", "suspected_causes", "evidence_class", "source_refs",
        "canonical_fields_affected", "prompt_risk_patterns", "mitigations", "verification_metrics",
        "regression_fixtures", "provider_specific_notes", "cpcs_ownership", "integration_classifications",
        "empirical_confidence", "cpcs_render_campaign_status", "unresolved_questions", "researched_at"
    ],
    "properties": {
        "schema_version": {"const": "cpcs.failure_record/1.0"},
        "failure_id": {"type": "string", "pattern": "^failure://[a-p]/[a-z0-9_]+/1$"},
        "ordinal": {"type": "integer", "minimum": 1},
        "family_id": {"enum": list(FAMILY_META.keys())},
        "family_name": {"type": "string", "minLength": 1},
        "name": {"type": "string", "minLength": 3},
        "definition": {"type": "string", "minLength": 10},
        "scope": {
            "type": "object",
            "required": ["provider", "model", "version", "workflows", "content_types"],
            "properties": {
                "provider": {"type": ["string", "null"]},
                "model": {"type": ["string", "null"]},
                "version": {"type": ["string", "null"]},
                "workflows": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                "content_types": {"type": "array", "items": {"type": "string"}},
            },
            "additionalProperties": False,
        },
        "trigger_conditions": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 5}},
        "observed_symptoms": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 5}},
        "suspected_causes": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object",
                "required": ["statement", "status", "confidence", "falsification_test"],
                "properties": {
                    "statement": {"type": "string"},
                    "status": {"enum": ["verified_architecture_fact", "provider_documented", "cross_provider_mechanistic_inference", "hypothesis"]},
                    "confidence": {"enum": ["high", "moderate", "low"]},
                    "falsification_test": {"type": "string"},
                },
                "additionalProperties": False,
            },
        },
        "evidence_class": {"type": "string"},
        "source_refs": {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "string", "pattern": "^[RMB][0-9]{3}$"}},
        "canonical_fields_affected": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "prompt_risk_patterns": {"type": "array", "items": {"type": "string"}},
        "mitigations": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object",
                "required": ["level", "method", "expected_benefit", "token_or_character_cost", "generation_cost_impact", "risk_of_new_failure", "provider_dependency", "evidence_strength", "verification_method", "rollback", "limitations"],
                "properties": {
                    "level": {"enum": [f"L{i}" for i in range(10)]},
                    "method": {"type": "string"},
                    "expected_benefit": {"type": "string"},
                    "token_or_character_cost": {"type": "string"},
                    "generation_cost_impact": {"type": "string"},
                    "risk_of_new_failure": {"type": "string"},
                    "provider_dependency": {"type": "string"},
                    "evidence_strength": {"type": "string"},
                    "verification_method": {"type": "string"},
                    "rollback": {"type": "string"},
                    "limitations": {"type": "array", "items": {"type": "string"}},
                },
                "additionalProperties": False,
            },
        },
        "verification_metrics": {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "string", "pattern": "^metric_[a-z0-9_]+$"}},
        "regression_fixtures": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "provider_specific_notes": {"type": "array", "items": {"type": "string"}},
        "cpcs_ownership": {
            "type": "object",
            "required": ["existing_owner", "research_owner", "implementation_owner", "new_parallel_schema_allowed"],
            "properties": {
                "existing_owner": {"type": "string"},
                "research_owner": {"type": "string"},
                "implementation_owner": {"type": "string"},
                "new_parallel_schema_allowed": {"const": False},
            },
            "additionalProperties": False,
        },
        "integration_classifications": {"type": "array", "items": {"enum": ["knowledge_only", "contract_affecting", "implementation_affecting", "provider_version_affecting", "verification_affecting", "policy_affecting", "unverified"]}},
        "empirical_confidence": {"enum": ["high", "moderate", "low"]},
        "cpcs_render_campaign_status": {"type": "string"},
        "unresolved_questions": {"type": "array", "items": {"type": "string"}},
        "researched_at": {"type": "string", "format": "date"},
    },
    "additionalProperties": False,
}


def metric_definition(metric_id: str) -> dict[str, Any]:
    measured_keywords = ["count", "distance", "duration", "offset", "error", "trajectory", "foot_slip", "latency", "frame", "coverage", "truncation", "conflict"]
    semantic_keywords = ["agreement", "assignment", "instruction", "semantic", "action_graph", "causal_edge", "role", "target"]
    if any(k in metric_id for k in measured_keywords):
        lane = "measured"
        method = "Compute an interval-scoped numeric value from calibrated tracking, segmentation, pose, audio, optical-flow, or media-timing records; preserve raw traces."
    elif any(k in metric_id for k in semantic_keywords):
        lane = "semantic_plus_human"
        method = "Decompose the canonical target into atomic assertions, query a version-pinned video evaluator, and require human review for critical or conflicting assertions."
    else:
        lane = "human_calibrated_multilane"
        method = "Combine detector/semantic evidence with a pre-registered human rubric; no lane may silently override another."
    blind_spots = [
        "Fast events can be missed by sparse frame sampling.",
        "Occlusion, reflections, blur, stylization, and similar actors can break trackers or segmenters.",
        "A score is not physical ground truth; conflicts require review.",
    ]
    threshold_policy = "Provider/task-specific threshold must be pre-registered from human-calibrated fixtures; no universal threshold is asserted by this package."
    return {
        "schema_version": "cpcs.evaluation_metric/1.0",
        "metric_id": metric_id,
        "observable_dimension": metric_id.removeprefix("metric_").replace("_", " "),
        "required_lane": lane,
        "measurement_method": method,
        "evaluator_requirements": ["version-pinned", "configuration-hashed", "artifact-hash-bound", "domain-calibrated"],
        "known_blind_spots": blind_spots,
        "human_calibration_requirement": "Required before a metric can block or promote a provider/model/version; required on any cross-lane conflict.",
        "failure_threshold_policy": threshold_policy,
        "confidence_reporting": "Report raw value, uncertainty or confidence, sample count, failed frames/intervals, and evaluator version; never emit an unsupported scalar certainty.",
    }


ALL_METRIC_IDS = sorted({m for r in FAILURE_RECORDS for m in r["verification_metrics"]})
EVALUATION_METRICS = [metric_definition(mid) for mid in ALL_METRIC_IDS]

EVALUATION_METRICS_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/evaluation-metric/1.0",
    "type": "object",
    "required": ["schema_version", "metric_id", "observable_dimension", "required_lane", "measurement_method", "evaluator_requirements", "known_blind_spots", "human_calibration_requirement", "failure_threshold_policy", "confidence_reporting"],
    "properties": {
        "schema_version": {"const": "cpcs.evaluation_metric/1.0"},
        "metric_id": {"type": "string", "pattern": "^metric_[a-z0-9_]+$"},
        "observable_dimension": {"type": "string", "minLength": 2},
        "required_lane": {"enum": ["measured", "semantic_plus_human", "human_calibrated_multilane"]},
        "measurement_method": {"type": "string"},
        "evaluator_requirements": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "known_blind_spots": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "human_calibration_requirement": {"type": "string"},
        "failure_threshold_policy": {"type": "string"},
        "confidence_reporting": {"type": "string"},
    },
    "additionalProperties": False,
}


def provider_row(provider: str, model: str, model_id: str, date_scope: str, status: str, access_path: str, modes: str, inputs: str, duration: str, output: str, audio: str, controls: str, prompt_limit: str, seed: str, source_ids: str, recommended_use: str, caveats: str) -> dict[str, str]:
    return {
        "provider": provider,
        "model_family": model,
        "model_or_endpoint_id": model_id,
        "release_or_document_scope": date_scope,
        "current_status_at_2026_08_05": status,
        "access_path": access_path,
        "documented_generation_modes": modes,
        "documented_inputs": inputs,
        "documented_duration": duration,
        "documented_output": output,
        "documented_audio": audio,
        "documented_reference_or_control_inputs": controls,
        "documented_prompt_limit": prompt_limit,
        "seed_or_reproducibility": seed,
        "official_source_ids": source_ids,
        "empirical_failure_reliability": "NOT ESTABLISHED by official documentation; CPCS repeated-seed qualification required",
        "recommended_cpcs_role": recommended_use,
        "critical_caveats": caveats,
    }


PROVIDER_ROWS = [
    provider_row("Google Vertex AI", "Veo 3.1", "veo-3.1-generate-001", "official docs current through 2026", "documented production endpoint", "Vertex AI predictLongRunning", "T2V; I2V; first+last frame; extension on documented workflows", "text; first frame; optional last frame", "4/6/8s per generation; extension workflow separate", "720p/1080p; 24 fps", "official pages are endpoint-specific; current CPCS repo profile sets sound_generation=false", "first/last images; negativePrompt; seed", "not asserted by CPCS repo profile; provider request budget is adapter policy", "uint32 seed documented; artifact verification still required", "M001 M013 R007", "High-quality endpoint with explicit endpoint qualification; use first/last only as endpoint constraints, not hidden-path proof.", "Google documentation exposes endpoint/model differences, including audio and 4K preview distinctions; bind exact endpoint and date."),
    provider_row("Google Vertex AI", "Veo 3.1 Fast", "veo-3.1-fast-generate-001", "official docs current through 2026", "documented production/fast endpoint", "Vertex AI predictLongRunning", "T2V; I2V; first+last frame", "text; first frame; optional last frame", "4/6/8s", "720p/1080p; 24 fps", "endpoint-specific; verify before compile", "first/last images; seed", "endpoint-specific", "seed documented; same-request identity is not a compliance guarantee", "M001 M013", "Fast ablation and draft generation after exact capability check.", "Do not infer quality parity with standard model."),
    provider_row("Runway", "Gen-4.5", "gen4.5", "API available 2026-02-10", "current API model", "Runway API", "T2V; I2V", "text; first image for I2V", "integer 2-10s", "T2V 1280x720/720x1280; additional I2V ratios; 720-class API outputs", "not documented as native joint audio in cited endpoint", "first image; ratio; duration; seed", "1-1000 UTF-16 code units", "same seed described as similar, not exact identity", "M002 M015 M021 M022", "Prompt- and image-conditioned short shots; pair with external audio and post when exact sync is required.", "No official model-specific failure distribution; prompt limit requires compiler compression."),
    provider_row("Runway", "Aleph 2.0", "aleph2", "official product/API docs 2026", "current source-video editing model", "Runway API / Edit Studio", "V2V editing", "source video + text and/or images", "2-30s input", "preserves source resolution up to 1080p; <=30 fps input", "source audio handling must be verified for the exact workflow", "source video; edit prompt; up to workflow-specific keyframe/reference images", "1-1000 UTF-16 code units in API prompt fields where applicable", "capture request and artifact hashes; no exact semantic-isolation guarantee", "M002 M016 M021", "Localized repair, preservation-heavy transformation, and effect layering on accepted motion plates.", "Editing can spill outside the intended region; verify all hard locks, not only the requested change."),
    provider_row("Runway", "Seedance 2.0 adapter", "seedance2 / seedance2_fast / seedance2_mini", "current Runway API 2026-08-05", "current third-party adapter", "Runway API", "T2V; I2V; V2V", "text; images including first/last/reference; video; model-specific refs", "endpoint/model-specific", "endpoint/model-specific", "endpoint/model-specific", "multimodal reference inputs exposed by adapter", "1-1000 UTF-16 code units", "Runway seed semantics; verify model-specific schema", "M002 M015 M021", "Adapter qualification and cross-provider experiments when native Seedance access is unavailable.", "Do not assume native ByteDance limits or behavior are preserved by the adapter."),
    provider_row("ByteDance Seed", "Seedance 2.0", "Seedance 2.0", "released 2026-02-12", "officially launched; exact API access path varies", "Seedance product/native ecosystem", "T2V; I2V; multimodal reference; editing; extension; multi-shot AV", "text; up to 9 images; 3 videos; 3 audio clips", "up to 15s official launch claim", "high-quality multi-shot AV; exact API resolution not verified in this pass", "native joint audio-video; provider acknowledges occasional audio distortion", "image/video/audio references; extension/editing", "not verified with 100% certainty for every interface", "not verified for native interface", "M004", "Multimodal/reference-heavy experiments and complex AV scenes after exact interface capture.", "Provider-authored quality claims are not reliability proof; detail stability, multi-subject consistency, text rendering, complex editing, and occasional audio distortion remain acknowledged limits."),
    provider_row("Kuaishou", "Kling Video 3.0 / 3.0 Omni", "Kling Video 3.0; Video3 Omni", "released 2026-02-05", "officially launched", "Kling AI product/API subject to exact access", "T2V; I2V; R2V; in-video editing; multi-shot", "text; image; audio; video", "up to 15s in official release", "exact resolution/fps must be verified in the selected interface", "native multilingual audio and multi-character dialogue claimed", "multiple image/video references; multimodal editing", "interface-specific; not verified here", "not verified here", "M019", "Reference-to-video and native-audio qualification arms.", "Official consistency/control claims are provider-authored; exact API request schema and limits require live interface capture."),
    provider_row("MiniMax", "Hailuo 2.3", "MiniMax-Hailuo-2.3", "released 2025-10-28", "current documented API model", "MiniMax API", "T2V; I2V", "text; first frame for I2V", "6s or 10s at 768p; 6s at 1080p", "768p/1080p", "no native audio capability established by cited video endpoint", "first-frame image; camera-command prompt syntax on documented T2V guide", "up to 2000 characters on cited T2V documentation", "capture task ID and output; exact reproducibility not established", "M006 M007 M020", "Short T2V/I2V provider comparison with explicit prompt-budget adapter.", "Fast/standard variants have different modes; official realism claims are not qualification evidence."),
    provider_row("MiniMax", "Hailuo 2.3 Fast", "MiniMax-Hailuo-2.3-Fast", "released 2025-10-28", "current documented API model", "MiniMax API", "I2V", "text + first frame", "6s or 10s at 768p; 6s at 1080p", "768p/1080p", "not established", "first frame", "endpoint-specific", "not established", "M006 M020", "Low-cost I2V ablation arm.", "Not a T2V model according to release notes."),
    provider_row("MiniMax", "Hailuo 02", "MiniMax-Hailuo-02", "current docs accessed 2026-08-05", "current documented API model", "MiniMax API", "text/image video modes including first/last/reference depending endpoint", "text; first/last/reference images", "up to 10s", "up to 1080p", "not established", "first/last/reference images", "endpoint-specific", "not established", "M020", "First/last-frame comparison arm.", "Exact mode-by-mode limits must be captured from the selected endpoint."),
    provider_row("Alibaba Cloud", "Wan 2.7 Text-to-Video", "wan2.7-t2v-2026-06-12", "docs updated 2026-07-01", "current documented API model", "Model Studio/DashScope", "T2V with audio; multi-shot", "text; optional custom audio", "2-15s", "720p/1080p; 30 fps; MP4", "audio synchronization and custom audio documented", "audio input; prompt rewriting setting", "model-specific", "seed support must be checked in exact endpoint", "M014", "Longer AV and multi-shot qualification after prompt-rewrite policy is fixed.", "Provider multi-shot/physics claims require empirical CPCS runs."),
    provider_row("Alibaba Cloud", "Wan 2.7 Image-to-Video", "wan2.7-i2v-2026-04-25", "docs updated 2026-06/07", "current documented API model", "Model Studio/DashScope", "first-frame; first+last; continuation; audio-driven", "text; image; audio; video continuation input", "2-15s", "720p/1080p; 30 fps; MP4", "automatic dubbing or custom audio documented", "first/last frames; continuation; multimodal input", "model-specific", "same seed should not be treated as exact artifact identity", "M014 M024 M025", "Endpoint-constrained continuity tests and first/last-frame ablations.", "Endpoint constraints do not prove the intermediate path; prompt rewriting must be disabled or recorded."),
    provider_row("Alibaba Cloud", "Wan 2.7 Reference-to-Video", "wan2.7-r2v-2026-06-12", "docs updated 2026-07", "current documented API model", "Model Studio/DashScope", "reference image/video to video; multi-character", "text; images; reference video; audio", "2-10s when video reference is supplied; longer without video per API rules", "720p/1080p; 30 fps", "audio/voice-timbre controls documented", "multi-entity references; first frame optional", "up to 5000 characters on cited native API summary", "fixed seed improves reproducibility but does not guarantee identical output", "M014 M025", "Identity/role/reference qualification.", "Reference conflicts and multi-subject consistency still require verification."),
    provider_row("Alibaba Cloud", "Wan 2.7 VideoEdit", "wan2.7-videoedit", "docs updated 2026-07", "current documented API model", "Model Studio/DashScope", "instruction-based V2V editing; effect/camera replication", "text; image; source video", "2-10s", "720p/1080p; 30 fps", "depends on input/output mode", "source video; style/effect/camera reference", "model-specific", "capture exact input/output hashes", "M014", "Localized repair and effect/camera transfer.", "Semantic edits may alter non-target state; verify full continuity ledger."),
    provider_row("Lightricks", "LTX-2", "LTX-2 open weights/workflows", "announced 2025-10-23; repository current 2026", "open repository and weights/workflows", "local inference / ComfyUI / repository", "T2V; I2V; V2V; multi-keyframe; extension; control adapters", "text; images/keyframes; video; control representations", "up to 10s synchronized AV for LTX-2 documented; older 0.9.8 workflows up to 60s", "repository claims native 4K/up to 50 fps for LTX-2; validate checkpoint/workflow", "synchronized audio-video", "multi-keyframe; IC-LoRA/control; camera logic; LoRA", "local prompt handling varies", "local seed and full config can be captured", "M008", "Reproducible local control-media and keyframe experiments.", "Exact checkpoint, sampler, quantization, VAE, and workflow must be pinned; repository claims need independent qualification."),
    provider_row("Wan-Video", "Wan 2.2 Open", "Wan2.2 T2V/I2V/TI2V/S2V/Animate", "released 2025-07 onward", "open repository", "local inference / Diffusers / ComfyUI", "T2V; I2V; TI2V; speech-to-video; character animation/replacement", "text; image; audio; pose/reference video depending checkpoint", "checkpoint/workflow-specific", "480p/720p documented open workflows; checkpoint-specific fps", "S2V/audio-driven variants", "pose video; source motion; reference character", "local", "full seed/config capture possible; exact determinism depends runtime", "M009", "Local controlled experiments, pose/audio controls, and deterministic evidence capture.", "Hardware/runtime and checkpoint selection materially affect output."),
    provider_row("Tencent Hunyuan", "HunyuanVideo 1.5", "HunyuanVideo-1.5", "released 2025-11 onward", "open repository", "local inference", "T2V; I2V; super-resolution", "text; first image", "workflow-specific", "480p/720p generation; super-resolution to 1080p", "not established in cited base repository", "image conditioning; prompt rewriting", "local", "seed and config capture", "M010", "Open-model baseline and architecture-level ablations.", "Prompt rewriting and official evaluations must be separated from raw prompt behavior and independent evidence."),
    provider_row("Z.ai/THUDM", "CogVideoX 1.5", "CogVideoX1.5 T2V/I2V", "repository current through 2025", "open repository", "local inference / Diffusers", "T2V; I2V; continuation", "text; image/video depending checkpoint", "10s documented", "1360x768 documented for 1.5; workflow-specific fps", "not established", "first image/video; LLM prompt optimization optional", "long prompts supported by training, exact interface-specific", "seed/config capture", "M011", "Open compositional baseline and prompt-optimization ablation.", "LLM prompt optimization can change semantics; treat as a separate arm."),
    provider_row("Genmo", "Mochi 1 Preview", "Mochi 1", "released 2024 onward", "open preview repository", "local inference", "T2V", "text", "checkpoint/workflow-specific", "repository/workflow-specific", "not established", "no official structural controls in cited overview", "local", "seed/config capture", "M012", "Open architecture baseline for compression/temporal failure research.", "Preview/open model; not comparable to current commercial services without controlled settings."),
    provider_row("Luma AI", "Ray 3.2", "Ray 3.2 Modify Video", "published 2026-05-27", "current modify-video workflow", "Dream Machine/Luma workflow", "V2V modify only", "source video; text; many source-indexed keyframes", "preserves exact source duration in product guide; product marketing and API limits must be reconciled", "HDR/EXR/1080p product controls; exact API availability varies", "source audio handling depends workflow", "dense arbitrary keyframes; adherence/character controls", "interface-specific", "source and output hash capture", "M017", "Preservation-heavy restyle/repair where motion and timing already exist.", "It is not T2V, I2V animation, or extension; marketing page and current API exposure must be distinguished."),
    provider_row("OpenAI", "Sora 2", "Sora 2", "system card 2025-09-30; status note 2026-04-26", "consumer product unavailable as of 2026-04-26; no current public production interface verified", "none verified in this pass", "historical video+audio generation", "historical product inputs", "not used for current matrix qualification", "not used for current matrix qualification", "synchronized audio claimed historically", "not currently available for CPCS qualification", "not applicable", "not applicable", "M018", "None until an official current interface is documented and authorized.", "Do not list as currently available merely from the old system card or showcase."),
]


CLAIMS = [
    {"claim_id": "C001", "claim": "Current video generators can produce visually plausible outputs while failing dynamics, causality, or information preservation.", "status": "supported_by_benchmark", "source_ids": "B027 B028 B044 B045", "scope": "Benchmarked model/version sets; not every current provider endpoint."},
    {"claim_id": "C002", "claim": "Temporary complete occlusion is a hidden-state continuity problem, not only a negative-prompt problem.", "status": "supported_by_cross_domain_evidence_and_inference", "source_ids": "B012 B013 B014 B017 B027 B028", "scope": "Generation, video prediction, tracking, and evaluator evidence jointly support the control framing."},
    {"claim_id": "C003", "claim": "First and last frames constrain endpoints but do not guarantee the path, event order, or hidden state between them.", "status": "capability_fact_plus_mechanistic_inference", "source_ids": "M001 M014 M024 B003 B027", "scope": "No cited provider documentation guarantees intermediate path compliance."},
    {"claim_id": "C004", "claim": "Compositional generation remains difficult for attribute, action, motion, spatial, interaction, and count binding.", "status": "supported_by_benchmark", "source_ids": "B002 B043 B039 B041", "scope": "Model/version and benchmark scoped."},
    {"claim_id": "C005", "claim": "Prompt engineering alone is insufficient for many dynamic physical failures.", "status": "supported_by_benchmark", "source_ids": "B005 B045 B044", "scope": "Dynamic physics benchmarks; does not mean wording never helps."},
    {"claim_id": "C006", "claim": "Camera motion and actor/object motion should be represented as separate control tracks.", "status": "supported_by_control_research", "source_ids": "B031 B035 B037", "scope": "Strong design rationale; provider support varies."},
    {"claim_id": "C007", "claim": "Trajectory control alone may fail to specify environmental interaction consequences.", "status": "supported_by_control_research", "source_ids": "B038", "scope": "Method-specific observation; motivates causal effect graph."},
    {"claim_id": "C008", "claim": "Iterative generation-verification-correction can improve compositional control but inherits evaluator errors and added cost.", "status": "supported_by_research_and_inference", "source_ids": "B039 B029 B030 B034", "scope": "Framework-level result and evaluator limitation."},
    {"claim_id": "C009", "claim": "Automatic evaluators must not be treated as ground truth for fast temporal events, camera geometry, or localized failures.", "status": "supported_by_benchmark", "source_ids": "B029 B030 B031 B033 B034", "scope": "Evaluator/version and task scoped."},
    {"claim_id": "C010", "claim": "Aggregate quality scores can pass an artifact with one production-critical localized failure.", "status": "inference_supported_by_metric_design", "source_ids": "B001 B008 B009 B033 B034", "scope": "Requires interval-scoped CPCS assertions for confirmation in production."},
    {"claim_id": "C011", "claim": "XML, YAML, or JSON does not universally make a prompt-string video model more intelligent.", "status": "repository_policy_and_unverified_hypothesis_boundary", "source_ids": "R005 M001 M002 M007", "scope": "No cited official provider documents a universal structured prompt parser for generation semantics."},
    {"claim_id": "C012", "claim": "CPCS should keep canonical JSON as authority and compile one provider-native request representation.", "status": "repository_architecture_fact", "source_ids": "R001 R002 R005 R006", "scope": "Repository design decision."},
    {"claim_id": "C013", "claim": "The same seed is not a substitute for artifact-level identity and compliance verification.", "status": "official_capability_and_repository_policy", "source_ids": "M001 M002 M025 R008 R009", "scope": "Providers describe seeds differently; Wan explicitly disclaims identical output."},
    {"claim_id": "C014", "claim": "Exact contact, penetration avoidance, and hidden 3D geometry should not be promised by prompt-only generation.", "status": "benchmark_supported_engineering_conclusion", "source_ids": "B004 B005 B016 B032 B044", "scope": "Requires provider-specific qualification; visual controls or source motion are preferred for tight tolerances."},
    {"claim_id": "C015", "claim": "Complete opaque effects should be moved to postproduction when they must hide a precise continuity transition without changing world state.", "status": "workflow_recommendation", "source_ids": "B012 B013 B016 R009", "scope": "Engineering recommendation pending per-provider cost/quality ablation."},
    {"claim_id": "C016", "claim": "Current official interfaces differ materially in input modalities, durations, prompt limits, audio, keyframes, references, and edit controls.", "status": "officially_documented_capability", "source_ids": "M001 M002 M004 M006 M014 M017 M019 M020", "scope": "Version and interface scoped as of access date."},
    {"claim_id": "C017", "claim": "Official provider capability and marketing claims do not establish empirical reliability.", "status": "methodological_rule", "source_ids": "M004 M019 R003", "scope": "Package-wide evidence policy."},
    {"claim_id": "C018", "claim": "Sora 2 should not be represented as a currently available CPCS provider based on old launch material.", "status": "official_current_status", "source_ids": "M018", "scope": "Official page states consumer product unavailable from 2026-04-26; no current interface verified."},
    {"claim_id": "C019", "claim": "Ray 3.2 should be modeled as source-video modification, not T2V or I2V animation.", "status": "official_current_capability", "source_ids": "M017", "scope": "Current product guide as of 2026-05-27."},
    {"claim_id": "C020", "claim": "The minimum sufficient representation must include persistent entities, state deltas, ordered events, causal edges, spatial frames, visibility intervals, interaction/support constraints, camera/edit state, and verification assertions.", "status": "research_synthesis", "source_ids": "R006 R008 R009 B003 B012 B027 B028 B035 B038", "scope": "CPCS design conclusion; exact field shapes require governed schema review."},
]


# ---------------------------------------------------------------------------
# CPCS contract extensions and repository ownership map
# ---------------------------------------------------------------------------

OCCLUSION_CONTINUITY_CONTRACT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/occlusion-continuity-contract/1.0",
    "title": "CPCS Occlusion Continuity Contract candidate",
    "type": "object",
    "required": [
        "schema_version", "contract_id", "subject_id", "occluder_id", "pre_occlusion_state_ref",
        "occlusion_interval", "hidden_motion_path", "expected_reappearance_region", "identity_lock",
        "actor_count_lock", "state_change_allowed", "state_change_forbidden", "visibility_bridge",
        "verification_assertions"
    ],
    "properties": {
        "schema_version": {"const": "cpcs.occlusion_continuity_contract/1.0-candidate"},
        "contract_id": {"type": "string", "pattern": "^occlusion_[A-Za-z0-9._-]+$"},
        "subject_id": {"type": "string", "minLength": 1},
        "occluder_id": {"type": "string", "minLength": 1},
        "pre_occlusion_state_ref": {"type": "string", "minLength": 1},
        "occlusion_interval": {
            "type": "object",
            "required": ["start_seconds", "end_seconds", "visibility_state"],
            "properties": {
                "start_seconds": {"type": "number", "minimum": 0},
                "end_seconds": {"type": "number", "exclusiveMinimum": 0},
                "visibility_state": {"enum": ["partial", "complete", "off_screen", "submerged", "graphic_cover"]}
            },
            "additionalProperties": False
        },
        "hidden_motion_path": {
            "type": "object",
            "required": ["coordinate_frame", "start_region", "end_region", "trajectory_class", "control_asset_ref"],
            "properties": {
                "coordinate_frame": {"enum": ["screen_normalized", "camera_relative", "world_relative", "actor_relative"]},
                "start_region": {"type": "array", "minItems": 2, "maxItems": 4, "items": {"type": "number"}},
                "end_region": {"type": "array", "minItems": 2, "maxItems": 4, "items": {"type": "number"}},
                "trajectory_class": {"enum": ["stationary", "linear", "ballistic", "arc", "dive", "fall", "custom_control"]},
                "control_asset_ref": {"type": ["string", "null"]}
            },
            "additionalProperties": False
        },
        "expected_reappearance_region": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"type": "number", "minimum": 0, "maximum": 1}},
        "identity_lock": {"type": "boolean"},
        "actor_count_lock": {"type": "integer", "minimum": 0},
        "state_change_allowed": {"type": "array", "uniqueItems": True, "items": {"type": "string"}},
        "state_change_forbidden": {"type": "array", "uniqueItems": True, "items": {"type": "string"}},
        "visibility_bridge": {
            "type": "object",
            "required": ["kind", "subject_id", "asset_ref", "minimum_coverage_fraction"],
            "properties": {
                "kind": {"enum": ["none", "silhouette", "shadow", "bubble_trail", "partial_limb", "mask", "point_track", "pose_track", "depth_track"]},
                "subject_id": {"type": "string"},
                "asset_ref": {"type": ["string", "null"]},
                "minimum_coverage_fraction": {"type": "number", "minimum": 0, "maximum": 1}
            },
            "additionalProperties": False
        },
        "verification_assertions": {"type": "array", "minItems": 1, "items": {"type": "string"}}
    },
    "additionalProperties": False
}

STATE_LEDGER_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/state-ledger/1.0",
    "title": "CPCS State Ledger candidate",
    "type": "object",
    "required": ["schema_version", "ledger_id", "timebase", "entities", "transitions", "invariants"],
    "properties": {
        "schema_version": {"const": "cpcs.state_ledger/1.0-candidate"},
        "ledger_id": {"type": "string", "pattern": "^ledger_[A-Za-z0-9._-]+$"},
        "timebase": {"enum": ["seconds", "frames", "beats"]},
        "entities": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object",
                "required": ["entity_id", "entity_type", "initial_state", "persistent_attributes"],
                "properties": {
                    "entity_id": {"type": "string"},
                    "entity_type": {"enum": ["actor", "prop", "product", "environment", "effect", "audio_source"]},
                    "initial_state": {
                        "type": "object",
                        "required": ["exists", "visible", "count", "holder", "location_ref", "material_state"],
                        "properties": {
                            "exists": {"type": "boolean"},
                            "visible": {"type": "boolean"},
                            "count": {"type": "integer", "minimum": 0},
                            "holder": {"type": ["string", "null"]},
                            "location_ref": {"type": ["string", "null"]},
                            "material_state": {"type": "object"}
                        },
                        "additionalProperties": False
                    },
                    "persistent_attributes": {"type": "object"}
                },
                "additionalProperties": False
            }
        },
        "transitions": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["transition_id", "entity_id", "at", "from_state", "to_state", "cause_event_id", "reversible"],
                "properties": {
                    "transition_id": {"type": "string"},
                    "entity_id": {"type": "string"},
                    "at": {"type": "number", "minimum": 0},
                    "from_state": {"type": "object"},
                    "to_state": {"type": "object"},
                    "cause_event_id": {"type": ["string", "null"]},
                    "reversible": {"type": "boolean"}
                },
                "additionalProperties": False
            }
        },
        "invariants": {"type": "array", "uniqueItems": True, "items": {"type": "string"}}
    },
    "additionalProperties": False
}

SPATIAL_STATE_TRANSITION_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/spatial-state-transition/1.0",
    "title": "CPCS Spatial State Transition candidate",
    "type": "object",
    "required": ["schema_version", "transition_id", "coordinate_frame", "camera_state_ref", "before", "motion", "after", "invariants"],
    "properties": {
        "schema_version": {"const": "cpcs.spatial_state_transition/1.0-candidate"},
        "transition_id": {"type": "string"},
        "coordinate_frame": {"enum": ["screen_normalized", "camera_relative", "world_relative", "actor_relative"]},
        "camera_state_ref": {"type": "string"},
        "before": {"type": "object"},
        "motion": {
            "type": "object",
            "required": ["entity_id", "trajectory", "screen_lane_before", "screen_lane_after", "depth_lane_before", "depth_lane_after"],
            "properties": {
                "entity_id": {"type": "string"},
                "trajectory": {"type": "array", "minItems": 2, "items": {"type": "array", "minItems": 2, "maxItems": 4, "items": {"type": "number"}}},
                "screen_lane_before": {"enum": ["left", "center", "right", "offscreen_left", "offscreen_right"]},
                "screen_lane_after": {"enum": ["left", "center", "right", "offscreen_left", "offscreen_right"]},
                "depth_lane_before": {"type": "string"},
                "depth_lane_after": {"type": "string"}
            },
            "additionalProperties": False
        },
        "after": {"type": "object"},
        "invariants": {"type": "array", "items": {"type": "string"}}
    },
    "additionalProperties": False
}

CAUSAL_EVENT_GRAPH_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/causal-event-graph/1.0",
    "title": "CPCS Causal Event Graph candidate",
    "type": "object",
    "required": ["schema_version", "graph_id", "events", "edges", "terminal_state"],
    "properties": {
        "schema_version": {"const": "cpcs.causal_event_graph/1.0-candidate"},
        "graph_id": {"type": "string"},
        "events": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object",
                "required": ["event_id", "initiator_id", "target_id", "action", "onset", "apex", "consequence", "reaction_delay", "recovery"],
                "properties": {
                    "event_id": {"type": "string"},
                    "initiator_id": {"type": ["string", "null"]},
                    "target_id": {"type": ["string", "null"]},
                    "action": {"type": "string"},
                    "onset": {"type": "number", "minimum": 0},
                    "apex": {"type": "number", "minimum": 0},
                    "consequence": {"type": "string"},
                    "reaction_delay": {"type": "number", "minimum": 0},
                    "recovery": {"type": "string"}
                },
                "additionalProperties": False
            }
        },
        "edges": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["from_event", "to_event", "relation", "hard"],
                "properties": {
                    "from_event": {"type": "string"},
                    "to_event": {"type": "string"},
                    "relation": {"enum": ["causes", "enables", "prevents", "only_after", "before", "while", "terminates"]},
                    "hard": {"type": "boolean"}
                },
                "additionalProperties": False
            }
        },
        "terminal_state": {"type": "object"}
    },
    "additionalProperties": False
}

EVALUATOR_PROVENANCE_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/evaluator-provenance/1.0",
    "title": "CPCS Evaluator Provenance candidate",
    "type": "object",
    "required": ["schema_version", "evaluator_id", "version", "configuration_hash", "artifact_hash", "observable_dimension", "lane", "confidence", "known_blind_spots", "human_calibration_status"],
    "properties": {
        "schema_version": {"const": "cpcs.evaluator_provenance/1.0-candidate"},
        "evaluator_id": {"type": "string"},
        "version": {"type": "string"},
        "configuration_hash": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"},
        "artifact_hash": {"type": "string", "pattern": "^sha256:[0-9a-f]{64}$"},
        "observable_dimension": {"type": "string"},
        "lane": {"enum": ["direct", "semantic", "measured", "human_review"]},
        "confidence": {"type": ["number", "null"], "minimum": 0, "maximum": 1},
        "known_blind_spots": {"type": "array", "items": {"type": "string"}},
        "human_calibration_status": {"enum": ["not_calibrated", "calibrated_in_domain", "calibrated_out_of_domain", "human_only"]}
    },
    "additionalProperties": False
}

CONTRACT_SCHEMAS = {
    "schemas/OCCLUSION_CONTINUITY_CONTRACT.schema.json": OCCLUSION_CONTINUITY_CONTRACT_SCHEMA,
    "schemas/STATE_LEDGER.schema.json": STATE_LEDGER_SCHEMA,
    "schemas/SPATIAL_STATE_TRANSITION.schema.json": SPATIAL_STATE_TRANSITION_SCHEMA,
    "schemas/CAUSAL_EVENT_GRAPH.schema.json": CAUSAL_EVENT_GRAPH_SCHEMA,
    "schemas/EVALUATOR_PROVENANCE.schema.json": EVALUATOR_PROVENANCE_SCHEMA,
}

CONTRACT_EXAMPLES: dict[str, dict[str, Any]] = {
    "examples/occlusion_continuity_water_splash.json": {
        "schema_version": "cpcs.occlusion_continuity_contract/1.0-candidate",
        "contract_id": "occlusion_water_splash_b_dive",
        "subject_id": "actor_B",
        "occluder_id": "effect_water_column_01",
        "pre_occlusion_state_ref": "state://beat_04/actor_B",
        "occlusion_interval": {"start_seconds": 4.25, "end_seconds": 5.10, "visibility_state": "complete"},
        "hidden_motion_path": {
            "coordinate_frame": "screen_normalized",
            "start_region": [0.68, 0.58],
            "end_region": [0.72, 0.73],
            "trajectory_class": "dive",
            "control_asset_ref": "asset_pose_track_actor_B_001"
        },
        "expected_reappearance_region": [0.62, 0.62, 0.82, 0.90],
        "identity_lock": True,
        "actor_count_lock": 2,
        "state_change_allowed": ["actor_B.visible:false", "actor_B.pose:continued_dive"],
        "state_change_forbidden": ["actor_B.identity", "actor_B.costume", "actor_B.role", "actor_count", "world_layout"],
        "visibility_bridge": {"kind": "bubble_trail", "subject_id": "actor_B", "asset_ref": "asset_bubble_track_001", "minimum_coverage_fraction": 0.60},
        "verification_assertions": [
            "actor_B remains the same persistent entity throughout the hidden interval",
            "actor_B reappears only inside expected_reappearance_region",
            "actor_count remains exactly 2",
            "water column originates at actor_A kick impact point, not actor_B position"
        ]
    },
    "examples/state_ledger_two_actor_water_scene.json": {
        "schema_version": "cpcs.state_ledger/1.0-candidate",
        "ledger_id": "ledger_two_actor_water_scene",
        "timebase": "seconds",
        "entities": [
            {
                "entity_id": "actor_A", "entity_type": "actor",
                "initial_state": {"exists": True, "visible": True, "count": 1, "holder": None, "location_ref": "screen_lane_left", "material_state": {"costume": "orange_jacket_charcoal_base"}},
                "persistent_attributes": {"identity_lock": True, "role": "attacker", "screen_side_lock": "left"}
            },
            {
                "entity_id": "actor_B", "entity_type": "actor",
                "initial_state": {"exists": True, "visible": True, "count": 1, "holder": None, "location_ref": "screen_lane_right", "material_state": {"costume": "indigo_tunic_grey_trousers"}},
                "persistent_attributes": {"identity_lock": True, "role": "defender", "screen_side_lock": "right"}
            },
            {
                "entity_id": "water_plane", "entity_type": "environment",
                "initial_state": {"exists": True, "visible": True, "count": 1, "holder": None, "location_ref": "continuous_flat_plane", "material_state": {"surface_height": 0.0, "topology": "continuous_flat"}},
                "persistent_attributes": {"topology_lock": True}
            }
        ],
        "transitions": [
            {"transition_id": "t_actor_b_submerge", "entity_id": "actor_B", "at": 4.25, "from_state": {"visible": True}, "to_state": {"visible": False, "exists": True}, "cause_event_id": "event_B_dive", "reversible": True},
            {"transition_id": "t_actor_b_reappear", "entity_id": "actor_B", "at": 5.10, "from_state": {"visible": False, "exists": True}, "to_state": {"visible": True, "exists": True}, "cause_event_id": "event_B_surface", "reversible": True}
        ],
        "invariants": ["actor_count==2", "actor_A.left_of(actor_B)", "water_plane.surface_height==0.0", "no_new_props", "no_identity_or_costume_change"]
    },
    "examples/causal_event_graph_water_strike.json": {
        "schema_version": "cpcs.causal_event_graph/1.0-candidate",
        "graph_id": "graph_water_strike_sequence",
        "events": [
            {"event_id": "event_B_dive", "initiator_id": "actor_B", "target_id": None, "action": "dives below the kick line", "onset": 3.90, "apex": 4.25, "consequence": "actor_B is below the kick trajectory", "reaction_delay": 0.0, "recovery": "continues hidden dive path"},
            {"event_id": "event_A_kick_water", "initiator_id": "actor_A", "target_id": "water_plane", "action": "axe kick misses actor_B and strikes only the water", "onset": 4.05, "apex": 4.42, "consequence": "surface displacement begins at the kick impact point", "reaction_delay": 0.03, "recovery": "actor_A retracts and settles"},
            {"event_id": "event_water_column", "initiator_id": "water_plane", "target_id": None, "action": "water column rises from the kick impact point", "onset": 4.45, "apex": 4.85, "consequence": "brief opaque occlusion", "reaction_delay": 0.03, "recovery": "column collapses into centered ripples"}
        ],
        "edges": [
            {"from_event": "event_B_dive", "to_event": "event_A_kick_water", "relation": "only_after", "hard": True},
            {"from_event": "event_A_kick_water", "to_event": "event_water_column", "relation": "causes", "hard": True}
        ],
        "terminal_state": {"actor_A": "left, recovering", "actor_B": "right, submerged then reappearing", "water_plane": "same topology, centered ripples", "actor_count": 2}
    }
}

OWNER_BY_FAMILY = {
    "A": "lab/compiler universal score continuity/actions; lab/verification assertions; lab/second_brain evidence",
    "B": "lab/compiler entities/continuity/assets; lab/verification state checks",
    "C": "lab/compiler entities/interactions/continuity; lab/verification identity-role checks",
    "D": "lab/compiler scenes/shots/actions/camera; lab/verification geography checks",
    "E": "lab/compiler beats/actions/editing; lab/verification event-graph checks",
    "F": "lab/compiler actions/interactions/audio; lab/verification causal assertions",
    "G": "lab/compiler interactions/motion/camera; lab/verification measured/human lanes",
    "H": "lab/compiler motion/interactions; lab/verification support/momentum metrics",
    "I": "lab/compiler interactions/style/continuity; lab/verification material-response checks",
    "J": "lab/compiler camera/motion/shots; lab/verification camera/actor separation",
    "K": "lab/compiler editing/continuity/style; lab/verification cut/effect classification",
    "L": "lab/compiler motion/style/performance; lab/verification recovery assertions",
    "M": "lab/compiler provider build and adapter; lab/experiments format arms",
    "N": "lab/compiler constraints/warnings/loss report; shot planner; lab/experiments capacity staircases",
    "O": "lab/compiler audio/actions/beats; lab/verification AV anchors",
    "P": "lab/verification; lab/second_brain immutable evidence and human calibration"
}

REPOSITORY_FILES_REVIEWED = [
    "AGENTS.md", "ARCHITECTURE.md", "lab/AGENTS.md", "lab/CONTROL_SURFACE.md",
    "lab/FORMAT_CONTROL_MAP.md", "lab/UNIVERSAL_MOTION_SKELETON.md", "lab/compiler/AGENTS.md",
    "lab/compiler/schemas/universal_score.schema.json", "lab/compiler/providers/veo_3_1.yaml",
    "lab/verification/AGENTS.md", "lab/verification/schemas/compliance_report.schema.json",
    "lab/second_brain/AGENTS.md", "lab/second_brain/IMPLEMENTATION_PLAN.md"
]

REPOSITORY_GAPS = [
    {
        "gap_id": "repo_gap_001",
        "finding": "The requested root REPO_CONTINUITY_IMPLEMENTATION_PLAN.md was not found in the inspected tree.",
        "impact": "The research uses ARCHITECTURE.md plus lab/second_brain/IMPLEMENTATION_PLAN.md as the nearest current architecture/continuity owners; this substitution must be reviewed by the repository owner.",
        "action": "Do not create a duplicate plan. Confirm whether the root file was renamed, moved, or never committed."
    },
    {
        "gap_id": "repo_gap_002",
        "finding": "Only Veo 3.1 is represented as a versioned compiler provider capability profile in the inspected repository.",
        "impact": "Seedance, Kling, Runway, MiniMax, Wan, LTX, and other rows in this research remain knowledge records, not executable adapters.",
        "action": "Add provider profiles one at a time through the existing compiler provider schema after official-interface and live-request qualification."
    },
    {
        "gap_id": "repo_gap_003",
        "finding": "The universal score has existing top-level owners but several relevant objects remain structurally open rather than typed for hidden state, state transitions, and causal events.",
        "impact": "Prompt adapters can serialize intent, but cannot deterministically prove that all continuity obligations were represented.",
        "action": "Review the candidate schemas in this package as minimal nested extensions under existing owners; do not add a second root score."
    },
    {
        "gap_id": "repo_gap_004",
        "finding": "Current verification supports artifact identity/basic media properties and a small number of closed measurements, but not the complete failure metric catalog.",
        "impact": "Most new failure assertions require new calibrated measured/semantic/human lanes before they can block or promote a run.",
        "action": "Implement metrics incrementally behind lab/verification, starting with actor/object count, event order, screen side, effect origin, and occlusion reappearance region."
    },
    {
        "gap_id": "repo_gap_005",
        "finding": "No authorized provider render campaign or human calibration bundle was available in this session.",
        "impact": "The package cannot report provider-specific success rates or universal complexity thresholds.",
        "action": "Execute the pre-registered repeated-seed fixtures and record raw prompts, requests, seeds, outputs, evaluator versions, and human verdicts."
    }
]


def overlap_row(record: dict[str, Any]) -> dict[str, str]:
    family = record["family_id"]
    if family == "P":
        coverage = "partial"
        missing_mitigation = "Failure-specific evaluator arbitration and calibration policy are not yet complete."
    elif family in {"M", "N"}:
        coverage = "partial"
        missing_mitigation = "Compiler has authority/loss surfaces but lacks calibrated provider-specific attention and complexity limits."
    else:
        coverage = "partial"
        missing_mitigation = "Existing canonical owners exist, but the named failure contract and escalation rule are not yet first-class."
    return {
        "failure_id": record["failure_id"],
        "failure_name": record["name"],
        "existing_owner": OWNER_BY_FAMILY[family],
        "existing_coverage": coverage,
        "missing_evidence": "No CPCS repeated-seed provider/model/version distribution is recorded for this exact failure fixture.",
        "missing_mitigation": missing_mitigation,
        "missing_test": record["regression_fixtures"][0],
        "recommended_owner": FAMILY_META[family]["owner"],
        "parallel_owner_prohibited": "true"
    }


REPOSITORY_OVERLAP_ROWS = [overlap_row(r) for r in FAILURE_RECORDS]

FAILURE_MITIGATION_ROWS: list[dict[str, str]] = []
for r in FAILURE_RECORDS:
    primary = r["mitigations"][0]
    fallback = r["mitigations"][1]
    FAILURE_MITIGATION_ROWS.append({
        "failure_id": r["failure_id"],
        "family_id": r["family_id"],
        "family_name": r["family_name"],
        "failure_name": r["name"],
        "trigger_conditions": " | ".join(r["trigger_conditions"]),
        "observable_symptoms": " | ".join(r["observed_symptoms"]),
        "primary_level": primary["level"],
        "primary_method": primary["method"],
        "fallback_level": fallback["level"],
        "fallback_method": fallback["method"],
        "verification_metrics": " ".join(r["verification_metrics"]),
        "evidence_strength": primary["evidence_strength"],
        "empirical_confidence": r["empirical_confidence"],
        "render_campaign_status": r["cpcs_render_campaign_status"]
    })


# F — Contact, penetration, balance, support, and physics (8)
add_failure(
    "F01", "Contact, balance, and physics", "False or missing contact",
    "The output shows contact when a staged miss/near-contact was requested, or fails to show contact when contact is required.",
    ["fast limbs", "motion blur", "effect-obscured apex", "camera-cheated impact", "monocular depth ambiguity", "multiple nearby targets"],
    ["limb stops short without reaction", "reaction occurs with a visible gap", "limb visibly intersects despite a miss", "impact effect masks an incorrect contact"],
    ["mechanism://physical_constraint_absence", "mechanism://coordinate_frame_ambiguity", "mechanism://evaluator_observability_gap"],
    ["B004", "B005", "B017", "B018", "B019", "B020"],
    ["interactions", "actions", "shots", "motion", "verification_requirements"],
    ["'hits' without contact type/frame/target region", "negative-only 'does not hit'", "effect used to hide all interaction geometry"],
    ("L2", "Type the interaction as physical contact, staged near-contact, camera-cheated contact, effect-obscured near-contact, grasp, or surface contact; encode separation/contact threshold, target region, apex frame, and reaction timing.", "Prevents semantically different contact modes from collapsing into one verb."),
    ("L4", "Provide pose/mask/depth/keyframe control at the apex and first reaction frame.", "Directly constrains the interaction geometry at the decisive frames."),
    ["metric_contact_distance", "metric_reaction_latency_error", "metric_causal_edge_accuracy", "metric_human_readability"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Use a camera-cheated angle, foreground occlusion, or cut on impact instead of requiring exact full-body contact.", "Preserves perceived force while reducing 3D geometry demands."),
)
add_failure(
    "F02", "Contact, balance, and physics", "Body, limb, or object penetration",
    "Bodies, limbs, held objects, clothing, or surfaces occupy incompatible space beyond a permitted stylized smear interval.",
    ["grapples", "crossed limbs", "close camera", "fast motion", "occlusion", "nonrigid clothing", "complex props"],
    ["limbs pass through torsos", "feet sink into floor", "object penetrates hand", "bodies fuse", "surface contact has no boundary"],
    ["mechanism://physical_constraint_absence", "mechanism://entity_binding_ambiguity", "mechanism://underdetermined_hidden_state"],
    ["B004", "B005", "B016", "B018"],
    ["interactions", "motion", "entities", "style", "verification_requirements"],
    ["contact described without allowed overlap", "multiple actors share silhouette", "stylized deformation has no recovery deadline"],
    ("L2", "Encode collision pairs, permitted contact regions, maximum projected overlap, deformation window, and required separability/recovery frame.", "Defines which overlaps are intended, temporary, or prohibited."),
    ("L4", "Use pose, depth, segmentation, or control-video trajectories with distinct actor/object layers.", "Constrains topology and relative depth."),
    ["metric_penetration_duration", "metric_contact_distance", "metric_depth_order_accuracy", "metric_anatomy_recovery_latency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Composite separately generated actors/props with tracked occlusion mattes or repair penetrations frame-locally.", "Provides deterministic layer ordering when native interaction fails."),
)
add_failure(
    "F03", "Contact, balance, and physics", "Foot skating or support loss",
    "A planted foot slides, detaches, sinks, or changes support role without an authored step, pivot, jump, or camera explanation.",
    ["standing turns", "dance/fight footwork", "camera tracking", "low floor texture", "motion blur", "long holds", "stylized locomotion"],
    ["planted foot drifts", "body glides", "foot floats above floor", "support foot swaps instantly", "landing point moves after contact"],
    ["mechanism://physical_constraint_absence", "mechanism://camera_scene_entanglement"],
    ["B004", "B005", "B021"],
    ["motion", "interactions", "camera", "continuity.state_ledger", "verification_requirements"],
    ["locomotion described without support phases", "camera movement and body translation combined", "no floor/contact reference"],
    ("L2", "Compile support phases: support foot, contact interval, pivot allowance, base of support, takeoff, landing target, and settle.", "Makes foot contact a state machine rather than an emergent detail."),
    ("L4", "Use pose/root trajectories, foot-contact tracks, floor plane/depth, or a control video.", "Directly constrains support points and ground relation."),
    ["metric_foot_slip_distance", "metric_support_plausibility", "metric_camera_actor_entanglement", "metric_momentum_continuity"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L7", "Regenerate the smallest support interval with fixed boundary poses and preserve accepted upper-body motion where possible.", "Targets the localized slip without discarding the full shot."),
)
add_failure(
    "F04", "Contact, balance, and physics", "Weightless takeoff, landing, or recovery",
    "A body launches, flies, lands, rebounds, or recovers without readable weight transfer, impulse, compression, deceleration, or settle.",
    ["jump or fall", "anime launch", "impact", "camera shake", "short duration", "prompt emphasizes pose over transition"],
    ["instant airborne state", "soft/no landing compression", "body stops dead", "no recoil/follow-through", "gravity direction feels inconsistent"],
    ["mechanism://physical_constraint_absence", "mechanism://temporal_dependency_collapse"],
    ["B004", "B005", "B006", "B026"],
    ["motion", "interactions", "actions", "beats", "style"],
    ["start and end poses only", "'jumps' without support/flight/landing phases", "impact effect substitutes for body mechanics"],
    ("L2", "Represent weight transfer, takeoff impulse, flight trajectory, landing target, compression, rebound, recovery, and settle; for stylization, lock the causal skeleton while allowing exaggeration.", "Preserves perceptual weight without demanding literal simulation."),
    ("L4", "Use pose/root trajectory control and boundary keyframes for support, apex, landing, and recovery.", "Constrains the phases most responsible for weight perception."),
    ["metric_support_plausibility", "metric_momentum_continuity", "metric_temporal_event_error", "metric_human_readability"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Split launch/flight/landing into shots or use an authored hold/smear between physically anchored phases.", "Lets stylization occur between stable causal anchors."),
)
add_failure(
    "F05", "Contact, balance, and physics", "Momentum discontinuity",
    "Actor or object velocity, direction, rotation, or impulse changes abruptly without a visible force, contact, support change, cut, or authored time manipulation.",
    ["rapid direction change", "collision", "camera move", "speed ramp", "effect obscures transition", "long hidden interval"],
    ["instant reversal", "constant-speed arc", "momentum vanishes", "recoil direction wrong", "object accelerates before touch"],
    ["mechanism://physical_constraint_absence", "mechanism://camera_scene_entanglement", "mechanism://underdetermined_hidden_state"],
    ["B004", "B005", "B006", "B021", "B025"],
    ["motion", "actions", "interactions", "camera", "editing"],
    ["trajectory endpoints without velocity conditions", "camera and object acceleration conflated", "genre adjective replaces force/cause"],
    ("L2", "Encode trajectory segments with entry/exit direction, qualitative speed profile, impulse source, deceleration, and allowed stylized discontinuities.", "Makes unexplained changes detectable while preserving authored exaggeration."),
    ("L4", "Use trajectory/control video or keyframes with velocity-aware spacing rather than only endpoint images.", "Carries motion continuity into conditioning."),
    ["metric_momentum_continuity", "metric_causal_edge_accuracy", "metric_camera_motion_agreement", "metric_temporal_event_error"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Place a cut, smear, or hold only where a discontinuity is intentional and restore a defined post-transition trajectory.", "Turns an uncontrolled jump into an authored edit convention."),
)
add_failure(
    "F06", "Contact, balance, and physics", "Grip, grasp, or support failure",
    "A hand, arm, seat, wall, floor, or support object does not carry the intended load or loses contact while the supported object/body continues as if attached.",
    ["lifting", "hanging", "carrying", "sitting", "leaning", "two-hand support", "occluded contact"],
    ["floating body/object", "hand not touching handle", "seat passes through body", "support changes without transition", "load moves independently"],
    ["mechanism://physical_constraint_absence", "mechanism://state_representation_gap", "mechanism://entity_binding_ambiguity"],
    ["B004", "B005", "B017"],
    ["interactions", "motion", "entities", "continuity.state_ledger", "verification_requirements"],
    ["'carries/supports' without contact and load relation", "support surface not identified", "occluded grip assumed"],
    ("L2", "Compile support/grasp edges with contact regions, load bearer, supported entity, interval, release condition, and required reaction to support loss.", "Makes support a causal relation rather than a visual coincidence."),
    ("L4", "Use contact-region masks, hand/body pose, or a control video that keeps support points aligned.", "Constrains attachment and load-bearing geometry."),
    ["metric_contact_distance", "metric_object_state_transition", "metric_support_plausibility", "metric_causal_edge_accuracy"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Use inserts or separate shots for establish-grip, load motion, and release.", "Reduces continuous topology demands."),
)
add_failure(
    "F07", "Contact, balance, and physics", "Contact-target or reaction mismatch",
    "Contact occurs at one region or actor while the effect/reaction is assigned to another region or entity.",
    ["multiple actors", "crossed limbs", "effect obscures contact", "fast cuts", "similar body regions", "off-axis camera"],
    ["head reacts to torso contact", "wrong actor recoils", "object deforms away from touch point", "effect appears on wrong side"],
    ["mechanism://entity_binding_ambiguity", "mechanism://physical_constraint_absence", "mechanism://temporal_dependency_collapse"],
    ["B002", "B004", "B005", "B017"],
    ["interactions", "actions", "entities", "motion", "verification_requirements"],
    ["contact and reaction in separate clauses without shared event ID", "target region omitted", "multiple simultaneous contacts"],
    ("L2", "Use one interaction ID linking initiator, contact limb/object, target entity/region, contact type, consequence, and reaction chain.", "Prevents local geometry and downstream response from being assigned independently."),
    ("L4", "Provide keyframes/masks at contact and first reaction, with per-entity target labels.", "Constrains both the apex and consequence ownership."),
    ["metric_contact_distance", "metric_role_assignment_accuracy", "metric_causal_edge_accuracy", "metric_effect_origin_error"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Limit each shot to one critical contact chain or isolate simultaneous contacts into separate beats/shots.", "Reduces assignment ambiguity."),
)
add_failure(
    "F08", "Contact, balance, and physics", "Scale, center-of-mass, or body-proportion instability",
    "Body or object proportions and apparent center of mass change in ways that invalidate balance, reach, contact, or trajectory.",
    ["wide-to-close transition", "perspective exaggeration", "anime foreshortening", "camera zoom", "occlusion", "long complex action"],
    ["limbs lengthen permanently", "body mass shifts without pose", "reach becomes impossible", "landing balance changes", "object scale changes during contact"],
    ["mechanism://physical_constraint_absence", "mechanism://camera_scene_entanglement", "mechanism://graphic_world_state_conflation"],
    ["B004", "B016", "B017"],
    ["entities", "motion", "style", "camera", "continuity.state_ledger"],
    ["perspective exaggeration has no recovery frame", "screen size treated as body scale", "no immutable body-proportion signature"],
    ("L2", "Separate immutable body/object proportions from temporary perspective deformation; define center-of-mass/support phases and a recovery deadline.", "Allows stylized projection while protecting physical identity and balance."),
    ("L3", "Use full-body multi-view references and source/destination keyframes with consistent scale anchors.", "Provides proportion and staging anchors."),
    ["metric_identity_continuity", "metric_support_plausibility", "metric_anatomy_recovery_latency", "metric_camera_motion_agreement"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Use 2D/3D animation or compositing for shots where exact reach, scale, and balance are non-negotiable.", "Moves critical geometry to a controllable production system."),
)

# G — Fluid, cloth, hair, debris, and VFX (7)
add_failure(
    "G01", "Fluid, material, and VFX", "Splash without surface displacement",
    "A splash, ripple, wake, or water column appears without the corresponding entry/contact displacement or appears before it.",
    ["water entry", "strike near water", "effect-heavy prompt", "contact obscured", "fast action", "multiple possible impact points"],
    ["splash precedes entry", "water remains flat under body", "column appears with no impact", "ripples are not centered on contact"],
    ["mechanism://physical_constraint_absence", "mechanism://temporal_dependency_collapse"],
    ["B004", "B005", "B006", "B026"],
    ["interactions", "motion", "actions", "style", "verification_requirements"],
    ["'splash' listed as an independent visual", "impact point omitted", "effect intensity emphasized over displacement cause"],
    ("L2", "Compile the solid–fluid event chain: entrant/impactor, surface contact point, displacement onset, splash origin/peak/decay, ripples, and resulting subject state.", "Prevents the effect from being scheduled independently of its cause."),
    ("L4", "Use masks/trajectory/control video or a simulated/precomposed displacement guide at the contact interval.", "Constrains the causal geometry of the fluid response."),
    ["metric_causal_edge_accuracy", "metric_effect_origin_error", "metric_effect_decay_error", "metric_material_state_consistency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Generate clean body motion and add splash/ripples from the verified contact point in postproduction.", "Makes the fluid consequence deterministic."),
)
add_failure(
    "G02", "Fluid, material, and VFX", "Fluid treated as a solid or noninteractive plane",
    "Water, mud, snow, smoke, or another material fails to deform/displace appropriately, supports a body incorrectly, or ignores penetration/submersion.",
    ["standing/running on water unintentionally", "submersion", "shallow/deep ambiguity", "stylized reflection plane", "fast entry", "low surface texture"],
    ["actor stands on water", "body does not displace fluid", "feet never submerge", "surface clips through body", "fluid behaves like glass"],
    ["mechanism://physical_constraint_absence", "mechanism://state_representation_gap"],
    ["B004", "B005", "B026"],
    ["scenes", "interactions", "motion", "continuity.state_ledger", "style"],
    ["water named only as background", "depth and support behavior unspecified", "anime surface-running convention not explicitly allowed/forbidden"],
    ("L2", "Declare material type, surface/depth field, support policy, penetration/submersion state, displacement response, and whether stylized surface-running is allowed.", "Separates environment appearance from interaction physics."),
    ("L4", "Provide depth/mask/control media or a simulated interaction plate for the material boundary.", "Constrains the contact/submersion topology."),
    ["metric_material_state_consistency", "metric_contact_distance", "metric_penetration_duration", "metric_support_plausibility"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Composite the actor with a simulated or stock material interaction layer.", "Provides reliable material response when prompt-only generation plateaus."),
)
add_failure(
    "G03", "Fluid, material, and VFX", "Effect origin follows the wrong actor or location",
    "Splash, smoke, dust, debris, fire, light, or an impact flash originates from the moving actor/effect mass rather than the causal contact point or target region.",
    ["moving actor and static impact point", "camera tracking", "large effect", "multiple contacts", "occlusion", "long effect duration"],
    ["water column follows actor", "dust spawns behind wrong foot", "flash appears on wrong body", "debris source drifts"],
    ["mechanism://physical_constraint_absence", "mechanism://entity_binding_ambiguity", "mechanism://camera_scene_entanglement"],
    ["B004", "B005", "B017", "B021"],
    ["interactions", "motion", "camera", "style", "verification_requirements"],
    ["effect attached grammatically to actor instead of event location", "origin not distinguished from trajectory", "camera-relative point used as world point"],
    ("L2", "Bind the effect to a causal event ID and fixed/trajectory-aware world-space origin, with onset, expansion, advection, and decay separated from the actor track.", "Prevents effect ownership from following the most salient moving subject."),
    ("L4", "Use an origin mask/point, control video, or reference storyboard marking the causal location.", "Provides direct localization."),
    ["metric_effect_origin_error", "metric_causal_edge_accuracy", "metric_camera_motion_agreement", "metric_material_state_consistency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Add the effect as a tracked world-space composite after verifying the causal point.", "Guarantees effect origin and camera compensation."),
)
add_failure(
    "G04", "Fluid, material, and VFX", "Effect onset, decay, or persistence mismatch",
    "A VFX/material response starts too early/late, persists after its cause, disappears instantly, or changes topology without a new event.",
    ["smoke/splash/debris", "long clip", "cut/flash", "multiple effects", "audio cue", "no lifecycle specification"],
    ["smoke never clears", "splash freezes", "debris vanishes", "flash lasts too long", "effect begins before cause"],
    ["mechanism://temporal_dependency_collapse", "mechanism://state_representation_gap", "mechanism://graphic_world_state_conflation"],
    ["B003", "B010", "B017"],
    ["actions", "interactions", "style", "editing", "continuity.state_ledger"],
    ["effect adjective without lifecycle", "effect and cut share timing token", "no post-effect state"],
    ("L2", "Represent effect lifecycle as onset, peak, expansion/advection, decay, end, residual state, and relation to any edit boundary.", "Makes premature or persistent effects explicitly invalid."),
    ("L6", "Generate or composite the effect separately with an authored opacity/area envelope.", "Provides deterministic lifecycle timing."),
    ["metric_effect_decay_error", "metric_causal_edge_accuracy", "metric_edit_graphic_classification", "metric_material_state_consistency"],
    "requires_postproduction",
    additional_mitigation=("L7", "Replace only the failing effect interval/layer and reverify preserved body/camera motion.", "Avoids full-scene resampling."),
)
add_failure(
    "G05", "Fluid, material, and VFX", "Cloth or hair interpenetration and attachment drift",
    "Cloth or hair passes through bodies/objects, detaches from its anchor, changes length/topology, or follows the wrong motion.",
    ["fast turns", "close contact", "wind", "long hair/loose cloth", "occlusion", "grapple", "motion blur"],
    ["hair enters face/body", "cape detaches", "sleeve merges with arm", "cloth changes length", "secondary motion leads primary motion"],
    ["mechanism://physical_constraint_absence", "mechanism://entity_binding_ambiguity"],
    ["B004", "B016", "B018"],
    ["entities", "motion", "interactions", "style", "continuity.state_ledger"],
    ["cloth/hair treated only as appearance", "anchors and collision bodies unspecified", "too many overlapping secondary motions"],
    ("L2", "Define material anchor regions, allowed deformation, collision exclusions, follow-through lag, maximum topology change, and recovery/settle state.", "Separates attachment and secondary motion from generic style."),
    ("L4", "Use masks, pose/control video, or reference motion with clear silhouette and limited overlap.", "Constrains attachment and gross trajectory."),
    ["metric_penetration_duration", "metric_identity_continuity", "metric_material_state_consistency", "metric_anatomy_recovery_latency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Simulate/composite hair or cloth separately for hero shots with strict collision requirements.", "Moves secondary dynamics to a controllable system."),
)
add_failure(
    "G06", "Fluid, material, and VFX", "Debris trajectory or source mismatch",
    "Debris, glass, mud, snow, sparks, or fragments emerge from the wrong source, travel against the causal impulse, duplicate, or disappear inconsistently.",
    ["collision/destruction", "multiple breakable objects", "camera movement", "dense particles", "occlusion", "long persistence"],
    ["fragments originate in empty space", "fly toward impact", "duplicate object remains intact", "debris vanishes mid-flight", "wrong material fragments"],
    ["mechanism://physical_constraint_absence", "mechanism://state_representation_gap", "mechanism://camera_scene_entanglement"],
    ["B004", "B005", "B006", "B026"],
    ["interactions", "entities", "motion", "continuity.state_ledger", "style"],
    ["'explodes into debris' without source-state transition", "no fragment/material identity", "impulse direction omitted"],
    ("L2", "Encode source object, destruction-state transition, fragment material/count range, origin region, impulse direction, lifespan, and residual state.", "Links debris to conservation-like visual bookkeeping without pretending to run a simulator."),
    ("L6", "Create destruction/debris in a simulation or compositing pass using the verified collision point and camera track.", "Provides deterministic source, direction, and persistence."),
    ["metric_causal_edge_accuracy", "metric_effect_origin_error", "metric_effect_decay_error", "metric_object_state_transition"],
    "requires_postproduction",
    additional_mitigation=("L5", "Cut on the destruction event and establish the post-destruction state in a separate shot.", "Reduces the need to preserve source and fragment states in one sample."),
)
add_failure(
    "G07", "Fluid, material, and VFX", "Water level, topology, wetness, or ripple-state drift",
    "The environment's material state changes without cause: water level/plane topology shifts, wet clothing resets, ripples relocate, or disturbed surfaces become pristine.",
    ["camera move", "multi-shot", "submersion", "long clip", "large splash", "lighting/reflection change"],
    ["water plane rises/falls", "shoreline changes", "ripples move away from impact", "wet actor becomes dry", "surface resets after cut"],
    ["mechanism://state_representation_gap", "mechanism://camera_scene_entanglement", "mechanism://graphic_world_state_conflation"],
    ["B003", "B011", "B016", "B017"],
    ["scenes", "continuity.state_ledger", "interactions", "camera", "editing"],
    ["material state not carried across shots", "reflection/lighting change interpreted as topology", "no residual-state ledger"],
    ("L2", "Store environment material state—surface plane/depth, disturbance fields, wetness, residual ripples, and legal decay—at every beat/shot boundary.", "Prevents the environment from silently reverting to its initial condition."),
    ("L3", "Use state-specific environment references/keyframes and a shared background plate across shots.", "Anchors topology and residual state visually."),
    ["metric_material_state_consistency", "metric_effect_decay_error", "metric_camera_motion_agreement", "metric_object_state_transition"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Use a fixed environment plate or simulation/composite for persistent fluid state.", "Makes material continuity deterministic across clips."),
)

# H — Camera, editing, graphic discontinuity, and anime recovery (7)
add_failure(
    "H01", "Camera, edit, and anime discontinuity", "Camera pan or tracking becomes actor/world movement",
    "The model satisfies a camera instruction by translating actors/backgrounds, freezing locomotion, or altering world-space trajectories.",
    ["pan/track plus complex action", "low-texture background", "static reference image", "multiple moving subjects", "short clip", "parallax ambiguity"],
    ["actor slides with frame", "background rotates while camera appears static", "locomotion stops during tracking", "screen motion correct but world motion wrong"],
    ["mechanism://camera_scene_entanglement", "mechanism://coordinate_frame_ambiguity"],
    ["B021", "R004", "R006"],
    ["camera", "motion", "shots", "scenes", "verification_requirements"],
    ["camera and actor motion in one undifferentiated sentence", "screen-space path used as world trajectory", "no background/camera reference"],
    ("L2", "Compile independent world-space actor tracks, screen-space projections, camera translation/rotation/lens, background motion, and edit events.", "Lets verification distinguish a correct frame composition from a wrong physical realization."),
    ("L4", "Provide separate camera/control trajectory or a reference/control video while holding actor motion simple.", "Constrains camera motion independently."),
    ["metric_camera_motion_agreement", "metric_camera_actor_entanglement", "metric_screen_direction_consistency", "metric_momentum_continuity"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Generate actor motion with a simpler/locked camera, then add camera motion in a separate shot or postproduction transform where feasible.", "Reduces entanglement at generation time."),
)
add_failure(
    "H02", "Camera, edit, and anime discontinuity", "Zoom/lens change causes scale or geometry inconsistency",
    "A zoom, dolly, lens, or framing change alters subject body/object dimensions, world distance, or perspective inconsistently.",
    ["rapid zoom", "dolly zoom", "close-up transition", "wide-angle exaggeration", "reference image", "complex pose"],
    ["subject grows physically", "limbs stretch", "distance changes without locomotion", "background parallax wrong", "product proportions drift"],
    ["mechanism://camera_scene_entanglement", "mechanism://state_representation_gap"],
    ["B016", "B021"],
    ["camera", "entities", "shots", "continuity.state_ledger", "style"],
    ["'zoom in' without optical/dolly distinction", "subject screen-size target treated as world scale", "no recovery after perspective exaggeration"],
    ("L2", "Separate optical zoom, focal-length change, dolly translation, crop, and subject/world scale; lock immutable geometry and expected perspective behavior.", "Prevents framing operations from changing object identity or distance."),
    ("L3", "Provide start/end frames with consistent subject geometry and known camera intent.", "Anchors the projection endpoints."),
    ["metric_camera_motion_agreement", "metric_identity_continuity", "metric_spatial_relation_accuracy", "metric_anatomy_recovery_latency"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Perform simple crop/zoom/reframe in postproduction when no true parallax is required.", "Eliminates unnecessary generative resynthesis."),
)
add_failure(
    "H03", "Camera, edit, and anime discontinuity", "Tilt, whip, orbit, or shake induces teleportation or axis error",
    "A rapid camera rotation/impulse causes actors to jump vertically/horizontally, reverse lanes, or reset world position.",
    ["whip pan", "sky-to-ground tilt", "orbit", "impact shake", "full-frame blur", "complex choreography"],
    ["actor teleports", "ground relation changes", "screen sides reverse", "camera shake deforms body", "world position resets after blur"],
    ["mechanism://camera_scene_entanglement", "mechanism://coordinate_frame_ambiguity", "mechanism://graphic_world_state_conflation"],
    ["B017", "B021", "R004"],
    ["camera", "shots", "motion", "editing", "continuity.state_ledger"],
    ["large camera move and dense action combined", "no pre/post camera transform", "blur interval treated as unobserved scene reset"],
    ("L2", "Encode the camera transform, unchanged world-state invariants, pre/post screen projection, and whether the interval is camera motion, graphic blur, or edit.", "Protects world continuity through rapid image-space change."),
    ("L3", "Use first/last frames or storyboard panels with identical world state and the intended camera transform.", "Anchors both sides of the ambiguous interval."),
    ["metric_camera_motion_agreement", "metric_reappearance_position_error", "metric_axis_crossing_count", "metric_edit_graphic_classification"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L5", "Split the camera move from the role/contact-critical action or use an explicit cut with a bridge frame.", "Avoids simultaneous camera and choreography reconstruction."),
)
add_failure(
    "H04", "Camera, edit, and anime discontinuity", "Motion blur destroys identity or topology",
    "Blur/smear intervals lose actor boundaries, face/body identity, limb ownership, or prop attachment, and the damaged reconstruction persists afterward.",
    ["fast motion", "long shutter aesthetic", "full-body overlap", "whip pan", "low resolution", "effect-heavy contact"],
    ["face melts", "limbs duplicate", "actors fuse", "prop detaches", "identity changes after blur"],
    ["mechanism://underdetermined_hidden_state", "mechanism://entity_binding_ambiguity", "mechanism://graphic_world_state_conflation"],
    ["B015", "B016", "B017", "B019", "B021"],
    ["style", "motion", "entities", "continuity.visibility_intervals", "continuity.state_ledger"],
    ["blur requested without exposure window/recovery frame", "identity-critical close contact hidden entirely", "blur and cut conflated"],
    ("L2", "Treat blur/smear as a bounded visibility interval with stable entity IDs, silhouette anchors, permitted deformation, and mandatory post-blur recovery frame.", "Allows temporary loss of detail without authorizing persistent identity/topology change."),
    ("L3", "Provide a clean post-blur keyframe and, when possible, a trajectory/silhouette reference through the blur.", "Anchors recovery and coarse motion."),
    ["metric_identity_continuity", "metric_anatomy_recovery_latency", "metric_actor_count_consistency", "metric_occlusion_continuity"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Add motion blur/smear as a postproduction effect over clean accepted motion.", "Separates stylistic blur from identity generation."),
)
add_failure(
    "H05", "Camera, edit, and anime discontinuity", "Flash, wipe, black frame, or cut causes scene reset",
    "A graphic or editorial discontinuity resets identity, costume, layout, lighting, object state, or art style when world state should remain continuous.",
    ["impact flash", "one-frame monochrome", "smoke/splash wipe", "black frame", "hard cut", "transformation burst"],
    ["new background", "costume changes", "actors swap", "object state resets", "style changes", "teleportation after effect"],
    ["mechanism://graphic_world_state_conflation", "mechanism://underdetermined_hidden_state", "mechanism://state_representation_gap"],
    ["B003", "B010", "B015", "B017"],
    ["editing", "style", "continuity.state_ledger", "entities", "shots"],
    ["effect described as 'transition' without world-state policy", "pre/post states not linked", "transformation vocabulary used for impact accent"],
    ("L2", "Classify the interval as graphic discontinuity, camera cut, world-state discontinuity, temporal hold, blur, or occlusion; enumerate state fields that must remain unchanged.", "Stops an editorial effect from implicitly authorizing a world reset."),
    ("L3", "Use matched pre/post keyframes or first/last frames with unchanged identity/layout/state.", "Anchors continuity across the discontinuity."),
    ["metric_edit_graphic_classification", "metric_identity_continuity", "metric_object_state_transition", "metric_spatial_relation_accuracy"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Apply the flash/wipe/black frame in editing over a continuous accepted clip or between independently continuity-locked shots.", "Makes the discontinuity deterministic and nonsemantic."),
)
add_failure(
    "H06", "Camera, edit, and anime discontinuity", "Smear or perspective deformation persists as anatomy",
    "A temporary stylized deformation—elongation, extra contour, perspective enlargement, duplicated smear limb—fails to resolve into the intended destination anatomy.",
    ["anime smear", "impact pose", "speed lines", "extreme foreshortening", "one-frame exaggeration", "blur"],
    ["extra limb remains", "hand stays oversized", "torso remains stretched", "joint reconnects incorrectly", "smear becomes a second actor"],
    ["mechanism://graphic_world_state_conflation", "mechanism://underdetermined_hidden_state", "mechanism://entity_binding_ambiguity"],
    ["B016", "B017"],
    ["style", "motion", "entities", "continuity.state_ledger", "editing"],
    ["deformation requested without affected region/window", "no source/destination pose", "smear duplicate not typed as graphic-only"],
    ("L2", "Compile a Controlled Deformation Contract: body region, source pose, destination pose, onset/end, maximum deformation, silhouette anchors, exposure frames, and required recovery frame.", "Allows authored exaggeration while defining when normal anatomy must return."),
    ("L3", "Provide source and destination keyframes plus optional smear reference isolated from persistent identity.", "Anchors both valid anatomical states."),
    ["metric_anatomy_recovery_latency", "metric_identity_continuity", "metric_actor_count_consistency", "metric_edit_graphic_classification"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L6", "Create smear frames as 2D animation/postproduction overlays between clean generated poses.", "Makes deformation duration and recovery deterministic."),
)
add_failure(
    "H07", "Camera, edit, and anime discontinuity", "Post-effect anatomy, identity, or style recovery failure",
    "After an allowed effect/deformation interval, one or more protected properties fail to return to the required postcondition.",
    ["transformation-like VFX", "smear", "flash", "smoke", "extreme pose", "style transfer", "multi-shot"],
    ["anatomy partly restored", "costume/art style remains changed", "actor count wrong", "pose lands in wrong state", "face remains distorted"],
    ["mechanism://graphic_world_state_conflation", "mechanism://state_representation_gap", "mechanism://underdetermined_hidden_state"],
    ["B014", "B015", "B016", "B017"],
    ["continuity.state_ledger", "style", "entities", "motion", "verification_requirements"],
    ["only forbidden changes listed", "postcondition not defined", "recovery frame not visible long enough to verify"],
    ("L2", "Define a full post-effect recovery state for anatomy, identity, costume, style, count, pose, and world layout, plus a deadline and minimum stable exposure.", "Converts recovery from an implication into a verifiable terminal state."),
    ("L3", "Use a required recovery keyframe/last frame and preserve it long enough for verification.", "Directly anchors the postcondition."),
    ["metric_anatomy_recovery_latency", "metric_identity_continuity", "metric_object_state_transition", "metric_human_readability"],
    "requires_visual_or_control_conditioning",
    additional_mitigation=("L7", "Regenerate only the effect-to-recovery interval with fixed clean boundary frames.", "Limits resampling to the failed restoration."),
)

# I — Prompt, serialization, and attention-budget failures (6)
add_failure(
    "I01", "Prompt and attention budget", "Constraint overload",
    "Too many hard constraints, exact events, camera moves, actors, effects, negatives, and repeated serializations cause omission, averaging, stiffness, or random prioritization.",
    ["long prompt near provider limit", "same semantics repeated in XML/JSON/YAML/prose", "many exact timestamps", "dense choreography", "conflicting hard locks"],
    ["instructions ignored", "stiff motion", "broken anatomy", "scene incomplete", "random subset of controls obeyed"],
    ["mechanism://conditioning_competition", "mechanism://temporal_dependency_collapse"],
    ["R005", "M002", "M007", "B003"],
    ["normalized_intent", "constraints", "provider_neutral_controls", "provider_realization", "warnings"],
    ["duplicate semantic authorities", "flat list of equal-priority constraints", "format nesting used as emphasis", "style and verification fields sent to provider"],
    ("L1", "Emit one concise provider-native semantic authority ordered by hard locks, identities, event/causal spine, spatial/visibility transitions, camera, then style; remove verification-only fields and duplicate formats.", "Improves adherence per character and makes priority explicit."),
    ("L2", "Use an attention-budget compiler that estimates semantic density, detects conflicts/repetition, and decides compress/simplify/split/reference/post before provider serialization.", "Prevents overload deterministically rather than reacting after failure."),
    ["metric_event_graph_agreement", "metric_control_retention", "metric_observability_coverage", "metric_human_readability"],
    "preventable_by_prompting",
    additional_mitigation=("L5", "Split the clip when hard controls cannot fit the provider's duration/conditioning budget without loss.", "Reduces simultaneous control demand."),
)
add_failure(
    "I02", "Prompt and attention budget", "Under-specification and hallucinated filler",
    "The prompt omits identity, start state, event order, hidden transitions, end state, allowed variation, or forbidden variation, leaving the model to invent content.",
    ["generic genre prompt", "long duration with few events", "temporary occlusion", "multi-actor scene", "open-ended ending", "no state ledger"],
    ["new attacks/gestures/dialogue", "teleportation", "scene change", "unmotivated effects", "identity/state drift"],
    ["mechanism://state_representation_gap", "mechanism://underdetermined_hidden_state"],
    ["B003", "B011", "B014", "B017"],
    ["normalized_intent", "entities", "beats", "actions", "continuity", "constraints"],
    ["only mood/style and one action", "no terminal state", "negative prompt substitutes for positive event plan"],
    ("L2", "Require a minimum sufficient specification: stable IDs/signatures, initial state, ordered critical events, causal edges, coordinate frame, visibility intervals/hidden path, final state, allowed variation, and explicit hard prohibitions.", "Closes the highest-risk ambiguity while avoiding exhaustive microdirection."),
    ("L3", "Bake high-dimensional identity/layout/state information into references rather than expanding prose indefinitely.", "Uses the appropriate carrier for visual facts."),
    ["metric_event_graph_agreement", "metric_identity_continuity", "metric_object_state_transition", "metric_occlusion_continuity"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L5", "Shorten/split any interval whose hidden or sequential state cannot be represented and observed reliably.", "Reduces the amount of invented interpolation required."),
)
add_failure(
    "I03", "Prompt and attention budget", "Contradictory instructions or impossible constraint set",
    "Two or more instructions cannot be satisfied simultaneously, refer to incompatible states/coordinate frames, or exceed the provider's documented capabilities.",
    ["multiple authoring layers", "stale profile overlays", "negative and positive mention of same event", "camera/world conflicts", "duration shorter than required phases"],
    ["random choice among constraints", "averaged behavior", "ignored lock", "physically impossible scene", "provider silently drops unsupported field"],
    ["mechanism://conditioning_competition", "mechanism://coordinate_frame_ambiguity", "mechanism://temporal_dependency_collapse"],
    ["R005", "R006", "R007", "M002"],
    ["profile_resolution", "constraints", "provider_neutral_controls", "provider_realization", "unresolved", "warnings"],
    ["'static camera' and 'orbit camera'", "'never hidden' and 'full-frame splash'", "same event both required and forbidden", "unsupported reference/control silently serialized"],
    ("L2", "Run deterministic typed-merge, contradiction, satisfiability, duration-feasibility, and provider-capability gates; stop with needs_input or explicit unsupported loss instead of compiling a contradictory prompt.", "Prevents stochastic conflict resolution by the model."),
    ("L8", "Select a provider/workflow that can carry the required control set or revise the production design.", "Avoids silently degrading nonnegotiable controls."),
    ["metric_observability_coverage", "metric_control_retention", "metric_event_graph_agreement"],
    "currently_unreliable_or_unsupported",
    additional_mitigation=("L5", "Decompose incompatible simultaneous requirements into shots or layers with valid local constraints.", "Transforms an impossible global request into satisfiable components."),
)
add_failure(
    "I04", "Prompt and attention budget", "Duplicate-format semantic competition",
    "Equivalent or near-equivalent instructions are sent as prose plus YAML/JSON/XML, producing token overhead, subtle contradictions, and unclear authority rather than guaranteed better parsing.",
    ["XML containing JSON/YAML", "same timeline repeated", "manual edits diverge across formats", "provider accepts only text", "character limit"],
    ["fields omitted", "one serialization followed while another ignored", "priority dilution", "prompt rejected or truncated", "model improvises between variants"],
    ["mechanism://conditioning_competition"],
    ["R005", "M002", "M007"],
    ["research_translation", "provider_neutral_controls", "provider_realization", "warnings", "provenance"],
    ["three parallel authorities", "structure assumed to be machine parsed without documentation", "format repetition used as emphasis"],
    ("L1", "Maintain JSON as canonical internal authority, YAML as human authoring, optional XML as an event envelope only when justified, and compile exactly one provider-native prompt payload.", "Removes contradiction and overhead while preserving internal structure."),
    ("L2", "Run identical-semantics A/B tests across formats and select by measured adherence per character for each provider/version; never generalize across providers without evidence.", "Turns format choice into an empirical adapter policy."),
    ["metric_control_retention", "metric_event_graph_agreement", "metric_observability_coverage", "metric_human_readability"],
    "preventable_by_prompting",
    additional_mitigation=("L8", "Use the provider's documented structured API fields or change workflow when exact structure is required but the endpoint accepts only opaque text.", "Avoids pretending a text box is a structured parser."),
)
add_failure(
    "I05", "Prompt and attention budget", "Negative-instruction leakage",
    "A forbidden concept introduced in a negative instruction becomes visually present, is overemphasized, or competes with the positive target.",
    ["long negative list", "forbidden concept visually salient", "provider-specific negative prompt behavior", "contradictory positive mention", "rare desired state"],
    ["extra limb/clone appears despite prohibition", "unwanted action is introduced", "scene becomes visually dominated by forbidden concept", "positive event weakens"],
    ["mechanism://conditioning_competition"],
    ["M001", "M003", "R005"],
    ["constraints", "provider_realization", "warnings", "research_translation"],
    ["many 'no/not/never' phrases in main prompt", "forbidden noun repeated", "negative prompt used instead of positive count/state contract"],
    ("L0", "Prefer positive invariants and mutually exclusive allowed states—'exactly two actors, one per lane'—over repeated forbidden concepts; use provider-native negative fields only where documented and tested.", "Reduces lexical activation and gives the model a concrete target."),
    ("L2", "Compile hard prohibitions into canonical validators and positive state/count contracts; serialize only the minimal provider-appropriate negative subset.", "Keeps prohibition authority in verification even when prompt wording is compressed."),
    ["metric_actor_count_consistency", "metric_event_graph_agreement", "metric_control_retention"],
    "preventable_by_prompting",
    additional_mitigation=("L3", "Use a positive reference image/storyboard that excludes the forbidden state.", "Provides a direct visual target rather than a lexical negation."),
)
add_failure(
    "I06", "Prompt and attention budget", "Numeric precision illusion",
    "Exact coordinates, timestamps, velocities, camera values, or biomechanical numbers are serialized as text even though the provider has no documented parameter/control that guarantees those values.",
    ["numeric-heavy YAML/XML", "provider text prompt only", "exact frame/timestamp demands", "coordinates without control media", "camera/lens values in prose"],
    ["numbers ignored or approximated", "false confidence in deterministic control", "other semantics diluted", "evaluation accepts text presence rather than visual compliance"],
    ["mechanism://conditioning_competition", "mechanism://coordinate_frame_ambiguity", "mechanism://evaluator_observability_gap"],
    ["R004", "R005", "R007", "M002", "M007"],
    ["provider_neutral_controls", "provider_realization", "verification_requirements", "warnings", "loss_report"],
    ["numbers treated as API fields when they are prompt tokens", "no capability disposition", "unmeasurable precision not downgraded"],
    ("L2", "Classify each numeric control as direct API parameter, control-media carrier, compressed-to-text approximation, evaluation-only target, or unsupported loss; never silently upgrade text to deterministic control.", "Aligns confidence with actual carrier capability."),
    ("L4", "Move exact spatial/timing trajectories into control media or a workflow that exposes the relevant parameter.", "Uses a carrier capable of representing the required precision."),
    ["metric_observability_coverage", "metric_camera_motion_agreement", "metric_temporal_event_error", "metric_reappearance_position_error"],
    "partially_mitigated_by_prompting",
    additional_mitigation=("L9", "Mark the requirement unsupported when no available provider/control/post workflow can enforce and verify the demanded precision.", "Prevents false claims of exactness."),
)

# J — Audio synchronization and evaluator failure (8)
add_failure(
    "J01", "Audio and evaluator", "Audio event lead or lag",
    "Impact, splash, step, breath, music accent, or other sound occurs too early/late relative to the intended visual event.",
    ["joint audio-video generation", "fast impact", "multiple events", "camera cut", "long reverberation", "frame-rate/sample-rate mismatch"],
    ["sound before impact", "splash sound without entry", "music accent misses apex", "breath timing inconsistent"],
    ["mechanism://temporal_dependency_collapse", "mechanism://physical_constraint_absence"],
    ["B022", "B023"],
    ["audio", "actions", "interactions", "beats", "verification_requirements"],
    ["sound described independently of event ID", "no onset offset/tolerance", "multiple sounds share generic labels"],
    ("L2", "Create cross-modal anchors linking each sound to a typed visual event, source entity/location, onset, allowed offset, duration, and semantic class.", "Separates temporal and semantic synchronization requirements."),
    ("L6", "Generate or edit audio after the visual event timing is accepted; align impacts and accents to verified event frames.", "Makes synchronization deterministic."),
    ["metric_audio_event_alignment", "metric_temporal_event_error", "metric_causal_edge_accuracy"],
    "requires_postproduction",
    additional_mitigation=("L7", "Replace only the failing audio interval/stem and preserve accepted visuals.", "Avoids resampling synchronized visual content."),
)
add_failure(
    "J02", "Audio and evaluator", "Speech–lip synchronization mismatch",
    "Visible mouth articulation, speaker identity, phonetic content, and speech audio do not align.",
    ["joint dialogue generation", "profile view", "fast speech", "multiple speakers", "stylized face", "camera cut", "voice replacement"],
    ["mouth leads/lags speech", "wrong actor mouths line", "phoneme shapes mismatch", "voice continues while mouth stops"],
    ["mechanism://entity_binding_ambiguity", "mechanism://temporal_dependency_collapse", "mechanism://evaluator_observability_gap"],
    ["B023", "B024"],
    ["audio", "entities", "performance", "actions", "verification_requirements"],
    ["dialogue and complex action in one prompt", "speaker not bound by ID", "no audio/visual timing anchor"],
    ("L2", "Bind utterance text/audio, speaker ID, shot visibility, phoneme/time alignment target, and mouth-performance interval in the canonical score.", "Prevents speaker and timing from being inferred independently."),
    ("L6", "Use dedicated lip-sync/voice postproduction after picture lock or generate dialogue-focused shots separately.", "Provides precise alignment without resampling complex action."),
    ["metric_lip_sync_offset", "metric_role_assignment_accuracy", "metric_audio_event_alignment", "metric_identity_continuity"],
    "requires_postproduction",
    additional_mitigation=("L5", "Use dialogue coverage with readable frontal/profile constraints and separate high-action shots.", "Reduces simultaneous articulation and choreography demands."),
)
add_failure(
    "J03", "Audio and evaluator", "Sound hallucination, omission, or wrong source",
    "Audio is generated for nonexistent events, omitted for visible events, or assigned to the wrong source/location/entity.",
    ["joint audio-video generation", "off-screen sources", "multiple impacts", "silent style request", "ambient scene", "provider prompt rewriting"],
    ["impact sound with no impact", "silent splash", "wrong actor voice", "sound comes from wrong side", "unwanted dialogue/music"],
    ["mechanism://entity_binding_ambiguity", "mechanism://state_representation_gap", "mechanism://temporal_dependency_collapse"],
    ["B022", "B023"],
    ["audio", "actions", "entities", "scenes", "constraints"],
    ["audio mood prompt without event/source ledger", "silence expressed only negatively", "one generic sound label for multiple sources"],
    ("L2", "Maintain an audio event ledger with allowed event classes, source entity/location, onset window, and explicit silence regions; every generated sound must map to an allowed event or ambience class.", "Makes hallucinated or missing sound detectable."),
    ("L6", "Separate sound design from video generation and build audio from verified visual events.", "Provides deterministic semantic and spatial source assignment."),
    ["metric_audio_event_alignment", "metric_event_graph_agreement", "metric_role_assignment_accuracy"],
    "requires_postproduction",
    additional_mitigation=("L8", "Disable native audio or substitute a visual-only model/workflow when the provider cannot expose reliable sound control.", "Avoids uneditable joint-generation errors."),
)
add_failure(
    "J04", "Audio and evaluator", "VLM misses fast action or invents contact",
    "A semantic evaluator fails to observe a short event, infers contact/reaction that is not visible, or produces a confident narrative inconsistent with the frames.",
    ["one-to-three-frame event", "motion blur", "effect-obscured contact", "anime smear", "low frame sampling", "leading verification prompt"],
    ["false pass on contact", "false omission", "wrong event order", "confident explanation unsupported by frames", "disagreement with tracking/measurement"],
    ["mechanism://evaluator_observability_gap"],
    ["B007", "B008", "B009", "B017", "B025"],
    ["verification_requirements", "evidence_trace", "repair_plan", "warnings"],
    ["single VLM verdict used as authority", "sparse frame sampling", "yes/no question presupposes event", "no uncertainty/conflict preservation"],
    ("L2", "Use event-targeted frame windows, neutral forced-choice questions, confidence, evaluator/version pinning, and an explicit unobservable status; never infer contact from reaction alone.", "Reduces prompt bias and false certainty."),
    ("L4", "Add independent measurement lanes—point/pose/segmentation/flow/audio—and preserve conflicts for human adjudication.", "Provides evidence that does not share the VLM's semantic failure mode."),
    ["metric_evaluator_disagreement", "metric_observability_coverage", "metric_contact_distance", "metric_event_graph_agreement"],
    "currently_unreliable_or_unsupported",
    additional_mitigation=("L9", "Block automatic promotion when the critical event remains unobservable or evaluators materially disagree.", "Prevents evaluator uncertainty from becoming production authority."),
)
add_failure(
    "J05", "Audio and evaluator", "Tracker identity swap or occlusion loss",
    "A point/object/actor tracker attaches to the wrong entity, loses the track during occlusion, or resumes on a visually similar region.",
    ["actor crossing", "full occlusion", "similar appearance", "cut", "deformation", "reflection", "low texture", "motion blur"],
    ["trajectory jumps", "wrong actor receives track", "false teleport detected", "real identity drift missed", "visibility bridge attaches incorrectly"],
    ["mechanism://evaluator_observability_gap", "mechanism://entity_binding_ambiguity"],
    ["B013", "B018", "B019", "B020", "B021"],
    ["verification_requirements", "continuity.visibility_intervals", "evidence_trace", "repair_plan"],
    ["one tracker used without confidence", "track continued across a cut", "reflection not excluded", "no semantic identity cross-check"],
    ("L2", "Store tracker version/config, per-frame visibility/confidence, cut boundaries, and entity-binding evidence; terminate/reinitialize tracks explicitly rather than silently bridging uncertain gaps.", "Makes track uncertainty and identity rebinding auditable."),
    ("L4", "Fuse multiple trackers/segmentation/identity cues and require human review at crossings, full occlusions, and low-confidence reattachments.", "Reduces single-tool failure and false continuity claims."),
    ["metric_evaluator_disagreement", "metric_visibility_bridge_coverage", "metric_reappearance_position_error", "metric_identity_continuity"],
    "currently_unreliable_or_unsupported",
    additional_mitigation=("L9", "Mark trajectory/identity metrics unobservable for intervals that cannot be reliably tracked and block automatic repair based on them.", "Avoids acting on corrupted measurement evidence."),
)
add_failure(
    "J06", "Audio and evaluator", "Shot detector mistakes flash, black frame, smear, or wipe for a cut",
    "An evaluator inserts a false edit boundary or misses a true cut, corrupting continuity, timing, identity, and repair scope.",
    ["one-frame flash", "full-frame splash/smoke", "black frame", "whip pan", "style change", "rapid exposure shift"],
    ["continuity evaluated across wrong intervals", "state reset falsely accepted", "repair targets wrong shot", "event timing segmented incorrectly"],
    ["mechanism://evaluator_observability_gap", "mechanism://graphic_world_state_conflation"],
    ["B009", "B010", "B017"],
    ["editing", "verification_requirements", "evidence_trace", "repair_plan"],
    ["single threshold shot detector", "no graphic-effect classifier", "edit list inferred without canonical comparison"],
    ("L2", "Compare detected boundaries with canonical edit events and classify discontinuities as cut, flash, smear, wipe, blur, hold, or occlusion using pre/post identity/state checks.", "Prevents visual discontinuity from automatically becoming an edit boundary."),
    ("L4", "Use multiple detectors/features and require human adjudication for one-frame/full-frame ambiguous intervals.", "Reduces brittle threshold decisions."),
    ["metric_edit_graphic_classification", "metric_evaluator_disagreement", "metric_object_state_transition", "metric_identity_continuity"],
    "currently_unreliable_or_unsupported",
    additional_mitigation=("L9", "Block interval-local repair until the edit/graphic boundary is resolved.", "Prevents repair from operating on the wrong temporal scope."),
)
add_failure(
    "J07", "Audio and evaluator", "Pose or segmentation evaluator fails out of distribution",
    "Pose, anatomy, segmentation, depth, flow, or object detectors fail on anime, smears, severe blur, reflections, unusual bodies, VFX, or transparent materials.",
    ["anime/stylized art", "extreme foreshortening", "smear frames", "water/reflection", "occlusion", "low resolution", "nonhuman character"],
    ["extra/missing keypoints", "reflection counted as actor", "mask fragments", "false penetration", "wrong depth order", "foot slip metric invalid"],
    ["mechanism://evaluator_observability_gap"],
    ["B016", "B017", "B018", "B019", "B020", "B021"],
    ["verification_requirements", "evidence_trace", "repair_plan", "warnings"],
    ["realistic detector applied to anime without calibration", "metric reported despite low confidence", "no excluded deformation window"],
    ("L2", "Declare evaluator domain/version, calibrate on matched positive/negative fixtures, carry confidence and blind spots, and exclude authored deformation windows from inappropriate realistic-anatomy metrics.", "Prevents invalid measurements from masquerading as objective evidence."),
    ("L4", "Use domain-specific detectors, multiple evidence lanes, and human animation review for stylized intervals.", "Improves coverage while preserving uncertainty."),
    ["metric_evaluator_disagreement", "metric_observability_coverage", "metric_anatomy_recovery_latency", "metric_penetration_duration"],
    "currently_unreliable_or_unsupported",
    additional_mitigation=("L9", "Return unobservable rather than pass/fail when no calibrated evaluator can measure the required property.", "Preserves epistemic integrity."),
)
add_failure(
    "J08", "Audio and evaluator", "Human rating ambiguity or disagreement",
    "Raters disagree because the event, role, contact, style convention, or acceptance criterion is underspecified, or because a plausible output does not match the canonical target.",
    ["anime timing", "camera-cheated contact", "subtle identity drift", "ambiguous prompt", "mixed expertise", "unblinded cherry-picked output"],
    ["low inter-rater agreement", "aesthetic preference overrides compliance", "different event interpretations", "showcase accepted despite hard-lock violation"],
    ["mechanism://evaluator_observability_gap", "mechanism://state_representation_gap"],
    ["B007", "B008", "B009", "B025"],
    ["verification_requirements", "evidence_trace", "repair_plan", "experiment_registry"],
    ["single free-form quality score", "raters see provider/condition labels", "no forced-choice event/role questions", "criteria changed after viewing outputs"],
    ("L2", "Pre-register operational criteria and forced-choice questions, blind/randomize outputs, separate compliance from aesthetics, capture confidence/rationale, and calculate agreement.", "Makes human evidence auditable and reduces post-hoc preference bias."),
    ("L4", "Use calibrated expert review for animation/physics/style-critical cases and preserve dissent rather than averaging it away.", "Improves interpretation of specialized or ambiguous phenomena."),
    ["metric_human_readability", "metric_evaluator_disagreement", "metric_observability_coverage"],
    "currently_unreliable_or_unsupported",
    additional_mitigation=("L9", "Do not promote a provider rule or repair action when critical human judgments remain unresolved under the pre-registered adjudication policy.", "Prevents ambiguous evidence from becoming authoritative knowledge."),
)

FAILURE_BY_CODE = {f["failure_code"]: f for f in FAILURES}
assert len(FAILURES) == 71, f"Expected 71 failure records, got {len(FAILURES)}"

# ---------------------------------------------------------------------------
# Markdown rendering helpers
# ---------------------------------------------------------------------------


def md_cell(value: Any) -> str:
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return str(value).replace("|", "\\|").replace("\n", " ")


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(md_cell(c) for c in row) + " |" for row in rows]
    return "\n".join([head, sep] + body)


def source_links(ids: list[str]) -> str:
    return ", ".join(f"[{sid}]" for sid in ids)


def failure_records_for(families: list[str]) -> list[dict[str, Any]]:
    return [r for r in FAILURE_RECORDS if r["family_id"] in families]


def render_failure_record(record: dict[str, Any], include_full: bool = True) -> str:
    primary, fallback = record["mitigations"][:2]
    lines = [
        f"### {record['family_id']}.{record['ordinal']:02d} — {record['name']}",
        "",
        f"**Failure ID:** `{record['failure_id']}`  ",
        f"**Empirical confidence:** {record['empirical_confidence']}  ",
        f"**CPCS render evidence:** `{record['cpcs_render_campaign_status']}`  ",
        f"**Sources:** {source_links(record['source_refs'])}",
        "",
        f"**Trigger.** {record['trigger_conditions'][0]}",
        "",
        f"**Observable symptom.** {record['observed_symptoms'][0]}",
        "",
        f"**Likely cause.** {record['suspected_causes'][0]['statement']} This is recorded as `{record['suspected_causes'][0]['status']}` rather than as a verified closed-model internal mechanism.",
        "",
        f"**Primary intervention — {primary['level']} ({MITIGATION_LEVELS[primary['level']]}).** {primary['method']}",
        "",
        f"**Fallback — {fallback['level']} ({MITIGATION_LEVELS[fallback['level']]}).** {fallback['method']}",
        "",
        f"**Verification.** `{record['verification_metrics'][0]}` is the primary metric; companion checks: " + ", ".join(f"`{m}`" for m in record['verification_metrics'][1:]) + ".",
    ]
    if include_full:
        lines += [
            "",
            "**Compiler/score impact.** " + ", ".join(f"`{p}`" for p in record["canonical_fields_affected"]) + ".",
            "",
            "**Prompt risks.** " + "; ".join(record["prompt_risk_patterns"]) + ".",
            "",
            "**Falsification checkpoint.** " + record["suspected_causes"][0]["falsification_test"],
        ]
    return "\n".join(lines)


def render_family_report(title: str, families: list[str], executive_finding: str, contract_text: str) -> str:
    records = failure_records_for(families)
    family_rows = []
    for fam in families:
        meta = FAMILY_META[fam]
        family_rows.append([
            fam, meta["name"], len(failure_records_for([fam])), meta["owner"], ", ".join(meta["metrics"])
        ])
    parts = [
        f"# {title}",
        "",
        f"**Research date:** {ACCESS_DATE}  ",
        f"**Repository revision inspected:** `{REPO_SHA}`  ",
        "**Evidence status:** literature and repository synthesis complete; CPCS provider render campaign not run in this session.",
        "",
        "## Decision finding",
        "",
        executive_finding,
        "",
        "## Covered families",
        "",
        md_table(["ID", "Family", "Records", "Existing owner", "Core metrics"], family_rows),
        "",
        "## Canonical contract implications",
        "",
        contract_text,
        "",
        "The fields proposed here are candidate nested extensions under the existing universal score, verification, and second-brain owners. They are not production authority and must not become a parallel CPCS root schema.",
        "",
        "## Failure records",
        ""
    ]
    parts.extend(render_failure_record(r) + "\n" for r in records)
    parts += [
        "## Provider qualification requirement",
        "",
        "Official documentation proves that an interface accepts text, images, video, keyframes, audio, masks, or related inputs; it does **not** prove reliable adherence to the contracts above. Each current provider/model/version must run the paired repeated-seed fixtures in `experiments/`, with raw artifacts and failed samples retained.",
        "",
        "## Evidence boundary",
        "",
        "The source IDs in brackets resolve through `SOURCE_CATALOG.csv`. Mechanistic explanations for closed commercial models are reported as falsifiable engineering inferences unless the provider discloses the relevant architecture and test evidence."
    ]
    return "\n".join(parts)


EXECUTIVE_SYNTHESIS = f"""# Executive Synthesis

**Research date:** {ACCESS_DATE}  
**Repository:** `{REPO}` at `{REPO_SHA}`  
**Package status:** source/repository research complete; live repeated-seed provider qualification not run.

## BLUF

The dominant control problem in current generative video is not merely visual quality. It is **state underdetermination across time**. A prompt can describe what is visible, but it usually does not carry a persistent, machine-checkable representation of who and what exists, which state changes are legal, how hidden subjects continue moving, which event causes which effect, how camera coordinates relate to world coordinates, and which exact interval must be verified. When visibility drops or multiple constraints compete, the model is free to resolve missing information with a statistically plausible continuation. That is the gap the user observed when a fighter disappears behind a water splash.

The correct CPCS response is therefore a mitigation ladder, not a larger negative prompt:

1. **Represent the missing state** in the canonical score: persistent IDs, state ledger, event graph, spatial frame, visibility interval, causal edges, terminal state, and hard invariants.
2. **Compile only the provider-relevant subset** into one native request representation; do not duplicate identical semantics across XML, YAML, and JSON.
3. **Escalate conditioning** when text cannot carry the missing information: reference frames, identity sheets, masks, point/pose/depth tracks, control video, or source-video editing.
4. **Split the shot** before a long opaque interval, dense interaction, role crossing, or causal chain exceeds the empirically qualified provider/task envelope.
5. **Move deterministic effects to postproduction** when exact topology, timing, count, contact, or audio synchronization matters more than generative spontaneity.
6. **Verify interval-level assertions** and retain failures. Aggregate aesthetic scores cannot overrule one production-critical identity, count, event-order, or contact failure.

## What the research package establishes

- **96 distinct failure records** across 16 families, each with triggers, symptoms, causes, mitigations, verification metrics, CPCS owners, confidence, and unresolved questions.
- **60 evaluator definitions** with explicit lanes, blind spots, human-calibration requirements, and threshold policy.
- **21 provider/interface rows** separating official capability from unmeasured reliability.
- **81 source records** spanning repository authority, official provider documentation/model repositories, peer-reviewed work, benchmarks, control methods, tracking/measurement tools, and recent preprints.
- **Candidate contracts** for occlusion continuity, persistent state, spatial transitions, causal events, and evaluator provenance.
- **Repeated-seed experiment fixtures** for occlusion, serialization, action density, spatial control, causality, repair, identity/state, and evaluator calibration.

## Ten load-bearing findings

1. **Opaque occlusion changes the information problem.** The model no longer observes the subject; unless state and trajectory survive outside the pixels, reappearance is reconstruction rather than continuation. [B012] [B013] [B014] [B027] [B028]
2. **Endpoint images are constraints, not proofs of the path.** First/last-frame modes can anchor endpoints, but current official documentation does not guarantee correct intermediate order, hidden trajectory, contact, or causality. [M001] [M014] [M024]
3. **Compositional binding remains fragile.** Attribute, count, role, action, motion, spatial relation, and interaction bindings all degrade as scenes become denser. [B002] [B041] [B043]
4. **Visual plausibility and physical correctness are separable.** Benchmarks continue to expose failures in mass, momentum, support, collisions, fluids, and causality even when a clip looks coherent at a glance. [B004] [B005] [B025] [B027] [B044] [B045]
5. **Prompt detail has diminishing returns.** When the missing variable is a trajectory, mask, contact geometry, source motion, or deterministic effect, more prose competes for attention without becoming an executable control. [B005] [B035] [B036] [B037] [B038]
6. **Camera and world motion require separate tracks.** Screen-space flow alone cannot reliably identify whether the camera, actor, or background moved; zoom and translation are especially confusable. [B031] [B035] [B037]
7. **Graphic discontinuity is not world-state discontinuity.** Flashes, smears, wipes, speed lines, and full-frame effects need explicit recovery frames and continuity locks or they can become scene-reset opportunities.
8. **Structured serialization is a compiler discipline, not model intelligence.** JSON is CPCS authority because it is deterministic and validated; XML/YAML can be useful authoring envelopes, but no evidence supports universal provider-side superiority. [R005] [M001] [M002] [M007]
9. **Evaluators fail in systematic ways.** Fast temporal events, occlusion, stylization, camera geometry, screen-overlap contact, and sparse localized failures require calibrated multi-lane evidence and human review. [B029] [B030] [B031] [B032] [B033] [B034]
10. **The cheapest reliable intervention is provider/task specific.** CPCS should learn a failure-to-mitigation policy from immutable paired runs; it should never hard-code a universal action-per-second or prompt-length threshold from one provider or showcase.

## Water-splash case: why the model fills the gap

For the two-fighter water sequence, the splash simultaneously creates several high-risk conditions: a complete opaque occlusion, a solid-fluid transition, overlapping cause/effect timing, one actor's hidden dive trajectory, another actor's kick and recovery, actor-count continuity, screen-side continuity, and a full-frame high-frequency effect. A text model can satisfy the surface concept—“kick, splash, fighter submerged”—without preserving the exact latent state. The splash is therefore a **permission boundary** unless CPCS represents:

```text
B remains the same existing actor while invisible
B's hidden dive path continues from entry state to a bounded reappearance region
A's kick misses B and contacts only the water
water displacement starts only at A's impact point
actor count stays exactly two
costumes, roles, screen sides, water topology, and world layout do not change
```

Even that canonical contract does not guarantee prompt-only compliance. When the subject is fully hidden and the result must be exact, CPCS should choose at least one of: a visible bridge, tracked control media, first/last/reference frames plus path control, a shot split, clean-plate compositing, or source-video modification.

## Decision boundary

Prompt-only generation should be abandoned when any of the following is both **hard** and **not directly observable throughout the generated interval**:

- exact identity/count through complete occlusion;
- exact hidden trajectory or reappearance region;
- precise hand-object or body-body contact;
- collision-free geometry or support mechanics;
- causal material response from a specific impact point;
- multi-actor crossings with persistent role assignment;
- deterministic graphic/anatomy recovery after a full-frame effect;
- frame-accurate audio-event synchronization;
- exact product geometry, logos, dimensions, or state transitions.

The escalation target is not always the most expensive control. CPCS should select the lowest mitigation level whose repeated-seed distribution clears the pre-registered acceptance threshold without adding a new critical failure.
"""

RESEARCH_METHOD = f"""# Research Method

## Scope and evidence model

This package executes the uploaded research brief as a **Phase 1 professional evidence and implementation study**. It covers text-to-video, image-to-video, first-frame, first-and-last-frame, reference-conditioned, reference-video, video-to-video, multi-shot, joint audio-video, and pose/depth/mask/trajectory/control-video workflows. It covers realistic, cinematic, UGC, product, dialogue, anime, stylized action, VFX, and multi-actor scenes.

The evidence hierarchy is:

1. repository authority and controlled repository observation;
2. official model papers, technical reports, documentation, API references, model cards, and model repositories;
3. peer-reviewed benchmarks and publications;
4. official benchmark code and disclosed evaluation protocols;
5. recent preprints and controlled independent research, explicitly marked as such;
6. engineering inference with a falsification test;
7. community anecdotes only as experiment hypotheses.

Official documentation is used only for **capability**: accepted inputs, endpoint IDs, durations, resolutions, prompt limits, audio, references, seeds, and documented controls. It is not used as proof of adherence or reliability. Provider showcases and marketing rankings are not counted as reliability evidence.

## Repository-first procedure

The inspected repository is `{REPO}` at revision `{REPO_SHA}`. The review mapped ownership before proposing fields. The canonical JSON score, compiler, provider profiles, verification, immutable experiment evidence, and second-brain curation remain the existing authorities. Candidate schemas in this package are research proposals only.

Reviewed files include:

""" + "\n".join(f"- `{p}`" for p in REPOSITORY_FILES_REVIEWED) + """

The root `REPO_CONTINUITY_IMPLEMENTATION_PLAN.md` requested by the brief was not found in the inspected tree. The package uses `ARCHITECTURE.md` and `lab/second_brain/IMPLEMENTATION_PLAN.md` as the nearest current owners and records this as an unresolved repository gap rather than silently inventing the missing file.

## Literature and capability procedure

For each model-specific row, the research records provider, model/endpoint, date scope, input modes, durations, output properties, prompt limits, seed semantics, source IDs, and unresolved caveats. The package does not claim 100% verification where an official interface was inaccessible, region-specific, product-only, adapter-mediated, or internally contradictory.

For each failure record, the synthesis records:

```text
trigger conditions
observable symptoms
likely causes and inference status
canonical fields affected
prompt risk patterns
mitigation levels
verification metrics
provider-specific caveats
repository owner
empirical confidence
unresolved questions
```

## What was and was not executed

Executed in this session:

- repository ownership audit;
- primary-source and benchmark synthesis;
- 96-record failure taxonomy;
- provider capability matrix;
- source and claim traceability matrices;
- JSON Schema design and validation;
- repeated-seed experiment designs;
- CPCS compiler, decomposition, verification, and repair recommendations;
- package integrity validation and ZIP generation.

Not executed in this session:

- paid or credentialed commercial provider generation;
- local open-model inference requiring model weights/GPU workflows not supplied to this environment;
- human rating panels;
- seed-level success distributions;
- live CPCS ingestion, curation, promotion, or production-authority changes.

Therefore, provider-specific failure rates, action-density limits, prompt-length sweet spots, mitigation effect sizes, and evaluator thresholds remain **not measured by CPCS**. The experiment fixtures are designed to produce those measurements without changing production authority.

## Statistical design principles

- Use paired arms and identical canonical meaning.
- Use the same seed where the provider exposes a seed, while recognizing that seeds do not guarantee identical artifacts.
- Use at least 20 completed candidates per arm for an initial provider screen and 30+ for open/local models when affordable; expand near decision boundaries.
- Report successes and failures per seed, Wilson intervals for binary criteria, medians and bootstrap intervals for continuous error, and human/evaluator disagreement.
- Pre-register critical assertions and stop conditions before generation.
- Apply correction for multiple comparisons within an ablation family.
- Never discard failed outputs or select only the best render.
- Bind every artifact to the exact request, model/version, provider, seed/retry identifier, assets, evaluator versions, and human verdict.

## Reproducibility boundary

The package is reproducible as a research artifact: schemas, JSONL, CSV, YAML, manifest, checksums, and validation report are generated deterministically from this script. Generative-video outputs remain stochastic and provider-dependent. Reproducibility means preserving the complete attempt and its evidence, not claiming byte-identical regeneration.
"""

FAILURE_CAUSE_MODEL = """# Failure Cause Model

## Core model

CPCS should diagnose a failed video by locating the first broken contract in a layered chain:

```mermaid
flowchart LR
    I[Intent] --> S[Persistent state]
    S --> E[Ordered event graph]
    E --> C[Causal consequences]
    C --> G[Spatial and interaction geometry]
    G --> V[Visibility and material response]
    V --> P[Provider projection]
    P --> R[Rendered pixels and audio]
    R --> X[Re-extraction and verification]
    X --> D[Failure classification]
    D --> M[Bounded mitigation]
    M --> P
```

The useful distinction is between **target representation failure**, **provider realization failure**, and **evaluator failure**:

- A target representation failure occurs when CPCS never encoded an identity, state, ordering, causal, spatial, visibility, support, or recovery obligation.
- A provider realization failure occurs when the obligation was encoded and compiled without loss but the generated artifact violates it.
- An evaluator failure occurs when the artifact and target are misclassified because the measurement or semantic judge cannot observe the relevant property.

A repair is unsafe until those three cases are separated. Adding prompt text cannot repair a missing tracker, and replacing a provider cannot repair a contradictory canonical score.

## Mechanism catalog

""" + "\n\n".join(
    f"### {m['name']}\n\n**ID:** `{m['mechanism_id']}`  \n**Confidence:** {m['confidence']}  \n**Evidence:** {source_links(m['evidence_basis'])}\n\n{m['description']}\n\n**Falsifiable prediction:** {m['falsifiable_prediction']}"
    for m in MECHANISMS
) + """

## Diagnostic decision sequence

1. **Validate canonical completeness.** Are actor IDs, counts, state transitions, event dependencies, coordinate frames, visibility intervals, causal origins, support/contact obligations, terminal state, and verification assertions present?
2. **Validate compiler fidelity.** Did the provider projection retain every hard lock and report unsupported/evaluation-only controls instead of silently dropping them?
3. **Validate provider capability.** Does the exact model/version/interface officially accept the required carrier: first/last frames, multiple references, masks, keyframes, trajectory, source video, audio, or edit instruction?
4. **Localize first divergence.** Identify the earliest frame/interval where state or event evidence departs from the target.
5. **Challenge the evaluator.** Re-run with a second lane and human review if fast motion, occlusion, reflection, stylization, camera geometry, or screen-overlap contact is involved.
6. **Choose the minimum sufficient mitigation.** Wording only for lexical ambiguity; structured contract for missing state; visual controls for unobserved trajectories/geometry; decomposition for density; postproduction for deterministic effects; provider substitution only after capability mismatch is established.
7. **Re-verify all hard locks.** Localized repair can create collateral damage outside the edited concept or interval.

## Why negative prompting is insufficient

A negative prompt can discourage visible concepts, but it does not provide the positive state trajectory that must occupy an ambiguous interval. “No duplicate,” “no teleport,” and “do not change clothing” identify forbidden outcomes; they do not specify which latent pose, path, count, material state, or reappearance region should persist. Negative constraints therefore belong in the contract, but the contract must also include a positive continuation and an observable verification method.
"""


FAMILY_SUMMARY_ROWS = [
    [fid, meta["name"], len(failure_records_for([fid])), meta["owner"], source_links(meta["default_sources"])]
    for fid, meta in FAMILY_META.items()
]

FAILURE_TAXONOMY = """# Failure Taxonomy

## Taxonomy design

The taxonomy is organized by the **first violated production contract**, not by surface artifact alone. The same visible symptom can have different causes: a teleport may come from an undefined hidden trajectory, an actor-tracker swap, a camera-coordinate error, or a genuine provider failure despite a complete score. Classification should therefore retain symptom, suspected mechanism, evidence lane, and first-divergence interval.

This package defines **96 versioned failure records** in `FAILURE_RECORDS.jsonl`. Each record is schema-valid and contains a provider-neutral failure ID, triggers, symptoms, likely cause, evidence status, canonical paths, prompt risks, mitigations, metrics, regression fixture, owner, confidence, and unresolved questions.

## Families

""" + md_table(["ID", "Family", "Records", "Existing owner", "Default evidence"], FAMILY_SUMMARY_ROWS) + """

## Taxonomy invariants

- A failure ID names one stable failure concept; provider/model/version observations attach to it rather than replacing it.
- A visible symptom does not establish a hidden internal cause.
- Official provider capability is not empirical reliability.
- Prompt, canonical contract, visual control, shot decomposition, postproduction, localized regeneration, and provider substitution remain distinct mitigation levels.
- Evaluator failure is a first-class family, not noise to be averaged away.
- No record authorizes a production schema change or curated promotion.

## Complete record index

""" + md_table(
    ["Ordinal", "Failure ID", "Family", "Failure", "Primary mitigation", "Primary metric", "Confidence"],
    [[r["ordinal"], r["failure_id"], r["family_id"], r["name"], r["mitigations"][0]["level"], r["verification_metrics"][0], r["empirical_confidence"]] for r in FAILURE_RECORDS]
) + """

## Machine-readable authority

The Markdown index is for navigation. `FAILURE_RECORDS.jsonl` plus `FAILURE_RECORD.schema.json` is the machine-readable research authority for this package. The records are candidate evidence only; CPCS repository promotion still requires the existing second-brain distillation and human-curation path.
"""

MITIGATION_HIERARCHY_DOC = """# Mitigation Hierarchy

## Governing rule

Use the **lowest-cost intervention that carries the missing information in a form the selected provider can actually receive and that clears a pre-registered verification threshold across repeated seeds**. Do not default to “add more detail.” More detail can worsen attention competition, conflict, and temporal overload.

""" + "\n\n".join(
    f"## {level} — {name}\n\n**Use when:** " + {
        "L0": "The canonical target is complete and the failure is caused by an ambiguous or provider-hostile phrase.",
        "L1": "The provider receives a prompt string, but deterministic compiler structure is needed to prioritize identities, events, hard locks, and end state.",
        "L2": "The missing information is a persistent state, event dependency, spatial frame, causal edge, visibility interval, support/contact state, or terminal invariant.",
        "L3": "Appearance, identity, layout, start/end pose, product geometry, or reappearance state needs a visual anchor.",
        "L4": "The missing information is time-varying and cannot be represented reliably by text: mask, pose, point, depth, trajectory, camera, audio, or source-motion control.",
        "L5": "One clip contains too many dependencies, actors, crossings, camera moves, effects, or opaque intervals for the qualified provider/task envelope.",
        "L6": "The required behavior is deterministic finishing: splash, flash, smoke, shake, sound, logo, count, geometry, topology, or exact effect timing.",
        "L7": "Most of the artifact is accepted and the first divergence can be bounded with stable in/out frames and preservation checks.",
        "L8": "The selected provider lacks a documented carrier or repeatedly fails despite a complete target and appropriate controls.",
        "L9": "No available workflow can satisfy the hard requirement with an acceptable success distribution or verification confidence."
    }[level] + "\n\n**Exit checkpoint:** " + {
        "L0": "Paired wording arm improves the same critical assertion without changing the canonical target.",
        "L1": "The adapter retains every hard lock and produces no semantic conflict or overflow loss.",
        "L2": "The score validates and every required state/event/spatial/causal obligation has an explicit verification assertion.",
        "L3": "Reference identity, role, rights, and binding are verified; conflicts with text are resolved before submission.",
        "L4": "Control assets are hash-bound, aligned to the exact timebase/coordinate frame, and validated before generation.",
        "L5": "Each shot has a complete handoff state, no hidden dependency across the edit, and a deterministic assembly plan.",
        "L6": "The generated plate preserves required clean geometry/identity and the composite passes all continuity assertions.",
        "L7": "The repaired interval and both seams pass; all non-target hard locks are rechecked across the entire artifact.",
        "L8": "The substitute provider profile is officially verified and the same sealed experiment is rerun without changing acceptance criteria.",
        "L9": "The system returns an explicit unsupported result and does not fabricate a controllability claim."
    }[level]
    for level, name in MITIGATION_LEVELS.items()
) + """

## Escalation algorithm

```text
validate canonical target
→ identify first divergence
→ challenge evaluator
→ determine missing carrier
→ choose lowest compatible level
→ compile with explicit loss report
→ generate paired candidates
→ verify interval and all hard locks
→ retain failed evidence
→ escalate only if pre-registered threshold is not met
```

## Cost and risk accounting

Every mitigation record in `FAILURE_RECORDS.jsonl` includes expected benefit, prompt/character cost, generation cost, risk of a new failure, provider dependency, evidence strength, verification, and rollback. CPCS should learn provider/model/version-conditioned mitigation ordering from immutable isolated comparisons; learned weights may rank admissible choices but cannot override hard constraints or authored policy.
"""

PROMPT_COMPILER_RULES = """# Prompt Compiler Rules

## Authority rule

The fully resolved `cpcs.universal_score/1.0` JSON remains the only semantic authority. Natural language, Markdown, YAML, XML, JSON prompt text, hybrid envelopes, references, and control media are projections or inputs. No serialization may become a second truth source.

## Deterministic compile sequence

1. **Normalize entities.** Assign stable IDs and distinguish identity, role, screen lane, world position, voice, prop ownership, and material state.
2. **Resolve state.** Materialize initial state, state deltas, visibility intervals, irreversible transitions, and terminal state.
3. **Topologically order events.** Compile dependencies before timestamps: `before`, `only_after`, `causes`, `while`, `prevents`, `terminates`.
4. **Declare coordinate frames.** Never emit unqualified left/right when camera motion or cuts can change screen projection.
5. **Separate actor, camera, effect, edit, and audio tracks.** Do not rely on one prose clause to distinguish these motions.
6. **Classify controls.** Each field is hard, soft, evaluation-only, unsupported, or delegated to a reference/control asset.
7. **Resolve conflicts before provider submission.** Contradictory fields must fail closed or require explicit selection; the provider must not arbitrate canonical conflicts.
8. **Select one provider-native representation.** Do not duplicate the same meaning as XML+JSON+YAML inside a prompt unless a controlled experiment proves a version-scoped benefit.
9. **Compress by information value.** Preserve identities, event order, causal links, hidden transitions, terminal state, and hard locks before style adjectives, redundant negatives, or verifier-only fields.
10. **Emit a loss report.** Every canonical field receives a capability disposition; unsupported or evaluation-only controls remain visible.
11. **Disable or record prompt rewriting.** Provider-side enhancement/rewrite changes the experiment arm and can alter semantics. If it cannot be disabled, capture the setting and returned/expanded prompt where available.
12. **Bind assets and timebases.** References, masks, pose tracks, depth, trajectories, audio, and source video require content hashes, roles, coordinate frames, intervals, and rights basis.
13. **Predeclare verification.** Hard fields without an observable metric are not ready for provider execution.

## Priority order under prompt limits

```text
safety and legal constraints
> identity, actor/object count, and role locks
> initial and terminal state
> ordered primary events and causal edges
> spatial/visibility/contact invariants
> camera and edit state
> audio anchors
> provider-required syntax
> style and secondary detail
> negative constraints not paired with a positive target
> explanatory prose and evaluator-only notes
```

A hard lock may not be silently truncated. If the prompt budget cannot carry the required subset, the compiler must change carrier, split the shot, or return unsupported loss.

## Positive continuation rule

A forbidden outcome is not a complete instruction. Each critical negative must be paired with the positive state that should persist:

```text
weak: no teleport, no duplicate, no costume change
stronger canonical target:
  actor_B.exists=true throughout
  actor_B follows hidden_path_01
  actor_B reappears in region R_B
  actor_count=2
  actor_B.costume remains costume_B_01
```

## Serialization experiments

The format experiment must hold canonical meaning constant across natural language, flat YAML, XML, JSON, XML+JSON, and XML+JSON+YAML. Compare semantic coverage, hard-lock retention, prompt cost, and failure distributions. Do not compare hand-written prompts with unequal information or provider-specific optimization and call the result a format test.

## Provider adapter rules

- Bind the exact provider, endpoint/model ID, API/product interface, date, region, duration, resolution, frame rate, seed semantics, prompt limit, reference roles, audio behavior, and rewrite policy.
- Third-party adapters are separate provider surfaces; do not assume native limits or behavior.
- A documented seed is an experiment key, not proof of deterministic or compliant output.
- First/last-frame modes are endpoint constraints, not hidden-path, contact, or causal guarantees.
- Source-video edit modes must verify preservation outside the requested change.
- Marketing claims never populate empirical reliability fields.

## Attention-budget decision

The compiler should calculate a version-scoped complexity vector rather than one universal score:

```text
primary_event_count
dependency_depth
simultaneous_actor_actions
actor_similarity
screen_crossings
complete_occlusion_seconds
contact_complexity
camera_motion_complexity
effect_density
audio_anchor_count
prompt_characters
reference_count
```

Provider/task-specific experiment results define warning and split thresholds. Before calibration, CPCS may warn on rising complexity but must not claim universal maximum actions per second.
"""

SHOT_DECOMPOSITION_RULES = """# Shot Decomposition Rules

## Objective

Decomposition converts one underdetermined, overloaded generation problem into several bounded problems with explicit state handoffs. It is not merely shorter prompting. Every split must preserve identity, state, geography, event causality, audio, and edit intent across the boundary.

## Mandatory split conditions

Split the clip—or use source/control media—when a hard requirement depends on any of the following and no continuous control signal is available:

- complete opaque occlusion with a production-critical hidden trajectory;
- two or more similar actors crossing, grappling, or swapping depth lanes;
- precise contact plus a complex camera move or full-frame effect;
- more dependent events than the provider/task has empirically qualified;
- irreversible object/material transition followed by a cut or long absence;
- graphic/anime deformation requiring a guaranteed recovery frame;
- deterministic product geometry, logo, handoff, or state change;
- frame-accurate dialogue, impact, or music synchronization;
- a provider prompt budget that cannot retain all hard controls;
- one failed interval inside an otherwise accepted artifact when an edit-capable workflow can preserve the rest.

## Preferred cut points

Use boundaries where state is fully observable and low-velocity:

- before complete occlusion begins;
- after a landing, settle, recoil, or recovery;
- before actors cross the action axis;
- after a prop release and before a new acquire;
- before a full-frame flash/splash/smoke wipe;
- at a neutral establishing view before a reverse angle;
- on a musical beat only when the visual handoff state is also explicit.

Avoid cuts in the middle of ambiguous contact, during untracked possession transfer, or while identity is fully hidden unless the next shot starts from a strong keyframe/reference.

## Handoff contract

Every shot boundary records:

```text
outgoing frame/artifact hash
incoming reference/keyframe hash
entity IDs and actor count
identity and costume signatures
object inventory and possession
world layout and screen/depth lanes
pose, velocity, support, and recovery state
material/effect state
camera pose/lens/motion state
ordered unfinished dependencies
terminal state of the outgoing shot
initial state of the incoming shot
allowed edit discontinuities
forbidden world-state discontinuities
verification assertions across the seam
```

## Decomposition patterns

### Hidden-state bridge

```text
shot 1: entry trajectory remains visible → cut before total cover
shot 2: effect plate or short opaque transition
shot 3: authored reappearance keyframe → continuation and recovery
```

### Interaction plate plus effects

```text
generate or film clean choreography with readable silhouettes
→ verify contact/near-contact, roles, and state
→ add splash/smoke/flash/shake in V2V or compositing
→ reverify identity, count, effect origin, and seams
```

### Multi-actor role preservation

```text
establish distinct actors and lanes
→ isolate one primary exchange per shot
→ use neutral re-establishing shot before screen-side reversal
→ maintain role and object ledgers across every cut
```

## Assembly verification

The assembled sequence must be verified as one artifact. Passing each clip separately is insufficient: identity, object state, screen direction, audio phase, camera continuity, and material state can fail only at the seam.
"""

LOCALIZED_REPAIR_PLAYBOOK = """# Localized Repair Playbook

## Preconditions

Localized repair is permitted only after the exact original build, provider request, result, artifact, evaluator evidence, and first-divergence interval are hash-bound. The repair planner may reassert existing canonical controls; it may not invent new directing knowledge or mutate the accepted canonical target.

## Procedure

1. **Freeze accepted evidence.** Record the original artifact hash, accepted intervals, failed interval, hard-lock verdicts, and human review.
2. **Find first divergence.** Diagnose the earliest frame where actor/object identity, count, state, event order, spatial relation, contact, material response, camera, anatomy, or audio departs from target.
3. **Challenge evaluator.** If the failure involves fast motion, occlusion, stylization, reflections, screen-overlap contact, or camera ambiguity, require a second lane and human review.
4. **Classify the cause.** Missing canonical state; compiler loss; provider realization; asset/control error; edit seam; or evaluator failure.
5. **Choose a repair carrier.** Wording, canonical contract, reference/keyframe, mask/pose/depth/trajectory/control video, shot split, V2V edit, deterministic compositing, audio replacement, or provider substitution.
6. **Define the preservation envelope.** List every field and interval outside the target change that must remain unchanged.
7. **Create boundary frames.** Prefer accepted in/out frames around the failed interval; include pose, velocity, state, camera, and material continuity.
8. **Execute one isolated change.** Do not bundle prompt rewrite, provider change, new reference, and shot split in one causal experiment.
9. **Verify the repair and collateral state.** Re-run every critical assertion across the entire artifact, not only the repaired interval.
10. **Record outcome immutably.** Retain failed and successful attempts, cost, latency, request/settings, seeds/retries, evaluator disagreement, and human verdict.

## Failure-specific routes

""" + md_table(
    ["Failure class", "First repair", "Escalation", "Required recheck"],
    [
        ["Occlusion/hidden state", "L2 visibility/state contract", "L4 tracked control or L5 split", "identity, count, path, reappearance, world state"],
        ["Identity/role", "L2 persistent IDs and event binding", "L3 references or L4 per-actor controls", "face/costume/body/role/screen lane/voice"],
        ["Object state/possession", "L2 ledger transition", "L4 object track or V2V", "count, holder, contact, dimensions, material state"],
        ["Spatial/geography", "L2 coordinate frame and transition", "L3 storyboard or L4 trajectory/depth", "screen direction, depth, target region, camera transform"],
        ["Order/causality", "L2 event graph", "L5 event-per-shot decomposition", "onset, apex, only-after, consequence, recovery"],
        ["Contact/physics", "L2 interaction/support contract", "L4 source/control motion or L6 deterministic finishing", "distance, penetration, support, reaction latency"],
        ["Fluid/VFX", "L2 effect origin/lifetime", "L6 separate plate/composite", "impact origin, topology, persistence, identity/count"],
        ["Camera entanglement", "separate camera and actor tracks", "L4 camera/source control", "world trajectory, zoom vs translation, direction"],
        ["Anime deformation", "L2 deformation/recovery interval", "L3 recovery keyframe or L6 authored effect", "silhouette, limb count, recovery frame"],
        ["Audio sync", "L2 shared event anchor", "L6 replace/mix audio", "onset offset, semantic cause, speaker/voice"],
    ]
) + """

## Rollback

A repair never overwrites the original. Rollback means selecting the previous accepted build/artifact and preserving the failed repair attempt as evidence. If an edit produces collateral hard-lock failures, it is rejected even when the target interval improves.
"""


# ---------------------------------------------------------------------------
# Claim/source matrix and repository overlap mapping
# ---------------------------------------------------------------------------

CLAIMS = [
    {"claim_id": "C001", "claim": "Current video generators remain materially weak on compositional binding, spatial relationships, temporal transitions, and multi-entity interactions; aggregate visual quality does not imply event-level compliance.", "claim_type": "benchmark_supported", "source_refs": ["B001", "B002", "B003"], "confidence": "high", "status": "verified within cited benchmark scope", "cpcs_implication": "Use typed event/state/spatial metrics rather than a single quality score."},
    {"claim_id": "C002", "claim": "Temporary occlusion is a hidden-state continuity problem: absence of pixels does not provide evidence of deletion, transformation, or teleportation, yet generation and evaluation systems can fail to preserve the hidden entity/state.", "claim_type": "cross-domain synthesis", "source_refs": ["B011", "B012", "B013", "B014", "B017"], "confidence": "high for phenomenon; medium for universal internal mechanism", "status": "supported", "cpcs_implication": "Add visibility intervals, persistent entity existence, hidden paths, and reappearance contracts."},
    {"claim_id": "C003", "claim": "Object permanence and recurrence consistency degrade as content leaves view or reappears after longer intervals.", "claim_type": "benchmark_supported", "source_refs": ["B011", "B012", "B014", "B015"], "confidence": "high", "status": "supported", "cpcs_implication": "Carry state/entity ledgers across shots and recurrence gaps."},
    {"claim_id": "C004", "claim": "Prompt engineering alone is insufficient for many dynamic physical phenomena; current models can satisfy semantics while violating mass, momentum, support, contact, or material response.", "claim_type": "benchmark_supported", "source_refs": ["B004", "B005", "B006"], "confidence": "high", "status": "supported", "cpcs_implication": "Escalate high-precision physics to control media, decomposition, simulation, or postproduction."},
    {"claim_id": "C005", "claim": "On the hard subset reported by VideoPhy-2, the best evaluated model achieved 22% joint semantic-and-physical adherence; this result is version- and benchmark-scoped, not a universal provider ranking.", "claim_type": "benchmark_result", "source_refs": ["B004"], "confidence": "high", "status": "verified within cited study", "cpcs_implication": "Treat physical compliance as a separate qualification gate."},
    {"claim_id": "C006", "claim": "Benchmark corrections and prompt/ground-truth audits can change model rankings, so evaluator datasets and criteria are part of the evidence chain rather than neutral ground truth.", "claim_type": "benchmark_audit", "source_refs": ["B007", "B025"], "confidence": "high", "status": "supported", "cpcs_implication": "Version datasets/evaluators, preserve conflicts, and require human calibration."},
    {"claim_id": "C007", "claim": "Learned video evaluators correlate with humans but remain fallible and domain-dependent; no single VLM, tracker, pose estimator, flow model, or segmentation model should be treated as authoritative for all failure classes.", "claim_type": "evaluation_synthesis", "source_refs": ["B008", "B009", "B017", "B018", "B019", "B020", "B021"], "confidence": "high", "status": "supported", "cpcs_implication": "Use direct, semantic, measured, and human-review lanes with preserved disagreement."},
    {"claim_id": "C008", "claim": "XML, YAML, and JSON do not universally make an opaque text-prompt endpoint more intelligent or deterministic; their value is internal separation, compilation, validation, and controlled provider-specific A/B testing.", "claim_type": "repository_and_interface_inference", "source_refs": ["R005", "M002", "M007"], "confidence": "high for internal-control value; provider adherence effect unverified", "status": "partially verified", "cpcs_implication": "Keep one canonical JSON authority and emit one provider-native payload."},
    {"claim_id": "C009", "claim": "A visible bridge such as a mask, point track, silhouette, partial limb, or trajectory control can carry continuity evidence through occlusion, but its attachment to the correct entity must itself be verified.", "claim_type": "measurement/control synthesis", "source_refs": ["B013", "B018", "B019", "B020"], "confidence": "medium-high", "status": "mechanistically supported; generative effect size pending", "cpcs_implication": "Bind bridges to entity IDs and intervals; do not treat them as generic effects."},
    {"claim_id": "C010", "claim": "Shot decomposition is not merely a workaround; it converts hidden, dense, or mutually competing constraints into observable boundary states and smaller satisfiable generation problems.", "claim_type": "system_design_inference", "source_refs": ["B003", "B010", "R002"], "confidence": "high", "status": "supported as engineering strategy; effect sizes pending", "cpcs_implication": "Add deterministic split gates based on hidden-state duration, dependency depth, control loss, and observability."},
    {"claim_id": "C011", "claim": "The cited Google Vertex AI Veo 3.1 first/last-frame endpoint documents first-and-last frame conditioning, 4/6/8-second durations, 720p/1080p, seed, and negative prompt controls.", "claim_type": "official_capability", "source_refs": ["M001"], "confidence": "high", "status": "verified for cited endpoint/date", "cpcs_implication": "The Veo adapter may carry boundary frames and seed, but adherence still requires repeated-seed verification."},
    {"claim_id": "C012", "claim": "ByteDance's Seedance 2.0 official launch documents unified text, image, audio, and video references, up to 9 images, 3 videos, 3 audio clips, and up to 15-second multi-shot audio-video generation.", "claim_type": "official_capability", "source_refs": ["M004"], "confidence": "high", "status": "verified as documented capability", "cpcs_implication": "Create a multimodal-reference adapter and independently qualify reference priority/coreference."},
    {"claim_id": "C013", "claim": "Kling VIDEO 3.0's official guide documents T2V, I2V, start/end frames, native audio, multi-shot, element references, and flexible 3-15 second generation.", "claim_type": "official_capability", "source_refs": ["M005"], "confidence": "high", "status": "verified as documented capability", "cpcs_implication": "Map element/reference IDs and shot structure, but do not infer reliability from the guide."},
    {"claim_id": "C014", "claim": "MiniMax release/API documentation identifies Hailuo-2.3 as T2V/I2V and Hailuo-2.3-Fast as I2V, with documented duration/resolution combinations and a 2000-character T2V prompt field plus bracketed camera commands.", "claim_type": "official_capability", "source_refs": ["M006", "M007"], "confidence": "high", "status": "verified as documented capability", "cpcs_implication": "The adapter should distinguish text camera syntax from direct numeric control and test command adherence."},
    {"claim_id": "C015", "claim": "The official LTX repository documents LTX-2 workflows including synchronized audio-video, multiple keyframes, extension, video-to-video, and control models.", "claim_type": "official_capability", "source_refs": ["M008"], "confidence": "high", "status": "verified as repository-documented capability", "cpcs_implication": "Local/open adapters can expose stronger control carriers and reproducible configs, but checkpoint-specific qualification is mandatory."},
    {"claim_id": "C016", "claim": "The official Wan2.2 repository documents T2V, I2V, unified TI2V, speech-to-video, pose/control, and animation/replacement variants.", "claim_type": "official_capability", "source_refs": ["M009"], "confidence": "high", "status": "verified as repository-documented capability", "cpcs_implication": "Route by task checkpoint and record exact checkpoint/sampler/seed/hardware."},
    {"claim_id": "C017", "claim": "HunyuanVideo-1.5's official repository documents T2V and I2V workflows at 480p/720p with a 1080p super-resolution workflow and local seed/configuration controls.", "claim_type": "official_capability", "source_refs": ["M010"], "confidence": "high", "status": "verified as repository-documented capability", "cpcs_implication": "Keep generation and super-resolution qualification separate."},
    {"claim_id": "C018", "claim": "CogVideoX1.5's official repository documents T2V and I2V checkpoints with roughly 10-second model-family outputs and checkpoint-specific resolutions/frames.", "claim_type": "official_capability", "source_refs": ["M011"], "confidence": "medium-high", "status": "verify exact checkpoint before implementation", "cpcs_implication": "Capability negotiation must be checkpoint-specific."},
    {"claim_id": "C019", "claim": "Mochi 1 is an open preview model with an official repository, but its existence does not establish current commercial parity or reliable complex choreography.", "claim_type": "official_capability_with_limit", "source_refs": ["M012"], "confidence": "high", "status": "supported", "cpcs_implication": "Use only after local qualification and do not overgeneralize preview claims."},
    {"claim_id": "C020", "claim": "The repository already defines one provider-neutral CPCS kernel and canonical score; new failure research must extend those owners rather than create a second compiler or ontology.", "claim_type": "controlled_repository_observation", "source_refs": ["R001", "R002", "R003", "R006"], "confidence": "high", "status": "verified at repository SHA", "cpcs_implication": "Integrate through typed minimal extensions and governed second-brain records."},
    {"claim_id": "C021", "claim": "The current provider-capability schema is hard-coded to Google Vertex AI Veo 3.1 and therefore cannot represent the full provider matrix without a controlled schema generalization.", "claim_type": "controlled_repository_observation", "source_refs": ["R007"], "confidence": "high", "status": "verified at repository SHA", "cpcs_implication": "Generalize provider/model constants and capability fields while preserving existing adapter behavior."},
    {"claim_id": "C022", "claim": "The current verification-plan schema already has direct, semantic, measured, and human-review observability lanes, which are the correct ownership surface for failure-specific metrics.", "claim_type": "controlled_repository_observation", "source_refs": ["R008"], "confidence": "high", "status": "verified at repository SHA", "cpcs_implication": "Extend metric catalog and requirement types; do not build a second verifier."},
    {"claim_id": "C023", "claim": "The current compliance-report schema already supports interval-scoped evidence, conflicts, and bounded repairs that reassert existing canonical controls.", "claim_type": "controlled_repository_observation", "source_refs": ["R009"], "confidence": "high", "status": "verified at repository SHA", "cpcs_implication": "Add failure classification and repair escalation while preserving canonical authority."},
    {"claim_id": "C024", "claim": "The minimum sufficient anti-invention representation is not exhaustive frame scripting; it is a compact set of stable entity IDs/signatures, state ledger, event/causal graph, coordinate-frame spatial transitions, visibility intervals/hidden trajectories, boundary states, allowed variation, and forbidden transitions.", "claim_type": "evidence-backed synthesis", "source_refs": ["B002", "B003", "B011", "B014", "B015", "B017", "R006"], "confidence": "high as system design; exact field efficacy pending", "status": "research conclusion", "cpcs_implication": "Implement these as typed minimal extensions and test ablations against matched prose."},
    {"claim_id": "C025", "claim": "Audio-generation failure and visual-generation failure must be measured separately, then joined through typed cross-modal event anchors.", "claim_type": "benchmark_supported", "source_refs": ["B022", "B023", "B024"], "confidence": "high", "status": "supported", "cpcs_implication": "Store semantic and temporal audio alignment as separate verdicts."},
    {"claim_id": "C026", "claim": "No universal maximum actions-per-second or dependency-depth threshold can be responsibly asserted across providers; thresholds must be estimated by provider/version, duration, workflow, and task through repeated-seed distributions.", "claim_type": "methodological conclusion", "source_refs": ["B003", "M001", "M002", "M004", "M005", "M006"], "confidence": "high", "status": "supported", "cpcs_implication": "Learn empirical adapter budgets without promoting them before qualification."},
    {"claim_id": "C027", "claim": "Negative prompts should not replace positive state/count/causal contracts; negative-field behavior is provider-specific and must be tested.", "claim_type": "interface_and_control_inference", "source_refs": ["M001", "M003", "R005"], "confidence": "medium-high", "status": "partially verified", "cpcs_implication": "Compile positive invariants first and retain prohibitions in verification."},
    {"claim_id": "C028", "claim": "Exact numbers embedded in prose are not direct controls unless the provider documents and exposes the corresponding parameter or control carrier.", "claim_type": "interface conclusion", "source_refs": ["R004", "R005", "R007", "M002", "M007"], "confidence": "high", "status": "supported", "cpcs_implication": "Every numeric control needs a capability disposition: direct, media-carried, text approximation, evaluation-only, or unsupported."},
    {"claim_id": "C029", "claim": "Failed samples, prompts, seeds/configurations, provider versions, raw videos, evaluator versions, and human verdicts are required evidence; selected showcase clips cannot establish reliability.", "claim_type": "methodological conclusion", "source_refs": ["B007", "B008", "B009", "R003", "R010"], "confidence": "high", "status": "supported", "cpcs_implication": "Write immutable experiment bundles and rebuild derived knowledge from them."},
    {"claim_id": "C030", "claim": "This package does not establish provider-specific failure rates or rankings because no live repeated-seed generation was run with authenticated provider endpoints and raw output retention.", "claim_type": "scope_statement", "source_refs": [], "confidence": "certain", "status": "explicit limitation", "cpcs_implication": "Keep provider rules at research/proposal status until empirical qualification."},
    {"claim_id": "C031", "claim": "For exact contact, collision, fluid, debris, or body-support behavior, postproduction or simulation may be the lowest-risk solution even when a generator can produce a plausible-looking result.", "claim_type": "evidence-backed production inference", "source_refs": ["B004", "B005", "B006", "B026"], "confidence": "high", "status": "supported", "cpcs_implication": "The compiler should choose production method, not only prompt wording."},
    {"claim_id": "C032", "claim": "A successful result under one seed does not establish a control rule; repeated seeds and paired conditions are required to estimate success distributions and regressions.", "claim_type": "experimental-design conclusion", "source_refs": ["R003", "B007", "B008", "B009"], "confidence": "high", "status": "supported", "cpcs_implication": "Use screening and confirmatory stages with immutable per-seed evidence."},
    {"claim_id": "C033", "claim": "Reference capability is not equivalent to reference adherence: image/video/keyframe support must be version-scoped and empirically tested for identity, layout, motion, and role retention separately.", "claim_type": "capability/reliability distinction", "source_refs": ["M001", "M004", "M005", "M008", "M009"], "confidence": "high", "status": "supported", "cpcs_implication": "Provider profiles must separate documented carrier availability from measured success distributions."},
    {"claim_id": "C034", "claim": "Local repair must reverify the entire set of protected controls because interval regeneration, inpainting, compositing, or provider substitution can regress identity, style, timing, and camera continuity outside the primary failure dimension.", "claim_type": "system-design conclusion", "source_refs": ["R009", "B008", "B009"], "confidence": "high", "status": "supported", "cpcs_implication": "Preserve control IDs and run full regression verification after every repair."},
    {"claim_id": "C035", "claim": "The safest closed-loop policy is canonical target → provider compile/loss report → generation → multi-lane re-extraction → failure classification → smallest bounded repair → full re-verification → immutable experiment record.", "claim_type": "repository-and-evidence synthesis", "source_refs": ["R002", "R008", "R009", "R010"], "confidence": "high", "status": "research conclusion", "cpcs_implication": "Adopt this as the single failure-aware control loop."},
]

CATEGORY_OWNERS = {
    "Occlusion and hidden state": ("lab/compiler/schemas/universal_score.schema.json#continuity + entities + actions; lab/verification", "partial", "Typed visibility interval/hidden-path contract; failure-specific metrics; repeated-seed occlusion evidence"),
    "Object permanence and state": ("lab/compiler/schemas/universal_score.schema.json#continuity + entities + assets + interactions; lab/verification", "partial", "State-ledger typing, possession transitions, object-state tests, multi-shot persistence evidence"),
    "Identity and role": ("lab/compiler/schemas/universal_score.schema.json#entities + actions + interactions + performance + audio; lab/verification", "partial", "Multimodal identity signatures, role-edge typing, nonfacial verification calibration"),
    "Spatial and screen geography": ("lab/compiler/schemas/universal_score.schema.json#scenes + shots + camera + actions; lab/verification", "partial", "Coordinate-frame and state-transition contract, scene map, screen/world transform metrics"),
    "Temporal action and causality": ("lab/compiler/schemas/universal_score.schema.json#beats + actions + interactions + editing + audio; lab/verification", "partial", "Typed causal/event dependencies, feasibility/scheduling gate, provider action-density distributions"),
    "Contact, balance, and physics": ("lab/compiler/schemas/universal_score.schema.json#motion + interactions + actions + style; lab/verification", "partial", "Contact/support/deformation contracts, physics-aware metrics, control/post escalation evidence"),
    "Fluid, material, and VFX": ("lab/compiler/schemas/universal_score.schema.json#interactions + motion + style + continuity; lab/verification", "partial", "Material state/lifecycle contracts, solid-fluid event primitives, simulation/post policies"),
    "Camera, edit, and anime discontinuity": ("lab/compiler/schemas/universal_score.schema.json#camera + editing + style + motion + continuity; lab/verification", "partial", "Graphic-vs-world discontinuity typing, camera/actor track separation, recovery-frame metrics"),
    "Prompt and attention budget": ("lab/compiler + lab/FORMAT_CONTROL_MAP.md + provider profiles/adapters", "partial", "Attention-budget compiler, generalized provider capabilities, controlled format ablations"),
    "Audio and evaluator": ("lab/compiler/schemas/universal_score.schema.json#audio + verification_requirements; lab/verification", "partial", "Audio event ledger, evaluator catalog/calibration, conflict policy, unobservable gates"),
}

OVERLAP_ROWS = []
for f in FAILURES:
    owner, coverage, missing = CATEGORY_OWNERS[f["category"]]
    OVERLAP_ROWS.append({
        "failure_id": f["failure_id"],
        "failure_code": f["failure_code"],
        "failure_name": f["name"],
        "existing_owner": owner,
        "existing_coverage": coverage,
        "missing_evidence": "No provider/version repeated-seed CPCS qualification with raw retained outputs; literature/benchmark coverage is task-scoped.",
        "missing_mitigation": missing,
        "missing_test": f"Run {f['regression_fixtures'][0]}, {f['regression_fixtures'][1]}, and {f['regression_fixtures'][2]} across selected provider/version cells.",
        "recommended_owner": owner,
        "integration_class": ";".join(f["finding_classification"]),
    })

FIELD_OWNERSHIP_ROWS = [
    {"proposed_contract_or_field": "continuity.state_ledger", "existing_owner": "universal_score.continuity", "status": "minimal typed extension", "purpose": "Persist entity/object/environment states, possession, allowed transitions, and shot-boundary snapshots", "must_not_create": "parallel state database or second canonical score"},
    {"proposed_contract_or_field": "continuity.visibility_intervals", "existing_owner": "universal_score.continuity", "status": "minimal typed extension", "purpose": "Represent visible/partial/hidden states, occluder, hidden path, bridge, and reappearance", "must_not_create": "standalone occlusion compiler"},
    {"proposed_contract_or_field": "entities[].identity_signature", "existing_owner": "universal_score.entities", "status": "minimal typed extension", "purpose": "Bind face, body, hair, costume, voice, role, and reference assets to stable IDs", "must_not_create": "separate identity ontology"},
    {"proposed_contract_or_field": "actions[].event_edges", "existing_owner": "universal_score.actions/beats/interactions", "status": "minimal typed extension", "purpose": "Encode dependency, causality, role, concurrency, and phase timing", "must_not_create": "parallel event scheduler"},
    {"proposed_contract_or_field": "shots[].spatial_transition", "existing_owner": "universal_score.shots/camera/scenes", "status": "minimal typed extension", "purpose": "Coordinate frames, lane/depth transitions, axis policy, entrances/exits, camera transforms", "must_not_create": "separate scene-graph authority"},
    {"proposed_contract_or_field": "interactions[].contact_contract", "existing_owner": "universal_score.interactions/motion", "status": "minimal typed extension", "purpose": "Contact type, participants, regions, separation, reaction, support, allowed deformation", "must_not_create": "physics simulator represented as prompt schema"},
    {"proposed_contract_or_field": "editing[].discontinuity_type", "existing_owner": "universal_score.editing/style/continuity", "status": "minimal typed extension", "purpose": "Distinguish graphic effect, cut, world reset, hold, blur, and occlusion", "must_not_create": "parallel edit decision system"},
    {"proposed_contract_or_field": "audio.event_anchors", "existing_owner": "universal_score.audio/actions", "status": "minimal typed extension", "purpose": "Bind sounds/utterances to events, sources, timing, and semantic class", "must_not_create": "independent audio timeline authority"},
    {"proposed_contract_or_field": "provider capability generalization", "existing_owner": "lab/compiler/schemas/provider_capability.schema.json + providers", "status": "schema generalization", "purpose": "Represent provider/model/version-specific modes, controls, limits, audio, references, repair, and evidence", "must_not_create": "one-off adapter schemas per provider"},
    {"proposed_contract_or_field": "failure metrics catalog", "existing_owner": "verification_plan + compliance_report + lab/verification", "status": "typed metric extension", "purpose": "Attach observable dimensions, methods, versions, confidence, blind spots, and thresholds", "must_not_create": "second verifier or hidden promotion path"},
    {"proposed_contract_or_field": "failure records", "existing_owner": "second_brain frozen/curated/immutable/derived tiers", "status": "research proposal until qualification", "purpose": "Store source-grounded failure mechanisms and derived failure cards", "must_not_create": "direct research-to-curated self-promotion"},
]

# ---------------------------------------------------------------------------
# JSON Schemas
# ---------------------------------------------------------------------------

FAILURE_RECORD_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/failure-record/1.0",
    "title": "CPCS Failure Research Record",
    "type": "object",
    "required": [
        "failure_id", "failure_code", "name", "category", "definition", "scope",
        "trigger_conditions", "observed_symptoms", "suspected_causes", "evidence_class",
        "source_refs", "empirical_confidence", "severity", "likelihood_when_triggered",
        "canonical_fields_affected", "prompt_risk_patterns", "mitigations",
        "verification_metrics", "regression_fixtures", "provider_specific_notes",
        "unresolved_questions", "cpcs_impact", "finding_classification", "controllability",
        "research_status"
    ],
    "properties": {
        "failure_id": {"type": "string", "pattern": "^failure://"},
        "failure_code": {"type": "string", "pattern": "^[A-J][0-9]{2}$"},
        "name": {"type": "string", "minLength": 3},
        "category": {"type": "string", "minLength": 3},
        "definition": {"type": "string", "minLength": 20},
        "scope": {
            "type": "object",
            "required": ["providers", "models", "workflows", "version_scope"],
            "properties": {
                "providers": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                "models": {"type": "array", "items": {"type": "string"}},
                "workflows": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                "version_scope": {"type": "string"},
            },
            "additionalProperties": False,
        },
        "trigger_conditions": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "observed_symptoms": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "suspected_causes": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object",
                "required": ["mechanism_id", "mechanism", "causal_status"],
                "properties": {
                    "mechanism_id": {"type": "string", "pattern": "^mechanism://"},
                    "mechanism": {"type": "string"},
                    "causal_status": {"type": "string"},
                },
                "additionalProperties": False,
            },
        },
        "evidence_class": {"type": "string"},
        "source_refs": {"type": "array", "items": {"type": "string", "pattern": "^[RMB][0-9]{3}$"}},
        "empirical_confidence": {"type": "string"},
        "severity": {"enum": ["low", "medium", "high", "critical"]},
        "likelihood_when_triggered": {"type": "string"},
        "canonical_fields_affected": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "prompt_risk_patterns": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "mitigations": {
            "type": "array", "minItems": 2,
            "items": {
                "type": "object",
                "required": ["level", "level_name", "method", "expected_benefit", "token_or_character_cost", "generation_cost_impact", "risk_of_new_failure", "provider_dependency", "evidence_strength", "verification_method", "verification_metric_ids", "rollback", "limitations"],
                "properties": {
                    "level": {"enum": list(MITIGATION_LEVELS)},
                    "level_name": {"type": "string"},
                    "method": {"type": "string", "minLength": 10},
                    "expected_benefit": {"type": "string"},
                    "token_or_character_cost": {"type": "string"},
                    "generation_cost_impact": {"type": "string"},
                    "risk_of_new_failure": {"type": "string"},
                    "provider_dependency": {"type": "string"},
                    "evidence_strength": {"type": "string"},
                    "verification_method": {"type": "string"},
                    "verification_metric_ids": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": "^metric_"}},
                    "rollback": {"type": "string"},
                    "limitations": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                },
                "additionalProperties": False,
            },
        },
        "verification_metrics": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": "^metric_"}},
        "regression_fixtures": {"type": "array", "minItems": 3, "items": {"type": "string", "pattern": "^fixture://"}},
        "provider_specific_notes": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "unresolved_questions": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "cpcs_impact": {"type": "object", "minProperties": 10},
        "finding_classification": {"type": "array", "minItems": 1, "items": {"enum": ["knowledge_only", "contract_affecting", "implementation_affecting", "provider_version_affecting", "verification_affecting", "policy_affecting", "unverified"]}},
        "controllability": {"enum": ["preventable_by_prompting", "partially_mitigated_by_prompting", "requires_visual_or_control_conditioning", "requires_shot_decomposition", "requires_postproduction", "currently_unreliable_or_unsupported"]},
        "research_status": {"type": "string"},
    },
    "additionalProperties": False,
}

EVALUATION_METRICS_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/evaluation-metric/1.0",
    "title": "CPCS Failure Evaluation Metric",
    "type": "object",
    "required": ["metric_id", "name", "observable_dimension", "measurement_method", "unit", "threshold_policy", "evaluator_or_tool", "confidence", "known_blind_spots", "human_calibration_requirement", "source_refs"],
    "properties": {
        "metric_id": {"type": "string", "pattern": "^metric_[A-Za-z0-9._-]+$"},
        "name": {"type": "string", "minLength": 3},
        "observable_dimension": {"type": "string", "minLength": 10},
        "measurement_method": {"type": "string", "minLength": 10},
        "unit": {"type": "string"},
        "threshold_policy": {"type": "string"},
        "evaluator_or_tool": {"type": "string"},
        "confidence": {"type": "string"},
        "known_blind_spots": {"type": "string"},
        "human_calibration_requirement": {"type": "string"},
        "source_refs": {"type": "array", "items": {"type": "string", "pattern": "^[RMB][0-9]{3}$"}},
    },
    "additionalProperties": False,
}

EXPERIMENT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/failure-experiment/1.0",
    "type": "object",
    "required": ["schema", "experiment_id", "title", "status", "hypothesis", "failure_codes", "providers", "design", "variables", "conditions", "metrics", "sample_plan", "analysis_plan", "evidence_retention", "promotion_gate", "limitations"],
    "properties": {
        "schema": {"const": "cpcs.failure_experiment/1.0"},
        "experiment_id": {"type": "string", "pattern": "^experiment://failure/"},
        "title": {"type": "string"},
        "status": {"enum": ["designed_not_run", "screening", "confirmatory", "complete", "blocked"]},
        "hypothesis": {"type": "string"},
        "failure_codes": {"type": "array", "minItems": 1, "items": {"pattern": "^[A-J][0-9]{2}$"}},
        "providers": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "design": {"type": "object"},
        "variables": {"type": "object"},
        "conditions": {"type": "array", "minItems": 2, "items": {"type": "object"}},
        "metrics": {"type": "array", "minItems": 1, "items": {"pattern": "^metric_"}},
        "sample_plan": {"type": "object"},
        "analysis_plan": {"type": "object"},
        "evidence_retention": {"type": "array", "minItems": 5, "items": {"type": "string"}},
        "promotion_gate": {"type": "object"},
        "limitations": {"type": "array", "minItems": 1, "items": {"type": "string"}},
    },
    "additionalProperties": False,
}


def experiment(
    eid: str,
    title: str,
    hypothesis: str,
    failure_codes: list[str],
    conditions: list[dict[str, Any]],
    metrics: list[str],
    variables: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema": "cpcs.failure_experiment/1.0",
        "experiment_id": f"experiment://failure/{eid}",
        "title": title,
        "status": "designed_not_run",
        "hypothesis": hypothesis,
        "failure_codes": failure_codes,
        "providers": ["provider/model/version cells selected from PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv; exact endpoint required"],
        "design": {
            "type": "matched-condition repeated-seed ablation",
            "randomization": "Randomize condition order within provider and seed; blind human raters to provider and condition.",
            "paired_seed_policy": "Use the same exposed seed across matched conditions where the provider supports seed; otherwise randomize requests and treat samples as unpaired with provider request IDs retained.",
            "constant_controls": ["semantic target except ablated variable", "duration", "aspect ratio", "resolution", "provider/version", "reference assets except ablated reference", "safety settings", "prompt enhancement settings"],
        },
        "variables": variables,
        "conditions": conditions,
        "metrics": metrics,
        "sample_plan": {
            "smoke": "3 seeds/cell to detect invalid requests or catastrophic failure",
            "screening": "12 seeds/cell; report Wilson intervals for binary gates and bootstrap intervals for continuous metrics",
            "confirmatory": "30 paired seeds/cell for shortlisted contrasts; increase if interval width or effect-size uncertainty remains unacceptable",
            "stopping_rule": "Do not stop on a visually successful sample. Stop only for safety/cost caps, deterministic request failure, or pre-registered futility/superiority boundaries.",
        },
        "analysis_plan": {
            "primary": "Per-seed hard-lock pass rate and failure-class incidence, not selected best-of-N output.",
            "paired_tests": "McNemar for paired binary outcomes; paired bootstrap or permutation tests for continuous metrics; Cochran's Q for more than two paired conditions.",
            "multi_provider": "Hierarchical logistic/ordinal model with condition fixed effect and provider/version/task random effects when assumptions and sample size permit.",
            "multiple_comparisons": "Pre-register primary contrasts and control false discovery for secondary metrics.",
            "reporting": "Publish every seed, median, dispersion, confidence intervals, failures, evaluator disagreements, and cost/latency.",
        },
        "evidence_retention": [
            "canonical target and exact compiled provider payload",
            "provider/model/version/endpoint and request/response metadata",
            "seed/configuration and all reference/control assets with SHA-256",
            "raw generated video/audio including failed and rejected samples",
            "evaluator versions/configuration/raw outputs and human verdicts",
            "cost, latency, retry, moderation, and provider-error logs",
            "immutable manifest and checksums",
        ],
        "promotion_gate": {
            "minimum": "Confirmatory evidence must show the intervention improves the pre-registered primary metric without unacceptable regression on protected controls.",
            "authority": "Results remain immutable evidence/derived knowledge until reviewed and promoted through existing CPCS governance.",
            "disqualifiers": ["cherry-picked samples", "unknown model version", "missing raw failures", "changed prompt semantics", "unblinded single-rater judgment", "unresolved evaluator conflict on critical controls"],
        },
        "limitations": ["The package designs but does not execute authenticated provider generations.", "Provider behavior can change without model-name changes; access date and endpoint must be recorded."],
    }


EXPERIMENTS = [
    experiment(
        "e101_occlusion_continuity", "Occlusion continuity: splash width, visibility bridge, and hidden path",
        "Complete opaque occlusion will increase identity/count/path failures; a visible bridge and explicit hidden path will reduce them, with control media outperforming text-only on long occlusions.",
        ["A01", "A02", "A03", "A04", "A06", "A07", "G01"],
        [
            {"condition_id": "C0", "description": "No splash/control; same action and camera."},
            {"condition_id": "C1", "description": "Narrow partial splash; actor remains partially visible."},
            {"condition_id": "C2", "description": "Complete opaque splash; no hidden-path statement."},
            {"condition_id": "C3", "description": "Complete splash plus silhouette/bubble-trail visibility bridge."},
            {"condition_id": "C4", "description": "Complete splash plus Occlusion Continuity Contract compiled to concise text."},
            {"condition_id": "C5", "description": "Complete splash plus mask/trajectory/control media and boundary frames where supported."},
        ],
        ["metric_occlusion_continuity", "metric_actor_count_consistency", "metric_identity_continuity", "metric_reappearance_position_error", "metric_visibility_bridge_coverage", "metric_effect_origin_error"],
        {"independent": ["occlusion completeness", "occlusion duration", "visibility bridge", "hidden-path contract", "control media"], "strata": ["one vs two actors", "static vs moving camera", "realistic vs anime", "T2V vs I2V"]},
    ),
    experiment(
        "e102_prompt_serialization", "Identical-semantics prompt serialization and attention budget",
        "After semantic equivalence and length are controlled, duplicated formats will not universally outperform one concise authority; provider-specific differences may exist.",
        ["I01", "I03", "I04", "I05", "I06"],
        [
            {"condition_id": "NL", "description": "Ordered natural language."},
            {"condition_id": "YAML", "description": "Flat YAML rendered into the provider text field."},
            {"condition_id": "XML", "description": "Minimal XML event envelope rendered into the provider text field."},
            {"condition_id": "JSON", "description": "Compact JSON rendered into the provider text field."},
            {"condition_id": "XML_JSON", "description": "XML containing duplicated JSON semantics."},
            {"condition_id": "XML_JSON_YAML", "description": "Three duplicated semantic representations."},
        ],
        ["metric_event_graph_agreement", "metric_control_retention", "metric_human_readability", "metric_observability_coverage"],
        {"independent": ["serialization", "character count", "field order", "provider prompt enhancement on/off"], "constraints": ["identical normalized semantics", "same hard-lock ordering", "no hidden format-specific details"]},
    ),
    experiment(
        "e103_action_density", "Action density and dependency-depth breakpoint",
        "Event omission/merge/order error will rise with primary action count and dependency depth; the breakpoint is provider/version/task specific.",
        ["E01", "E02", "E03", "E04", "E07", "E08"],
        [
            {"condition_id": "A1", "description": "One primary action with setup and recovery."},
            {"condition_id": "A3", "description": "Three sequential primary actions."},
            {"condition_id": "A5", "description": "Five sequential primary actions."},
            {"condition_id": "FULL", "description": "Full choreography."},
            {"condition_id": "SPLIT", "description": "Full choreography split at stable state boundaries and edited."},
        ],
        ["metric_event_graph_agreement", "metric_temporal_event_error", "metric_causal_edge_accuracy", "metric_human_readability", "metric_control_retention"],
        {"independent": ["primary action count", "dependency depth", "duration", "actor count", "shot split"], "outputs": ["provider-specific pass-rate curves", "estimated breakpoint with uncertainty"]},
    ),
    experiment(
        "e104_spatial_control", "Spatial control carrier: prose, lanes, coordinates, storyboard, and depth/pose",
        "Explicit coordinate frames and visual spatial controls will reduce direction, depth, axis, and target-region errors relative to unqualified prose.",
        ["D01", "D02", "D03", "D04", "D05", "D06", "C06"],
        [
            {"condition_id": "VERBAL", "description": "Unqualified left/right prose."},
            {"condition_id": "FRAMED", "description": "Qualified screen/world/actor/camera directions."},
            {"condition_id": "LANES", "description": "Explicit screen and depth lanes plus axis policy."},
            {"condition_id": "COORDS", "description": "Normalized coordinates in text with explicit evaluation-only disposition if unsupported."},
            {"condition_id": "STORYBOARD", "description": "Reference storyboard/keyframes."},
            {"condition_id": "CONTROL", "description": "Pose/depth/mask/trajectory control where supported."},
        ],
        ["metric_spatial_relation_accuracy", "metric_screen_direction_consistency", "metric_axis_crossing_count", "metric_depth_order_accuracy", "metric_reappearance_position_error"],
        {"independent": ["spatial carrier", "camera complexity", "actor crossing"], "strata": ["single shot", "cut", "orbit", "reverse angle"]},
    ),
    experiment(
        "e105_causality", "Compressed event description versus explicit causal event graph",
        "Explicit cause/initiator/target/onset/apex/consequence/reaction/recovery edges will reduce premature and mislocalized effects compared with compressed action nouns.",
        ["E04", "E05", "E06", "F07", "G01", "G03"],
        [
            {"condition_id": "COMPRESSED", "description": "Compressed event phrase, e.g. 'axe kick, splash, B submerged'."},
            {"condition_id": "ORDERED_PROSE", "description": "Ordered causal prose with explicit initiator/target and 'only after'."},
            {"condition_id": "EVENT_GRAPH_TEXT", "description": "Canonical event graph compiled into concise provider-native text."},
            {"condition_id": "EVENT_GRAPH_VISUAL", "description": "Event graph plus contact/origin keyframes or controls."},
        ],
        ["metric_causal_edge_accuracy", "metric_reaction_latency_error", "metric_effect_origin_error", "metric_event_graph_agreement", "metric_temporal_event_error"],
        {"independent": ["causal representation", "effect density", "contact visibility"], "critical_edges": ["initiator", "target", "cause", "consequence", "reaction"]},
    ),
    experiment(
        "e106_repair", "Repair strategy: full regenerate, localized interval, shot split/edit, and postproduction",
        "Localized repair and postproduction will preserve more already-passing controls than full regeneration, but can introduce boundary artifacts requiring full re-verification.",
        ["A01", "E06", "F01", "G01", "H05", "J01"],
        [
            {"condition_id": "FULL_REGEN", "description": "Regenerate full clip with revised prompt."},
            {"condition_id": "LOCAL_REGEN", "description": "Regenerate only failing interval with fixed boundaries."},
            {"condition_id": "SHOT_SPLIT", "description": "Split and edit at stable state boundary."},
            {"condition_id": "POST", "description": "Preserve core motion and replace effect/audio/contact concealment in postproduction."},
            {"condition_id": "SUBSTITUTE", "description": "Use a provider/model with a stronger required carrier."},
        ],
        ["metric_control_retention", "metric_event_graph_agreement", "metric_identity_continuity", "metric_camera_motion_agreement", "metric_evaluator_disagreement"],
        {"independent": ["repair level", "failure type", "boundary observability"], "costs": ["generation dollars", "human minutes", "latency", "new-regression count"]},
    ),
    experiment(
        "e107_identity_role", "Identity and role retention under similarity, crossing, occlusion, and cuts",
        "Distinct multimodal signatures, role edges, stable lanes, and separate references will reduce identity/role swaps, especially at crossings and recurrence gaps.",
        ["C01", "C02", "C03", "C04", "C05", "C06", "C07"],
        [
            {"condition_id": "SIMILAR", "description": "Similar actors; prose labels only."},
            {"condition_id": "COLOR", "description": "Distinct wardrobe/color signatures."},
            {"condition_id": "ROLE", "description": "Stable IDs plus typed initiator/target/speaker edges."},
            {"condition_id": "REF", "description": "Separate multi-view actor/voice references."},
            {"condition_id": "LANE", "description": "References plus stable screen/depth lanes; no crossing."},
        ],
        ["metric_identity_continuity", "metric_role_assignment_accuracy", "metric_actor_count_consistency", "metric_screen_direction_consistency", "metric_lip_sync_offset"],
        {"independent": ["actor similarity", "identity carrier", "role contract", "crossing", "recurrence distance"], "strata": ["two actors", "three actors", "dialogue", "contact"]},
    ),
    experiment(
        "e108_contact_physics", "Contact/support control escalation",
        "Text contracts improve semantic targeting but precise contact/support will require visual control or shot redesign for high pass rates.",
        ["F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08"],
        [
            {"condition_id": "PROSE", "description": "Natural-language contact/action."},
            {"condition_id": "CONTRACT", "description": "Typed contact/support/phase contract compiled to text."},
            {"condition_id": "KEYFRAMES", "description": "Contract plus setup/apex/recovery keyframes."},
            {"condition_id": "CONTROL", "description": "Pose/depth/trajectory/control video."},
            {"condition_id": "CHEAT", "description": "Camera-cheated contact or shot decomposition."},
        ],
        ["metric_contact_distance", "metric_penetration_duration", "metric_foot_slip_distance", "metric_support_plausibility", "metric_momentum_continuity", "metric_reaction_latency_error"],
        {"independent": ["control level", "contact type", "actor count", "camera visibility"], "styles": ["realistic", "cinematic", "anime"]},
    ),
    experiment(
        "e109_material_vfx", "Solid-fluid and VFX causality",
        "Material contracts plus visual origin/control or postproduction will reduce effect-before-cause, wrong-origin, and persistence failures more than effect adjectives alone.",
        ["G01", "G02", "G03", "G04", "G05", "G06", "G07"],
        [
            {"condition_id": "EFFECT_NOUN", "description": "Effect named without causal/material lifecycle."},
            {"condition_id": "MATERIAL_CONTRACT", "description": "Cause, material state, origin, lifecycle, and residual state compiled to text."},
            {"condition_id": "ORIGIN_CONTROL", "description": "Contract plus origin mask/trajectory/keyframes."},
            {"condition_id": "POST", "description": "Clean action plus simulated/composited effect."},
        ],
        ["metric_effect_origin_error", "metric_effect_decay_error", "metric_material_state_consistency", "metric_causal_edge_accuracy", "metric_penetration_duration"],
        {"independent": ["material", "effect control", "occlusion completeness", "camera motion"], "materials": ["water", "smoke", "dust", "debris", "cloth/hair"]},
    ),
    experiment(
        "e110_camera_edit_anime", "Camera/edit discontinuity and anatomy recovery",
        "Separating camera/world tracks and defining graphic-only intervals with recovery frames will reduce teleportation, scene reset, and persistent smear anatomy.",
        ["H01", "H02", "H03", "H04", "H05", "H06", "H07"],
        [
            {"condition_id": "COMBINED", "description": "Complex camera, action, and effect in one prose prompt."},
            {"condition_id": "SEPARATED_TEXT", "description": "Independent camera/world tracks plus discontinuity/recovery contract."},
            {"condition_id": "BOUNDARY_FRAMES", "description": "Contract plus pre/post keyframes."},
            {"condition_id": "SPLIT", "description": "Camera/effect/action split into shots."},
            {"condition_id": "POST", "description": "Clean generated motion plus blur/flash/smear/reframe in postproduction."},
        ],
        ["metric_camera_motion_agreement", "metric_camera_actor_entanglement", "metric_edit_graphic_classification", "metric_anatomy_recovery_latency", "metric_identity_continuity"],
        {"independent": ["camera complexity", "graphic discontinuity", "recovery carrier"], "styles": ["realistic", "anime"]},
    ),
    experiment(
        "e111_audio_sync", "Cross-modal event and lip-sync anchors",
        "Typed source/event/time anchors and postproduction alignment will reduce semantic and temporal audio mismatch compared with unconstrained joint generation.",
        ["J01", "J02", "J03", "C07"],
        [
            {"condition_id": "JOINT_GENERIC", "description": "Joint generation with generic audio instruction."},
            {"condition_id": "JOINT_ANCHORED", "description": "Joint generation with typed event/source/timing anchors."},
            {"condition_id": "SEPARATE_AUDIO", "description": "Picture generation followed by sound design/voice/lip-sync postproduction."},
        ],
        ["metric_audio_event_alignment", "metric_lip_sync_offset", "metric_role_assignment_accuracy", "metric_event_graph_agreement"],
        {"independent": ["audio workflow", "speaker count", "event density"], "strata": ["speech", "impact", "water", "music accent"]},
    ),
    experiment(
        "e112_evaluator_calibration", "Evaluator blind spots and adjudication calibration",
        "Single evaluators will produce failure-class-specific false positives/negatives; multi-lane evidence with human adjudication will reduce false certainty.",
        ["J04", "J05", "J06", "J07", "J08"],
        [
            {"condition_id": "VLM_ONLY", "description": "Single version-pinned VLM with sparse sampling."},
            {"condition_id": "VLM_TARGETED", "description": "Event-targeted dense frame windows and neutral questions."},
            {"condition_id": "MEASUREMENT", "description": "Tracking/segmentation/pose/flow/audio lanes."},
            {"condition_id": "MULTI_LANE", "description": "Semantic + measurement + blinded human adjudication with conflicts preserved."},
        ],
        ["metric_evaluator_disagreement", "metric_observability_coverage", "metric_human_readability", "metric_contact_distance", "metric_edit_graphic_classification"],
        {"independent": ["evaluator lane", "frame sampling", "domain/style", "occlusion/blur"], "gold": ["human-annotated event intervals", "identity/role labels", "known flash/cut labels", "known control violations"]},
    ),
]
assert len(EXPERIMENTS) == 12

CPCS_INTEGRATION_RECOMMENDATIONS = f"""# CPCS Integration Recommendations

## Architectural verdict

The repository already has the correct top-level control plane: one canonical universal score, one compiler/provider-build boundary, one render-verification owner, one immutable experiment/evidence path, and a human-curated second brain. The failure research should **extend those owners**, not add a failure compiler, separate ontology, or second canonical score.

The inspected architecture explicitly treats the fully resolved JSON score as semantic authority. Provider prompts and requests are projections; research and derived evidence cannot silently mutate curated truth. These laws should remain unchanged.

## Minimal candidate extensions

""" + md_table(
    ["Candidate extension", "Existing owner", "Purpose", "Classification", "Promotion gate"],
    [
        ["continuity.state_ledger", "universal score continuity", "Persistent existence, visibility, count, possession, material/object state, irreversible deltas, terminal state", "contract_affecting", "schema review + compiler fixture + verifier"],
        ["continuity.visibility_intervals", "universal score continuity", "Occlusion start/end, hidden path, reappearance region, visibility bridge, permitted/forbidden state changes", "contract_affecting", "occlusion ablation + artifact-bound verification"],
        ["continuity.identity_ledger", "entities + continuity", "Identity signatures, role, voice, costume, body proportions, screen/depth lane history", "contract_affecting", "identity fixtures + human-calibrated metric"],
        ["continuity.spatial_state", "scenes/shots/camera", "Coordinate frames, world/screen/depth transitions, axis and eyeline state", "contract_affecting", "spatial fixtures + camera calibration"],
        ["actions.event_graph", "beats/actions", "Ordered events, dependencies, cause/effect, onset/apex/reaction/recovery", "contract_affecting", "topological validation + temporal evaluator"],
        ["interactions.contact_support", "interactions/motion", "Contact type, target region, distance/separation, support foot, base of support, permitted near-contact cheat", "contract_affecting", "measured + human lane"],
        ["interactions.material_response", "interactions/style/continuity", "Material type, impact origin, displacement, topology invariants, effect lifetime", "contract_affecting", "material-specific fixtures"],
        ["camera.explicit_tracks", "camera + motion", "Separate camera translation/rotation/lens from actor world/screen motion", "implementation_affecting", "camera/actor ablation + estimator calibration"],
        ["editing.discontinuity_contract", "editing + continuity", "Distinguish cut, flash, smear, hold, blur, wipe, occlusion, and world-state reset", "contract_affecting", "effect-vs-cut fixtures"],
        ["style.deformation_recovery", "style + motion + continuity", "Authored deformation interval, silhouette anchors, maximum exposure, required anatomy recovery frame", "contract_affecting", "anime-specific human calibration"],
        ["audio.event_anchors", "audio + actions/beats", "Bind sound/speech/music events to visual event IDs and time windows", "contract_affecting", "AV-sync fixtures"],
        ["verification.failure_assertions", "lab/verification", "Failure ID, interval, observable lane, metric/version, threshold, conflicts, human requirement", "verification_affecting", "evaluator qualification"],
        ["provider capability generalization", "lab/compiler/providers", "Version-scoped modes, references, controls, prompt limits, seed/rewrite behavior, audio, edit modes", "provider_version_affecting", "official docs + one live canary + replay evidence"],
        ["failure/mitigation evidence objects", "lab/second_brain", "Curated failure concepts, immutable provider observations, derived mitigation ranking", "knowledge_only then implementation_affecting", "distill + human curation + isolated comparisons"],
    ]
) + f"""

## Repository overlap result

`REPOSITORY_OVERLAP_MATRIX.csv` maps every one of the {len(FAILURE_RECORDS)} failure records to an existing owner. All rows are currently `partial`: the repository has a location for the meaning, but not complete versioned failure contracts, metrics, repeated-seed evidence, and provider-specific mitigation distributions.

The missing requested root `REPO_CONTINUITY_IMPLEMENTATION_PLAN.md` is recorded as an unresolved repository gap. This package does not create a replacement because doing so could establish a parallel or obsolete plan without owner confirmation.

## Integration sequence

### Phase 0 — Ingest as non-authoritative research

- Register `SOURCE_CATALOG.csv`, `CLAIM_SOURCE_MATRIX.csv`, and selected Markdown passages through the existing source-extraction/distillation path.
- Stage failure concepts, mechanism claims, metric methods, and provider capability candidates.
- Preserve source IDs, dates, locators, confidence, and limitations.
- Do not promote machine-generated records automatically.

### Phase 1 — Add typed candidate fields behind the universal score

- Extend only existing score objects.
- Add closed JSON Schema definitions and field-specific merge operators.
- Add migration/adaptation only where existing fixtures require it.
- Fail on unknown/conflicting fields; never generic-recursive-merge continuity state.
- Keep provider strings and prompts out of the score.

### Phase 2 — Compile and report loss

- Add one provider at a time through the existing capability-profile owner.
- For every canonical field, emit `supported_native`, `compressed_to_text`, `delegated_to_asset`, `evaluation_only`, or `unsupported`.
- Make prompt overflow and hard-lock loss fatal.
- Capture provider-side prompt enhancement/rewrite settings.

### Phase 3 — Implement the minimum verifier set

Start with the highest-value deterministic or human-calibratable checks:

1. actor/object count and existence;
2. identity/role checkpoints around cuts and occlusions;
3. event order and effect origin;
4. screen side, reappearance region, and target region;
5. object possession/state transitions;
6. contact/penetration with explicit human review;
7. flash-vs-cut and recovery-frame assertions;
8. audio-event onset offsets.

Each metric must record evaluator/version/configuration, artifact hash, lane, blind spots, threshold policy, and human-calibration status.

### Phase 4 — Run sealed repeated-seed experiments

- Use the YAML fixtures in `experiments/`.
- Prepare exact canonical builds before sealing.
- Isolate one control difference per causal comparison.
- Record every candidate, failed output, cost, latency, and verdict.
- Reflect provider/model-conditioned mitigation weights only after immutable evidence exists.

### Phase 5 — Learn bounded routing, never truth

Derived evidence may recommend:

```text
failure family + provider/model/version + task complexity
→ cheapest mitigation level with acceptable success distribution
```

It may not rewrite canonical truth, override hard locks, or promote a provider marketing claim. Human authority remains the promotion gate.

## Acceptance checks for implementation

```bash
python3 -m lab.compiler.score validate
python3 -m lab.compiler.build validate
python3 -m lab.verification.verify validate
python3 -m lab.second_brain.src.validate schemas
python3 -m lab.second_brain.src.validate control-plane
python3 -m unittest discover -s lab/compiler/tests -p "test_*.py"
python3 -m unittest discover -s lab/verification/tests -p "test_*.py"
python3 -m unittest discover -s lab/second_brain/tests -p "test_*.py"
```

New tests should prove that the same canonical target produces stable semantic projections, hard locks cannot be dropped, unknown provider controls become explicit loss, evaluator conflicts remain unresolved, and `rm -rf lab/second_brain/derived` rebuilds byte-identically.
"""

MINIMUM_SUFFICIENT_REPRESENTATION = """# Minimum Sufficient Representation

## Evidence-backed answer

There is no representation that can **guarantee** a stochastic generative model will never invent information. The minimum sufficient CPCS representation is instead the smallest target that removes avoidable ambiguity, exposes unsupported obligations, selects the right conditioning carrier, and makes every critical failure observable.

For a visually ambiguous transition, that target must contain at least:

### 1. Persistent entity identity

```text
stable entity_id
entity type
actor/object count
identity/costume/body/voice signature
role
existence separate from visibility
allowed and forbidden identity/state changes
```

### 2. State ledger

```text
initial state
state at each critical beat/shot boundary
irreversible deltas
object inventory and possession
material/environment state
terminal state
invariants that remain true through occlusion and cuts
```

### 3. Ordered event graph

```text
initiator
target
action
onset
apex
consequence
reaction delay
recovery
before / only_after / while / causes / prevents / terminates edges
```

### 4. Spatial state transition

```text
explicit coordinate frame
world position versus screen projection
screen and depth lanes
camera pose/motion/lens state
entry trajectory
expected target/reappearance region
axis, eyeline, and crossing rules
```

### 5. Visibility and hidden-state contract

```text
occluder and subject IDs
start/end of partial or complete occlusion
subject remains existing while invisible
hidden motion path or control reference
visibility bridge when available
required reappearance state and region
actor/object count lock
```

### 6. Interaction, support, and material contract

```text
contact type or near-contact cheat
contact target region and interval
minimum separation / penetration tolerance
support foot or surface
momentum/reaction/recovery obligations
material impact origin, displacement, topology, and effect lifetime
```

### 7. Graphic, edit, and deformation contract

```text
cut versus flash versus smear versus occlusion
whether world time advances
whether world state may change
allowed stylized deformation interval
required anatomy/style recovery frame
```

### 8. Audio anchors

```text
sound/speech/music event ID
visual cause or off-screen classification
speaker/voice identity
target onset and permitted offset
```

### 9. Provider realization and loss

```text
exact provider/model/version/interface
supported carrier for each hard control
prompt/reference/control asset projection
rewrite/enhancement setting
unsupported/evaluation-only controls
character/token budget and overflow decision
```

### 10. Verification assertions

```text
failure/metric ID
artifact and interval
observable lane
method/evaluator/version/configuration
threshold policy
known blind spots
human-review requirement
critical versus advisory severity
```

## When prompt-only generation remains reasonable

Prompt-only is reasonable when the scene has a small number of visually distinct persistent entities; primary events are simple and mostly visible; spatial relations do not require an exact hidden path; contact and physical consequences are perceptual rather than geometric; the camera is simple; the terminal state is easy to state; and failures can be tolerated or cheaply regenerated.

## When to escalate to references

Use reference images/storyboards when identity, product geometry, wardrobe, layout, first/last pose, style, or reappearance state must be visually anchored but the time-varying path remains flexible.

## When to escalate to control media

Use masks, pose, points, depth, trajectories, camera paths, beat/audio tracks, or source/control video when a hard requirement is time-varying and not continuously observable from text: hidden motion, precise path, multi-actor assignment, contact geometry, camera motion, lip sync, or material/effect origin.

## When to split the shot

Split when dependency depth, action density, actor similarity/crossings, complete occlusion, contact, camera motion, effects, and audio anchors combine beyond the measured provider/task envelope; when the prompt budget cannot retain all hard controls; or when a clean state handoff is cheaper than asking the model to infer an invisible transition.

## When to use postproduction

Use deterministic postproduction for exact splash/smoke/flash/shake/audio timing, logos/text, precise object count and product geometry, clean occlusion used to hide a safe edit, or material effects whose topology and causal origin must be exact.

## When to declare unsupported

Declare unsupported when no available provider or controlled workflow can carry and verify the hard requirement at an acceptable success rate and cost. The correct system output is an explicit limitation and alternative production plan, not an overconfident prompt.
"""

EVALUATOR_FAILURES_DOC = """# Evaluator Failures

## Principle

A generated artifact is not correct because one VLM, tracker, pose estimator, shot detector, or aggregate metric says it is. Evaluation is itself a perception and reasoning problem. CPCS must preserve direct, semantic, measured, and human-review lanes without averaging away disagreement.

## Six primary evaluator failures

""" + "\n\n".join(render_failure_record(r) for r in failure_records_for(["P"])) + """

## Calibration policy

An evaluator can block or promote a provider/model/version only after:

- exact evaluator/version/configuration are pinned;
- the artifact hash and analyzed interval are bound;
- in-domain positive and negative fixtures are labeled by humans;
- false-positive and false-negative rates are reported by failure family;
- hard cases include fast events, full occlusion, reflections, actor crossings, camera zoom/translation, anime smears, and partial visibility;
- confidence and unobservable states are preserved;
- conflicts invoke human review instead of confidence averaging.

## Recommended lanes

""" + md_table(
    ["Dimension", "Primary lane", "Secondary lane", "Known hazard"],
    [
        ["actor/object count", "tracking + segmentation", "human", "reflection, occlusion, fusion, small objects"],
        ["identity/role", "appearance + trajectory + event assignment", "human", "similar actors, cuts, effects"],
        ["event order/causality", "atomic temporal semantic questions", "frame/timecode human review", "sparse frame sampling and plausible priors"],
        ["contact/penetration", "pose/depth/distance measurement", "human", "2D overlap is not 3D contact"],
        ["support/foot slip", "pose + optical flow + contact state", "human", "camera motion, stylization, occlusion"],
        ["camera motion", "geometric estimator", "semantic estimator + human", "zoom versus translation, weak parallax"],
        ["flash/cut/smear", "effect-aware shot classifier", "human", "full-frame histogram discontinuity"],
        ["material response", "effect origin/segmentation + temporal questions", "human", "fluid topology and transparency"],
        ["audio sync", "event onset/cross-modal model", "human", "semantic match can hide temporal offset"],
        ["human readability", "human rubric", "multi-evaluator support", "rater disagreement and cultural/style preference"],
    ]
) + """

## Aggregation rule

Critical assertions are conjunctive: one failure blocks the artifact even when the aggregate score is high. Advisory dimensions may be summarized, but the report must retain per-assertion raw values, failed intervals, evaluator provenance, conflicts, and human overrides.
"""

UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL = """# Unverified, Contradictory, and Anecdotal Findings

## Purpose

This file prevents attractive but unproven claims from entering CPCS as truth. Items here are hypotheses, capability ambiguities, or version-sensitive statements that require official interface capture, controlled generation, independent reproduction, or human calibration.

## Provider capability ambiguities

- **Veo 3.1 audio and 4K behavior are endpoint/mode specific.** The current repository profile sets `sound_generation=false` and 720p/1080p. Current Google documentation contains model/preview/mode distinctions that must be captured per endpoint rather than generalized.
- **Seedance 2.0 exact native API limits were not fully verified for every access surface.** The official launch documents multimodal inputs and up to 15-second AV generation, but adapter products may expose different limits and behavior.
- **Kling 3.0 exact API schemas, prompt limits, resolutions, and region/account availability require interface capture.** Official company materials establish broad multimodal capability, not reliability.
- **Runway third-party model adapters are separate surfaces.** A Seedance, Veo, or other model accessed through Runway must not inherit native-provider assumptions without qualification.
- **Wan regional endpoints and prompt rewriting can differ.** The selected region, endpoint alias, rewrite setting, and returned metadata must be recorded.
- **LTX repository performance claims depend on checkpoint, sampler, quantization, VAE, hardware, and workflow.** Local runs must pin all of them.
- **Ray 3.2 product and API availability can differ.** This package treats the documented Ray 3.2 workflow as source-video modification, not general T2V/I2V generation.
- **Sora 2 is not represented as a current CPCS provider.** The official current status page states the consumer Sora product is unavailable as of 2026-04-26, and no current public production interface was verified in this pass.

## Unverified control claims

- XML, YAML, or JSON may improve human/compiler organization, but no universal provider-side intelligence gain is established.
- Exact timestamps, numeric coordinates, camera values, or biomechanics parameters may be semantically approximated when the provider accepts only prompt text.
- Negative prompts can reduce some unwanted concepts, but they do not prove state persistence or causal correctness and may prime the forbidden concept in some settings.
- First/last frames may improve endpoints without improving—and sometimes while worsening—the intermediate path. Effect size is provider/task dependent.
- More references can create reference conflict, identity blending, or priority dilution; a higher reference count is not automatically better.
- Same-seed comparisons reduce one source of variation where supported but do not establish byte-identical or semantically isolated outputs.
- Provider prompt enhancement may improve aesthetics while changing canonical semantics. It must be a separate arm.

## Research/benchmark uncertainty

- Several important 2026 benchmarks in the source catalog are recent preprints. Their methods, rankings, code, and conclusions may change after peer review or independent reproduction.
- Benchmark prompts and evaluated model versions age quickly relative to commercial releases.
- Automated physical and semantic judges can share blind spots with the systems they evaluate.
- Simulated counterfactual and video-prediction benchmarks inform continuity mechanisms but do not directly measure every cinematic generative-video workflow.
- Aggregate benchmark results cannot predict success for one exact CPCS scene without a matched fixture.

## Community anecdotes

No community anecdote is used as final evidence in this package. Reports such as “Kling ignores JSON,” “Seedance preserves characters better,” “Veo understands physics,” or “XML works better” should enter only as versioned experiment hypotheses with exact prompts, interfaces, outputs, and dates.

## 100% certainty boundary

The package cannot verify with 100% certainty the hidden internal mechanism of closed commercial models, current account/region availability for every provider, undocumented prompt parsing, future service changes, or provider-specific reliability without executing the sealed campaigns. All such conclusions are marked as inference, current capability documentation, or not run.
"""


# ---------------------------------------------------------------------------
# Empirical program
# ---------------------------------------------------------------------------

EXPERIMENT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "cpcs://research/experiment-plan/1.0",
    "type": "object",
    "required": [
        "schema_version", "experiment_id", "title", "status", "research_question", "hypothesis",
        "providers", "fixed_factors", "arms", "seed_policy", "metrics", "critical_assertions",
        "human_review", "retention", "analysis", "stop_conditions"
    ],
    "properties": {
        "schema_version": {"const": "cpcs.experiment_plan/1.0"},
        "experiment_id": {"type": "string", "pattern": "^experiment://failure/[a-z0-9_/-]+/1$"},
        "title": {"type": "string"},
        "status": {"enum": ["designed_not_run", "authorized", "running", "complete", "blocked"]},
        "research_question": {"type": "string"},
        "hypothesis": {"type": "string"},
        "providers": {"type": "array", "minItems": 1, "items": {"type": "object"}},
        "fixed_factors": {"type": "object"},
        "arms": {
            "type": "array", "minItems": 2,
            "items": {
                "type": "object",
                "required": ["arm_id", "label", "isolated_control", "canonical_semantics", "provider_projection"],
                "properties": {
                    "arm_id": {"type": "string"},
                    "label": {"type": "string"},
                    "isolated_control": {"type": "string"},
                    "canonical_semantics": {"type": "string"},
                    "provider_projection": {"type": "string"}
                },
                "additionalProperties": True
            }
        },
        "seed_policy": {"type": "object"},
        "metrics": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": "^metric_[a-z0-9_]+$"}},
        "critical_assertions": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "human_review": {"type": "object"},
        "retention": {"type": "object"},
        "analysis": {"type": "object"},
        "stop_conditions": {"type": "array", "minItems": 1, "items": {"type": "string"}}
    },
    "additionalProperties": True
}


def experiment(
    experiment_id: str,
    title: str,
    question: str,
    hypothesis: str,
    fixed_factors: dict[str, Any],
    arms: list[dict[str, Any]],
    metrics: list[str],
    assertions: list[str],
) -> dict[str, Any]:
    return {
        "schema_version": "cpcs.experiment_plan/1.0",
        "experiment_id": experiment_id,
        "title": title,
        "status": "designed_not_run",
        "blocked_reason": "No authorized provider credentials, generation budget, local model weights, or human rating panel were supplied in this session.",
        "research_question": question,
        "hypothesis": hypothesis,
        "providers": [
            {"provider": "google_vertex_ai", "model": "veo-3.1-generate-001", "status": "candidate_requires_authorization_and_live_profile_check"},
            {"provider": "runway", "model": "gen4.5", "status": "candidate_requires_authorization"},
            {"provider": "bytedance_seed", "model": "Seedance 2.0 native exact endpoint TBD", "status": "candidate_requires_interface_capture"},
            {"provider": "kuaishou", "model": "Kling Video 3.0/Omni exact endpoint TBD", "status": "candidate_requires_interface_capture"},
            {"provider": "minimax", "model": "MiniMax-Hailuo-2.3", "status": "candidate_requires_authorization"},
            {"provider": "alibaba_model_studio", "model": "wan2.7 exact endpoint by mode", "status": "candidate_requires_region_and_endpoint_pin"},
            {"provider": "local", "model": "LTX-2 or Wan2.2 exact checkpoint/workflow", "status": "candidate_requires_weights_and_hardware_workflow"}
        ],
        "fixed_factors": fixed_factors,
        "arms": arms,
        "seed_policy": {
            "initial_completed_candidates_per_arm": 20,
            "open_local_target_per_arm": 30,
            "pairing": "Use identical seed values within provider where exposed; record retry/sample identifiers when seeds are unavailable.",
            "interpretation": "Seed pairing reduces one variation source but does not imply identical output or perfect causal isolation.",
            "randomization": "Randomize arm execution order within provider and batch; do not select best-of-N for the primary analysis."
        },
        "metrics": metrics,
        "critical_assertions": assertions,
        "human_review": {
            "required": True,
            "minimum_reviewers": 2,
            "blind_to_arm": True,
            "adjudication": "A third reviewer adjudicates disagreement on any critical assertion; preserve all original labels."
        },
        "retention": {
            "retain_all_outputs": True,
            "retain_failed_outputs": True,
            "required_lineage": ["canonical_score", "provider_build", "request", "assets", "provider/model/version", "seed_or_retry", "artifact", "evaluators", "human_labels", "cost", "latency"]
        },
        "analysis": {
            "binary_outcomes": "Per-arm success proportion with Wilson 95% confidence interval; paired analysis where pairing is valid.",
            "continuous_outcomes": "Median, distribution, and bootstrap 95% interval; report failed intervals, not only aggregate means.",
            "multiple_comparisons": "Holm correction within each family; predeclare the primary contrast.",
            "decision_rule": "Promote only when the isolated intervention improves the critical success distribution and does not increase another critical failure beyond its pre-registered margin."
        },
        "stop_conditions": [
            "Provider/interface/version changes during the campaign.",
            "Prompt rewrite or enhancement behavior cannot be disabled or captured consistently.",
            "Evaluator calibration falls below the pre-registered requirement.",
            "Artifact/request/asset lineage is incomplete.",
            "A safety, rights, or budget condition is violated."
        ]
    }


def arm(arm_id: str, label: str, isolated_control: str, canonical: str, projection: str) -> dict[str, str]:
    return {"arm_id": arm_id, "label": label, "isolated_control": isolated_control, "canonical_semantics": canonical, "provider_projection": projection}


EXPERIMENTS: dict[str, dict[str, Any]] = {}

EXPERIMENTS["experiments/01_occlusion_continuity.yaml"] = experiment(
    "experiment://failure/occlusion_continuity/1",
    "Occlusion continuity and water-splash hidden state",
    "Which carrier most reliably preserves one actor's identity, count, hidden dive path, and reappearance region through a splash?",
    "Complete opaque occlusion will produce the highest continuity failure; a visible bridge and then tracked control media will improve continuity more than equivalent additional prose.",
    {
        "scene": "two visually distinct actors on a continuous flat water plane; actor B dives; actor A's kick misses B and strikes only water; water column briefly occludes B",
        "duration_seconds": 8,
        "aspect_ratio": "16:9",
        "actor_count": 2,
        "camera": "locked or low-complexity tracking, no axis crossing",
        "canonical_event_graph": "identical across arms",
        "identity_and_costume": "locked",
        "negative_constraints": "identical across arms where representable"
    },
    [
        arm("OCC_A0", "No splash control", "no occlusion", "All events except splash; B remains fully visible", "baseline prompt/reference"),
        arm("OCC_A1", "Narrow partial splash", "partial occlusion", "Same event graph; B remains at least 30% visible", "prompt-only partial splash"),
        arm("OCC_A2", "Complete splash", "complete opaque occlusion", "Same hidden path and reappearance target", "prompt-only complete splash"),
        arm("OCC_A3", "Complete splash plus silhouette/trail", "visibility bridge", "Same hidden path; bridge bound to actor B", "reference/mask/silhouette/bubble trail where supported"),
        arm("OCC_A4", "Complete splash plus explicit hidden-path contract", "structured state and path", "Occlusion continuity contract included", "compressed provider-native prompt plus first/last/reference if available"),
        arm("OCC_A5", "Complete splash plus tracked control", "pose/point/depth path", "Same contract and control path", "provider-native control media or source-video workflow"),
        arm("OCC_A6", "Shot split and composited effect", "decomposition/post", "Same final canonical sequence", "clean choreography, separate splash plate, deterministic edit")
    ],
    ["metric_hidden_path_consistency", "metric_occlusion_reappearance_region_error", "metric_actor_count_consistency", "metric_identity_continuity", "metric_effect_origin_error", "metric_state_transition_accuracy"],
    [
        "actor count remains exactly two",
        "actor B remains the same identity and costume while invisible",
        "actor B follows the same hidden dive direction and reappears only in the declared region",
        "actor A's kick does not contact actor B",
        "water column begins only after and at the water impact point",
        "world layout and water topology do not reset"
    ]
)

EXPERIMENTS["experiments/02_format_semantic_equivalence.yaml"] = experiment(
    "experiment://failure/format_semantic_equivalence/1",
    "Prompt serialization semantic-equivalence ablation",
    "Does any serialization improve adherence when canonical meaning, provider prompt budget, and information content are matched?",
    "Single-authority concise projections will match or outperform duplicated multi-format prompts on adherence per character; no format will be universally superior across providers.",
    {
        "canonical_score": "one frozen content-addressed score",
        "scene": "two-actor ordered action with identity, spatial, causal, and terminal-state locks",
        "prompt_semantics": "equivalent fields and priorities",
        "reference_assets": "none",
        "duration_and_seed_policy": "identical within provider"
    },
    [
        arm("FMT_A0", "Natural language", "serialization only", "identical canonical controls", "ordered concise prose"),
        arm("FMT_A1", "Flat YAML", "serialization only", "identical canonical controls", "flat YAML string where provider accepts prompt text"),
        arm("FMT_A2", "XML", "serialization only", "identical canonical controls", "compact XML string"),
        arm("FMT_A3", "JSON", "serialization only", "identical canonical controls", "compact JSON string"),
        arm("FMT_A4", "XML plus JSON", "duplicate representation", "identical canonical controls duplicated", "hybrid prompt"),
        arm("FMT_A5", "XML plus JSON plus YAML", "triple duplication", "identical canonical controls triplicated", "hybrid prompt"),
        arm("FMT_A6", "Provider-native optimized prose", "adapter-specific compression", "identical canonical controls", "provider-native syntax and ordering without semantic additions")
    ],
    ["metric_prompt_semantic_equivalence", "metric_field_projection_coverage", "metric_hard_lock_retention", "metric_prompt_truncation_loss", "metric_instruction_coverage", "metric_primary_action_completion"],
    ["all hard canonical controls are represented", "no contradictory duplicate field is introduced", "event order and terminal state remain identical", "prompt length and provider rewrite behavior are captured"]
)

EXPERIMENTS["experiments/03_action_density.yaml"] = experiment(
    "experiment://failure/action_density/1",
    "Provider-specific action-density staircase",
    "At what dependency depth and action density does each provider/task begin to omit, merge, reverse, or invent events?",
    "Failure probability will rise with primary action count and dependency depth; provider-specific split thresholds will be more reliable than universal actions-per-second rules.",
    {
        "actors": 2,
        "identity_and_scene": "fixed",
        "camera": "locked",
        "effects": "minimal",
        "duration_seconds": "fixed within staircase, then repeated at longer duration",
        "event_vocabulary": "matched action difficulty"
    },
    [
        arm("DEN_A1", "One primary action", "action count=1", "setup-action-recovery", "provider-native projection"),
        arm("DEN_A2", "Three ordered actions", "action count=3", "three events, two dependencies", "provider-native projection"),
        arm("DEN_A3", "Five ordered actions", "action count=5", "five events, four dependencies", "provider-native projection"),
        arm("DEN_A4", "Full sequence", "maximum planned sequence", "all requested events and dependencies", "provider-native projection"),
        arm("DEN_A5", "Full sequence split", "shot decomposition", "same sequence across multiple clips", "per-shot builds plus edit")
    ],
    ["metric_action_graph_agreement", "metric_action_omission_rate", "metric_primary_action_completion", "metric_temporal_event_error", "metric_recovery_presence", "metric_hallucinated_action_rate"],
    ["no primary event is omitted or duplicated", "all hard dependencies hold", "reaction follows cause", "terminal state occurs without invented filler"]
)

EXPERIMENTS["experiments/04_spatial_control.yaml"] = experiment(
    "experiment://failure/spatial_control/1",
    "Spatial control and coordinate-frame ablation",
    "Which representation best preserves screen lanes, world direction, target regions, and axis through camera movement?",
    "Explicit coordinate frames and visual layout/trajectory controls will outperform unqualified left/right prose, especially after camera motion or cuts.",
    {
        "actors": 2,
        "event_graph": "fixed attack/dodge/target sequence",
        "identity": "distinct and fixed",
        "camera_variants": ["locked", "pan", "orbit", "reverse_angle"],
        "duration": "fixed"
    },
    [
        arm("SPA_A0", "Verbal left/right", "unqualified spatial prose", "same target positions", "natural-language left/right"),
        arm("SPA_A1", "Explicit screen lanes", "screen-relative state", "same target positions", "actor A lane left; actor B lane right"),
        arm("SPA_A2", "Normalized coordinates", "numeric screen regions", "same target positions", "provider-native prose or metadata where supported"),
        arm("SPA_A3", "Storyboard/keyframes", "visual layout", "same target positions", "reference storyboard"),
        arm("SPA_A4", "Trajectory/depth control", "time-varying spatial control", "same target path", "control media"),
        arm("SPA_A5", "Neutral re-establishing split", "decomposition", "same world state across camera reversal", "multi-shot edit")
    ],
    ["metric_screen_direction_consistency", "metric_depth_order_accuracy", "metric_trajectory_target_error", "metric_eyeline_consistency", "metric_camera_motion_agreement"],
    ["actor identities remain bound to world IDs", "screen-side changes occur only through declared crossings/camera transforms", "target region is correct", "axis/eyeline continuity is maintained or explicitly re-established"]
)

EXPERIMENTS["experiments/05_causality.yaml"] = experiment(
    "experiment://failure/causality/1",
    "Causal-event representation ablation",
    "Does an explicit causal graph reduce premature effects, wrong effect origin, and wrong-target reactions compared with compressed event phrases?",
    "Ordered cause-and-effect statements and then a canonical causal event graph will outperform compressed noun/verb bundles on causal agreement.",
    {
        "scene": "actor B dives; actor A's kick misses B and contacts water; water column follows; actor A recovers",
        "duration": 8,
        "camera": "locked",
        "identity": "fixed",
        "effect_style": "fixed"
    },
    [
        arm("CAU_A0", "Compressed phrase", "compressed semantics", "same requested concepts", "'axe kick, splash, B submerged'"),
        arm("CAU_A1", "Ordered prose", "explicit order", "same canonical events", "'B dives first; A misses B; kick hits only water; water column follows'"),
        arm("CAU_A2", "Canonical event graph", "explicit cause/dependency/reaction", "same canonical events and timing windows", "provider-native compressed projection plus verification"),
        arm("CAU_A3", "Storyboard causal beats", "visual cause/effect anchors", "same graph", "keyframes/storyboard"),
        arm("CAU_A4", "Separated effect plate", "postproduction consequence", "same graph and terminal state", "clean motion plus composited water column")
    ],
    ["metric_causal_edge_agreement", "metric_effect_origin_error", "metric_reaction_latency", "metric_target_assignment_accuracy", "metric_action_graph_agreement"],
    ["B's dive precedes the kick-water contact", "kick does not contact B", "splash starts after contact", "effect origin is the impact point", "reaction is assigned to the correct actor and event"]
)

EXPERIMENTS["experiments/06_repair_strategy.yaml"] = experiment(
    "experiment://failure/repair_strategy/1",
    "Full regeneration versus localized repair",
    "Which repair route restores the failed interval while minimizing collateral identity, state, geography, and timing changes?",
    "Localized interval repair or shot split will preserve accepted state better than full regeneration when stable boundary frames and an edit-capable workflow exist; postproduction will be best for deterministic effects.",
    {
        "input": "one retained failed artifact with one adjudicated failure interval",
        "canonical_score": "fixed",
        "acceptance": "fixed",
        "provider": "same provider for primary contrasts; substitution is a separate secondary experiment"
    },
    [
        arm("REP_A0", "Full regeneration", "regenerate entire artifact", "same score", "new full request"),
        arm("REP_A1", "Localized repair prompt", "text-only interval repair", "same score and preservation envelope", "provider edit/inpaint where available"),
        arm("REP_A2", "Localized repair with boundary frames", "first/last accepted frames", "same score", "edit workflow with in/out anchors"),
        arm("REP_A3", "Shot split and edit", "decomposition", "same final event graph", "regenerate failed subshot and assemble"),
        arm("REP_A4", "Postproduction effect replacement", "deterministic finishing", "same final event graph", "replace only effect/audio/camera impulse"),
        arm("REP_A5", "Provider substitution", "model/provider", "same sealed canonical target", "new provider build")
    ],
    ["metric_state_transition_accuracy", "metric_identity_continuity", "metric_environment_layout_consistency", "metric_action_graph_agreement", "metric_instruction_coverage"],
    ["original failed assertion is corrected", "all previously passing critical assertions remain passing", "seams are acceptable", "no undeclared state change occurs", "cost and latency are recorded"]
)

EXPERIMENTS["experiments/07_identity_state.yaml"] = experiment(
    "experiment://failure/identity_state/1",
    "Identity, role, object permanence, and state-ledger ablation",
    "How much do persistent IDs, separate references, explicit roles, and state ledgers reduce actor/prop swaps and state reset?",
    "Persistent IDs and explicit transitions will reduce role/object-state failures; separate visual references and control tracks will be required when appearance or possession is briefly unobserved.",
    {
        "scene": "two actors with one unique prop; one handoff; one cut; one brief occlusion",
        "duration": "provider-qualified",
        "camera": "fixed then one controlled cut",
        "events": "fixed"
    },
    [
        arm("IDS_A0", "Descriptive prose only", "no persistent ledger", "same desired events", "natural language"),
        arm("IDS_A1", "Stable IDs and roles", "identity/role contract", "same desired events", "provider-native labels"),
        arm("IDS_A2", "State ledger", "count/possession/state transitions", "same desired events", "compressed state-aware prompt"),
        arm("IDS_A3", "Separate actor/prop references", "visual identity anchors", "same desired events", "reference inputs"),
        arm("IDS_A4", "Tracked handoff/control", "time-varying possession", "same desired events", "pose/object control or source video"),
        arm("IDS_A5", "Handoff split", "decomposition", "same final event graph", "two shots with explicit state handoff")
    ],
    ["metric_identity_continuity", "metric_role_assignment_accuracy", "metric_object_count_consistency", "metric_state_transition_accuracy", "metric_contact_distance_error"],
    ["actor identities and roles remain stable", "object count remains one", "release precedes acquire", "object state persists across cut/occlusion", "no reflection becomes a physical duplicate"]
)

EXPERIMENTS["experiments/08_evaluator_calibration.yaml"] = experiment(
    "experiment://failure/evaluator_calibration/1",
    "Failure-aware evaluator calibration",
    "Which evaluator lanes can reliably observe each failure family, and where is human review mandatory?",
    "Atomic interval questions plus measured evidence will outperform a single global VLM score, but fast action, occlusion, stylization, and 3D contact will retain material human-review requirements.",
    {
        "dataset": "balanced retained CPCS clips with human-adjudicated positive and negative examples",
        "strata": ["fast action", "complete occlusion", "reflection", "actor crossing", "zoom versus translation", "anime smear", "partial visibility", "contact versus near-contact"],
        "evaluation": "blind and version-pinned"
    },
    [
        arm("EVA_A0", "Single global VLM score", "aggregate semantic evaluator", "same human labels", "one full-video prompt"),
        arm("EVA_A1", "Atomic interval questions", "scene-graph assertions", "same human labels", "time-bounded semantic questions"),
        arm("EVA_A2", "Measured trackers/pose/flow/audio", "numeric evidence", "same human labels", "tool-specific extraction"),
        arm("EVA_A3", "Multilane arbitration", "semantic + measured + human conflict policy", "same human labels", "CPCS compliance report"),
        arm("EVA_A4", "Human-only benchmark", "reference authority", "same rubric", "two raters plus adjudicator")
    ],
    ["metric_evaluator_calibration", "metric_human_agreement", "metric_false_positive_rate", "metric_false_negative_rate", "metric_cut_flash_classification"],
    ["report per-family confusion matrix", "preserve unobservable state", "no confidence averaging across opposing lanes", "human review required for critical unresolved conflicts"]
)

EXPERIMENT_AND_ABLATION_PLAN = """# Experiment and Ablation Plan

## Status

The experiment program is **designed but not run**. No authorized provider credentials, generation budget, local model weights, or human rating panel were supplied in this session. The package therefore reports no provider-specific success distributions and invents no universal capacity limits.

## Campaign sequence

1. **Evaluator calibration first.** Build a small human-adjudicated set containing the exact failure families. Do not allow an uncalibrated VLM to decide the later experiments.
2. **Low-cost provider/interface qualification.** Capture exact model IDs, endpoint schemas, prompt/rewrite settings, durations, resolutions, references, seeds, audio, outputs, and costs.
3. **Occlusion and state campaign.** Run the water-splash fixture and a non-fluid opaque-control fixture to distinguish hidden-state failure from material complexity.
4. **Serialization campaign.** Hold canonical meaning constant and compare formats, including duplicated hybrids.
5. **Capacity staircases.** Estimate provider/task-specific action/dependency/camera/effect thresholds.
6. **Control and decomposition.** Compare wording, state contracts, visual controls, source/video edit, shot splits, and postproduction.
7. **Repair campaign.** Use retained failed artifacts and isolate one repair intervention at a time.
8. **Immutable recording and reflection.** Admit only lineage-complete runs, then derive provider/model-conditioned mitigation rankings.

## Fixtures

""" + md_table(
    ["File", "Experiment", "Primary independent variable", "Primary outcome"],
    [[path, plan["title"], "; ".join(a["isolated_control"] for a in plan["arms"]), ", ".join(plan["metrics"][:3])] for path, plan in EXPERIMENTS.items()]
) + """

## Required repeated-seed design

- Initial screen: at least 20 completed outputs per arm/provider; 30+ for local/open workflows when affordable.
- Use paired seeds where supported and retain provider sample/retry identifiers everywhere.
- Randomize arm order; do not run one arm only during a different service/version window.
- Record provider/model/version/interface, region, request, prompt, prompt rewrite, seed, references, masks/control assets, duration, aspect ratio, resolution, FPS, cost, latency, safety/filter status, and output hash.
- Retain all outputs. The primary analysis may not choose the best candidate from a larger private pool.
- Human raters are blind to arm and provider where practical.
- Pre-register critical assertions; aggregate aesthetic quality is secondary.

## Outcomes

Binary critical success requires every critical assertion to pass. Continuous error metrics remain visible even when the binary verdict fails. Report:

```text
per-seed verdicts
success proportion and Wilson interval
continuous error distributions and bootstrap intervals
first-divergence frames/intervals
evaluator-human confusion and disagreement
cost and latency distributions
collateral failure rates
provider/model/version and date
```

## Promotion rule

A mitigation may become a derived recommendation only from evidence-complete isolated comparisons. A provider capability profile may change only from reviewed official documentation and live qualification. No experiment automatically promotes curated concepts, changes the canonical score, or grants production authority.
"""

EMPIRICAL_EXECUTION_STATUS = f"""# Empirical Execution Status

## Completed on {ACCESS_DATE}

- Repository inspection and ownership mapping at `{REPO_SHA}`.
- Source catalog with {len(SOURCES)} records.
- Claim/source matrix with {len(CLAIMS)} load-bearing claims.
- Failure taxonomy with {len(FAILURE_RECORDS)} schema-valid records across {len(FAMILY_META)} families.
- Evaluation catalog with {len(EVALUATION_METRICS)} metrics.
- Provider capability matrix with {len(PROVIDER_ROWS)} version/interface rows.
- Candidate JSON Schemas and examples.
- Eight repeated-seed experiment fixtures.
- Compiler, shot-decomposition, repair, integration, and minimum-representation recommendations.
- Local package validation, manifest, checksums, and ZIP assembly.

## Not run

- No commercial provider API/product generation.
- No local open-weight model generation.
- No image/video control asset execution.
- No human rating panel.
- No evaluator calibration corpus.
- No provider/model success distributions or action-density thresholds.
- No writes to the connected CPCS repository.
- No second-brain staging, curation, promotion, reflection, or production-qualification gate.

## Why this distinction matters

A literature package can establish failure families, control theory, candidate contracts, and experimental methodology. It cannot establish how often one current endpoint fails a specific CPCS scene. Any provider-specific reliability statement without raw repeated-seed evidence would be fabrication.

## Next executable evidence gate

Run `experiments/08_evaluator_calibration.yaml` and `experiments/01_occlusion_continuity.yaml` first. The first qualifies the judge; the second tests the exact water-splash hidden-state problem that motivated the research. Do not promote mitigation weights until both have lineage-complete human-calibrated results.
"""


OCCLUSION_REPORT = render_family_report(
    "Occlusion and Hidden-State Failures",
    ["A"],
    "Complete occlusion converts visible continuity into latent-state reconstruction. Prompt-only mitigation can remove lexical ambiguity, but precise identity, count, path, or reappearance obligations require a state contract plus visual control, decomposition, or postproduction.",
    "Use the candidate `Occlusion Continuity Contract`: persistent subject ID, pre-occlusion state, occluder, interval, visibility state, hidden path in a declared coordinate frame, expected reappearance region, identity/count locks, allowed/forbidden state changes, visibility bridge, and interval-level verification assertions. Visibility and existence must be separate fields."
)

IDENTITY_STATE_REPORT = render_family_report(
    "Identity, Object Permanence, and Role Failures",
    ["B", "C"],
    "Identity and persistence failures are binding failures across time: the system must keep stable entities, attributes, roles, counts, possession, and irreversible state deltas even when appearance, screen side, visibility, or shot context changes.",
    "Use a State Ledger and identity/role ledger under existing `entities`, `interactions`, and `continuity` owners. Bind every action to persistent initiator and target IDs; keep screen lanes and world identity distinct; represent object possession as release/acquire transitions; treat reflections and duplicates as typed entities, not appearance variants."
)

SPATIAL_REPORT = render_family_report(
    "Spatial and Screen-Geography Failures",
    ["D"],
    "Unqualified left/right and position descriptions collapse actor-relative, viewer-relative, camera-relative, and world-relative coordinates. A shot can satisfy a screen-space phrase while violating world geometry or the action axis.",
    "Use the Spatial State Transition Contract: coordinate frame, camera state, before/after world and screen relations, trajectories, screen/depth lanes, target regions, axis and eyeline invariants, and explicit transforms across pans, orbits, reverse angles, and cuts."
)

TEMPORAL_CAUSAL_REPORT = render_family_report(
    "Temporal, Action-Order, and Causality Failures",
    ["E", "F"],
    "A list of desired actions is not an executable event graph. As dependency depth rises, generators may merge, omit, repeat, reverse, or make events simultaneous; effects can then detach from causes or attach to the wrong actor or location.",
    "Represent each event with initiator, target, action, onset, apex, consequence, reaction delay, recovery, and secondary effects. Use hard dependency edges for `before`, `only_after`, `causes`, `prevents`, `while`, and `terminates`. Compile a topological order, preserve setup/recovery windows, and split when the provider/task-specific capacity staircase fails."
)

CONTACT_PHYSICS_REPORT = render_family_report(
    "Contact, Balance, Support, and Physics Failures",
    ["G", "H"],
    "Visual overlap is not physical contact, and cinematic plausibility is not a conservation or support solver. Prompt-only generation should not promise exact grip, collision-free geometry, support, momentum, landing, or reaction latency without appropriate control and measurement.",
    "Extend existing `interactions` and `motion` fields with contact type, target region, interval, minimum separation, allowed screen-space cheat, support state, base of support, takeoff/flight/landing, momentum/recoil/recovery, and verification lanes. Distinguish physical contact, staged near-contact, camera-cheated contact, effect-obscured contact, grasp/support, and surface contact."
)

FLUID_REPORT = render_family_report(
    "Fluid, Material, Cloth, Hair, Debris, and VFX Failures",
    ["I"],
    "Solid-fluid and other material transitions combine hidden state, effect generation, topology, causality, and persistence. A model can create a visually plausible splash while placing it before contact, centering it on the wrong subject, changing the water plane, or using the effect to reconstruct anatomy.",
    "Represent material class, source entity, impact point, onset/apex/decay, displacement region, topology invariants, allowed secondary particles, visibility effects, and terminal state. When exact effect origin/topology is hard, generate a clean interaction plate and composite the effect deterministically."
)

CAMERA_EDIT_ANIME_REPORT = render_family_report(
    "Camera, Edit, Graphic Discontinuity, and Anime-Recovery Failures",
    ["J", "K", "L"],
    "Camera motion, full-frame effects, cuts, smears, and stylized deformation are ambiguous unless CPCS distinguishes screen projection from world motion and graphic discontinuity from world-state change. Anime accents require explicit anatomy recovery rather than continuous realism.",
    "Separate camera translation, rotation, lens/zoom, actor world motion, actor screen motion, background motion, edit boundary, and impact impulse. Type every discontinuity as cut, flash, hold, smear, blur, wipe, occlusion, or world reset. For stylized deformation, encode affected region, onset, source/destination poses, maximum deformation, exposure duration, silhouette anchors, and required recovery frame."
)

PROMPT_ATTENTION_REPORT = render_family_report(
    "Prompt Format, Serialization, and Attention-Budget Failures",
    ["M", "N"],
    "Serialization helps CPCS validate and prioritize meaning; it does not automatically create provider-side structure. Duplicate representations, contradictions, prompt rewriting, and too many simultaneous requirements can dilute or erase hard controls, while under-specification invites filler.",
    "Keep canonical JSON authority, compile one provider-native representation, rank information by hard-control value, fail on unresolved conflict or hard-lock overflow, record prompt rewriting, and learn provider/task-specific capacity from repeated-seed staircases. End state, allowed variation, and forbidden new primary actions are mandatory when duration would otherwise be unassigned."
)

AUDIO_REPORT = render_family_report(
    "Audio-Video Synchronization Failures",
    ["O"],
    "Semantic audio relevance and temporal synchronization are separate requirements. A plausible impact sound can still occur before contact; a correct voice can still belong to the wrong speaker; music can be semantically appropriate but phase-misaligned.",
    "Bind every foreground audio event to a visual event ID or explicitly classify it as ambient/off-screen. Record speaker/voice identity, onset window, semantic cause, permitted offset, and recovery/tail. Separate generated-audio failure from visual failure and replace deterministic foreground audio in post when frame-level timing is critical."
)

REPOSITORY_AUDIT = f"""# Repository Audit and Ownership Map

## Inspected target

- Repository: `{REPO}`
- Revision: `{REPO_SHA}`
- Inspection date: `{ACCESS_DATE}`
- Branch observed: `main`

## Architectural findings

1. The repository defines one universal provider-neutral score as semantic authority.
2. Prompt serializations and provider requests are authoring/execution projections, not competing authority.
3. The compiler owns score resolution and non-submitting provider builds.
4. Verification owns artifact compliance, diagnosis, conflicts, and bounded repair planning.
5. The second brain separates curated truth, immutable occurrence evidence, and rebuildable derived inference.
6. Research may propose but cannot promote itself or directly change production authority.
7. The current architecture remains not production-qualified without live-provider, calibration, held-out, and other external gates.

## Files reviewed

""" + "\n".join(f"- `{p}`" for p in REPOSITORY_FILES_REVIEWED) + f"""

## Ownership matrix

""" + md_table(
    ["Failure family", "Current owner", "Coverage", "Required extension"],
    [[fid, OWNER_BY_FAMILY[fid], "partial", FAMILY_META[fid]["owner"]] for fid in FAMILY_META]
) + """

## Repository gaps

""" + "\n\n".join(
    f"### {g['gap_id']}\n\n**Finding:** {g['finding']}\n\n**Impact:** {g['impact']}\n\n**Action:** {g['action']}"
    for g in REPOSITORY_GAPS
) + """

## No-parallel-schema decision

The candidate contract schemas in `schemas/` are research review artifacts. If accepted, their fields should become typed nested definitions beneath existing universal-score owners and existing verification/evidence records. They must not become a new root score, alternate compiler, or independent failure ontology.

## Detailed overlap

`REPOSITORY_OVERLAP_MATRIX.csv` contains one row per failure record with current owner, coverage status, missing evidence, missing mitigation, missing test, and recommended owner.
"""

PROVIDER_CAPABILITY_NOTES = """# Provider Capability and Reliability Notes

## Interpretation

`PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv` separates **documented interface capability** from **empirical reliability**. A model can officially accept first/last frames, multiple references, source video, audio, seeds, or keyframes while still failing identity, hidden state, event order, contact, or causal material response.

## Current research decisions

- Bind every claim to exact provider, model/endpoint, access surface, region, version/date, workflow, and source.
- Treat third-party adapters as separate surfaces.
- Do not infer native-provider behavior from an aggregator UI.
- Do not infer reliability from a showcase, internal benchmark, or marketing statement.
- Treat provider-side prompt enhancement/rewrite as an experimental factor.
- Preserve seed semantics exactly as documented; never equate a seed with artifact identity or compliance.
- Require one live canary and replay evidence before an executable provider profile is treated as qualified.

## Matrix scope

The matrix includes current or documented interfaces for Veo, Runway, Seedance, Kling, MiniMax/Hailuo, Wan, LTX, Wan open models, HunyuanVideo, CogVideoX, Mochi, Luma Ray, and the current unavailable status of Sora 2. Fields marked unverified must be checked against the exact authorized interface before compilation.
"""

README_DOC = f"""# CPCS Failure-Aware Video Generation Research Package

**Version:** 1.0  
**Research date:** {ACCESS_DATE}  
**Repository inspected:** `{REPO}` at `{REPO_SHA}`  
**Status:** professional source/repository synthesis complete; provider render campaigns designed but not executed.

## Mission

This package answers the operational question:

> Given a requested video event, what conditions cause a generative video model to invent, merge, omit, reverse, deform, teleport, duplicate, obscure, or incorrectly resolve information, and what is the most reliable intervention at each failure boundary?

The central answer is that visually ambiguous intervals must be modeled as **persistent hidden state**, not merely discouraged with negative prompts. CPCS needs enough state, event, spatial, identity, causal, visibility, interaction, camera/edit, audio, and verification structure to remove avoidable ambiguity—and must escalate to references, control media, decomposition, postproduction, localized repair, or provider substitution when prompt text cannot carry or verify the hard requirement.

## Package facts

""" + md_table(
    ["Artifact", "Count", "Meaning"],
    [
        ["failure records", len(FAILURE_RECORDS), "16 families, each with trigger/cause/mitigation/verification/ownership"],
        ["evaluation metrics", len(EVALUATION_METRICS), "lane, method, blind spots, calibration, threshold policy"],
        ["provider rows", len(PROVIDER_ROWS), "official capability separated from reliability"],
        ["source records", len(SOURCES), "repository, official docs/repos, papers, benchmarks, tools"],
        ["claims", len(CLAIMS), "load-bearing conclusions with source and scope"],
        ["experiment fixtures", len(EXPERIMENTS), "paired repeated-seed plans, status designed_not_run"],
        ["candidate contract schemas", len(CONTRACT_SCHEMAS), "minimal nested extensions for owner review"],
    ]
) + """

## Start here

1. `EXECUTIVE_SYNTHESIS.md` — decisive findings and the water-splash analysis.
2. `MINIMUM_SUFFICIENT_REPRESENTATION.md` — the final design answer and escalation boundary.
3. `FAILURE_TAXONOMY.md` — all 96 failure records and IDs.
4. `FAILURE_CAUSE_MODEL.md` — target, provider, and evaluator failure model.
5. `MITIGATION_HIERARCHY.md` — L0 through L9 selection and exit checkpoints.
6. `CPCS_INTEGRATION_RECOMMENDATIONS.md` — exact owner-preserving implementation route.
7. `EXPERIMENT_AND_ABLATION_PLAN.md` — how to obtain provider-specific evidence.
8. `EMPIRICAL_EXECUTION_STATUS.md` — completed versus not run.

## Domain reports

- `OCCLUSION_AND_HIDDEN_STATE_FAILURES.md`
- `IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md`
- `SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md`
- `TEMPORAL_ACTION_CAUSALITY_FAILURES.md`
- `CONTACT_BALANCE_AND_PHYSICS_FAILURES.md`
- `FLUID_MATERIAL_AND_VFX_FAILURES.md`
- `CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md`
- `PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md`
- `AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md`
- `EVALUATOR_FAILURES.md`

## Machine-readable outputs

- `FAILURE_RECORDS.jsonl` and `FAILURE_RECORD.schema.json`
- `EVALUATION_METRICS.jsonl` and `EVALUATION_METRICS.schema.json`
- `PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv`
- `FAILURE_MITIGATION_MATRIX.csv`
- `SOURCE_CATALOG.csv`
- `CLAIM_SOURCE_MATRIX.csv`
- `REPOSITORY_OVERLAP_MATRIX.csv`
- `schemas/*.schema.json`
- `examples/*.json`
- `experiments/*.yaml`

## Evidence classes

The package distinguishes repository fact, official capability, peer-reviewed/preprint benchmark result, controlled research method, engineering inference, anecdote, and unverified claim. Source IDs such as `[M001]`, `[B004]`, and `[R006]` resolve in `SOURCE_CATALOG.csv`. Recent preprints and provider-authored claims are explicitly limited.

## Empirical limitation

No commercial or local provider renders were executed because no authorized credentials, generation budget, model weights/workflow, or human rating panel were supplied. The package does not report fabricated success rates. Every failure record carries `cpcs_render_campaign_status=not_run_no_authorized_provider_credentials_or_budget_in_session`.

## Validation

Run:

```bash
python3 scripts/validate_package.py .
```

The generated `VALIDATION_REPORT.json` records the validation result, and `SHA256SUMS.txt` provides file integrity hashes.
"""


# Preserve the high-resolution engineering catalogs defined earlier, then expose
# the A-P taxonomy/evaluator catalogs as the required package authorities.
ENGINEERING_FAILURE_RECORD_SCHEMA = FAILURE_RECORD_SCHEMA
ENGINEERING_EVALUATION_METRIC_SCHEMA = EVALUATION_METRICS_SCHEMA
ENGINEERING_FAILURE_RECORDS = FAILURES
ENGINEERING_EVALUATION_METRICS = METRICS

FAILURE_RECORD_SCHEMA = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
 '$id': 'cpcs://research/taxonomy-failure-record/1.0',
 'title': 'CPCS Failure Taxonomy Record',
 'type': 'object',
 'required': ['schema_version',
              'failure_id',
              'ordinal',
              'family_id',
              'family_name',
              'name',
              'definition',
              'scope',
              'trigger_conditions',
              'observed_symptoms',
              'suspected_causes',
              'evidence_class',
              'source_refs',
              'canonical_fields_affected',
              'prompt_risk_patterns',
              'mitigations',
              'verification_metrics',
              'regression_fixtures',
              'provider_specific_notes',
              'cpcs_ownership',
              'integration_classifications',
              'empirical_confidence',
              'cpcs_render_campaign_status',
              'unresolved_questions',
              'researched_at'],
 'properties': {'schema_version': {'const': 'cpcs.failure_record/1.0'},
                'failure_id': {'type': 'string', 'pattern': '^failure://[a-p]/[a-z0-9_]+/1$'},
                'ordinal': {'type': 'integer', 'minimum': 1},
                'family_id': {'type': 'string', 'pattern': '^[A-P]$'},
                'family_name': {'type': 'string', 'minLength': 3},
                'name': {'type': 'string', 'minLength': 3},
                'definition': {'type': 'string', 'minLength': 20},
                'scope': {'type': 'object',
                          'required': ['provider', 'model', 'version', 'workflows', 'content_types'],
                          'properties': {'provider': {'type': ['string', 'null']},
                                         'model': {'type': ['string', 'null']},
                                         'version': {'type': ['string', 'null']},
                                         'workflows': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                                         'content_types': {'type': 'array',
                                                           'minItems': 1,
                                                           'items': {'type': 'string'}}},
                          'additionalProperties': False},
                'trigger_conditions': {'type': 'array', 'minItems': 1, 'items': {'type': 'string', 'minLength': 5}},
                'observed_symptoms': {'type': 'array', 'minItems': 1, 'items': {'type': 'string', 'minLength': 5}},
                'suspected_causes': {'type': 'array',
                                     'minItems': 1,
                                     'items': {'type': 'object',
                                               'required': ['statement', 'status', 'confidence', 'falsification_test'],
                                               'properties': {'statement': {'type': 'string', 'minLength': 20},
                                                              'status': {'type': 'string'},
                                                              'confidence': {'type': 'string'},
                                                              'falsification_test': {'type': 'string',
                                                                                     'minLength': 20}},
                                               'additionalProperties': False}},
                'evidence_class': {'type': 'string'},
                'source_refs': {'type': 'array',
                                'minItems': 1,
                                'uniqueItems': True,
                                'items': {'type': 'string', 'pattern': '^[RMB][0-9]{3}$'}},
                'canonical_fields_affected': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                'prompt_risk_patterns': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                'mitigations': {'type': 'array',
                                'minItems': 2,
                                'items': {'type': 'object',
                                          'required': ['level',
                                                       'method',
                                                       'expected_benefit',
                                                       'token_or_character_cost',
                                                       'generation_cost_impact',
                                                       'risk_of_new_failure',
                                                       'provider_dependency',
                                                       'evidence_strength',
                                                       'verification_method',
                                                       'rollback',
                                                       'limitations'],
                                          'properties': {'level': {'type': 'string', 'pattern': '^L[0-9]$'},
                                                         'method': {'type': 'string', 'minLength': 10},
                                                         'expected_benefit': {'type': 'string'},
                                                         'token_or_character_cost': {'type': 'string'},
                                                         'generation_cost_impact': {'type': 'string'},
                                                         'risk_of_new_failure': {'type': 'string'},
                                                         'provider_dependency': {'type': 'string'},
                                                         'evidence_strength': {'type': 'string'},
                                                         'verification_method': {'type': 'string'},
                                                         'rollback': {'type': 'string'},
                                                         'limitations': {'type': 'array',
                                                                         'minItems': 1,
                                                                         'items': {'type': 'string'}}},
                                          'additionalProperties': False}},
                'verification_metrics': {'type': 'array',
                                         'minItems': 1,
                                         'uniqueItems': True,
                                         'items': {'type': 'string', 'pattern': '^metric_[a-z0-9_]+$'}},
                'regression_fixtures': {'type': 'array',
                                        'minItems': 1,
                                        'items': {'type': 'string', 'pattern': '^fixture://'}},
                'provider_specific_notes': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                'cpcs_ownership': {'type': 'object',
                                   'required': ['existing_owner',
                                                'research_owner',
                                                'implementation_owner',
                                                'new_parallel_schema_allowed'],
                                   'properties': {'existing_owner': {'type': 'string'},
                                                  'research_owner': {'type': 'string'},
                                                  'implementation_owner': {'type': 'string'},
                                                  'new_parallel_schema_allowed': {'const': False}},
                                   'additionalProperties': False},
                'integration_classifications': {'type': 'array',
                                                'minItems': 1,
                                                'uniqueItems': True,
                                                'items': {'enum': ['knowledge_only',
                                                                   'contract_affecting',
                                                                   'implementation_affecting',
                                                                   'provider_version_affecting',
                                                                   'verification_affecting',
                                                                   'policy_affecting',
                                                                   'unverified']}},
                'empirical_confidence': {'type': 'string'},
                'cpcs_render_campaign_status': {'type': 'string'},
                'unresolved_questions': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                'researched_at': {'type': 'string', 'format': 'date'}},
 'additionalProperties': False}

EVALUATION_METRICS_SCHEMA = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
 '$id': 'cpcs://research/evaluator-definition/1.0',
 'title': 'CPCS Evaluation Metric Definition',
 'type': 'object',
 'required': ['schema_version',
              'metric_id',
              'observable_dimension',
              'required_lane',
              'measurement_method',
              'evaluator_requirements',
              'known_blind_spots',
              'human_calibration_requirement',
              'failure_threshold_policy',
              'confidence_reporting'],
 'properties': {'schema_version': {'const': 'cpcs.evaluation_metric/1.0'},
                'metric_id': {'type': 'string', 'pattern': '^metric_[a-z0-9_]+$'},
                'observable_dimension': {'type': 'string', 'minLength': 3},
                'required_lane': {'type': 'string', 'minLength': 3},
                'measurement_method': {'type': 'string', 'minLength': 20},
                'evaluator_requirements': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                'known_blind_spots': {'type': 'array', 'minItems': 1, 'items': {'type': 'string'}},
                'human_calibration_requirement': {'type': 'string', 'minLength': 10},
                'failure_threshold_policy': {'type': 'string', 'minLength': 10},
                'confidence_reporting': {'type': 'string', 'minLength': 10}},
 'additionalProperties': False}


# Complete the candidate contract example set.
CONTRACT_EXAMPLES.update({
    "examples/spatial_state_transition_water_scene.json": {
        "schema_version": "cpcs.spatial_state_transition/1.0-candidate",
        "transition_id": "spatial_actor_b_dive_right_lane",
        "coordinate_frame": "screen_normalized",
        "camera_state_ref": "camera://shot_01/locked_axis",
        "before": {
            "actor_A": {"screen_lane": "left", "depth_lane": "mid", "facing": "right"},
            "actor_B": {"screen_lane": "right", "depth_lane": "mid", "facing": "left"}
        },
        "motion": {
            "entity_id": "actor_B",
            "trajectory": [[0.72, 0.54], [0.73, 0.62], [0.74, 0.74]],
            "screen_lane_before": "right",
            "screen_lane_after": "right",
            "depth_lane_before": "mid",
            "depth_lane_after": "subsurface_mid"
        },
        "after": {
            "actor_A": {"screen_lane": "left", "depth_lane": "mid"},
            "actor_B": {"screen_lane": "right", "depth_lane": "subsurface_mid"}
        },
        "invariants": ["actor_A remains left of actor_B", "no axis crossing", "no world-layout reset"]
    },
    "examples/evaluator_provenance_identity_check.json": {
        "schema_version": "cpcs.evaluator_provenance/1.0-candidate",
        "evaluator_id": "evaluator://identity_continuity/human_calibrated_v1",
        "version": "example-only-not-qualified",
        "configuration_hash": "sha256:" + "0" * 64,
        "artifact_hash": "sha256:" + "1" * 64,
        "observable_dimension": "actor_B identity continuity across the complete water-splash occlusion interval",
        "lane": "human_review",
        "confidence": None,
        "known_blind_spots": ["fast smear frames", "complete opaque occlusion", "similar costume colors"],
        "human_calibration_status": "human_only"
    }
})

ENGINEERING_FAILURE_MITIGATION_ROWS: list[dict[str, Any]] = []
for record in ENGINEERING_FAILURE_RECORDS:
    for order, mitigation in enumerate(record["mitigations"], 1):
        ENGINEERING_FAILURE_MITIGATION_ROWS.append({
            "failure_code": record["failure_code"],
            "failure_id": record["failure_id"],
            "category": record["category"],
            "failure_name": record["name"],
            "severity": record["severity"],
            "controllability": record["controllability"],
            "mitigation_order": order,
            "mitigation_level": mitigation["level"],
            "mitigation_level_name": mitigation["level_name"],
            "method": mitigation["method"],
            "expected_benefit": mitigation["expected_benefit"],
            "token_or_character_cost": mitigation["token_or_character_cost"],
            "generation_cost_impact": mitigation["generation_cost_impact"],
            "risk_of_new_failure": mitigation["risk_of_new_failure"],
            "provider_dependency": mitigation["provider_dependency"],
            "evidence_strength": mitigation["evidence_strength"],
            "verification_method": mitigation["verification_method"],
            "verification_metric_ids": mitigation["verification_metric_ids"],
            "rollback": mitigation["rollback"],
            "limitations": mitigation["limitations"],
            "source_refs": record["source_refs"],
            "research_status": record["research_status"],
        })

ENGINEERING_CPCS_IMPACT_ROWS: list[dict[str, Any]] = []
for record in ENGINEERING_FAILURE_RECORDS:
    base = {
        "failure_code": record["failure_code"],
        "failure_id": record["failure_id"],
        "failure_name": record["name"],
        "category": record["category"],
        "finding_classification": record["finding_classification"],
        "controllability": record["controllability"],
    }
    for surface, value in record["cpcs_impact"].items():
        ENGINEERING_CPCS_IMPACT_ROWS.append({**base, "cpcs_surface": surface, "required_change_or_effect": value})

CANONICAL_CONTRACT_EXAMPLES_DOC = """# Canonical Contract Examples

## Status

These contracts are **candidate nested extensions** for owner review. They do not create a new CPCS root schema or production authority. Each example validates against a Draft 2020-12 JSON Schema in `schemas/`.

## Water-splash continuity chain

The example set encodes one two-actor scene in five linked views:

1. `state_ledger_two_actor_water_scene.json` establishes existence, count, identity/costume, side, water topology, and legal visibility transitions.
2. `causal_event_graph_water_strike.json` establishes that B dives first, A misses B, A strikes only water, and the water column occurs only after and at the impact point.
3. `spatial_state_transition_water_scene.json` keeps B in the right lane while moving below the water plane and preserves the action axis.
4. `occlusion_continuity_water_splash.json` carries B through the opaque interval with a hidden dive path, reappearance region, count/identity locks, and a bubble-trail bridge.
5. `evaluator_provenance_identity_check.json` shows how every verification verdict must bind evaluator version/configuration, artifact hash, observable dimension, confidence, blind spots, and human-calibration state.

## Governing distinction

A canonical contract defines **what must be true**. A provider projection carries only what the selected interface can accept. A verification plan checks what remains observable. A loss report records what could not be carried. The contract is not proof that the provider can satisfy the request.
"""

RESEARCH_EXECUTION_LOG = f"""# Research Execution Log

## Scope executed

- Parsed the uploaded 1,216-line research brief and preserved its A-P failure-family framing.
- Inspected `{REPO}` at `{REPO_SHA}` for canonical ownership, compiler, provider-capability, verification, compliance, and second-brain boundaries.
- Cataloged {len(SOURCES)} repository, official provider, model-repository, paper, benchmark, and evaluator/tool sources.
- Produced {len(FAILURE_RECORDS)} A-P taxonomy records and {len(ENGINEERING_FAILURE_RECORDS)} high-resolution engineering records.
- Produced {len(EVALUATION_METRICS)} evaluator definitions and {len(ENGINEERING_EVALUATION_METRICS)} high-resolution implementation metrics.
- Produced {len(PROVIDER_ROWS)} provider/interface rows and {len(CLAIMS)} source-linked claims.
- Designed {len(EXPERIMENTS)} repeated-seed campaigns with blocked/not-run status.
- Generated candidate contracts, compiler/decomposition/repair rules, CPCS integration recommendations, validators, manifest, checksums, and archive.

## Not executed

No authenticated commercial generation, local checkpoint inference, human rater panel, or evaluator calibration run was available. Consequently, this package does not report provider-specific success rates, universal action-density limits, or model rankings from CPCS renders.

## Evidence checkpoint

The package is complete as a source-grounded research and experiment-design artifact. It is **not** a live-provider qualification report. Promotion into CPCS requires the existing review and evidence gates.
"""

FINAL_RESEARCH_ANSWER = MINIMUM_SUFFICIENT_REPRESENTATION + """

## Decision summary

Prompt-only generation should be abandoned as soon as a production-critical requirement depends on information that is invisible, geometric, time-varying, tightly synchronized, or not carried by the selected provider interface. References anchor appearance and boundaries; control media carries paths and geometry; shot decomposition converts hidden transitions into observable handoff states; postproduction guarantees deterministic effects and synchronization; unsupported status is correct when no qualified workflow clears the gate.
"""

# ---------------------------------------------------------------------------
# Package assembly, validation, and archive creation
# ---------------------------------------------------------------------------

REQUIRED_OUTPUTS = [
    "README.md",
    "FAILURE_TAXONOMY.md",
    "FAILURE_CAUSE_MODEL.md",
    "OCCLUSION_AND_HIDDEN_STATE_FAILURES.md",
    "IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md",
    "SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md",
    "TEMPORAL_ACTION_CAUSALITY_FAILURES.md",
    "CONTACT_BALANCE_AND_PHYSICS_FAILURES.md",
    "FLUID_MATERIAL_AND_VFX_FAILURES.md",
    "CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md",
    "PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md",
    "AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md",
    "MITIGATION_HIERARCHY.md",
    "PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv",
    "FAILURE_MITIGATION_MATRIX.csv",
    "SOURCE_CATALOG.csv",
    "CLAIM_SOURCE_MATRIX.csv",
    "FAILURE_RECORDS.jsonl",
    "FAILURE_RECORD.schema.json",
    "EVALUATION_METRICS.schema.json",
    "EVALUATION_METRICS.jsonl",
    "MINIMUM_SUFFICIENT_REPRESENTATION.md",
    "FINAL_RESEARCH_ANSWER.md",
    "EMPIRICAL_EXECUTION_STATUS.md",
    "REPOSITORY_AUDIT.md",
    "EXPERIMENT_AND_ABLATION_PLAN.md",
    "PROMPT_COMPILER_RULES.md",
    "SHOT_DECOMPOSITION_RULES.md",
    "LOCALIZED_REPAIR_PLAYBOOK.md",
    "CPCS_INTEGRATION_RECOMMENDATIONS.md",
    "UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL.md",
]

GROUP_DOCS = {
    "OCCLUSION_AND_HIDDEN_STATE_FAILURES.md": OCCLUSION_REPORT,
    "IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md": IDENTITY_STATE_REPORT,
    "SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md": SPATIAL_REPORT,
    "TEMPORAL_ACTION_CAUSALITY_FAILURES.md": TEMPORAL_CAUSAL_REPORT,
    "CONTACT_BALANCE_AND_PHYSICS_FAILURES.md": CONTACT_PHYSICS_REPORT,
    "FLUID_MATERIAL_AND_VFX_FAILURES.md": FLUID_REPORT,
    "CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md": CAMERA_EDIT_ANIME_REPORT,
    "PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md": PROMPT_ATTENTION_REPORT,
    "AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md": AUDIO_REPORT,
    "EVALUATOR_FAILURES.md": EVALUATOR_FAILURES_DOC,
}

def normalize_source_refs(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    text = str(value).replace(",", " ").replace(";", " ")
    return [part.strip() for part in text.split() if part.strip()]


CLAIM_SOURCE_ROWS: list[dict[str, str]] = []
for claim in CLAIMS:
    refs = normalize_source_refs(claim.get("source_refs", claim.get("source_ids")))
    for sid in refs:
        src = SOURCE_BY_ID[sid]
        CLAIM_SOURCE_ROWS.append({
            "claim_id": claim["claim_id"],
            "claim": claim["claim"],
            "claim_status": claim.get("status", ""),
            "claim_scope": claim.get("claim_type", claim.get("scope", "")),
            "claim_confidence": claim.get("confidence", ""),
            "cpcs_implication": claim.get("cpcs_implication", ""),
            "source_id": sid,
            "source_title": src["title"],
            "source_evidence_class": src["evidence_class"],
            "source_url": src["url"],
            "source_limitations": src["limitations"],
        })

VALIDATOR_SCRIPT = r'''#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_jsonl(path: Path):
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path}:{lineno}: {exc}") from exc
    return rows


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    checks = []

    required = [
        "README.md", "FAILURE_TAXONOMY.md", "FAILURE_CAUSE_MODEL.md",
        "OCCLUSION_AND_HIDDEN_STATE_FAILURES.md",
        "IDENTITY_OBJECT_PERMANENCE_AND_ROLE_FAILURES.md",
        "SPATIAL_AND_SCREEN_GEOGRAPHY_FAILURES.md",
        "TEMPORAL_ACTION_CAUSALITY_FAILURES.md",
        "CONTACT_BALANCE_AND_PHYSICS_FAILURES.md",
        "FLUID_MATERIAL_AND_VFX_FAILURES.md",
        "CAMERA_EDIT_AND_ANIME_DISCONTINUITY_FAILURES.md",
        "PROMPT_FORMAT_AND_ATTENTION_BUDGET_FAILURES.md",
        "AUDIO_VIDEO_SYNCHRONIZATION_FAILURES.md", "MITIGATION_HIERARCHY.md",
        "PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv", "FAILURE_MITIGATION_MATRIX.csv",
        "SOURCE_CATALOG.csv", "CLAIM_SOURCE_MATRIX.csv", "FAILURE_RECORDS.jsonl",
        "FAILURE_RECORD.schema.json", "EVALUATION_METRICS.schema.json", "EVALUATION_METRICS.jsonl",
        "MINIMUM_SUFFICIENT_REPRESENTATION.md", "FINAL_RESEARCH_ANSWER.md",
        "EMPIRICAL_EXECUTION_STATUS.md", "REPOSITORY_AUDIT.md",
        "EXPERIMENT_AND_ABLATION_PLAN.md", "PROMPT_COMPILER_RULES.md",
        "SHOT_DECOMPOSITION_RULES.md", "LOCALIZED_REPAIR_PLAYBOOK.md",
        "CPCS_INTEGRATION_RECOMMENDATIONS.md", "UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL.md"
    ]
    missing = [p for p in required if not (root / p).is_file()]
    if missing:
        raise RuntimeError(f"Missing required outputs: {missing}")
    checks.append({"check": "required_outputs", "status": "passed", "count": len(required)})

    source_rows = list(csv.DictReader((root / "SOURCE_CATALOG.csv").open(encoding="utf-8")))
    source_ids = {r["source_id"] for r in source_rows}
    if len(source_ids) != len(source_rows):
        raise RuntimeError("Duplicate source IDs")

    failure_schema = json.loads((root / "FAILURE_RECORD.schema.json").read_text(encoding="utf-8"))
    metric_schema = json.loads((root / "EVALUATION_METRICS.schema.json").read_text(encoding="utf-8"))
    experiment_schema = json.loads((root / "schemas/EXPERIMENT_PLAN.schema.json").read_text(encoding="utf-8"))
    for schema in [failure_schema, metric_schema, experiment_schema]:
        Draft202012Validator.check_schema(schema)

    failures = load_jsonl(root / "FAILURE_RECORDS.jsonl")
    fv = Draft202012Validator(failure_schema)
    failure_ids = set()
    ordinals = set()
    for row in failures:
        errors = sorted(fv.iter_errors(row), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Failure record invalid {row.get('failure_id')}: {errors[0].message}")
        if row["failure_id"] in failure_ids:
            raise RuntimeError(f"Duplicate failure ID {row['failure_id']}")
        if row["ordinal"] in ordinals:
            raise RuntimeError(f"Duplicate failure ordinal {row['ordinal']}")
        failure_ids.add(row["failure_id"])
        ordinals.add(row["ordinal"])
        missing_refs = sorted(set(row["source_refs"]) - source_ids)
        if missing_refs:
            raise RuntimeError(f"Unknown source refs in {row['failure_id']}: {missing_refs}")
    checks.append({"check": "failure_records", "status": "passed", "count": len(failures)})

    metrics = load_jsonl(root / "EVALUATION_METRICS.jsonl")
    mv = Draft202012Validator(metric_schema)
    metric_ids = set()
    for row in metrics:
        errors = sorted(mv.iter_errors(row), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Metric invalid {row.get('metric_id')}: {errors[0].message}")
        if row["metric_id"] in metric_ids:
            raise RuntimeError(f"Duplicate metric ID {row['metric_id']}")
        metric_ids.add(row["metric_id"])
    referenced_metrics = {m for f in failures for m in f["verification_metrics"]}
    if referenced_metrics - metric_ids:
        raise RuntimeError(f"Missing metric definitions: {sorted(referenced_metrics - metric_ids)}")
    checks.append({"check": "evaluation_metrics", "status": "passed", "count": len(metrics)})

    ev = Draft202012Validator(experiment_schema)
    experiment_count = 0
    for path in sorted((root / "experiments").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(ev.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Experiment invalid {path.name}: {errors[0].message}")
        unknown_metrics = set(data["metrics"]) - metric_ids
        if unknown_metrics:
            raise RuntimeError(f"Experiment {path.name} references unknown metrics: {sorted(unknown_metrics)}")
        experiment_count += 1
    checks.append({"check": "experiment_plans", "status": "passed", "count": experiment_count})

    contract_pairs = [
        ("schemas/OCCLUSION_CONTINUITY_CONTRACT.schema.json", "examples/occlusion_continuity_water_splash.json"),
        ("schemas/STATE_LEDGER.schema.json", "examples/state_ledger_two_actor_water_scene.json"),
        ("schemas/CAUSAL_EVENT_GRAPH.schema.json", "examples/causal_event_graph_water_strike.json"),
        ("schemas/SPATIAL_STATE_TRANSITION.schema.json", "examples/spatial_state_transition_water_scene.json"),
        ("schemas/EVALUATOR_PROVENANCE.schema.json", "examples/evaluator_provenance_identity_check.json"),
    ]
    for schema_rel, example_rel in contract_pairs:
        schema = json.loads((root / schema_rel).read_text(encoding="utf-8"))
        example = json.loads((root / example_rel).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema).iter_errors(example), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Example invalid {example_rel}: {errors[0].message}")
    checks.append({"check": "contract_examples", "status": "passed", "count": len(contract_pairs)})

    provider_rows = list(csv.DictReader((root / "PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv").open(encoding="utf-8")))
    for row in provider_rows:
        refs = set(row["official_source_ids"].split())
        if refs - source_ids:
            raise RuntimeError(f"Provider row {row['model_or_endpoint_id']} has unknown sources {sorted(refs - source_ids)}")
    claim_rows = list(csv.DictReader((root / "CLAIM_SOURCE_MATRIX.csv").open(encoding="utf-8")))
    for row in claim_rows:
        if row["source_id"] not in source_ids:
            raise RuntimeError(f"Claim row {row['claim_id']} has unknown source {row['source_id']}")
    checks.append({"check": "source_traceability", "status": "passed", "sources": len(source_rows), "providers": len(provider_rows), "claim_source_edges": len(claim_rows)})

    manifest_path = root / "MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for item in manifest["files"]:
            path = root / item["path"]
            if not path.is_file():
                raise RuntimeError(f"Manifest file missing: {item['path']}")
            if path.stat().st_size != item["bytes"]:
                raise RuntimeError(f"Manifest byte size mismatch: {item['path']}")
            if sha256(path) != item["sha256"]:
                raise RuntimeError(f"Manifest hash mismatch: {item['path']}")
        checks.append({"check": "manifest", "status": "passed", "count": len(manifest["files"])})

    sums_path = root / "SHA256SUMS.txt"
    if sums_path.exists():
        count = 0
        for line in sums_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, rel = line.split("  ", 1)
            path = root / rel
            if sha256(path) != digest:
                raise RuntimeError(f"SHA256SUMS mismatch: {rel}")
            count += 1
        checks.append({"check": "sha256sums", "status": "passed", "count": count})

    report = {"status": "passed", "root": str(root), "checks": checks}
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def write_jsonl(rel: str, rows: list[dict[str, Any]]) -> None:
    write_text(rel, "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows))


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def validate_package_in_process() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    schema_objects = {
        "FAILURE_RECORD.schema.json": FAILURE_RECORD_SCHEMA,
        "EVALUATION_METRICS.schema.json": EVALUATION_METRICS_SCHEMA,
        "schemas/EXPERIMENT_PLAN.schema.json": EXPERIMENT_SCHEMA,
        "schemas/ENGINEERING_FAILURE_RECORD.schema.json": ENGINEERING_FAILURE_RECORD_SCHEMA,
        "schemas/ENGINEERING_EVALUATION_METRIC.schema.json": ENGINEERING_EVALUATION_METRIC_SCHEMA,
        **CONTRACT_SCHEMAS,
    }
    for name, schema in schema_objects.items():
        Draft202012Validator.check_schema(schema)
    checks.append({"check": "schema_meta_validation", "status": "passed", "count": len(schema_objects)})

    fv = Draft202012Validator(FAILURE_RECORD_SCHEMA)
    for record in FAILURE_RECORDS:
        errors = sorted(fv.iter_errors(record), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Failure schema validation failed {record['failure_id']}: {errors[0].message}")
    checks.append({"check": "failure_records", "status": "passed", "count": len(FAILURE_RECORDS)})

    mv = Draft202012Validator(EVALUATION_METRICS_SCHEMA)
    for metric in EVALUATION_METRICS:
        errors = sorted(mv.iter_errors(metric), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Metric schema validation failed {metric['metric_id']}: {errors[0].message}")
    checks.append({"check": "evaluation_metrics", "status": "passed", "count": len(EVALUATION_METRICS)})

    efv = Draft202012Validator(ENGINEERING_FAILURE_RECORD_SCHEMA)
    for record in ENGINEERING_FAILURE_RECORDS:
        errors = sorted(efv.iter_errors(record), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Engineering failure schema validation failed {record['failure_id']}: {errors[0].message}")
    emv = Draft202012Validator(ENGINEERING_EVALUATION_METRIC_SCHEMA)
    for metric in ENGINEERING_EVALUATION_METRICS:
        errors = sorted(emv.iter_errors(metric), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Engineering metric schema validation failed {metric['metric_id']}: {errors[0].message}")
    checks.append({"check": "engineering_catalogs", "status": "passed", "failure_records": len(ENGINEERING_FAILURE_RECORDS), "metrics": len(ENGINEERING_EVALUATION_METRICS)})

    ev = Draft202012Validator(EXPERIMENT_SCHEMA)
    metric_ids = {m["metric_id"] for m in EVALUATION_METRICS}
    for path, plan in EXPERIMENTS.items():
        errors = sorted(ev.iter_errors(plan), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Experiment schema validation failed {path}: {errors[0].message}")
        unknown = set(plan["metrics"]) - metric_ids
        if unknown:
            raise RuntimeError(f"Experiment {path} references unknown metrics {sorted(unknown)}")
    checks.append({"check": "experiments", "status": "passed", "count": len(EXPERIMENTS)})

    example_schema_map = {
        "examples/occlusion_continuity_water_splash.json": OCCLUSION_CONTINUITY_CONTRACT_SCHEMA,
        "examples/state_ledger_two_actor_water_scene.json": STATE_LEDGER_SCHEMA,
        "examples/causal_event_graph_water_strike.json": CAUSAL_EVENT_GRAPH_SCHEMA,
        "examples/spatial_state_transition_water_scene.json": SPATIAL_STATE_TRANSITION_SCHEMA,
        "examples/evaluator_provenance_identity_check.json": EVALUATOR_PROVENANCE_SCHEMA,
    }
    for name, schema in example_schema_map.items():
        errors = sorted(Draft202012Validator(schema).iter_errors(CONTRACT_EXAMPLES[name]), key=lambda e: list(e.path))
        if errors:
            raise RuntimeError(f"Contract example validation failed {name}: {errors[0].message}")
    checks.append({"check": "contract_examples", "status": "passed", "count": len(example_schema_map)})

    source_ids = {s["source_id"] for s in SOURCES}
    if len(source_ids) != len(SOURCES):
        raise RuntimeError("Duplicate source IDs")
    for record in FAILURE_RECORDS:
        missing = set(record["source_refs"]) - source_ids
        if missing:
            raise RuntimeError(f"Unknown source refs {sorted(missing)} in {record['failure_id']}")
    for claim in CLAIMS:
        missing = set(normalize_source_refs(claim.get("source_refs", claim.get("source_ids")))) - source_ids
        if missing:
            raise RuntimeError(f"Unknown claim source refs {sorted(missing)} in {claim['claim_id']}")
    for row in PROVIDER_ROWS:
        missing = set(normalize_source_refs(row["official_source_ids"])) - source_ids
        if missing:
            raise RuntimeError(f"Unknown provider source refs {sorted(missing)} in {row['model_or_endpoint_id']}")
    checks.append({"check": "source_traceability", "status": "passed", "sources": len(SOURCES), "claims": len(CLAIMS), "providers": len(PROVIDER_ROWS)})

    failure_ids = [r["failure_id"] for r in FAILURE_RECORDS]
    if len(failure_ids) != len(set(failure_ids)):
        raise RuntimeError("Duplicate failure IDs")
    if sorted(r["ordinal"] for r in FAILURE_RECORDS) != list(range(1, len(FAILURE_RECORDS) + 1)):
        raise RuntimeError("Failure ordinals are not contiguous")
    checks.append({"check": "identity_and_ordinal_integrity", "status": "passed"})

    missing_required = [p for p in REQUIRED_OUTPUTS if not (ROOT / p).is_file()]
    if missing_required:
        raise RuntimeError(f"Missing required output files: {missing_required}")
    checks.append({"check": "required_outputs", "status": "passed", "count": len(REQUIRED_OUTPUTS)})

    return {
        "schema_version": "cpcs.research_package_validation/1.0",
        "status": "passed",
        "validated_at": ACCESS_DATE,
        "repository": REPO,
        "repository_revision": REPO_SHA,
        "render_campaign_status": "not_run",
        "checks": checks,
        "counts": {
            "failure_records": len(FAILURE_RECORDS),
            "families": len(FAMILY_META),
            "metrics": len(EVALUATION_METRICS),
            "providers": len(PROVIDER_ROWS),
            "sources": len(SOURCES),
            "claims": len(CLAIMS),
            "experiments": len(EXPERIMENTS),
            "engineering_failure_records": len(ENGINEERING_FAILURE_RECORDS),
            "engineering_metrics": len(ENGINEERING_EVALUATION_METRICS),
            "contract_examples": len(CONTRACT_EXAMPLES),
        },
        "limitations": [
            "No authorized provider renders or human rating panel were executed.",
            "Provider reliability remains unmeasured by CPCS.",
            "Recent preprints and official provider claims retain the limitations recorded in SOURCE_CATALOG.csv."
        ]
    }


def assemble_package() -> None:
    write_text("README.md", README_DOC)
    write_text("EXECUTIVE_SYNTHESIS.md", EXECUTIVE_SYNTHESIS)
    write_text("RESEARCH_METHOD.md", RESEARCH_METHOD)
    write_text("REPOSITORY_AUDIT.md", REPOSITORY_AUDIT)
    write_text("FAILURE_TAXONOMY.md", FAILURE_TAXONOMY)
    write_text("FAILURE_CAUSE_MODEL.md", FAILURE_CAUSE_MODEL)
    for rel, text in GROUP_DOCS.items():
        write_text(rel, text)
    write_text("MITIGATION_HIERARCHY.md", MITIGATION_HIERARCHY_DOC)
    write_text("PROVIDER_CAPABILITY_NOTES.md", PROVIDER_CAPABILITY_NOTES)
    write_text("EXPERIMENT_AND_ABLATION_PLAN.md", EXPERIMENT_AND_ABLATION_PLAN)
    write_text("PROMPT_COMPILER_RULES.md", PROMPT_COMPILER_RULES)
    write_text("SHOT_DECOMPOSITION_RULES.md", SHOT_DECOMPOSITION_RULES)
    write_text("LOCALIZED_REPAIR_PLAYBOOK.md", LOCALIZED_REPAIR_PLAYBOOK)
    write_text("CPCS_INTEGRATION_RECOMMENDATIONS.md", CPCS_INTEGRATION_RECOMMENDATIONS)
    write_text("MINIMUM_SUFFICIENT_REPRESENTATION.md", MINIMUM_SUFFICIENT_REPRESENTATION)
    write_text("UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL.md", UNVERIFIED_CONTRADICTORY_AND_ANECDOTAL)
    write_text("EMPIRICAL_EXECUTION_STATUS.md", EMPIRICAL_EXECUTION_STATUS)
    write_text("FINAL_RESEARCH_ANSWER.md", FINAL_RESEARCH_ANSWER)
    write_text("CANONICAL_CONTRACT_EXAMPLES.md", CANONICAL_CONTRACT_EXAMPLES_DOC)
    write_text("RESEARCH_EXECUTION_LOG.md", RESEARCH_EXECUTION_LOG)

    if SRC_BRIEF.exists():
        shutil.copy2(SRC_BRIEF, ROOT / "RESEARCH_BRIEF.md")
    else:
        write_text("RESEARCH_BRIEF.md", "# Research Brief\n\nOriginal uploaded brief was not available at package-build time.")

    write_jsonl("FAILURE_RECORDS.jsonl", FAILURE_RECORDS)
    write_json("FAILURE_RECORD.schema.json", FAILURE_RECORD_SCHEMA)
    write_jsonl("EVALUATION_METRICS.jsonl", EVALUATION_METRICS)
    write_json("EVALUATION_METRICS.schema.json", EVALUATION_METRICS_SCHEMA)
    write_jsonl("ENGINEERING_FAILURE_RECORDS.jsonl", ENGINEERING_FAILURE_RECORDS)
    write_json("schemas/ENGINEERING_FAILURE_RECORD.schema.json", ENGINEERING_FAILURE_RECORD_SCHEMA)
    write_jsonl("ENGINEERING_EVALUATION_METRICS.jsonl", ENGINEERING_EVALUATION_METRICS)
    write_json("schemas/ENGINEERING_EVALUATION_METRIC.schema.json", ENGINEERING_EVALUATION_METRIC_SCHEMA)
    write_jsonl("MECHANISMS.jsonl", MECHANISMS)
    write_jsonl("CLAIMS.jsonl", CLAIMS)
    write_jsonl("PROVIDER_CAPABILITY_RECORDS.jsonl", PROVIDER_ROWS)
    for rel, schema in CONTRACT_SCHEMAS.items():
        write_json(rel, schema)
    write_json("schemas/EXPERIMENT_PLAN.schema.json", EXPERIMENT_SCHEMA)
    for rel, example in CONTRACT_EXAMPLES.items():
        write_json(rel, example)
    for rel, plan in EXPERIMENTS.items():
        write_text(rel, yaml.safe_dump(plan, sort_keys=False, allow_unicode=True, width=120))

    write_csv("SOURCE_CATALOG.csv", SOURCES)
    write_csv("CLAIM_SOURCE_MATRIX.csv", CLAIM_SOURCE_ROWS)
    write_csv("PROVIDER_CAPABILITY_AND_FAILURE_MATRIX.csv", PROVIDER_ROWS)
    write_csv("FAILURE_MITIGATION_MATRIX.csv", FAILURE_MITIGATION_ROWS)
    write_csv("ENGINEERING_FAILURE_MITIGATION_MATRIX.csv", ENGINEERING_FAILURE_MITIGATION_ROWS)
    write_csv("ENGINEERING_CPCS_IMPACT_MATRIX.csv", ENGINEERING_CPCS_IMPACT_ROWS)
    write_csv("REPOSITORY_OVERLAP_MATRIX.csv", REPOSITORY_OVERLAP_ROWS)
    write_csv("CPCS_FIELD_OWNERSHIP_MAP.csv", FIELD_OWNERSHIP_ROWS)
    write_csv("ENGINEERING_OVERLAP_MATRIX.csv", OVERLAP_ROWS)
    write_json("REPOSITORY_GAPS.json", REPOSITORY_GAPS)

    write_text("scripts/validate_package.py", VALIDATOR_SCRIPT)
    (ROOT / "scripts/validate_package.py").chmod(0o755)
    write_text("requirements.txt", "jsonschema>=4.21\nPyYAML>=6.0\n")
    try:
        write_text("scripts/build_package.py", Path(__file__).read_text(encoding="utf-8"))
    except Exception:
        pass

    validation_report = validate_package_in_process()
    write_json("VALIDATION_REPORT.json", validation_report)
    validation_md = "# Validation Report\n\n" + \
        f"**Status:** `{validation_report['status']}`  \n**Validated:** {validation_report['validated_at']}  \n**Repository revision:** `{validation_report['repository_revision']}`  \n**Live render campaign:** `{validation_report['render_campaign_status']}`\n\n" + \
        "## Counts\n\n" + md_table(["Catalog", "Count"], [[k, v] for k, v in validation_report["counts"].items()]) + \
        "\n\n## Checks\n\n" + md_table(["Check", "Status", "Details"], [[c.get("check"), c.get("status"), json.dumps({k: v for k, v in c.items() if k not in {"check", "status"}}, ensure_ascii=False)] for c in validation_report["checks"]]) + \
        "\n\n## Limitations\n\n" + "\n".join(f"- {x}" for x in validation_report["limitations"])
    write_text("VALIDATION_REPORT.md", validation_md)

    manifest_files = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and p.name not in {"MANIFEST.json", "PACKAGE_MANIFEST.json", "SHA256SUMS.txt"}):
        rel = path.relative_to(ROOT).as_posix()
        manifest_files.append({"path": rel, "bytes": path.stat().st_size, "sha256": file_sha256(path)})
    manifest = {
        "schema_version": "cpcs.research_package_manifest/1.0",
        "package_name": ROOT.name,
        "package_version": "1.0",
        "created_at": ACCESS_DATE,
        "repository": REPO,
        "repository_revision": REPO_SHA,
        "empirical_status": "source_and_repository_research_complete_provider_render_campaign_not_run",
        "counts": validation_report["counts"],
        "files": manifest_files,
        "source_brief_sha256": file_sha256(ROOT / "RESEARCH_BRIEF.md") if (ROOT / "RESEARCH_BRIEF.md").is_file() else None,
        "manifest_scope_note": "The manifest lists all files except MANIFEST.json, PACKAGE_MANIFEST.json, and SHA256SUMS.txt. SHA256SUMS.txt covers both manifest aliases and all other files except itself."
    }
    write_json("MANIFEST.json", manifest)
    write_json("PACKAGE_MANIFEST.json", manifest)

    sums = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and p.name != "SHA256SUMS.txt"):
        sums.append(f"{file_sha256(path)}  {path.relative_to(ROOT).as_posix()}")
    write_text("SHA256SUMS.txt", "\n".join(sums))

    # Execute the packaged validator against the final package, including manifest and checksums.
    import subprocess
    result = subprocess.run(
        ["python3", str(ROOT / "scripts/validate_package.py"), str(ROOT)],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Standalone package validation failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
            zf.write(path, arcname=f"{ROOT.name}/{path.relative_to(ROOT).as_posix()}")

    # Archive-level integrity check.
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        bad = zf.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP integrity failure at {bad}")
        names = set(zf.namelist())
        expected = {f"{ROOT.name}/{p.relative_to(ROOT).as_posix()}" for p in ROOT.rglob("*") if p.is_file()}
        if names != expected:
            raise RuntimeError("ZIP member set does not match package directory")

    print(json.dumps({
        "status": "passed",
        "package_dir": str(ROOT),
        "zip": str(ZIP_PATH),
        "zip_bytes": ZIP_PATH.stat().st_size,
        "zip_sha256": file_sha256(ZIP_PATH),
        "file_count": sum(1 for p in ROOT.rglob("*") if p.is_file()),
        "counts": validation_report["counts"],
        "standalone_validator": json.loads(result.stdout),
    }, indent=2))


if __name__ == "__main__":
    assemble_package()
