# Instagram lead sheet — the three narrow landing offers

_2026-09-08. 20 handles per offer, taken from businesses **already qualified on condition ④** (they demonstrably pay for this today), not from Instagram keyword search._

## Where these came from, and why not Instagram search

Instagram's search matches account **names**, so querying `jewelry brand` returns accounts literally called that — mostly dormant or spam. These handles were instead taken from the **own websites** of leads that already passed the condition-④ gate, so each is a real operating business in the ICP with its evidence recorded beside it. Same populations as the email batches (`gtm_tools/batch_*_2026-09-08.json`), so a business can be worked on either channel — but not both at once without noting it.

Spot-checked live: **@slownorth** 28.7K followers / 2,480 posts (candle brand with a storefront), **@indirap** 5.9K / 3,054 ("Video Production Service"). Follower counts for the rest are **unverified** — worth a pass before prioritising.

## The mechanic — read this before touching any handle

The ¥27,800 RedNote deal converted through **评论区触达 — comment sections, not DMs**
(`reddit-demand-mining-buyer-side-2026-08-31.md` §H0). A cold DM to a non-follower lands in
Message Requests and breaks condition ② (回应不算越界). "Outreach" defaults to "DM" everywhere
else we run, which is exactly how this list gets used wrong.

**So: comment first. DM only after they reply to the comment.**

And the opener discipline from `relationship_leads.md`: for `ecommerce_visual_buyer`,
**reply with output, not a deck** — generate 2-3 frames on *their* product and post those.
Not a link, not a pitch, not a portfolio.

⚠️ Log every touch in `gtm_tools/outreach_denominator.csv`, same five columns as email and
Facebook, or this channel ends up like RedNote: a result with no denominator, uncomparable to
anything. Track leads in `gtm_tools/relationship_leads.json` with `channel: "instagram"` —
**do not create a new tracker**, the INDEX rule is that tables split by reply mechanic.


## Ecommerce — 1 SKU → product images + on-model + short video

Small brands that own a product and sell it online. Qualified on a live storefront / SKU breadth **and** evidence they already pay for content (lookbook, campaign, model imagery, video in use).

⚠️ **On-model is not a shipped tool** — it exists only as `dev/jayw/design-agent-v0/tools/model-swap`. Offer it as work we run, never as something they can log into.

_56 qualified handles available; top 20 by evidence strength._

| # | Handle | Business | Type | Why they qualify (④) |
|--:|---|---|---|---|
| 1 | [@slownorth](https://instagram.com/slownorth) | Slow North | home | live storefront; SKU breadth; restock/drop cadence; priced publicly; wholesale/retail line; paid |
| 2 | [@luxechiccoutureboutique](https://instagram.com/luxechiccoutureboutique) | Luxechic Couture Boutique | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; paid content already; runs  |
| 3 | [@customjewelrylab](https://instagram.com/customjewelrylab) | Custom Jewelry Lab | jewelry | live storefront; SKU breadth; priced publicly; wholesale/retail line; paid content already; runs |
| 4 | [@midnightpacific](https://instagram.com/midnightpacific) | Midnight Pacific Studio & Jewelry  | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; wholesale/retail line; runs |
| 5 | [@essanceskincare](https://instagram.com/essanceskincare) | Essance Skincare | beauty | live storefront; SKU breadth; restock/drop cadence; priced publicly; paid content already; runs  |
| 6 | [@noirluxcandleco](https://instagram.com/noirluxcandleco) | Noir Lux Candle Bar | home | live storefront; SKU breadth; restock/drop cadence; priced publicly; wholesale/retail line; runs |
| 7 | [@pumarosacandles](https://instagram.com/pumarosacandles) | Pumarosa Candles | home | live storefront; SKU breadth; restock/drop cadence; priced publicly; wholesale/retail line; runs |
| 8 | [@hemline_austin](https://instagram.com/hemline_austin) | Hemline Austin | apparel | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 9 | [@hollierayboutique](https://instagram.com/hollierayboutique) | Hollie Ray Boutique | apparel | live storefront; SKU breadth; priced publicly; paid content already; runs paid ads; video in use |
| 10 | [@jugrnaut](https://instagram.com/jugrnaut) | Jugrnaut | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; paid content already; video |
| 11 | [@pinkskyboutique](https://instagram.com/pinkskyboutique) | Pink Sky Boutique | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 12 | [@judithbright](https://instagram.com/judithbright) | Judith Bright Jewelry Nashville | jewelry | live storefront; SKU breadth; priced publicly; paid content already; runs paid ads; video in use |
| 13 | [@betsyandiya](https://instagram.com/betsyandiya) | Betsy & Iya | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 14 | [@studiomnm](https://instagram.com/studiomnm) | M&M Jewelry Studio | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 15 | [@regalstudiojewelry](https://instagram.com/regalstudiojewelry) | Regal Studio | jewelry | live storefront; SKU breadth; wholesale/retail line; paid content already; runs paid ads; video  |
| 16 | [@spruce.apothecary](https://instagram.com/spruce.apothecary) | Spruce Apothecary | jewelry | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 17 | [@taos_bos](https://instagram.com/taos_bos) | Tao's - Chinatown | beauty | live storefront; SKU breadth; restock/drop cadence; priced publicly; paid content already; runs  |
| 18 | [@shopgoodco](https://instagram.com/shopgoodco) | Shop Good | beauty | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 19 | [@shopgoodco](https://instagram.com/shopgoodco) | Shop Good | beauty | live storefront; SKU breadth; restock/drop cadence; priced publicly; runs paid ads; video in use |
| 20 | [@7thstreetcandle.co](https://instagram.com/7thstreetcandle.co) | 7th Street Candle Co | home | live storefront; SKU breadth; restock/drop cadence; priced publicly; wholesale/retail line; runs |

Full list incl. website + email: `gtm_tools/leads_ecom_2026-09-08.json`

## Tourism — visitor photo → ~30s personalised souvenir video

Attractions, museums and tours that sell admission **and** already commission media or sell photos.

⚠️ **This offer is unvalidated.** The one closed deal in this vertical (client-007, ¥27,800) was 文创 merchandise, not video, and `gtm-progress.md` rates that shape low-repeat / high-manufacturing-risk / 做完当案例，不复制. Do not imply we have run souvenir video for another attraction.

_34 qualified handles available; top 20 by evidence strength._

| # | Handle | Business | Type | Why they qualify (④) |
|--:|---|---|---|---|
| 1 | [@spaceneedle](https://instagram.com/spaceneedle) | Space Needle | attraction | sells tickets; tour schedule; group/school trade; priced publicly; gift shop; commissions media; |
| 2 | [@explorer5280](https://instagram.com/explorer5280) | Explorer Denver Tours | nature | sells tickets; tour schedule; group/school trade; priced publicly; gift shop; commissions media |
| 3 | [@pittockmansion](https://instagram.com/pittockmansion) | Pittock Mansion | nature | sells tickets; tour schedule; priced publicly; gift shop; commissions media |
| 4 | [@vizcaya_museum](https://instagram.com/vizcaya_museum) | Vizcaya Museum & Gardens | heritage | sells tickets; tour schedule; priced publicly; commissions media; seasonal campaigns |
| 5 | [@fieldmuseum](https://instagram.com/fieldmuseum) | Field Museum | heritage | sells tickets; tour schedule; priced publicly; commissions media; seasonal campaigns |
| 6 | [@shorelinesightseeing](https://instagram.com/shorelinesightseeing) | Shoreline Sightseeing | tour | sells tickets; tour schedule; priced publicly; commissions media; seasonal campaigns |
| 7 | [@citycruises](https://instagram.com/citycruises) | Boston Harbor City Cruises | tour | sells tickets; group/school trade; priced publicly; gift shop; seasonal campaigns |
| 8 | [@bullockmuseum](https://instagram.com/bullockmuseum) | Bullock Texas State History Museum | heritage | sells tickets; priced publicly; gift shop; commissions media |
| 9 | [@balboapark](https://instagram.com/balboapark) | Balboa Park | nature | sells tickets; priced publicly; gift shop; seasonal campaigns |
| 10 | [@omsi](https://instagram.com/omsi) | OMSI | heritage | sells tickets; priced publicly; commissions media; seasonal campaigns |
| 11 | [@portlandjapanesegarden](https://instagram.com/portlandjapanesegarden) | Portland Japanese Garden | nature | sells tickets; priced publicly; gift shop; commissions media |
| 12 | [@artinstitutechi](https://instagram.com/artinstitutechi) | The Art Institute of Chicago | heritage | sells tickets; tour schedule; priced publicly; commissions media |
| 13 | [@skydeckchicago](https://instagram.com/skydeckchicago) | Skydeck Chicago | attraction | sells tickets; tour schedule; commissions media; seasonal campaigns |
| 14 | [@dfwairport](https://instagram.com/dfwairport) | DFW Founders' Plaza | nature | sells tickets; tour schedule; priced publicly; commissions media |
| 15 | [@aspiretoursco](https://instagram.com/aspiretoursco) | Aspire Tours | nature | sells tickets; tour schedule; priced publicly; commissions media |
| 16 | [@navypierchicago](https://instagram.com/navypierchicago) | Navy Pier | nature | sells tickets; gift shop; seasonal campaigns |
| 17 | [@texassciencemuseum](https://instagram.com/texassciencemuseum) | Texas Science & Natural History Mu | heritage | sells tickets; gift shop; seasonal campaigns |
| 18 | [@fristartmuseum](https://instagram.com/fristartmuseum) | Frist Art Museum | heritage | sells tickets; gift shop; commissions media |
| 19 | [@mfaboston](https://instagram.com/mfaboston) | Museum of Fine Arts, Boston | heritage | sells tickets; priced publicly; seasonal campaigns |
| 20 | [@museumofscience](https://instagram.com/museumofscience) | Museum of Science | heritage | sells tickets; priced publicly; commissions media |

Full list incl. website + email: `gtm_tools/leads_tourism_2026-09-08.json`

## Creator / Photographer — raw content → edited + localized short-form

Video producers and content studios that already edit to a professional standard.

⚠️ **They are editors.** Do not offer editing skill or "AI editing" — they have both. The edge is **localization**: the same cut shipped in every language. Video Localization is one of only two solution narratives marked *Proven*, and the tooling is the deepest we have.

_53 qualified handles available; top 20 by evidence strength._

| # | Handle | Business | Type | Why they qualify (④) |
|--:|---|---|---|---|
| 1 | [@indirap](https://instagram.com/indirap) | INDIRAP | video_production | client roster; package menu; priced publicly; recurring content line; booking flow; post-product |
| 2 | [@clearlineproduction](https://instagram.com/clearlineproduction) | Clearline Production | creator | client roster; package menu; priced publicly; recurring content line; booking flow; post-product |
| 3 | [@bottlerocket312](https://instagram.com/bottlerocket312) | Bottle Rocket Media | video_production | client roster; package menu; priced publicly; recurring content line; post-production named; cap |
| 4 | [@bluebarncreative](https://instagram.com/bluebarncreative) | Blue Barn Creative | video_production | client roster; package menu; priced publicly; recurring content line; post-production named; cap |
| 5 | [@mosaic_media_films](https://instagram.com/mosaic_media_films) | Mosaic Media Films | video_production | client roster; priced publicly; recurring content line; post-production named; captions/subtitle |
| 6 | [@bennettcreative](https://instagram.com/bennettcreative) | Bennett Creative Video Production | video_production | client roster; package menu; recurring content line; post-production named; captions/subtitles;  |
| 7 | [@awingvisuals](https://instagram.com/awingvisuals) | A-Wing Visuals | Denver Video Prod | creator | client roster; priced publicly; recurring content line; booking flow; post-production named; loc |
| 8 | [@homefieldproductions](https://instagram.com/homefieldproductions) | Homefield Productions | video_production | package menu; recurring content line; booking flow; post-production named; captions/subtitles; l |
| 9 | [@autumnleavesvideo](https://instagram.com/autumnleavesvideo) | Autumn Leaves Video Productions | event | client roster; package menu; recurring content line; booking flow; captions/subtitles; localizat |
| 10 | [@redefineu](https://instagram.com/redefineu) | RedefineU Media | agency | client roster; package menu; recurring content line; post-production named; captions/subtitles;  |
| 11 | [@ryangreenfilms](https://instagram.com/ryangreenfilms) | Ryan Green Films | event | package menu; priced publicly; recurring content line; post-production named; captions/subtitles |
| 12 | [@leftmindmedia](https://instagram.com/leftmindmedia) | Left Mind Media | video_production | client roster; package menu; recurring content line; booking flow; post-production named; locali |
| 13 | [@haleproductionstudios](https://instagram.com/haleproductionstudios) | Hale Production Studios | video_production | client roster; package menu; priced publicly; post-production named; captions/subtitles; localiz |
| 14 | [@castleview.agency](https://instagram.com/castleview.agency) | Castleview Video Agency | agency | client roster; package menu; recurring content line; post-production named; captions/subtitles;  |
| 15 | [@playfishmedia](https://instagram.com/playfishmedia) | Playfish Media | video_production | client roster; recurring content line; booking flow; post-production named; captions/subtitles;  |
| 16 | [@charlesrivermedia](https://instagram.com/charlesrivermedia) | Charles River Media | video_production | client roster; recurring content line; post-production named; captions/subtitles; localization/t |
| 17 | [@focusmedia.vp](https://instagram.com/focusmedia.vp) | Focus Media | video_production | client roster; priced publicly; booking flow; post-production named; localization/translation; s |
| 18 | [@think_branded_media](https://instagram.com/think_branded_media) | Think Branded Media | video_production | client roster; package menu; post-production named; captions/subtitles; localization/translation |
| 19 | [@bonomotion_video](https://instagram.com/bonomotion_video) | Bonomotion Video Agency | video_production | client roster; priced publicly; post-production named; captions/subtitles; localization/translat |
| 20 | [@blissful_films_](https://instagram.com/blissful_films_) | Blissful Films - Texas Wedding Vid | event | package menu; recurring content line; post-production named; captions/subtitles; localization/tr |

Full list incl. website + email: `gtm_tools/leads_creator_2026-09-08.json`

## What to do next

1. **Verify follower counts and recent activity** on the top 20 — a 400-follower account with nothing posted since March is not worth a comment.
2. **Comment on a recent post with output**, not a pitch. For ecommerce that means 2-3 generated frames of *their* product; for creator, a subtitled cut of *their* footage.
3. **Stop at 20 comments and evaluate**, matching the Facebook pilot's discipline. 20 contacts means 20 comments left, not 20 profiles opened.
4. **Log the denominator** — profiles read / comments left / replies / moved to DM.

## What would falsify this channel

If 20 comments on condition-④-qualified accounts return ~0 replies, the failure is not the list — it is that Instagram comments from a 90-follower brand account carry no weight. That is the account-weight caveat already recorded in `gtm-progress.md` against the IG/TikTok row, and it would be confirmed rather than discovered.
