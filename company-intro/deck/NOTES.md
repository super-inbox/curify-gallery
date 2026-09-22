# Curify AI · 公司介绍（客户版）

**产出**：`Curify_AI_公司介绍_客户版.pdf` · A4 · 9 页 · 中文 · 全页斜向水印

上级目录那两份（`Curify_AI_公司简介与产品介绍_ZH.pdf` / `…(EN).pdf`）是**投资人/合作方版**：
4 页纯文字，讲的是「工业级多模态 AI 内容引擎」「三条生产流水线」「从概率型 AI 到生产级系统」，
一张图都没有。**那两份不要发客户**——客户不关心我们有几条流水线，只关心拿到手的是什么文件。

这一份是客户版，2026-08-28 重写，三条改动原则：

1. **按交付物写，不按技术能力写。** 第 3 页那张表的表头是「你手上多出哪些文件」，
   每一行都在后面案例里有实物对应。
2. **把设计摆到和 AI 同等位置。** 第 2 页三张卡是 设计 / AI 生产系统 / 落地，
   设计那张明写**设计师出身美术学院**（按用户要求不点校名），并解释为什么这三样必须在一家
   （纯 AI 团队出的东西「AI 味重」，纯设计团队接不了三十款的量）。
3. **每个案例讲一个客户会踩的坑**，不只是展示成品。

### 2026-08-28 的几处修订

- **删掉了黎族景区文创那页**——项目还是 WIP，用户决定先不放。
  素材没删，还在 `../../lizu-merch-08-22/proposal/assets/`，项目做完可以加回来
  （加回来记得同步改案例编号、第 3 页表格的「景区 / 城市文创」那行、封面与作品速览的缩略图）。
- **不点名美术学院**：只写「设计师出身美术学院」。
- **第 3 页那段关于数字的话重写了**——原来那版在跟读者论证「生成模型会瞎编数字」，
  现在只讲我们自己做什么（数字由代码写、能查出处、页脚注明非模具图纸）。
- **换装截帧重取**：原来那两帧取在 5.5s，正卡在粒子转场上，糊。
  改取 8s（清 / 明两套），并把第 7 页图注从「唐」改成「清」。
  注意用锐度指标（拉普拉斯方差）自动选帧在这里会**选错**——转场的颗粒噪声让方差最高。

## 五个案例的来源

| 案例 | 素材来源 |
|---|---|
| 一 · 城市文创插画（Q版上海） | `curify-frontend/raw/cute-city-08-25/`，见 `curify-frontend/docs/city-illustration-cute.md` |
| 二 · IP 衍生品与 3D | `../../吊坠-3d-model/portfolio/assets/`（与吊坠作品集共用） |
| 三 · 电商视觉 + 换装 | `nano_insp/template-fashion-ecommerce-*` + `curify-gallery/costume_tryon/` 截帧 |
| 四 · 影像与视频 | `curify-gallery/cultural_videos/`、`brand_brief/`、`ecommerce_workflow/` 截帧（各取 35–45% 时长处） |
| 五 · 教育内容 | `daily_inspirations/Jul_8/` 的 HSK 分级课文与合体字识字卡 |

**城市插画那页的重点不是成品，是 v1→v4 的迭代对照。**
四轮各换一个变量，结论反直觉：问题不在细节多少，在**线条实不实**。
v1 满细节→AI 味重、v2 极简→变冷、v3 加萌→线还是飘、v4 暖色铅笔+实线条才立住。
另一条约束来自物理：成品磁贴只有 5cm，所以画法是被产品尺寸倒逼的。
这套推理过程比六张成品图更能说明「我们知道自己在干什么」，别为了省版面删掉。

## 怎么改

```bash
vi intro_src.html          # 不要改 intro_built.html
python3 build.py           # 重建 HTML + PDF
python3 build.py --html    # 只出 HTML（调版式快）
```

## 斜向水印

用的是 house 配方，不是另起一套：`make_watermark_tile.cjs` 从
`curify-frontend/scripts/lib/watermark.cjs` **import** `DEFAULT_LOGO_PATH` 和 `TILE_DEFAULTS`
（logo 0.22 页宽 / 旋转 -30° / 间距 1.8 倍），生成一张 tile，`style.css` 用
`.page::after` 平铺。所以这份 deck 和所有其他打过水印的 Curify 素材是同一个标记。

唯一的偏离是**透明度**：helper 的 0.15 是给照片调的，压在 A4 白底上会跟正文抢；
deck 降到 light 0.08 / dark 0.11，script 里有注释说明。改水印跑：

```bash
node make_watermark_tile.cjs   # 重出 tile → assets/wm_tile*.png + wm_tile.json
python3 build.py               # 重新内联进 CSS
```

（那个 helper 的 `applyTiledWatermark()` 是把水印合成**到一张图上**，
deck 的页面不是图，所以这里复用的是它构造 tile 的那两步，而不是直接调它。）

`style.css` 是从 `吊坠-3d-model/portfolio/` 拷来的**副本**，不是共享文件 ——
改这里不会影响吊坠那两份，反过来也一样。版面填充机制（`spread` / `fill`）和
PDF 打印走 Playwright 的原因，都见那边的 NOTES。

## 待确认 / 弱点

- **第 2 页那四个数字**（6 个交付品类 / 10 个语种 / ≥98% 一致性 / 同日出方案）
  是我按已跑通的案例数和上级 ZH 版里的口径填的，**发客户前请自己核一遍**，
  尤其「10 个语种」和「≥98%」这两个偏承诺性质。
- **案例一（城市插画）是探索项目**，`docs/city-illustration-cute.md` 写明
  **exploratory — no client order yet**。文案没暗示它是付费单，但客户追问「做给谁的」要照实说是自研样例。
  删掉黎族那页之后，这是打头的案例，被问到的概率更高了。
- 联系方式取自上级 ZH 版：`team@curify-ai.com` / 微信 `17692190183`。
