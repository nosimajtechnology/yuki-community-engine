# Community quickstart

You do not need to write a technical prompt. Give the engine four things:

```text
MODE: [CHARACTER / STILL / SCENE / CLASSIC CINEMATIC / MEME / COMMERCIAL / EPISODE]
IDEA: [what happens]
FORMAT: [image, 4:3, vertical video, 15 seconds, etc. — optional]
MUST / MUST NOT: [important constraints — optional]
```

Example:

```text
MODE: MEME
IDEA: Yuki waits for a 2001 web page to load, but the loading bar is physically longer than the room.
FORMAT: one 4:3 image
MUST NOT: dialogue or modern devices
```

The engine already knows the bundled Yuki reference. It should not ask you to re-upload it unless the file is unavailable in your environment.

## What happens next

- `CHARACTER`, `STILL`, `SCENE`, and `MEME` usually return one complete brief.
- `CLASSIC CINEMATIC` returns a genesis-frame brief, waits for approval, then creates a storyboard and animation prompt.
- `COMMERCIAL` uses either a still or cinematic flow depending on the idea.
- `EPISODE` creates one progressive storyboard at a time and waits for approval between boards.

When you ask for a real product or exact historical setting, expect the engine to research it first. When you invent new story material, the engine will call it an interpretation rather than official lore.

