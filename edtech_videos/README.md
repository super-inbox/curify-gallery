# edtech_videos

Narrated educational video assets. Merged 2026-09-23 from the former
`ed_narration/` (which is now gone — everything moved here, nothing dropped:
161 files in, 161 files out).

Organised by **content line → batch date → asset type**, so a batch's rendered
videos sit next to the narration text they were read from.

```
hsk-reading/            bilingual HSK reading cards, zh female narration over a slow scroll
  2026-07-24-folk-tales/    10 videos — fairy tales / 成语 fables
  2026-09-06-daily-life/    20 videos — the pivot to daily-life scenes
  2026-09-23-daily-life/    20 videos — read-along pace (-25%, 400ms sentence breaks)
  2026-10-10-world-and-daily-life/ 20 videos — approved watercolor reading template
  2026-11-07-autumn-and-weekend/   10 videos — Halloween, red leaves, beach and everyday scenes
science-explainers/     EN narrated science cards with burned-in subtitles
  2026-05-26/               14 videos + srt/ass
product-demos/          ⚠️ NOT edtech — see below
  2026-06-02/               13 videos + 6 clips
_reference/             ⚠️ third-party material — see below
```

Each batch folder holds `video/`, `narration/` (the .txt read aloud, plus .wav
where the synthesised audio was kept) and, where applicable, `subtitles/`.

## Why HSK is the line that matters

TikTok like counts on the published HSK read-alongs split by **level and
situation**, not story quality — HSK2 everyday transactions beat the one HSK1
card ~6x (去买东西 721, 看医生 627, 我的家 570 vs 在学校的一天 96). The
2026-07-24 batch is folk tales, the category nobody measured; 09-06 and 09-23
are the correction. Keep weighting new batches to HSK2–3 transactional daily
life.

Source of truth for the HSK cards is `curify-frontend`:
`scripts/configs/hsk_daily_life_<date>.json` (hand-authored passages + verified
pinyin) → `scripts/generate_hsk_reading_cards.cjs` for the posters →
`curify_background/scripts/render_hsk_reading_videos.py` for these videos.
Never let a model compose the Chinese: see `docs/pinyin-generation-guide.md`.

## Two things that need a decision

**`product-demos/` is not educational.** It is the old `ed_narration/videos_June_2/`:
abtasty, t-shirt, fashion, travel-pack, bejing, cable, sign-look — ecommerce and
marketing experiments at assorted aspect ratios (230x89, 350x350, 4800x3584).
It was merged here only because it lived inside `ed_narration/`. It probably
belongs in `Marketing_media/` or `ecommerce_ad_videos/`. It is also most of the
weight — ~396MB of the folder. Two files in it are broken artifacts rather than
deliverables: `two_combined.mp4` (47MB, will not probe — no readable streams)
and `travel_pack_separate.temp.mp4` (44MB, a `.temp` render with no audio).

**`_reference/` is somebody else's work.** `sciencebyansh-avalanche-1080x1920.mp4`
carries the watermarks `@DEADLYKALESH` and `sciencebyansh`. It was sitting
unlabelled in `edtech_videos/` as `s9xg41HBqOOVfKfn.mp4`. It is saved reference
material, not a Curify deliverable — do not publish or reuse it.

October and November 2026 watercolor batches retain their approved card references, exact generation prompts, source passages and QA evidence. Cards use the built-in image generator with verbatim authored Chinese and pinyin; videos use `curify-frontend/scripts/render_hsk_readalong.py` with slow female Mandarin narration. Open each batch’s `index.html` to review its cards and videos.
