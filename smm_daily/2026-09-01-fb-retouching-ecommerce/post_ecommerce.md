# FB Groups · E-commerce workflow — 1 post (2026-09-01)

Companion to `posts_retouching.md`. One text post + one natively-uploaded video,
into the four buyer-side groups.

**Format:** text + **native video upload**. No image, no carousel, no link in the
post body — FB throttles link-outs, and a native video upload is not a link-out.
CTA in the first comment.

**Engine:** relationship / demand-mining. Same as the retouching series — the KPI
is replies, not reach.

**Drift check:** ✅ group-scoped, off-Page.

---

## Asset

`curify-gallery/ecommerce_workflow/` — **29 videos, all 1080×1920, h264+AAC**, two
families:

| Family | Count | Length | Structure |
|---|---:|---|---|
| `<product>_marketing_kit_en.mp4` | 9 | ~12.6 s | `PRODUCT PHOTO → HERO POSTER → AMAZON LISTING → SOCIAL CAMPAIGNS`, EN narration over ducked music |
| `<product>_viral_en.mp4` | 20 | ~15–30 s | title card → 5 captioned product shots → CTA card |

**Pick the video that matches the group's category** — do not send the coffee maker
to an apparel group:

| Group | Video |
|---|---|
| B3 `313105103563214` Apparels/Fashion Sell & Buy | `sneakers_viral_en.mp4` |
| B1 `105108073643190` E-commerce product photography | `product_to_marketing_kit_en.mp4` (the flagship — the full 4-stage arc) |
| B2 `765595303494969` Product Photographer USA | `camera_marketing_kit_en.mp4` |
| B4 `1212659302803905` Online E-Commerce sellers solution | `earbuds_marketing_kit_en.mp4` |

**Clearance:** `curify-studio/docs/asset-authority-distribution-inventory.md`
classifies the workflow demos as *自有素材，自有输出 → ✅ 立即可用* — own source,
own output, no IP exposure. (Unlike the Labubu / Cinnamoroll print assets, which
are permanently off the public feed.)

⚠️ Only 5 of the 29 are on CDN or YouTube, and these are **not** in the autopost
item pool (`project_fb_follower_growth.md`). This is a manual native upload from
the local file.

---

## FB post copy

📦 The expensive part of e-commerce photography isn't the shoot. It's that one SKU needs several *different* photographs, and a booked shoot gives you one or two of them.

Think about what a single product actually has to carry on the page:

· A clean pack shot — for the shopper comparing five tabs
· An on-model or in-use shot — for the impulse buy
· A lifestyle scene — for discovery and social
· An editorial frame — for paid
· A short vertical video — for everything else

That's five jobs from one product. Then the colourway drops, or the season turns, or you list on a second marketplace at a different aspect ratio, and you're booking the studio again.

A commercial shoot typically runs 3–7 days from booking to delivered files. Most stores list weekly. Some list daily. Those two clocks don't match, and the gap between them is exactly where a listing goes up with one grey photo and then just… stays there.

The video is one product photo run through our pipeline — hero poster, then the marketplace listing, then the social set. Same single input.

It isn't magic and it isn't free of judgement. The output still needs someone to check that every claim on the page belongs to the product (we've shipped that mistake ourselves and it's a quiet, expensive one). But the bottleneck moves from *when can the studio fit me in* to *which shots do I actually want.*

Genuinely curious how the rest of you handle this. Do you shoot everything, generate everything, or split it by SKU tier? 👇

---

## First comment (the CTA)

```
If you want to try it on your own product: curify-ai.com/tools/ecommerce-photo —
upload one photo, it generates the set. Or just drop a product shot in the
comments and I'll run one for you.
```

`/tools/ecommerce-photo` is self-serve — it renders a real inline image2image
generate block, not a waitlist card. Confirm it loads before posting.

⛔ Do **not** point this at `/tools/packaging-mockup`. That one has no self-serve
backend and carries a contact CTA only.

---

## Copy provenance

Reused rather than reinvented — these lines are already ours and already public:

- **YouTube `ecom_kit` description** (`curify_background/scripts/run_workflow_youtube_batch.py`):
  *"One product photo → a full marketing kit: clean product shots, lifestyle scenes,
  banners, and a video ad. From a single image, in minutes."*
- **On-screen hook baked into the flagship video**
  (`dev/jayw/video_pipelines/ecommerce_to_video/spec.json`): *"Only have ONE product photo?"*
- **The client brochure** behind `client_VC_portfolio/curify_ecommerce.pdf`
  (`curify-frontend/scripts/oneoff_ecommerce_booklet_pdf_2026-08-12.py`) — source of
  the 3–7 day shoot-cycle figure (*"一次商业拍摄从约档到出图通常 3–7 天"*), the pain
  lines (*"Shoots are slow and expensive — and they don't scale with your launch
  cadence"*), and the ladder *One photo → Six-grid main → Detail page → Scene &
  model → Short video*.
- **The company deck, 案例三** (`company-intro/deck/intro_src.html`) — the framing
  this post is built on: *「电商最贵的一段不是拍，是『一款要好几种图』…约一次摄影只能
  拿到其中一两种，而且换季、换色、上新就要重来。」*

The one line that is not lifted is *"we've shipped that mistake ourselves"* — that
refers to the hair-dryer listing in `posts_retouching.md` post 5, which is our own
documented failure and safe to reference.

---

## Cadence

One group at a time, ~3 days apart. **B1 last** — it has the explicit anti-spam ban
rule, so let the retouching teardown (post 1) establish standing there first. A
video post reads more promotional than a teardown does, and B1 is where that matters.

Log any reply into `gtm_tools/relationship_leads.json` with
`channel: "facebook_group"` and `need_verbatim`. Counts toward the same
**20-comment stop rule** as the retouching series.
