# Etsy pack review + 4 new pack candidates — 2026-08-28

## Audit of the 12 existing packs

All 12 are `active: true` in both registries (frontend `lib/etsy_packs.json` and
backend `app/data/etsy_packs.json`), and both are in sync. Two findings matter.

**None of them is actually listed on Etsy.** `etsy_listing_url` is null on all 12.
We have built and uploaded 587 clean images across 12 ZIPs and wired a working
redemption flow, and no buyer can reach any of it. That is the binding constraint —
not the catalogue size.

**Two packs carry third-party IP and should not be listed as-is:**

| pack | issue |
|---|---|
| `mbti-character` (100 cards) | Titled "Marvel, Ghibli & Friends". Cover image is `template-mbti-marvel-en-captainamerica.jpg` — Captain America is the storefront image on a paid listing. |
| `zhenhuan-mbti` (16 cards) | "Empresses in the Palace" (甄嬛传) is a licensed TV property. |

Both are the *largest* and the most commercially obvious packs, which is exactly why
they are the risk. Etsy's IP takedown process is complaint-driven and account-level:
a single successful claim can suspend the shop, not just the listing. Recommend
delisting both from any launch set and replacing `mbti-character` with `mbti-animal`
(below), which covers the same buyer intent with no rights exposure.

## 4 new pack candidates — screened, no IP

Screened every template with ≥24 examples against a rights blocklist (studio IP,
franchises, real-person likenesses). Rejected on screening: `word-scene` (5 Crayon
Shin-chan entries), `mbti-nba` (5 real athletes), `mbti-siliconvalley` (4 real
founders), `original-character-sticker-pack` (4 entries are Hello Kitty / Mario
despite the template's "original-ip" tag).

### 1. `mbti-animal` — 49 examples, 0 flags · **top pick**
**Title:** MBTI Animal Personality Posters (49 Cards for All 16 Types)
**Description:** Every MBTI type as an animal character, illustrated as a printable
poster set. 49 cards covering all 16 types with trait summaries, cognitive-function
notes, and matching colour palettes. Print for a classroom wall, a therapy or
coaching practice, a team-building session, or a gift for the personality-test
obsessive in your life. High-resolution files, no watermark, print at A4 or Letter.

*Why:* personality content is proven Etsy demand and it is the same buyer as the
existing MBTI pack — without Marvel or Ghibli attached.

### 2. `education-card` — 72 examples, 0 flags
**Title:** Illustrated Science & Learning Cards (72 Classroom Printables)
**Description:** A 72-card illustrated reference set covering science and general
knowledge, drawn in a clean cartoon style that reads at wall distance. Each card
pairs a labelled diagram with a short explanation. Built for homeschool binders,
classroom walls, and morning-basket routines. Print-ready, no watermark, A4/Letter.

*Why:* largest clean pool we have, and homeschool printables are a durable Etsy
category with year-round demand rather than a seasonal spike.

### 3. `kids-vocabulary-poster` — 25 examples, 0 real flags
**Title:** Kids First Words Vocabulary Posters (25 Illustrated Wall Prints)
**Description:** 25 illustrated vocabulary posters covering first-words themes —
animals, food, colours, jobs, weather, and more. Each poster pairs bright artwork
with clear labels, sized for a nursery wall or a preschool classroom. Print at A4 or
Letter, no watermark, unlimited personal and single-classroom use.

*Note:* the screen flagged `…-jobs`; that is occupations vocabulary, a false positive.

### 4. `english-dialogue-scene` — 26 examples, 0 flags
**Title:** Everyday English Dialogue Scene Cards (26 ESL Conversation Posters)
**Description:** 26 illustrated scene cards showing everyday English conversations —
ordering food, asking directions, at the doctor, on the phone. Each card pairs a
kawaii-style scene with the full dialogue, so learners see the situation and the
language together. For ESL tutors, language classrooms, and self-study. Print-ready,
no watermark.

*Why:* ESL printables sell steadily and this is a format most competitors don't have —
the scene and the script on one card.

## Blocker before any of these can be sold

The gallery images on disk are **watermarked**. Every shipped paid pack has clean
renders in `packs/<sku>/` (12 dirs, 587 images); the `packs/template-*/` dirs are
empty placeholders. So each new pack needs its clean set generated before it can be
zipped and sold — roughly 172 images for all four. The free 5-card lead-magnet PDFs
can be built from watermarked gallery images today and already exist under
`raw/template-packs/` for `education-card` and `kids-vocabulary-poster`.

## Delivery automation (shipped)

`scripts/build_etsy_delivery_pdf.py` replaces the hand-made Canva file. One hero
image + one **tappable** link per SKU, with `?c=etsy-<sku>-listing` attribution baked
in so redemptions are traceable per listing.

    python scripts/build_etsy_delivery_pdf.py                 # all active packs
    python scripts/build_etsy_delivery_pdf.py mbti-animal     # one SKU
    python scripts/build_etsy_delivery_pdf.py --code=etsy-fall-sale travel-maps

Output: `raw/etsy-packs/<sku>-delivery.pdf`.
