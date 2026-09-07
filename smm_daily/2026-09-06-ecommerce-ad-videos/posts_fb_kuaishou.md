# E-commerce & ad videos — FB Groups + Kuaishou index (2026-09-06)

Indexes `curify-gallery/ecommerce_ad_videos` for social distribution. Machine-readable
companion: `index.json`. Prompt provenance + the Minimax H3 series: `prompts/`.

**Ask was 10 videos.** 4 are cleared, 2 need one question answered, **4 cannot go on a
public feed** — see §1. The copy in §3 is written for the 6 that can plausibly ship;
the 4 internal ones are indexed for completeness with no post copy, because writing
promo copy for them would imply they are postable.

---

## 1. Clearance first (read before scheduling anything)

`asset-authority-distribution-inventory.md` §3 already draws this line: **自有素材，自有输出
→ ✅ 立即可用** vs **第三方版权 → ❌ 不可公开**, the same rule that keeps Labubu and the
Chaplin/Forrest Gump translation demos permanently off the public feed. Applying it here:

| # | Video | On-screen brand | Verdict |
|---|---|---|---|
| 1 | `angryAlert/AngryAlert_vertical.mp4` (+ landscape cut) | Curify | ✅ **ship** |
| 2 | `matcha_drink.mp4` | none | ✅ **ship** |
| 3 | `rotation_chair.mp4` | none | ✅ **ship** |
| 4 | `redbull/kungfu_redbull_SF.mp4` | Curify | ✅ **ship** — ⚠️ rename file first |
| 5 | `model-standing.mp4` | none | ⚠️ **check** — likeness |
| 6 | `oilight/oilight final.mp4` | OILIGHT™ | ⚠️ **check** — client brand + live footage |
| 7 | `corona/Mountain_Sunrise_Beer_Climax.mp4` | **Corona** | ⛔ **internal** |
| 8 | `starbucks/mooncakes.mp4` | **Starbucks siren** | ⛔ **internal** |
| 9 | `popmart/Molly_walks_into_a_cozy_forest.mp4` | **POPMART + Snow White** | ⛔ **internal** |
| 10 | `beauty_cream.mp4` | **POND'S** | ⛔ **internal** |

**The four ⛔ rows are spec ads for live trademarks** — AB InBev, Starbucks, POP MART
(plus a Disney character design), Unilever. They are genuinely good work and they are
exactly right for an investor deck or a sales call, where the exposure is low. On a
public feed they are someone else's mark on our marketing, and the beer one additionally
trips alcohol ad-policy on both FB and Kuaishou.

**They are not wasted — they are re-renderable.** The craft is in the prompt, not the
logo. `prompts/beauty_cream.json` carries a de-branded re-render of #10 under a house
name; the same one-line swap fixes #7–#9. That is the unlock, and it costs one
generation each.

**The two ⚠️ rows, one question each:**
- **#5 `model-standing.mp4`** — photoreal human face. If the render used a pose or
  likeness reference of a real model, the output carries that person's face. Confirm the
  reference was synthetic; if it wasn't, re-render before it goes anywhere external.
- **#6 `oilight final.mp4`** — OILIGHT™ reads as a real client brand, and the opening
  desert shot is live-action with an identifiable person (licensed stock, or not ours).
  Needs the client's written OK *and* the footage provenance.

**#4 rename:** no energy-drink mark appears in any sampled frame — the brand is in the
*filename only*. Rename to `kungfu_sf_energy_spec.mp4` so the asset name stops implying
a tie-in that the footage doesn't make.

---

## 2. Channel mechanics

| | **FB — Groups, not the Page** | **Kuaishou 快手** |
|---|---|---|
| Why | Page identity is locked to Sinosphere culture edutainment. An ad-craft video in the Page feed is Position Drift. Groups don't carry that risk — same call as the 09-01 e-commerce post. | New surface, no positioning history to protect. Audience is 实体商家 / 电商卖家 / 工厂老板 — the people who actually buy batch ad production. |
| Format | **Native video upload**, single video, never a carousel. No link in the post body — FB throttles link-outs; a native upload is not one. | 竖屏 9:16 原生上传。前 3 秒必须是成品画面，不要 logo 开场。 |
| Language | English | 中文，口语，别端着 |
| CTA | **First comment**, never the body | 主页 + 私信；口播带一次官网 |
| KPI | replies, not reach | 私信数，不是播放量 |
| Drift check | ✅ group-scoped, off-Page | ✅ new account |

**Groups** (from the 09-01 series): **B1** `105108073643190` E-commerce product
photography (5.2K, ⚠️ has an explicit anti-spam ban rule) · **B2** `765595303494969`
Product Photographer USA (1.3K) · **B3** `313105103563214` Apparels/Fashion Sell & Buy
(5.0K) · **B4** `1212659302803905` Online E-Commerce sellers solution (6.9K).

**Cadence:** one post per group per ~3 days. Never the same video into two groups the
same day. B1 last — it's the ban-rule group, and a video post reads more promotional
than a teardown does.

**Kuaishou orientation note:** `kungfu_sf` and the angryAlert landscape cut are 16:9.
Kuaishou is a vertical feed — use `AngryAlert_vertical.mp4` there, and either recut
`kungfu_sf` to 9:16 or hold it for FB only.

**The CTA, both platforms** — self-serve `curify-ai.com/tools/product-video` (verified
live, renders the real inline generate surface, not a waitlist card), batch/contact
`curify-ai.com/contact` (verified live).

---

## 3. Per-video copy

### 3.1 `matcha_drink.mp4` — 15.1s · 9:16 · unbranded ✅
*The lead asset. Zero brand risk, universally legible, and beverage is a category every
seller group understands.* → **B4**, then Kuaishou.

**FB post:**
> 🍵 This is 15 seconds of iced matcha — the banana slices falling, the milk pour, the condensation on the finished glass.
>
> There was no shoot. No food stylist, no bounce card, no getting the pour right on take 40 while the ice melts and the whole setup has to be rebuilt.
>
> I'm posting it because beverage is the category where the gap is widest. A drink has to look *cold*, and cold is the single hardest thing to hold on a hot set — you're fighting condensation and melt on a clock. That's why the pour shot is the one everybody outsources.
>
> Worth saying what it isn't: it's not a substitute for shooting a product whose real texture matters to the buyer. It's a substitute for the fifth variation of a shot you already got right once.
>
> For those of you selling food and drink — where does your listing actually break down? The hero, the texture macro, or the lifestyle scene? 👇

**First comment:**
```
If you want to try it on your own product: curify-ai.com/tools/product-video
Or drop a product shot in the comments and I'll run one for you.
```

**快手文案：**
> 🍵 一杯冰抹茶，15 秒。
>
> 香蕉片落下、牛奶倒进去、杯壁上那层水珠——没拍。没有摄影棚，没有食品造型师，没有为了一个倒奶镜头拍到第 40 条、冰全化了再重摆一遍。
>
> 饮品是最难拍的品类之一。要拍出"冰"的感觉，你得跟化冰和起雾抢时间，所以倒液镜头几乎所有人都外包出去。
>
> 说句实话：真材实料的质感该拍还得拍。这东西替代的不是第一条，是你已经拍对了一次、还要再出的第五个版本。
>
> 做食品饮料的老板，你们最卡的是主图、细节图还是场景图？评论区说说。

**口播尾 / 主页：** 整条产品线可以批量做，一个 SKU 出一整套广告片。官网 curify-ai.com，批量合作私信。

---

### 3.2 `rotation_chair.mp4` — 10s · 9:16 · unbranded ✅
*The strongest B2B proof in the set — feature-explainer motion graphics normally need a
3D artist.* → **B4**, then Kuaishou (best batch-inquiry driver of the six).

**FB post:**
> 🪑 Ten seconds on an office chair: airflow rendered moving through the mesh back, a readout on the armrest as it adjusts, then a 360 in a styled room.
>
> The middle shot is the point. Airflow through a mesh back is *invisible* — you cannot photograph it. Every furniture brand that wants to sell breathability ends up commissioning a 3D artist for that one shot, and that's a quote and a two-week turnaround for six seconds of video.
>
> Same for the armrest readout. It's the shot that answers "how far does it actually adjust," which is the question that decides the sale on a chair.
>
> Hard goods are where this pays off most, I think — furniture, appliances, tools. Anything where the buyer's real question is *how does it work*, not *what colour is it*. A photo can't answer that. A diagram can, but nobody watches a diagram.
>
> If you sell hard goods: which feature of yours have you never managed to show properly? 👇

**First comment:**
```
Self-serve on your own product: curify-ai.com/tools/product-video
Catalog-scale (a full SKU line, batched): curify-ai.com/contact
```

**快手文案：**
> 🪑 一把人体工学椅，10 秒。
>
> 网背透气的气流被画出来了、扶手调节时旁边跳数据、最后一个 360 度环绕。
>
> 重点是中间那段。网背透气这事**根本拍不出来**——气流是看不见的。所以想讲透气性的家具品牌，最后都得找三维师做这一个镜头，一笔报价、两周工期，就为了 6 秒画面。
>
> 扶手那个数据条也一样。买椅子的人真正想知道的是"到底能调多少"，这个问题决定成交。
>
> 硬件品类最吃这一套：家具、家电、工具——买家关心的是**怎么用**，不是什么颜色。照片答不了，图纸能答但没人看。
>
> 做硬件的，你有哪个卖点是一直没拍明白的？评论区说说。

**口播尾 / 主页：** 一个 SKU 一整套广告片，产品线可以批量出。官网 curify-ai.com，批量合作私信。

---

### 3.3 `angryAlert/AngryAlert_vertical.mp4` — 20.3s · 9:16 · Curify-branded ✅
*Landscape cut `AngryAlert_landscape.mp4` (16s) for FB, vertical for Kuaishou.*
*The product is fictional — say so. It reads as a joke, and the joke is the hook.*
→ **B2** (the photographer group — they'll read the craft), then Kuaishou.

**FB post:**
> 📣 A finished 20-second app commercial — office scenes, an actor, a HUD overlay, a logo sting.
>
> The app does not exist. I made it up. It's called Angry Alert and it supposedly warns you before someone gets annoyed.
>
> That's the actual point. There's a whole category of thing you can't shoot yet: the app you haven't built, the SKU still at the factory, the packaging you're deciding between. That's exactly when you most need to *see* the ad — a pitch deck, a pre-order page, a "does this concept land" test before committing the budget.
>
> The old order is shoot → then market. This inverts it: you make the commercial for the thing first, look at it, and let that tell you whether the thing is worth making.
>
> The honest limit: it's convincing precisely because nothing in it has to be true. For a real product every claim on screen still has to be one you can stand behind.
>
> Has anyone here made the ad before the product? 👇

**First comment:**
```
curify-ai.com/tools/product-video — self-serve.
Concept work / batches: curify-ai.com/contact
```

**快手文案：**
> 📣 一条 20 秒的 App 广告：办公室实景、演员、HUD 特效、logo 收尾。
>
> 这个 App 不存在。我编的。叫 Angry Alert，号称能在别人生气之前提醒你。
>
> 这才是重点。有一类东西你**根本没法拍**：还没做出来的 App、还在工厂的款、正在纠结的包装。而恰恰是这个时候你最需要先看到广告长什么样——融资、预售页、或者只是想验证这个概念到底立不立得住。
>
> 以前是先做出来再营销。现在可以反过来：先把广告做出来看一眼，再决定这东西值不值得做。
>
> 但也得说清楚：它之所以好看，是因为里面没有一句话需要为真。换成真产品，屏幕上每一句都得站得住。
>
> 有没有人是先做广告后做产品的？评论区聊聊。

**口播尾 / 主页：** 概念片、产品片都能做，产品线批量出。官网 curify-ai.com，合作私信。

---

### 3.4 `redbull/kungfu_redbull_SF.mp4` — 20.6s · 16:9 · Curify-branded ✅
**⚠️ Rename to `kungfu_sf_energy_spec.mp4` before posting.** 16:9 — FB only, or recut
for Kuaishou. → **B3**.

**FB post:**
> 🥋 Twenty seconds: a kungfu figure on a tiled rooftop hung with red lanterns, a leap across a downtown rooftop, and a final stance at the Golden Gate at sunset with autumn leaves coming down.
>
> Three locations. Two of them you cannot get. Filming on the Golden Gate approach means permits, insurance, a crew call and a sunrise window you get one shot at — and rooftop-to-rooftop needs a stunt team and a closed set.
>
> This is the lane where the economics stop being close. Product photography, you can argue — a good photographer is fast and the result is real. But landmark-scale action is a five-figure line item before anyone shows up, and for most brands the honest alternative isn't a cheaper shoot, it's *not making the spot at all*.
>
> That's the shift worth naming: it's less about replacing shoots and more about the ads that never got made because the location was out of reach.
>
> Anyone here priced a location shoot recently? Curious what the real numbers look like in 2026. 👇

**First comment:**
```
curify-ai.com/tools/product-video for the self-serve version.
Campaign / batch work: curify-ai.com/contact
```

**快手文案（如重剪 9:16）：**
> 🥋 20 秒，三个场景：挂满红灯笼的瓦顶、市中心楼顶一跃、金门大桥日落收势，落叶纷飞。
>
> 三个场景里有两个是拿不到的。金门大桥要许可、保险、剧组通告，还得赌那一个日出窗口；楼顶跳跃要武行和封闭场地。
>
> 这条赛道上账根本不用算。拍产品图还能争一争——好摄影师又快又真。但地标级动作片，人还没到现场就是五位数起，对大部分品牌来说，真实的替代方案不是"拍便宜点",是**这条片子压根不拍了**。
>
> 所以真正变的不是替代拍摄，是那些因为场景够不着而从来没做成的广告。
>
> 最近有谁问过外景报价？评论区说个真实数字。

**口播尾 / 主页：** 官网 curify-ai.com，批量和 campaign 合作私信。

---

### 3.5 `model-standing.mp4` — 10s · 9:16 · ⚠️ hold pending likeness check
Copy is drafted so it's ready the moment the reference is confirmed synthetic.
**Do not post before that.** → **B3** (apparel).

**FB post:**
> 👔 A full-length on-model shot of a black suit — marble-and-brass lobby, slow orbit, ten seconds.
>
> On-model is the shot apparel sellers can least afford to skip and least afford to repeat. One model, one studio day covers maybe a handful of looks, and then a colourway drops or you list on a marketplace at a different crop and you're booking again.
>
> Two things I'd flag rather than oversell. Fabric behaviour is still the tell — how a real garment falls and creases is the thing generation is worst at, and a suit is a forgiving case because the drape is structured. And if you generate a model, the face has to be genuinely synthetic, not a real person's likeness carried over from a reference. That one is a legal problem, not a quality problem.
>
> Where do you land on generated models — using them, avoiding them, or only for flat-lay adjacent stuff? 👇

**First comment:**
```
curify-ai.com/tools/product-video — try it on one of your own products.
Full catalog runs: curify-ai.com/contact
```

**快手文案（待确认后再发）：**
> 👔 一套黑西装的全身模特图，大理石黄铜电梯厅，慢速环绕，10 秒。
>
> 服装卖家最省不掉、也最重复不起的就是模特图。一个模特一天棚拍下来也就几套，然后出新色、或者上另一个平台要不同尺寸，又得重约。
>
> 两句实话。面料的垂坠和褶皱仍然是最容易露馅的地方，西装算好做的，因为版型硬挺。另外——如果你要生成模特，那张脸必须是真合成的，不能是参考图里真人的样子带过来的。这是法律问题，不是画质问题。
>
> 你们怎么看 AI 模特图？在用、不用、还是只用在平铺图上？

---

### 3.6 `oilight/oilight final.mp4` — 26.4s · ⚠️ hold
No copy drafted. Needs the client's written OK and the source-footage provenance
(§1). Once cleared, the angle is the desert-dig opening → product end card as a
brand-story arc, which none of the other nine do.

---

### 3.7–3.10 `corona` · `mooncakes` · `Molly` · `beauty_cream` — ⛔ internal
Indexed in `index.json`, no post copy by design. Use in decks and sales calls.
For public use, re-render de-branded — `prompts/beauty_cream.json` shows the swap.

---

## 4. Suggested order

| Slot | Video | Where |
|---|---|---|
| 1 | `rotation_chair` | B4 — strongest B2B proof, clearest batch pull |
| 2 | `matcha_drink` | Kuaishou — first post, zero risk |
| 3 | `angryAlert` (landscape) | B2 |
| 4 | `rotation_chair` | Kuaishou |
| 5 | `kungfu_sf` *(renamed)* | B3 |
| 6 | `angryAlert` (vertical) | Kuaishou |
| 7 | `matcha_drink` | B1 — last, ban-rule group |
| — | `model_standing` | B3, **only after the likeness check** |

~3 days apart per group. Log every reply into `gtm_tools/relationship_leads.json` with
`channel: "facebook_group"` or `"kuaishou"` plus `need_verbatim`. Same **20-comment stop
rule** as the 09-01 series — if 20 comments produce no real conversation, stop and
re-read the demand rather than posting more.
