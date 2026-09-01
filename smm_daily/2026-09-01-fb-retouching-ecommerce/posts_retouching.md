# FB Groups · Retouching series — 6 posts + 2 supply-side recuts (2026-09-01)

Follow-up to `curify-studio/docs/reddit-demand-mining-buyer-side-2026-08-31.md` §H,
which named Facebook seller groups as the ⭐ first channel to test but explicitly
flagged §H as **untested procedure** — no group joined, no contact made. These are
the assets that make it runnable.

**Account Positioning.** These go into **Groups**, never the FB·Curify Page feed.
The Page identity is East-Asian language & culture edutainment (EN); a retouching
teardown in the Page feed is Position Drift. Group posts do not carry that risk.
Drift check: ✅ (group-scoped, off-Page).

**Engine:** relationship / demand-mining. KPI is *replies*, not reach.

**Register:** value teardown, soft CTA. Chosen because `105108073643190` carries an
explicit ban rule — *"Let's not spam this group as you will be banned from the
group then."* — and because the native competing format (Image Solutions India's
service ads: before/after + bullet list + hashtag wall) is one we cannot honestly
run yet (see Red lines).

**House constraints carried over** (`2026-07-22-summer-festivals-sinosphere/caption_fb.md`,
`2026-08-13-layer-separation/captions_layer_separation.md`):
- **Single image. Never a carousel** — proven dead on FB·Curify.
- **No external link in the post body** — FB throttles link-outs. CTA goes in the
  **first comment**.
- Upload the image natively.

---

## Sourcing — every claim below traces to something already public

All substance is lifted from **`/blog/ghost-mannequin-ai-guide`** (shipped
2026-09-01; `curify-frontend/messages/en/blog.json` → `blog.ghostMannequinAiGuide`)
and **`/blog/50-ai-makeover-prompts`** (`blog.fiftyAiMakeoverPrompts`). Both are
our own writing, already published under our own name. Nothing here is a claim we
have not already made in public.

SEO rationale for pointing at that blog rather than a tool page: `ghost mannequin ai`
is **KD 1 / 110 vol / CPC $4.11** and `ai ghost mannequin` is **KD 0** — undefended
trade vocabulary — versus `ai clothes changer` at **KD 52 / 9,900 vol / CPC $0.95**.
Write in trade words (ghost mannequin, on-model, flat lay, placket, silhouette,
neck joint). Never consumer-tool words ("AI clothes changer", "AI background
remover") — those read as a free toy and land us in the contested SERP.

---

## Red lines (do not cross when adapting these)

1. **No client imagery, ever.** client-006's references are third-party e-commerce
   imagery with unresolved likeness licensing; client-008's are *"photographs of
   identifiable children."* Both stay local. Every image in this folder is our own
   generated output or our own template example.
2. **No delivered-outcome claims on the retouching track.** client-006 is
   `"Nothing sent to the client yet."`; client-008 is `"THE TRIAL CANNOT START."`
   The only paid engagement is client-007 (¥27,800), which is cultural merch/print,
   not retouching. Everything below is a **method** claim about our own runs.
3. **Keep `¥30/张 → ¥5/张, 100 → 3,000/day, 95% 验收率` (spec §7ab-D) out.**
   It is an internal target, not a shipped result.
4. **No third-party brands in the imagery.** `template-fashion-ecommerce-zh-jacket.jpg`
   was rejected for exactly this — it is clean, English and unwatermarked, but the
   garment carries a visible CAMEL logo.
5. **`template-fashion-before-after-outfit-annotation-card-*` is NOT retouching
   proof.** It is labelled BEFORE/AFTER but the "after" only adds callout labels —
   no retouch happened. Excluded from the series.

---

# Post 1 — the neck joint

**Image:** `01-neck-joint-cycling-jersey.jpg`
*(from `nano_insp/template-fashion-ecommerce-cycling-jersey-aerodynamic.jpg` — the
blog's own hero image, already published on curify-ai.com)*

## FB post copy

🧵 A bad ghost mannequin gives itself away in one square inch of the frame — and it isn't the one people look at.

It's the inside of the back collar.

Here's why. The traditional technique is two photographs: the garment on a form, and the garment turned so the **inside of the back collar** is visible. An editor cuts one into the other. That patch is the entire craft — everything else is background removal.

AI collapses both frames into one. You upload a single photo, and the model is asked to *invent* an interior that was never photographed.

So when a result looks wrong but you can't say why, check three things, in this order:

1️⃣ **The inside-back collar.** Is the colour right? Is there a facing, a contrast binding, a label that should be there — or one that shouldn't? This is where invention concentrates.

2️⃣ **The shoulder line.** A real garment on a form has a shoulder seam that sits slightly proud. Generated ones round it off, and that's what makes an output read as inflated rather than worn.

3️⃣ **The opening's depth.** A convincing neck opening shows *some* interior — a shadow, a hint of the back panel. Too flat and it reads as a sticker; too deep and the garment looks like it has a hole in it.

The classic method composites something real. The AI method generates something plausible. Almost every failure follows from that one sentence.

None of this needs a trained eye. It needs knowing which square inch to look at first — which is the part nobody tells you. 👇

**First comment:** `We wrote the whole checklist up here → curify-ai.com/blog/ghost-mannequin-ai-guide`

---

# Post 2 — inner-layer bleed

**Image:** `02-inner-layer-bleed-apparel-listing.jpg`
*(from `curify-frontend/raw/product-listing-fix-07-18/apparel_after.jpg` — our own
output; a clean single-layer source photo beside the listing built from it)*

## FB post copy

👕 If your AI ghost mannequin keeps showing the model's undershirt, the prompt isn't the problem. The source photo is.

It's called **inner-layer bleed**, and in our own runs it is the single most common reason a take gets discarded outright.

What happens: the source photo is on a model wearing a camisole or a tee under the product. That layer survives into the output. The placket reads open, the product looks like it's being worn over underwear, and the shot isn't "close" — it's unusable.

The instinct is to add a line to the prompt. *Do not render the inner garment.* We tried that. Prompt instructions alone are unreliable here.

The fix is upstream, in the input:

✅ Pick source photos where the wearer's own top is a single layer — nothing underneath to carry over
✅ Better, shoot on a dress form. The garment is already holding a correct shape, so less has to be generated at all
✅ If the product is worn closed, say so explicitly — every button fastened, placket visible, and state that the reference's inner garment does not carry over

You can't prompt your way out of a bad input. That turns out to be true of most of this work. 👇

**First comment:** `Send me a garment photo and I'll run it — happy to show you what comes back, good or bad. Full failure list here → curify-ai.com/blog/ghost-mannequin-ai-guide`

---

# Post 3 — silhouette drift & detail flattening

**Image:** `03-silhouette-drift-same-jersey.jpg`
*(crop of the same cycling-jersey template — one garment rendered twice; the two
silhouettes visibly differ through the torso)*

## FB post copy

📏 Silhouette drift is the expensive one.

A boxy garment quietly comes back fitted. Nobody flags it, because the image looks good. The model just carries a prior about how clothes sit on bodies, and applies it.

It changes the fit the buyer is judging. That shows up later as returns.

Its cheaper cousin is **detail flattening**:

· Button counts change
· A pointed hem tab becomes a straight hem
· Pocket seams vanish

Countable details are where generation is least reliable — and, usefully, where checking is easiest. So count the buttons.

One thing worth knowing before anyone builds a checker for this. In one of our own runs, three takes in a row flattened a hem into a plain ribbed band. All three were *correct*. Our spec said "notched V-split." The garment actually had a wide ribbed band angling into two pointed centre-front tabs, the right overlapping the left, fastened by two more buttons — nine in total, not seven.

We fixed it by re-reading the garment photograph. Detail compliance went 0/3 to 3/3, with no checker involved.

A gate on a generator that fails half the time just automates rejection. Read the product hard enough to describe it, before you decide you need something to catch what you failed to describe. 👇

**First comment:** `The other two failure modes, and how to check them → curify-ai.com/blog/ghost-mannequin-ai-guide`

---

# Post 4 — the two-ratio check

**Image:** `04-two-ratio-check.jpg`
*(built for this series — see `Build note` at the bottom)*

## FB post copy

📐 Two ratios catch a bad ghost mannequin result in under a minute. Neither one is a pixel comparison.

**Length** — (hem_y − shoulder_y) ÷ (hip_y − shoulder_y)
**Width at bust** — garment_width_at_bust ÷ body_width_at_bust

Both measured against pose landmarks, never against absolute pixels. Ratios survive crop and camera distance. Pixel measurements don't.

And then the rule that matters more than either formula:

⛔ **Do not measure the output against your source photo.**

If your source is a garment on a dress form and your output is a garment holding a human shape, the two share no landmark, no scale and no pose. Any proportion you compute between them is measuring the dress form, not the error.

Compare against your size chart in centimetres. Or against nothing at all — that is more honest than a number that means nothing.

For discrete details, don't measure. **Count.** Buttons, buckles, visible seams, hem structure. It's the check most people skip because it feels too simple to be worth doing. 👇

**First comment:** `Full method → curify-ai.com/blog/ghost-mannequin-ai-guide`

---

# Post 5 — the image was fine, the listing was wrong

**Image:** `05-wrong-listing-vs-right-listing.jpg`
*(crop of `curify-frontend/raw/product-listing-fix-07-18/hairdryer_before-after.jpg`
— our own documented failure beside our own fix)*

## FB post copy

🚨 The image was fine. The listing was wrong. Those are two different failures, and only one of them is visible.

**Left**: a detail page we generated for a hair dryer. Read it. The headline says *Salon-grade fast drying.* The body copy says 100% Mulberry Silk. Soft & Breathable. Premium Craftsmanship. Lounge Ready. Effortless Elegance. There's a size chart with **bust, waist and hips.**

For a hair dryer.

Every individual image on that page is clean. The page is nonsense. What happened is that the template carried its category's attributes onto the wrong product, and nothing in an image review would ever catch it.

**Right**: the same product rebuilt. High-velocity airflow. Ionic frizz control. 1600W, 580g, digital brushless motor, 2.7m cord, concentrator nozzle.

The lesson we took from it: a listing isn't a set of images, it's a set of **claims** — and image QC doesn't touch claims. If you're building detail pages at SKU velocity, your checklist needs one line that has nothing to do with how anything looks:

✅ *Does every attribute on this page actually belong to this product?*

We're posting our own miss because this one costs money quietly. The page just converts badly, and nobody can say why. 👇

**First comment:** `We built the fix into the flow here → curify-ai.com/tools/ecommerce-photo`

---

# Post 6 — write the retouching notes out

**Image:** `06-portrait-retouching-blueprint.jpg`
*(from `nano_insp/template-portrait-retouching-blueprint-en 1.jpg` — our own
template example, unwatermarked, already published on curify-ai.com)*

## FB post copy

✍️ "Glow-up" is the word that ruins the result.

Retouching briefs get written in adjectives — glow-up, makeover, upgrade, flawless. Every one of those pushes a model straight to porcelain airbrushing. Pores gone, texture gone, a face that reads as a mask.

The fix is boring and it works: **write the notes out, region by region.**

· **Skin** — even the tone, reduce oiliness and redness. Keep the pores.
· **Eyes** — reduce dark circles and puffiness. Don't reshape.
· **Brows & jaw** — define, don't redraw.
· **Hair** — tame flyaways, add natural volume.
· **Lighting** — soften the background, balance the fill.

That's the image above. The left panel is the markup; the right is the result of following it. Nothing on that list is a mood. Every line names a region and an action.

Our own standing rule, in every retouching brief we run: **no mask-like smoothed skin — preserve natural texture.** Specific descriptors beat aspirational ones every single time, because a model can only act on what you actually named.

The test for any brief, whether you're sending it to a retoucher or to a model: could someone else execute it without asking you a question? 👇

**First comment:** `Drop a portrait in the comments and I'll run it against a written brief like this one, so you can see the difference a specific note makes.`

---

# Supply-side recut

For `524557767708832` (29.0K, "EARN MORE BY DOING PHOTO RETOUCHING JOB"),
`452139992386987` (13.6K, Dhaka freelance suppliers) and `729600757556835` (4.0K).

⚠️ **These groups are supply, not demand.** Pitching retouching services at
retouchers is the same error the reddit doc diagnosed on Reddit: asking the supply
side of a market whether it contains demand. So these two posts ask for something
instead of selling something. Do **not** post 1–6 here unchanged.

## Recut A — the reject list (adapted from posts 1 + 3)

**Image:** `01-neck-joint-cycling-jersey.jpg`

👋 To the retouchers in here — a question, and a swap.

We run AI-assisted apparel work (ghost mannequin, on-model, background replacement) and we keep a written taxonomy of what goes wrong, because none of it ships without a human pass. Four failures account for most of our rejects:

· **Invented inside-back collar** — wrong colour more often than wrong shape
· **Inner-layer bleed** — the source model's camisole survives into the output
· **Silhouette drift** — a boxy garment comes back fitted
· **Detail flattening** — button counts change, a pointed hem tab goes straight

The generation does the volume. The judgement is still the part that doesn't automate — knowing that a shoulder seam should sit slightly proud, or that a neck opening needs *some* interior or it reads as a sticker.

Two things:

1️⃣ **What's on your reject list that isn't on ours?** Genuinely asking.
2️⃣ We're building a bench of retouchers to hand overflow to, white-label. If you take that kind of work, say so below and I'll follow up.

Not pitching services at this group — you're the people who'd be doing the work. 👇

## Recut B — how do you QC it? (adapted from post 4)

**Image:** `04-two-ratio-check.jpg`

📐 Retouchers — how do you QC an AI-generated garment shot when there's no "original" to compare it against?

We settled on two ratios, both measured against pose landmarks rather than absolute pixels:

**Length** — (hem_y − shoulder_y) ÷ (hip_y − shoulder_y)
**Width at bust** — garment_width_at_bust ÷ body_width_at_bust

Ratios survive crop and camera distance. Pixels don't.

The trap we fell into first was measuring the output against the source photo. If the source is a garment on a dress form and the output is a garment holding a human shape, they share no landmark, no scale and no pose — whatever number you get is measuring the dress form, not the error.

Genuinely curious how people who do this by hand handle it. Do you check against the size chart, against a reference shot, or by eye? 👇

---

# Placement matrix

Buyer groups: **B1** `105108073643190` E-commerce product photography (5.2K, ⚠️ ban rule) ·
**B2** `765595303494969` Product Photographer USA (1.3K) ·
**B3** `313105103563214` Apparels/Fashion Sell & Buy US/CA/UK/AU (5.0K) ·
**B4** `1212659302803905` Online E-Commerce sellers solution (6.9K).
Supply groups: **S1** `524557767708832` (29.0K) · **S2** `452139992386987` (13.6K) ·
**S3** `729600757556835` (4.0K).

| Post | Goes to | When |
|---|---|---|
| 1 · neck joint | B1, B3 | **post this first**, into B1 only |
| 2 · inner-layer bleed | B3, B2 | week 1 |
| 3 · silhouette drift | B3, B1 | week 2 |
| 4 · ratio check | B1, B2 | week 2 |
| 5 · wrong listing | B1, B4, B2 | week 3 — strongest for non-apparel sellers |
| 6 · retouching notes | S3, B1 | week 3 |
| Recut A | S1, S2, S3 | week 1 |
| Recut B | S1, S2 | week 3 |

**Cadence: one post per group per ~3 days.** Never the same post into two groups on
the same day — FB collapses it as duplicate distribution.

**B1 first, alone.** It is the group with the explicit ban rule, so it is the
strictest test of whether this register survives. If post 1 stands for a week
without moderation, roll out the rest. If it gets pulled, the register is wrong and
the rest of the schedule should not run.

`facebook.com/uniqretouch` is a **competitor Page** (9 followers, Houston,
"high-end image retouching and editing company"). We cannot post there. Worth
watching as a format benchmark — their pattern is a listicle hook plus
*"Check list in comment section 👇"*, the same comment-CTA mechanic used here.

---

# The mechanic that actually matters

From the reddit doc §H0, and the thing most likely to be got wrong:

> The RedNote motion that produced 3 conversations and the ¥27,800 deal was
> **评论区触达 — comment-section outreach**, not DMs. […] **DM only after they
> reply to the comment.**

These six posts are the standing exhibit, not the motion. The motion is: read the
group daily, find a post where someone **states a need in their own words**, and
reply in the comments with output on *their* product category — not a link, not a
deck, not a portfolio. The posts exist so that when someone clicks through after
that comment, there is something credible to find.

**Logging:** every comment left goes into `gtm_tools/relationship_leads.json` with
`channel: "facebook_group"`, `need_verbatim` (their exact words) and
`need_confidence: "stated"`. **Do not create a new file.**

**Stop rule: 20 comments, then evaluate.** Not 20 posts read — 20 comments left.
The small n is deliberate.

---

# Build note

`04-two-ratio-check.jpg` is the only asset built for this series (1200×1200).
Everything else is a copy or a crop of something already on disk and already
published. Palette is the company-deck palette (`#FAF8F2` ground, `#C0521E` accent,
`#93A3C4` rules) so it sits with the rest of our material.

Images are taken from `curify-frontend/public/images/nano_insp/`, which holds the
**clean** copies. The `curify-gallery/` and `company-intro/deck/assets/` copies of
the same shots are tile-watermarked and read heavy at feed size.
