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

---

# Etsy packs — 2026-09-04 build round (8 SKUs, 79 cards)

Catalogue went **17 → 25**. Registered in both registries, ZIPs built, `active: true`,
`etsy_listing_url` null. **Not yet live** — the frontend registry ships on a feature
branch and the backend needs its own deploy, so `/pack/<sku>` and the download
endpoint both 404 until those go out.

| SKU | cards | ZIP | delivery PDF |
|---|---|---|---|
| `character-breakdown` | 10 | 9.2 MB | — none built — |
| `travel-scrapbook` | 10 | 9.5 MB | — none built — |
| `landmark-posters` | 10 | 11.3 MB | — none built — |
| `travel-journal` | 10 | 11.1 MB | — none built — |
| `world-drinks` | 9 | 7.8 MB | — none built — |
| `artist-bios` | 10 | 10.7 MB | — none built — |
| `fashion-collage` | 10 | 9.0 MB | — none built — |
| `clothing-evolution` | 10 | 7.1 MB | — none built — |

Card counts and ZIP sizes were verified against the archives and match the registry
exactly. Watermark separation is correct: every pack copy spot-checked differs from
its same-named gallery copy, and the gallery copy is the one carrying the diagonal
mark.

## Etsy listing copy

As registered in both registries. **These are missing the format line** that all five
08-28 descriptions end with (*"No watermark, prints at A4 or Letter"*) — the 08-28
round established it, this round dropped it on all 8. Worth appending before listing,
with the caveat in *Print size* below.

### `character-breakdown` — 10 cards · 9.2 MB

**Title**

> Chinese Classic Character Design Sheets (10 Panoramic Breakdown Posters)

**Description**

> Character setting sheets for the great figures of Chinese classical literature: Sun Wukong, Zhu Bajie, Tang Sanzang, Lin Daiyu, Jia Baoyu, Wu Song, Lin Chong, Zhuge Liang, Guan Yu and Nezha. Each sheet centres a full-body illustration and rings it with the character's clothing layers, an expression set, signature props, material close-ups and everyday personal items, hand-annotated on aged paper. For concept artists, character designers, illustration students and reference walls.

### `travel-scrapbook` — 10 cards · 9.5 MB

**Title**

> Vintage Travel Scrapbook Posters (10 Hand-Drawn Journal Pages)

**Description**

> Hand-drawn travel journal pages for Kyoto, Santorini, Lisbon, Marrakech, Amalfi Coast, Reykjavik, Bali, New Orleans, Cape Town and Queenstown. Torn-paper backgrounds, watercolour splashes, polaroid snapshots, handwritten notes, doodled landmarks and a map pin on every page. For gallery walls, travel-lover gifts, scrapbooking and journal spreads.

### `landmark-posters` — 10 cards · 11.3 MB

**Title**

> Vintage World Landmark Info Posters (10 Illustrated Guides)

**Description**

> Illustrated landmark guides covering the Taj Mahal, the Eiffel Tower, the Great Wall of China, the Colosseum, Machu Picchu, Christ the Redeemer, Stonehenge, the Sagrada Familia, Angkor Wat and Neuschwanstein Castle. Each poster pairs a detailed hand-drawn illustration with the landmark's nickname, country flag, build date, dimensions and the facts a visitor actually wants, in the muted palette of a mid-century travel poster. For classrooms, hallways and travel-themed rooms.

### `travel-journal` — 10 cards · 11.1 MB

**Title**

> Watercolour Travel Journal Collages (10 Expedition Pages)

**Description**

> Watercolour expedition journals for Jungle Expedition, Alpine Mountain Ascent, Coastal Exploration, Autumn Forest Hike, Desert Trek, Arctic Expedition, Safari Journey, Island Sailing Voyage, Volcano Trail and Cherry Blossom Walk. An open vintage notebook sits at the centre of each collage, surrounded by the landscape of the journey, a retro film camera, pressed botanicals, maps and ticket stubs, all in soft washed watercolour. For nursery walls, study nooks and nature-journal lovers.

### `world-drinks` — 9 cards · 7.8 MB

**Title**

> Traditional Drinks of the World Infographics (9 Illustrated Posters)

**Description**

> Illustrated guides to the traditional drinks of Scotland, Ireland, the Caribbean, Germany, Brazil, Greece, Peru, Poland and Vietnam. Hand-drawn bottles, glasses and traditional vessels on a deep starred background, each labelled with its name and a one-line note on what it is and how it is served. For bars, kitchens, restaurants and home drinks corners.

### `artist-bios` — 10 cards · 10.7 MB

**Title**

> Artist Biography Infographic Posters (10 Art-History Prints)

**Description**

> Illustrated biography infographics for Katsushika Hokusai, Gustav Klimt, Johannes Vermeer, Georgia O'Keeffe, Henri Matisse, Rembrandt van Rijn, Edvard Munch, Wassily Kandinsky, Paul Cezanne and Hilma af Klint. Each print sets the artist's name and dates against a short account of their movement and legacy, a portrait, a signature-work strip and their working palette. For studios, classrooms, libraries and art-student walls.

### `fashion-collage` — 10 cards · 9.0 MB

**Title**

> Vintage Collage Fashion Lookbook Posters (10 Collection Boards)

**Description**

> Polaroid-collage lookbook boards across 10 collection themes: denim patchwork, french workwear, retro streetwear, coastal linen, monochrome tailoring, y2k pastel, earth knitwear, utility cargo, sheer romantic and preppy varsity. Aged beige paper, flowing script headlines, cut-out full-body model stickers, taped fabric swatches and handwritten margin notes. For boutique windows, brand mood boards, fashion-student portfolios and social campaign templates.

### `clothing-evolution` — 10 cards · 7.1 MB

**Title**

> Evolution of World Clothing Posters (10 Fashion-History Prints)

**Description**

> Clothing-history timelines for Scottish, Mexican, Russian, Victorian English, Spanish, Italian, Vietnamese, Nigerian, Turkish and Greek dress. Six eras per poster, each with a cartoon figure in period dress, the era name, a short style note and a numbered dotted timeline. Clean, kawaii and legible from across a room. For classrooms, costume departments and fashion-history teaching.

## Visual review — 3 ship, 1 fixable, 4 blocked

The 08-28 rule held exactly: **short structured labels render correctly, long prose
degrades**. Every pack that survived review is label-driven; every pack that failed
asked the model to write sentences.

### Ship after a size pass

- **`landmark-posters`** — strongest of the round. Spot-checked facts are right: Taj
  Mahal 1632–1653, dome ~73 m, UNESCO 1983; Stonehenge earliest phase ~3000 BC,
  tallest trilithon 7.3 m, sarsen circle ~33 m, inscribed 1986. Compass roses and
  flags are correct.
- **`artist-bios`** — dates, works and quotes check out across Hokusai (1760–1849,
  name adopted 1798, *Hokusai Manga* 1814, *Thirty-Six Views* 1830–32) and Munch.
  Two fixes: Munch's breakdown is dated **1902**, but the hospitalisation was **1908**
  (1902 is the Tulla Larsen shooting); and "Born in **Loten**" drops the ø in Løten.
- **`travel-scrapbook`** — attractive and legible. Nits: "Kyoto Chronicles**.**" has a
  stray full stop, one caption ends mid-sentence on a comma, and the Kyoto postmark
  reads **OCT 15, 1998** while a polaroid on the same sheet is captioned **'23**.

### Fixable

- **`character-breakdown`** — art is excellent, text is not proofed. On the Sun Wukong
  sheet alone: "Fo**o**cuing gaze", "Playful **emirk**", "**Bronze bronze** Mirror",
  "Jade Rabbit **deesign**", and "Moisturizing **calve**" (salve). Lin Daiyu has
  "**Miniatare** Incense Burner". Two further problems: headers are inconsistent across
  the set (*Sun Wukong / Journey to the West* vs *DREAM OF THE RED CHAMBER — LIN DAIYU:
  CONCEPT DEPTH BREAKDOWN* vs *NEZHA: PANORAMIC CHARACTER D…*), as are the layout
  systems; and the Sun Wukong sheet gives a Ming-dynasty mythological figure an
  **"Intimate Undergarment Layer"** of micro-fibre boxer briefs, *"Nimbus" brand*, plus
  a tube of *"Heavenly Glow"* moisturiser. Lin Daiyu handles the same slot correctly
  with a period 肚兜.

### Blocked

- **`clothing-evolution`** — *content is clean and accurate* (the 1746 Dress Act ban,
  the Victorian romantic revival and the six-era structure are all right), but **all
  ten posters carry a fabricated "Curify" logo baked into the top-left corner**, and
  it is a *different invented mark on every sheet* — a sun, a bee, a magnifying glass
  with a face, a blue badge, one rendered "Curify**,**" with a stray comma, and one
  multicolour "C" roundel that reads as a Google/Microsoft mark. This is in the **paid
  pack files**, not the watermarked gallery copies. Regenerate with the brand mark
  suppressed; nothing else about this pack needs work.
- **`world-drinks`** — four independent problems. **(1) Live trademarks rendered as
  branded product**: Drambuie and Irn-Bru (Scottish), Angostura Bitters and Mount Gay
  Rum (Caribbean), Metaxa (Greek), and a stag-head green bottle that is Jägermeister
  trade dress (German). Per the 08-28 note, Etsy IP complaints are account-level.
  **(2) Duplicate and orphan content**: the Scottish poster prints the Irn-Bru callout
  **twice** and leaves a seventh illustration unlabelled. **(3) Model junk in the
  artwork**: the Polish poster ends with a baked-in caption bar reading
  *"© Polish Traditional Drinks Infographic – Fun & Informative!"*, and Peruvian and
  Brazilian gloss names with themselves — *Pisco Sour (Pisco Sour)*, *Cachaça
  (Cachaça)* — six times on the Brazilian sheet. The Peruvian sheet also admits one
  entry does not belong: *"Leche de Tigre… \*Not an alcoholic drink."* **(4) Not a set**:
  3 landscape + 6 portrait, in at least three different illustration styles
  (painterly, flat doodle, kawaii-faces).
- **`fashion-collage`** — every board carries a **fabricated brand, street address and
  URL** in a footer bar: *"BRAND: PASTEL POP | SHOP NOW: WWW.PASTELPOP.COM | 123 RETRO
  AVE, FASHION CITY"*, *"RETRO THREADS CO. | 123 Vintage Ave, Cityville |
  retrothreads.com"*. These are advertisements, not wall art, and the invented domains
  may belong to someone. One handbag also carries a rhinestone **CK** monogram.
- **`travel-journal`** — the pack's whole premise is an open notebook, and **5 of 10
  notebooks are unreadable**. `desert-trek` is literal **Lorem Ipsum** (*"Lorem ipsum
  aszge coronum nom quammad…"*). `alpine-mountain-ascent` ("Here is ao more june sceams
  to chawt was a through a fain journel"), `island-sailing-voyage`, `autumn-forest-hike`
  and `coastal-exploration` are degraded prose; two of those also print the same entry
  twice. Clean: arctic, cherry-blossom, jungle, safari, volcano — though arctic
  misspells "**Arcitc** Circle" and the cherry-blossom sheet renders a **Canon AE-1**
  with legible branding.

## Print size — the format line needs a caveat

Native output is 768–1408 px on the long edge (848×1264 typical), unchanged from every
prior round. At A4 that is roughly **105 DPI**, not 300 — the 300 in the JPEG header is
metadata, not pixels. The five 08-28 descriptions already promise *"prints at A4 or
Letter"*; either upscale before listing or keep the claim to the size the pixels
actually support.

Aspect ratios are also not uniform **within** a pack, which matters for a set sold for
one gallery wall:

- `world-drinks` — 3 landscape 1408×768, 6 portrait 768×1376
- `landmark-posters` — 7 at 848×1264, 3 at 768×1376 (angkor-wat, christ-the-redeemer, stonehenge)
- `travel-scrapbook` — 9 at 1408×768, marrakech at 1200×896
- `artist-bios` — 9 at 1408×768, vermeer at 1376×768
- Uniform: `character-breakdown`, `clothing-evolution`, `fashion-collage`, `travel-journal`

## The concurrency race cost 42 of 79 gallery records

`generate_template_examples.cjs` was run in parallel. Each process reads
`nano_inspiration.json` whole at start and writes it whole at the end, so the last
writer wins. The images are all on disk and all 79 are in the ZIPs — but only **37
gallery records** were committed:

| pack | in ZIP | gallery records |
|---|---|---|
| `artist-bios` | 10 | 10 |
| `landmark-posters` | 10 | 10 |
| `clothing-evolution` | 10 | 9 |
| `character-breakdown` | 10 | 8 |
| `fashion-collage` | 10 | **0** |
| `travel-journal` | 10 | **0** |
| `travel-scrapbook` | 10 | **0** |
| `world-drinks` | 9 | **0** |

Checked against `HEAD`: none of the 42 missing ids existed before this round, so this
is lost writes, not `Skip (exists)`. The staging-dir collision is fixed (pid + random
suffix), but the JSON race is not — **run sequentially**, or re-sync the gallery after.

## Next

- Regenerate `clothing-evolution` without the brand mark — best content-to-effort ratio
  in the round.
- Proofread and re-render `character-breakdown`; drop the modern-underwear slot.
- Decide on `world-drinks`, `fashion-collage`, `travel-journal`: each needs a prompt
  change, not a retouch. All three are currently `active: true` in both registries.
- Re-sync the 42 lost gallery records.
- Append the format line to all 8 descriptions; build the 8 delivery PDFs.
