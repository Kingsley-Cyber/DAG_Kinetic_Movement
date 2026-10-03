# Owner actions — the only things the model cannot do for you

Everything else is in the queue. These are short and in plain steps.

## 1. Tell the model which Seedance route you use (once)

Answer in one line in chat, or write it here:

- Route: (for example: Dreamina app, Volcengine API, Runway, fal)
- Model version:
- Prompt box limit if you know it:

Until you answer, the profile assumes a 2,000-character limit from third-party docs.

## 2. Render at GATE A (one sitting)

For each run folder under `director/runs/` that has a `prompt.txt`:

1. Open `prompt.txt`. Paste it into your video model. Render.
2. Open `baseline.txt`. Paste it into the same model with the same settings. Render.
3. If the folder has an `arms/` subfolder, render each file in it, using the same seed for each
   arm when the model lets you set one. Three seeds per arm is the target.
4. Open `verdict.md` in that folder and fill in the scores (1 to 5) and one line of notes.
   For contact moments also answer yes or no: did the contact happen, did the reaction follow,
   is the end pose sane.

Then tell the model "verdicts are in". It reads them, runs the kill check and reports.

## 3. Say "push" when you want commits on GitHub

The model commits locally and never pushes on its own.

## Blocked questions from the model

(The implementing model writes questions here when it would otherwise have to guess.)
