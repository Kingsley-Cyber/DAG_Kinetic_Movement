# Director Motion Reasoning Execution Kit

This kit converts the uploaded 1,400-line specification into a repository-aware execution package for `Kingsley-Cyber/ai-video-movement-prompt-system`.

## Start here

1. `01_SPEC_AUDIT_AND_VERDICT.md` — what is already present, what conflicts with repo law, and the verified gaps.
2. `04_HARDENED_CODEX_EXECUTION_PROMPT.md` — paste this into Codex/Claude Code/Qoder or another repository-writing agent.
3. `05_DEEP_RESEARCH_SOURCE_PROMPT.md` — use this for a dedicated Pro Deep Research evidence pass.
4. `06_REPO_INTEGRATION_PLAN.md` — deterministic integration sequence and gates.
5. `02_REPO_GAP_MATRIX.csv` — 55 requirement clusters with owner, status, priority, action, and verification checkpoint.
6. `07_SOURCE_SEED_CATALOG.csv` — authoritative source starting set with caveats.

## Core decision

Do not create a second parallel motion ontology under `research/` by default. The current repository freezes that directory and already contains CPCS v1.2 and CPCS-MX v1.0 packages covering most of the requested architecture. Integrate the actual gaps into the active `lab/` control plane, or explicitly change the governance law in the same commit before adding a new frozen package.

## Highest-priority gaps

- Bartenieff six connectivity patterns;
- BML/SAIBA synchronization alignment;
- explicit non-universal verdict and project-specific normalized phase profile;
- five-way semantic-equivalence compiler/tests;
- closed-loop render re-extraction and compliance metrics;
- scene/VOG graph versus repo knowledge-graph separation;
- claim-level source coverage and reliability calibration.

## Validate this kit

```bash
cd director_motion_reasoning_execution_kit
python3 tools/validate_kit.py
sha256sum --check SHA256SUMS.txt
```

The validator checks the manifest, gap schema/JSONL/CSV parity, required prompt sections, source IDs, and file presence. It validates this execution kit only; it does not claim that the GitHub repository was modified or that its tests were run.
