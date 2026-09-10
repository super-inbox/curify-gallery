# FB Groups · Child photography — 6 posts (2026-09-01)

Third pass in the buyer-side pilot, after
`2026-09-01-fb-retouching/` + `2026-09-01-fb-ecommerce/`. Source material is **client-008**
(场景增强 — locked-subject background enrichment for a children's portrait studio),
recorded at
`agentic-adhoc-inbox/real-projects/projects/2026-08-31-client-008-context-enrichment.json`.

**Register:** value teardown, soft CTA — same as the retouching series, and more
necessary here. This audience is parents and small studios, and a service ad in
front of them reads worse than in any e-commerce group.

**House constraints:** single image, never a carousel; no external link in the post
body; CTA in the first comment; upload natively.

---

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
than a stock before/after would have been.** Post 1's image is built entirely from
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
person.** `../2026-09-01-fb-retouching/07-locked-subject-three-backdrops.jpg` is one
frame moved to three backdrops with the subject held: same face, same knit, same
pose. The subject is **synthetic and an adult**, so it clears both constraints above
— no likeness question, and no child-shaped image in front of a group of parents.
It is the same claim as post 1's bottle, made on the body plan that actually matters
to this audience, and it lands harder. The bottle post keeps its slot; treat 07 as a
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
chosen and none has been tested."* Post 2 says so. Do not let that line get edited
out.

---

# Post 1 — look at what moved

**Image:** `01-look-at-what-moved.jpg`

## FB post copy

🔬 Two runs of the same product through the same pipeline. Look at the bottle, not the background.

Top row: two scenes generated separately. Same product, same prompt family, and the bottle came back **different both times**. The pump collar is a single smooth sleeve in one and a stepped collar with a visible ring in the other. The label goes from opaque white with a hard edge to translucent grey. The shoulder goes from narrow and square to wide and rounded.

Nobody staged that. It's just what two runs produced.

Bottom row: the same product, cut out once, dropped onto two different backdrops. Byte-identical in both — not because anyone asked for it, but because the subject never went into the model at all.

This is a serum bottle, so the stakes are a redrawn label. Run the same process on a portrait and the thing that comes back subtly different is a face.

If you're sending children's portraits out for background work, this is the whole question in one image. Which row is your editor delivering? 👇

**First comment:** `The mechanism, and how to tell which one you got → curify-ai.com/blog/preserve-facial-features-ai-generation`

---

# Post 2 — two pipelines

**Image:** `02-two-pipelines.jpg`

## FB post copy

🧷 Following on from the bottle: there are two ways to replace a background, and they are not variations of the same thing.

**Full-frame diffusion.** The whole photo goes into the model, the whole photo comes out. Every pixel is perturbed by construction — that isn't a bug in someone's settings, it's what the method does. The face comes back changed. Often subtly enough that you sign it off.

**Segment → generate background → composite.** The subject is cut out first. The background is generated separately. The original subject pixels are pasted back. They're untouched *by definition* — not because someone asked nicely, but because they never entered the model.

This is why "please don't change the child" in a prompt is not a control. **A prompt is a request. Compositing is a guarantee.**

Fair warning on my own claim: this is our reading of the problem from a brief we studied closely, not a tested result — we haven't run it. But it's worth knowing the difference before you buy.

If your editor can't tell you which of the two they do, that's information as well. 👇

**First comment:** `Longer write-up on keeping identity locked through an edit → curify-ai.com/blog/preserve-facial-features-ai-generation`

---

# Post 3 — write the notes out

**Image:** `03-write-the-notes-out.jpg`
*(our own portrait-retouching template example, an adult — deliberately)*

## FB post copy

✍️ The fastest way to ruin a child's portrait in the edit is to write the brief in adjectives.

Glow-up. Clean up. Flawless. Makeover. Every one of those pushes an editor — human or model — straight to porcelain. Pores gone, freckles gone, the scab on the knee gone. Parents notice. They often can't name what's wrong, but they know it isn't their kid.

Write it out instead, region by region:

· **Skin** — even the tone, reduce shine. Keep the texture. Keep the freckles.
· **Eyes** — take down redness if you must. Don't reshape, don't enlarge.
· **Hair** — tame the one flyaway crossing the face. Leave the rest.
· **Background** — soften, balance the fill.
· And the line that belongs on every children's brief: **no smoothed or plastic retouching.**

That last one isn't clever. It's the sort of line studios end up writing into their briefs in plain language after being burned a few times, and it works precisely because it says what *not* to do.

The example image is an adult on purpose — reason in post 6 of this series. The method is identical.

The test for any brief, whether it's going to a person or a model: **could someone else execute it without asking you a question?** 👇

**First comment:** `Ten worked examples of specific-over-aspirational retouching notes → curify-ai.com/blog/50-ai-makeover-prompts`

---

# Post 4 — five places to look

**Image:** `04-five-places-to-look.jpg`

## FB post copy

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

# Post 5 — read the pictures first

**Image:** `05-read-the-pictures-first.jpg`

## FB post copy

📋 If someone hands you a written brief *and* reference images for a volume job — read the pictures first, and use the words to check them.

A brief we studied recently arrived as a 37-line written spec plus two reference image pairs. Same child, same pose, same crop, different background. One glance at that pair fixed a constraint the prose had spent a full paragraph failing to pin down.

Then go back to the words, hunting two specific things.

**Contradictions.** That brief banned any overlay of the arms and hands in one section, and appeared to permit props occluding the limbs in another — in a sentence that was missing its verb. Props sitting *behind* the child versus crossing *in front* of them is a visible decision, on every frame, across the entire order.

**Deliverables the template doesn't cover.** It named three framings — full body, half body, close-up — and supplied one template. The close-up crop excludes nearly every element that template describes. So a third of the order was, strictly speaking, unspecified.

Neither is a reason to walk away. Both are reasons to ask *before* you quote. Afterwards it's a change request you already sold at the old rate.

Posting it because the same two failures turn up in school and wedding volume work, and the fix costs nothing: read it properly, once, at the start. 👇

**First comment:** *(no link — invite replies)* `Curious what's caught people out on volume briefs before. What do you check now that you didn't use to?`

---

# Post 6 — why there are no children in any of these posts

**Image:** `06-we-do-not-publish-children.jpg`

## FB post copy

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

# Placement

| Post | Group | When |
|---|---|---|
| 6 · no children | `857871658366623` Babies and Kids Photoshoot | **first** — it's the introduction, and it earns the right to post the rest |
| 1 · look at what moved | Babies and Kids Photoshoot · Inspired by Newborn Photography | week 1 — the strongest hook, and it needs post 6 to explain the bottle |
| 2 · two pipelines | Inspired by Newborn Photography | week 2 |
| 4 · five places to look | Inspired by Newborn Photography · Photographers HIRING photographers | week 2 |
| 3 · write the notes out | Babies and Kids Photoshoot | week 3 |
| 5 · read the pictures first | Photographers HIRING photographers | week 3 — the outsource-intent group |

**Join first, post later.** We are not yet a member of any of the three. Per §H1 the
join can take days and is often screened; apply to all three now, and read each feed
for a few days before posting so the register can be adjusted to what the group
actually tolerates.

**Post 6 goes first, deliberately.** In a parents-and-editors group, leading with a
teardown reads as marketing. Leading with a stated limit on our own behaviour does
not — and it also pre-answers the obvious question about post 1, which is why there
is a cosmetics bottle in a child-photography group.

---

# Logging

Same as the other passes: `gtm_tools/relationship_leads.json`,
`channel: "facebook_group"`, `need_verbatim`, `need_confidence: "stated"`.
**Do not create a new file.** These comments count toward the same **20-comment stop
rule** — one pilot across all three passes, not three pilots.

---

# Build note

- `01-look-at-what-moved.jpg` — `make_01_drift_card.py` (1200×1650). Reads
  `serum_scene_shelf.jpg`, `serum_scene_vanity.jpg` and `serum.png` from
  `dev/jayw/video_pipelines/ecommerce_to_video/products/gen/`. The bottom row's
  backdrops are gradient sweeps generated in the script, so the composite is
  reproducible and provably uses one cutout twice.
- `02`, `04`, `05`, `06` — `make_child_cards.py` (1200×1200).
- `03-write-the-notes-out.jpg` — copy of
  `curify-frontend/public/images/nano_insp/template-portrait-retouching-blueprint-en 1.jpg`.

Palette throughout is the company-deck one: `#FAF8F2` ground, `#C0521E` accent,
`#3A6A54` for the good path, `#1A1A1A` reversed for post 6.
