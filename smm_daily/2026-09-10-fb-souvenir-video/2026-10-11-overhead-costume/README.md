# Overhead costume transitions · 2026-10-11

**Queue:** Q1 → Q2 → Q3 after the previously scheduled fashion/culture batch. All three are **pending review and scheduling** on Instagram, Facebook, RedNote and Kuaishou. No dates or live posts are recorded.

| Queue | Video | Looks | Format |
|---|---|---|---|
| Q1 | [Rollover Wardrobe · Chinese Embroidery](../../../cultural_videos/costume_tryon/2026-10-11-overhead-costume/rollover-chinese-embroidery-curify.mp4) | MIAO-INSPIRED → BAI-INSPIRED → YI-INSPIRED | 1080 × 1920 · 30fps · 21s |
| Q2 | [Fan Sweep · Asian Silhouettes](../../../cultural_videos/costume_tryon/2026-10-11-overhead-costume/fan-sweep-asian-silhouettes-curify.mp4) | KIMONO-INSPIRED → HANBOK-INSPIRED → SARI-INSPIRED | 1080 × 1920 · 30fps · 15s |
| Q3 | [Glowstick Wardrobe · World Textiles](../../../cultural_videos/costume_tryon/2026-10-11-overhead-costume/glowstick-world-textiles-curify.mp4) | VYSHYVANKA-INSPIRED → TEHUANTEPEC-INSPIRED → ATLAS-INSPIRED | 1080 × 1920 · 30fps · 15s |

Captions are consolidated in [English FB / Instagram copy](../posts_fb.md) and [中文小红书 / 快手文案](../posts_rednote_kuaishou.md).

## Production

Original adult models, completely flat reclining poses and locked overhead cameras. Template images guide garment motifs; the output is an AI fashion interpretation, not a documentary reconstruction. Ukrainian / Mexican / Uzbek looks retain their distinct named references; the atlas robe is interpreted as contemporary womenswear.

Nine controlled stills generated with imagegen. First/last-frame pairs rendered with MiniMax-Hailuo-02 (1080P, 6s each), two transitions per video. Revision v2: the Chinese embroidery video uses full-body side rolls to reveal each new outfit; the Asian silhouettes video uses one slim cream-coloured blade composited close to the lens, with its pivot outside the frame. The world-textile video retains its original glowstick transitions. The sari still was corrected for an extra hand before animation. No reference video footage or audio was reused.

Original world-textile edit: two retimed transitions (brief introduction, accelerated foreground sweep and slowed final reveal), plus a 10-frame final-pose hold, total 12s; then the identical 3s Curify ending from the previous batch. Optical-flow interpolation smooths the final reveal. Final video is exactly 450 frames at 30fps. Music from the gallery music library, normalized to -16 LUFS with a fade-out. English / Chinese labels burned in. CTA: **Batch fashion try-on · curify-ai.com**.

Source details and generation prompts: [motion-prompts.json](motion-prompts.json), [manifest.json](manifest.json), [template-sources.json](template-sources.json). Verification: [media-report.json](media-report.json).


## Revision v2 · 2026-10-12 · rollover and slim cream blade

Replaced the Chinese embroidery and Asian silhouettes MP4s **in place**, retaining their filenames and queue positions. The v2 Chinese filename retained the original prefix; revision v3 below replaces and renames it. China: two controlled MiniMax-Hailuo-02 side-roll clips, with the Bai take also played in reverse for the return, matched outfit cuts at aligned side poses, then a short Yi front-view hero shot. The requested final Yi return generation failed and its retry hit insufficient API balance; no failed take is used. Asia: three stable breathing portraits under a single slim cream blade; a tracked opaque matte reveals the next outfit behind its sweep. Both bodies are exactly 12s, followed by the unchanged 90-frame / 3s Curify ending. Existing music and CTA retained. The world-textile video is unchanged. Previous versions are backed up in the production workspace. [Revised prompts](motion-prompts-v2.json).

## Revision v3 · 2026-10-12 · complete rollover

Chinese embroidery only: replaced the half-roll edit with complete forward-played rolls, then outfit cuts after the rotation. Generated fresh takes with Veo 3.1 on pale ivory bedding; rejected morphing and incomplete-roll takes. Two 8s rolls, a 2s Yi reveal and the unchanged 3s Curify ending: 21s, 630 frames at 30fps. Renamed to `rollover-chinese-embroidery-curify.mp4`; captions and queue links updated. Fan and world-textile videos unchanged. Production references and prompts: [revision-v3](revision-v3/).
