# Model Adapter Rules

Keep creative intent separate from provider syntax. Build the model-neutral
artifact first, then adapt it.

## Image package

Include:

1. scene and action
2. canonical Yuki reference assignment
3. latest approved project-image assignment when available
4. wardrobe and props
5. world and spatial layout
6. rendering/style construction
7. camera and composition
8. decisive negative constraints

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
identity. Do not ask a video model to redesign the storyboard.

## Named models

For Seedance, Kling, Sora, Higgsfield, or another model:

- use only controls and limits verified in the current user interface or supplied
  by the user
- preserve the same model-neutral shot plan
- translate syntax without changing the story
- keep exact voiceover separate when reliable in-model speech is unknown
- avoid redundant style language that competes with the visual reference

If the interface is unverified, label controls `unverified or variable` and give
a generic copy-paste prompt.

## Character limits

When an exact maximum is requested, count every character in the final prompt,
including spaces. Preserve, in order:

1. Yuki identity and anti-drift constraints
2. approved continuity and shot progression
3. world/rendering contract
4. motion and camera behavior
5. decisive negatives
6. atmosphere and optional flourishes

Report the measured count.
