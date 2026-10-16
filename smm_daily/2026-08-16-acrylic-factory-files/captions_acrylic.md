# SMM · Curify — 亚克力工厂文件 / Acrylic factory files · 2026-08-16

Same shape as the layer-separation post: a **demand probe**, not a launch. The
exporter works and produces a real production package, but it is not self-serve,
so the CTA is to send us artwork.

**CTA:** https://www.curify-ai.com/contact — *send the artwork, tell us the size.*

| asset | note |
|---|---|
| `acrylic_plates_en.jpg` / `_zh.jpg` | 4 plates: front · back (mirrored) · white ink · cutline + hole |

> The white plate is deliberately shown **on a dark board**. It is white ink under
> clear acrylic — on a white background it is invisible, which is exactly why
> customers do not know they are missing it.

⚠️ **IP note (same rule as the layer post):** the demo artwork is Cinnamoroll —
Sanrio. Fine to process as a client job, **not** for a public Curify feed. For a
public post, re-run the exporter on artwork we own; the plates look identical and
the IP question disappears. Copy below is written to be artwork-agnostic.

---

## EN · Facebook

> "Send us print-ready files."
>
> For an acrylic keychain that sentence means five things, and most people send
> one of them.
>
> Acrylic is clear. Print colour straight onto it and you get a washed-out tint —
> so the factory lays down an opaque **white plate** underneath first. That plate
> is a separate file. It also has to be pulled *inward* about 0.25mm, because the
> white and colour passes never line up perfectly and un-choked white shows as a
> pale halo around every edge.
>
> Then there's the hole. Too close to the edge and the keychain tears out of its
> own hole on the first day.
>
> We built the export step: artwork in, and out comes the front, the mirrored
> back, the white plate, the cutline with the hole, and a spec sheet — as a zip a
> factory can quote from. The hole position is *computed* against the cut path and
> refuses to place one that would crack the part.
>
> Not self-serve yet. **Send us the artwork and the size you want.** What comes
> back decides what we build next.
>
> 🔗 (first comment)

### EN · short

> Acrylic is clear, so colour needs an opaque white plate under it — choked 0.25mm
> or it halos. Most "print-ready" files arrive without one.
>
> Artwork in → front, mirrored back, white plate, cutline + hole, spec. One zip a
> factory can quote from. Hole position computed, not eyeballed.
>
> Send us artwork + size 👇

---

## 中文 · 小红书

> **「发个印刷文件过来」——亚克力钥匙扣这句话背后是 5 个文件，大多数人只发了 1 个。**
>
> 亚克力是透明的。颜色直接印上去会发灰发虚，所以工厂要先打一层**不透明白墨**打底。
> 这层是**单独的文件**。而且必须往里**缩 0.25mm**——白墨和彩色两道套印不可能完全对齐，
> 不缩的话边缘会露出一圈白边。
>
> 还有孔位。离边太近，钥匙扣第一天就会从自己的孔那里裂开。
>
> 我们把导出这一步做了：一张图进去，出来**正面图、背面镜像图、白墨层、带孔位的刀线、
> 规格表**，打包成工厂能直接报价的 zip。孔位是**按刀线算出来的**——放不下就直接告诉你，
> 而不是给你一个会开裂的件。
>
> 还没做成自助工具。**把图和你要的尺寸发我们**，收到什么就先做什么。
>
> 📩 主页链接 / 私信

**Tags:** #亚克力 #谷子 #吧唧 #周边设计 #印前 #白墨 #工厂文件 #设计效率

### 中文 · 短版

> 亚克力透明，彩色下面必须垫一层白墨，还得往里缩 0.25mm，不然边缘露白。
> 一张图 → 正面/背面镜像/白墨层/刀线+孔位/规格表，工厂能直接报价。
> 孔位按刀线算，放不下就说放不下。**把图和尺寸发我们。**

---

## Claims ledger

- ✅ **white plate is choked inward** — verified numerically: 0 px of white outside
  the artwork, 9,497 px choked band, plate is pure 255 white.
- ✅ **back is mirrored** — differs from front, identical area.
- ✅ **hole refuses when illegal** — a 6mm bar rejects a 4mm hole needing 2mm walls.
- ⚠️ **0.25mm choke and 2mm wall are industry-typical values we chose**, not numbers
  confirmed with a specific factory. Say "typical", not "your factory's spec",
  until a supplier confirms.
- ⚠️ **No physical sample has been produced from these files.** They are
  structurally correct; nobody has cut one yet. Do not claim a finished piece.
