# cultural_videos

Cultural / heritage costume video work. `costume_tryon/` was a sibling top-level
folder until 2026-09-09 and is now a subfolder here — same subject, no reason for
two entries at the root.

| folder | what it is |
|---|---|
| `tengwangge/` | 滕王阁「宴启霓裳」 — Tang banquet, Nanchang. Scenic-spot tender sample, three rounds |
| `kyoto/` | 京都「着物さんぽ」 — autumn kimono walk. Original AI character, no client photo |
| `bali/` | BALI — two generations, see below |
| `dubai/` | DUBAI — two generations, see below |
| `granada/` | GRANADA「palace, hill, cave」 — Nasrid courts down to a Sacromonte zambra |
| `wukang/` | 上海武康大楼 — autumn street-style souvenir; current v03, 20s, clean + slanted Curify watermark |
| [`london-camera-motion/`](london-camera-motion/) | London city photography motion study, 16.90s, with two music versions |
| `costume_tryon/` | earlier dynasty-costume try-on tests |
| loose files at root | earlier cultural pieces, pre-dating the subfolder convention |

All five destination folders are produced by
`curify-studio/dev/jayw/video_pipelines/costume_story_video/`, whose README
carries the method and the failure modes, and whose `STORYLINES.md` carries the
cultural research behind the three Latin destination pieces. Each cut is 30.0s,
9:16, 1080×1920, and ships in a clean and a watermarked version.

## bali and dubai — the v1 cuts are kept, and should not be sent

Same convention as `tengwangge/`: the progression is the useful part, so both
generations stay. The filename is the generation, and it maps 1:1 to the project
directory that produced it.

| file stem | generation |
|---|---|
| `bali-resort-30s` | **v1, superseded.** Eleven near-identical full-body wides, nine of them golden hour, a Western ivory maxi dress that is wrong for a Balinese temple, nobody else in frame. Its final shot is rotated 90°, and its theme line runs off the bottom of the frame reading `one photo, one fi` |
| `bali-melukat-30s` | **current.** 「melukat」the water blessing — correct temple dress, the sash tied on camera, the offering carried up, the spring taken on her face |
| `dubai-desert-30s` | **v1, superseded.** Six of eleven shots are empty sand, and a cream abaya against cream sand makes her vanish from most of them. Same two typography bugs |
| `dubai-creek-30s` | **current.** 「the creek, the souk, the sand」— dhow wharf, abra, spice and gold souks, gahwa in the majlis, falcon, blue hour |

Send the current cuts. The v1 pair is reference for why the shot list is written
the way it is, not deliverable work.

**Person depicted:** the characters in `bali/`, `dubai/` and `granada/` are
original inventions and depict nobody. No release is needed and none of the
tengwangge constraint below applies to them.

**Music:** all three Latin destination pieces currently carry the same neutral
`leberch-travel` placeholder cue, because the gallery library has no gamelan, no
oud and nothing Spanish. Each `project.json` records what its edit is actually
scored for. Replace before any client-facing send.

## tengwangge — three generations, keep them together

The progression is the useful part, so all three are kept rather than only the
newest:

- `-preview` — the first cut, built on a stock character reference.
- `-realmodel` — rebuilt after the client sent photographs of the real model.
  This is the version she critiqued: 人物说实话不是很像 … 时而不太一样, and the
  closing dance 很呆板.
- `-v3` — current. The face is a separate pass from one source photograph across
  all shots, which is what makes the eleven agree with each other; the dance is
  rewritten as movement rather than as anti-drift constraints.

**Person depicted:** `-realmodel` and `-v3` reproduce the likeness of a real
model the client supplied photographs of, for this tender. No release is on
file with us. This repo is private — keep it that way, and do not republish
these two outside the tender without checking. The client's source photographs
live in `curify-frontend/raw/tengwangge-09-07/` and are gitignored there.

`kyoto/` has no such constraint: that character is an original invention and
depicts nobody.

## ⚠️ Two files here can never be pushed

`wuG9jPf5SCrBtez7.mp4` (127 MB) and `创意西安v1.m4v` (121 MB) exceed GitHub's
**100 MB hard limit**, so a commit containing them cannot be pushed at all — the
same situation as the supplier quote already listed in the repo's `.gitignore`.
They are excluded there too. If they need versioning, this repo would need Git
LFS, which is not installed.

Everything else here is well under the limit; the largest file is the 39 MB
`bali/bali-melukat-30s-watermarked.mp4`.

## Shanghai Wukang — autumn street style (2026-10-22)

`wukang/` adds a 20-second citywalk / fashion souvenir to the original destination collection. Its current cut is project v03: aerial opening, autumn outfit, changing poses with shutter sounds, full-bleed autumn end card. Both clean and slanted Curify-watermarked masters are present. It uses the user-selected MGM reference soundtrack, not the older travel placeholder. See [version and source notes](wukang/README.md). Queued locally for Facebook and Rednote in the souvenir SMM sequence; no platform schedule or publication has been made.
