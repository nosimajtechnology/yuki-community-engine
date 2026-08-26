# Creative brief contract

Every mode produces the same model-neutral core before provider translation.

## Required fields

```yaml
request:
  mode: CHARACTER | STILL | SCENE | CLASSIC_CINEMATIC | MEME | COMMERCIAL | EPISODE
  concept: "one-sentence premise"
  deliverable: "what the user will receive"
  format: "aspect ratio, duration, shot count, or platform if known"

authority:
  tier_1: ["assets/canon/yuki-turnaround.png"]
  tier_2: []
  tier_3: []
  historical_research: []
  interpretations: []

canon:
  immutable_character_block: "compressed Yuki canon lock"
  allowed_variations: []
  forbidden_mutations: []

world:
  verified_claims: []
  period_or_style_target: ""
  grounded_anchors: []
  invented_elements: []

continuity:
  wardrobe: ""
  props: []
  geography: ""
  lighting_weather: ""
  physical_state: ""
  unresolved_action: ""

production:
  action: "one primary readable action"
  composition: ""
  camera: ""
  lighting: ""
  sound_dialogue: ""
  negative_constraints: []
```

## Output order

1. **Intent** — mode, premise, format, and assumptions.
2. **Authority** — sources used and interpretation labels.
3. **Canon lock** — identity anchors and allowed change.
4. **World/action plan** — readable event and grounded details.
5. **Continuity** — state before and after the output.
6. **Generation brief** — provider-neutral positive direction.
7. **Avoid** — only likely failure modes.
8. **Approval/adaptation** — next gate or requested adapter.

## Simplification rule

When a model may struggle, preserve priorities in this order:

1. Yuki's identity and silhouette;
2. one readable action;
3. continuity and spatial orientation;
4. key world anchor;
5. atmosphere;
6. secondary props and effects.

Remove simultaneous actions, background characters, particles, signage, and complex effects before weakening canon.

