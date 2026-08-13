# SMM · Curify — 图片转分层文件 / Image → Layered PSD · 2026-08-13

Demand-probe post, not a launch. The tool works and a designer has reviewed the
output (*"分层效果看着效果还可以，5层结构基本覆盖了常见修改需求"*), but it is **not
self-serve yet** — so the whole point of this post is the CTA: get people to send
us the artwork they actually need split, so we learn which inputs matter before
building the product surface.

**CTA (all posts):** https://www.curify-ai.com/contact — *send us your file, tell
us what you need to edit.*

| Post | Hero image | Case |
|---|---|---|
| P1 EN | `layers_mbti_en.jpg` | WWII-MBTI China poster (illustration, residue 23.6%) |
| P1 中文 | `layers_mbti_zh.jpg` | 同上 |
| P2 EN | `layers_product_en.jpg` | CHICPUPPY packaging insert (line art, **residue 1.2%**) |
| P2 中文 | `layers_product_zh.jpg` | 同上 |

> **Post P2 as the second image in the same post, not a separate one.** The
> packaging insert is by far the stronger proof (98.8% of the artwork explained by
> LineArt + FlatColor alone) and it is the input class we actually want more of.

> **FB rules (see [[project_fb_follower_growth]]):** upload natively, **no
> carousels**, and **keep the link out of the post body** — put it in the **first
> comment**, or reach gets throttled.

⚠️ **Platform note on the MBTI hero.** It is WWII-themed (fighter planes, rifles,
持久抗战 badge) on a Chinese national subject. On 小红书 specifically, war-history
content mixed with pop-psychology typing can draw the wrong kind of attention or
get limited. **Recommendation: lead the 小红书 post with `layers_product_zh.jpg`**
(the packaging insert) and keep the MBTI image for the EN/Facebook post, where it
reads as an illustration sample. Copy below is written so either can lead.

---

## P1 — EN · Facebook

**Hero:** `layers_mbti_en.jpg` · second image `layers_product_en.jpg`

> A flat JPG is where edits go to die.
>
> Client asks for a colour change. Or the text in another language. Or the same
> line art on a different SKU. You have one flattened image, so you redraw it.
>
> We've been testing something that splits a finished image back into editable
> layers — line art, flat colour, shadow, highlight, and a residue layer that
> catches whatever the other four didn't explain. Five layers, a real PSD, opens
> layer by layer.
>
> The second image is a packaging insert we ran through it: **98.8% of that
> artwork came back as just line art + flat colour.** All the linework and every
> character of the copy landed on their own layer, transparent, ready to edit —
> the background is clean underneath.
>
> It works best on flat illustration and line-art work: packaging inserts,
> instruction cards, stickers, character art. Painterly or photographic images
> split less cleanly, and we'd rather say that than pretend otherwise.
>
> It isn't a self-serve tool yet — which is exactly why we're posting. **Send us
> the file you keep having to redraw and tell us what you need to change.** The
> inputs we get back decide what we build.
>
> 🔗 (first comment)

### P1 — EN · short (IG / Threads / X)

> A flat JPG is where edits go to die.
>
> We split finished artwork back into 5 editable layers — line art, flat colour,
> shadow, highlight, residue. Real PSD, opens layer by layer.
>
> On this packaging insert, **98.8% came back as line art + flat colour** — every
> character of the copy on its own transparent layer.
>
> Not self-serve yet. Send us the file you keep redrawing 👇

---

## P2 — 中文 · 小红书

**首图建议：** `layers_product_zh.jpg`（包装插卡，分层最干净）· 第二张 `layers_mbti_zh.jpg`

> **一张平面图，改一个字就要重画整张？**
>
> 客户说颜色换一下、文案换个语言、同一套线稿换个 SKU——手里只有一张压平的图，
> 只能重画。
>
> 我们在测一个东西：把已经做完的图**还原成可编辑图层**。线稿、色块、阴影、高光，
> 再加一层"余量"兜住前四层没解释掉的部分。**5 层，真 PSD，能一层一层改。**
>
> 图里这张包装插卡跑下来：**98.8% 的画面只靠线稿 + 色块就还原了**。所有线条、
> 每一个中文字都单独落在透明图层上，底下的背景是干净的。
>
> 说实话一点：**它最吃平面插画和线稿类**——包装插卡、说明卡、贴纸、角色稿。
> 厚涂和实拍类分得没这么干净，这个我们不藏着。
>
> 现在还没做成能自己上传的工具，所以才发这条：
> **把你反复重画的那张图发给我们，告诉我们你需要改哪里。** 收到什么，就先做什么。
>
> 📩 主页链接 / 私信都可以

**Tags:** #包装设计 #平面设计 #设计效率 #AI设计 #印前 #电商设计 #源文件 #设计素材

### P2 — 中文 · 更短版（评论区 / 微信）

> 平面图 → 5 个可编辑图层（线稿/色块/阴影/高光/余量），真 PSD。
> 包装插卡实测：98.8% 只用线稿+色块就还原了，中文字单独成层。
> 平面插画、线稿类最合适。还没做成自助工具——**把你要改的图发我们**，我们按需求排。

---

## What we are claiming, and what we are not

Kept explicit so nobody has to walk a claim back later:

- ✅ **"5 editable layers, real PSD"** — verified by reading the file back with an
  independent reader: 5 named layers, real per-pixel alpha, byte-exact against the
  exported PNGs, and hiding a layer changes the render.
- ✅ **"98.8% line art + flat colour"** — `product.jpg`, residue 0.012, recon
  MAE 0.0044.
- ⚠️ **Raster layers, not vector.** Strokes can be painted over, not re-weighted.
  Do not answer "yes" if someone asks for editable vector paths.
- ⚠️ **The residue layer overrides recolours beneath it** (it holds original
  pixels). If a customer trials this, tell them to hide Residue while recolouring.
- ⚠️ **Not opened in Adobe Photoshop by us** — spec-valid and correct on read-back.
  If a designer reports a problem opening it, that is new information, not a
  known-and-hidden issue.

## Assets

Generated by `curify-studio/dev/jayw/image-to-layered-psd/`:

```bash
python3 layered_export.py <image> -o case_x --colors 24 --verify
python3 make_showcase.py case_x <image> out.jpg --lang en|zh
```

Sources: `curify-frontend/raw/layer-separation-08-13/{product,template-mbti-generic-en-China}.jpg`
