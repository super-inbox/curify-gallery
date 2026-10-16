# Curify Gallery

Source media, generated assets and pipeline notes for **[Curify AI](https://www.curify-ai.com)** — an AI-powered video & visual-content platform. The repo holds **videos, images and the SMM threads that distribute them**: example projects, ad creatives, component effects, product demos and the per-channel post copy behind them.
Each row links to inputs, methods, and output previews.

The shipped, user-facing versions of these capabilities live on the product:

- 🎬 [Video Dubbing](https://www.curify-ai.com/tools/video-dubbing) — multilingual video translation with lip-sync
- 📝 [Bilingual Subtitles](https://www.curify-ai.com/tools/bilingual-subtitles) — dual-language subtitle generation
- 🎨 [Style Transfer](https://www.curify-ai.com/tools/style-transfer) — Ghibli / Pixar / anime restyle of live-action video
- 📚 [Manga Translation](https://www.curify-ai.com/tools/manga-translation) — comic-panel text translation with layout preserved
- ✨ [Video Enhance](https://www.curify-ai.com/tools/video-enhance) — restore archival / low-res footage

---

## 📖 Gallery Index

| Project Name             | Input(s)                         | Theme / Goal                         | Method              | Output Preview |
|--------------------------|-----------------------------------|---------------------------------------|---------------------|----------------|
| **E-comm Ad · Fabric** ⭐ | Text-to-video prompt (6 timecoded beats) | Apparel / textile — cotton boll → finished shirt | MiniMax H3 | [▶️ Video](ecommerce_ad_videos/fabric_ad/fabric_ad-watermarked.mp4) |
| **E-comm Ad · Matcha** ⭐ | Product brief | Food & beverage, fully unbranded | Text-to-video | [▶️ Video](ecommerce_ad_videos/matcha_drink/matcha_drink-watermarked.mp4) |
| **E-comm Ad · Office Chair** ⭐ | Product brief + feature list | Hard goods — airflow viz, HUD adjust readout | Text-to-video | [▶️ Video](ecommerce_ad_videos/rotation_chair/rotation_chair-watermarked.mp4) |
| **E-comm Ad · Beauty Cream** | 10-scene brief | Skincare hero — ⛔ **internal only**, third-party mark on screen | Text-to-video | [▶️ Video](ecommerce_ad_videos/beauty_cream/beauty_cream-watermarked.mp4) |
| **Content Search · E-commerce** | Search query → generated result | Product listing creative from a query | Query → generation | [🖼️ Poster](content-search-explainer/curify-query-ecomm-poster.jpg) · `curify-query-ecomm.mp4` |
| **Content Search · History** | Search query → generated result | Historical explainer from a query | Query → generation | [🖼️ Poster](content-search-explainer/curify-query-history-poster.jpg) · `curify-query-history.mp4` |
| **Content Search · Kids** | Search query → generated result | Kid-facing how-to card set | Query → generation | [🖼️ Poster](content-search-explainer/curify-query-kids-poster.jpg) · `curify-query-kids.mp4` |
| **Content Search · Music** | Search query → generated result | Music-genre era infographic | Query → generation | [🖼️ Poster](content-search-explainer/curify-query-music-poster.jpg) · `curify-query-music.mp4` |
| **Content Search · World Cup** | Search query → generated result | Player comparison card — ⚠️ **see clearance note below** | Query → generation | [🖼️ Poster](content-search-explainer/curify-query-WC-poster.jpg) · `curify-query-WC.mp4` |
| **SMM · E-commerce** | Ad videos, teardown stills, workflow demos | Seller-side demand: apparel, accessories, hard goods | FB groups · 小红书 / 快手 | [FB](smm_daily/2026-09-01-ecommerce/posts_fb.md) · [小红书/快手](smm_daily/2026-09-01-ecommerce/posts_rednote_kuaishou.md) · [README](smm_daily/2026-09-01-ecommerce/README.md) |
| **SMM · Retouching** | Before/after sheets, method cards | Studio-side: wedding, portrait, children, real estate | FB groups · 小红书 | [FB](smm_daily/2026-09-01-retouching/posts_fb.md) · [小红书](smm_daily/2026-09-01-retouching/posts_rednote.md) |
| **SMM · Souvenir Video** | Destination films (Bali, Dubai, Granada, Kyoto, 滕王阁) | Travel keepsake sold as a photo-package add-on | FB groups · 小红书 / 快手 | [FB](smm_daily/2026-09-10-fb-souvenir-video/posts_fb.md) · [小红书/快手](smm_daily/2026-09-10-fb-souvenir-video/posts_rednote_kuaishou.md) · [README](smm_daily/2026-09-10-fb-souvenir-video/README.md) |
| **Museum Intro**         | Script + reference images         | Cultural introduction video           | ComfyUI workflow    | [▶️ Video](museum_intro/outputs/museum_intro.mp4) |
| **Car Ad**               | Car images + text prompt          | Automotive ad creative                | VideoGen model      | [▶️ Video](ad_videos/cars/outputs/car_ad.mp4) |
| **Popmart Ad**           | POPMART character images + script | Brand promo video                     | Python montage      | [▶️ Video](ad_videos/popmart/outputs/popmart_ad.mp4) |
| **Transitions**          | Stock footage + scene markers     | Showcase video transitions            | Python script       | [▶️ Video](effects/transitions/outputs/transitions_demo.mp4) |
| **Logo Effect**          | Curify logo image                 | Logo → dynamic animation              | ComfyUI + AfterFX   | [▶️ Video](effects/logo_effects/outputs/logo_demo.mp4) |
| **Subtitle Removal**     | Video with hard-coded subtitles   | Clean video without subtitles         | Python + Inpainting | [▶️ Video](product_demos/subtitle_removal/outputs/demo.mp4) |
| **Video Translation**    | Original video + target language  | Multilingual dubbed video             | Whisper + XTTS      | [▶️ Video](product_demos/video_translation/outputs/demo.mp4) |
| **Templated Generation** | Script + assets                   | Template-driven creative ad/story     | ComfyUI + Prompts   | [▶️ Video](product_demos/templated_generation/outputs/demo.mp4) |
| **Manga Translation**    | Manga image(s) in source language | Manga localized into target language  | OCR + LLM + Overlay | [▶️ Video](product_demos/manga_translation/outputs/demo.mp4) |

⭐ **Watermarked and committed.** The four e-commerce ad videos carry the house tiled
watermark (slanted −30°, params taken verbatim from `curify-frontend/scripts/lib/watermark.cjs`)
and are the only videos in this repo checked into git — everything else is local media that the
links below point at by path. Rebuild with `ecommerce_ad_videos/watermark_videos.py`.

🖼️ **Content-search rows link a committed poster, not the mp4.** The clips run 3–51 MB and stay
local; the poster is a frame from each and is checked in, so the preview resolves on GitHub.

⚠️ **Clearance is not uniform across this table.**
- `beauty_cream` shows a third-party skincare mark — ⛔ internal decks and sales calls only,
  never a public feed. The watermark does not change that.
- The World Cup card carries **visible Nike, Spotify, PUMA and Etihad marks plus two
  identifiable players**. Same class as the standing red line on third-party brands in outbound
  creative — treat as internal until cleared.
- The music infographic shows small streaming-platform icons; low risk, but it is a
  third-party mark in frame.
- Per-asset clearance for the e-commerce set lives in
  [`smm_daily/2026-09-01-ecommerce/index.json`](smm_daily/2026-09-01-ecommerce/index.json).

⚠️ **The nine rows below this note are stale** — `museum_intro/`, `ad_videos/cars/`,
`effects/` and `product_demos/` do not exist in the repo, so those links 404. Left in place
rather than silently deleted; they need either restoring or removing as a separate pass.

---

## 📂 Repo Structure

```
gallery/
│
├── museum_intro/
│   ├── inputs/
│   ├── outputs/
│   ├── method.md
│   └── README.md
│
├── ad_videos/
│   ├── cars/
│   ├── popmart/
│
├── effects/
│   ├── transitions/
│   ├── logo_effects/
│
├── product_demos/
│   ├── subtitle_removal/
│   ├── video_translation/
│   ├── templated_generation/
│   ├── manga_translation/
│
└── README.md   # this file
```

---

## 📁 Daily Inspirations — curated docs

`daily_inspirations/` holds the daily content-research logs (dated `<Mon>_<DD>/` folders, each with a `README.md` + reference images). The substantive analysis/research documents that were scattered across those date folders are collected into two category directories — each moved doc is prefixed with its source date folder (e.g. `Jul_4__…`) for provenance:

- **`daily_inspirations/_tooling-survey-diagnose/`** — tooling surveys, competitor comparisons, and feature/accuracy diagnostics. Includes the Miguo/Vizcom/Sketch-To software test (`软件测试`), Curify vs Google NotebookLM, Reddit search comparison (`reddit搜索对比`), Curify-vs-Pinterest coverage (`5.21`), template match-accuracy diagnosis (`匹配`), ComfyUI, and the image2image capability survey (`图生图`).
- **`daily_inspirations/_merchandising-case-industry/`** — merchandising cases + 文创/POD industry research. Includes the 文创工厂 AI output/layout specs (`文创工厂…出图与排版规范`), 文创 collection & analysis (`文创搜集` / `文创分析`), plus two research batches: `Jun_5-merch-brand-portfolios/` (10 brand stories/portfolios) and `Jun_7-factory-oem/` (16 OEM/ODM manufacturer notes).

Docs intentionally left in their date folders (not in either category): template/prompt JSON dumps (`nano-templates.json*.docx`, `inspiration card*.docx`, prompt-template content), SEO bridge articles (`SEO桥接*.docx`), blogs/guides, the SMM account breakdown (`账号全内容拆解`), the education-flashcard portfolio, and the `May_31/` SEO keyword-seed batch.

---

## 🛠 Notes
- Methods vary: some projects use **ComfyUI workflows**, some use **Python scripts**, and others use **prompt-based video generation models**.  
- Outputs may be stored in `outputs/` folders (consider Git LFS if videos are large).  
- Each project folder includes its own `README.md` with more details.

## About Curify

[Curify AI](https://curify-ai.com) is an applied-AI company building the **deterministic production layer above foundation models** — reliable, traceable, enterprise-grade pipelines, not a prompt wrapper. Our products span two lines:

- **Enterprise AI** — an industrial-grade multimodal content engine + enterprise **document intelligence** (RAG with mandatory source citation, structured extraction, on-premise; *deterministic · traceable · data stays yours*).
- **AI-Native Product** — creator / SMB-facing generation at [curify-ai.com](https://curify-ai.com): structured data & long-tail keywords → thousands of on-brand visual assets, multilingual video, and one-click design tools.

**Links** · Website: [curify-ai.com](https://curify-ai.com) · Mentorship (founder, Jay Wang): [mentorcruise.com/mentor/jaywang](https://mentorcruise.com/mentor/jaywang/)
