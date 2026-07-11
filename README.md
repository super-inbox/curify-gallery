# 🎬 Curify Video Gallery

Source media + pipeline notes for the demos used across **[Curify AI](https://www.curify-ai.com)** — an AI-powered video & visual-content platform. This repo showcases example projects, ad creatives, component effects, and product demos generated through different pipelines (ComfyUI, Python scripts, or direct video generation models).
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
| **Museum Intro**         | Script + reference images         | Cultural introduction video           | ComfyUI workflow    | [▶️ Video](museum_intro/outputs/museum_intro.mp4) |
| **Car Ad**               | Car images + text prompt          | Automotive ad creative                | VideoGen model      | [▶️ Video](ad_videos/cars/outputs/car_ad.mp4) |
| **Popmart Ad**           | POPMART character images + script | Brand promo video                     | Python montage      | [▶️ Video](ad_videos/popmart/outputs/popmart_ad.mp4) |
| **Transitions**          | Stock footage + scene markers     | Showcase video transitions            | Python script       | [▶️ Video](effects/transitions/outputs/transitions_demo.mp4) |
| **Logo Effect**          | Curify logo image                 | Logo → dynamic animation              | ComfyUI + AfterFX   | [▶️ Video](effects/logo_effects/outputs/logo_demo.mp4) |
| **Subtitle Removal**     | Video with hard-coded subtitles   | Clean video without subtitles         | Python + Inpainting | [▶️ Video](product_demos/subtitle_removal/outputs/demo.mp4) |
| **Video Translation**    | Original video + target language  | Multilingual dubbed video             | Whisper + XTTS      | [▶️ Video](product_demos/video_translation/outputs/demo.mp4) |
| **Templated Generation** | Script + assets                   | Template-driven creative ad/story     | ComfyUI + Prompts   | [▶️ Video](product_demos/templated_generation/outputs/demo.mp4) |
| **Manga Translation**    | Manga image(s) in source language | Manga localized into target language  | OCR + LLM + Overlay | [▶️ Video](product_demos/manga_translation/outputs/demo.mp4) |

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
