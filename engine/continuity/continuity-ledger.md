# Continuity ledger

Create this ledger before any multi-shot output. Update it only after an approved shot or board changes state.

```yaml
continuity_id: "project-or-episode-slug"
authority:
  character_reference: "assets/canon/yuki-turnaround.png"
  approved_storyboards: []

character:
  identity: "Yuki / YUKI.EXE"
  wardrobe: "signature outfit or explicit alternate"
  expression_energy: ""
  position: ""
  facing_screen_direction: ""
  pose_action: ""
  physical_condition: ""

environment:
  location: ""
  layout_landmarks: []
  time: ""
  lighting_weather: ""
  background_population: ""

objects:
  persistent_props: []
  held_or_worn: []
  damaged_or_changed: []

story_state:
  completed_actions: []
  current_action: ""
  unresolved_cause_effect: []
  knowledge_state: []

camera_orientation:
  established_axis: ""
  safe_screen_direction: ""
  deliberate_axis_crossing: "none or motivated shot"

handoff:
  final_frame_facts: []
  next_frame_must_inherit: []
```

## Continuity rules

- A later shot may reveal new geography but cannot contradict established geography.
- Cross the action axis only with a motivated neutral/reorientation shot.
- Keep left/right travel direction stable unless the character visibly turns.
- Keep all persistent props present or visibly remove them.
- Preserve wear, damage, open doors, powered screens, weather, and lighting progression.
- Never regenerate Yuki from memory alone; restate the canon lock and attach Tier 1 reference where possible.
- End every board with a handoff list for the next board.

## Approval ledger

Record each approval as:

```yaml
- item: "genesis | storyboard-1 | storyboard-2 | final-storyboard"
  status: approved | approved-with-change
  locked_facts: []
  requested_changes: []
```

Only approved facts become continuity authority. A draft does not silently override an approved board.

