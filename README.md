# 🎬 Curify Video Gallery

This repo showcases example projects, ad creatives, component effects, and product demos generated using different pipelines (ComfyUI, Python scripts, or direct video generation models).  
Each row links to inputs, methods, and output previews.

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

## 🛠 Notes
- Methods vary: some projects use **ComfyUI workflows**, some use **Python scripts**, and others use **prompt-based video generation models**.  
- Outputs may be stored in `outputs/` folders (consider Git LFS if videos are large).  
- Each project folder includes its own `README.md` with more details.
