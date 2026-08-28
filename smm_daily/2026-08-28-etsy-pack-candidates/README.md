# Etsy packs — 2026-08-28 build round

Five new SKUs built, registered in both registries, uploaded to Azure, and live.
Catalogue went **12 → 17**.

| SKU | cards | ZIP | delivery PDF |
|---|---|---|---|
| `city-miniatures` | 30 | 28.5 MB | `etsy-packs/city-miniatures-delivery.pdf` |
| `butcher-charts` | 30 | 25.3 MB | `etsy-packs/butcher-charts-delivery.pdf` |
| `confusing-english-words` | 30 | 21.5 MB | `etsy-packs/confusing-english-words-delivery.pdf` |
| `watercolor-maps` | 10 | 9.7 MB | `etsy-packs/watercolor-maps-delivery.pdf` |
| `dessert-color-lab` | 10 | 6.2 MB | `etsy-packs/dessert-color-lab-delivery.pdf` |

All `active: true`, ZIPs at `packs/sku/<sku>/pack-v1.zip`, ~150 clean
(pre-watermark) images generated, gallery copies watermarked and synced to CDN.
`etsy_listing_url` is null on all of them — that field is simply not backfilled;
listings are created manually on Etsy.

## What each pack is

- **city-miniatures** — 30 world cities as 3D miniature dioramas built on their own
  antique street maps. Amsterdam, Istanbul, Kyoto, Prague, Seoul, Venice, Berlin,
  Vienna, Reykjavik, Havana, Jaipur and more.
- **butcher-charts** — 30 vintage butcher charts. Duck, turkey, goat, venison,
  rabbit, salmon, tuna, lobster, crab, octopus, squid, quail, veal, bison and more,
  each with labelled cuts and cooking methods.
- **confusing-english-words** — 30 grammar posters. then/than, lay/lie, fewer/less,
  who/whom, principal/principle, stationary/stationery, imply/infer, flout/flaunt
  and more, each with both definitions, a worked example and a memory trick.
- **watercolor-maps** — 10 watercolor region maps. British Isles, Scandinavia,
  Mediterranean, Southeast Asia, Caribbean, Alps, Japan, Iberian Peninsula,
  New Zealand, Central America.
- **dessert-color-lab** — 10 nine-dessert grids, each built on one colour story:
  blush pink, chocolate brown, citrus orange, matcha green, lavender, midnight
  black, caramel gold, berry wine, cream & ivory, turquoise mint.

## The rule that decides whether a template is packable

**Short structured labels render correctly. Long prose paragraphs degrade into
gibberish.** This predicts sellability without inspecting every file:

- Clean — butcher-chart cut labels (one or two words), word-pair definitions and
  examples, dessert names, map country labels. Spot-checked and factually right:
  the fewer/less poster gets countable-vs-uncountable correct, squid anatomy
  correctly separates arms from tentacles.
- Garbled — `great-minds` one-sentence achievement blurbs: *"GEOCERTAIC NODCE:
  Beselaped the Earth-conterêd oaiverse Ibeary"*. Names and dates survive;
  sentences do not.

## `great-minds` — generated, NOT shipped

10 images sit in `packs/great-minds/` and are deliberately unregistered. Two
independent blockers:

1. **The text is the product.** On a decorative print, garbled lettering reads as
   texture. On a classroom reference poster, the blurb is what someone buys.
2. **Right-of-publicity.** The template fills category themes (astronomers, poets)
   with *named individuals*, and it chose **Carl Sagan** (d. 1996) and **Vera
   Rubin** (d. 2016) — recent enough that heirs hold publicity rights.

Fixing it needs a pre-1900-deaths prompt constraint plus a regeneration.

## Two existing packs carry third-party IP

Not from this round, but found while auditing and worth acting on:

- **`mbti-character`** (100 cards) — titled "Marvel, Ghibli & Friends", and its
  cover image is `template-mbti-marvel-en-captainamerica.jpg`, i.e. Captain America
  is the storefront image on a paid listing.
- **`zhenhuan-mbti`** (16 cards) — "Empresses in the Palace" is a licensed property.

Etsy IP claims are account-level: one successful complaint can suspend the shop,
not just the listing. `mbti-animal` (49 clean examples, screened) is the drop-in
replacement at the same buyer intent.

Also screened and rejected as pack candidates: `word-scene` (5 Crayon Shin-chan),
`mbti-nba` (5 real athletes), `mbti-siliconvalley` (4 real founders),
`original-character-sticker-pack` (4 are Hello Kitty / Mario despite the
template's own "original-ip" tag).

## Tooling built this round

- `scripts/build_etsy_delivery_pdf.py` — replaces the hand-made Canva file. One
  hero + one **tappable** link per SKU with `?c=etsy-<sku>-listing` attribution.
  Writes to `curify-gallery/etsy-packs/`. Uses the clean pack image as the hero,
  not the same-named watermarked gallery copy.
- `scripts/register_etsy_pack.py` — zips a pack folder and writes **both**
  registries from one record, refusing a partial pair. Updates existing SKUs in
  place, so a pack grown 10 → 30 does not keep advertising 10 cards.
- Ordering that matters: register (inactive) → upload ZIP → `--activate`.

## Two traps worth remembering

**`build_topic_thumbnails.cjs` is not idempotent housekeeping.** Re-running it
after a content drop deleted the `branding`, `packaging` and `social-media-posts`
thumbnails and replaced `portrait`'s curated icon — `TopicStrip` drops any entry-bar
item without a manifest thumbnail, so it would have silently removed three items
from site-wide navigation. Check its diff against `lib/entry_bar.ts` before ever
committing it.

**Never filter the generator's output.** `generate_template_examples.cjs` prints a
per-item `✗ {error}` line but ends with a tidy Added/Skipped/Failed block and
**exits 0 even when every item fails**. A 60-image run returned 0/60 with exit 0;
piping through `grep "^Added|^Failed"` hid the cause. It was
`429 RESOURCE_EXHAUSTED — monthly spending cap`, visible only on an unfiltered rerun.

## Next

- Scale `watercolor-maps` and `dessert-color-lab` from 10 to 30 (both have unused
  subject headroom).
- Regenerate `great-minds` with a pre-1900 constraint, or drop it.
- Replace `mbti-character` with `mbti-animal`; retire `zhenhuan-mbti`.
