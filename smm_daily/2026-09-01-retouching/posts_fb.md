# FB Groups · Retouching — 14 posts + 2 supply-side recuts (2026-09-01)

_Consolidated 2026-09-11 from `2026-09-01-fb-retouching/` and
`2026-09-01-fb-child-photography/`. They shared a register, a red-line list, a logging
sink, a stop rule — and, it turned out, two images held under different names._

Two series, one channel:

| | Buyer | Posts | Source material |
|---|---|---|---|
| **Series A** — apparel & e-commerce retouching | sellers, brands, and (recut) retouchers | A1–A8 + recuts | our own pipeline output, `/blog/ghost-mannequin-ai-guide` |
| **Series B** — child photography | parents, small studios | B1–B6 | client-008 (场景增强), no image of theirs used |

The 小红书 cut of the same material is **`posts_rednote.md`** in this folder. It is kept
separate rather than merged because the constraint that governs it is not a Facebook
constraint — it is an **account-positioning conflict** that has to be resolved before
anything ships there at all. Same red lines, different channel problem.

**Image manifest** — 16 files, `a*` Series A, `b*` Series B, `shared-*` both, `rn*` 小红书:

| File | Used by |
|---|---|
| `a1-neck-joint-cycling-jersey.jpg` | A1, Recut A |
| `a2-inner-layer-bleed.jpg` | A2 |
| `a3-silhouette-drift.jpg` | A3 |
| `a4-two-ratio-check.jpg` | A4, Recut B |
| `a5-wrong-vs-right-listing.jpg` | A5 |
| `a8-wedding-portrait-retouch.jpg` | A8 ⛔ held — see red line 6 |
| `shared-retouching-blueprint.jpg` | **A6 + B3** |
| `shared-locked-subject-backdrops.jpg` | **A7 + B bonus slot** |
| `b1-look-at-what-moved.jpg` | B1 |
| `b2-two-pipelines.jpg` | B2 |
| `b4-five-places-to-look.jpg` | B4 |
| `b5-read-the-pictures-first.jpg` | B5 |
| `b6-we-do-not-publish-children.jpg` | B6 |
| `rn1-批量一致性.jpg` · `rn2-模特图翻车点.jpg` · `rn3-场景增强.jpg` | 小红书 1–3 |

⚠️ There is no `a6`, `a7` or `b3` file. Those three slots run the two `shared-*` images,
which is the whole point of the consolidation — **do not "fix" the gap by re-copying.**

---

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
6. **"Our own output" has to mean our own pipeline.** `08-wedding-portrait-retouch.jpg`
   was made in a third-party chat model, not on our stack — the source PNG carries
   `kMDItemWhereFroms: https://chatgpt.com/` and a Chrome quarantine record. Red line 1
   still holds (no client, no real person, no brand), but the series' standing phrasing
   — *"in our own runs"*, *"we tried that"* — does not extend to it, and it cannot be
   captioned as something our pipeline produced. See the gate on A8.

(Series B adds one more, argued in full below: **no child in any frame,** including a generated one.)

---

# Series A — apparel & e-commerce retouching

## A1 — the neck joint

**Image:** `a1-neck-joint-cycling-jersey.jpg`
*(from `nano_insp/template-fashion-ecommerce-cycling-jersey-aerodynamic.jpg` — the
blog's own hero image, already published on curify-ai.com)*

### FB post copy

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

## A2 — inner-layer bleed

**Image:** `a2-inner-layer-bleed.jpg`
*(from `curify-frontend/raw/product-listing-fix-07-18/apparel_after.jpg` — our own
output; a clean single-layer source photo beside the listing built from it)*

### FB post copy

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

## A3 — silhouette drift & detail flattening

**Image:** `a3-silhouette-drift.jpg`
*(crop of the same cycling-jersey template — one garment rendered twice; the two
silhouettes visibly differ through the torso)*

### FB post copy

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

## A4 — the two-ratio check

**Image:** `a4-two-ratio-check.jpg`
*(built for this series — see `Build note` at the bottom)*

### FB post copy

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

## A5 — the image was fine, the listing was wrong

**Image:** `a5-wrong-vs-right-listing.jpg`
*(crop of `curify-frontend/raw/product-listing-fix-07-18/hairdryer_before-after.jpg`
— our own documented failure beside our own fix)*

### FB post copy

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

## A6 — write the retouching notes out

**Image:** `shared-retouching-blueprint.jpg`
*(from `nano_insp/template-portrait-retouching-blueprint-en 1.jpg` — our own
template example, unwatermarked, already published on curify-ai.com)*

### FB post copy

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

## A7 — the giveaway is the floor, not the cut-out

**Image:** `shared-locked-subject-backdrops.jpg`
*(from `client_VC_portfolio/scene-enhancement-demo-09-07/_contact-sheet.jpg` — our own
generated frame, moved to three backdrops. 894×1842; the same 1:2-ish strip shape as
A1, which already runs in-feed.)*

### FB post copy

🖼️ When a background replacement looks wrong, everyone blames the cut-out. It's almost never the cut-out.

Matting handles hair now. What gives a composite away is that the subject and the new backdrop were lit by two different lights — and the place it shows up first is the floor at the subject's feet.

Four checks, in this order:

1️⃣ **Ground contact.** A standing subject throws a small, dark, hard-edged shadow directly under the shoe, and a softer one falling away from the light. Composites usually get the soft one and skip the contact shadow. The person then reads as hovering a centimetre off the floor — nobody can name it, everybody feels it.

2️⃣ **Light direction.** Find the shadow side of the face. Then find where the light in the new plate comes from. Window camera-left, face lit camera-right, and there is no grade that saves it.

3️⃣ **Colour spill.** A grey sweep throws grey into a cream knit. Drop that subject onto a warm daylight interior and the sweater stays slightly cold while everything around it is warm. Neutralise the spill *on the subject* — warming the plate just widens the gap.

4️⃣ **Camera height.** The plate has a horizon and the subject was shot at some height. Plate at hip height, subject at chest height, and the floor plane meets the shoes at an angle that can't happen.

The image is one frame on three backdrops — white sweep, grey plaster, daylight interior. Same face, same sweater ribbing, same trouser crease, same pose.

And the part that actually matters, because it's where this goes wrong: that is **one photograph fed back in three times with only the backdrop changed.** It is not three generations of "woman in a cream sweater." Three generations give you three different women — different jaw, different knit, different fit — and a before/after built that way isn't a before/after. It's two pictures of two people.

Same subject or it doesn't count. (The base frame here is our own generated model, by the way, not a client's file — we don't post client sessions.) 👇

**First comment:** `Send me a full-length frame from your last session and I'll run three backdrops on it, so you can check the four things above yourself. I'll show you the ones that fail too — the floor is where they fail.`

---

## A8 — wedding & portrait, at set scale

> ⚠️ **GATE — do not post until re-rendered on our own stack.**
> The asset is a third-party-model card (red line 6). The copy below is written and
> ready, and its claims are all method claims we can stand behind — but the series'
> credibility rests on *every image here being our own output*, and this one isn't yet.
> Re-run the three pairs through our own pipeline, swap the file, then post.
> Two further conditions once it does run:
> · **Never crop the footer.** *"AI-generated retouching concepts"* is the line that
>   keeps this inside red line 2. Cropping it turns a concept card into a delivered-work
>   claim.
> · It is the closest thing in this series to the Image Solutions India service-ad
>   format we said we can't honestly run. It goes to a group **after** a teardown from
>   this series has already stood there — never as the opening post, and never into B1.

**Image:** `a8-wedding-portrait-retouch.jpg`
*(1122×1402 — 4:5, the one asset in the series already cut to feed ratio. From
`client_VC_portfolio/scene-enhancement-demo-09-07/wedding-retouch.png`.)*

### FB post copy

💍 The hard part of a wedding edit isn't any single frame. It's that four hundred frames have to look like one afternoon.

The couple walked the cliff at five, under flat grey cloud. The ceremony ran long. The light you showed them in the sample gallery never arrived — so now every frame gets warmed by hand, and warmed by the *same* amount, or the gallery reads as three different days.

That's the job, and it's most of why a wedding edit costs what it costs:

· **Relight, consistently.** Not one hero frame graded beautifully. Every frame carrying the same sun position, the same warmth, the same falloff.
· **Skin that stays skin.** Even the tone, drop the redness, keep the pores. A bride rendered as porcelain is the complaint that arrives a week later, when she's looked at it forty times.
· **Cleanup the couple never saw.** The three strangers on the sand. The bin, the cable, the car in the treeline.
· **The dress.** A veil and a chiffon train are semi-transparent against a bright sky — precisely where automatic tools eat the edge and hand it back as a hard line.

What's above are **concepts, not a client gallery.** We don't publish client sessions, so that's our own material run against the same brief: left is the flat frame, right is a relight plus a skin pass plus a background cleanup, with the pose, the face and the fabric left alone.

If you shoot volume — a studio, batch work, second shooters handing you two thousand frames a weekend — the consistency question is the one worth asking about before anything else. Ask it of any tool, including ours. 👇

**First comment:** `Happy to run a few of your own frames so you can put them beside your own hand edit. Drop one below or DM.`

---

## Supply-side recut

For `524557767708832` (29.0K, "EARN MORE BY DOING PHOTO RETOUCHING JOB"),
`452139992386987` (13.6K, Dhaka freelance suppliers) and `729600757556835` (4.0K).

⚠️ **These groups are supply, not demand.** Pitching retouching services at
retouchers is the same error the reddit doc diagnosed on Reddit: asking the supply
side of a market whether it contains demand. So these two posts ask for something
instead of selling something. Do **not** post A1–A8 here unchanged.

### Recut A — the reject list (adapted from A1 + A3)

**Image:** `a1-neck-joint-cycling-jersey.jpg`

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

### Recut B — how do you QC it? (adapted from A4)

**Image:** `a4-two-ratio-check.jpg`

📐 Retouchers — how do you QC an AI-generated garment shot when there's no "original" to compare it against?

We settled on two ratios, both measured against pose landmarks rather than absolute pixels:

**Length** — (hem_y − shoulder_y) ÷ (hip_y − shoulder_y)
**Width at bust** — garment_width_at_bust ÷ body_width_at_bust

Ratios survive crop and camera distance. Pixels don't.

The trap we fell into first was measuring the output against the source photo. If the source is a garment on a dress form and the output is a garment holding a human shape, they share no landmark, no scale and no pose — whatever number you get is measuring the dress form, not the error.

Genuinely curious how people who do this by hand handle it. Do you check against the size chart, against a reference shot, or by eye? 👇

---

## Placement matrix

Buyer groups: **B1** `105108073643190` E-commerce product photography (5.2K, ⚠️ ban rule) ·
**B2** `765595303494969` Product Photographer USA (1.3K) ·
**B3** `313105103563214` Apparels/Fashion Sell & Buy US/CA/UK/AU (5.0K) ·
**B4** `1212659302803905` Online E-Commerce sellers solution (6.9K).
Supply groups: **S1** `524557767708832` (29.0K) · **S2** `452139992386987` (13.6K) ·
**S3** `729600757556835` (4.0K).

| Post | Goes to | When |
|---|---|---|
| A1 · neck joint | B1, B3 | **post this first**, into B1 only |
| A2 · inner-layer bleed | B3, B2 | week 1 |
| A3 · silhouette drift | B3, B1 | week 2 |
| A4 · ratio check | B1, B2 | week 2 |
| A5 · wrong listing | B1, B4, B2 | week 3 — strongest for non-apparel sellers |
| A6 · retouching notes | S3, B1 | week 3 |
| A7 · locked subject | B2, B3 | week 4 |
| A8 · wedding & portrait | ⛔ **held** — see gate | — |
| Recut A | S1, S2, S3 | week 1 |
| Recut B | S1, S2 | week 3 |

**Cadence: one post per group per ~3 days.** Never the same post into two groups on
the same day — FB collapses it as duplicate distribution.

**B1 first, alone.** It is the group with the explicit ban rule, so it is the
strictest test of whether this register survives. If A1 stands for a week
without moderation, roll out the rest. If it gets pulled, the register is wrong and
the rest of the schedule should not run.

`facebook.com/uniqretouch` is a **competitor Page** (9 followers, Houston,
"high-end image retouching and editing company"). We cannot post there. Worth
watching as a format benchmark — their pattern is a listicle hook plus
*"Check list in comment section 👇"*, the same comment-CTA mechanic used here.

---

## Build note

`a4-two-ratio-check.jpg` is the only asset built for this series (1200×1200).
Everything else is a copy or a crop of something already on disk and already
published. Palette is the company-deck palette (`#FAF8F2` ground, `#C0521E` accent,
`#93A3C4` rules) so it sits with the rest of our material.

Images are taken from `curify-frontend/public/images/nano_insp/`, which holds the
**clean** copies. The `curify-gallery/` and `company-intro/deck/assets/` copies of
the same shots are tile-watermarked and read heavy at feed size.

### A7–A8, added 2026-09-10

Both are copies of portfolio assets, not new builds. The originals stay where the
outreach batches point at them — `curify-studio/gtm_tools/batch_marketing_agency_2026-09-10.json`
attaches by absolute path, so **do not move or rename the
`client_VC_portfolio/*-demo-*` folders.**

| Here | Original | Made by | Status |
|---|---|---|---|
| `shared-locked-subject-backdrops.jpg` | `client_VC_portfolio/scene-enhancement-demo-09-07/_contact-sheet.jpg` | our own prompt, `gen_scene_demo.py` (prompt inline) | ✅ runnable |
| `a8-wedding-portrait-retouch.jpg` | `.../scene-enhancement-demo-09-07/wedding-retouch.png`, re-encoded to JPEG q92 | third-party chat model — see red line 6 | ⛔ held |

`shared-locked-subject-backdrops.jpg` carries its own PROVENANCE record in the source folder: `00-base.png` is
synthetic, so **no real person is in the frame**, and the three backdrops were made
by feeding that one frame back in — which is the whole claim the post makes. That
record is worth reading before answering any question in the comments about it.

`a8-wedding-portrait-retouch.jpg` has no such record and no generation script on disk; its provenance is what the
xattr says and what its own footer admits. That asymmetry is the gate.

### A7 is also the asset Series B wanted

Series B had to argue *subject drift under regeneration vs subject preserved under
compositing* on a serum bottle, because it could not put a child in the frame and
would not synthesise one. A7 makes the identical argument on an adult — a synthetic adult, so no likeness question, and no child-shaped image
in front of a group of parents. It is a legitimate candidate for
`857871658366623` **Babies and Kids Photoshoot** once we are a member there, and it
lands harder than the bottle does. B1 keeps its place; this is a second
shot on goal, not a replacement.

**This is the reason the two series now share a folder** — the argument, and the
image that makes it, turned out not to belong to either one of them alone.

---

# Series B — child photography

## The image constraint, and how it was solved

**There is no child imagery in this series and there cannot be.**

1. **client-008's own images are withheld.** The record's words: the two embedded
   images (a theme catalogue and a 6-pair before/after contact sheet) are
   *"photographs of identifiable children."*
2. **The trial never started.** `"outcome": {"status": "brief_received", "delivered": []}`
   and, verbatim, `"THE TRIAL CANNOT START"`. There is no before/after of ours to
   show even in principle.
3. **We are not generating AI children for this.** Technically easy, wrong call: a
   synthetic child is still a child-shaped image posted into a group full of
   parents, and Meta already labels such posts "AI content" — which in this
   audience reads as a warning, not a feature.

**The substitute is a real demonstration on a non-human subject, and it is better
than a stock before/after would have been.** B1's image is built entirely from
our own e-commerce pipeline output at
`dev/jayw/video_pipelines/ecommerce_to_video/products/gen/`:

- **Top row — the drift, unstaged.** `serum_scene_shelf.jpg` and
  `serum_scene_vanity.jpg` are two independently generated scenes of the same
  product. The bottle is visibly *not the same bottle*: the pump collar is one
  smooth sleeve in the first and a stepped collar with a ring in the second, the
  label goes from opaque white with a hard edge to translucent grey, and the
  shoulder goes from narrow and square to wide and rounded. Nobody staged this —
  it is what two runs produced.
- **Bottom row — the fix, provably.** `serum.png` (the segmented cutout) composited
  onto two studio sweeps built in the same script. The subject is byte-identical
  across both panels because it is literally the same file pasted twice.

That is the client-008 argument end to end — subject drift under regeneration,
subject preserved under compositing — with no person in the frame at all. The
footer carries the transfer: *on a bottle this is a label redraw; on a face it is
someone else's child.*

Other assets checked and rejected: `template-child-hobby-skill-*` (illustrated
cartoon children, clean and Curify-branded, but parenting content — off-message in
a photography-technique series); `costume_tryon/*` (adult identity-lock, but the
subjects are footballers — real-person likeness, banned by `services_xianyu.md` §五).

**Added 2026-09-10 — there is now a second asset that makes this argument, on a
person.** `shared-locked-subject-backdrops.jpg` — Series A's A7 — is one
frame moved to three backdrops with the subject held: same face, same knit, same
pose. The subject is **synthetic and an adult**, so it clears both constraints above
— no likeness question, and no child-shaped image in front of a group of parents.
It is the same claim as B1's bottle, made on the body plan that actually matters
to this audience, and it lands harder. The bottle post keeps its slot; treat it as a
second post into `857871658366623` once we're a member, not a replacement.

---

## ⚠️ Group fit — read before posting

The named group is **`857871658366623` Babies and Kids Photoshoot** — 13.6K members,
public, created Feb 2021, genuinely active (11 posts today, 385 in the last month,
+38 members this week). **We are not a member yet**; it shows "Join group".

On one visit the top post was a graphic-design service advertising branded
first-birthday composites with a phone number — *"After edited photos thanks for
choosing … graphic design and data services"*, 174 reactions, Meta-labelled "AI
content". That is the shape of a **consumer + editor-advertising** group, not a
group of studios buying volume retouching. Same split §H2a keeps finding.

**This is one reading of one visit** — exactly the caveat now written into the doc's
§G — so it is not enough to write the surface off. It is enough to say: post here,
but do not build the pilot on it alone.

Two better-fit surfaces found while checking, both worth joining:

| Group | Members · activity | Why |
|---|---|---|
| **Inspired by Newborn Photography** | 46K · 2/day | Actual newborn-photographer community, low churn |
| **Photographers HIRING photographers** (second shooters etc) | 44K · 8/day | ⭐ **hiring** in the name — outsource intent is the stated purpose |

Also noted: `Real Estate Photoshop Outsourcing` exists at 30K private / 8.2K public
with 30–60+ posts a day. **The outsourcing-group format is proven on Facebook — it
just has no children's-photography equivalent.** That absence is itself a finding:
the client-008 buyer (a studio ordering 70 sets) is not in a community group, and
may not be on Facebook at all.

⚠️ Avoid the `FREE PHOTO EDITING` mega-groups (872K, 707K, 671K, 569K, 264K). They
are the consumer "edit my photo for free" pool, and the doc's 500k-is-spam rule was
written for exactly this.

---

## Sourcing

Every factual claim traces to the client-008 record or to already-published Curify
writing (`/blog/preserve-facial-features-ai-generation`,
`/blog/50-ai-makeover-prompts`). The client is never named, no image of theirs is
used, and no delivered outcome is claimed — because there is none.

⚠️ **One claim is hedged on the card itself and in the body**: the compositing
thesis is logged as *"Recorded as a lead, NOT a decision — no approach has been
chosen and none has been tested."* B2 says so. Do not let that line get edited
out.

---

## B1 — look at what moved

**Image:** `b1-look-at-what-moved.jpg`

### FB post copy

🔬 Two runs of the same product through the same pipeline. Look at the bottle, not the background.

Top row: two scenes generated separately. Same product, same prompt family, and the bottle came back **different both times**. The pump collar is a single smooth sleeve in one and a stepped collar with a visible ring in the other. The label goes from opaque white with a hard edge to translucent grey. The shoulder goes from narrow and square to wide and rounded.

Nobody staged that. It's just what two runs produced.

Bottom row: the same product, cut out once, dropped onto two different backdrops. Byte-identical in both — not because anyone asked for it, but because the subject never went into the model at all.

This is a serum bottle, so the stakes are a redrawn label. Run the same process on a portrait and the thing that comes back subtly different is a face.

If you're sending children's portraits out for background work, this is the whole question in one image. Which row is your editor delivering? 👇

**First comment:** `The mechanism, and how to tell which one you got → curify-ai.com/blog/preserve-facial-features-ai-generation`

---

## B2 — two pipelines

**Image:** `b2-two-pipelines.jpg`

### FB post copy

🧷 Following on from the bottle: there are two ways to replace a background, and they are not variations of the same thing.

**Full-frame diffusion.** The whole photo goes into the model, the whole photo comes out. Every pixel is perturbed by construction — that isn't a bug in someone's settings, it's what the method does. The face comes back changed. Often subtly enough that you sign it off.

**Segment → generate background → composite.** The subject is cut out first. The background is generated separately. The original subject pixels are pasted back. They're untouched *by definition* — not because someone asked nicely, but because they never entered the model.

This is why "please don't change the child" in a prompt is not a control. **A prompt is a request. Compositing is a guarantee.**

Fair warning on my own claim: this is our reading of the problem from a brief we studied closely, not a tested result — we haven't run it. But it's worth knowing the difference before you buy.

If your editor can't tell you which of the two they do, that's information as well. 👇

**First comment:** `Longer write-up on keeping identity locked through an edit → curify-ai.com/blog/preserve-facial-features-ai-generation`

---

## B3 — write the notes out

**Image:** `shared-retouching-blueprint.jpg`
*(our own portrait-retouching template example, an adult — deliberately)*

### FB post copy

✍️ The fastest way to ruin a child's portrait in the edit is to write the brief in adjectives.

Glow-up. Clean up. Flawless. Makeover. Every one of those pushes an editor — human or model — straight to porcelain. Pores gone, freckles gone, the scab on the knee gone. Parents notice. They often can't name what's wrong, but they know it isn't their kid.

Write it out instead, region by region:

· **Skin** — even the tone, reduce shine. Keep the texture. Keep the freckles.
· **Eyes** — take down redness if you must. Don't reshape, don't enlarge.
· **Hair** — tame the one flyaway crossing the face. Leave the rest.
· **Background** — soften, balance the fill.
· And the line that belongs on every children's brief: **no smoothed or plastic retouching.**

That last one isn't clever. It's the sort of line studios end up writing into their briefs in plain language after being burned a few times, and it works precisely because it says what *not* to do.

The example image is an adult on purpose — reason in B6. The method is identical.

The test for any brief, whether it's going to a person or a model: **could someone else execute it without asking you a question?** 👇

**First comment:** `Ten worked examples of specific-over-aspirational retouching notes → curify-ai.com/blog/50-ai-makeover-prompts`

---

## B4 — five places to look

**Image:** `b4-five-places-to-look.jpg`

### FB post copy

🔍 Five places to look before an edited portrait goes back to the parent. Takes about a minute.

Open the delivered file at 100% — not the preview. A compressed preview hides exactly the detail you're checking for.

**1. Eyelashes and flyaway hair.** If a single hair moved, the subject was regenerated, not composited.

**2. Skin at 100%.** Pores should still be there. Smooth is the tell, not the goal.

**3. The hair–background edge.** A halo, a hard cut, or hair that ends too cleanly — all three mean the matte was rushed.

**4. Fabric weave and print.** Knit texture and any pattern on the clothing should be pixel-identical to your original.

**5. The catchlight in the eyes.** On a small face this is the fastest tell of the lot — a regenerated eye moves it, and a model almost never puts it back in the same place.

If you only ever check one, check five. It's small, it's high contrast, and it gives the game away instantly.

None of this asks you to understand how any of it works. It asks you to know where to look, which is the part nobody hands you. 👇

**First comment:** `The longer version, on what actually survives an edit → curify-ai.com/blog/preserve-facial-features-ai-generation`

---

## B5 — read the pictures first

**Image:** `b5-read-the-pictures-first.jpg`

### FB post copy

📋 If someone hands you a written brief *and* reference images for a volume job — read the pictures first, and use the words to check them.

A brief we studied recently arrived as a 37-line written spec plus two reference image pairs. Same child, same pose, same crop, different background. One glance at that pair fixed a constraint the prose had spent a full paragraph failing to pin down.

Then go back to the words, hunting two specific things.

**Contradictions.** That brief banned any overlay of the arms and hands in one section, and appeared to permit props occluding the limbs in another — in a sentence that was missing its verb. Props sitting *behind* the child versus crossing *in front* of them is a visible decision, on every frame, across the entire order.

**Deliverables the template doesn't cover.** It named three framings — full body, half body, close-up — and supplied one template. The close-up crop excludes nearly every element that template describes. So a third of the order was, strictly speaking, unspecified.

Neither is a reason to walk away. Both are reasons to ask *before* you quote. Afterwards it's a change request you already sold at the old rate.

Posting it because the same two failures turn up in school and wedding volume work, and the fix costs nothing: read it properly, once, at the start. 👇

**First comment:** *(no link — invite replies)* `Curious what's caught people out on volume briefs before. What do you check now that you didn't use to?`

---

## B6 — why there are no children in any of these posts

**Image:** `b6-we-do-not-publish-children.jpg`

### FB post copy

🚫 A note on why there isn't a single child in any of these posts.

We don't publish photographs of children. Not our clients'. Not our own. Not generated ones either.

**Not our clients'.** Consent for a shoot is not consent for a portfolio. The parents agreed to a session, not to a marketing feed.

**Not our own.** A face put online at four is online at forty, and a studio's advertising isn't where that decision should get made.

**Not generated ones.** A synthetic child is still a child-shaped image posted into a group full of parents. We're not doing that either — and the fact that it's the easy shortcut is exactly why it's worth naming out loud.

It's also why the first post in this series makes its point on a serum bottle. The mechanism is identical and the bottle can't object.

So what do we show? The method. Diagrams, checklists, and the two or three things that actually go wrong. A before-and-after proves one edit. A checklist travels.

One practical use for this: if you're vetting an editor and their portfolio is full of other people's children, ask them who signed off on that. It's a fair question, and the answer tells you a great deal about how they'll handle your files.

Nobody imposed this rule on us. It's just the one we landed on. 👇

**First comment:** *(no link)* `Happy to talk through any of the method posts in this series — ask here rather than DM, it's more useful to everyone.`

---

## Placement

| Post | Group | When |
|---|---|---|
| B6 · no children | `857871658366623` Babies and Kids Photoshoot | **first** — it's the introduction, and it earns the right to post the rest |
| B1 · look at what moved | Babies and Kids Photoshoot · Inspired by Newborn Photography | week 1 — the strongest hook, and it needs B6 to explain the bottle |
| B2 · two pipelines | Inspired by Newborn Photography | week 2 |
| B4 · five places to look | Inspired by Newborn Photography · Photographers HIRING photographers | week 2 |
| B3 · write the notes out (shared image) | Babies and Kids Photoshoot | week 3 |
| B5 · read the pictures first | Photographers HIRING photographers | week 3 — the outsource-intent group |

**Join first, post later.** We are not yet a member of any of the three. Per §H1 the
join can take days and is often screened; apply to all three now, and read each feed
for a few days before posting so the register can be adjusted to what the group
actually tolerates.

**B6 goes first, deliberately.** In a parents-and-editors group, leading with a
teardown reads as marketing. Leading with a stated limit on our own behaviour does
not — and it also pre-answers the obvious question about B1, which is why there
is a cosmetics bottle in a child-photography group.

---

## Build note

- `b1-look-at-what-moved.jpg` — `make_b1_drift_card.py` (1200×1650). Reads
  `serum_scene_shelf.jpg`, `serum_scene_vanity.jpg` and `serum.png` from
  `dev/jayw/video_pipelines/ecommerce_to_video/products/gen/`. The bottom row's
  backdrops are gradient sweeps generated in the script, so the composite is
  reproducible and provably uses one cutout twice.
- `b2`, `b4`, `b5`, `b6` — `make_b_cards.py` (1200×1200).
- **B3 has no image of its own.** It runs `shared-retouching-blueprint.jpg`, the same
  file A6 runs — a copy of
  `curify-frontend/public/images/nano_insp/template-portrait-retouching-blueprint-en 1.jpg`.
  The two series held byte-identical copies under different names until 2026-09-11.

Palette throughout is the company-deck one: `#FAF8F2` ground, `#C0521E` accent,
`#3A6A54` for the good path, `#1A1A1A` reversed for B6.

---

# Shared — the mechanic, and the one stop rule

From the reddit doc §H0, and the thing most likely to be got wrong:

> The RedNote motion that produced 3 conversations and the ¥27,800 deal was
> **评论区触达 — comment-section outreach**, not DMs. […] **DM only after they
> reply to the comment.**

These fourteen posts are the standing exhibit, not the motion. The motion is: read the
group daily, find a post where someone **states a need in their own words**, and
reply in the comments with output on *their* product category — not a link, not a
deck, not a portfolio. The posts exist so that when someone clicks through after
that comment, there is something credible to find.

**Logging — one pilot, not three.** Series A, Series B and the 小红书 cut all log to
`gtm_tools/relationship_leads.json`, with `channel: "facebook_group"` or `"rednote"`,
`need_verbatim` (their exact words) and `need_confidence: "stated"`.
**Do not create a new file.**

**Stop rule: 20 comments, then evaluate** — counted across all three series together,
not 20 each. Not 20 posts read; 20 comments left. The small n is deliberate.
