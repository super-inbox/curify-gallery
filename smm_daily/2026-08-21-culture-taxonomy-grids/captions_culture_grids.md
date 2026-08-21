# SMM · 古代…的不同叫法 taxonomy grids · 2026-08-21

10 images in the format that produced our best Facebook post to date.
Source references: `curify-frontend/raw/culture-images-08-21/`.

## Why this format

From the FB dashboard screenshot (2026-08-21):

| post | views | viewers | engagement | comments |
|---|---:|---:|---:|---:|
| **"One civilization, many…"** (古代建筑的不同叫法) — SINOSPHERE | **26,149** | 17,278 | **4,095** | 4 |
| same post — Chinese Culture group | 10,459 | 7,776 | 1,520 | 6 |
| "East Asia stands out…" (IQ ranking grid) — SINOSPHERE | 13,587 | 7,615 | 1,392 | **71** |
| same post — 3 smaller groups | 1,010 / 1,002 / 670 | | | |

The architecture grid did **2x the views and 3x the engagement** of the ranking grid.
It is also the safer of the two: the IQ post earns its 71 comments from argument, and the
underlying national-IQ data is contested — so these 10 all follow the **taxonomy** format,
not the ranking format.

Reference anatomy: brush-calligraphy title, 4-column grid, one ink-and-watercolor object per
cell in three-quarter view, ONE Chinese character beneath each, rice-paper ground, no borders,
no English. Posted with a link to `curify-ai.com/topics/culture`.

## The 10

| # | file | title | what it teaches |
|---|---|---|---|
| 1 | `01-bronze-vessels.jpg` | 古代青铜器的不同叫法 | ritual bronzes: 鼎 尊 爵 壶 豆 盘 钟 镜 … |
| 2 | `02-instruments.jpg` | 古代乐器的不同叫法 | 琴 瑟 琵 笛 箫 笙 钟 鼓 … |
| 3 | `03-weapons.jpg` | 古代兵器的不同叫法 | 剑 刀 矛 戟 戈 钺 弓 弩 … |
| 4 | `04-garments.jpg` | 古代服饰的不同叫法 | 襦 裙 袍 衫 冠 巾 履 屐 … |
| 5 | `05-vessels-daily.jpg` | 古代器皿的不同叫法 | 碗 碟 盏 杯 瓶 罐 缸 钵 … |
| 6 | `06-furniture.jpg` | 古代家具的不同叫法 | 案 几 榻 屏 橱 柜 凳 椅 … |
| 7 | `07-scholar-desk.jpg` | 文房用具的不同叫法 | 笔 墨 纸 砚 洗 镇 印 匣 … |
| 8 | `08-headwear.jpg` | 古代衣饰配件的不同叫法 | 冠 巾 笠 盔 簪 钗 环 梳 … |
| 9 | `09-bridges.jpg` | 古代桥梁的不同叫法 | 拱 廊 索 梁 浮 亭 栈 渡 … |
| 10 | `10-boats.jpg` | 古代舟船的不同叫法 | 舟 船 舫 艇 筏 桨 帆 锚 … |

## Caption template (EN — the groups that performed are English-language)

> One word in English, sixteen in Chinese.
>
> English calls all of these "[X]". Classical Chinese gave each one its own character —
> and the character tells you what it was for, not just what it looked like.
>
> [one concrete example, e.g. 案 is a long narrow table for writing; 几 is the low one you
> sit beside; 榻 is the one you nap on.]
>
> Which of these does your language distinguish?
>
> More: curify-ai.com/topics/culture

**Why that last line matters.** The reference post asks a question and links to
`/topics/culture`. The question is what produced 4,095 engagements; the link is what makes the
reach worth having. Keep both. Post the link as a comment if the group throttles link posts.

## Production notes (read before generating more)

Generated with `gemini-3-pro-image-preview` (NOT flash — flash garbles CJK).
Script: `/tmp/gen_culture.py` pattern, `response_modalities=["IMAGE","TEXT"]`.

**The failure mode is rare characters.** First pass used the archaic vessel names
(簋 觚 罍 甗 匜 卣 觥) and the model invented roughly 7 of 16 glyphs — plausible-looking but
wrong, which this audience of all audiences would catch. Common characters (案 几 榻 屏 橱 柜)
rendered perfectly in the same run. Second pass swapped every archaic glyph for a
still-correct but commonly-used character and all 16 came back clean.

Rule: **if a character is rare enough that you would have to look it up, the model will invent
it.** Either choose a commoner synonym or composite the label in afterwards with PIL.

Also: asking for 「{title}」 put literal corner brackets in the rendered title. Say
"no quotation marks or brackets" explicitly.

**Watermarked** with `curify-frontend/scripts/lib/watermark.cjs` -> `applyTiledWatermark`
(tiled Curify logo, slanted -30 degrees, 0.15 opacity). Clean unwatermarked masters are
recoverable from git commit a37a93a if a version without the mark is ever needed.

Images are 928x1152 (4:5 portrait) — works for Facebook and is close enough to Pinterest's
2:3 to be usable there too.
