# 小红书 · Curify — 2026 诺贝尔物理学奖 · 中微子 / 冰立方 4 图 · 2026-10-06

**「反常识科普」第 2 期。** 系列规则、发布进度和读数都在 [`README.md`](README.md)，这里不重复。

**素材来源：** 新智元《刚刚，诺贝尔物理奖爆冷！82岁狂人一人独揽，凿穿南极冰川》（2026-10-06，
https://mp.weixin.qq.com/s/7h8-McqGIAUxqN1CmcMGgg ，引 nobelprize.org 2026 物理奖新闻稿）。
全文存档在 `curify-frontend/raw/诺奖中微子-smm-10-06/source_xinzhiyuan.txt`。

**和原文唯一的出入：** 原文写「此刻有约 650 亿个中微子穿过你的指甲盖」，没写时间单位。
标准数值是**每平方厘米每秒**约 6.5×10¹⁰ 个太阳中微子，所以卡片和正文都写「**每秒**」。

**生成方式：** 4 张图全部用站上已上线的 nano 模板生成，脚本
`curify-frontend/scripts/oneoff_nobel_neutrino_smm_2026-10-06.cjs`（gemini-3-pro-image-preview，3:4，2K）。
干净母版在 `raw/诺奖中微子-smm-10-06/out/`，本目录是**加水印版**。

| # | 图 | 模板 | 参数 |
|---|---|---|---|
| 1 | `01_ghost_through_fingernail.png` | [weird-cold-knowledge-popular-science-card](https://www.curify-ai.com/nano-template/weird-cold-knowledge-popular-science-card) | `science_topic = 每秒有 650 亿个中微子穿过你的指甲盖` |
| 2 | `02_icecube_structure.png` | [bilingual-object-structure-labeling](https://www.curify-ai.com/nano-template/bilingual-object-structure-labeling) | `object_name = IceCube Neutrino Observatory 冰立方中微子天文台` |
| 3 | `03_crazy_idea_to_nobel.png` | [history-timeline-infographic](https://www.curify-ai.com/nano-template/history-timeline-infographic) | `timeline_topic = 从疯狂构想到诺贝尔奖：冰立方 38 年` |
| 4 | `04_how_to_catch_a_ghost.png` | [science-education-infographic](https://www.curify-ai.com/nano-template/science-education-infographic) | `topic = 一个中微子是怎么被「抓」到的` |

**没有任何一张画哈尔岑本人。** 他是在世的真人，生成肖像既不准也不该；卡片讲的是粒子和探测器，反常识也在那里。

---

## 反常识内核（过不过系列门槛）

> **世界上最大的"望远镜"不朝天看——它埋在南极冰下两公里，看的是脚底下。**

辅助两条：
- 每秒 650 亿个中微子穿过你的指甲盖，你一个都感觉不到。
- 哈尔岑自己说：要不是当时对天然冰的光学性质**一无所知**，他大概也会放弃。——**他能成，是因为他不懂。**

过线。和隐翅虫那期一样：**正文文字优先，4 张图是落点。**

---

## CTA：批量生成视觉内容

这一期比第 1 期多一个任务：**把"热点 → 一套图"这件事本身当成案例**，导向批量生成。

规则沿用 [`../2026-09-01-ecommerce/posts_rednote_kuaishou.md`](../2026-09-01-ecommerce/posts_rednote_kuaishou.md)：
**小红书正文不放外链、不放微信/电话，CTA 只走私信 + 评论区。** RedNote · Curify 禁硬广，
所以正文里 CTA 只占最后两行，用"这几张图怎么来的"自然带出来，不用 #Curify。

- **正文结尾（软）**：说明 4 张图是同一套模板流程、当天出的；有需要的私信「批量」。
- **置顶评论（硬一点）**：4 个模板名 + "热点当天出一整套图"。模板链接只在评论区、且只在有人问的时候回。
- **私信话术**：见文末。落地给 `curify-ai.com/nano-template/...`（自助）和 `curify-ai.com/contact`（批量）。

---

## Post 1（主贴）— 最大的望远镜，不朝天看

**发布：** 10-07（诺奖热度窗口只有 2–3 天，这条今天发）
**封面：** `01_ghost_through_fingernail.png`
**配图顺序：** 01 → 02 → 04 → 03

**【标题】** 世界上最大的望远镜，埋在南极冰下两公里

**【正文】**

> **世界上最大的"望远镜"不朝天看，它埋在南极冰下两公里。**
>
> 今年的诺贝尔物理学奖，82 岁的哈尔岑一个人拿了。上一次物理奖只给一个人，还是 1992 年。
>
> 他抓的东西叫**中微子**。
> 不带电、质量几乎为零、几乎不和任何东西发生作用——
> **此刻每秒约有 650 亿个，正穿过你的指甲盖，你一个都感觉不到。**
>
> 为什么非抓它不可？
> 光会被尘埃挡住，宇宙射线会被磁场带偏，只有中微子走绝对直线。
> 黑洞旁边发生了什么，它能原封不动地带到地球。
>
> 问题是它太难抓：绝大多数直接穿过整个地球。
> 想等到几个"撞上"的，探测器就得大得离谱。
>
> 1988 年他提了个听起来像疯了的方案：**别去海里，直接用南极的冰。**
> 冰下够黑、够纯，没有会发光的水母，传感器冻进去就永远不动。
>
> 于是有了冰立方：
> 用热水钻融出 86 口两公里多深的井，挂进 5160 个光学传感器，
> 在冰下 1450—2450 米圈出整整**一立方公里**的纯冰当探测器。
> 中微子偶尔撞上冰里的原子核，会闪出一道幽幽的蓝光，传感器拍到它，就能反推出它从宇宙哪个方向来。
>
> 最反直觉的是他自己的回忆：
> **"要不是我当时对天然冰的光学性质一无所知，我大概也会放弃。"**
> 他能成，恰恰是因为他不懂。
>
> 图 2 是冰立方的结构，图 3 是一个中微子被"抓"到的六步，图 4 是从构想到诺奖的 38 年。
>
> ——
> 这 4 张图是用同一套模板、新闻出来当天做完的。
> 做科普号、课程、品牌内容，想把每周热点批量做成一整套图的，私信「批量」。
>
> #诺贝尔物理学奖 #中微子 #冰立方 #南极 #物理 #科普 #冷知识 #反常识

**【EN gloss】**
> The world's biggest "telescope" doesn't look up — it's buried two kilometres under the South Pole. Halzen won the 2026 physics Nobel alone for IceCube: 86 holes, 5,160 sensors, a cubic kilometre of ice watching for the blue flash of a neutrino hitting a nucleus. ~65 billion neutrinos pass through your fingernail every second. His own line: had he known anything about the optics of natural ice, he'd probably have given up. Soft CTA: these four cards were made the same day from one template set — DM "批量" to do the same for your weekly topics.

---

## Post 2（拆条，10-09）— 每秒 650 亿个穿过你

**封面：** `04_how_to_catch_a_ghost.png`

**【正文】**

> **每秒 650 亿个中微子穿过你的指甲盖，绝大多数连地球都直接穿过去了。**
>
> 那科学家是怎么"抓"到一个的？六步：
> 1️⃣ 黑洞附近的极端事件产生高能中微子，直线飞越数亿光年
> 2️⃣ 绝大多数直接穿过地球和探测器，什么也不碰
> 3️⃣ 极少数一头撞上南极冰里的原子核
> 4️⃣ 撞出的缪子在冰里跑得比**光在冰里**还快，发出蓝光——切伦科夫辐射
> 5️⃣ 冰下 5160 个传感器拍下这道光，传回冰面
> 6️⃣ 按蓝光的时间和位置，反推它从哪个方向来
>
> 注意第 4 步：不是比真空光速快，是比光在冰里的速度快。这个区别常被说错。
>
> ——
> 这类分步科普图可以批量出，一个主题一整套。需要的私信「批量」。
>
> #中微子 #诺贝尔奖 #物理科普 #冷知识 #切伦科夫辐射

---

## Post 3（拆条，10-11）— 从疯子构想到诺奖，38 年

**封面：** `03_crazy_idea_to_nobel.png`

**【正文】**

> **1988 年提出来的时候，所有人都觉得这是科幻小说。**
>
> 1993 浅冰里全是气泡，光传不出去；钻到 1400 米以下，冰突然变得透明。
> 2011 最后一根线缆放进冰里。
> 2013 第一次确认：有中微子从太阳系外飞来。
> 2017 一个中微子把全世界的望远镜引向一个耀变体。
> 2023 第一次用中微子"看见"银河系——靠的是机器学习。
> 2026 诺贝尔物理学奖，一人独得。
>
> 有意思的是：两年前诺奖颁给了机器学习的奠基人，今年这个奖里最亮的发现之一，就是机器学习挖出来的。
>
> ——
> 时间线、结构图、分步图，一个热点可以一次出一整套。私信「批量」。
>
> #诺贝尔奖 #冰立方 #科学史 #时间线 #科普

---

## 置顶评论（三条通用）

> 图是用这几个模板做的：冷知识科普卡 / 双语结构标注 / 历史时间线 / 科学分步图。
> 同一个热点当天出一整套，课程、科普号、品牌周更都能批量跑。要模板或想批量做，私信我。

## 私信回复话术（收到「批量」时）

> 你好～这套是我们的模板批量生成的：给一个主题 + 参考资料，一次出封面、结构图、时间线、分步图一整套，
> 文字会逐字校对。
> 想先自己试：curify-ai.com 搜「nano template」，选模板填主题就能出。
> 想按周批量做（比如每周 3 个热点 × 4 张）：说一下你的账号方向和每周量，我按你的选题先免费跑一套样图。

---

## 已知瑕疵（发之前看一眼）

- 图 2「光学传感器」标了两次（两条引线都指向传感器，不算错，只是重复）；计数用的是英文 "(86 total)"/"(5160 total)"。
- 图 1 右上角中微子图标写成 ν₂（中微子的一种质量本征态），不影响阅读。
- 图 3 诺奖奖章上的拉丁字是模型装饰，非真实奖章文字。
- **CJK 校对：** 最终 4 张是 2K 重生成后逐块放大人工核过的（为什么只跑脚本不够，见 README house rule 3）。
  1K 的废稿留在 `out/*.v1-backup.png`、`*.v2-1k.png` 以备对照。
