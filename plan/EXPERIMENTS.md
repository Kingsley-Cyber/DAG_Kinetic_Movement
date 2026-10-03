# Experiments — what renders must decide

Every rule in this plan that claims to improve a render is a hypothesis until one of these
experiments says otherwise. Each brief names the arms, what is held constant, how it is scored
and what result changes the plan. The owner renders; verdicts go to `director/runs/ledger.jsonl`.

Common rules for all experiments:

- Same model, same access path, same settings for every arm. Record model version and route.
- **Paired seeds** where the model exposes them: each seed is used once per arm, so arms differ
  only in the prompt. At least three seeds per arm; one good output can be luck.
- One clip, one beat or one causal event per test, so a failure can be attributed.
- Arms must be **fair**: each arm is the best plausible prompt of its kind. A strawman arm (for
  example newtons and metres per second in a text prompt) proves nothing.
- Score per event with three yes/no questions (contact happened, reaction followed, end pose
  sane) plus the adherence dimensions that apply (identity, action, spatial, temporal,
  performance quality, facial, connectivity, camera, continuity), 1–5.
- A result is per model and per route. It is `supported`, `contradicted` or `inconclusive`; small
  samples are conventions for a decision, not statistics.

## E1 — compiled vs baseline (the kill check) — tasks T12, T13

Arms: `prompt.txt` (compiled) · `baseline.txt` (the plain ask) · optional lean variant (T10).
Runs: 001 first, then 002–005. Decision: compiled beats baseline on most runs → continue;
otherwise stop and rethink before building more.

## E2 — absolute vs relative magnitudes — task T18a

**Hypothesis (owner; untested):** a video model follows magnitudes better when they are stated
relative to an anchor inside the clip than when stated as absolutes.

**Rules under test** (`ARCHITECTURE.md` §3.5.3, R-16):

| Level | Rule | Enforcement today |
|---|---|---|
| IR | every scaled quality and every force references an anchor; the compiler never writes two absolutes from scaled values | hard |
| free-text wording | bare magnitude words (`fast`, `heavy`, `powerful`, `strong`, `hard`, `big`, `exaggerated`) with no anchor in scope | lint warning |
| named techniques | `slow motion`, `real-time`, `speed ramp`, `time-lapse`, and terms in a profile's `defaults_to_counter` | allowed |

**Specimen:** one beat from the owner's fight IR (`Downloads/Additional/TERMINAL_DESCENT_FIGHT_IR_v1.json`;
"Can Mara prevent Veyr from touching the reactor core until the seal closes?"), cut to a single
clip the model supports (for example the interception beat, about 6 s). The full 30 s specimen is
not one clip on most models; do not test with it.

**Arms (same IR, two emissions):**

| Field | Absolute arm (fair) | Relative arm |
|---|---|---|
| anchor | none | beat 1 states the baseline as visible fact: "Veyr strides at a steady walking pace toward the core" |
| subject speed | "Mara sprints fast across the deck" | "Mara crosses the deck much faster than Veyr's walk" |
| force | "she slams into him hard" | "she hits him harder than her first shove; he gives a full step" |
| camera | "fast dolly in" | "dolly in; the foreground closes faster than the background" |
| playback | "slow motion on the impact" (named technique; identical in both arms) | same |

The IR may store multipliers (2× the anchor); the emitter turns them into words ("much faster
than"). Multipliers, newtons, metres per second and g-forces are not written into either arm.

**Seeds:** the same three (or more) seeds for both arms. **Risks to watch:** absolute arm →
stiff or exaggerated motion; relative arm → the anchor drifts across the clip, or the
foreground/background differential collapses when camera, subject and background all move.

**Decision:** relative better on at least two of three paired seeds for physical plausibility
with equal intent → the wording lint becomes a hard failure for that model. Otherwise the
warning stands. Either way the IR-level rule stays.

## E3 — wording rungs — task T18b

**Hypothesis (untested):** for one movement quality, the visible body description is followed
best, the Laban term worst.

Arms, same beat and anchor: numeric ("weight 0.8, time 0.9" inside a structured block) · Laban
term ("a strong, sudden, direct strike: a punch drive") · visible description ("the strike starts
in the planted rear foot, turns through hips and shoulders, and lands with the whole body behind
it"). Decision: the best rung becomes that model's default in its profile; the others stay
available as experiments.

## E4 — causal wording and the safety-avoidance question — task T35

Arms on the stomp: plain prompt · causal prompt (trigger → contact → reaction → settle) · causal
prompt with a prop in place of the person. If the prop version lands cleanly and the person
version does not, that points to avoidance behaviour rather than a wording gap. Decision: which
failures go in the failures registry as vocabulary gaps and which as ceilings.

## E5 — emphasis lever forms on Hailuo — task T53

Arms: `<i>word</i>` · `<emphasis>word</emphasis>` · `*word*` · no emphasis. Decision: the lever
with the best result becomes the profile's first `emphasis` lever with `evidence: measured`;
asterisks are dropped if they produce bleeps.

## E7 — front-loading

**Hypothesis (prompt-engineering heuristic; not in the research):** the first 20–30 words carry
more weight, so the main action should sit there. Arms: the emitter's default order (shot line,
subject, ordered action, …) · the same content with the core action sentence moved to the very
first line · the same content with camera and capture first. Decision: the best order becomes the
model profile's `clause_order`; no universal claim.

## E6 — camera grammar form — task T38

Arms: bare move word ("dolly in") · the four-part grammar (Movement / Speed / Framing / End) ·
locked-off as the control. Decision: whether the four-part form is worth its length per model.
