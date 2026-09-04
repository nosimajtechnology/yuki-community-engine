# Model Adapter Rules

Keep creative intent separate from provider syntax. Build the model-neutral
artifact first, then adapt it.

## fal.ai MiniMax H3 Max

For H3 Max, I2V, T2V, R2V, Classic Control, Direct Explore, or Character Lock,
read [fal-h3-max.md](model-adapters/fal-h3-max.md). That adapter controls route
selection, reference order, seed optimization, prompt structure, and verified
fal.ai fields. It may translate packaging but cannot override Yuki canon,
approved continuity, or the selected style adapter.

## Image package

Include:

1. scene and action
2. canonical Yuki reference assignment
3. selected adapter-specific translation sheet when active
4. latest approved project-image assignment when available
5. assigned style or gameplay references when their route is active
6. wardrobe and props
7. world and spatial layout
8. selected adapter or screenshot-derived rendering contract
9. camera and composition
10. decisive negative constraints

When direct image generation is available, generate instead of returning only a
prompt unless the user requests `prompt only`.

## Video package

Use:

```text
ANIMATION BRIEF

DURATION:
SHOT COUNT:
REFERENCE ASSIGNMENTS:
START STATE:
END STATE:
AUDIO INTENT:

SHOT 1 — [timing]
CAMERA:
YUKI / SUBJECT ACTION:
ENVIRONMENTAL MOTION:
TRANSITION:

[repeat]

CONTINUITY:
MOTION STYLE:
ESSENTIAL NEGATIVES:
LOOP CONDITION:
```

Assign the approved storyboard to shot order, composition, geography, action
state, and rendering. Assign the canonical turnaround to Yuki's underlying
identity. Assign a bundled adapter sheet only to style-specific translation.
Do not ask a video model to redesign the storyboard.

When a registered style adapter is active, preserve its display signifier,
rendering lock, temporal rhythm, motion profile, reference-role firewall,
expression preset, and exclusions. Keep any transformation pre-state,
change-only delta, and post-state explicit. Do not let provider syntax silently
replace adapter rules.

When console grounding was triggered, preserve the approved geometry budget,
texture density, lighting/material model, effects density, draw distance,
camera scale, and capture characteristics. Gameplay screenshots control only
their assigned rendering or environment roles; they never redesign Yuki.

## Named models

For Seedance, Kling, Sora, Higgsfield, or another model:

- use only controls and limits verified in the current user interface or supplied
  by the user
- preserve the same model-neutral shot plan
- translate syntax without changing the story
- keep exact voiceover separate when reliable in-model speech is unknown
- avoid redundant style language that competes with the visual reference
- avoid adapter wording such as `cinematic lighting`, `volumetric atmosphere`,
  `photoreal materials`, or `ultra-detailed` when it would modernize an approved
  console rendering contract
- avoid `smooth animation`, `fluid interpolation`, `glossy anime`, `cinematic
  depth of field`, or `modern digital color` when a broadcast-cel adapter is
  active

If the interface is unverified, label controls `unverified or variable` and give
a generic copy-paste prompt.

## Character limits

When an exact maximum is requested, count every character in the final prompt,
including spaces. Preserve, in order:

1. Yuki identity and anti-drift constraints
2. approved continuity and shot progression
3. selected adapter or screenshot-derived world/rendering contract
4. motion and camera behavior
5. decisive era and identity negatives
6. atmosphere and optional decorative detail

Report the measured count.
