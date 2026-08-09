---
id: cpcs.gaps.src010_open_research_questions
kind: gap_register
epistemic_status: PROVIDER_EXPERIMENT
acquisition: authored
sources: [SRC-010]
primary_route: cpcs/research/gaps/
---

# SRC-010 Open Research Questions

SRC-010 (Prompt Lab + references) is the only empirically validated source in
the corpus — but its evidence is deliberately narrow: one authoring session,
one observer, one isolated experiment. Most open questions are about turning
its hypotheses into isolated, replicated experiments.

## Implementation gaps

1. e001 (30 fps vs 24 fps cadence) is a `hypothesis` bundled in the champion.
   Run the isolated A/B: same content, same seed, only `camera.fps` changed —
   and measure whether the 30 fps clip still reads as UGC (p002 promotion).
2. e003 (format variance) has no quantitative variance metric. Define one
   (e.g., per-clip deviation across N format renderings) before p009 can move
   off `low`.
3. v005 (JSON alone) vs v006 (hybrid YAML+JSON) A/B has never been run on the
   same seed. Does the YAML authoring layer add anything the JSON canon
   doesn't already deliver (p008 medium)?
4. The verification loop's **post-render half** is open: no rendered output
   has been re-measured against a canon. Run extract/re-measure/compare with
   the 50 ms / 0.05 m round-trip thresholds on a v006-style render.
5. All 8 profiles are `production_example`/`safety_scoped_example` — none is
   render-validated. Pick one profile per domain and run it through the lab.
6. `blk_facs_au_track` (FACS as numeric AU track) is flagged unproven; it is
   also frontier channel #1. Design the isolated A/B (facial events with
   tolerance vs prose face direction).
7. The Tier 2 pose lane (`extract_pose_tier2.py`) has never been exercised
   end-to-end on a reference clip into a canon (Tier 3/4 lanes are entirely
   unbuilt).
8. p008 rests on a single run (r005). One more independent run would raise
   it from `medium`; one failure would demote it.
9. TOL_REACH 0.35 m and the round-trip thresholds (50 ms / 0.05 m) are
   authored, calibrated only by v006's single pass. What is a defensible
   tolerance set across actors and styles?
10. Low-confidence bundled patterns (p002, p003, p005) have no isolated
    evidence by design — each needs its one-lever A/B or an explicit demotion.

## Cross-source questions

11. The lab's 4 manual score dims approximate the paper's 6 metric families.
    Run the paper's objective metrics on lab renders (or lab-style renders)
    to bridge the gap — or state which dims map to which families.
12. v004's plastic-skin failure is lab-original; the paper's 15 named failures
    do not include it. Should the failure taxonomy gain a skin/plastics class?
13. The lab's 2 control paradigms vs the paper's 4 modes: only Mode A
    (structured prompt) is proven. Which lab artifact would exercise Mode B
    (agent compose) — the composition procedure already exists.
14. p006 (format-neutral for look) vs p008 (numeric structure controls
    motion) needs one joint experiment: same fight content as prose vs JSON
    vs hybrid — does look stay neutral while motion diverges?
15. The 7-condition style ablation is designed but unrun. Its results would
    directly validate the paper's 8-condition factorial design (H5 camera,
    H4 phase/contact analogs).

## Empirical unknowns

16. The 0.18 m reach deficit (1.60 m separation vs 1.42 m combined reach)
    was caught by tooling. What is the smallest canon inconsistency the tool
    can reliably catch — i.e., what is TOL_REACH's true detection floor?
17. The 30 fps cadence claim (p002) and the 0.28 s pause-before-proof speech
    rule come from one session. Replicate on a second model (LTX-2.3 vs
    Veo-3.1) before treating them as lab rules.
18. e002 (skin microtexture) is `isolated_confirmed` but single-observer,
    single-session. A second observer re-scoring the same runs would bound
    the observer effect on the lab's one confirmed pattern.
19. The 0.25 s sample rate and 24 fps timebase in v006 are convenience
    choices. Do finer rates change validation outcomes (frame math family)?

## Governance notes

- All tolerance values (TOL_SPEED 0.05 m/s, TOL_REACH 0.35 m, 50 ms, 0.05 m)
  are authored lab controls, not scientific constants.
- All run scores are qualitative, single-observer, single-session — treat
  pattern confidence as evidence, not conviction.
- Sora 2 / Videos API notes are deprecated (shutdown Sept 2026); per-model
  guidance must be re-verified against current provider docs.
- The lab records what happened in one authoring session; generalization
  claims remain hypotheses until the isolated A/Bs above run.
