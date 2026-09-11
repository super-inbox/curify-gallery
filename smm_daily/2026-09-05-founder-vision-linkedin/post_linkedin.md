# LinkedIn · Founder vision — 1 post (2026-09-05)

**Format:** native vertical video upload (4:5, 1080×1350, 67 s, burned-in captions).
No link in the post body — LinkedIn throttles link-outs. CTA in the first comment.

**Engine:** positioning / authority. The KPI is inbound conversation and profile
visits, not reach.

**Drift check:** ✅ Founder-voice macro thesis on the personal account — same lane
as the Jay RedNote theses, not a Curify feature announcement. The video deliberately
never says "Production AI is the cash cow"; externally it reads as *where we solve
real, high-volume commercial work today*, which lands stronger anyway.

---

## Asset

`curify-vision-linkedin.mp4` — 4:5, 1080×1350, 67.6 s, h264 + AAC, captions burned in.
Source talking head: `curify-frontend/raw/b-roll-09-05/human-video.mp4`.
`curify-vision-linkedin-nomusic.mp4` is the same cut with the music bed removed.

B-roll is all own-source / own-output (workflow demos, retouching blueprint, layered
PSD, agent + evaluation posters, ASL demo, `daily_inspirations` archive) — per
`curify-studio/docs/asset-authority-distribution-inventory.md`, *自有素材，自有输出 → ✅ 立即可用*.
No Labubu / Cinnamoroll print assets appear.

**Master asset.** The three chapters are cut on clean boundaries, so the 15–20 s
single-layer versions can be lifted without re-editing:

| Cutdown | In → out | Covers |
|---|---|---|
| Production AI | 7.3 s → 21.9 s | chapter card + 4 production beats |
| Workspace Intelligence | 24.7 s → 37.3 s | chapter card + design system, assets, inspiration archive |
| Frontier Research | 42.2 s → 52.9 s | chapter card + agents, evaluation, search, ASL |

---

## Post copy

After a year of building Curify, one thing is clear: AI design isn't about generating more images. It's about changing how visual work gets done.

Three layers, and they stack.

𝗣𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻 𝗔𝗜 — repetitive visual work becomes reliable, scalable workflows. Studio retouching, product imagery, merch and IP. This is where we solve real, high-volume commercial work today.

𝗪𝗼𝗿𝗸𝘀𝗽𝗮𝗰𝗲 𝗜𝗻𝘁𝗲𝗹𝗹𝗶𝗴𝗲𝗻𝗰𝗲 — that work should compound. A design system personalized to your organization, assets you can actually reuse, inspiration you can still find months after you saw it.

𝗙𝗿𝗼𝗻𝘁𝗶𝗲𝗿 𝗥𝗲𝘀𝗲𝗮𝗿𝗰𝗵 — real production problems drive it: design agents, evaluation, multimodal search, and new interfaces like our sign-language work.

The loop matters more than the layers. Production puts us inside real workflows, which earns customers, data and honest evaluation criteria. That turns one-off output into reusable organizational intelligence. And that is what makes the research worth doing — which feeds straight back into production.

Curify is where visual AI moves from generation to production, from isolated assets to reusable intelligence, and from today's workflows to what comes next.

60 seconds, below 👇

---

## Short variant

For X, and for the RedNote / 视频号 re-post where the long build doesn't land:

> A year into building Curify, the vision finally reads in one line: visual AI has to move from **generation** to **production**.
>
> Production AI solves the repetitive commercial work today. Workspace Intelligence turns that work into a design system and assets you can reuse. Frontier Research — agents, evaluation, multimodal search, ASL — is driven by the production problems the first layer surfaces.
>
> Three layers, one loop. 60 seconds ↓

---

## First comment (CTA)

> If you're running high-volume visual production — e-commerce listings, retouching,
> merch and IP — and want to compare notes on where the workflow actually breaks,
> I'm happy to trade findings. curify-ai.com

---

## Build

Reproducible from the raw drop — `gfx.py` (overlays, mosaic, ladder), `captions.py`
(Scribe word timings → ASS), `edit.py` (19 shots → concat → burn captions → mux).
`python3 gfx.py && python3 captions.py scribe.json captions.ass && python3 edit.py`.

- **Reframe.** The phone original is 9:16 with the subject low and ~40 % dead ceiling.
  Every human shot is cropped `720×900` and scaled to 1080×1350; chapter beats sit
  85 px higher so the layer graphic has clean ceiling to live on.
- **Captions.** Transcribed with ElevenLabs Scribe (the same path `curify_background`
  uses), broken into lines by shortest-path search that prefers breaking on pauses
  and punctuation rather than mid-phrase.
- **Structure.** 18.6 s of pure talking head + 8.2 s of talking head under the three
  chapter cards ≈ 27 s on camera, against ~30 s of product B-roll and the 11 s
  ladder-and-logo finale.
- **Music.** `assets/music/monume-modern-futuristic-technology-519250.mp3`, normalized
  then −16 dB and side-chain ducked under the voice, so it only swells over the end
  card. Integrated loudness −17.3 LUFS. Drop it by shipping the `-nomusic` file.
