# FB Groups · E-commerce workflow — 2 posts (2026-09-01, post 2 added 09-10)

Companion to `../2026-09-01-retouching/posts_fb.md`. Into the four
buyer-side groups.

| Post | Format | Asset |
|---|---|---|
| 1 · the shoot doesn't scale | text + **native video upload** | `ecommerce_workflow/*.mp4`, category-matched |
| 2 · one photo, nine variants | text + **single native image** | `01-one-photo-nine-variants.jpg` |

**Format rules, both posts:** never a carousel, never a link in the post body — FB
throttles link-outs, and a native upload (video or image) is not a link-out. CTA in
the first comment. One asset per post.

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

### Post 2's asset

`01-one-photo-nine-variants.jpg` (1272×1118) — a copy of
`client_VC_portfolio/ad-variants-demo-09-10/_one-to-nine.jpg`. One source pack shot
and the nine variants generated from it, captioned by setting.

Generated end-to-end from our own prompt (`gen_variants.py`, prompt inline); the
bottle is synthetic, and there is no brand, no logo and no client product in the
frame — the label is blank on purpose. Full record in that folder's `PROVENANCE.md`.
**Leave the original where it is**: `curify-studio/gtm_tools/batch_marketing_agency_2026-09-10.json`
attaches it by absolute path.

One honest limit, and the post says so: a blank label is an easier thing to hold
steady across nine renders than printed artwork is. This demonstrates that the
*object* is locked. It does not demonstrate that a real SKU's label survives.

---

# Post 1 — the shoot doesn't scale with your listing cadence

**Asset:** category-matched video, per the table above.

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
refers to the hair-dryer listing in `../2026-09-01-retouching/posts_fb.md` A5, which is our own
documented failure and safe to reference.

---

# Post 2 — one photo, nine variants

**Image:** `01-one-photo-nine-variants.jpg`

## FB post copy

📸 Here's the quiet reason "just generate more product shots" doesn't work: you don't get more shots of your product. You get more shots of a product that resembles yours.

Run the same prompt twice for a serum bottle on marble and two bottles come back. The dropper collar is a smooth sleeve in one and a stepped collar with a ring in the other. The label edge goes from hard and opaque to soft and translucent. The shoulder narrows. Nobody staged that — it's just what two runs produce, because each run invents the bottle again from the words.

For a mood board, fine. For a listing, that's a returns problem, and depending on what you sell it's a compliance one.

The fix isn't a better prompt. It's **feeding the product photo back in as the input** and changing only the setting around it. The product stops being described and starts being carried.

From one pack shot, that's:

· A clean white pack shot for the shopper comparing five tabs
· Marble and pastel podium for a brand-led detail page
· Bathroom counter and flat-lay for lifestyle and social
· Outdoor sun and botanical for seasonal
· Dark luxe for paid
· A gift-set frame for Q4

Nine settings above, one bottle, one camera angle.

Being straight about what you're looking at: that label is blank because the bottle is our own test object, not anyone's product. And a blank label is an easier thing to hold steady than printed artwork. This shows the *object* is locked. On a real SKU, the label is the first place to look, every time.

So test it before you trust it. Generate the same scene twice, put the two side by side, and **count something** — threads on the cap, rings on the collar, panels on the box. If the count moves between runs, the pipeline isn't holding your product, and no amount of prompt tightening is going to make it. 👇

## First comment (the CTA)

```
Same thing on your own product: curify-ai.com/tools/ecommerce-photo — upload one
photo and it generates the set. Or drop a product shot below and I'll run nine and
post them back, the misses included.
```

Same gate as post 1: `/tools/ecommerce-photo` is self-serve and renders a real
inline image2image generate block. Confirm it loads before posting, and still do
**not** point this at `/tools/packaging-mockup`.

## Copy provenance

The drift description in paragraph 2 is not hypothetical and not borrowed — it is
`serum_scene_shelf.jpg` vs `serum_scene_vanity.jpg` in
`dev/jayw/video_pipelines/ecommerce_to_video/products/gen/`, the same pair
`../2026-09-01-retouching/posts_fb.md` reads out in B1.
Two independently generated scenes of one product; the collar, the label and the
shoulder all move. Ours, observed, unstaged.

⚠️ The one line to keep out: do not say or imply the nine variants were made for a
customer. No delivered-outcome claim attaches to this asset — same standing rule as
the retouching series' red line 2.

---

# Cadence

One group at a time, ~3 days apart. **B1 last** — it has the explicit anti-spam ban
rule, so let the retouching teardown establish standing there first. A video post
reads more promotional than a teardown does, and B1 is where that matters.

| Post | Goes to | When |
|---|---|---|
| 1 · category video | B3, B2, B4, then **B1 last** | per the video table above |
| 2 · nine variants | B4, B2, then **B1 last** | after post 1 has stood in that group |

**Not B3 for post 2.** B3 is Apparels/Fashion — a serum bottle there is the same
category mismatch the video table exists to prevent. If post 2 is wanted in B3, the
asset has to be re-run on a garment first.

Never the same post into two groups on the same day — FB collapses it as duplicate
distribution.

Log any reply into `gtm_tools/relationship_leads.json` with
`channel: "facebook_group"` and `need_verbatim`. Counts toward the same
**20-comment stop rule** as the retouching series.
