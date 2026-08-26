# Adapter contract

Adapters translate an approved model-neutral brief into provider-ready instructions. They never redefine canon or story state.

## Required inputs

- approved creative brief;
- Yuki canon lock;
- attached Tier 1 turnaround when supported;
- continuity ledger for multi-shot work;
- output format, duration, and requested provider;
- provider-specific limits verified at use time.

## Translation rules

1. Keep positive visual intent before exclusions.
2. Restate identity anchors compactly; do not substitute a provider's assumed character knowledge.
3. Express one primary action and camera behavior per shot.
4. Convert continuity facts into explicit start/end states.
5. Remove unsupported parameters rather than guessing syntax.
6. If the prompt exceeds a provider limit, remove secondary atmosphere and props before canon or action.
7. Mark provider capabilities and limits as time-sensitive; verify current documentation when precision matters.

## Standard output

```text
PROVIDER / MODEL:
INPUT REFERENCES:
FORMAT / DURATION:
CANON LOCK:
WORLD / STYLE:
ACTION AND CAMERA:
CONTINUITY START:
CONTINUITY END:
SOUND / DIALOGUE:
AVOID:
```

Do not add music, dialogue, text, logos, transitions, or effects unless requested or structurally necessary.

