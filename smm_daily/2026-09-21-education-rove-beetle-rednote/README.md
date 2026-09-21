# smm_daily / education — 科普图文系列

_Series charter. Lives with the first drop; each later drop gets its own flat dated
folder named `<date>-education-<topic>-<platform>`, matching every other folder in
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
| 2026-09-21 | 隐翅虫 safety science | 4 | not yet | — | `2026-09-21-education-rove-beetle-rednote/` |
