# Operator-picked templates for Etsy packs — 2026-08-28

Seven templates requested. All exist. Two things need deciding before any becomes a
listing: **example counts are below pack size**, and **one template carries
right-of-publicity risk**.

## Counts — every one is under the bar

Smallest shipped pack is 16 cards (`zhenhuan-mbti`); the median is 40.

| template | examples | verdict |
|---|---|---|
| `city-miniature` | 16 | at the floor — shippable alone |
| `english-confusing-word-pair-educational-poster` | 8 | needs +8 |
| `watercolor-world-map-illustration` | 7 | needs +9 |
| `anatomy-cut-guide` | 7 | needs +9 |
| `historical-figure-educational` | 6 | needs +10 |
| `dessert-color-lab-infographic` | 6 | needs +10 |
| `historical-figure-biography-vintage-infographic` | 6 | see IP note |
| **total** | **56** | |

Two routes: generate up to size (~46 clean images for six packs), or bundle
thematically today with zero generation. Bundles that clear 16 right now:

- **Watercolor Travel Wall Art** — `watercolor-world-map` (7) + `city-miniature` (16) = **23**
- **Vintage Educational Poster Set** — `anatomy-cut-guide` (7) + `historical-figure-educational` (6) + `dessert-color-lab` (6) = **19**

## IP: one template must be filtered

`historical-figure-biography-vintage-infographic` — 3 of its 6 examples are
**post-mortem right-of-publicity** risks, not public-domain history:

- `bruce-lee` — Bruce Lee Enterprises licenses and enforces the likeness
- `michael-jackson` — estate enforces aggressively
- `nelson-mandela` — Nelson Mandela Foundation controls name and image

Safe in the same set: `confucius`, `elizabeth-i`, `robin-hood` (public domain /
fictional). California right of publicity runs 70 years post-mortem, so "he died
decades ago" is not a defence. **Drop those three, or drop the template.** With them
removed it has 3 usable examples, which is not a pack.

`historical-figure-educational` is unaffected — its examples are categories
(artists, composers, philosophers, scientists, writers), not named individuals.

## Titles + descriptions

### `city-miniature` — 16, ready now
**Title:** Miniature City Map Art Prints (16 World Cities)
**Description:** Sixteen world cities rendered as three-dimensional miniature
landscapes built on their own street maps — Paris, Tokyo, New York, Barcelona, Rome,
Mumbai, Oaxaca and more. Each print folds the city's landmarks into a tiny diorama
that still reads as the real map underneath. For a travel gallery wall, a
housewarming gift, or a memento of a city someone lived in. High resolution, no
watermark, prints at A4 or Letter.

### `watercolor-world-map-illustration` — 7
**Title:** Watercolor Continent Map Prints (Illustrated World Map Set)
**Description:** Soft watercolor maps of every continent, each country washed in its
own colour and labelled, with iconic landmarks and animals illustrated in place. Warm
enough for a nursery wall and accurate enough for a classroom. Print as a set for a
world-map gallery wall or singly by continent. No watermark, A4/Letter.

### `anatomy-cut-guide` — 7
**Title:** Vintage Butcher Chart Prints (Meat Cut Guide Poster Set)
**Description:** Vintage-style butcher charts showing where each cut comes from —
beef, pork, lamb, chicken, fish, plus a coffee-bean anatomy print. Full-body
illustration with every cut labelled and lines drawn to the joint, in the muted palette
of an old butcher's shop poster. For kitchens, butcher counters, steakhouse walls, and
anyone who cooks seriously. No watermark, A4/Letter.
*Note: this template is meat cuts, not zoological anatomy — the name misleads.*

### `historical-figure-educational` — 6
**Title:** Great Minds Educational Posters (Artists, Scientists & Thinkers)
**Description:** Illustrated poster set grouping the figures who shaped each field —
artists, composers, philosophers, scientists and writers — with portraits, dates and a
short line on what each is known for. Built as a classroom or study-wall reference
rather than decoration alone. Print-ready, no watermark, A4/Letter.

### `dessert-color-lab-infographic` — 6
**Title:** Dessert Colour Lab Prints (Patisserie Kitchen Art Set)
**Description:** Each print is a nine-dessert grid built around a single colour story —
vibrant red, golden, mystic purple, serene blue, fresh green — every dessert shot
against its own matched background and named beneath. Equal parts colour study and
patisserie menu. For kitchens, bakery walls, and food-styling reference. No watermark,
A4/Letter.

### `english-confusing-word-pair-educational-poster` — 8
**Title:** Commonly Confused English Words Posters (Grammar Study Set)
**Description:** Eight posters covering the pairs that trip up native speakers and
learners alike — affect vs effect, its vs it's, your vs you're, their vs there, loose
vs lose, accept vs except, advice vs advise, complement vs compliment. Each poster
gives both definitions, a worked example, and a memory trick. For ESL classrooms,
English tutors, and writers' walls. No watermark, A4/Letter.

### `historical-figure-biography-vintage-infographic` — HOLD
Do not build until `bruce-lee`, `michael-jackson` and `nelson-mandela` are removed and
replaced with public-domain figures. Copy withheld deliberately — writing a listing
for it now would make a rights problem easier to ship by accident.

## Next step

Say which route: **bundle** the two viable groupings above and list this week with no
generation, or **generate ~46 clean images** to bring six templates to 16+ each. Either
way the clean-image constraint from the main audit still applies — gallery renders on
disk are watermarked, and only `packs/<sku>/` holds sellable files.


---

# GENERATION RUN — 2026-08-28 · 16 clean images · **hold before listing**

Ran `generate_template_examples.cjs --config=scripts/configs/etsy_travel_wall_art_2026-08-28.json
--pack=travel-wall-art`. Result: **16 added, 0 failed**, 16 MB of clean
(pre-watermark) JPGs in `packs/travel-wall-art/`. Review ZIP at
`raw/etsy-packs/travel-wall-art-v1-REVIEW.zip`.

No `--sync`, so nothing is on the CDN. Nothing uploaded to Azure, and the SKU is
**not** registered — deliberately, see below.

Subjects (no overlap with the 23 existing): Amsterdam, Istanbul, Kyoto, Prague,
Seoul, Buenos Aires, Edinburgh, Marrakech, Venice, Copenhagen · British Isles,
Scandinavia, Mediterranean, Southeast Asia, Caribbean, The Alps.

## The 16 do NOT form one sellable pack. Two problems.

**1. The 10 city miniatures have garbled text baked into the artwork.**
Checked 2 of 10, both bad:
- *Amsterdam* — cartouche reads "DIE LOVERLA AMSTERDAM / VARECHEMY 17th CENTURY /
  TOMBAY"; street labels are gibberish ("Kldd mans", "Diesd Isde", "Priasrograsd raten").
- *Kyoto* — title block reads `大吉親京都`, which is not a phrase.

The template composes the diorama on top of an antique map, and the model invents the
map lettering. At Etsy-thumbnail size it passes as aged-map texture. At 300 DPI on a
wall it is visibly nonsense, and that is a refund-and-one-star risk on a paid print,
not a cosmetic nit. This is the same class of failure as the known CJK-garbling issue,
except it also affects Latin script here.

**2. The two halves do not look like one product.** The watercolor maps are flat,
light, landscape illustrations; the city miniatures are dark, photorealistic portrait
dioramas. A buyer expecting a matched set gets two unrelated aesthetics.

**The 6 watercolor maps are clean and sellable** — verified Scandinavia: correct
country labels (Norway / Sweden / Denmark), landmarks, compass rose, no watermark, no
garbled text. Only Finland is left unlabelled.

## Three ways forward — operator's call

1. **Ship the maps only.** Clean today, but 6 images is under the 16 floor; needs ~10
   more regions (Iberia, Balkans, Japan, East Africa, Central America, Baltics…).
   Cheapest path to a defensible product.
2. **Regenerate the cities with a no-text constraint** — force the map layer to be
   texture without lettering. Fixes the defect but costs another 10 generations and
   the style-mismatch in (2) remains.
3. **Ship all 16 anyway.** Only if the listing photos avoid close crops of the
   lettering. I would not: the buyer prints it large, which is the whole point.

**Recommendation: (1) then (2)** — sell the watercolor map set as its own coherent
product, and treat city miniatures as a separate SKU once the text is fixed. They were
never really one pack; bundling them was a way to clear the 16 floor, and the floor is
the wrong reason to combine two different products.

## RESOLVED 2026-08-28 — split into two SKUs of 10

Operator ruled the baked-in map lettering acceptable, and split the bundle. Topped the
maps up by 4 (Japan, Iberian Peninsula, New Zealand, Central America) to reach 10.

| SKU | cards | ZIP | delivery PDF |
|---|---|---|---|
| `city-miniatures` | 10 | 9.3 MB | 1,146 KB |
| `watercolor-maps` | 10 | 9.7 MB | 1,256 KB |

Registered in **both** registries (frontend + backend, 14 packs each, in sync).
`active: false` on both — the ZIPs are not on Azure yet, so the landing page must not
go live until `build_template_packs.cjs --mode=sku` uploads them.

**Remaining, operator-side:**
1. `node scripts/build_template_packs.cjs --mode=sku --sku=city-miniatures,watercolor-maps`
   (uploads the ZIPs to Azure) — then flip `active: true` in both registries.
2. `node scripts/sync_nano_inspiration.cjs` if the 20 new gallery examples should also
   appear publicly (watermarked copies; the clean pack bytes stay private).
3. Create the Etsy listings and paste the `etsy_listing_url` back into both registries.
   **This is still the binding constraint — 14 packs built, 0 listed.**
