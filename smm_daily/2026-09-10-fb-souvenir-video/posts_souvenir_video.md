# Souvenir video — SMM thread (2026-09-10, extended 2026-09-12)

_The third product line. `smm_daily` already has threads for ecommerce
(`2026-09-01-ecommerce`) and retouching
(`2026-09-01-retouching` — `posts_fb.md` and `posts_rednote.md`); this opens the missing one._

> **📄 2026-09-12 — this folder is now three files.** The copy moved out into per-channel files
> and **this file is the strategy, the asset registry and the log**:
>
> | file | what it holds |
> |---|---|
> | **[`posts_fb.md`](posts_fb.md)** | English copy, **5 destinations**, dual traveller + resort/hotel voice. CTA: DM in body, `curify-ai.com` in first comment |
> | **[`posts_rednote_kuaishou.md`](posts_rednote_kuaishou.md)** | 中文 copy, same 5 destinations. CTA: **私信 only, no link anywhere** |
> | **this file** | place × trade matrix, the G1–G5 voices, red lines, schedule & log |
>
> The G1–G5 matrix below is still correct and is what single-trade rooms use. The new
> dual-audience copy in `posts_fb.md` is for **destination groups**, where travellers and
> businesses sit in the same room.

**Offer:** a visitor's photo becomes a 20–30s cinematic souvenir video — sold as an add-on to a photo
package that already exists, with no second shoot.
**CTA:** DM. English adds `curify-ai.com` in the first comment; Chinese adds nothing.
_(WhatsApp **+86 176 9219 0183** appears in the older copy blocks below and still works, but the
current CTA for new posts is the DM line above.)_

## The two rules that decide whether this works

**1. The demo must be of the place the group is about.** A Kyoto video posted into a Bali group is the
generic pitch this whole design exists to avoid — the entire advantage is that the viewer recognises
their own location before reading a word.

**2. The voice must match the trade, not just the place.** The groups below are *not* one audience
cut five ways by geography. A destination photographer sells sessions; a tour operator sells seats and
has never edited a photo; a villa or hotel sells rooms and is buying marketing, not a product to
resell. The same paragraph cannot address all three — to a photographer "no second shoot" is the
hook, to an operator it is meaningless because they were never shooting in the first place.

Both rules apply at once: **place × trade**. Get either one wrong and the post reads as the cold
pitch that failed in `Product Photography`-type groups.

## Assets

**5 destinations as of 2026-09-12.** Bali and Dubai were rebuilt from scratch; Granada is new.
All under `cultural_videos/`.

| Destination | File | Status |
|---|---|---|
| **Bali · melukat** | `bali/bali-melukat-30s-watermarked.mp4` (39MB) | ✅ **current, built 09-12** |
| **Dubai · the creek** | `dubai/dubai-creek-30s-watermarked.mp4` (28MB) | ✅ **current, built 09-12** |
| **Granada · Alhambra** | `granada/granada-alhambra-30s-watermarked.mp4` (36MB) | ✅ **current, built 09-12** |
| Kyoto / kimono | `kyoto/kyoto-kimono-30s-watermarked.mp4` (30MB) | ✅ ready |
| China heritage (滕王阁) | `tengwangge/tengwangge-30s-preview-watermarked.mp4` (22MB) | ✅ **preview cut ONLY** |
| — compressed for email | `client_VC_portfolio/tourism-souvenir-demo-09-08/tengwangge-30s-souvenir-preview.mp4` (3MB) | ✅ |
| ~~Bali v1 · resort~~ | `bali/bali-resort-30s-watermarked.mp4` | ❌ **superseded — do not post** |
| ~~Dubai v1 · desert~~ | `dubai/dubai-desert-30s-watermarked.mp4` | ❌ **superseded — do not post** |
| 滕王阁 `-realmodel` / `-v3` | `tengwangge/…` | ⛔ **never post — real model, no release** |
| Santorini | — | ❌ no demo |

### Why v1 Bali and Dubai were rebuilt (2026-09-12)

Both were technically clean and commercially flat, and the diagnosis was the same twice:
**eleven near-identical full-body wides**, one light (nine of eleven Bali frames were golden
hour), nobody else in frame, and a wardrobe that fought the piece — Bali's ivory maxi dress is
not admissible temple dress, and Dubai's cream abaya vanished against cream sand for eleven
consecutive shots.

The rebuilds fix the shot grammar (4 wides / 4 mediums / 2 no-face detail shots / exactly one
close-up on the emotional beat), put the character *inside* a named ritual instead of walking
past scenery, fill the frames with other people, and walk the light from cold dawn to lamplight.
Two shipped bugs also surfaced and are fixed: v1 Bali's **final frame is rotated 90°**, and both
v1 pieces ran their theme line off the bottom of the frame reading `one photo, one fi`.

Full post-mortem: `curify-studio/dev/jayw/video_pipelines/costume_story_video/README.md`.
The cultural research behind the three Latin destinations — which ritual, which landmark, which
garment, and why each earned its frame — is in that pipeline's `STORYLINES.md`, with sources.

⚠️ **Music on Bali / Dubai / Granada is a neutral placeholder** (`leberch-travel`). Each
`project.json` records what its edit is actually scored for (gamelan/suling · oud over frame
drum · nylon-string guitar into bulería). Fine for a group post; replace before any of these
becomes a paid deliverable or a flagship ad.

The costume try-on library is still **Chinese costumes only** — extending it is what unlocks
destinations beyond these five.

---

# Groups × voice

Five trades sit inside the destination groups, and each buys a different thing. Pick the row by
**who is in the group**, then swap in the destination and its video.

| Voice | Group shape | Who they are | What they're actually buying |
|---|---|---|---|
| 📸 **G1** Destination photographer | `Bali photographers`, `Kyoto photographers`, `Dubai photographers` | sells sessions, edits their own work | a new line item on a package they already sell |
| 💍 **G2** Wedding / elopement | `Bali wedding photographers`, `Kyoto wedding photographers`, `Destination weddings` | higher ticket, already sells a film | ⚠️ **not** a film. A short social cut the couple posts that week |
| 👘 **G3** Costume & cultural experience | `Kimono photographers`, `Hanfu photography` | rents the costume, shoots as part of the experience | the souvenir the guest came for, upgraded |
| 🚐 **G4** Tour operator / safari / villa | `Japan tour operators`, `Bali villa & tour operators`, `Dubai desert safari operators` | **does not shoot** — sells seats and stays | a per-guest upsell requiring no photography skill |
| 🏨 **G5** Luxury travel trade & expat business | `UAE luxury travel`, `Bali expats & business owners` | hotels, concierges, agencies | marketing content for their own property, and a referral line |

**Destinations, per voice:** Kyoto · Bali · Dubai · **Granada** · China heritage (滕王阁).
Santorini has no demo — do not post the pitch there.

---

## 📸 G1 — Destination photographer

*The core voice, and the one the offer was designed around. They already shoot, already sell packages,
already have the raw material sitting in Lightroom. Nothing here asks them to learn anything.*

> **For photographers in [Bali] — what if every session also came with a 30-second cinematic souvenir
> video?**
>
> This was made from a single portrait. No second shoot, no video gear, no extra day on location — it
> can be sold as an add-on to the package you already offer.
>
> The reason I think it fits your work specifically: your clients are on a trip. They go home, and the
> gallery is what the trip becomes. A stills gallery gets looked at twice and a vertical video gets
> posted — which is also the version their friends see, with your name on it.
>
> If you run photo experiences in [Bali], I'll make one free sample from one of your photos. Send me
> your favourite frame from a recent session.
>
> DM me, or WhatsApp +86 176 9219 0183.

---

## 💍 G2 — Wedding & elopement

*⚠️ **The one voice where the obvious pitch is wrong.** This audience already sells a wedding film, or
works beside a videographer who does. "We turn photos into video" reads as an attack on a line item
they or their partner already own. Position it as the short social cut, explicitly beside the film.*

> **A question for destination wedding photographers — what do your couples post the week they get
> home?**
>
> Not the gallery; it isn't ready. Not the film; that's six weeks out. They post one phone photo and
> the moment passes.
>
> This is a 30-second vertical cut made from **one** of your stills — the elopement portrait you
> already delivered in the sneak peek. It isn't a wedding film and it doesn't replace one; a film is a
> different craft and a different budget. It's the thing that fills the six weeks in between, in the
> format the couple's friends actually watch.
>
> If you shoot destination weddings in [Bali], send me one frame from a recent sneak peek and I'll cut
> one free so you can see whether it sits next to your film or gets in its way.
>
> DM, or WhatsApp +86 176 9219 0183.

---

## 👘 G3 — Costume & cultural experience

*The tightest fit in the whole matrix. The guest has already paid to be dressed and photographed — the
photo IS the souvenir, so upgrading the souvenir needs no new argument. Kyoto/kimono and 汉服 both have
a finished demo, which is rare.*

> **Kimono studios in [Kyoto] — your guests are already paying for a souvenir. This is the same
> souvenir, moving.**
>
> Made from one portrait from a dressing session. The obi, the collar, the hair — all held; only the
> setting moves around her.
>
> Why I think this belongs in your offer and not somewhere else: a kimono session is *already* an
> experience purchase. Nobody books it for documentation, they book it to have been there. A still
> says they wore it. Thirty seconds says they were in Kyoto wearing it, and that's the one they send
> to their family the same evening.
>
> Happy to make one free from a photo of yours — a recent guest shot, with their permission, or one of
> your own promo frames if you'd rather not use a client's.
>
> DM, or WhatsApp +86 176 9219 0183.

---

## 🚐 G4 — Tour operator, safari & villa

*⚠️ **They do not shoot.** Every photography word — "session", "second shoot", "your frame" — is
meaningless or off-putting here. They own guests and guest phone photos, and they are looking for
something to attach to a booking. Lead with the guest, not the camera.*

> **[Bali] tour & villa operators — every guest already leaves with a hundred phone photos and nothing
> made out of them.**
>
> This is a 30-second cinematic cut built from **one** photo. No filming, no crew, nothing added to
> your day — one image goes in, this comes back.
>
> Where it fits your business: it's a per-guest add-on you can attach at booking or sell at checkout,
> priced like a souvenir rather than like video production. You need no photography skill and no
> equipment; the guest sends a picture and we do the rest, white-label under your name if you want it
> that way.
>
> And it does something a printed souvenir can't — guests post it, tagged, to exactly the audience
> that books trips like theirs.
>
> If you run tours, villas or experiences in [Bali], send me one guest photo (with their OK) and I'll
> make a free sample.
>
> DM, or WhatsApp +86 176 9219 0183.

---

## 🏨 G5 — Luxury travel trade & expat business owners

*Mixed room: hotels, concierges, agencies, and people who simply know everyone locally. Two hooks,
because there are two buyers — the property that wants content, and the connector who wants a referral.
Keep it short; this is the least targeted of the five groups and the most allergic to a pitch.*

> **Made this from a single photo — 30 seconds, shot nowhere.**
>
> Posting it here because two different people in this group can use it.
>
> If you run a property or an experience in [Dubai]: it's content for your own channels, built from
> stills you already own. One photo per clip, no shoot, no crew — and it's vertical, which is the only
> format that travels now.
>
> If you don't, but you know the photographers and operators who would: I'll make them a free sample
> too, and I'd rather be introduced than cold-DM anyone in here.
>
> Either way, the video above is the whole pitch — one image in, that out.
>
> DM, or WhatsApp +86 176 9219 0183.

---

## What changes between voices, and what never does

| | G1 photographer | G2 wedding | G3 costume | G4 operator | G5 trade |
|---|---|---|---|---|---|
| **Opening noun** | your session | your couple | your guest | your guest | your property |
| **The hook** | add-on to an existing package | fills the six weeks before the film | the souvenir they came for | per-guest upsell, no skill needed | content you already own the stills for |
| **Free sample asked of them** | a frame from a recent session | a sneak-peek frame | a guest or promo frame | a guest phone photo | either, or an introduction |
| **Must never say** | — | "replaces your film" | — | anything about shooting, sessions or editing | a long pitch |

Never varies: **one video per post, native upload, no link in the body, CTA in the first comment or
the DM line.** And the place name and the video swap **together** — never one without the other.

---

# Schedule & progress

One post per group per **~3 days**. Never the same destination video into two groups the
same day. **Read the result per cell, not per channel** — `G3 × Kyoto` and `G4 × Dubai` are
different businesses that happen to share a folder.

**Status** ✅ sent · ◻︎ planned · ❌ no demo

| Status | Voice | Destination | Video | Group | Comments | DMs | Samples |
|---|---|---|---|---|---|---|---|
| ✅ **sent** | ⚠️ record | Kyoto | `kyoto-kimono-30s` | ⚠️ record name + size | | | |
| ✅ **sent** | ⚠️ record | China (滕王阁) | `tengwangge-30s` | ⚠️ record name + size | | | |
| ✅ **09-11** | 🚐 G4 / 🏨 G5 | Dubai | `dubai-desert-30s` | ×3 — *travel* · *agents* · *tourism* | | | |
| ◻︎ | 🌍 **dual** | Bali | `bali-melukat-30s` | a **destination** group (travellers + businesses) — first test of the dual-audience copy | | | |
| ◻︎ | 📸 G1 | Bali | `bali-melukat-30s` | `Bali photographers` — 4 tracked leads, one already DM'd with nothing to show | | | |
| ◻︎ | 👘 G3 | Kyoto | `kyoto-kimono-30s` | `Kimono photographers` — tightest offer-to-buyer fit in the matrix | | | |
| ◻︎ | 📸 G1 | Kyoto | `kyoto-kimono-30s` | `Kyoto photographers` — isolates place from trade | | | |
| ◻︎ | 🌍 **dual** | **Granada** | `granada-alhambra-30s` | a Spain / Andalucía travel group — **brand-new destination, no prior cell** | | | |
| ◻︎ | 🏨 G5 | **Granada** | `granada-alhambra-30s` | Granada hotels / carmen & tourism trade | | | |
| ◻︎ | 🌍 **dual** | Dubai | `dubai-creek-30s` | re-run of the 09-11 Dubai cell with the **rebuilt** film and dual copy | | | |
| ◻︎ | 💍 G2 | Bali | `bali-melukat-30s` | `Bali wedding photographers` — only after G1/Bali has stood a week | | | |
| ◻︎ | 👘 G3 | China | `tengwangge-30s-preview` | `Hanfu photography` — tests whether G3 is about kimono or costume generally | | | |
| ◻︎ | 🚐 G4 | Bali | `bali-melukat-30s` | `Bali villa & tour operators` | | | |
| ◻︎ | 快手 | China | `tengwangge-30s-preview` | Kuaishou — no positioning conflict, highest 文旅/汉服 base. See `posts_rednote_kuaishou.md` | | | |
| ⛔ | any | China | `tengwangge-realmodel` / `-v3` | **never — real model, no release on file** | | | |
| ❌ | any | Santorini | — | **no demo — do not post the pitch there** (rule 1) | | | |

⚠️ **The two 09-11/earlier rows above used `bali-resort-30s` / `dubai-desert-30s`, which are now
superseded.** Any re-post of those cells must use `bali-melukat-30s` / `dubai-creek-30s`. The v1
files stay in the gallery as the "before" side of the rebuild comparison, not as deliverable work.

🌍 **`dual` is a new voice row**, added 2026-09-12: the traveller + property copy in
[`posts_fb.md`](posts_fb.md), for destination groups rather than trade groups. It is a genuinely
untested cell — read it on *which half replies*, per the note at the end of that file.

---

## ✅ 09-11 · Dubai, into travel / agents / tourism

⭐ **These are G4/G5 rooms, not G1.** Travel agents, tour operators and tourism businesses
**do not shoot** — so the G1 photographer copy ("no second shoot", "one of your photos",
"the package you already offer") is meaningless or actively wrong there. G4 exists for
exactly this audience and leads with the *guest*, not the camera.

⚠️ **Confirm which copy went out.** If the G1 text was used, expect silence rather than
objection — an operator reading *"sell it as an add-on to your session"* simply doesn't have
a session. The repost should use **G4**, and the ask should be *"send me one guest photo"*,
not *"send me a frame from a recent shoot"*.

✅ **The destination match is right** — a Dubai video into Dubai groups satisfies rule 1, and
`dubai-desert-30s` is the demo built for this cell.

**What the replies will tell you.** G4 lands when the question is *"what does it cost per
guest"* or *"can it carry our name"* — both are operator questions about a resellable
add-on. If the replies are about camera gear or editing, the room is photographers after
all, and the cell should be re-logged as G1.

## ✅ earlier · Kyoto and Tengwangge

Both went out before this doc had a log. **Record the groups and their sizes** — without
them these two are unattributable, which is the exact failure already sitting in
`gtm_tools/outreach_denominator.csv` for RedNote: a closed ¥27,800 deal with no denominator,
so it compares to nothing.

Kyoto is the highest-value cell to reconstruct: a `kimono` room is **G3** (the guest already
paid for a souvenir, so upgrading it needs no argument) while `Kyoto photographers` is
**G1**. Those are different businesses, and the same video serves both — knowing which one
received it is the difference between a reusable finding and an anecdote.

## ⚠️ What must not be claimed

The **only closed deal** in this vertical (client-007, ¥27,800) was **文创 merchandise, not video**,
and `gtm-progress.md` rates that shape low-repeat / high-manufacturing-risk / 做完案例不复制.

So: **no attraction, photographer or operator has bought this format.** Present the videos as examples
of the format. Do not imply a client engagement, and do not name one. This applies hardest in G5,
where "who else have you done this for" is the first question in the room.

Every demo is a synthetic character in an unbranded setting — no real person, no real property, no
visible mark. Do not caption any of them as a guest, a client session, or a named location's official
content.

## Log

The table in **Schedule & progress** is the working record. Mirror each row into
`gtm_tools/outreach_denominator.csv` so this channel stays comparable to email and RedNote:

```
date | voice | destination | group | members | demo | views | comments | DMs | samples | paid
```

Stop and evaluate **per cell**, not per channel. The question is whether
`destination photographer × souvenir video` converts — not whether "Facebook works".
