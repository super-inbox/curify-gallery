# Etsy packs batch 2 — 2026-08-28

Generated 40 clean images across 4 templates, 10 each, 0 failures. **Three ship,
one is held.**

| SKU | cards | ZIP | text quality | status |
|---|---|---|---|---|
| `butcher-charts` | 10 | 8.5 MB | clean | **shipped** |
| `confusing-english-words` | 10 | 7.2 MB | clean | **shipped** |
| `dessert-color-lab` | 10 | 6.2 MB | clean | **shipped** |
| `great-minds` | 10 | 18 MB | garbled | **HELD** |

## The pattern that decides whether a template is sellable

**Short structured labels render correctly. Long prose paragraphs degrade into
gibberish.** This is the single most useful thing learned from the batch and it
predicts which templates can be sold without inspection:

- `butcher-charts` — labels are one or two words (NECK, BREAST, THIGH, GIBLETS)
  plus short cooking methods. All correct, and the duck anatomy is accurate.
- `confusing-english-words` — short definitions and example sentences. Fully
  correct: "fewer" for countable, "less" for uncountable, with a right/wrong
  correction panel that is genuinely right.
- `dessert-color-lab` — nine two-to-three-word dessert names. All clean.
- `great-minds` — one-sentence achievement blurbs per figure. **Garbled**:
  "GEOCERTAIC NODCE: Beselaped the Earth-conterêd oaiverse Ibeary", "LANS GE
  PLANETARY NOTIOS: Fanaulated Hass leos describing the matian el planets".

Names and dates survive; sentences do not. Any future pack whose value IS the
prose should be inspected before listing, or restructured to short labels.

## Why `great-minds` is held — two reasons, either sufficient

**1. The text is the product.** On a decorative print, garbled lettering reads as
texture. On a classroom reference poster, the blurb is the reason someone buys it.
Shipping nonsense there is different in kind from the antique-map lettering on the
city miniatures.

**2. Right-of-publicity, and this corrects an earlier call.** I had cleared this
template on the grounds that its themes are categories (astronomers, poets) rather
than named people. That reasoning was wrong: the model FILLS each category with
named individuals, and it picked **Carl Sagan (d. 1996)** and **Vera Rubin
(d. 2016)** — both recent enough that heirs hold publicity rights. Same exposure
that held back `historical-figure-biography-vintage-infographic`, arriving through
a different door.

Fixing it needs a prompt constraint limiting figures to pre-1900 deaths, then a
regeneration. Not attempted here.

## Catalogue now

17 SKUs registered in both registries. Shipped this session: `city-miniatures`,
`watercolor-maps`, `butcher-charts`, `confusing-english-words`, `dessert-color-lab`
— all active, ZIPs on Azure, delivery PDFs built with clean heroes and tappable
attribution links.


---

## Content drop — 2026-08-28 (the generated images are live in the gallery)

170 records across the 6 templates are in `nano_inspiration.json`, all with asset
URLs, auto-tagged topics and search_aliases, and `locales` (en/zh). Full images and
previews verified 200 on the CDN. They surface on topic pages automatically —
travel 97, food 87, language 209, wall-art 150, city 43 tagged inspirations.

**Nothing further was needed, and two "obvious" steps were deliberately skipped:**

**`regen_nanobanana_metadata.cjs` — wrong target.** It regenerates prompt-tag
metadata from `nanobanana.json` (the gallery prompt corpus), not
`nano_inspiration.json`. New template examples do not flow through it.

**`build_topic_thumbnails.cjs` — RAN IT, IT WAS HARMFUL, REVERTED.** The regen
picks thumbnails dynamically from current inspirations, and adding 100 images
shifted the picks: it DELETED thumbnails for `branding`, `packaging` and
`social-media-posts`, and replaced `portrait`'s curated
`/images/topic_icon/portrait-selfie.jpg` with an arbitrary inspiration preview.
All four are entry-bar items, and `TopicStrip` drops any item without a manifest
thumbnail — so running this "housekeeping" regen would have silently removed three
entries from the site-wide navigation bar. Reverted; all four confirmed restored.

Lesson: this generator is not idempotent housekeeping. It re-derives from whatever
content exists at the time, so a content drop can quietly change navigation. Check
the diff against `lib/entry_bar.ts` before committing it, ever.

**10-locale example i18n was not added.** Only 15 of the 170 are `allow_i18n`. The
sitemap already culls i18n-authored examples with zero GSC visibility (the B1 rule),
so authoring 10 locales for 100 brand-new examples would be dropped by our own
pipeline before it earned an impression.