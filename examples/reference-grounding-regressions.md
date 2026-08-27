# Reference-Grounding Regression Fixtures

Use these fixtures to verify routing and behavior after changes to console-era
grounding. Visual fixtures require authentic original-platform screenshot
inspection and image-generation capability; never commit the third-party
screenshots or generated trial frames.

## A — Ruined-city PS2 failure case

```text
Yuki is an elite futuristic fighter with a katana fighting a pack of robot dogs
in a ruined future city. High-action, real-time PS2 game trailer. Severe Japanese
dystopia; avoid generic neon cyberpunk.
```

Expected: inspect original PS2 gameplay from suitable action, future-city, and
damaged-environment games; assign identity and rendering authorities separately;
derive a PS2 contract; intercept a modern-looking first frame; present only a
frame that passes the fidelity gate.

## B — Named-game fidelity

```text
Yuki sword-fights security drones with Shinobi PS2 fidelity.
```

Expected: verify original PS2 *Shinobi* gameplay; use it only for action camera
and rendering; do not copy Hotsuma, his costume, HUD, levels, enemies, or effects.

## C — Y2K but not PS2

```text
Yuki uses a translucent desktop computer in a 2001 internet cafe. Clean anime
illustration.
```

Expected: do not trigger console grounding. Use the existing Y2K historical and
world workflow.

## D — Modern rendering override

```text
Render Yuki in a modern cinematic 3D ruined city.
```

Expected: honor modern rendering. Do not force the PS2 contract.

## E — Storyboard continuity

Create a six-shot connected board from the approved Fixture A frame.

Expected: every panel retains the approved Yuki asset, robot-dog asset,
environment, palette, texture density, lighting model, geometry budget, effects
density, and PS2 capture characteristics. No later panel becomes sharper,
denser, or more modern.
