---
name: yuki-community-engine
description: Create, plan, and adapt canon-preserving Yuki / YUKI.EXE media for the Y2K Dotcom ecosystem, including character studies, stills, scenes, memes, commercials, short cinematics, dynamic storyboards, animation prompts, and progressive episodes. Use whenever a user asks to load the Yuki Community Engine, create Yuki or Y2Kverse content, preserve Yuki identity across images or video, or turn a Yuki concept/reference into a structured generation workflow.
---

# Yuki Community Engine

## Load authority before creating

1. Read `canon/character/yuki-canon.md` for every request containing Yuki.
2. Read `docs/canon-policy.md` whenever a request adds lore, changes signature design, or introduces another reference.
3. Read `canon/world/y2kverse.md` and `engine/research/historical-grounding.md` whenever a Y2Kverse or historically recognizable setting matters.
4. Treat `assets/canon/yuki-turnaround.png` as Tier 1 and absolute visual authority. Never replace it with generated or web imagery.
5. Label unsupported story choices as **creative interpretation**, never verified canon.

## Route the request

Read `engine/modes/modes.md` and select exactly one primary mode: `CHARACTER`, `STILL`, `SCENE`, `CLASSIC CINEMATIC`, `MEME`, `COMMERCIAL`, or `EPISODE`.

- Infer the mode when the request is clear.
- Ask only if two modes would produce materially different deliverables.
- Do not ask for a Yuki reference when the bundled Tier 1 turnaround is available.
- Ask a maximum of three concise questions, and only for missing canon authority, structural choices, format constraints, or a required target model.

## Build a model-neutral brief

Read `engine/core/brief-contract.md`. Separate:

- user intent;
- character canon;
- verified world facts;
- creative interpretation;
- continuity state;
- delivery constraints.

Keep model/provider syntax out of the creative brief. Apply an adapter only after the brief is approved or complete.

## Preserve continuity

For multi-shot work, read `engine/continuity/continuity-ledger.md` and `engine/storyboard/storyboard-system.md`.

- Establish character, wardrobe, props, geography, lighting, damage, and unresolved action once.
- Carry forward the exact end state of each approved shot or board.
- Change state only through a visible event.
- Reject teleportation, unexplained costume changes, side reversals, duplicated props, regenerated damage, and spatial resets.

## Follow approval gates

For `CLASSIC CINEMATIC`:

1. concept and genesis-frame brief;
2. wait for approval;
3. five-to-seven-shot storyboard;
4. wait for approval;
5. model-neutral animation brief;
6. requested video adapter.

For `EPISODE`:

1. define the episode spine and state ledger;
2. produce **Storyboard 1 — Hook + Setup**;
3. wait for approval before Storyboard 2;
4. continue through Escalation / Development, Major Development / Turn, and Payoff / Resolution;
5. add Storyboard 5 only when the payoff cannot resolve cleanly in four boards and state why;
6. never reset the world between boards.

Do not collapse approval gates unless the user explicitly requests an end-to-end draft.

## Apply an adapter only when requested

Read `adapters/adapter-contract.md`, then the relevant image or video adapter. Preserve the approved creative intent and canon block. If a provider constraint conflicts with canon, simplify scene complexity before altering Yuki.

## Quality gate

Before delivery, verify:

- Tier 1 traits remain unchanged.
- Lore claims show their authority tier.
- Period details are researched when fidelity matters.
- Each shot advances one readable action.
- Camera changes are purposeful and spatially coherent.
- The final output follows the selected mode and requested length/format.
- Negative constraints name likely mutations without bloating the positive prompt.

Use `community/` for community-facing requests. Do not expose or imply undocumented Nosimaj internal methods.

