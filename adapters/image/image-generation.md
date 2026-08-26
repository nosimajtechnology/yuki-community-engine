# Image-generation adapter

Use for ChatGPT image generation and other reference-capable still-image systems.

## Procedure

1. Attach `assets/canon/yuki-turnaround.png` as the primary character reference.
2. State whether the output is canonical default, controlled alternate outfit, or creative interpretation.
3. Describe the image in this order: composition, visible action/pose, Yuki identity, environment, grounded anchors, lighting/rendering, exclusions.
4. Ask for one image unless the user requests variants.
5. For a genesis frame, compose a stable start state that can be animated and record its end-state facts.

## Template

```text
Create [format] showing [single composition and action].

Yuki must match the attached canonical five-view turnaround: [compressed canon lock].

Environment: [location, layout, two grounded anchors].
Camera: [height, distance, angle, lens language].
Lighting/rendering: [specific treatment].
Interpretation label: [canonical default / alternate look / fictional scene].

Preserve: [three most vulnerable identity traits].
Avoid: [only likely mutations, modern contamination, extra text, or anatomy failures].
```

Do not use an unofficial online image when the bundled turnaround is available.

