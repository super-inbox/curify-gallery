# E-commerce — FB Groups + 快手, one folder (2026-09-01 … 09-06)

_Consolidated 2026-09-11 from `2026-09-01-fb-ecommerce/` and
`2026-09-06-ecommerce-ad-videos/`. Same buyer, same four groups, same cadence rule,
same CTA gates, same stop rule — they were two folders because they were written a
week apart, not because they were two campaigns._

| File | What |
|---|---|
| **`posts_fb.md`** | Every Facebook post — 2 workflow posts (W1–W2) + 5 ad-video posts |
| **`posts_kuaishou.md`** | 快手 —— 5 条中文文案，和 FB 是不同的语气，不是翻译 |
| `index.json` | machine-readable index of `curify-gallery/ecommerce_ad_videos` |
| `prompts/` | prompt provenance + the Minimax H3 series |
| `w2-one-photo-nine-variants.jpg` | the only image in this folder — W2's asset |

**This file holds what governs both channels.** Clearance, the group list, cadence
and the stop rule are not per-channel and are not repeated in the two post files.

---

## Two asset families, one buyer

| | Source | Where they live | Posts |
|---|---|---|---|
| **Workflow** | `curify-gallery/ecommerce_workflow/` — 29 videos + the nine-variant still | 29 × 1080×1920 h264+AAC | W1, W2 |
| **Ad videos** | `curify-gallery/ecommerce_ad_videos/` — 10 videos | see `index.json` | 5 shippable, by `id` |

Neither set is in this folder — only `w2-one-photo-nine-variants.jpg` is, and that is
itself a copy. **Videos are a manual native upload from the local file**; only 5 of the
29 workflow videos are on CDN/YouTube and none are in the autopost pool
(`project_fb_follower_growth.md`).

⚠️ `w2-one-photo-nine-variants.jpg` is byte-identical to
`client_VC_portfolio/ad-variants-demo-09-10/_one-to-nine.jpg` (the original) and to
`smm_daily/2026-08-21-xianyu-services/H-one-sku-nine-variants.jpg` (the 闲鱼/淘宝 copy).
**Leave the portfolio original where it is** —
`curify-studio/gtm_tools/batch_marketing_agency_2026-09-10.json` attaches it by
absolute path. The three copies are deliberate: three platforms, three folders that
each have to stand alone.

---

## Clearance — read before scheduling anything

`asset-authority-distribution-inventory.md` §3 already draws this line: **自有素材，自有输出
→ ✅ 立即可用** vs **第三方版权 → ❌ 不可公开**, the same rule that keeps Labubu and the
Chaplin/Forrest Gump translation demos permanently off the public feed. Applying it here:

| `id` | Video | On-screen brand | Verdict |
|---|---|---|---|
| `angryalert` | `angryAlert/AngryAlert_vertical.mp4` (+ landscape cut) | Curify | ✅ **ship** |
| `matcha_drink` | `matcha_drink.mp4` | none | ✅ **ship** |
| `rotation_chair` | `rotation_chair.mp4` | none | ✅ **ship** |
| `kungfu_sf` | `redbull/kungfu_redbull_SF.mp4` | Curify | ✅ **ship** — ⚠️ rename file first |
| `model_standing` | `model-standing.mp4` | none | ⚠️ **check** — likeness |
| `oilight` | `oilight final.mp4` | OILIGHT™ | ⚠️ **check** — client brand + live footage |
| `corona_sunrise` | `corona/Mountain_Sunrise_Beer_Climax.mp4` | **Corona** | ⛔ **internal** |
| `mooncakes` | `starbucks/mooncakes.mp4` | **Starbucks siren** | ⛔ **internal** |
| `molly_forest` | `popmart/Molly_walks_into_a_cozy_forest.mp4` | **POPMART + Snow White** | ⛔ **internal** |
| `beauty_cream` | `beauty_cream.mp4` | **POND'S** | ⛔ **internal** |

**The four ⛔ rows are spec ads for live trademarks** — AB InBev, Starbucks, POP MART
(plus a Disney character design), Unilever. They are genuinely good work and they are
exactly right for an investor deck or a sales call, where the exposure is low. On a
public feed they are someone else's mark on our marketing, and the beer one additionally
trips alcohol ad-policy on both FB and Kuaishou.

**They are not wasted — they are re-renderable.** The craft is in the prompt, not the
logo. `prompts/beauty_cream.json` carries a de-branded re-render of `beauty_cream` under a house
name; the same one-line swap fixes the other three. That is the unlock, and it costs one
generation each.

**The two ⚠️ rows, one question each:**
- **`model_standing`** — photoreal human face. If the render used a pose or
  likeness reference of a real model, the output carries that person's face. Confirm the
  reference was synthetic; if it wasn't, re-render before it goes anywhere external.
- **`oilight`** — OILIGHT™ reads as a real client brand, and the opening
  desert shot is live-action with an identifiable person (licensed stock, or not ours).
  Needs the client's written OK *and* the footage provenance.

**`kungfu_sf` rename:** no energy-drink mark appears in any sampled frame — the brand is in the
*filename only*. Rename to `kungfu_sf_energy_spec.mp4` so the asset name stops implying
a tie-in that the footage doesn't make.

---

⚠️ **The numbering changed on 2026-09-11.** Videos are keyed by the `id` in `index.json` now, not by row number — the old clearance table and the old §3 were numbered differently from each other, so `#3` meant two different videos depending on which table you read.

---

## Channel mechanics

| | **FB — Groups, not the Page** | **Kuaishou 快手** |
|---|---|---|
| Why | Page identity is locked to Sinosphere culture edutainment. An ad-craft video in the Page feed is Position Drift. Groups don't carry that risk — same call as the 09-01 e-commerce post. | New surface, no positioning history to protect. Audience is 实体商家 / 电商卖家 / 工厂老板 — the people who actually buy batch ad production. |
| Format | **Native video upload**, single video, never a carousel. No link in the post body — FB throttles link-outs; a native upload is not one. | 竖屏 9:16 原生上传。前 3 秒必须是成品画面，不要 logo 开场。 |
| Language | English | 中文，口语，别端着 |
| CTA | **First comment**, never the body | 主页 + 私信；口播带一次官网 |
| KPI | replies, not reach | 私信数，不是播放量 |
| Drift check | ✅ group-scoped, off-Page | ✅ new account |

**Groups** (from the 09-01 series): **B1** `105108073643190` E-commerce product
photography (5.2K, ⚠️ has an explicit anti-spam ban rule) · **B2** `765595303494969`
Product Photographer USA (1.3K) · **B3** `313105103563214` Apparels/Fashion Sell & Buy
(5.0K) · **B4** `1212659302803905` Online E-Commerce sellers solution (6.9K).

**Cadence:** one post per group per ~3 days. Never the same video into two groups the
same day. B1 last — it's the ban-rule group, and a video post reads more promotional
than a teardown does.

**Kuaishou orientation note:** `kungfu_sf` and the angryAlert landscape cut are 16:9.
Kuaishou is a vertical feed — use `AngryAlert_vertical.mp4` there, and either recut
`kungfu_sf` to 9:16 or hold it for FB only.

**The CTA, both platforms** — self-serve `curify-ai.com/tools/product-video` (verified
live, renders the real inline generate surface, not a waitlist card), batch/contact
`curify-ai.com/contact` (verified live).

---

## Suggested order — ad videos

| Slot | Video | Where |
|---|---|---|
| 1 | `rotation_chair` | B4 — strongest B2B proof, clearest batch pull |
| 2 | `matcha_drink` | Kuaishou — first post, zero risk |
| 3 | `angryAlert` (landscape) | B2 |
| 4 | `rotation_chair` | Kuaishou |
| 5 | `kungfu_sf` *(renamed)* | B3 |
| 6 | `angryAlert` (vertical) | Kuaishou |
| 7 | `matcha_drink` | B1 — last, ban-rule group |
| — | `model_standing` | B3, **only after the likeness check** |

~3 days apart per group. Log every reply into `gtm_tools/relationship_leads.json` with
`channel: "facebook_group"` or `"kuaishou"` plus `need_verbatim`. Same **20-comment stop rule** as everything else — if 20 comments produce no real conversation, stop and
re-read the demand rather than posting more.

## Cadence and logging — both channels, and the workflow posts too

One group at a time, **~3 days apart**. Never the same asset into two groups on the
same day — FB collapses it as duplicate distribution.

**B1 last, always.** `105108073643190` carries an explicit anti-spam ban rule, and a
video post reads more promotional than a teardown does. Let the retouching teardown
(`../2026-09-01-retouching/posts_fb.md` A1) establish standing there first.

**Category match is not optional.** Do not send the coffee maker to an apparel group,
and do not send the serum bottle to B3 — that is the same mismatch the video table in
`posts_fb.md` exists to prevent.

**Logging:** every reply into `gtm_tools/relationship_leads.json` with
`channel: "facebook_group"` or `"kuaishou"`, plus `need_verbatim` and
`need_confidence: "stated"`. **Do not create a new file.** Counts toward the same
**20-comment stop rule** as the retouching series — one pilot across all of it, not
one per folder. If 20 comments produce no real conversation, stop and re-read the
demand rather than posting more.
