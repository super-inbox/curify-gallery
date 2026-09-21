# smm_daily / education — 科普图文系列

_Series charter. Lives with the first drop; each later drop gets its own flat dated
folder named `<date>-education`, matching every other folder in
`smm_daily/`. Link back here rather than copying these rules._

Drops where the hook is **a fact that corrects a common belief**, delivered as a
small set of infographic cards generated from shipped nano templates.

Started 2026-09-21 with the 隐翅虫 (rove beetle) set.

## The rule this series lives or dies by

RedNote · Curify's algo identity is **Chinese history/culture reverse-trivia,
text-first** (see `smm-account-positioning-playbook`). A card-first "education"
series is *off* that identity, and flashcard-style cards as the flagship format
are a measured bottom performer.

So every drop here must clear one bar before it is written:

> **Does it have a reverse-trivia core — a sentence that tells the reader the
> opposite of what they assume?**

If yes, it can run on RedNote · Curify as a text-first post with the cards as the
payoff. If no, it is a utility post and belongs somewhere else, or nowhere.

The 隐翅虫 set clears it: *the beetle doesn't bite you — your own slap is the
injury.* Column name is therefore **「反常识科普」**, not「教育科普」. Same content,
but the first one is on-identity and the second is drift.

## House rules for a drop

1. **Ground every claim in a source document**, committed or linked. These posts
   give health and safety advice; an invented number here is not a typo.
2. **Reuse a shipped nano template per card**, with the parameter recorded, so a
   reader who clicks through can reproduce the card. The template page is the
   landing page.
3. **Run the CJK transcription QA** (`curify-frontend/scripts/qa_cjk_transcribe.cjs`)
   on every card before publishing. Image models draw plausible *wrong*
   characters — round 1 of the 隐翅虫 set shipped 袴 for 将, 捐伤 for 损伤, the
   Japanese shinjitai 軽軽 for 轻轻, and an entirely fabricated pie chart. None of
   it was visible at thumbnail size.
4. **Never put a prohibition in the facts block** of a generation prompt. It gets
   treated as content and rendered onto the card. Prohibitions go in the
   instruction block; facts stay positive.
5. **Publish the watermarked copies**; keep clean masters in
   `curify-frontend/raw/<topic>/out/`.
6. **Strip third-party identifiers** from source documents — company names,
   hotlines, addresses. The facts are public; the contact details are not ours.

## Drops

| Date | Topic | Cards | Posted | Read-out | Folder |
|---|---|---|---|---|---|
| 2026-09-21 | 隐翅虫 safety science | 4 | ✅ 3 posts, RedNote | pending — see below | `2026-09-21-education/` |

---

# Schedule & progress

Same shape as the sibling threads (`../2026-09-01-retouching/posts_fb.md`,
`../2026-09-10-fb-souvenir-video/README.md`) so this channel stays comparable.

**Status** ✅ sent · 🔴 sent off-plan · ◻︎ planned · ⛔ blocked

Copy for all three is in [`captions_rove_beetle.md`](captions_rove_beetle.md). All four cards
went out watermarked; clean masters are in `curify-frontend/raw/隐翅虫-smm-09-21/out/`.

| Status | Post | Cover | Cards in post | Account | 点赞 | 收藏 | 评论 | 进推荐 |
|---|---|---|---|---|---|---|---|---|
| ✅ **09-21** | **1 · 主贴** — 不咬人也不喷毒，那一巴掌才是伤你的 | `03_why_not_slap.png` | 03 → 01 → 02 → 04 | ⚠️ record | | | | |
| ✅ **09-21** | **2** — 它到底长什么样 | `01_structure_bilingual.png` | 01 | ⚠️ record | | | | |
| ✅ **09-21** | **3** — 四步 + 防护清单 | `04_first_aid_and_prevention.png` | 04 | ⚠️ record | | | | |

⚠️ **Three fields are unrecorded and only you can fill them:** which account each post went to,
the post URLs, and the posting times. Without the account this drop is unattributable — the whole
point of the read-out below is *which identity* the algorithm rewarded, and that cannot be
recovered later.

⚠️ **All three went out the same day.** The sibling threads run one post per room per ~3 days
precisely to avoid self-collision; three posts from one account in one day is a different
cadence than anything else in `smm_daily`. Worth noting in the read-out whether posts 2 and 3
suppressed each other, because if they did it is a cadence result, not a topic result.

ℹ️ **Card 02 (`02_species_science.png`) is not a cover anywhere** — it only appears inside post 1's
carousel. If post 1 underperforms, 02 is the spare cover to test, not a fifth card to make.

## What to read, and when

KPI is **收藏 + 评论**, not 点赞 and not clicks — this is the reach-authority engine
(see *The rule this series lives or dies by* above).

Fill the table at **+48h** and again at **+7d**, then answer the three questions this drop exists
to answer:

1. **Did the reverse-trivia hook carry it?** Post 1 leads on the 反常识 line; posts 2 and 3 are
   reference material. If 1 outperforms 2 and 3 by a wide margin, the hook is doing the work and
   「反常识科普」 is the right column name. If they perform alike, the topic is doing the work and
   the column can be broader.
2. **Was 科普 off-identity for the account?** This was filed as a 20% exploration bet against an
   account whose proven identity is CN history/culture reverse-trivia. Compare 收藏率 against a
   recent history/culture post from the same account — not against other education posts, of
   which there are none yet.
3. **Go / no-go on a 固定栏目.** Only make this a standing column on a clear yes to both.

Mirror the result into `gtm_tools/outreach_denominator.csv` so RedNote stays comparable to
the FB and email channels.

```
date | account | column | post | cover | 点赞 | 收藏 | 评论 | 推荐 | DMs
```
