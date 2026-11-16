# Reddit 需求选题研究｜DS × AI × Engineering｜2026-11-16

本轮交付：六个选题、六篇小红书中文稿、六篇 Facebook 英文稿。定位为 Jay 的求职／转行 coaching 与 AI startup 技术及产品 coaching；全部是草稿，未排期、未发布。编辑顺序不代表 Reddit 热度排名。

## 方法与证据边界

- 复用 `reddit-demand-mining` 技能；另查阅本地 `curify-studio/docs/skills/reddit-demand-mining.md` 中的 Arctic Shift 备用采集说明。按用户指定，将研究及文案放在本系列，而非技能默认的 Curify 产品营销目录。
- 两个人群：A 为 DS／DE／软件工程求职与转行者；B 为 AI startup 创始人和技术负责人。本轮不运行原技能的八类消费／商业素材用户检索。
- 2026-11-16，Reddit JSON 搜索返回 Blocked HTML，未取得可解析帖子；Arctic Shift 的有界查询返回 `data: null` 与 `Timeout. Maybe slow down a bit`，不计作成功采集，也不把空结果解释为没有需求。
- 改用网页搜索索引与 Reddit 原帖页面。七条搜索查询见下文；筛出下表 13 个独立需求样本。其中 R01、R04、R06、R08、R10、R11 进一步打开原帖阅读正文及可见评论；其余依据搜索工具返回的帖文／评论摘录。未展开全部评论、未做完整 subreddit 抓取。
- AI portfolio 在 r/AI_India 与 r/developersIndia 的同文跨贴合并为 R02，不算两份独立需求。其他低信息量帖子、重复 portfolio 展示及只推广工具的帖子不纳入这 13 条。
- 以 2026 年讨论为目标，搜索并非严格时间过滤。下表日期来自搜索索引；部分原帖页面的“几天前／几个月前”与索引不一致，日期未用 API 独立核实。因此不声称“本周趋势”，不按时间精确排名。采样日期确定为 2026-11-16。
- 帖子和评论都是自述，不验证其工作经历、商业结果或建议正确性。评论中的课程、工具或服务推广会降低证据权重。Reddit 英文社区的讨论也不能直接推算小红书受众偏好、付费意愿或整个市场规模。
- 不收集用户名、联系方式，不联系发帖人，不回帖，不将他们转换成外联名单。正式文案使用原创练习，不把匿名帖子改写成 Jay 的客户案例。

实际搜索查询：

1. `site:reddit.com/r/datascience 2026 portfolio interview projects AI`
2. `site:reddit.com/r/MachineLearning 2026 production evaluation LLM`
3. `site:reddit.com/r/startups 2026 AI pilot paying customers`
4. `site:reddit.com/r/datascience 2026 "AI engineer" transition`
5. `site:reddit.com/r/ExperiencedDevs 2026 "agents" "production"`
6. `site:reddit.com/r/LLMDevs 2026 "evaluation" "production"`
7. `site:reddit.com/r/datascience 2026 "A/B" "interview"`

搜索结果可能来自其他 subreddit；实际来源以下表为准。未使用“全网最热”“多数工程师”等比例或排名表述。

## 与既有专业内容的关系

通过浏览器只读查看用户提供的 [Lark SMM 表](https://xb8b3vzwjso.sg.larksuite.com/sheets/Qx3JsufexhNOJZtGoFglxa4Ig1b?sheet=bDMDxU) 的可见第 2–16 行，未修改表格，也未读取其他业务 tab。可见选题覆盖视觉 AI、Goodhart’s Law／Benchmaxxing、always-on agents、AI inference、数据标注与评测、DS／ML／AI 职业方向、多智能体协同、企业 AI 落地及 Harness／Rubric／Trajectory 等。这里仅作主题对照，未读到每篇完整正文和互动数据；删除线不能独立证明具体平台已发布。

本系列 S01–S10 已覆盖技术栈、时间序列、检索、KV Cache、推理、行业观点、数据需求和书籍介绍。新稿改为具体的 coaching 场景，不再重复工具总览：

| 新稿 | 延续已有方向 | 本次增加的具体交付 |
|---|---|---|
| S11 | AI Stack／项目实践 | 一页项目决策记录＋故障定位自测 |
| S12 | 企业 AI／创业观点 | 一个流程的 pilot 验收与采购决策问题 |
| S13 | DS／ML／AI 职业方向 | JD 三栏差距诊断，按原有背景设计练习 |
| S14 | 数据标注／Agent 评测 | 业务状态、可观察工具行为、任务成本三类检查 |
| S15 | 多智能体协同／学习反馈 | 追踪一次用户动作，审查隐含设计与有效测试 |
| S16 | DS 职业／统计判断 | 岗位要求与面试形式分开，设计诊断练习 |

## 需求证据表

“票数”仅记搜索索引中可见的主帖快照，不是实时指标，也不用来推算购买意图；评论数本轮未可靠取得。

| ID | 索引日期（未独立核实） | 原帖与社区 | 可见主帖票数 | 需求摘要与限制 |
|---|---|---|---|---|
| R01 | 2026-09-16 | [Are portfolios meaningless now that anyone can build anything?](https://www.reddit.com/r/dataengineering/comments/1wi4n4w/are_portfolios_meaningless_now_that_anyone_can/) · r/dataengineering | +75 | 怀疑 AI 时代 portfolio 的价值；评论对招聘是否查看有分歧，但出现“项目理解能支持面试”的意见。不能保证项目带来面试。 |
| R02 | 2026-09-29 | [What 1–2 projects would you build?](https://www.reddit.com/r/AI_India/comments/1wteejj/ai_engineers_genai_engineers_what_12_projects/) · r/AI_India | +10 | 想深入做少量项目，能解释评测、成本、延迟、故障处理及选型。r/developersIndia 同文去重。 |
| R03 | 2026-05-05 | [Two End-to-End Projects Done with AI assistance](https://www.reddit.com/r/askdatascience/comments/1t4powv/two_endtoend_projects_done_05m_records_with_ai/) · r/askdatascience | +1 | 理解算法但依赖 AI 实现，担心如何证明独立能力。低票样本，只证明有人提出问题。 |
| R04 | 2026-10-15 | [How can I transition into AI Engineering?](https://www.reddit.com/r/learnmachinelearning/comments/1x6lauf/how_can_i_transition_into_ai_engineering_in_the/) · r/learnmachinelearning | +79 | 有 DE 经历但不清楚先学什么；讨论中对 AI Engineer 的含义存在差异。原页相对时间与索引不一致。 |
| R05 | 2026-08-13 | [Stuck between my current career path and my interest in AI/ML](https://www.reddit.com/r/datasciencecareers/comments/1vneqf7/stuck_between_my_current_career_path_and_my/) · r/datasciencecareers | 未记录 | 想知道工程背景如何逐步转向 AI／ML，而非泛泛路线图。 |
| R06 | 2026-10-01 | [Data Science Interview these days](https://www.reddit.com/r/datasciencecareers/comments/1wuxzd3/data_science_interview_these_days/) · r/datasciencecareers | +11 | DA 转 DS，对编码、统计深度和新工具的准备范围困惑；回复明确反映流程差异，部分带辅导产品推广。 |
| R07 | 2026-01-28 | [Data Science Interview Experiences](https://www.reddit.com/r/learndatascience/comments/1qp3v37/data_science_interview_experiences/) · r/learndatascience | +4 | 一位候选人列出不同公司的项目、SQL、统计等考核差异。较早样本，不作当前统一招聘标准。 |
| R08 | 2026-03-20 | [How are you actually evaluating agentic systems in production?](https://www.reddit.com/r/LLMDevs/comments/1ryzv71/how_are_you_actually_evaluating_agentic_systems/) · r/LLMDevs | +11 | 手测无法覆盖多步骤、版本回归与静默失败；评论含服务推广，工具效果未核验。 |
| R09 | 2026-09-01 | [Most people evaluating LLM changes are just eyeballing outputs](https://www.reddit.com/r/LLMDevs/comments/1w43rhc/most_people_evaluating_llm_changes_are_just/) · r/LLMDevs | +13 | prompt 变更缺少稳定比较和回归集。主帖附课程推广，降低权重；标题中的“most people”不采纳为事实。 |
| R10 | 2026-09-23 | [Maintaining quality in the age of Agentic Engineering](https://www.reddit.com/r/ExperiencedDevs/comments/1wojx18/maintaining_quality_in_the_age_of_agentic/) · r/ExperiencedDevs | +469 | 生成速度超过理解与 review 能力，难维护系统认知。讨论有明显争议，不能推导 AI 编程普遍降低质量。 |
| R11 | 2026-09-07 | [Starting a 2 week Pilot with B2B client](https://www.reddit.com/r/startups/comments/1w9xv3f/starting_an_2_week_pilot_with_b2b_client_for/) · r/startups | +5 | 文档处理产品创始人直接询问成功标准、真实使用反馈和付费转化。具体程度高，未验证商业结果。 |
| R12 | 2026-10-27 | [Failed trying to ride AI software wave. What next?](https://www.reddit.com/r/startupideas/comments/1xh1wc1/failed_trying_to_ride_ai_software_wave_what_next/) · r/startupideas | +55 | 自述语音 Agent 找不到新客户；不能由个案得出整个 AI SaaS 市场不可做。 |
| R13 | 2026-11-12 | [Bootstrapped founders: first paying customers?](https://www.reddit.com/r/SaaS/comments/1xu74l0/bootstrapped_founders_what_actually_got_you_your/) · r/SaaS | +14 | 围绕信任、试点、实际使用与付费展开；评论路径互相不同，不据此宣布某个获客渠道最有效。 |

## 人群与语言信号

A 人群的缺口是“我的能力如何被验证”，而不只是缺一个工具清单。R01–R03 支持作品集与 AI 辅助实现的焦虑；R04–R07 支持目标岗位不清晰和准备范围过宽。建议交付一次差距诊断、一个项目深挖练习或一页可解释的决策记录。是否愿意付费仍需由实际咨询反馈验证。

B 人群的缺口是“做出来之后，如何知道可以交付、客户为何继续用”。R08–R09 支持评测问题，R11–R13 支持从 demo 到试点与购买的断点。S12 不提供合同法律意见、不照搬原帖定价；S14 不把一个小评测集当作上线安全保证。

可借鉴的真实措辞（短语摘录，来源见上表）：

| 来源 | 原词／短语 | 文案落点 |
|---|---|---|
| R01 | “Are portfolios meaningless” | 承认作品集价值焦虑，再给可操作证据 |
| R02 | “1–2 solid AI projects” | 深入一个项目，而非堆十个题目 |
| R04 | “where to start and what to prioritize” | 从 JD 和现有能力确定下一步 |
| R08 | “failing silently” | 区分成功回复与真实业务状态 |
| R10 | “mental model” | 解释为对系统如何运作的理解 |
| R11 | “beyond ‘they liked it’” | 提前约定试点验收问题 |

工具提及仅用于识别讨论上下文，不推荐、不排名。按上述已读片段做最低出现计数（同一线程只记一次）：Confident AI 1（R08 评论，带推荐倾向）；PostHog 1（R11 主帖）；Azure／Databricks 1（R04 主帖）；Claude 3（R01、R04、R10）；Codex 2（R04、R10）。该计数不是完整评论语料统计，更不是市占率。选题价值不依赖这些品牌。

## 建议发布顺序与 coaching 交付

| 顺序 | 选题 | ICP／视角 | 需求来源 | 推荐理由／限制 | 可引导的咨询 |
|---|---|---|---|---|---|
| S11 | 作品集怎么证明判断力 | A／求职实操 | R01–R03 | 多个独立问题，关联已有项目系列；不给招聘结果保证 | 项目诊断、模拟深挖 |
| S12 | AI pilot 怎样验收 | B／创业实践 | R11–R13 | 具体购买决策问题，和求职交替；低票但需求清晰 | 试点范围、指标与决策设计 |
| S13 | 转 AI 先补哪块 | A／职业路径 | R04–R05 | 利用已有经验，避免统一学习清单 | JD／背景差距评估 |
| S14 | Agent 真的完成任务了吗 | B／工程科普 | R08–R09 | 从既有评测主题推进到可执行任务；营销评论降权 | 评测方案与发布标准 |
| S15 | AI 代码该审什么 | A→B／工程观点 | R10＋R03 | 高参与但有争议，适合提出 review 练习，不下普遍结论 | 项目 review、工程能力诊断 |
| S16 | DS 面试怎么收敛准备 | A／求职诊断 | R06–R07 | 岗位和面试差异明确；不押题、不承诺 offer | 目标岗位准备计划 |

每个主题都是文字帖，可直接使用现有平台文档中的正文，无需等待新增图。小红书按既有习惯可把长文转成平台图文卡；Facebook 用英文讨论帖。建议观察有背景的提问与咨询，而不是用点赞替代付费意图。暂不设发布日历、不创建定时任务。

## 技术核对与编辑约束

- S14 的评测结构参考 [Anthropic：Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)。仅用于核对任务、试次、评分与真实结果的区分；帖子中的订单例子和练习安排是本轮编辑设计。
- S11／S13／S15／S16 的检查表是 Jay 视角的 coaching 建议，不声称为行业统一招聘标准；不将 Reddit 评论“多数 AI 岗位只需接 API”或“公司不看算法”当作事实。
- S12 保留“有设计的免费试点也可提供信息”，不把免费试点一律否定。数字阈值需按场景约定，不虚构转化案例或收益。
- 未复用旧系列的热点数字、实验室排名或未经验证的新模型信息。小红书正文无外链，Facebook 每篇只设一个 MentorCruise 转化链接。
- S09／S10 为此前单平台内容，小红书从 S08 跳到 S11 是为了统一系列 ID，不是漏稿。S01–S10 的既有文案和发布状态保持原样。

## 交付入口

- [小红书 Publication Sequence＋完整文案](posts_rednote.md#s11)
- [Facebook Publication Sequence＋完整文案](posts_fb.md#s11)

后续若实际发布，分别更新对应平台状态和真实日期。收到咨询后可记录其背景、问题类别与是否愿意进一步沟通；不把本轮 Reddit 发帖人当作已经确认的客户。
