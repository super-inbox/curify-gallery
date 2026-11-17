# Production record

## Chinese Silhouettes revision v2 — local review

Regenerated with MiniMax-Hailuo-02 first/last-frame control: Tang-to-Song (6s), Song-to-modern (first 4s), then its final 2s eased to a 5s hero hold. The separate modern-hold take was rejected because it introduced a hand wave. Removed flash montage, mismatched independent gestures and the return to the first outfit. Fixed camera; joins use the same authored identity/pose. Existing 3s CTA and soundtrack retained. Updated the original video path in place and retained v1 in the production workspace. Captions consolidated into the parent posting files. The baseline notes below describe v1 where they differ.



## References and creative interpretation

- Supplied local reference: `cultural_videos/costume_tryon/fashion_Renaissance.mp4` (58.33 seconds). Reviewed extracted frames: dark-background editorial portraits, turns, fabric changes, and era labels. Our Time Machine short uses a new original character and three looks: Renaissance-inspired, Art Deco, future tailoring.
- [NANYA reference reel](https://www.instagram.com/p/DeHK5jMTCm6/): visible caption describes sarung styled with kebaya, a work shirt, and a batik jacket. Caption and comments were readable; playback redirected to a login gate. We used that documented styling idea, not its footage, soundtrack, brand or likeness. No affiliation is implied.
- Curify costume library reviewed: `daily_inspirations/Mar_23/template-costume-tang-dynasty-female-wedding.jpg` and `daily_inspirations/Mar_24/template-costume-song-dynasty-female-wedding.jpg`. Their layered silhouette language informs the Chinese-inspired concept. The new outfits are explicitly contemporary interpretations, not reconstructions or copies of those wedding ensembles.

## Image and motion generation

Nine new first frames were produced with the built-in imagegen tool: three original adult models, then two outfit variants per model. Same face, body, framing and setting were retained within each sequence. No real customer/model reference was used for the new shorts.

Motion uses the existing `curify-studio/dev/jayw/video_pipelines/costume_story_video/animate.py` MiniMax request/poll/download helpers: `MiniMax-Hailuo-2.3`, image-to-video, 1080P, six seconds per look. Motion prompts request restrained head/shoulder turns, natural weight shifts or sleeve presentation, and stable garments/identity. The final films contain generated motion, not still-image slideshows.

The editing workflow, prompt specification, first frames, raw clips, generation state, end-card master and QA outputs are retained in the production workspace under `output/fashion-culture-20261010/`.

## Ending

Adapted from `CardNarrationPipeline._reading_cta` in `curify_background/app/pipelines/card_narration_pipeline.py`. Preserves the purple vertical gradient, official Curify icon, large Curify wordmark, bilingual slogan, purple rounded CTA pill and website. Layout is refitted to 9:16. Reading copy is replaced with:

- Batch fashion try-on
- 一张照片 · 百变穿搭
- Try your next look ›
- curify-ai.com

Three-second duration. The new shorts carry music through the end card with a fade. Feitian's original 30-second music track is preserved; its appended card is silent, matching the reading pipeline's post-narration CTA behavior.

## Edit and music sources

New shorts: 1.2-second three-look preview, three 4.2-second outfit sections, 1.2-second first-look callback with viewer-choice text, and three-second CTA = 18 seconds.

Existing Curify music-library tracks (source begins at 8 seconds):

- Time Machine: `alexgrohl-sweet-life-luxury-chill-438146.mp3`
- Sarong: `crab_audio-elegant-style-301129.mp3`
- Chinese silhouettes: `kaazoom-from-gentle-stream-to-the-city-streets-modern-chinese-music-434753.mp3`

Stereo AAC 192 kbps; new-short audio normalized toward -16 LUFS, -1.5 dBTP with final fade. Feitian keeps its existing mixed soundtrack. No audio from either inspiration reference is reused.

## Publication status

All four entries are drafts; no social posting or outreach occurred. The website CTA on Chinese captions is explicitly requested for this new batch. The historical no-link copy elsewhere in the parent thread was not rewritten.

## Quality checks

All nine generated clips were inspected at multiple motion points for face consistency, garment continuity and usable movement. Finished edits were inspected as contact sheets; opening captions were moved lower to keep faces clear. All four exports passed a full FFmpeg decode, expected duration, 1080 × 1920 dimensions, 30 fps and AAC-audio checks. The exact output metadata is in `media-report.json`; overview frames are in `previews/`.
