# Daily Inspirations — 2026-07-01

Owner: hongjie

Drop new nano-template inspiration assets in this folder using the
existing daily-drop convention:

    template-<template-id>-<descriptive-suffix>.jpg

Notes:
- Filename suffix becomes the inspiration's id_suffix in
  nano_inspiration.json after ingestion via scripts/sync_nano_inspiration.cjs.
- One image per inspiration; no nested subfolders.
- Free-text .txt files in this folder are accepted as research notes
  and ignored by the sync script.

Pipeline (frontend side, runs after assets land here):
1. Cherry-pick the matching nano_templates.json delta from the
   hongjie28-patch-<N> branch (per memory feedback_hongjie_patch_branches.md).
2. Run scripts/add_<source>_<date>_i18n.py for the new templates
   (10-locale i18n in the same workflow, per feedback_daily_drop_i18n.md);
   backfill rank_score (default 90) per feedback_daily_drop_rank_score.md.
3. node scripts/sync_nano_inspiration.cjs --supabase
4. bash scripts/sync_large_assets.sh
5. Commit + push curify-frontend; delete the remote hongjie28-patch-<N> branch.

Status: pending drop.
