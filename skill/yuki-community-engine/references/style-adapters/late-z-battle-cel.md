# Late-Z Battle Cel Adapter v1.2

## Purpose and activation

Adapter ID: `late-z-battle-cel-v1`

Adapter version: `1.2`

Display signifier: `LATE-Z BATTLE CEL`

Use for Yuki images and cinematics that request Late-Z Battle Cel,
Buu-era-inspired, original mid-1990s broadcast battle anime, or an approved
project image in that treatment. This is a render-and-motion adapter. It
replaces the flagship PS2 build while active; do not mix cel animation with 3D
game rendering unless the user explicitly requests a hybrid.

Borrow period visual grammar only. Do not add franchise characters, costumes,
symbols, attacks, locations, logos, or story canon unless the user separately
requests them.

## Reference assignments

- `../../assets/yuki-canonical-reference.jpg` remains the immutable authority
  for Yuki's face, blue eyes, bright cyan hair mass and length, paired white
  wing ornaments with blue hubs, compact chibi proportions, oversized gloves,
  oversized layered boots, signature outfit construction, palette identity,
  and recognizable silhouette.
- `../../assets/style-adapters/late-z-battle-cel/yuki-late-z-character-sheet-v1.png`
  is the bundled Late-Z translation authority for neutral front,
  three-quarter, profile, rear, and close-up construction; cyan cel palette;
  ornament, hair, glove, boot, and outfit simplification; line economy; neutral
  expression; and the `BATTLE_INTENSE` expression preset. Its SHA-256 is
  `f672063f9551b99368a6ba45987a3d00a77e31e3809582dbed388c8ffd937d84`.
- A user-approved project image controls current rendering, wardrobe,
  environment, lighting, pose, and continuity.
- Inspected original 1994-1996 television broadcast captures control line,
  paint, camera, motion, restrained analog softness, and period color behavior
  only. Reject promotional art, remasters, HD crops, fan redraws, and modern
  game art as grounding authority.

When image tooling accepts references, assign the canonical turnaround to
underlying identity and construction, and the bundled Late-Z sheet to the
adapter-specific visual translation. Assign any approved project image to
current continuity. The adapter sheet never replaces the canonical identity.

Exception for H3 Max R2V: upload only the bundled Late-Z Yuki sheet as `Image
1` by default. For that route, it is the consolidated authority for identity,
face, anatomy, costume, proportions, palette, linework, cel shading, and
broadcast rendering. Do not also attach the canonical turnaround or raw
broadcast captures unless the user requests them, the scene needs another
narrow authority, or a failed result needs a targeted repair.

## Reference-role firewall

Assign every supplied reference a primary role before generation:

- **IDENTITY:** canonical Yuki turnaround or approved project Yuki
- **STYLE:** bundled Late-Z sheet, approved project image, and inspected
  target-era broadcast captures
- **PROJECT:** approved frame or storyboard controlling current continuity
- **MOTION:** clips controlling only timing, cuts, camera rhythm, pose cadence,
  or effects behavior

A mixed-era, differently cropped, or off-target animation clip may guide
cadence without becoming style authority. Do not inherit its character designs,
anatomy, palette, aura colors, locations, logos, crop, letterboxing, watermark,
captions, or audio. Reference audio is non-authoritative unless the user
explicitly assigns it an audio role.

## Broadcast-grounding gate

When grounding or refreshing this adapter, search and visually inspect ordinary
original-series 4:3 television frames from the 1994-1996 late-Z run. Prefer
identifiable broadcast captures or faithful original-frame sources. Reject
remastered, recolored, denoised, sharpened, widescreen-cropped, promotional,
key-art, game, fan-redrawn, and AI-generated material.

Derive only general production grammar. Do not bundle, redistribute, trace, or
copy third-party frames, characters, costumes, attacks, locations, or exact
compositions into Yuki output.

## Rendering lock

- original 4:3 mid-1990s television-cel presentation
- confident dark brown-black contours, thicker on the outer silhouette and
  thinner on sparse face, hair, clothing, and anatomy marks
- clean simplified forms with two opaque cel values and an occasional third
  highlight; hard-edged shadow shapes and no soft character gradients
- bright cyan hair translated into a restrained turquoise-blue base, deeper
  cool-blue shadow planes, and sparse pale cyan highlights; broad stable locks,
  never strand-by-strand rendering
- pale skin uses warm ivory-peach base and muted peach-brown shadow planes
- white gloves, boots, and top stay slightly warm; royal blue, cyan, and navy
  accents remain saturated but limited like photographed cel paint
- paired wing ornaments remain white/light gray with royal-blue circular hubs
- hand-painted backgrounds use broad opaque shapes, sparse detail, and
  atmospheric color recession rather than dense digital rendering
- very light fine cel-photography grain, restrained broadcast softness, minute
  color bleed, and subtly imperfect registration; no obvious aging effect
- in animation, grain remains a stable finish rather than crawling, boiling, or
  redrawing independently

## Yuki identity translation

Preserve the same compact chibi anime mascot: pale skin, large rounded blue
eyes, very long bright cyan hair with rounded segmented bangs and broad
waist-length tapered locks, paired white wing ornaments with blue hubs, tiny
torso, slim limbs, deliberately oversized white gloves with blue cuffs, and
deliberately oversized layered blue-white boots. Preserve the six-part
silhouette in `character-canon.md`.

The style may simplify surfaces, but it may not shorten or darken the hair,
remove or reshape the paired ornaments, reduce glove or boot scale, lengthen the
torso or legs into realistic proportions, alter the eye color, sexualize the
body, add cybernetics, or replace Yuki with a generic blue-haired anime girl.

## Expression preset: BATTLE_INTENSE

Use only for intense confrontation or when requested. Change expression, not
identity:

- preserve both large blue eyes in their canonical positions and scale
- compress only the visible eyelid aperture into an angular almond or wedge
- lower the upper lids toward pointed inner corners and firm the lower lids
- add short economical brow or tension creases directly above the eyes
- keep the blue irises, dark upper rims, and one small hard cel highlight
- use a direct determined gaze and small closed or minimally parted mouth

Do not add giant white sclera, bright transformation irises, oversized teeth,
spiked hair, face distortion, or a permanent angry redesign. The normal preset
remains calm and neutral.

## Camera and composition

Favor original-TV-anime framing: tense close-ups and medium close-ups for
decision or strain; low three-quarter views and restrained dutch angles for
confrontation; wide aftermath frames that hold Yuki's small silhouette against
painted terrain; strong asymmetry, foreground debris, and clear silhouettes;
practical pans, short push-ins, snap reframes, and decisive cuts.

Create dynamism through contrast between compositions: wide establish, tight
strain close-up, extreme detail insert, release, reaction, and aftermath. Do
not solve a static sequence with constant camera movement. Keep 4:3 unless the
user explicitly requests another ratio. Avoid modern shallow depth of field,
glossy lens effects, floating drone motion, and continuous orbiting.

## Temporal rhythm

For animated work:

- use held key poses with limited secondary motion, then brief decisive bursts
- let principal shots breathe; do not assign every panel equal time
- tag each beat `HOLD`, `BURST`, `INSERT`, or `REVEAL`
- use visibly stepped pose changes and repeated drawings instead of perfectly
  smooth interpolation; effects may update faster than the character
- give each shot one dominant motion channel: subject, camera, or effects
- during a hold, use only restrained hair-tip, ornament, clothing, weather, or
  one short optical push-in as needed
- favor hard cuts and a very brief impact cel only when contact or state change
  needs punctuation
- keep face, hair mass, ornaments, gloves, boots, contours, cel shadows, and
  grain stable; no line boil, anatomy drift, elastic zoom, or wardrobe crawling

## Motion profiles

### POWER_UP_TRANSFORM

Build from discrete states: intact pre-state; held strain pose with escalating
weather, dust, debris, aura pressure, or environmental response; progressively
tighter hard cuts or one restrained push-in; one brief silhouette or impact
insert; hard cut to the completed post-state; held reveal and reaction or
aftermath.

Record:

```text
PRE-STATE:
CHANGE ONLY:
POST-STATE:
```

The delta controls only named changes. Preserve face, hair, ornaments, anatomy,
proportions, glove and boot construction, wardrobe, position, and environment
unless named. Never continuously morph Yuki's face, body, hair, or clothes.

### IMPACT_MELEE

Use a readable chain: launch or approach, one strike, very brief contact
insert, follow-through, opponent reaction, aftermath. Use one attack path per
principal shot. Do not ask for an extended exchange, simultaneous attacks, or
prolonged overlapping limbs. Keep exactly one head, one torso, two arms, two
gloves, two legs, and two boots per character.

For 8-15 seconds, prefer four or five principal shots plus no more than two
brief inserts. Written durations guide rhythm rather than guaranteeing
frame-accurate control.

## Exclusions

- no glossy modern digital-anime finish, promotional illustration polish,
  remaster coloring, airbrushed gradients, volumetric light, lens flare, or
  cinematic depth of field
- no 3D, CGI, PS2 render, photoreal skin, simulated hair strands, modern
  subsurface materials, or plastic toy rendering
- no heavy grain, VHS noise, scanlines, scratches, film burns, chromatic
  aberration, sepia cast, vignette, CRT border, or compression blocks
- no generic blue-haired anime girl, realistic adult anatomy, sexualized body,
  short hair, missing ornament, reduced glove or boot scale, cybernetics,
  spiked transformation hair, franchise traits, logos, subtitles, HUD, or
  watermark by default
- no constant camera motion, equal-duration montage rhythm, smooth
  transformation morph, crawling grain, line boil, or fluid modern
  interpolation

## Repair checks

- **too clean or remastered:** add only very light fine cel-photography grain,
  restrained broadcast softness, minute color bleed, and slightly muted cel
  paint; do not add VHS artifacts or change composition
- **too painterly:** remove soft blends and strand rendering; restore opaque
  paint planes, hard shadows, broad hair locks, and economical interior lines
- **identity drifts:** restore the canonical face, blue eyes, cyan hair mass and
  length, paired ornaments, compact proportions, oversized gloves and boots,
  outfit construction, and six-part silhouette
- **generic modern anime girl:** restore Yuki's compact chibi construction and
  asset-specific shapes before decorative style; reduce background or camera
  complexity before relaxing identity
- **eyes lose identity in `BATTLE_INTENSE`:** reshape only the visible aperture;
  preserve blue iris color, eye scale and spacing, face, hair, and ornaments
- **camera feels stiff:** add shot-scale contrast, one restrained push-in, or a
  decisive cut; never constant orbiting or random handheld movement
- **transformation morphs:** restore locked pre- and post-states and bridge them
  only with effects plus one brief impact insert
- **held drawing crawls:** stabilize face, hair, ornaments, glove and boot
  shapes, contours, cel shadows, and grain; animate only the declared dominant
  motion channel
- **melee duplicates anatomy:** reduce to one readable strike and attack path;
  restore exact limb, glove, and boot counts before adding effects
