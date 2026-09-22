# Souvenir video — SMM thread (opened 2026-09-10)

A visitor's photo becomes a ~30s cinematic film of the place they were. Sold as an add-on to a
photo package that already exists, with **no second shoot**.

This file is the whole strategy: assets, publish status, the voice matrix, the red lines and the
log. The copy lives in two channel files.

| file | what it is |
|---|---|
| [`posts_fb.md`](posts_fb.md) | English copy for Facebook groups — 5 destinations, dual traveller + resort/hotel voice, plus the five single-trade variants. CTA: DM in body, `curify-ai.com` in first comment |
| [`posts_rednote_kuaishou.md`](posts_rednote_kuaishou.md) | 中文 copy for 小红书 / 快手 — same 5 destinations. CTA: 私信 only, **no link anywhere** |

---

## Assets × publish status

**5 destinations.** Post masters (22–39MB, watermarked) in
`curify-gallery/cultural_videos/<destination>/`, built by
`curify-studio/dev/jayw/video_pipelines/costume_story_video/`.

**`demos/tourism-souvenir-demo-09-08/`** — moved into this thread 2026-09-14 from
`curify-gtm/client_VC_portfolio/smm/`. These are the **email-sized cuts** (2.5–5.4MB) of the same five
destinations, and they are **live attachments**: `gtm_tools/batch_tourism_2026-09-08.json`
and `batch_hotels_2026-09-12.json` attach them by absolute path. Those paths had been broken
since the folder was moved outside git; they are repointed here and now resolve. **Do not
move `demos/` without updating those two files.** Use the `cultural_videos/` masters for
social posts and the `demos/` cuts for email — a 39MB attachment will not send.

✅ posted · ◻︎ not yet · ⛔ never

| Destination | Asset (`cultural_videos/`) | FB groups | 小红书 | 快手 |
|---|---|---|---|---|
| **Bali · melukat** | `bali/bali-melukat-30s-watermarked.mp4` (39MB) | ✅ **09-13** — found via `bali photographer`, `bali villa` | ◻︎ 🔴 未发 | ⚠️ 待确认 |
| **Dubai · the creek** | `dubai/dubai-creek-30s-watermarked.mp4` (28MB) | ✅ **09-13** `dubai resorts`/`dubai travel` · ✅ **09-17** `dubai photography` 🔴 撞群 | ◻︎ 🔴 未发 | ⚠️ 待确认 |
| **Granada · Alhambra** | `granada/granada-alhambra-30s-watermarked.mp4` (36MB) | ✅ **09-13** — `granada`, `granada tour` | ◻︎ 🔴 未发 | ⚠️ 待确认 |
| **Kyoto · kimono** | `kyoto/kyoto-kimono-30s-watermarked.mp4` (30MB) | ✅ **09-17** — via `kimono`（另有更早一次 pre-log，群未记录） | ◻︎ | ◻︎ |
| **China · 滕王阁** | `tengwangge/tengwangge-30s-preview-watermarked.mp4` (22MB) | ◻︎ *(earlier, pre-log)* | ◻︎ | ◻︎ **best first pick** — no positioning conflict, largest 文旅/汉服 base |
| ~~Bali v1 · resort~~ | `bali/bali-resort-30s-watermarked.mp4` | ⛔ superseded | ⛔ | ⛔ |
| ~~Dubai v1 · desert~~ | `dubai/dubai-desert-30s-watermarked.mp4` | ⛔ superseded | ⛔ | ⛔ |
| 滕王阁 `-realmodel` / `-v3` | `tengwangge/…` | ⛔ **never** | ⛔ | ⛔ |
| Santorini | — | ❌ no demo — do not post the pitch there | ❌ | ❌ |

### ✅ 09-17 · 京都进 `kimono` 群 —— 矩阵里贴合度最高的一格，而且是按计划走的

这一格本来就排在表上，说明写的是「tightest offer-to-buyer fit」，现在跑了。

⭐ **它之所以是最紧的一格：和服体验的客人本来就是为「留个纪念」付的钱。**
升级那个纪念品不需要额外论证 —— 不像跟摄影师解释"这是可以加价卖的加购项"，
和服店老板自己就知道客人要带什么回家。这也是唯一一格 demo 和买家完全同源的：
`kyoto-kimono-30s` 拍的就是这件事本身。

**回来看什么：** 问「一条多少钱」「能不能挂我们店名」→ 体验商家在算加购账，对了；
问「用什么软件做的」→ 落到了同行摄影师手里，那是 G1 不是 G3。

### 🔴 09-17 · 迪拜进 `dubai photography` 群 —— 买家对，但和修图线三天内撞了同一批人

`../2026-09-01-retouching/posts_fb.md` 的 **W3（09-14）** 发进了四类群，
其中两类是 **`dubai photographer`** 和 `UAE photographer`。
今天旅拍的迪拜片子又发进 **`dubai photography`** 群。

**买家没错 —— 目的地摄影师本来就同时是这两样东西的买家**：
他们拍片所以需要后期，他们卖套餐所以可以加卖纪念短片。
`2026-09-10-fb-three-campaigns/campaign_matrix.md` 里 Dubai 这一格本来就写着两条线配对。

**错的是节奏。** 标准是「一个群每 ~3 天一帖」，而且**从来不是两个不同的报价**。
现在的情况可能是：同一批迪拜摄影师 09-14 收到"我们做白标修图"，
09-17 收到"把客人照片做成纪念短片"。**三天两个不同的生意**，读起来就是广撒网 ——
而评论区触达这套打法的全部前提就是不广撒网。

**这是第二次撞了，而且方向反过来了。** 09-14 记的那次是修图 W3 撞进旅拍的 `dubai travel`；
这次是旅拍撞进修图的 `dubai photographer`。两张排期表互相看不见，所以**这会一直发生**。

⚠️ **下一条迪拜内容之前必须做的两件事：**
1. **把两个线程的迪拜群 ID 对一遍。** 真重叠了就**给那个房间只留一个 offer**。
2. **选哪一个：留旅拍短片。** 理由是它是**加购**不是替代 ——
   摄影师可以把它加进现有套餐去卖，不用换掉任何现有供应商；
   白标修图要求他们换掉或补上一个后期环节，决策更重、周期更长。
   先卖那个更容易说"好"的。

### 🔴 09-14 · 和修图线撞群的风险（Dubai）

`../2026-09-01-retouching/posts_fb.md` 的 **W3** 在 09-14 发进了四类群，其中一类是
**`dubai travel`** —— 而本线程 09-11 的迪拜投放正是 *travel · agents · tourism*。

**如果是同一个群，它在三天内收到了我们两个不同的报价**：先是给他们客人做的纪念短片，
再是给摄影师做的修图。这读起来就是广撒网，而"评论区触达"这套打法的全部前提是不广撒网。

⚠️ **下一条迪拜内容发出去之前，把两个线程的群 ID 对一遍。** 两张排期表互相看不见 ——
它们是两个文件、两张表，这是第一次撞上。真撞了就**给那个房间只留一个 offer**：
**留旅拍短片** —— 那批人手里有的是客人，不是相机；修图那条对他们没有意义。

### Two things the 09-13 round still owes the log

1. **Group names and member counts.** The search keywords above record *how* the groups were
   found, not *which* groups received the post or how big they were. Without the group and its
   size there is no denominator, and the cell cannot be compared to anything — the exact failure
   already sitting in `gtm_tools/outreach_denominator.csv` for RedNote, where a ¥27,800 close has
   no denominator and so compares to nothing. Fill these in from the posting history while it is
   still recoverable.
2. 🔴 **更正（09-14）：小红书那三条没有发过。** 这一条原本写的是"三条已经违反定位文档发出去了"，
   并据此要求去改 `smm-account-positioning-playbook-2026-07-05.md`。**前提是错的，要求也撤回。**
   小红书这条渠道还没开张，定位冲突仍然是**未解的前置条件**，不是既成事实 ——
   处理方式见 `../2026-09-01-retouching/posts_rednote.md` 开头那一节：改文档，或者开第三个号，二选一。
   同一批记录里的快手三条也需要核实。
   ⚠️ 教训：**把没发的记成已发，比空着更危险** —— 空着只是缺数据，记错会让后面每个判断都建在假分母上。

⚠️ **Music on Bali / Dubai / Granada is a neutral placeholder** (`leberch-travel`). Each
`project.json` records what its edit is actually scored for (gamelan/suling · oud over frame drum ·
nylon-string guitar into bulería). Fine for a group post; replace before any of these becomes a
paid deliverable or a flagship ad.

### Why v1 Bali and Dubai were rebuilt (2026-09-12)

Both were technically clean and commercially flat, same diagnosis twice: **eleven near-identical
full-body wides**, one light (nine of eleven Bali frames were golden hour), nobody else in frame,
and a wardrobe that fought the piece — Bali's ivory maxi dress is not admissible temple dress, and
Dubai's cream abaya vanished against cream sand for eleven consecutive shots.

The rebuilds fix the shot grammar (4 wides / 4 mediums / 2 no-face detail shots / exactly one
close-up on the emotional beat), put the character *inside* a named ritual instead of walking past
scenery, fill the frames with people, and walk the light from cold dawn to lamplight. Two shipped
bugs also surfaced and are fixed: v1 Bali's **final frame is rotated 90°**, and both v1 pieces ran
their theme line off the bottom of the frame reading `one photo, one fi`.

Full post-mortem and the cultural research with sources: that pipeline's `README.md` and
`STORYLINES.md`.

The costume try-on library is still **Chinese costumes only** — extending it is what unlocks
destinations beyond these five.

---

## The two rules that decide whether this works

**1. The demo must be of the place the group is about.** A Kyoto video in a Bali group is the
generic pitch this whole design exists to avoid — the advantage is that the viewer recognises their
own location before reading a word. **The place name and the video swap together, never one
without the other.**

**2. The voice must match the trade, not just the place.** These groups are *not* one audience cut
five ways by geography. A destination photographer sells sessions; a tour operator sells seats and
has never edited a photo; a hotel sells rooms and is buying marketing, not a product to resell. To
a photographer "no second shoot" is the hook; to an operator it is meaningless because they were
never shooting.

Both apply at once: **place × trade**. Get either wrong and it reads as the cold pitch that failed
in `Product Photography`-type groups.

## Groups × voice

Pick the row by **who is in the group**, then swap in the destination and its video. Full copy for
each is in [`posts_fb.md`](posts_fb.md).

| Voice | Group shape | Who they are | What they're actually buying |
|---|---|---|---|
| 🌍 **dual** | destination groups — travellers *and* businesses in one room | both | *the* default since 09-12; traveller para + property para, one ask |
| 📸 **G1** Destination photographer | `Bali photographers`, `Kyoto photographers` | sells sessions, edits their own work | a new line item on a package they already sell |
| 💍 **G2** Wedding / elopement | `Bali wedding photographers`, `Destination weddings` | higher ticket, already sells a film | ⚠️ **not** a film. The short social cut the couple posts that week |
| 👘 **G3** Costume & cultural experience | `Kimono photographers`, `Hanfu photography` | rents the costume, shoots as part of the experience | the souvenir the guest came for, upgraded |
| 🚐 **G4** Tour operator / safari / villa | `Bali villa & tour operators`, `Dubai desert safari operators` | **does not shoot** — sells seats and stays | a per-guest upsell needing no photography skill |
| 🏨 **G5** Luxury travel trade & expat business | `UAE luxury travel`, `Bali expats & business owners` | hotels, concierges, agencies | content for their own property, and a referral line |

| | G1 photographer | G2 wedding | G3 costume | G4 operator | G5 trade |
|---|---|---|---|---|---|
| **Opening noun** | your session | your couple | your guest | your guest | your property |
| **The hook** | add-on to an existing package | fills the six weeks before the film | the souvenir they came for | per-guest upsell, no skill needed | content you already own the stills for |
| **Free sample asked of them** | a frame from a recent session | a sneak-peek frame | a guest or promo frame | a guest phone photo | either, or an introduction |
| **Must never say** | — | "replaces your film" | — | anything about shooting, sessions or editing | a long pitch |

---

## Red lines

1. ⛔ **Never post `tengwangge-30s-realmodel` or `-v3`.** They reproduce the likeness of a **real
   model** whose photographs a client supplied for a tender, and **no release is on file**. Tender
   material in a private repo. The `-preview` cut is synthetic and is the one that posts. In doubt,
   post Kyoto.
2. ⛔ **Never post `bali-resort-30s` or `dubai-desert-30s`.** Superseded 09-12.
3. ⛔ **No client claims.** The only closed deal in this vertical (client-007, ¥27,800) was 文创
   merchandise, **not video**. **No attraction, hotel, photographer or operator has bought this
   format.** Every film is an example of the *format*. "Who else have you done this for" is the
   first question in a trade room; the honest answer is "nobody yet — that's why the first is free."
4. ⛔ **Never caption a demo** as a guest, a client session, or a named property's content. Every
   character is invented and depicts nobody.
5. ⛔ **No prices** in the post body. Price is a DM conversation.
6. **Single native video, never a carousel.** Proven dead on FB·Curify.
7. **Groups only, never the FB·Curify Page feed** — the Page identity is East-Asian language &
   culture edutainment, and a souvenir pitch there is Position Drift.

---

## Schedule & log

One post per group per **~3 days**. Never the same destination video into two groups the same day.
**Read the result per cell** (`destination × trade`), not per channel: `G3 × Kyoto` and `G4 × Dubai`
are different businesses that happen to share a folder.

| Status | Voice | Destination | Channel / group | Members | Comments | DMs | Samples |
|---|---|---|---|---|---|---|---|
| ✅ **09-13** | 🌍 dual | Bali | FB — via `bali photographer`, `bali villa` | ⚠️ record | | | |
| ✅ **09-13** | 🌍 dual | Dubai | FB — via `dubai resorts`, `dubai travel` | ⚠️ record | | | |
| ✅ **09-13** | 🌍 dual | Granada | FB — via `granada`, `granada tour` | ⚠️ record | | | |
| ◻︎ | 中文 | Bali · Dubai · Granada | 小红书 ×3 | 🔴 **更正 09-14：没有发过。** 之前记成 ✅ 09-13，是错的 | | | |
| ⚠️ | 中文 | Bali · Dubai · Granada | 快手 ×3 | **待确认** —— 同一批记录里小红书那行是错的，这行也要核 | | | |
| ✅ 09-11 | 🚐 G4 / 🏨 G5 | Dubai | FB ×3 — *travel* · *agents* · *tourism* | 🔴 **可能与修图线撞群** —— 见下 | | | |
| ✅ earlier | ⚠️ unrecorded | Kyoto | FB — pre-log | ⚠️ record | | | |
| ✅ earlier | ⚠️ unrecorded | China (滕王阁) | FB — pre-log | ⚠️ record | | | |
| ◻︎ | 快手 | China (滕王阁) | **next pick** — no positioning conflict, biggest 文旅/汉服 base | | | | |
| ✅ **09-17** | 👘 G3 | Kyoto | FB — via `kimono` | ⚠️ record | | | |
| ◻︎ | 📸 G1 | Kyoto | `Kyoto photographers` — isolates place from trade | | | | |
| ✅ **09-17** | 📸 G1 | Dubai | FB — via `dubai photography` | 🔴 **与修图 W3 撞群** — 见下 | | | |
| ◻︎ | 🏨 G5 | Granada | Granada hotels / carmen & tourism trade | | | | |
| ◻︎ | 💍 G2 | Bali | `Bali wedding photographers` — only after Bali has stood a week | | | | |
| ◻︎ | 🚐 G4 | Bali | `Bali villa & tour operators` | | | | |
| ❌ | any | Santorini | **no demo — do not post** (rule 1) | | | | |

Mirror each row into `gtm_tools/outreach_denominator.csv` so this channel stays comparable to
email and RedNote:

```
date | voice | destination | group | members | demo | views | comments | DMs | samples | paid
```

**The signal to watch, now that 09-13 is out:** *which half replies.* If travellers reply and
properties don't, the offer is B2C and should be priced and sold that way. If properties reply and
travellers don't, drop the traveller paragraph and go back to the G1–G5 matrix. If neither, the
destination is wrong, not the copy.

Related: 40 hotels in Bali / Dubai / Granada / Kyoto were emailed the same films in their own
languages on 09-12 — `curify-studio/gtm_tools/HOTEL_VIDEO_BATCH_2026-09-12.md`. That batch and
these posts hit the **same buyers in the same week**, so a property replying to either should be
checked against both before it is counted twice.
