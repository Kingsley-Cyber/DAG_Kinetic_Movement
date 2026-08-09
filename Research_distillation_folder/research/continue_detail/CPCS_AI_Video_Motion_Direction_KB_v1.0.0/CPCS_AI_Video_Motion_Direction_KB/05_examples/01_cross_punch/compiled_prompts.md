# Compiled Prompts — Grounded Cross Punch

## Veo 3.1

**Request plan:** 8-second generation only when required by the selected reference/high-resolution mode; otherwise choose the nearest supported duration and trim to the 3-second canonical beat. Use a start image showing both full bodies and the action axis.

**Prompt:** Two trained performers stage a safe martial-arts exchange in a clear medium-full two-shot. The attacker drives a compact right cross from the rear foot through the hips and torso, then shoulder, elbow, and fist. The defender’s left forearm meets the fist before it reaches the face and redirects it slightly outward. Both feet remain visible and planted through contact. The attacker immediately recoils to guard. Stable lateral tracking camera, one brief damped jolt exactly at guard contact, realistic timing and contact, no injury, no blood.

**Loss:** phase timing, BESS, and FACS are prompt-only; contact remains high risk.

## Kling VIDEO 3.0

Use a three-shot custom sequence only if geography stays stable: 0.8 s guard master; 1.2 s cross/block; 1.0 s recoil master. Prefer element references for both performers.

## Runway Gen-4.5

Use the opening frame as image input. Keep prompt focused on motion because composition is carried by the image. Request 3 seconds, 24 fps. Do not add a separate close-up that could break contact continuity.
