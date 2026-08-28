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

## Etsy listing copy

Exactly as registered in both registries — this is what renders on `/pack/<sku>`.

### `city-miniatures` — 30 cards · 28.5 MB

**Title**

> Miniature City Map Art Prints (30 World Cities)

**Description**

> Thirty world cities rendered as three-dimensional miniature landscapes built on their own antique street maps — Amsterdam, Istanbul, Kyoto, Prague, Seoul, Venice, Copenhagen, Edinburgh, Marrakech, Buenos Aires, Berlin, Vienna, Budapest, Stockholm, Helsinki, Dublin, Porto, Seville, Florence, Naples, Krakow, Bangkok, Singapore, Osaka, Taipei, Cape Town, Rio de Janeiro, Havana, Jaipur and Reykjavik. Each print folds the city's landmarks into a tiny diorama sitting on the map it grew from. For a travel gallery wall, a housewarming gift, or a memento of a city someone lived in. High resolution, no watermark, prints at A4 or Letter.

### `butcher-charts` — 30 cards · 25.3 MB

**Title**

> Vintage Butcher Chart Prints (30 Meat & Seafood Cut Guides)

**Description**

> Thirty vintage-style butcher charts showing where every cut comes from — duck, turkey, goose, quail, pheasant, goat, venison, rabbit, veal, bison, wild boar, mutton, and a full seafood set covering salmon, tuna, cod, halibut, trout, mackerel, sardine, red snapper, eel, squid, octopus, lobster, crab, prawn, scallop, oyster, mussel and clam. Each print pairs a full-body illustration with labelled cuts, clean pointer lines, and the cooking method each cut suits, in the muted palette of an old butcher's shop poster. For kitchens, butcher counters, restaurant walls, and anyone who cooks seriously. No watermark, prints at A4 or Letter.

### `confusing-english-words` — 30 cards · 21.5 MB

**Title**

> Commonly Confused English Words (30 Grammar Study Posters)

**Description**

> Thirty posters covering the word pairs that trip up native speakers and learners alike — then/than, lay/lie, fewer/less, who/whom, farther/further, principal/principle, stationary/stationery, bring/take, imply/infer, historic/historical, everyday/every day, assure/ensure, elicit/illicit, discreet/discrete, council/counsel, cite/site, peak/peek, capital/capitol, desert/dessert, breath/breathe, allusion/illusion, emigrate/immigrate, adverse/averse, appraise/apprise, born/borne, canvas/canvass, credible/creditable, disinterested/uninterested, flout/flaunt and pore/pour. Each gives both definitions, a worked example, a memory trick, and a wrong-vs-right correction panel. For ESL classrooms, English tutors, and writers' walls. No watermark, A4/Letter.

### `watercolor-maps` — 10 cards · 9.7 MB

**Title**

> Watercolor Region Map Prints (10 Illustrated Travel Maps)

**Description**

> Ten soft watercolor maps — the British Isles, Scandinavia, the Mediterranean, Southeast Asia, the Caribbean, the Alps, Japan, the Iberian Peninsula, New Zealand and Central America. Each country is washed in its own colour and labelled, with iconic landmarks and animals illustrated in place. Warm enough for a nursery wall and accurate enough for a classroom. Print as a set for a travel gallery wall or singly by region. No watermark, A4/Letter.

### `dessert-color-lab` — 10 cards · 6.2 MB

**Title**

> Dessert Colour Lab Prints (10 Patisserie Kitchen Posters)

**Description**

> Ten prints, each a nine-dessert grid built around a single colour story — blush pink, chocolate brown, citrus orange, matcha green, lavender, midnight black, caramel gold, berry wine, cream and ivory, turquoise mint. Every dessert is shot against its own matched background and named beneath. Equal parts colour study and patisserie menu. For kitchens, bakery walls, and food-styling reference. No watermark, A4/Letter.

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
