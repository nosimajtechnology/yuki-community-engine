# Reference-Grounded Console Fidelity

Use this workflow when the user requests `PS2`, `PlayStation 2`, an equivalent
early-2000s console era, gameplay or in-game rendering, a real-time game trailer,
or fidelity based on a named console game. Do not trigger it merely because a
scene is set in the Y2Kverse. Clean anime illustration, character studies,
memes, ordinary nostalgia, and explicit modern rendering retain their normal
routes.

Console-era fidelity is a construction problem, not a filter. The selected era
must control geometry, textures, materials, lighting, draw distance, effects,
camera language, subject scale, and capture characteristics.

## Search and inspect before generation

Retrieve and visually inspect three to five useful screenshots when available:

1. an action and gameplay-camera reference
2. an environment and architecture reference
3. a materials, lighting, and texture-density reference
4. optionally an enemy, vehicle, or machinery-construction reference
5. optionally the named-game fidelity reference requested by the user

Prefer authentic screenshots from the original console release, in order:

1. identifiable original-platform gameplay captures
2. identifiable original-platform in-engine cutscenes
3. contemporary reviews, manuals, or archival pages that clearly label the
   platform and show real-time graphics
4. secondary screenshot databases only when platform and release are credible

Reject remasters, HD collections, emulator texture packs, widescreen patches,
ReShade captures, fan remakes, promotional key art, box art, pre-rendered
cinematics, modern concept art, and captures whose platform cannot be reasonably
identified. If authentic sources are too limited, say so briefly instead of
inventing precise reference observations.

Inspect the images themselves, not only search-result titles or prose. Record
only useful observations: polygon density and silhouette construction; texture
resolution, repetition, blur, compression, and UV behavior; material response;
light and shadow model; draw distance and fog; effect density; camera height,
distance, framing, and subject scale; enemy reuse; and capture ratio/aliasing.

## Assign reference roles

State assignments internally before prompting:

```text
YUKI CANONICAL TURNAROUND — identity authority only: face, cyan hair, paired
ornaments, proportions, gloves, boots, and underlying silhouette.

APPROVED PROJECT IMAGE — current wardrobe, environment, geography, light,
palette, props, and action state.

GAMEPLAY REFERENCE A — action camera and subject scale only.
GAMEPLAY REFERENCE B — environment massing and draw distance only.
GAMEPLAY REFERENCE C — geometry, textures, materials, lighting, and effects only.
USER MOOD REFERENCE — mood or composition only unless explicitly reassigned.
```

Never let gameplay references replace Yuki's identity. An approved project image
continues to outrank the rendering references for current scene state.

## Derive the PS2 rendering contract

For a PS2 request, use constraints equivalent to:

- native-looking 4:3, 480i/640x480-era capture unless another ratio is requested
- limited polygon counts with chunky, faceted silhouettes
- broad 128-256px-feeling diffuse textures with blur, compression, repetition,
  and mild UV stretching
- vertex/Gouraud-style lighting with restrained material response
- simple baked, projected, blob, or hard-edged shadows
- short or fog-managed draw distance
- sparse smoke planes and limited particles
- restrained reflections, bloom, and post-processing
- visible aliasing and period-appropriate texture filtering
- gameplay-readable subject separation and reusable enemy assets

Reject:

- modern PBR or ray-traced materials
- volumetric fog, global illumination, bokeh, or cinematic depth of field
- high-poly machinery or detailed joint assemblies
- photoreal skin, cloth, or individual hair strands
- dense rubble, decals, particles, or environmental micro-detail
- modern Unreal-style grading, concept-art polish, or remaster sharpness
- scanlines, blur, chromatic aberration, or noise used to disguise modern assets

Adapt the contract when another console generation is requested. Derive its
constraints from inspected original-platform captures rather than reusing the
PS2 list mechanically.

## Named-game grounding

Verify that the inspected captures are from the requested original platform.
Extract only transferable rendering facts such as camera scale, asset density,
texture handling, environmental massing, and effect limits. Do not copy protected
characters, costumes, HUDs, logos, exact enemies, exact levels, signature props,
or shot compositions. A named game is rendering authority, not content authority.

## Internal fidelity gate

Before presenting a genesis frame, still, scene, commercial frame, or storyboard,
compare it with the selected gameplay references. Count these failures:

- materials look physically based or photoreal
- geometry is substantially denser than the screenshots
- debris or effects are substantially denser than the screenshots
- lighting uses modern volumetrics, global illumination, or cinematic depth of
  field
- enemies look like bespoke high-detail models instead of reusable game assets
- camera staging reads as modern concept art instead of gameplay/trailer footage
- softness looks applied as a filter over otherwise modern assets

Two or more failures mean the image is not an approval candidate. Do not show it
as if it passed.

Make one automatic narrow repair:

```text
LOCK:
Yuki identity, action, geography, composition, wardrobe, palette, and correct
scene layers.

CHANGE ONLY:
Failed rendering-era layers. Reduce geometry, texture/material complexity,
lighting, effects, draw distance, or camera modernity to match the inspected
original-platform screenshots.

DO NOT CHANGE:
Yuki's canonical identity, approved project state, story action, spatial layout,
or any layer that already passes.
```

Repair only failed layers when one or two are wrong. Regenerate from scratch when
the underlying assets, lighting, and camera are all modern. Re-run the gate. If
the second attempt still fails, report the limitation briefly and ask whether
the user wants another grounded attempt.

For connected storyboards and episode boards, retain the approved reference set
and rendering contract in every panel. Later shots cannot silently gain polygons,
modern materials, denser effects, upgraded lighting, or remaster sharpness.

## Copyright boundary

Inspect screenshots to infer general rendering and camera characteristics. Do
not bundle, redistribute, trace, or reproduce third-party screenshots in the
repository or output. Do not copy protected game content. Transform the observed
technical constraints into an original Yuki scene.
