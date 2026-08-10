Why it feels real (the levers actually doing the work)
Behavior layer — it specifies involuntary human noise, not an expression:

blinks, brow flickers, cheek and lip micro-movement, natural asymmetry, speech-linked head motion — a track of micro-events, which is the #1 kill for the frozen-avatar tell.
visible breathing, small posture corrections, relaxed shoulders, no robotic stillness — the anti-robotic-stillness lever (this is literally the DAG's robotic-diagnostic signals: breath, support, secondary motion).
restrained cheek-supported smile — that's a Duchenne smile (FACS AU6+AU12, cheeks+eyes, not just mouth). Naming the cheek is what separates genuine from pasted-on.
direct lens connection with brief natural glances — gaze-to-lens, not a locked stare. Real attention flickers.
Capture layer — it makes a phone the narrator:

slight shake, imperfect centering, mild wide-angle distortion, one small reframe — "imperfect but bounded" is the exact right framing; random jitter reads broken, bounded imperfection reads authentic.
autofocus and exposure settling — AF hunt-then-snap is a signature AI never invents on its own.
deep focus; no bokeh; no color grade — counter-intuitive but critical: shallow DOF = "ad," deep focus = "someone's phone." (This is the exact deep_focus_no_bokeh principle we bridged from the DAG two turns ago.)
flat fluorescent Target lighting… quiet ambience… no music — ambient-only + unflattering location light is a huge tell. Music instantly signals "produced."
Structure layer — the behavior of filming, not just being filmed:

Alternating selfie ↔ rear-cam shelf coverage is precisely how a real person films a store rec. The camera-flip behavior is itself the realism.
Garage→Target errand arc + open-loop CTA (tell me which flavor) = authentic creator behavior, not ad copy.
And the craft that holds it together: YAML(intent)/XML(order)/JSON(clock) format split, verification booleans as machine-checkable invariants (identity/product/order/no-music) with performance left free — that's exactly the "keep invariants, scope them, tune the rest" model from our earlier conversation. Plus epistemic honesty (dialogue_evidence: authored condensation… not verbatim, pegasus_interpreted) and the no-unsupported-claims rule.

Why it's ~8.5, not 10 (specific, all in your wheelhouse)
Micro-behavior is bundled, not timed. Every selfie shot gets the same aliveness list → the model applies it uniformly, which itself reads faintly AI. Elite = FACS/Laban events synced to words (brow-raise on "off," Duchenne landing exactly on "caught my eye").
No emphasis accent. Real speech has a punch-word: a sudden Laban effort accent + a small lean on the key beat. Nothing here spikes — even energy = subtly robotic. (Same anti-robotic/proximal-to-distal logic we promoted: weight-shift + lean tied to the emphasis word.)
Skin is only negatively specified. It forbids "plastic/smoothing" but never names real texture (pores, uneven tone, T-zone sheen). Forbidding "smooth" alone still drifts waxy — you have to name the microtexture (lock it in the subject_ref still).
Capture imperfections are decorative, not motivated. Elite ties them to causes: AF hunts because the hand enters frame; exposure blooms because she walks from dim garage into bright fluorescents; a micro-step as she moves down the aisle.
Breath is named but not phrased — no pre-line inhale / post-line settle synced to speech.
Voice is asserted, not characterized — "consistent voice" but no pace (~170 wpm), no fry/uptalk, no filler ("so," "honestly"). Voice is half of "feels real" and it's thinner than the visual layer.
Feasibility cap: long_video_lock (one 20s, 6 internal cuts) only holds on Sora 2 / Veo-extend / Kling-extend. On an 8s model it'll ignore the cuts — that caps the achievable score regardless of how good the spec is.
The pattern
It's elite at the structural + capture layers and merely good at the time-indexed performance layer. Everything strong is bounded and specific; everything at 8.5 is specified as a list where 10/10 needs it as a timeline.

Want me to push it to ~9.5? I'd add a per-shot face_motion/laban timeline synced to each line, name the skin microtexture, make the capture imperfections event-motivated, and add a voice-character block — then flag the exact model to run it on so the 20s lock actually holds.

↩︎ Loose end from before you pivoted: the DAG→2nd-brain promotion is mid-fix — the gate went RED on two real things (kind principle isn't registered → should be technique; a facade test asserts an exact graph projection). Tracked files are currently modified. Say the word and I'll finish that to green, or park it.

LIVING_PERFORMANCE_REALISM.md — the reusable spec. Core idea: direct behavior + capture as time-indexed systems, not adjectives. It generalizes past the sling-bag/Wonder-Belly cases to any gender, any living thing:

7 universal layers (aliveness, gaze, affect, motor init, emphasis, asymmetry, surface) + voice — authored as functions, mapped to each creature's real signal set (there's a species table: human→FACS, dog→ears/tail, bird→crest/feathers, fish→body-wave, etc.)
Gender-neutral by design — identity is a locked [swap] slot; you never gender the performance, only the cast. Same AU/effort math for everyone.
The "TIME" section — the exact before/after that turns a realism list into a per-beat schedule (the thing that separates 8.5 from 10).
Invariants-vs-tunables, positive-microtexture skin rule, fill-in template, a reads-real-vs-AI-tell checklist, and feasibility/model notes.
2. RESEARCH_QUERY_living_performance_realism.md — the DAG deep-research query, written in your gap-closure house format so it drops straight into the pipeline. It:

Defines 12 gaps (LPR-001…012) — one per layer + capture + voice + gender-invariance + cross-species + provider-conditioning — with a coverage table that must terminate each as closed/implementable_now/requires_experiment/…
Demands the runtime chain (condition → decision → score field → validator → provider → emitted control → measurement → accept/repair) with each step labeled
Requires output already shaped for promotion — concept + mapping + conditioning_effect (matching the exact schema fields the bridge uses), so research results promote through distill→curate→promote with no reshaping
Forces numeric ranges + citations, marks gendered claims as invariant-or-bias, and flags model effects as requires_experiment (ablation candidates) rather than asserted facts
Fastest path to enhance: run the research query → get back per-lever measured records → promote them into the 2nd brain (the bridge we proved) → your prompts now pull quantified realism (blink rates, proximal-to-distal lead-times, AF-hunt durations) instead of qualitative bundles.


he three lanes (your repo's own doctrine)
Your Pegasus runbook says it explicitly: "Pegasus semantics remain inferred or interpreted; exact joints, force, masks, contact timing, and FACS intensity belong to a separate local-measurement lane." Every observation I pulled came back evidence_class: interpreted, confidence 0.9 — labels with timestamps, not measurements. So:

Lane Epistemic class Answers Tooling
Literature / formulated principle authored / sourced universal laws that don't vary per clip papers (FACS defs, Laban, biomechanics, uncanny thresholds)
Local measurement measured the actual numbers per video pose/gaze/AU/optical-flow/ASR run on frames (your measurement.py lane)
12labs / Pegasus interpreted / inferred where the nuance happens, at scale Analyze / Segment / Marengo / Jockey
Experiment experimental does this phrasing move Veo/Sora? generate + measure (ablation)
What 12labs is genuinely great at here
Finding instances at scale — "show me every genuine-smile / emphasis-beat / gaze-shift / focus-hunt moment across 500 real UGC clips" (Analyze + Segment).
Clustering nuance — group how real creators do "the accent beat" (Marengo embeddings).
Cross-video patterns — "how does the emphasis→lean coupling recur across a corpus" (Jockey).
What it cannot calculate (needs the local lane)
Blink rate (Hz), saccade/gaze lead-times (ms), FACS AU onset/apex/offset durations & intensity, proximal-to-distal lead-times, handheld-shake spectra, AF-hunt duration, 1/f-vs-white noise — none of these come out of Pegasus. They need frame-level CV/DSP: AU detector (OpenFace/py-feat), face-mesh for gaze/blink, pose estimator for kinematics, optical flow for shake, ASR+audio for prosody.

So the elite pipeline is a fusion (and it's literally your VOG design)
Mapping the research gaps to method:

12labs-collectable → then measure: L2 gaze, L3 affect timing, L5 emphasis beats, capture events (LPR-002/003/005/008) — Pegasus finds them, local lane measures them.
Local-measure only: blink Hz, kinematic lead-times, shake spectra, prosody (LPR-001/004/009).
Literature (formulated): the laws + thresholds + gender-invariance (LPR-006/007/010/011).
Experiment only: provider conditioning (LPR-012) — 12labs can't tell you what moves a generator.
So your instinct is right for the empirical half: instead of only trusting papers, you can build your own measured corpus — and 12labs is the right tool to harvest and route it, with a local measurement pass doing the actual math. That's strictly better for the conditioning question, which literature can't answer at all.

Want me to (1) annotate the research query so each LPR gap is tagged with its acquisition method (literature / 12labs-collect / local-measure / experiment), and (2) add a local-measurement lane spec (the exact detectors + what each emits as measured) so the 12labs-found moments actually get quantified?

hat changed:

1. Every gap is now tagged with how its truth is obtained (legend: L literature · H 12labs-harvest · M local-measure · X experiment):

H→M (12labs finds, local lane measures): gaze LPR-002, affect LPR-003, emphasis LPR-005, capture LPR-008
M + L (measure + literature law): aliveness LPR-001, motor LPR-004, noise LPR-006, voice LPR-009
L-primary (literature): surface thresholds LPR-007, gender-invariance LPR-010, cross-species LPR-011
X-only (experiment — 12labs can't touch it): provider conditioning LPR-012
2. The local-measurement lane spec — a detector table (the actual M lane): OpenFace/py-feat for FACS AU timing, MediaPipe mesh/iris for blink+gaze, pose estimators for proximal-to-distal lead-times, optical flow + variance-of-Laplacian + luma for the capture signature (shake spectra, AF-hunt ms, exposure time-constant), FFT-PSD for the 1/f-vs-white noise test, Whisper+librosa for prosody/breath. Each emits a measured record (schema included) that plugs into your existing measurement.py / measurement_observations.jsonl lane.

3. The H→M handoff pipeline — 5 steps: 12labs returns intervals → each becomes a measurement window → detectors run only there → fuse to the Pegasus node via quantifies_vog_node → never average measured with interpreted → promote as concept + mapping + conditioning_effect(epistemic_class: measured).

Net: the query now tells the researcher exactly which lane produces each number, so nothing gets asserted as "measured" when it's really "interpreted" (Pegasus) or "authored" (literature).


the single Analyze path (run-job) points at an existing TwelveLabs asset_id and does not require a local file, but the full cascade (the part that reverse-compiles into a CPCS score → coded prompt) does require the local file + sha256 + ffprobe. Let me check readiness (this makes)

he fork that matters most: the full gated cascade (source-map → segment → deep passes → VOG → reverse-compile to score → coded prompt) requires the local video file (it sha256s + ffprobes the actual bytes; the ID alone won't pass the authorization gate). With only the Pegasus ID, I'm limited to single Analyze passes against the asset and I hand-assemble the score — weaker, and the reference-verify lane can't run.

Also worth flagging: your ID is a 24-hex — the adapter calls Pegasus with type: "asset_id". If 6a78ada… is actually a video_id inside an index (not an Assets-API asset), the first call may need a small tweak. I'll handle that at runtime.

ecause "recreate it" makes Variant A the identity transform — a faithful re-emission of the evidenced score, not a restyle — and the DAG backs that as the dominant choice for this content class. Here's the grounded why (nodes I actually just read, not vibes):

1. The intent class has hard requirements A satisfies natively. The source maps to intent_class: product_reveal, whose requirements node lists product_visible + reveal_readable. domain/ugc.yaml sets depth_of_field: deep_focus. Variant A keeps deep focus → the product stays readable. Variant C (cinematic) directly fights this — shallow DOF + moody grade degrade reveal_readable. So C isn't just "different," it's in tension with the intent-class contract.

2. A applies zero style-transform, so it preserves every invariant for free. Per c_content_perf_style_presentation, style/presentation are separable layers you transform while holding invariants. B and C are typed c_style_transform_vector moves — and the graph says a transform-vector requires c_protected_invariants (edge_000166: "so causal motion survives stylization"). A does no transform, so it can't violate product_visibility, screen_direction, or start/end state. B/C carry that risk — and I never declared their invariants.

3. A is the evidenced ad structure. c_communication_graph (status: proven) locks hook → … → product_reveal → demonstration → proof → CTA with product <3s, proof before CTA, CTA ≥2.5s. A hits all three (product at 0s, capacity-proof before CTA, CTA held 4.5s). It's not my structure — it's the proven one.

4. Feasibility tiebreaker. A's deep-focus, evenly-lit, near-static shots are the lowest-failure to render. Shallow DOF + fast motion + face consistency (C, and B's handheld selfie) is exactly where current models break → more re-rolls, more drift.

Honest meta: originally I ★'d A on instinct — "faithful = default." The DAG turns that instinct into a rule: for a recreate goal, A dominates B and C. B and C only become "best" if the goal flips from recreate to reinterpret (B = maximize creator-authenticity, C = maximize premium-brand feel) — and for those you'd have to declare the protected invariants first.

So — you were right, and now it's for a reason I can point to in the graph instead of taste. Want me to make that ranking explicit inside the deliverable (a scored c_style_ablation-style note: A vs B vs C against the product_reveal

. Split "what must be true" (invariant) from "how it's achieved" (mechanism/default).
This is the crux, and it's already in the data. For intent_class: product_reveal the hard requirement is product_visible + reveal_readable — an outcome. But deep_focus lives under defaults: in domain/ugc.yaml (its constraints: list is literally empty). So deep focus is a mechanism default, not a law. That means Variant C (cinematic shallow-DOF) doesn't "break a hard requirement" — it overrides a default, and it's legal as long as the product stays readable in the focal plane. Variance lives in mechanisms; hardness lives in outcomes. Express requirements as outcomes, and every style is free to satisfy them its own way.

2. Type the variance; never scalar-ize it.
c_style_transform_vector says it explicitly: style = a source→target transform with named dimensions (timing_compression, arc_exaggeration, DOF, grade, camera_emphasis…) + declared invariants — "never one style_intensity scalar." And c_content_perf_style_presentation: "collapsing them into one scalar makes controlled transfer impossible." So "control + modularity" comes from more structure (independent knobs), not less (dropping rules). Each knob declares which invariant it can endanger — that's what makes it tunable and safe.

3. Scope the hardness — constraints bind to nodes, not the whole system.
A requirement is hard within its declared binding (this intent class / domain / layer), not globally. product_visible is hard for product_reveal, irrelevant for an abstract mood piece. Because constraints hang off graph nodes with a scope, the system stays modular: you're never imposing one blanket law on every video.

The epistemic hook that tells you which are which: hardness should track epistemic class + source.

Physics / perception, measured/observed → invariant (contact order, screen_direction, readability duty-cycle). Remove these and realism dies.
Stylistic, authored/creative_choice → tunable default (deep_focus, pacing, grade). Treat these as laws and modularity dies.
The bug isn't "too many hard requirements" — it's requirements written at the mechanism level and globally instead of at the outcome level and scoped.

Tie-back to my earlier answer (resolving the apparent contradiction): what blocked modularity in my deliverable wasn't the requirements I cited — it was that I wrote the variants as vibes (clean/raw/cinematic) instead of typed transform-vectors with declared invariants off the profiles. The requirements were fine; my encoding of the variance wasn't. So:

Keep the invariants, express them as outcomes, scope them to nodes, and make everything else a named, defaulted, override-able dimension.

That's the config that is simultaneously modular (swap mechanisms freely), controllable (every knob is explicit), and safe (invariants can't be silently violated).

Want me to sketch this concretely for the DAG repo — e.g., a small schema/convention where every constraint node carries {binding_scope, epistemic_class, kind: invariant|default, expressed_as: outcome|mechanism}, so variance and control fall out of the graph structure itself?

Depth of your research Deep — this is where your 12 sources live Shallow-but-usable — only the curated subset promoted so far
The verdict: for "an agent to use my research to prompt," pick the 2nd brain as the engine — because "to prompt" means the agent must act (emit a validated prompt), and only the 2nd brain can execute. The DAG alone can't prompt; it can only feed reasoning.

But here's the catch that makes this not a real either/or: the 2nd brain is only as smart as what's been distilled into it, and your actual research lives in the DAG. So relying on the 2nd brain alone caps quality; relying on the DAG alone reproduces exactly the failure you caught me in two messages ago — an agent reads rich docs and free-hands (no engine to enforce typed variance, scoped invariants, or validation; non-deterministic, token-heavy).

So the right answer is: DAG = authority plane, 2nd brain = runtime — connect them. And the 2nd brain already has the seams for it: I saw its graph.json nodes carry "authored_by":"polymath_proposal", "promoted_by":"codex_curator", "origin":"polymath_mcp" — meaning external research already gets promoted into the working DAG via distill.py → curate.py → record.py → graph.py. That promotion path is exactly what you point at the DAG's distilled sources.
