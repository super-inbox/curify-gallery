# FB Groups · E-commerce — 7 posts (2026-09-01 … 09-06)

_Facebook half of this folder. The 快手 half is **`posts_kuaishou.md`** — different
register, not a translation. **Clearance, the group list, cadence and the stop rule
are in [`README.md`](README.md)** and are not repeated here._

Companion to `../2026-09-01-retouching/posts_fb.md`. Into the same four buyer-side
groups: **B1** `105108073643190` E-commerce product photography (5.2K, ⚠️ ban rule) ·
**B2** `765595303494969` Product Photographer USA (1.3K) · **B3** `313105103563214`
Apparels/Fashion Sell & Buy (5.0K) · **B4** `1212659302803905` Online E-Commerce
sellers solution (6.9K).

| Post | Format | Asset | Goes to |
|---|---|---|---|
| **W1** · the shoot doesn't scale | text + native video | `ecommerce_workflow/*.mp4`, category-matched | B3, B2, B4, then B1 |
| **W2** · one photo, nine variants | text + native image | `w2-one-photo-nine-variants.jpg` | B4, B2, then B1 — **not B3** |
| `rotation_chair` | native video | ad-video library | B4 |
| `angryalert` (landscape cut) | native video | ad-video library | B2 |
| `kungfu_sf` | native video | ad-video library | B3 |
| `matcha_drink` | native video | ad-video library | B1 — last |
| `model_standing` | native video | ad-video library | B3, ⚠️ **only after the likeness check** |

**Format rules, every post:** never a carousel, never a link in the post body — FB
throttles link-outs, and a native upload is not a link-out. CTA in the first comment.
One asset per post.

**Engine:** relationship / demand-mining. KPI is replies, not reach.
**Drift check:** ✅ group-scoped, off-Page — the Page identity is Sinosphere culture
edutainment, so an ad-craft post in the Page feed would be Position Drift.

**⚠️ Not B3 for W2.** B3 is Apparels/Fashion; a serum bottle there is exactly the
category mismatch the video table exists to prevent. To run W2 in B3, re-run the
asset on a garment first.

---

## The workflow video library

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

### W2's asset

`w2-one-photo-nine-variants.jpg` (1272×1118) — a copy of
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

# Workflow posts

## W1 — the shoot doesn't scale with your listing cadence

**Asset:** category-matched video, per the table above.

### FB post copy

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

### First comment (the CTA)

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

### Copy provenance

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

## W2 — one photo, nine variants

**Image:** `w2-one-photo-nine-variants.jpg`

### FB post copy

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

### First comment (the CTA)

```
Same thing on your own product: curify-ai.com/tools/ecommerce-photo — upload one
photo and it generates the set. Or drop a product shot below and I'll run nine and
post them back, the misses included.
```

Same gate as post 1: `/tools/ecommerce-photo` is self-serve and renders a real
inline image2image generate block. Confirm it loads before posting, and still do
**not** point this at `/tools/packaging-mockup`.

### Copy provenance

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

# Ad-video posts

_Ordered by shipping slot. Each is keyed by its `index.json` `id`._

## `rotation_chair` — 10s · 9:16 · unbranded ✅
*The strongest B2B proof in the set — feature-explainer motion graphics normally need a
3D artist.* → **B4**, then 快手（`posts_kuaishou.md`） (best batch-inquiry driver of the six).

**FB post:**
> 🪑 Ten seconds on an office chair: airflow rendered moving through the mesh back, a readout on the armrest as it adjusts, then a 360 in a styled room.
>
> The middle shot is the point. Airflow through a mesh back is *invisible* — you cannot photograph it. Every furniture brand that wants to sell breathability ends up commissioning a 3D artist for that one shot, and that's a quote and a two-week turnaround for six seconds of video.
>
> Same for the armrest readout. It's the shot that answers "how far does it actually adjust," which is the question that decides the sale on a chair.
>
> Hard goods are where this pays off most, I think — furniture, appliances, tools. Anything where the buyer's real question is *how does it work*, not *what colour is it*. A photo can't answer that. A diagram can, but nobody watches a diagram.
>
> If you sell hard goods: which feature of yours have you never managed to show properly? 👇

**First comment:**
```
Self-serve on your own product: curify-ai.com/tools/product-video
Catalog-scale (a full SKU line, batched): curify-ai.com/contact
```

---

## `angryalert` — 20.3s · 9:16 · Curify-branded ✅
*Landscape cut `AngryAlert_landscape.mp4` (16s) for FB, vertical for 快手.*
*The product is fictional — say so. It reads as a joke, and the joke is the hook.*
→ **B2** (the photographer group — they'll read the craft), then 快手 — see `posts_kuaishou.md`.

**FB post:**
> 📣 A finished 20-second app commercial — office scenes, an actor, a HUD overlay, a logo sting.
>
> The app does not exist. I made it up. It's called Angry Alert and it supposedly warns you before someone gets annoyed.
>
> That's the actual point. There's a whole category of thing you can't shoot yet: the app you haven't built, the SKU still at the factory, the packaging you're deciding between. That's exactly when you most need to *see* the ad — a pitch deck, a pre-order page, a "does this concept land" test before committing the budget.
>
> The old order is shoot → then market. This inverts it: you make the commercial for the thing first, look at it, and let that tell you whether the thing is worth making.
>
> The honest limit: it's convincing precisely because nothing in it has to be true. For a real product every claim on screen still has to be one you can stand behind.
>
> Has anyone here made the ad before the product? 👇

**First comment:**
```
curify-ai.com/tools/product-video — self-serve.
Concept work / batches: curify-ai.com/contact
```

---

## `kungfu_sf` — 20.6s · 16:9 · Curify-branded ✅
**⚠️ Rename to `kungfu_sf_energy_spec.mp4` before posting.** 16:9 — FB only, or recut
for Kuaishou. → **B3**.

**FB post:**
> 🥋 Twenty seconds: a kungfu figure on a tiled rooftop hung with red lanterns, a leap across a downtown rooftop, and a final stance at the Golden Gate at sunset with autumn leaves coming down.
>
> Three locations. Two of them you cannot get. Filming on the Golden Gate approach means permits, insurance, a crew call and a sunrise window you get one shot at — and rooftop-to-rooftop needs a stunt team and a closed set.
>
> This is the lane where the economics stop being close. Product photography, you can argue — a good photographer is fast and the result is real. But landmark-scale action is a five-figure line item before anyone shows up, and for most brands the honest alternative isn't a cheaper shoot, it's *not making the spot at all*.
>
> That's the shift worth naming: it's less about replacing shoots and more about the ads that never got made because the location was out of reach.
>
> Anyone here priced a location shoot recently? Curious what the real numbers look like in 2026. 👇

**First comment:**
```
curify-ai.com/tools/product-video for the self-serve version.
Campaign / batch work: curify-ai.com/contact
```

---

## `matcha_drink` — 15.1s · 9:16 · unbranded ✅
*The lead asset. Zero brand risk, universally legible, and beverage is a category every
seller group understands.* → **B4**, then 快手 — see `posts_kuaishou.md`.

**FB post:**
> 🍵 This is 15 seconds of iced matcha — the banana slices falling, the milk pour, the condensation on the finished glass.
>
> There was no shoot. No food stylist, no bounce card, no getting the pour right on take 40 while the ice melts and the whole setup has to be rebuilt.
>
> I'm posting it because beverage is the category where the gap is widest. A drink has to look *cold*, and cold is the single hardest thing to hold on a hot set — you're fighting condensation and melt on a clock. That's why the pour shot is the one everybody outsources.
>
> Worth saying what it isn't: it's not a substitute for shooting a product whose real texture matters to the buyer. It's a substitute for the fifth variation of a shot you already got right once.
>
> For those of you selling food and drink — where does your listing actually break down? The hero, the texture macro, or the lifestyle scene? 👇

**First comment:**
```
If you want to try it on your own product: curify-ai.com/tools/product-video
Or drop a product shot in the comments and I'll run one for you.
```

---

## `model_standing` — 10s · 9:16 · ⚠️ hold pending likeness check
Copy is drafted so it's ready the moment the reference is confirmed synthetic.
**Do not post before that.** → **B3** (apparel).

**FB post:**
> 👔 A full-length on-model shot of a black suit — marble-and-brass lobby, slow orbit, ten seconds.
>
> On-model is the shot apparel sellers can least afford to skip and least afford to repeat. One model, one studio day covers maybe a handful of looks, and then a colourway drops or you list on a marketplace at a different crop and you're booking again.
>
> Two things I'd flag rather than oversell. Fabric behaviour is still the tell — how a real garment falls and creases is the thing generation is worst at, and a suit is a forgiving case because the drape is structured. And if you generate a model, the face has to be genuinely synthetic, not a real person's likeness carried over from a reference. That one is a legal problem, not a quality problem.
>
> Where do you land on generated models — using them, avoiding them, or only for flat-lay adjacent stuff? 👇

**First comment:**
```
curify-ai.com/tools/product-video — try it on one of your own products.
Full catalog runs: curify-ai.com/contact
```

---

## `oilight` — 26.4s · ⚠️ hold
No copy drafted. Needs the client's written OK and the source-footage provenance
(§1). Once cleared, the angle is the desert-dig opening → product end card as a
brand-story arc, which none of the other nine do.

---

## `corona_sunrise` · `mooncakes` · `molly_forest` · `beauty_cream` — ⛔ internal
Indexed in `index.json`, no post copy by design. Use in decks and sales calls.
For public use, re-render de-branded — `prompts/beauty_cream.json` shows the swap.

---
