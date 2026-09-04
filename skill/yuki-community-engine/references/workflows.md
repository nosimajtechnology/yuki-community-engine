# Modes and Workflows

## Resolve the visual style first

Before the first creative stage, resolve `FLAGSHIP PS2` or a registered adapter
using `style-adapters.md`. A registered adapter replaces console rendering,
camera, and motion rules while active unless the user explicitly requests a
hybrid. Keep Yuki's canonical turnaround as underlying identity authority in
every style.

## Reference-grounded console fidelity

When the request names a console era, a specific game's fidelity, gameplay
rendering, or an in-engine trailer, read `rendering-grounding.md` and insert this
shared stage before the first generated image:

```text
IDEA -> ERA / GAME FIDELITY DETECTION -> AUTHENTIC SCREENSHOT SEARCH
-> VISUAL INSPECTION -> REFERENCE ROLE ASSIGNMENT -> RENDERING CONTRACT
-> IMAGE -> INTERNAL FIDELITY GATE
```

Apply this stage to STILL, SCENE, CLASSIC CINEMATIC, COMMERCIAL, and EPISODE
only when triggered and no registered adapter overrides the game build. Y2K
settings, clean anime art, character studies, memes, and modern-rendering
requests do not trigger it by themselves.

## CHARACTER

Purpose: establish or study Yuki's canonical identity.

Default output: one clean portrait, turnaround-compatible view, expression study,
or outfit study. Use a neutral background when identity inspection matters.
Do not create a story or animation package unless requested.

## STILL

Workflow:

```text
IDEA -> IMAGE DIRECTION -> [GROUNDING WHEN TRIGGERED] -> IMAGE
-> FIDELITY GATE WHEN TRIGGERED -> NARROW REPAIR OR VARIATION
```

Generate one strong image. Include enough environment to explain the premise.
Do not add a storyboard or video prompt automatically.

## SCENE

Purpose: one contained event around Yuki without the full approval pipeline.

Default to a single image or concise scene concept. If the user asks to animate
or expand it, promote the approved visual to CLASSIC CINEMATIC.

When console fidelity is triggered, ground and gate the single image before
presenting it.

## CLASSIC CINEMATIC

Workflow:

```text
IDEA -> CONCEPT -> [GROUNDING WHEN TRIGGERED] -> GENESIS FRAME
-> FIDELITY GATE WHEN TRIGGERED -> APPROVAL -> CONNECTED STORYBOARD
-> APPROVAL -> MODEL-NEUTRAL ANIMATION BRIEF -> MODEL PROMPT
```

Defaults: 5-7 shots, approximately 8-15 seconds, one clear premise, one
continuous location or motivated travel between connected spaces. If the idea is
already clear, skip concept options and create the genesis frame.

The first frame locks identity, wardrobe, main props, world, light, rendering,
geography, and tone. Do not show or expand a frame that fails the triggered
rendering contract.

## MEME

Optimize for one immediately readable joke, reaction, behavior, or cultural
reference. Keep Yuki recognizable at small size. Prefer one visual premise over
multiple captions. Do not invent official lore or add token-price messaging.

Return an image when generation is available. If text is required, provide the
caption separately unless embedded text is essential.

## COMMERCIAL

Workflow:

```text
PRODUCT OR SERVICE -> HOOK -> VISUAL PROGRESSION -> BRAND PUNCTUATION
-> [GROUNDING WHEN TRIGGERED] -> GENESIS FRAME
-> FIDELITY GATE WHEN TRIGGERED -> APPROVAL -> STORYBOARD -> APPROVAL
-> ANIMATION PACKAGE
```

Treat fictional products seriously inside the world. Begin with an action,
failure, reveal, or strange product use instead of a passive establishing shot.
Keep the product readable. Use dialogue or narration only when requested or
structurally necessary. Separate exact voiceover from the video prompt when the
model cannot reliably deliver it.

## EPISODE

Use progressive storyboards for a longer continuous narrative.

Default architecture:

1. **Storyboard 1 — Hook + Setup**: begin with the premise already active or
   immediately visible; establish the goal, disruption, or question.
2. **Storyboard 2 — Escalation / Development**: complicate the goal and advance
   action without resetting the world.
3. **Storyboard 3 — Major Development / Turn**: deliver a meaningful reversal,
   discovery, commitment, or confrontation.
4. **Storyboard 4 — Payoff / Resolution**: resolve the central visual promise or
   end on an intentional cliffhanger.
5. **Storyboard 5 — Optional only when structurally justified**: use for a true
   second climax, aftermath, or bridge that cannot fit cleanly in Board 4.

Approval is mandatory after each board. Before creating the next board, capture
the prior board's final frame as a continuation lock:

- exact location and geography
- every character's position, facing, pose, and condition
- wardrobe and carried objects
- prop and vehicle state
- light, weather, damage, opened/closed doors, and screen direction
- unresolved action and emotional beat

Start the next board from that state. Do not restage the premise, replay the last
action, teleport characters, repair damage, reset props, or change time of day
without a visible transition.

When console fidelity is triggered, ground the first genesis frame before Board
1 and retain its reference set and rendering contract through every board. Do
not expand a frame that fails the fidelity gate. Re-run the gate on each board
before presenting it.

Plan four boards by default. Add Board 5 only after stating in one sentence why
Board 4 cannot deliver a clean payoff.

## Storyboard grammar

For every board:

- use one rendering contract across all panels
- retain the selected style adapter, adapter version, style-local expression
  preset, motion profile, and assigned reference roles across every panel
- retain the approved geometry budget, texture density, lighting model, effects
  density, draw distance, and capture characteristics in every panel
- preserve identical character and prop assets
- use equal panels with thin gutters and no labels unless requested
- progress one continuous action state
- vary distance, height, angle, foreground, lens feel, and movement purposefully
- keep screen direction and geography readable
- avoid repetitive shot sizes or six versions of the same camera
- avoid simultaneous actions that cannot be read in one panel

A storyboard is previsualization for connected footage, not a collage of concept
variations.

## Video creation routes

Resolve this after mode and style, before developing concepts or generating a
video source. Skip the chooser when intent already makes the route clear.

### CLASSIC CONTROL

Use for a polished scene whose opening composition, continuity, and edit need
approval. It is automatic for CLASSIC CINEMATIC.

```text
SEED IDEA -> STYLE -> OPTIMIZED CONCEPT -> GPT IMAGE 2 GENESIS FRAME
-> SELECTED-STYLE GATE -> APPROVAL -> GPT IMAGE 2 STORYBOARD -> APPROVAL
-> MODEL-NEUTRAL ANIMATION BRIEF -> H3 MAX I2V PROMPT
```

Upload the approved Genesis Frame as the literal I2V opening frame. The
storyboard remains planning and editorial authority; do not upload it to H3 Max
by default. Use its shot order, geography, action states, and transitions in the
prompt. The canonical and selected style sheets remain upstream identity and
style authorities used to create and repair the frame.

### DIRECT EXPLORE

Use for fast, free concept iteration. Send no image, video, or audio reference.
The T2V prompt must fully describe Yuki, the selected rendering style, setting,
action, camera, continuity, and ending. Identity is interpretive rather than
canon-locked; after repeated drift, recommend CHARACTER LOCK or CLASSIC CONTROL
instead of bloating the text prompt.

If a seed idea is loose, offer no more than three distinct T2V-ready concepts.
If it is clear, refine one direction and continue without forcing a choice.

### CHARACTER LOCK

Use when Yuki must remain recognizable but the opening frame should stay free.
The canonical Yuki sheet is the primary R2V reference. Add the selected
style-specific sheet second when one is active. Add a secondary character,
environment, prop, wardrobe, motion, or audio reference only when the scene
needs it, and assign each one a narrow role. A compact shot plan may guide the
prompt, but a Genesis Frame and storyboard are not required.

For fal.ai H3 Max packaging, use `model-adapters/fal-h3-max.md`.
