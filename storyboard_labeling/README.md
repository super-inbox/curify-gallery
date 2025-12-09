# 🎬 Video Storyboard Labeling Dataset

This repository contains our internal **video storyboard labeling experiments**, where we combine multimodal analysis (camera movement, shot types, objects, scene mood, motion intensity, and narrative structure) to produce detailed JSON storyboards for each video clip.

Each `.mp4` file in this directory has a corresponding machine-labeled JSON file capturing:
- Scene segmentation  
- Camera movement and shot types  
- Environment and mood attributes  
- Object and face detection  
- Motion intensity  
- Color palette extraction  
- Narrative-style scene descriptions  

This dataset is used for:
- Evaluating our **Curify Storyboard Labeler**
- Training downstream multimodal reasoning models
- Writing blog posts analyzing classical and modern video scenes

---

## 📁 Labeled Video–Storyboard Pairs

| Video (.mp4) | Storyboard (.json) |
|--------------|--------------------|
| `cope.mp4` | `cope_story.json` |
| *(Not a video)* | `old_story.json` |
| `pop.mp4` | `pop_story.json` |
| `sky.mp4` | `sky_story.json` |
| `small.mp4` | *(No JSON provided)* |
| `up.mp4` | *(JSON TBD)* |
| *(Not a video)* | `china_story.json` |
| *(Not a video)* | `hammer_story.json` |
| *(Not a video)* | `magic_story.json` |
| *(Not a video)* | `movie_story.json` |
| *(Not a video)* | `music_story.json` |
| *(Not a video)* | `youtube_story.json` |

---

## 🧪 Processing Pipeline

Our storyboard generator integrates multiple analyzers:

- `video_analyzer.py` — shot detection, color palette, scene segmentation  
- `camera_analyzer.py` / `advanced_camera_analyzer.py` — camera motion + shot type  
- `object_detector.py` — YOLO-based object recognition  
- `pose_analyzer.py` — human pose and motion  
- `face_processor.py` — face count, emotion, framing  
- `storyboard_generator.py` — merges all signals into a structured storyboard JSON  
- `ai_analyzer.py` — LLM-powered narrative enhancement  

---

## 📦 Directory Summary

```
.
├── *.mp4
├── *_story.json
├── *_story.txt
├── video_analyzer.py
├── camera_analyzer.py
├── pose_analyzer.py
├── object_detector.py
├── face_processor.py
├── storyboard_generator.py
├── ai_analyzer.py
└── requirements.txt
```

---

## ✨ Future Work

- Upload more high-value classical film scenes  
- Compare storyboard labels vs human editors  
- Blog series on cinematic AI understanding  
- Demo for scene-by-scene breakdown
