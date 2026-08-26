# v1 validation report

Date: 2026-08-26

## Method

- Inspected the Tier 1 image at full 1491×1055 resolution across front, three-quarter, side, back, and opposite-side views.
- Performed eight textual dry-runs in `examples/dry-runs.md`; no paid generations were required.
- Ran `python3 scripts/validate_engine.py` to check required architecture, canonical asset integrity, mode coverage, episode structure, reference tiers, and absence of a public license.

## Results

| Scenario | Fidelity | Workflow | Continuity | Lore control | Result |
|---|---|---|---|---|---|
| Canonical portrait | Tier 1 lock and default outfit explicit | Direct CHARACTER output | N/A | No biography | Pass |
| Everyday scene | Signature silhouette preserved | One SCENE brief | End state recorded | Ordinary action labeled interpretation | Pass |
| Absurd scene | No character mutation needed for joke | Single readable STILL | N/A | Absurdity labeled interpretation | Pass |
| Y2K nostalgia | Canon separate from environment | Historical protocol triggered | Spatial anchors stated | Era claim labeled | Pass |
| Cinematic | Canon repeated in multi-shot workflow | Approval gates correct | Genesis and six-shot handoff explicit | No official story claim | Pass |
| Dynamic storyboard | Vulnerable silhouette protected | Shot functions vary | Axis and travel direction maintained | No lore dependency | Pass |
| Community meme | Canon anchors retained | Caption separated | One-frame state | Clearly community interpretation | Pass |
| Progressive episode | Same outfit/identity across boards | Four-board default used | Exact board-to-board inheritance | Website story remains invented | Pass |

## Evaluation summary

- **Character fidelity:** Strong at specification level. Actual provider output still needs human visual review.
- **Workflow clarity:** Each mode has explicit deliverables; cinematic and episode approvals are unambiguous.
- **Continuity:** State ledger covers wardrobe, props, geography, lighting, physical condition, action axis, and handoff.
- **Versatility:** Tests cover clean, ordinary, absurd, nostalgic, cinematic, meme, and long-form use.
- **Hallucinated lore:** The engine refuses unsupported biography and marks all test narratives as interpretations.
- **Usability:** Community requests can be expressed in four plain-language fields.
- **Prompt quality:** Briefs lead with readable action and canon, then grounded world detail and compact exclusions.
- **Agent comprehension:** Root `SKILL.md`, README, source register, and direct one-level references provide deterministic routing.

## Remaining limitations

- Textual testing cannot prove face fidelity inside every image/video model.
- The exact front-shirt mark and official color values need vector/brand assets for pixel-accurate reproduction.
- Official social pages should be rechecked when platform access allows direct inspection.
- Adapters intentionally omit volatile API parameters and must be verified against current provider docs.

