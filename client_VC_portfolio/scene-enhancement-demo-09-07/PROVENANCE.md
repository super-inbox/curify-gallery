# Scene-enhancement demo — 2026-09-07

Outreach collateral for the `studio_portfolio` motion (photography studios).

## Why this exists

It replaces `curify-frontend/raw/context-enrichment-08-31/ai-gen.png` as the
attachable asset. That file is **not usable for marketing**: it was rendered to
client-008's spec using their 关键词模板 — a working asset the §7z record
withholds as "not ours to republish" — while we are in a competitive 试稿
against another vendor for that same job.

## Provenance of these files

- Generated end-to-end from our own prompt (`gen_scene_demo.py`, prompt inline).
- `00-base.png` is synthetic. **No real person appears in any of these frames**,
  so there is no likeness question and nothing here is a client's material.
  (This applies to `00-base.png`, `01-*.png` and `_contact-sheet.jpg`. For
  `wedding-retouch.png`, see the section at the bottom.)
- Subjects are adults. The capability shown — subject locked, background
  changed — is identical regardless of the subject's age, so there was no reason
  to synthesise children for a marketing asset.
- `01-*.png` were produced by feeding `00-base.png` back in and changing ONLY the
  backdrop. Two independently generated images would be two different people and
  would not demonstrate a locked subject — it would be a fake before/after.

## What it demonstrates

Same face, same sweater ribbing and folds, same trouser crease, same pose, same
framing; three backdrops (white sweep / grey plaster / daylight interior).
That is the claim the `studio_portfolio` voice makes, and this is evidence for it.

`_contact-sheet.jpg` (894x1842) is the single attachable file.

## Still true

No delivered-outcome claim attaches to these. They show what we can run, not
what a named client accepted.

---

## `wedding-retouch.png` — added 2026-09-09, different provenance

⚠️ **This file did not come off our stack.** The PNG carries
`kMDItemWhereFroms: https://chatgpt.com/` and a Chrome quarantine record — it was
generated in a third-party chat model and downloaded, not produced by
`gen_scene_demo.py`. There is no generation script for it in this folder.

What that does and does not change:

- **Red-line-1 clean.** No client, no named brand, no real person's session. Its own
  footer says *"AI-generated retouching concepts"*. Both frames of each pair are
  synthetic, so the "before" is not anyone's raw file.
- **Not evidence of our pipeline.** It cannot be captioned as a run of our stack, and
  the rest of this folder's claim — *our own prompt, end to end* — does not cover it.
  It is a positioning card: 3 before/after pairs (cliff-top relight, portrait skin and
  hair, beach relight with cleanup), 1122×1402, with a `curify-ai.com` /
  *"DM for studio & batch projects"* footer baked in.
- **Never crop the footer.** That line is what keeps the card inside the
  no-delivered-outcome rule.

To make it usable as proof rather than as a poster, re-render the three pairs through
our own pipeline and replace the file. `smm_daily/2026-09-01-fb-retouching/`
post 8 is written and held pending exactly that.
