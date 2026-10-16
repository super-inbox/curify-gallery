# 小红书 · Curify — 刀版图 → 3D 包装效果图 · 2026-08-07

**案例：** `3D-mockup/fortune-box/` — 仁寿字绘包装盒（117 × 114 × 39 mm，四川仁寿文旅礼盒）
**主题：** 干货 + 前后对比。核心信息 = *刀版图客户看不懂，3D 效果图才是能确认的东西；而 AI 做这件事最大的坑是比例。*
**与贴纸系列的关系：** 贴纸那组讲 **设计 → 出厂文件**（往工厂走）；这组讲 **出厂文件 → 效果图**（往客户走）。两头都通，才是完整的 design-to-manufacture。

**配图：**
| 文件 | 用途 |
|---|---|
| `仁寿盒-刀版转3D.jpg` / `renshou-dieline-to-3d-EN.jpg` | P1 封面（前后对比） |
| `包装3D-比例坑.jpg` / `packaging-3d-proportion-trap-EN.jpg` | P2 封面（① / ✕ / ✓ 干货图） |
| `../仁寿盒-45度效果图.jpg` | 轮播补充（真实交付图） |

> ⚠️ 注意：`../仁寿盒-正面效果图.jpg` **不要用于对外发布**——正面那版的汉字被模型写错了
> （华严寺→"华户寺"、报恩寺→"招串寺"、仁寿大佛→"仁房大佛"），小红书的设计受众一眼就能看出来。
> 只用 45° 那张。参考 memory `feedback_chinese_caption_gemini_model`（中文需 gemini-3-pro-image）。

---

## Post P1 — 刀版图客户看不懂，3D 图才看得懂
**封面图：** `仁寿盒-刀版转3D.jpg`

**【中文】**
> **客户看不懂刀版图，看得懂这张 📦**
>
> 做包装的都懂：刀版展开图发过去，客户回一句"这是啥"。
> 但同一个文件，折成 3D 效果图，确认、汇报、上电商页——一次就过。
>
> 这单是仁寿的文旅礼盒。我们做的事很简单：
> 从 .ai 刀版里**读出真实尺寸 117 × 114 × 39mm**，加上折叠关系、350g 卡纸的材质感，
> 直接出 45° / 正面 / 白底电商图。
>
> 尺寸、折法、材质，全部从文件里读，不靠猜——所以出来的盒子，和打样出来是同一个盒子。
>
> 💬 包装 / 文创设计**可定制接单**——私信或评论，我们免费给你出一版 + 报价。
>
> #包装设计 #刀版图 #包装盒 #3D效果图 #文创设计 #印刷 #设计干货 #AI设计

**【EN】**
> **Your client can't read a dieline. They can read this 📦**
>
> Every packaging designer knows it: you send the flat dieline, the client replies "…what am I looking at?"
> Same file, folded into a 3D mockup — sign-off, internal review, product page, done in one pass.
>
> This one is a cultural-tourism gift box for Renshou, Sichuan. What we actually do is simple:
> **read the true size — 117 × 114 × 39 mm — out of the .ai dieline**, add the fold logic and the 350gsm board feel,
> then render 45° / front / white-background e-commerce shots.
>
> Size, folds, material — read from the file, never guessed. So the box on screen is the box you get from the sample run.
>
> 💬 We take **custom packaging & cultural-merch commissions** — DM for a free first pass + quote.
>
> #packagingdesign #dieline #3dmockup #packagingmockup #printdesign #AIdesign #productpackaging

---

## Post P2 — AI 做包装 3D 图，最大的坑是比例
**封面图：** `包装3D-比例坑.jpg`

**【中文】**
> **AI 做包装 3D 图，90% 的人栽在这一步 ⚠️**
>
> 不是渲染不好看，是**比例不对**。
>
> 你只丢一句"帮我把这个包装做成 3D 效果图"，模型默认给你画个**方盒子**。
> 可这单的真实尺寸是 **117 × 114 × 39mm**——它是个**扁盒**。
> 方盒和扁盒，客户一眼看得出来，工厂更是一眼看得出来。
>
> 诀窍就一条：**长宽高必须从刀版文件里读出来，别让模型自己猜。**
> 刀版里本来就写着尺寸——问题从来不是模型不会渲染，是没人把尺寸喂给它。
>
> （同理还有：折叠关系、纸张厚度、开窗位置，能从文件里读的都别猜。）
>
> 💬 包装 / 文创设计**可定制接单**——私信或评论，我们免费给你出一版 + 报价。
>
> #包装设计 #AI设计 #设计干货 #3D效果图 #刀版图 #包装盒 #避坑指南 #印刷
>
> **评论区钩子：** 你被 AI 画歪过哪种包装？扁盒、异形盒、还是开窗盒？

**【EN】**
> **The #1 trap when you let AI render packaging ⚠️**
>
> It's not the lighting. It's the **proportions**.
>
> Prompt it with "turn this packaging into a 3D mockup" and the model hands you a **cube**.
> But this box is **117 × 114 × 39 mm** — it's a **flat box**.
> A cube vs a flat box: the client spots it instantly, and the factory spots it faster.
>
> One rule: **read W×H×D out of the dieline file — never let the model guess.**
> The dimensions were in the file the whole time. The model can render fine; nobody fed it the numbers.
>
> (Same goes for fold logic, board thickness, window positions — if it's in the file, don't guess it.)
>
> 💬 We take **custom packaging & cultural-merch commissions** — DM for a free first pass + quote.
>
> #packagingdesign #AIdesign #dieline #3dmockup #designtips #printdesign #packagingmockup
>
> **Comment hook:** which package shape has AI botched for you — flat boxes, odd shapes, or window boxes?

---

## 复现
`make_xhs_cards.py`（同目录）生成全部 4 张图，1080×1080，2x 超采样后下采样。
沿用贴纸组的视觉规范：`#F5F5FA` 背景 · 白卡片 · ✕ 红 / ✓ 绿 · 紫色箭头 · 底部一行结论。
