# Instagram lead sheet — AI fashion image / video buyers

_2026-09-26. Successor to `../2026-09-08-instagram-three-offers/`, which was mostly jewelry/candle/beauty. This one is apparel only, cut to the ICP in memory: **high-SKU fashion sellers who need per-garment model imagery at listing volume.**_

**Totals:** 40 brand leads (24 already paying for AI imagery/try-on) · 4 small brands surfaced via KOL content · 28 KOLs (partners / comment sections to mine).

Every brand handle was read off **the brand's own website**, not guessed or taken from IG search. None of the 40 domains appears in `gtm_tools/sent_log.txt`, `sent_messages.jsonl` or the `batch_fashion_ai` files, so none of them has been emailed. Nobody has been contacted.

## The mechanic (same rule as the 09-08 sheet)

**Comment first, DM only after a reply.** A cold DM to a non-follower lands in Message Requests. For these buyers: **reply with output, not a deck.** Generate 2–3 on-model frames of one of *their* listed SKUs and post those.

Log every touch in `gtm_tools/outreach_denominator.csv`, and track leads in `gtm_tools/relationship_leads.json` with `channel: "instagram"`. Don't start a new tracker.

Proof asset, if one is needed: only the cleared batch-campaign demo (see `FASHION_PROOF_VIDEO`). It proves the format, **not** measured garment fidelity; never imply it was made for a client.

---

## Messages + CTA

**CTA pick, by region. Neither channel wins everywhere:**
- **WhatsApp `{WHATSAPP}`** for MENA, LatAm, India, SEA and Eastern Europe (in Tier A: Stop Jeans, Geroo Jaipur, Noētic, COÉGA, Fashion.sa, Reehan, Hanayen, G2000, Maxifashion). WhatsApp is how business gets done there, and it's the faster close.
- **`team@curify-ai.com`** for US, UK, EU, AU, NZ and CA (most of Tier A plus all of Tier B). Brands there rarely take WhatsApp from a stranger, and a **+86 number from an unknown account reads as a scam flag.** Email also brings in the person who signs off on spend.
- **Never put either in a public comment.** The comment is only the hook; the CTA goes in the DM, *after* they reply. Keeping them in the DM thread is always the first ask. Email or WhatsApp is the handoff for files and a quote.

**Intro line, which opens every DM:** *"I'm {name} from Curify. We make on-model photos and short product videos for fashion brands, done for you, per garment."* It stays out of comments, where a pitch reads as spam.

`[frames]` = 2–3 on-model shots generated from one of their own listed SKUs, attached in the DM. Only offer a free sample of their own product. Never send client work.

### Tier A: already using an AI tool

> **Comment:** This drop is 🔥. We ran the {product} through our on-model pipeline and it came out great. Can I DM you the shots?

> **DM (after reply):** {Intro line} Here's your {product}: [frames]. You're already on {Genlook / Botika}, so no prompting on your side: 5 shots per garment on the same model plus a 6–9s video, ready to list. Want a quote for your next drop? {CTA}

### Tier B: high volume, no AI yet

> **Comment:** Love how fast you drop new styles. Mind if I DM you something we made with one of your pieces?

> **DM (after reply):** {Intro line} Here's your {product} on-model, no studio day: [frames]. 5 shots per garment on the same model plus a short video, for less than a shoot costs. Want to try a batch of 10 styles? {CTA}

### Tier C: small brands already experimenting with AI

> **DM** (a comment is fine too): {Intro line} Loved your AI {campaign}. Here's one of your pieces done: [frames]. Want the rest of the line? {CTA}

### KOLs: partnership, not a sale

> **DM:** {Intro line} Your audience keeps asking how to get model photos for their clothing brand, and that's exactly what we do. Open to an affiliate cut or a collab post? Happy to run one of your followers' products free as the demo. **team@curify-ai.com**

---

## Tier A: already paying for AI fashion imagery or try-on (start here)

Found through vendor case studies (Botika), Shopify App Store reviews of AI try-on / model-photo apps (Genlook, TryPoint, SellerPic), and the vendor widget appearing in their homepage code. They have proven budget, but most bought a **self-serve tool**. **The angle is a done-for-you per-garment set at listing volume** (5 images on one model + a 6–9s PDP video), which those tools don't deliver.

SKUs come from `/products.json`, capped at 500. "new" = published in the last 90 days, a rough figure because Shopify republishes reset the date. *uncorroborated* = the review's store name was matched to the domain, but the widget wasn't seen on the site.

| # | Handle | Brand | Category | Country | Signal | SKUs |
|--:|---|---|---|---|---|---|
| 1 | [@getdressedcollective](https://instagram.com/getdressedcollective) | Get Dressed Collective | multi-brand boutique | US | Botika customer ([case studies](https://botika.com/resources/case-studies)) | 480 · 102 new |
| 2 | [@nilandmon](https://instagram.com/nilandmon) | NIL+MON | premium casual | DE | Botika customer, MD quoted | 112 |
| 3 | [@juanandme_](https://instagram.com/juanandme_) | JUAN & ME | resort wear | AU | Botika case study ("6 weeks → 24h") | 62 |
| 4 | [@jordache](https://instagram.com/jordache) | Jordache | denim | US | Botika case study | 62 online |
| 5 | [@aabcollection](https://instagram.com/aabcollection) | Aab | modest wear | UK | Genlook try-on on site | 500+ · 168 new |
| 6 | [@saltrock](https://instagram.com/saltrock) | Saltrock | surf apparel | UK | Genlook review 06-02 + widget | 500+ · 362 new |
| 7 | [@maxifashion.bg](https://instagram.com/maxifashion.bg) | Maxifashion | plus-size women | BG | Genlook review + Genlook **and** FASHN code | 500+ · 164 new |
| 8 | [@ange.paris](https://instagram.com/ange.paris) | Ange Paris | womenswear | FR | Genlook review 03-19 *(uncorroborated)*; **1.8 img/SKU**, a visible gap | 500+ |
| 9 | [@stopjeans_](https://instagram.com/stopjeans_) | Stop Jeans | denim | CO | Genlook review 03-27 *(uncorroborated)*; LatAm like Shasa | 500+ |
| 10 | [@bayeas.official](https://instagram.com/bayeas.official) | Bayeas | denim, wholesale+DTC | US | 2 TryPoint reviews (Jul) + code on site | ~1,400 est. |
| 11 | [@geroojaipur](https://instagram.com/geroojaipur) | Geroo Jaipur | ethnic wear | IN | TryPoint review 08-20 + code | 500+ · 130 new |
| 12 | [@noetic.sa](https://instagram.com/noetic.sa) | Noētic | modest / dresses | SA | Genlook review + widget | 282 |
| 13 | [@coegasunwear](https://instagram.com/coegasunwear) | COÉGA Sunwear | modest swim | AE | TryPoint review + code | 433 |
| 14 | [@bluegeniesdenim](https://instagram.com/bluegeniesdenim) | Blue Genies World | denim | US | Genlook review 07-23 *(uncorroborated)* | 450 |
| 15 | [@bl_nk_london](https://instagram.com/bl_nk_london) | bl-nk | womenswear | UK | Genlook review + widget | 283 · 51 new |
| 16 | [@lemunir_](https://instagram.com/lemunir_) | LE MUNIR | womenswear | ES | Genlook review + widget; 2.4 img/SKU | 188 · 106 new |
| 17 | [@fashion.sa_](https://instagram.com/fashion.sa_) | Fashion.sa | multi-brand fast fashion | SA | Genlook review 09-08 + widget | 500+ |
| 18 | [@g2000sg](https://instagram.com/g2000sg) | G2000 | workwear chain | SG | Genlook review + widget | 500+ · 226 new |
| 19 | [@modernambition](https://instagram.com/modernambition) | Modern Ambition | menswear | CA | Genlook review 09-21 + widget | 136 · 101 new |
| 20 | [@sohotswimwear](https://instagram.com/sohotswimwear) | SoHot Swimwear | multi-brand swim | US | TryPoint review + code | 500+ |
| 21 | [@reehan.eg](https://instagram.com/reehan.eg) | Reehan | women / modest | EG | Genlook review; try-on code | ? |
| 22 | [@signaturedress](https://instagram.com/signaturedress) | Signature Dress | occasion wear | UK | SellerPic review *(uncorroborated)* | 243 |
| 23 | [@sapienclothes](https://instagram.com/sapienclothes) | Sapien Clothes | minimalist apparel | PL | SellerPic review *(uncorroborated)* | ? |
| 24 | [@hanayengroup](https://instagram.com/hanayengroup) | Hanayen | abayas | AE | volume only (467 abayas) | 500+ |

## Tier B: volume fit, no AI signal yet

High SKU count and fast drops, so they fit the per-garment pain, but nothing shows they buy AI imagery. Pitch cost per garment against a studio day.

| # | Handle | Brand | Category | Country | Note |
|--:|---|---|---|---|---|
| 25 | [@veiledcollection](https://instagram.com/veiledcollection) | Veiled | modest wear | US | 500+ SKUs |
| 26 | [@mariamscol](https://instagram.com/mariamscol) | Mariam's Collection | modest wear | US | 266 new/90d, 13.7 img/SKU |
| 27 | [@selfie_leslie](https://instagram.com/selfie_leslie) | Selfie Leslie | boutique | US | 377 dresses |
| 28 | [@hazelandolive_](https://instagram.com/hazelandolive_) | Hazel & Olive | boutique | US | **3.0 img/SKU** |
| 29 | [@magnoliaboutiqueindianapolis](https://instagram.com/magnoliaboutiqueindianapolis) | Magnolia Boutique | boutique | US | 367 new/90d |
| 30 | [@shoppriceless](https://instagram.com/shoppriceless) | Priceless | boutique | US | 500+ |
| 31 | [@shop12thtribe](https://instagram.com/shop12thtribe) | 12th Tribe | womenswear | US | 217 new/90d |
| 32 | [@shopbohme](https://instagram.com/shopbohme) | Bohme | boutique | US | 500+ |
| 33 | [@kulanikinis](https://instagram.com/kulanikinis) | Kulani Kinis | swimwear | AU | 205 new/90d |
| 34 | [@jolynclothing](https://instagram.com/jolynclothing) | JOLYN | athletic swim | US | 437 new/90d · in Apollo pool |
| 35 | [@dippindaisys](https://instagram.com/dippindaisys) | Dippin' Daisy's | swimwear | US | 249 SKUs |
| 36 | [@montce_swim](https://instagram.com/montce_swim) | Montce | swimwear | US | 179 new/90d |
| 37 | [@setactive](https://instagram.com/setactive) | Set Active | activewear | US | 3.9 img/SKU · in Apollo pool |
| 38 | [@buffbunny_collection](https://instagram.com/buffbunny_collection) | Buffbunny | activewear | US | ⚠ handle from page code only, eyeball it · in Apollo pool |
| 39 | [@jamiekay](https://instagram.com/jamiekay) | Jamie Kay | kidswear | NZ | 411 new/90d |
| 40 | [@little_bipsy](https://instagram.com/little_bipsy) | Little Bipsy | kidswear | US | 131 SKUs |

Rows 34, 37 and 38 also sit in the Apollo apparel pools, unsent. Work each one on one channel only, and note which.

## Tier C: small brands surfaced through KOL content

| Handle | Brand | Evidence |
|---|---|---|
| [@henrydacostabrand](https://instagram.com/henrydacostabrand) | Henry Dacosta (bridal, ~130 followers) | Commissioned an AI bridal campaign from @mariispace, 2026-08 ([post](https://www.instagram.com/p/DcJWM67DXuF/)) |
| [@acte.brand](https://instagram.com/acte.brand) | ACTE (~121K) | Featured in AI campaign work by @ksyush.ai; unclear whether paid or fan content |
| [@kaybahdapparel](https://instagram.com/kaybahdapparel) | Kay Bahd (~31K) | Rob Prsa's own clothing brand; he makes content about AI video for apparel |
| [@hera](https://instagram.com/hera) | HERA (~243K) | Ash White's former brand, now owned by a Gymshark director's family |

Big names seen in the same research (J.Crew, Gucci, Guess, Jason Wu, Norma Kamali, Pangaia) prove the market exists but are not realistic Curify buyers, so they're left off.

---

## KOLs: partners, and comment sections worth mining

The KOLs are **not** the buyers. Their audiences are. Use them two ways: (1) a sponsored mention or partnership, (2) read the comment sections of their "for clothing brand owners" posts by hand. Follower counts were read off the IG profile on 2026-09-25.

| Handle | Followers | Audience | Use |
|---|---|---|---|
| [@bryanlowwww](https://instagram.com/bryanlowwww) | 869K | clothing-brand owners (tool roundups) | a tool-roundup mention |
| [@varyalai](https://instagram.com/varyalai) | 271K | AI shoots of real garments on AI models; bridal/couture | followers = service buyers; white-label partner? |
| [@harvishahcoach](https://instagram.com/harvishahcoach) | 230K | Indian "fashionpreneurs"; paid club of 10K+ | sponsored masterclass |
| [@airohit.tech](https://instagram.com/airohit.tech) | 176K | Hindi "AI model for clothing brand" | Indian D2C sellers |
| [@gordonly](https://instagram.com/gordonly) | 124K | "If you own a clothing brand…" + comment-for-link | **top comment section to mine** |
| [@madebyizan](https://instagram.com/madebyizan) | 116K | AI workflows for streetwear brands | affiliate |
| [@saintlouvent_](https://instagram.com/saintlouvent_) | 90K | AI campaigns for luxury houses (later commissioned by Gucci) | brand marketers follow her |
| [@fashion.coupids](https://instagram.com/fashion.coupids) | 58K | AI editorial courses | education partner |
| [@rayinthedarkk](https://instagram.com/rayinthedarkk) | 54K | scaling Shopify clothing brands; comment "AI" | **comment section to mine** |
| [@malikk.w](https://instagram.com/malikk.w) | 52K | "AI ads for my clothing brand" | brand owner who also runs an agency |
| [@martwayne](https://instagram.com/martwayne) | 47K | fashion business coach | designers becoming brands |
| [@shackvault](https://instagram.com/shackvault) | 34K | streetwear brand-owner education | commenters = owners |
| [@masonschaedel](https://instagram.com/masonschaedel) | 27K | "DM 'Grow' to scale your clothing brand" | coach audience |
| [@ashwhite_](https://instagram.com/ashwhite_) | 25K | clothing-brand coaching + Skool | community |
| [@kolaflare](https://instagram.com/kolaflare) | 24K | AI clothing campaigns; sells done-for-you work to brands | **fulfilment partner** |
| [@fashionaischool](https://instagram.com/fashionaischool) | 24K | AI workshops for fashion creatives | sponsor slot |
| [@samfinn.studio](https://instagram.com/samfinn.studio) | 20K | AI photographer (J.Crew, Ugg, Skims) | mine his tags |
| [@ksyush.ai](https://instagram.com/ksyush.ai) | 19K | real shoots + AI for brands | tags brands |
| [@robprsabiz](https://instagram.com/robprsabiz) | 15K IG / 100K YT | Apparel Success podcast, 500+ brand owners | **Skool community full of owners** |
| [@bitbranding](https://instagram.com/bitbranding) | 14K | Shopify marketing for clothing stores, 250+ brands | agency partnership |
| [@walllow.creative](https://instagram.com/walllow.creative) | 14K | "ChatGPT puts models in your brand's clothes" | boutique-owner comments |
| [@__e_johnson](https://instagram.com/__e_johnson) | 7.3K | brand owner; "AI model for our clothing brand" | peer case |
| [@janeyparkxyz](https://instagram.com/janeyparkxyz) | 6.6K | *The Digital Runway* newsletter (AI × fashion) | newsletter feature |
| [@designedbywil](https://instagram.com/designedbywil) | 4K IG / 70.5K YT | streetwear AI studio-shoot tutorials | YT audience |

Also confirmed but weaker: @str4ngething (202K, concept art), @s.fashion.ai, @lesya.neuro, @matthieugb, and the small coaches @thefashioncultivator / @thefashionbusinesscoach / @thefashionexpertuk.

---

## Commenter mining: what was found, and why it's not a list yet

- **Generic AI-fashion posts attract the wrong commenters.** Checked by hand on 3 posts from #aifashionphotography / "ai photoshoot for clothing brand" (@prompts.ig, @pri_design_official, @elicoleman_). Almost every comment is a comment-for-link keyword ("Prompt", "Studio") or an emoji from an engagement pod. These are DIY prompters, not buyers. The one plausible commenter was `carolfenixwomanbrazil` (possibly a Brazilian womenswear label), **unverified**.
- **Where to mine instead:** the comment sections of brand-owner-facing KOLs (@gordonly, @rayinthedarkk), plus Rob Prsa's and Ash White's Skool groups. Qualify a commenter as a buyer only if their profile is a shop with a storefront link.
- **Bulk scraping was stopped on purpose.** An in-browser pull of commenters through Instagram's internal API was blocked as automated scraping from a logged-in account, and I didn't work around it. Mining at volume means reading by hand, or you deciding to allow it.
- **The Reddit / Shopify-Community commenter search didn't finish** (Reddit blocked the search tool, and the agent stalled). Not attempted again.

## Excluded on purpose

Rainbow Shops (a model is suing it over an AI likeness) and Athletifreak (NY AI-model disclosure complaint): legal exposure. Moon Bourne, Mahogany Coast and Valara Fit: under 15 SKUs. Petal & Pup, Meshki, Tiger Mist, Peppermayo, Motel Rocks, Oner Active, BloomChic, Akira, VICI, Andie and Triangl: above the ICP (in-house studios); several are already in the Apollo pools.

**Competitors seen** (not leads): Botika, FASHN, Genlook, TryPoint, SellerPic, PicCopilot, WearView, Claid, Photoroom, Modelia, Lalaland, Higgsfield, The New Black, Rawshot, Picjam, Modelize, ZenCreator; agencies Seraphinne Vallora, Maison Meta, Pixel Moda, AICONIC.
