# Data Science × AI — 系列编辑说明

更新：2026-10-28。原目录 `2026-09-05-founder-vision-linkedin` 更名为 `2026-09-05-data-science-ai-series`，日期保留历史起点。各平台的发布顺序与完整文案已合并：

- [小红书：Publication Sequence＋文案](posts_rednote.md)
- [Facebook：Publication Sequence＋文案](posts_fb.md)

各平台表格独立回填状态，不再维护单独的 Publication Sequence 文件。原文完整保留在 [Founder Vision 历史稿](post_founder_vision_archive.md)，视频和制作脚本随目录一起保留。

## 定位与两个 ICP

| 路线 | 受众与当前问题 | 内容承诺 | 转化方向 |
|---|---|---|---|
| A · 看懂并做出第一个项目 | 想转入 Data Science / AI 的学习者、数据分析师或工程师；工具很多，不知道先学什么 | 用生活例子解释概念，再给一个可实践的小任务 | 学习路线、作品集项目与职业转型 mentoring |
| B · 把 AI 做成可靠的产品 | 已在做 AI 的创始人、技术负责人、小团队；面对选型、延迟、成本和差异化 | 用业务问题引出技术取舍，让读者看出判断依据 | AI 架构、检索、评估、推理部署与产品技术路线 consulting |

账号：小红书采用用户提供的「摇曳的光明」（Jay）知识／思考型个人表达，Facebook 面向 Jay 的专业受众。本系列不混入 Curify 历史文化号。基础技术解释是 Jay 原有宏观思考方向的有意扩展；以项目与决策作主线，观察是否吸引目标受众，不用品牌硬广开头。

语言：小红书中文，Facebook 英文。2026-10-28 根据操作者逐题反馈重写：浅显指解释术语、展示过程，不意味着省略技术。各题采用不同写法，不再统一改成场景比喻和产品选型建议。必要时保留公式、步骤和对比；先说明符号和术语，不假设读者已经熟悉推理基础设施。

| 编号 | 主视角 | 本文需要交付的内容 | CTA／交流方向 |
|---|---|---|---|
| S01 | 技术总览＋学习路线 | 九层职责、代表工具、每层试一两个；端到端制度助手及按需选型 | 转行 AI、补齐实践链路 |
| S02 | 统计与 AI 交叉科普 | 传统统计方法、预训练迁移、Timestral 图的上下两阶段、协变量和预测区间 | 统计／数据分析转向 AI 项目 |
| S03 | 技术教学＋hands-on | BM25＋embedding，RRF 公式、A/B/C/D 算例与小数据练习 | 检索项目 mentoring |
| S04 | 工程场景延展 | 保留已写的 grep／aliases 与数据类型适配 | 检索设计交流／咨询 |
| S05 | 从使用体验出发的机制科普 | 长文追问 → prefill/decode → KV；区分跨请求前缀复用；解释修改输入后的重算 | AI 工程基础学习 |
| S06 | 专家讲解＋架构对比 | Ollama、vLLM、SGLang 的优化点、适用条件与具体应用；不把能力写成互斥 | 转行 AI Engineering，尤其推理基础设施 |
| S07 | 行业竞争／争议讨论 | 发布节奏、相互追赶、Meta Muse 与 Kimi K3；谁领先／掉队，以及判断维度 | 讨论观点，轻量专业交流 |
| S08 | 创业观点 | 用户已认可，保留原文 | 原 CTA 保留 |

S08 小红书已发布，由操作者在本轮确认；具体日期与帖子链接尚未提供。Facebook 状态不随之改为已发布。

CTA：小红书只用私信或“在 MentorCruise 搜 Jay Wang”，正文不放网址；Facebook 可直接附 [Jay Wang 的 MentorCruise 主页](https://mentorcruise.com/mentor/jaywang/)。A 邀请讨论背景、目标和项目；B 按选题邀请描述业务、负载、瓶颈或参与行业讨论；S05/S06 已明确转向工程学习 CTA。不承诺拿 offer、固定收益或未经测试的提速。

已参考该账号的实际可见笔记与互动，详见 [账号措辞观察](audience_notes.md)。取样用于措辞方向，不当作全账号排名或因果结论。

## 素材使用与编辑备注

七份 Assets 均已纳入八篇顺序；Hybrid Retrieval 拆为入门与代码检索延展两篇。素材保留原文件名，包括 `time-series-forecsting.gif` 的原拼写。素材是选题依据，不等于正文必须照搬其中的数字或结论。按本轮角度使用配图讲解：S01 总览、S02 上下两阶段、S03 手算 RRF、S05 prefill/decode、S06 工具对比。小红书可用长文转图文卡，Facebook 用英文说明搭配适当素材；原图的简化在正文中解释，不把原图视为完整规格。以下备注仅供编辑，不复制进帖子。

| 编号 | 素材与口径处理 |
|---|---|
| S01 | 图中的版本号与“80 tools”不是课程清单；正文不复述未逐项核验的产品版本。用图作九层总览，文案补职责、代表工具和端到端练习；不要求项目把九层全部装齐。 |
| S02 | GIF 为 Timestral 示意，保留 TheAiEdge.io 来源标识；不把动态图的示例曲线写成实测效果。发布正文可独立使用，不依赖 GIF 自动播放。 |
| S03 | 图中的 60 是 RRF 的示例参数，不是所有实现必须取的值；检索改善不保证回答正确。正文直接计算图中 A、C、B、D 的融合分数，并附 20 文档／10 问题练习。 |
| S04 | 由用户提出的 grep / aliases 场景延展；不宣称所有 Coding Agent 都只用 grep，也不把 agentic search 等同于 BM25。混合检索的通用设计与具体 BM25＋向量＋RRF 实现分开讲。 |
| S05 | 原图署名 @Dev.EmbodiedAI，作为参考保留署名；“O(T)”需限定为单步注意力计算的上下文长度依赖，不能说整个生成过程线性。正文沿现有图的 prefill/decode 框架展开，另外区分前缀缓存与输入修改；不声称缓存命中是某个聊天产品的固定行为。当前目录未发现独立命名的 V2 图片，未新造或替换图片。 |
| S06 | 原图对三者做了简化：Ollama 支持并发；vLLM 也支持前缀缓存和结构化输出。正文具体解释分页缓存、连续批处理、RadixAttention，再给典型场景和重叠能力；vLLM 支持多模态不等于仅用于多模态。 |
| S07 | Frontier List 原页说明是对 70 人的主观调查，不是统一 benchmark；不要将“落后一代”写成客观测量。可作为争议讨论图；按“该调查如何分组”描述具体公司，区别作者观点与客观测量，不宣布某家公司已经永久出局。 |
| S08 | 原图的 $2T、$948B、Q2 收入及 35 家样本口径未核验，不作为发布事实。此篇按文字观点稿发布；保留图片作选题参考，不随帖上传该数字图。 |

## 资料核对（2026-10-28；内部参考，不放入小红书 CTA）

- S01：采用功能层次讲解，不对图中每一项工具和版本背书；这是本系列的教学组织方式。
- S02：[Mistral Timestral 官方说明](https://mistral.ai/news/timestral/)支持预训练、协变量与概率预测的描述；[Forecasting: Principles and Practice](https://otexts.com/fpp3/toolbox.html)用于基线和时间顺序评估方法。动态图上的 TheAiEdge.io 为素材来源标识。
- S03：[Elastic RRF 文档](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)说明按排名融合不同检索列表。不要把示意图里的 k=60 当成普遍约束。
- S04：[Anthropic context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)说明 glob / grep 按需检索；[Claude Code 工具设计文章](https://claude.dev/blog/seeing-like-an-agent/)描述从预索引检索转向 Agent 自行找上下文的经验。aliases、退款词汇和数据类型对照是本文教学例子，不是对 Claude 内部实现的额外断言。
- S05：[Hugging Face KV cache 说明](https://huggingface.co/docs/transformers/cache_explanation)用于历史 K/V 复用与缓存增长；本文限定常见全注意力实现，不把单步复杂度当成全流程复杂度。
- S06：[Ollama FAQ](https://docs.ollama.com/faq)明确支持并发；[vLLM 文档](https://docs.vllm.ai/en/latest/)列出连续批处理、前缀缓存和结构化输出；[SGLang 文档](https://docs.sglang.io/)介绍服务框架与缓存。实际选型需固定版本和负载重新测试，不作赢家排名。
- S07：[Frontier List 原始页面](https://frontierlist.com/lab-tiers)将图表描述为受访者观点；新版按调查意见展示分组并引出追赶／掉队讨论，不作为统一 benchmark 或既定事实。
- S08：[Anthropic 2026-05-28 融资公告](https://www.anthropic.com/news/series-h)记录的是该轮 $965B post-money valuation，不能用于证明原图 $2T 或整套收入比较。本文不报实时估值或收入数字，明确以创业判断观点为主。


## 本轮补充核对

- S01 的代表工具是学习示例，不是图中所有产品／版本的认证清单。九层指这张生成式 AI 应用图，非穷尽所有 DS／ML 技术。
- S03 的计算：A=0.03252247，C=0.03226646，B=0.01612903，D=0.01587302。文案采用五位小数；正确性与召回表现仍由练习数据判断。
- S05：[vLLM 自动前缀缓存](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)与 [Hugging Face KV 缓存](https://huggingface.co/docs/transformers/cache_explanation)分别支撑跨请求复用和生成中复用。输入修改的说明限定常见自回归 Transformer，受分块与缓存保留影响。
- S06：[PagedAttention 原论文](https://arxiv.org/abs/2309.06180)、[SGLang 原论文](https://arxiv.org/abs/2312.07104)、[vLLM 多模态输入文档](https://docs.vllm.ai/en/latest/features/multimodal_inputs/)用于核对优化机制与多模态支持；Ollama 并发沿用官方 FAQ。这里的 SGLang 对应口述的“SD LAN”，vLLM 拼写统一。
- S07：[NVIDIA 与 Meta 2026-10-27 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Meta-to-Expand-Collaboration-on-Muse-and-Muse-Family-of-Models-Amid-Robust-Growth/default.aspx)核对 Muse 系列与训练／推理合作；[Moonshot 官方 Kimi K3 模型卡](https://huggingface.co/moonshotai/Kimi-K3)核对原生视觉、长上下文和代码方向。K3 并非本周新发布，文案不称其为本周首发；“按周观察”是作者的跟踪方式，不是保证每周名次必变。分组沿素材中的 Frontier List 调查，不将厂商自报能力直接换算成独立排名。

## 发布后回填

每个平台单独填写实际日期与帖子链接；预约与已发布分别记录。A 关注有背景和目标的学习／项目咨询，B 关注能描述业务和技术问题的咨询线索。记录收到的问题用于下一轮选题，不用虚构的阅读量或转化率判断效果。

## 历史 Founder Vision

[原 LinkedIn 文案与制作记录](post_founder_vision_archive.md)完整保留，仅供历史查阅；其中旧平台 CTA 和 Curify 产品表达不适用于本系列。原两个视频、ASS 字幕和三个 Python 制作脚本保持原名与内容。后续如需作为个人经历帖复用，另列新编号，不把历史素材当成已发布的系列新帖。
