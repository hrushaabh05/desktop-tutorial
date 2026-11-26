# The Ash-Smeared Heart — animated short

A 3 min 44 s animated short adapted from the treatment *The Ash-Smeared Heart*. It's
rendered procedurally as 2D painterly animation, with strong single-source light,
parallax and particles. All of the picture and sound comes from code in this folder
(Python + numpy + Pillow, encoded with ffmpeg). No external assets are used.

**Output:** `the_ash_smeared_heart.mp4` (1280×720, 24 fps, H.264 + AAC stereo)

## Structure

| Time | Movement | What happens |
|---|---|---|
| 0:00 | Title | Embers rise through smoke. A temple bell sounds. |
| 0:12 | **I · The Rudraksha Worlds** | Pre-dawn at the Varanasi ghats: lapping water, an oil lamp, and a slow push through parallax mist to Kashinath on his tiger skin. Cut to an extreme close-up in profile as his lips move. A heartbeat turns into the damru. Smash cut to the cosmic void, where 21 rudraksha beads grow into wrinkled planets orbiting his translucent face. *"He doesn't count the beads. They count him."* They spiral into the Third Eye and flash. |
| 1:02 | **II · The Offering** | Graphic-novel panels: cupped hands holding a bilva leaf with glowing veins, the lingam under the banyan, and an overhead shot of the leaves being placed. Then milk pours in slow motion under god rays, and golden droplets splash. |
| 1:30 | **III · The Madness of the Village** | Villagers in cold blue with grotesque laughing masks point at Kashinath, who stands in a pillar of gold light. Close-up: he draws the tripundra in white-hot ash while the camera spins 360°. *"Pride, and fear, and 'mine,' and 'how.'"* The ash ignites in a fire that doesn't burn, then settles to grey. |
| 1:58 | **IV · The Tandava** | He sits motionless. His shadow on the temple wall changes from a seated figure into the four-armed cosmic dancer. Star trails spin and fall as golden sparks into his crown. The whole frame pulses between blue-black and amber with each damru strike as it speeds up, and ends on thunder. |
| 2:26 | **V · The Blue Throat** | His reflection in the river ripples and becomes Shiva: a silver crescent moon, the Ganga falling as liquid light, a third eye, and a throat glowing cobalt. Close-up: he touches his throat and the skin turns translucent blue over the swirling poison. *"Keep what burns, and still you'll stay."* |
| 2:50 | **VI · The Final Snow** | White, pale blue and silver only. Frost spreads across the floor in crystal mountain peaks (Kailash). When it reaches his feet, snow rises instead of falling and his body dissolves into it. Silence, then a single distant **Om**. |
| 3:10 | **VII · The Drop Returns** | Villagers open his door onto blinding white light. Only a glowing impression of his body remains in the ash. Then an aerial pull-back in Turner-style gold: the Ganges becomes a silver ribbon, the mountains become the outline of Shiva lying down, and river and mountain pulse together as one form. *हर हर महादेव — "Har Har Mahadev."* Conch and bells. Fade to black. |

## Sound

Everything is synthesized in `audio.py`:

* a tanpura drone (Pa–Sa–Sa–Sa) with jawari buzz
* sitar-style plucks with meend glides
* inharmonic temple bells
* a heartbeat that turns into the damru
* an accelerating Tandava rhythm, timed to the visual pulse through `timeline.py`
* water, milk pour, crowd murmur and formant-synthesized mocking laughter
* fire, thunder, a conch
* an additive-formant **Om** (A→U→M)

## Files

* `engine.py`: painterly helpers. Covers noise and brush textures, fast blur, a height-field "chiaroscuro" shader, masks, text, and tone mapping.
* `figures.py`: characters and props: the seated ascetic, faces (frontal and profile), villagers, the Nataraja shadow, a bilva leaf, the lingam and the lying figure.
* `scenes.py`: the seven movements.
* `timeline.py`: scene timings and beat maps shared by picture and sound.
* `audio.py`: score and sound design.
* `render.py`: renders across multiple processes and pipes frames to ffmpeg. `render.py stills <t…>` renders still frames for checking.
* `make.sh`: full rebuild.

## Rebuild

```bash
./make.sh          # ~25-30 min on 4 cores
```

## Notes on the adaptation

* The runtime is a tight 3:44 cut, not the 8–10 minutes in the treatment. Every beat is kept, and each scene's duration is set in `timeline.py`, so you can lengthen scenes there.
* The treatment calls for narration of "the original poem". That text wasn't provided, so the film uses only the treatment's on-screen lines. A recorded voiceover can be mixed in later over `build/audio.wav`.
