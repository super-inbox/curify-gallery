# Instagram lead sheet — AI fashion image / video buyers

_2026-09-26. Successor to `../2026-09-08-instagram-three-offers/`, which was mostly jewelry/candle/beauty. This one is apparel only, cut to the ICP in memory: **high-SKU fashion sellers who need per-garment model imagery at listing volume.**_

**Totals (updated 2026-10-10):** 60 brand candidates: Tier A 24 · Tier B 27 · Tier C 4 · Uncategorized / alternate offer 5. The original 44 brands are retained; Jay’s 2026-10-09 batch adds 16 unique handles (17 links, Miuus submitted twice). KOL research remains below. **All 16 new leads are uncontacted in the recovered records; this update is research only.**

For the original September batch, every brand handle was read off **the brand's own website**, not guessed or taken from IG search. When the September sheet was built, none of the 40 domains appeared in `gtm_tools/sent_log.txt`, `sent_messages.jsonl` or the `batch_fashion_ai` files, so none had been emailed at that point. Nobody had been contacted at that point — see the Tier A section for what has gone out since.

## The mechanic (same rule as the 09-08 sheet)

**Comment first, DM only after a reply.** A cold DM to a non-follower lands in Message Requests. For these buyers: **reply with output, not a deck.** Generate 2–3 on-model frames of one of *their* listed SKUs and post those.

Log every touch in `gtm_tools/outreach_denominator.csv`, and track leads in `gtm_tools/relationship_leads.json` with `channel: "instagram"`. Don't start a new tracker.

Proof asset, if one is needed: only the cleared batch-campaign demo (see `FASHION_PROOF_VIDEO`). It proves the format, **not** measured garment fidelity; never imply it was made for a client.

---

## Messages + CTA

**CTA pick, by region. Neither channel wins everywhere:**
- **WhatsApp `{WHATSAPP}`** for MENA, LatAm, India, SEA and Eastern Europe (in Tier A: Stop Jeans, Geroo Jaipur, Noētic, COÉGA, Fashion.sa, Reehan, Hanayen, G2000, Maxifashion). WhatsApp is how business gets done there, and it's the faster close.
- **`team@curify-ai.com`** for US, UK, EU, AU, NZ and CA (most of Tier A plus the original US/UK/EU/AU/NZ/CA Tier B leads). Brands there rarely take WhatsApp from a stranger, and a **+86 number from an unknown account reads as a scam flag.** Email also brings in the person who signs off on spend.
- **Never put either in a public comment.** The comment is only the hook; the CTA goes in the DM, *after* they reply. Keeping them in the DM thread is always the first ask. Email or WhatsApp is the handoff for files and a quote.

**Intro line, which opens every DM:** *"I'm {name} from Curify. We make on-model photos and short product videos for fashion brands, done for you, per garment."* It stays out of comments, where a pitch reads as spam.

`[frames]` = 2–3 on-model shots generated from one of their own listed SKUs, attached in the DM. Only offer a free sample of their own product. Never send client work.

### Tier A: already using an AI tool

> **Comment:** This drop is 🔥. We ran the {product} through our on-model pipeline and it came out great. Can I DM you the shots?

> **DM (after reply):** {Intro line} Here's your {product}: [frames]. You're already on {Genlook / Botika}, so no prompting on your side: 5 shots per garment on the same model plus a 6–9s video, ready to list. Want a quote for your next drop? {CTA}

### Tier B: volume fit, no confirmed AI signal

> **Comment:** Love how fast you drop new styles. Mind if I DM you something we made with one of your pieces?

> **DM (after reply):** {Intro line} Here's your {product} on-model, no studio day: [frames]. 5 shots per garment on the same model plus a short video, for less than a shoot costs. Want to try a batch of 10 styles? {CTA}

### Tier C: small brands already experimenting with AI

> **DM** (a comment is fine too): {Intro line} Loved your AI {campaign}. Here's one of your pieces done: [frames]. Want the rest of the line? {CTA}

### KOLs: partnership, not a sale

> **DM:** {Intro line} Your audience keeps asking how to get model photos for their clothing brand, and that's exactly what we do. Open to an affiliate cut or a collab post? Happy to run one of your followers' products free as the demo. **team@curify-ai.com**

---

## Tier A: already paying for AI fashion imagery or try-on (start here)

Found through vendor case studies (Botika), Shopify App Store reviews of AI try-on / model-photo apps (Genlook, TryPoint, SellerPic), and the vendor widget appearing in their homepage code. They have proven budget, but most bought a **self-serve tool**. **The angle is a done-for-you per-garment set at listing volume** (5 images on one model + a 6–9s PDP video), which those tools don't deliver.

**Email, 2026-09-26:** 20 of 24 sent through the `ecom_video` voice, with the fashion batch-campaign demo attached (`gtm_tools/batch_fashion_ai_igtierA_2026-09-26.json`). 12 went to named contacts from Apollo, all verified (12 credits); 8 went to inboxes published on the brand's own site. #3 and #17 reached only customer-care inboxes, the weakest route, so the IG DM matters more for those two. #20–#23 have no findable email and are IG only.

**Comments, 2026-09-26 / 09-27:** the comment-first mechanic run on **12 of the 24**, Tier A template as written with one of the brand's own listed products named: **#1–#6 on 09-26, #7–#12 on 09-27.** (The 09-26 six were first recorded here as DMs; that was wrong — they were public comments. Corrected 09-27.) Each of the twelve had already been emailed on 09-26, so the comment is a second touch on a different channel, not a first one.

⚠ **No frames exist for any of the twelve.** The comment asks *"can I DM you the shots?"*, so a reply cannot be answered until 2–3 on-model frames of that brand's own SKU are generated. Two things are needed before the first reply lands:

- **Which product was named in each comment is not recorded.** The frames have to be of *that* garment, so the twelve product names need writing down while they can still be read off the comment.
- **Build the frames ahead of a reply for the strongest of the twelve**, rather than starting generation after someone answers.

#13–#24 have not been commented on.

SKUs come from `/products.json`, capped at 500. "new" = published in the last 90 days, a rough figure because Shopify republishes reset the date. *uncorroborated* = the review's store name was matched to the domain, but the widget wasn't seen on the site.

| # | Handle | Brand | Category | Country | Signal | SKUs | Status |
|--:|---|---|---|---|---|---|---|
| 1 | [@getdressedcollective](https://instagram.com/getdressedcollective) | Get Dressed Collective | multi-brand boutique | US | Botika customer ([case studies](https://botika.com/resources/case-studies)) | 480 · 102 new | IG comment 09-26; email 09-26 → victoria@ (Social Media Dir) |
| 2 | [@nilandmon](https://instagram.com/nilandmon) | NIL+MON | premium casual | DE | Botika customer, MD quoted | 112 | IG comment 09-26; email 09-26 → mw@linfashion.com (MD/Owner) |
| 3 | [@juanandme_](https://instagram.com/juanandme_) | JUAN & ME | resort wear | AU | Botika case study ("6 weeks → 24h") | 62 | IG comment 09-26; email 09-26 → customercare@ ⚠ CS inbox |
| 4 | [@jordache](https://instagram.com/jordache) | Jordache | denim | US | Botika case study | 62 online | IG comment 09-26; email 09-26 → devyn@ (VP Marketing) |
| 5 | [@aabcollection](https://instagram.com/aabcollection) | Aab | modest wear | UK | Genlook try-on on site | 500+ · 168 new | IG comment 09-26; email 09-26 → nazmin@ (Founder/CD) |
| 6 | [@saltrock](https://instagram.com/saltrock) | Saltrock | surf apparel | UK | Genlook review 06-02 + widget | 500+ · 362 new | IG comment 09-26; email 09-26 → sarah.loder@ (Mktg Mgr) |
| 7 | [@maxifashion.bg](https://instagram.com/maxifashion.bg) | Maxifashion | plus-size women | BG | Genlook review + Genlook **and** FASHN code | 500+ · 164 new | IG comment 09-27; email 09-26 → shop@ |
| 8 | [@ange.paris](https://instagram.com/ange.paris) | Ange Paris | womenswear | FR | Genlook review 03-19 *(uncorroborated)*; **1.8 img/SKU**, a visible gap | 500+ | IG comment 09-27; email 09-26 → sheila@angefashion.com (E-com Mgr) |
| 9 | [@stopjeans_](https://instagram.com/stopjeans_) | Stop Jeans | denim | CO | Genlook review 03-27 *(uncorroborated)*; LatAm like Shasa | 500+ | IG comment 09-27; email 09-26 → icorrea@stop.com.co (eCom lead) |
| 10 | [@bayeas.official](https://instagram.com/bayeas.official) | Bayeas | denim, wholesale+DTC | US | 2 TryPoint reviews (Jul) + code on site | ~1,400 est. | IG comment 09-27; email 09-26 → info@ |
| 11 | [@geroojaipur](https://instagram.com/geroojaipur) | Geroo Jaipur | ethnic wear | IN | TryPoint review 08-20 + code | 500+ · 130 new | IG comment 09-27; email 09-26 → info@ |
| 12 | [@noetic.sa](https://instagram.com/noetic.sa) | Noētic | modest / dresses | SA | Genlook review + widget | 282 | IG comment 09-27; email 09-26 → rnagro@noeticsa.com (GM) |
| 13 | [@coegasunwear](https://instagram.com/coegasunwear) | COÉGA Sunwear | modest swim | AE | TryPoint review + code | 433 | email 09-26 → valeria@ (Mktg Mgr) |
| 14 | [@bluegeniesdenim](https://instagram.com/bluegeniesdenim) | Blue Genies World | denim | US | Genlook review 07-23 *(uncorroborated)* | 450 | email 09-26 → klhbluegenies@gmail.com |
| 15 | [@bl_nk_london](https://instagram.com/bl_nk_london) | bl-nk | womenswear | UK | Genlook review + widget | 283 · 51 new | email 09-26 → eshop@ |
| 16 | [@lemunir_](https://instagram.com/lemunir_) | LE MUNIR | womenswear | ES | Genlook review + widget; 2.4 img/SKU | 188 · 106 new | email 09-26 → info@lemunir.com |
| 17 | [@fashion.sa_](https://instagram.com/fashion.sa_) | Fashion.sa | multi-brand fast fashion | SA | Genlook review 09-08 + widget | 500+ | email 09-26 → care@ ⚠ CS inbox |
| 18 | [@g2000sg](https://instagram.com/g2000sg) | G2000 | workwear chain | SG | Genlook review + widget | 500+ · 226 new | email 09-26 → nelsoncf@g2000.com.hk (Group CEO) |
| 19 | [@modernambition](https://instagram.com/modernambition) | Modern Ambition | menswear | CA | Genlook review 09-21 + widget | 136 · 101 new | email 09-26 → leah.crymble@ (Manager) |
| 20 | [@sohotswimwear](https://instagram.com/sohotswimwear) | SoHot Swimwear | multi-brand swim | US | TryPoint review + code | 500+ | no email found (site + Apollo) — IG only |
| 21 | [@reehan.eg](https://instagram.com/reehan.eg) | Reehan | women / modest | EG | Genlook review; try-on code | ? | no email found (site + Apollo) — IG only |
| 22 | [@signaturedress](https://instagram.com/signaturedress) | Signature Dress | occasion wear | UK | SellerPic review *(uncorroborated)* | 243 | no email found (site + Apollo) — IG only |
| 23 | [@sapienclothes](https://instagram.com/sapienclothes) | Sapien Clothes | minimalist apparel | PL | SellerPic review *(uncorroborated)* | ? | no email found (site + Apollo) — IG only |
| 24 | [@hanayengroup](https://instagram.com/hanayengroup) | Hanayen | abayas | AE | volume only (467 abayas) | 500+ | email 09-26 → navin@hanayen.ae (Brand Mgr) |

## Tier B: volume fit, no AI signal yet

Catalogue volume and/or recurring drops suggest a per-garment content workload, but AI purchasing and unmet demand remain unconfirmed. Pitch a concrete product sample and a small batch. Absence of a visible AI widget is not proof that a brand does not use AI.

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

### Malaysia additions — sourced 2026-10-09, verified 2026-10-09–10

**11 added to Tier B; none added to A or C.** These are fit assessments, not replies or demonstrated buying intent. All are Malaysian apparel sellers; “first / second / qualify” below is outreach priority within B, not a replacement tier system. Each handle was supplied by Jay and then matched to its own profile and storefront. Storefront counts are product listings, **not** inventory units, unique garment designs, or verified sell-through; colour-separated listings, accessories and sold-out items may be included.

| # | Handle / brand | Catalogue evidence and source | Priority and proposed angle | Status / remaining qualification |
|--:|---|---|---|---|
| 41 | [@sistersvoguediary2](https://www.instagram.com/sistersvoguediary2/) — Sisters Vogue Diary | Puchong boutique. Bio advertises weekly launches and 1,000+ ready-stock styles; [all-products category](https://www.sistersvoguediary.com/?product_cat=all) displays **1,323 results**. Website links back to the exact handle. | **First.** Recurring batch production for weekly drops. Start with one named outfit, then offer a 10-style pilot with consistent imagery. | Uncontacted. Strongest volume evidence; confirm whether they create imagery or reuse supplier assets, and which person commissions content. Public business email: sistersvogue.my@gmail.com. |
| 42 | [@lovenplainnnnn](https://www.instagram.com/lovenplainnnnn/) — LOVENPLAIN | [Shop all](https://lovenplain.com/collections/all) displays **296 products** on 10-10. Bio links this domain; registration number matches the site. Ready-stock womenswear with repeated new-arrival collections. | **First.** A consistent on-model set plus a short PDP clip for a new dress or set. Test a small batch before proposing recurring production. | Uncontacted. Retail examples around RM69–149 suggest price sensitivity; these are selling prices, not known margins. Public WhatsApp on site: +60 17-7146966. |
| 43 | [@alldaylucy__official](https://www.instagram.com/alldaylucy__official/) — All Day Lucy | Bio and website mutually link. [Catalogue](https://www.alldaylucy.com/collections/all) has 50 listings on page 1; [page 6](https://www.alldaylucy.com/collections/all?limit=50&page=6&sort=featured) also has 50 and links onward through page 11: **300+ listing positions**, not a completed count. Monthly arrivals; online-only shop. | **First.** Repeated PDP and launch assets for successive drops; make a same-garment proof, then quote by batch. | Uncontacted. Colourways are often separate listings. Website FAQ retains an older @alldaylucy__ handle; use the supplied @alldaylucy__official, confirmed by its bio and current site footer. Email shown is customer service, not a confirmed buyer. |
| 44 | [@hersstudio_ecopalladium](https://www.instagram.com/hersstudio_ecopalladium/) — Her’s Studio | **Clothing boutique, not jewelry.** Eco Palladium is its JB store location. Bio links [EasyStore catalogue](https://hersstudio72.easy.co/collections/all); site explicitly names the supplied IG. **~221 listings** inferred from 50/page and 21 on [final page 5](https://hersstudio72.easy.co/collections/all?limit=50&page=5&sort=featured). | **First.** Boutique sets and occasion dresses; show lace, trim and silhouette fidelity on one actual piece. Coordinate imagery across the Eco Palladium and Austin branches. | Uncontacted. The other branch is a related account, not another lead. Some catalogue items are shoes or innerwear. The earlier “palladium = jewelry” guess is withdrawn. |
| 45 | [@ruvve.co](https://www.instagram.com/ruvve.co/) — RuVvé | Bio links its [RuVvé-specific collection](https://hiedruvve.co/collections/ruvv%C3%A9-co) in HIED & RuVvé’s store. **~163 listings** inferred from 50/page and 13 on [final page 4](https://hiedruvve.co/collections/ruvv%C3%A9-co?limit=50&page=4&sort=featured). Sample dresses RM218–258; physical shop in Kuchai Lama, KL. | **First.** A refined editorial/PDP set for the same dress, emphasizing drape and texture. Higher observed retail prices make a paid sample worth testing; budget remains unknown. | Uncontacted. Count only the RuVvé collection, not the whole multi-brand store. HIED is a related business, not a new lead; confirm shared content decision-maker. |
| 46 | [@signature_truck](https://www.instagram.com/signature_truck/) — Signature Truck | Bio links [official site](https://signaturetruck.com.my/), which identifies petite womenswear and a self-made collection. [Shop](https://signaturetruck.com.my/shop/) exposes **16 pages**, but product cards were missing in the fetched shop HTML; no exact count asserted. Homepage has priced garments and multiple collection lines. | **Second.** Petite-proportion consistency and assets for self-made launches. Sample one current top/set without implying that generated images prove fit. | Uncontacted. Volume fit is supported by catalogue pagination but less directly measured. Confirm how many styles need new assets and whether work can be outsourced. |
| 47 | [@arimee__](https://www.instagram.com/arimee__/) — Arimeé / Maison De Mee | Bio links [official store](https://www.arimee.com/) and publishes marketing@arimee.com for collaborations. [Catalogue](https://www.arimee.com/category/shop-all) has 24 product links and “1 of 17”; [View All](https://www.arimee.com/category/shop-all?items_per_page=All&) still paginates, showing 100 links and “1 of 4”. **100+ directly observed listings; total not enumerated.** | **Second.** Overflow production for launches or additional campaign variants. Use the named marketing route after interest; frame as extra capacity around the existing visual process. | Uncontacted. Large following does **not** establish an in-house studio or justify automatic exclusion. Some colours are separate listings; internal team and outsourcing appetite unknown. |
| 48 | [@sunflowerc___](https://www.instagram.com/sunflowerc___/) — SUNFLOWERC | IG profile requires login, but [official catalogue](https://www.sunflowerc.com/collections/all) links to this exact handle. **~198 listings** inferred from 50/page and 48 on [final page 4](https://www.sunflowerc.com/collections/all?limit=50&page=4&sort=featured). Ready-stock tops, dresses, sets and seasonal collections. | **Second.** Economical catalogue batches and short launch clips. Choose a visually distinct garment that can justify a test despite modest unit prices. | Uncontacted. Verified through its storefront; no claim of viewing the restricted feed. Homepage examples RM35–89 indicate a need to qualify spend per style early. |
| 49 | [@95s_style.co](https://www.instagram.com/95s_style.co/) — 95’s STYLE.CO | Bio links [official site](https://www.95styleco.com/); site links to [catalogue](https://shop.95styleco.com/v2/menu/by-category/paginate?merchant_domain_name=95styleco&product_category_id=0), which links back to exact IG. **~94 listings** inferred from 20/page and 14 on [final page 5](https://shop.95styleco.com/v2/menu/by-category/paginate?product_category_id=0&search_keyword=&page=5). | **Second.** A small batch for ready-stock or seasonal dresses/sets. Check whether existing supplier photos need a consistent brand treatment. | Uncontacted. Smaller catalogue than the first group; do not promise recurring volume before asking about launch frequency. Public WhatsApp: +60 11-1109 3317. |
| 50 | [@eonnicollection.co](https://www.instagram.com/eonnicollection.co/) — Eonni Collection | Bio links [official catalogue](https://www.eonnicollection.com/collections/all); **93 distinct listing URLs** across its two pages (50 + 43). Butterworth boutique with MY/SG delivery and custom/Chinese-style collections. | **Second.** Seasonal capsule imagery and coordinated sets. A one-garment trial suits the smaller catalogue better than a large retainer pitch. | Uncontacted. Number of IG posts is not catalogue size. Some colourways may have separate listings; recurring content workload and budget unconfirmed. |
| 51 | [@jmei.studio](https://www.instagram.com/jmei.studio/) — Jmei Studio | Profile identifies Thailand/China purchasing and links [official shop](https://jmeistudio.com/); footer links back. [Catalogue](https://jmeistudio.com/collections/all) shows **50 listings on page 1 and further pages**, with ready-stock, Bangkok preorder and Chinese-style lines. | **Qualify before producing a sample.** Offer consistent listing presentation only if they have usable source images and repeated content spend. | Uncontacted. Observed items around RM15–47 and a purchasing/reseller model suggest tighter economics; margins are unknown. Ask about budget and image permissions first. No longer “profile unavailable”. |

**How to work this batch:** start with Sisters Vogue Diary, LOVENPLAIN, All Day Lucy, Her’s Studio and RuVvé. Priority reflects catalogue evidence, price positioning and likely workload; it does not measure willingness to buy. Use Chinese where the account’s own copy is Chinese, with English available. Keep the conversation in IG first; offer WhatsApp only where published or preferred, and respect an explicit marketing-email route such as Arimeé’s.

**Sample gate:** choose and record the exact product URL/colour before preparing a sample. Check garment construction and details against the source. The existing comment templates say “we made” / “we ran”; use those only after the named sample actually exists. Otherwise ask permission to prepare a sample, e.g. “这款的剪裁很有特点，可以用这款做一组模特展示图小样给你看看吗？” No sample was generated and no message was sent in this research pass.

## Tier C: small brands surfaced through KOL content

| Handle | Brand | Evidence |
|---|---|---|
| [@henrydacostabrand](https://instagram.com/henrydacostabrand) | Henry Dacosta (bridal, ~130 followers) | Commissioned an AI bridal campaign from @mariispace, 2026-08 ([post](https://www.instagram.com/p/DcJWM67DXuF/)) |
| [@acte.brand](https://instagram.com/acte.brand) | ACTE (~121K) | Featured in AI campaign work by @ksyush.ai; unclear whether paid or fan content |
| [@kaybahdapparel](https://instagram.com/kaybahdapparel) | Kay Bahd (~31K) | Rob Prsa's own clothing brand; he makes content about AI video for apparel |
| [@hera](https://instagram.com/hera) | HERA (~243K) | Ash White's former brand, now owned by a Gymshark director's family |

Big names seen in the same research (J.Crew, Gucci, Guess, Jason Wu, Norma Kamali, Pangaia) prove the market exists but are not realistic Curify buyers, so they're left off.

## Uncategorized / alternate offer — 2026-10-09 intake

These five are preserved below the three tiers. **Small size alone does not make a lead Tier C:** C is the existing AI/KOL-evidence group. None of the new 16 has verified paid-AI or AI-campaign evidence from this review.

| Handle / brand | Verified evidence | Decision and next step | Status |
|---|---|---|---|
| [@miuus_batupahat](https://www.instagram.com/miuus_batupahat/) — Miuus Official | Public bio names the Batu Pahat shop, @miuus_ecogalleria JB branch and [miuuswardrobe.boutir.com](https://miuuswardrobe.boutir.com/). The [store contact page](https://miuuswardrobe.boutir.com/p/contact_us?lang=ms) has the matching Batu Pahat address, but an older IG name. Catalogue fetch returned 403. | **Promising apparel lead; volume unverified.** Obtain current catalogue/style count and content workflow before promotion to B. Branch accounts should be worked as one business until ownership is clarified. | Uncontacted; not rejected. |
| [@nanya_my](https://www.instagram.com/nanya_my/) — NANYA | Bio explicitly says designed/made in Malaysia, small-batch independent production and one-to-one customization. Cultural-fusion clothing; links to Xiaohongshu plus another link rather than a verified catalogue in this pass. | **Different buying model.** Lower priority for volume PDP production; potentially a bespoke editorial/capsule sample. Ask launch cadence and budget. Do not infer low inventory from its eight visible posts. | Uncontacted; no AI evidence for C. |
| [@secretlife_os](https://www.instagram.com/secretlife_os/) — Secret Life | Page title identifies lingerie/sleepwear/night dresses; the page displays a restricted-profile login screen. No matched official shop, location, catalogue or decision-maker verified. | **Qualification pending.** Read its bio/shop link when a logged-in profile is available; do not match it to unrelated similarly named lingerie sites. If qualified, use a lingerie/sleepwear-specific product-visual offer. | Uncontacted; access limitation, not a quality judgment. |
| [@umijewelry_](https://www.instagram.com/umijewelry_/) — UmiJewelry Crystal | Bio says Malaysia and links [umijewelry8.easy.co](https://umijewelry8.easy.co/); storefront sells crystal/jade jewelry. The storefront footer links a different account (@upkuramajewelry), so confirm account relationship before contacting that alternate handle. | **Outside apparel offer.** Potential jewelry product photography, detail retouching or lifestyle visuals; avoid per-garment/on-model fashion copy. Preserve natural-stone colour, inclusions and actual product details in any sample. | Uncontacted; retained for alternate offer. |
| [@shuhu.my](https://www.instagram.com/shuhu.my/) — SHU HU | Bio links [shuhu.my](https://shuhu.my/), which links back. Bras, panties, bra tops and pyjamas. [Shop page](https://shuhu.my/shop/) exposes 16 product links, not a verified catalogue total; range and bundles differ from frequent fashion drops. | **Specialist offer; volume unverified.** A pyjama or bra-top PDP/detail set is a better initial hypothesis than generic fashion campaigns. Ask monthly launches and visual workload before assigning B. | Uncontacted. No verified AI vendor signal. |

### Verification notes — 2026-10-09–10

- Public IG bios and visible profile links were read in the built-in browser on 10-09. Secret Life and SUNFLOWERC required login; SUNFLOWERC’s own site independently confirmed its handle. No restricted profile was bypassed.
- Public storefronts and selected catalogue pages were fetched on **10-10**. Live LOVENPLAIN count was 296; older search snapshots showed 240/269 and are superseded. Counts prefixed `~` are inferred from page size and final-page cards, not a full de-duplicated catalogue export. All Day Lucy and Jmei expose moving pagination windows, so their totals remain unasserted. Listing count is not the number of unique garment designs.
- The accessible pages had no substantiated Genlook, TryPoint, Botika, FASHN, SellerPic, PicCopilot, WearView or Modelia integration. A raw “trypoint” substring in SHU HU was actually schema.org `EntryPoint`, a false positive. This is a limited page-source check, not proof of no AI use or a comprehensive technology audit; no paid-AI budget is established for any of the 16.
- The prior Claude session’s speculative classifications are superseded here: Her’s Studio is apparel; NANYA is small-batch/custom by its own description; Jmei’s profile and shop are accessible; Arimeé is not excluded solely for follower count. No follower count, post count or product image appearance is treated as evidence of paid AI usage.
- This document records qualification and next actions. Outreach counters remain unchanged because no outreach occurred; log actual touches in the existing `gtm_tools/outreach_denominator.csv` and use `gtm_tools/relationship_leads.json` when activating leads.

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
