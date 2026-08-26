# Yuki Community Engine v1

An AI-native character and community creative engine for Yuki / YUKI.EXE and the Y2K Dotcom ecosystem, built by Nosimaj Media.

This repository converts an approved character turnaround, documented source hierarchy, and repeatable production workflows into an agent-readable system. It helps an AI agent make portraits, stills, scenes, memes, commercials, short cinematics, storyboards, and progressive episodes without quietly redesigning Yuki or inventing official lore.

## Why it exists

Character generation usually fails in predictable ways: visual identity drifts, fan interpretation is mistaken for canon, storyboards reset between frames, and model-specific prompt tricks become inseparable from the character. This engine separates four layers:

1. **Character canon** — visually immutable Yuki traits.
2. **World canon** — verified Y2Kverse claims and grounded environment vocabulary.
3. **Creative interpretation** — scene-level choices that may vary safely.
4. **Production logic** — model-neutral workflows, continuity state, and optional adapters.

Lower-authority material can enrich a scene but cannot overwrite higher-authority canon.

## What it can generate

- Canonical character studies and portraits
- Standalone stills and everyday or absurd scenes
- Five-to-seven-shot short cinematics
- Dynamic multi-angle storyboards
- Community memes and remixable concepts
- Fictional Y2Kverse commercials and public-service spots
- Four-board progressive episodes, with an optional fifth board only when structurally necessary
- Provider-ready image and video briefs through isolated adapters

## What it does not do

- Declare fan art, search results, or generated images to be canon
- Guarantee an external model will reproduce Yuki perfectly
- Invent official biography, relationships, powers, locations, or history
- Reproduce proprietary Nosimaj production techniques not included here
- Grant rights to Yuki, Y2K Dotcom, third-party trademarks, or generated outputs
- Publish or license this private repository

## Quickstart

Ask an agent to load `SKILL.md`, then give it a mode and a concept:

> Use the Yuki Community Engine in CLASSIC CINEMATIC mode. Yuki enters an empty 2002-era mall arcade after closing and discovers every CRT cabinet displaying the same blinking cursor. No dialogue.

The engine will:

1. load the Tier 1 turnaround and character canon;
2. classify every unverified story detail as interpretation;
3. confirm only missing decisions that materially change the result;
4. create the concept and genesis-frame brief;
5. pause for approval;
6. create a continuity-aware storyboard;
7. pause for approval;
8. create a model-neutral motion brief and, when requested, a provider adapter.

For a faster start, see [`community/quickstart/quickstart.md`](community/quickstart/quickstart.md). For all modes, see [`engine/modes/modes.md`](engine/modes/modes.md).

## Canon and reference priority

| Tier | Authority | Current role |
|---|---|---|
| 1 | User/team-approved canonical reference | `assets/canon/yuki-turnaround.png`; absolute visual authority |
| 2 | Official Y2K/Yuki material | Project identity and verified public statements |
| 3 | Established community convention | Remix language and recurring community practice |
| 4 | Historical/environment research | Period-correct objects, spaces, interfaces, and media |
| 5 | Creative interpretation | New scenes, actions, props, outfits, and narrative premises |

See [`docs/canon-policy.md`](docs/canon-policy.md) and [`canon/references/source-register.md`](canon/references/source-register.md).

## Example workflow

```text
MODE: SCENE
CONCEPT: Yuki repairing a translucent desktop computer in a quiet bedroom at 2 a.m.
FORMAT: 4:3 still
CONSTRAINTS: no dialogue, historically plausible 1999–2002 consumer technology
```

Expected output: a compact intent summary, source/canon declaration, continuity state, composition and action plan, immutable character block, world grounding, negative constraints, and a model-neutral generation brief. The agent should not ask about details it can resolve safely from the engine.

## Architecture

```text
SKILL.md                         Agent entry point and routing
canon/                           Character, world, and reference authority
engine/                          Workflow, modes, continuity, storyboard logic
adapters/                        Optional provider-specific translation layer
community/                       Safe quickstart and remix surface
examples/                        Eight textual dry-runs
docs/                            Architecture, policy, contribution, portability
scripts/validate_engine.py       Deterministic repository checks
```

Creative intent always flows through canon and continuity before an adapter. Replacing an image or video provider must not change the character definition.

## Community-use philosophy

The engine should make good participation easier without requiring prompt-engineering knowledge. It asks only questions that change canon, story structure, delivery format, or provider constraints. Community remixes may be playful and transformative, but should be labeled as interpretations and must not be represented as official Y2K lore.

The public-facing layer intentionally includes portable rules and starter templates, not the entire Nosimaj internal production stack.

## Current status

**v1 private founding implementation.** The canonical turnaround is installed, seven modes are defined, provider-neutral adapters are scaffolded, progressive episode logic is included, and eight textual scenarios have been dry-run. Paid image/video generations are not part of validation. Public release, open-source licensing, and external distribution require explicit approval.

Known limitations:

- The supplied turnaround establishes visual identity but not biography or behavioral lore.
- Exact official brand colors and logo vector files have not been supplied.
- Dynamic pages on the official site and X limited direct text verification during the 2026-08-26 research pass; source confidence is recorded rather than filled with assumptions.
- Model-specific syntax and capabilities change; adapters must be rechecked at use time.

## Attribution and rights

- **Yuki / YUKI.EXE and Y2Kverse material:** associated with the Y2K Dotcom ecosystem; ownership is not claimed by this repository.
- **Engine architecture and documentation:** developed by Nosimaj Media for this founding implementation.
- **Third-party outputs:** governed by the applicable model provider and the rights of referenced material.
- **Community contributions:** remain attributable to their contributors and must identify their source tier.

No public license is included. All rights and permissions remain with their respective owners.

## Contributions

Keep the repository private unless authorized. Proposed canon changes require a Tier 1 or Tier 2 source, a source-register entry, and explicit review. Creative examples must be labeled as interpretations. Never replace the canonical turnaround with generated art. See [`docs/contribution-guide.md`](docs/contribution-guide.md).

