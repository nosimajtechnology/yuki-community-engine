# Video-generation adapters

Use after storyboard approval. Provider behavior changes; verify current syntax, duration, reference support, and prompt limits at use time.

## Shared motion brief

- Establish the exact first-frame state from the approved genesis/storyboard.
- Describe chronological action beats, not a collage of outcomes.
- Define camera path, speed, subject tracking, and end framing.
- Preserve Yuki's face, hair mass, wing ornaments, gloves, boots, outfit, and scale throughout motion.
- Keep props, geography, and screen direction consistent.
- State audio intent separately: ambient/SFX, dialogue, narration, music, or none.

## Seedance adapter

Favor chronological shot language and explicit dynamic camera movement. Keep character/action density low. When a user supplies a character limit, compress atmosphere first. Avoid ambiguous nouns that could be visualized as unwanted objects. State “no title cards, playing cards, floating symbols, or extra overlays” only when those artifacts are plausible.

## Kling adapter

Prioritize clear start/end motion, character consistency, and physical interactions. Split overly complex sequences rather than stacking actions. Reassert identity anchors after hard cuts or major angle changes.

## Sora adapter

Use a concise scene description, temporal progression, camera behavior, and continuity constraints. Describe the visual era through observable rendering properties rather than relying only on a game/film title.

## Higgsfield adapter

Select a camera/motion treatment that serves the approved shot rather than changing its story. Treat model presets as camera execution, not creative authority. Preserve the same canon and end state used by every other adapter.

## Provider-ready template

```text
[DURATION / FORMAT]
Use the approved storyboard/reference only.

0:00–0:__ — [visible action + camera + end state]
[continue chronological beats]

CANON: [compressed Yuki lock]
CONTINUITY: [persistent wardrobe, props, geography, lighting, damage]
AUDIO: [explicit]
AVOID: identity drift, extra accessories, outfit changes, teleportation, duplicated props, unreadable text, unrequested overlays, camera motion that obscures the action.
```

