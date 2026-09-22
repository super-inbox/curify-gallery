# Going public — what is actually blocking it

_2026-09-22. Written when `client_VC_portfolio/` was moved out to `curify-gtm` with the
intent of making this repo public._

**The move is done and it was the right move. It is not sufficient.** Two blockers remain,
and the second one is not fixable by deleting files.

---

## ⛔ Blocker 1 — `smm_daily/` is still here, and our own rule says it must not be

`curify-studio/docs/asset-authority-distribution-inventory.md` §1:

> **私有敏感资产**（VC / 销售 SOP / daily_report / smm_daily）→ 独立 private 库或云盘，
> **绝不进 public repo**。

Still tracked in this repo right now:

| path | tracked files |
|---|---|
| `smm_daily/` | **233** |
| `daily_report/` | 2 |

`smm_daily/` is not marketing samples. It contains the live commercial operation: Facebook
**group IDs and member counts**, which rooms were posted into on which day and what came back,
buyer-side analysis, the stop rules, competitor observations, and the reasoning behind pricing
and positioning. Two tracked files also carry a **personal WhatsApp number**.

Publishing it hands a competitor the target list and the playbook, and publishes a personal
phone number permanently.

**Fix:** move `smm_daily/` and `daily_report/` to `curify-gtm` the same way
`client_VC_portfolio/` just went, or accept that this repo stays private.

---

## ⛔ Blocker 2 — the history *is* the content

> "fine to have git history but not actual content"

**This is not how git works, and it is the dangerous one.** Deleting a file from `HEAD`
removes it from the current checkout. Every committed version stays in the object database and
is retrievable by anyone who can clone the repo:

```
git log --all --diff-filter=A --name-only -- client_VC_portfolio   # lists them
git show <sha>:<path> > recovered.pdf                              # recovers the bytes
```

Measured in this repo on 2026-09-22, **after** the move:

- **180 distinct client files** under `client_VC_portfolio/` exist in history
- spot-checked three: 1.30 MB, 1.06 MB and 1.46 MB recovered intact
- pack size **9.63 GiB**
- the paths themselves name counterparties — a state broadcaster's animation arm, a university
  press, a named individual on a supplier quote. **Path names leak even where a blob does not.**

Making the repo public publishes all of that to anyone who runs `git clone`.

### What would actually be required

1. **Rewrite history** — `git filter-repo --path client_VC_portfolio --invert-paths`
   (BFG is the alternative). This rewrites every commit SHA in the repo.
2. **Force-push** the rewritten history to every branch and tag.
3. **Every existing clone must be deleted and re-cloned.** An old clone still holds the old
   objects and can push them back.
4. **Expire the reflog and GC** on the remote, or ask GitHub Support to run it — otherwise
   unreferenced objects stay reachable by direct SHA for a while.
5. Only then flip visibility.

⚠️ **Order matters.** Flip to public first and the window between publishing and rewriting is
enough for anyone to clone the whole history. Rewrite first, verify, then flip.

⚠️ **The 9.63 GiB is mostly binaries** — videos, PDFs, rar archives — committed over the
repo's life. A history rewrite is also the only way that number comes down.

---

## What was done on 2026-09-22

- `Curify_GTM/csig_china_image_graphics/` deleted — byte-identical duplicate of the copy
  already under `client_VC_portfolio/`.
- `client_VC_portfolio/` (1.4 GB) moved to `curify-gtm`, untracked here, and added to
  `.gitignore` so it cannot be re-added by accident.
- The 132 previously-versioned files (~158 MB) were committed to `curify-gtm`; the remaining
  ~1.25 GB sits on disk unversioned, deliberately — committing large binaries is what produced
  the 9.63 GiB problem described above.
- Seven references across four SMM threads repointed to `curify-gtm/client_VC_portfolio/...`.

**Net effect: this repo's working tree is clean of client material. Its history is not, and
`smm_daily/` was never part of the move.** Both blockers above are open.
