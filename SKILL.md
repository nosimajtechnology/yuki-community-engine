---
name: yuki-community-engine
description: Repository entry point for the canonical Yuki Community Engine package. Use when a loader discovers this repository-level manifest; continue with skill/yuki-community-engine/SKILL.md for all creative workflows and rules.
---

# Yuki Community Engine

This repository-level file is a compatibility entry point. The sole canonical
skill manifest is
[skill/yuki-community-engine/SKILL.md](skill/yuki-community-engine/SKILL.md).

When loading the Engine from a repository checkout:

1. Read the canonical manifest linked above.
2. Resolve its links relative to `skill/yuki-community-engine/`.
3. Follow that manifest as the only behavioral authority.

For installation, use the release ZIP documented in `README.md`. Releases
package `skill/yuki-community-engine/` and do not include this compatibility
entry point.

Do not add Engine behavior, canon rules, or workflow instructions here. Make
those changes in the canonical package.
