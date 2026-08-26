# Architecture

## Design goal

A fresh agent should be able to load the repository, identify authority, select a workflow, preserve Yuki, and produce a structured brief without hidden creator context.

## Data flow

```text
User concept
  → mode router
  → source-tier classification
  → Yuki canon lock
  → world/research layer
  → model-neutral brief
  → continuity + storyboard state
  → approval gate
  → optional provider adapter
  → quality gate
```

## Modules

| Module | Responsibility | Must not do |
|---|---|---|
| `canon/character` | Define immutable visual identity and controlled variation | Invent biography or provider syntax |
| `canon/world` | Separate verified positioning, community convention, and world vocabulary | Turn generic nostalgia into official lore |
| `canon/references` | Record tier, claims, date, and limitations | Promote low-tier sources silently |
| `engine/core` | Normalize every request into a model-neutral contract | Hard-code one provider |
| `engine/modes` | Choose deliverables and approvals | Change canon |
| `engine/continuity` | Persist physical and story state | Treat drafts as approved authority |
| `engine/storyboard` | Create readable progressive visual sequences | Reset scenes between shots/boards |
| `engine/research` | Ground recognizable historical material | Rely on vague “Y2K aesthetic” assumptions |
| `adapters` | Translate approved intent to a provider | Add story, props, dialogue, or redesigns |
| `community` | Offer safe, low-friction remix interfaces | Expose undocumented internal production IP |

## Extension points

- Add a model under `adapters/image/` or `adapters/video/` using `adapters/adapter-contract.md`.
- Add another character as a separate canon module and Tier 1 asset; never merge its traits into Yuki.
- Add a new mode only if it changes the deliverable or approval structure.
- Add automation around brief validation, continuity diffs, source freshness, and adapter-length checks without automating canon judgment.

## Invariants

1. The Tier 1 turnaround outranks all prose and generated output.
2. Creative interpretation is never stored as official world or character canon.
3. Provider replacement cannot modify the character definition.
4. Approved physical state must pass between every shot and storyboard.
5. User-facing community templates remain usable without prompt-engineering expertise.

