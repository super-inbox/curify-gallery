# Data Science × AI｜Facebook · Jay

本表仅维护 Facebook 状态，截至 2026-11-20，S01 AI Stack 已于 2026-10-28 发布，S02 Time Series Forecasting 已于 2026-10-29 发布；S11–S12 已确认发布，具体日期和链接未提供；其余仍为草稿、未排期。 各篇按主题采用不同视角：技术总览、机制科普、专家对比、工程实践或行业讨论。

下方为英文文案，面向 Jay 的专业受众；S01–S08 沿用 MentorCruise CTA，S09 面向多模态数据需求，采用私信与圈内引荐 CTA；S10 为作者书籍介绍，采用 Amazon 购书与讨论 CTA。

定位、素材说明及资料核对见 [系列编辑说明](README.md)。

2026-11-16 新增 S11–S16：基于 Reddit 需求讨论的 coaching 系列；截至 2026-11-20，S11–S12 已发布，S13–S16 仍为草稿／未排期；编号跨平台统一。选题依据与建议顺序见 [本轮研究记录](reddit-demand-mining-2026-11-16.md)。

## Publication Sequence

| 顺序 | ICP | 视角 | 主题／标题 | 素材 | 文案 | 状态 | 发布日期／链接 |
|---|---|---|---|---|---|---|---|
| S01 | A · 转行入门 | 技术总览＋学习路径 | The AI stack: nine layers, and how to connect them. | [素材](assets/ai-stack.jpeg) | [查看文案](#s01) | 已发布（操作者确认） | 2026-10-28／链接未提供 |
| S02 | A · 统计／DS 转 AI | 统计×AI 科普 | Time-series foundation models sit at the intersection of statistics and AI. | [素材](assets/time-series-forecsting.gif) | [查看文案](#s02) | 已发布（操作者确认） | 2026-10-29／链接未提供 |
| S03 | A · 检索实践 | 技术教学＋动手练习 | Hybrid retrieval, explained with a four-document RRF example. | [素材](assets/hybrid-retrieval.png) | [查看文案](#s03) | 草稿／未排期 | — |
| S04 | A → B · 场景适配 | 场景适配／工程观点 | Why does an AI coding agent still use grep? | [延展自 Hybrid Retrieval](assets/hybrid-retrieval.png)；以文字场景讲解 | [查看文案](#s04) | 草稿／未排期 | — |
| S05 | A · AI 工程基础 | 机制科普 | Why long conversations need KV caching. | [素材](assets/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%A8%E7%90%86%E5%8A%A0%E9%80%9F1%EF%BC%9AKV%20Cache_1_Dev.E_%E6%9D%A5%E8%87%AA%E5%B0%8F%E7%BA%A2%E4%B9%A6%E7%BD%91%E9%A1%B5%E7%89%88.jpg) | [查看文案](#s05) | 草稿／未排期 | — |
| S06 | A · 转行 AI Engineering | 专家对比＋职业学习 | Ollama, vLLM and SGLang: what inference infrastructure actually optimizes. | [素材](assets/AI-inference.jpeg) | [查看文案](#s06) | 草稿／未排期 | — |
| S07 | B · AI 行业观察 | 行业观察／争议讨论 | The AI lab race is a moving picture, not a permanent tier list. | [素材](assets/frontier-labs.png) | [查看文案](#s07) | 草稿／未排期 | — |
| S08 | B · AI 创业与咨询 | 创业观点 | If the model improves next month, why will customers still need you? | [素材](assets/anthropic_vs_saas.jpeg) | [查看文案](#s08) | 草稿／未排期 | — |
| S09 | B · 多模态数据负责人／研究与采购 | 需求验证＋圈内引荐 | 3D reconstruction, design-task trajectories and evaluation data | [配套3D重建视频](../../drama_animation/white-model-reconstruction-2026-11-02/source-vs-white-model-v14.mp4) | [查看文案](#s09) | 草稿／未排期 | — |
| S10 | A → B · DS／AI 学习者与推荐系统从业者 | 作者视角＋技术导读 | My book: Building Recommender Systems Using Large Language Models | [书封](../../ds_ai/book_recommendation/LLM%20book.jpg) | [查看文案](#s10) | 草稿／未排期 | — |
| S11 | A · DS／AI 求职者 | 求职 coaching＋作品集实操 | Build a portfolio your target team has a reason to care about. | 文字帖／无需新增素材 | [查看文案](#s11) | 已发布（操作者确认） | 具体日期／链接未提供；2026-11-20 确认 |
| S12 | B · AI startup 创始人 | 创业 coaching＋pilot 设计 | An AI project gets harder when you promise the unproven parts. | 文字帖／无需新增素材 | [查看文案](#s12) | 已发布（操作者确认） | 具体日期／链接未提供；2026-11-20 确认 |
| S13 | A · DS／DE／软件工程转 AI | 职业路径＋差距诊断 | An AI career transition needs a schedule that leaves room for depth. | 文字帖／无需新增素材 | [查看文案](#s13) | 草稿／未排期 | — |
| S14 | B · AI 产品技术负责人 | 工程科普＋上线评审 | Your agent says “done.” What actually changed? | 文字帖／无需新增素材 | [查看文案](#s14) | 草稿／未排期 | — |
| S15 | A → B · 工程师／小团队技术负责人 | 工程观点＋review 练习 | “Fully implemented.” Excellent. Now show me what actually works. | 文字帖／无需新增素材 | [查看文案](#s15) | 草稿／未排期 | — |
| S16 | A · DS 求职／DA 转 DS | 面试 coaching＋练习设计 | Prepare for the work behind the data science title. | 文字帖／无需新增素材 | [查看文案](#s16) | 草稿／未排期 | — |
| S17 | A · 有经验的 DS／职业转型 | 专家观察＋职业选择 | Why are people reconsidering a data science career? | 文字帖／无需新增素材 | [查看文案](#s17) | 草稿／未排期 | — |
| S18 | A → B · 新人／带教负责人 | 培养路径＋mentorship | If AI handles beginner tasks, where does experience come from? | 文字帖／无需新增素材 | [查看文案](#s18) | 草稿／未排期 | — |

---

## S01

**The AI stack: nine layers, and how to connect them.**

This diagram focuses on generative AI applications. An AI stack diagram is most useful when you can explain what each layer does. Here is how I would introduce the nine layers to someone moving into AI engineering.

1. Models generate or interpret content: for example, Claude or Qwen.
2. Inference and access make a model callable: Ollama and vLLM are examples.
3. Orchestration coordinates steps and branches: LangGraph or LlamaIndex.
4. Tools and protocols connect business systems: HTTP APIs or MCP.
5. Memory retains selected information across interactions: a database with explicit rules, or a system such as Mem0. This is different from a model’s KV cache.
6. Retrieval storage keeps searchable material: pgvector or Elasticsearch.
7. Embeddings represent content as vectors; rerankers reorder retrieved candidates. Sentence Transformers and cross-encoder rerankers are useful examples to explore.
8. Extraction turns documents into usable inputs: for example, Docling.
9. Evaluation and observability check behaviour and trace execution: test scripts and a tool such as Langfuse.

My learning recommendation: get hands-on with one or two representatives in each layer. Understand their inputs, outputs and failure modes. You do not need every tool in the diagram, and one application does not need every layer.

Then connect a real workflow. For an employee-policy assistant, extract documents, split them into passages, embed and store them, retrieve evidence, generate a cited answer, and evaluate it against a fixed question set. Track latency along the way.

Add a leave-balance tool when the workflow needs live business data. Add persistent preferences when there is a reason to remember them. Add orchestration when the branching justifies it.

If you are changing careers into AI, we can discuss a learning plan that turns this overview into an end-to-end project.

[Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #DataScience #CareerTransition

---

## S02

**Time-series foundation models sit at the intersection of statistics and AI.**

Sales, electricity demand and sensor readings are familiar territory for statistics. They are now also a setting for foundation models.

Exponential smoothing models levels, trends and seasonal patterns. ARIMA models temporal relationships in a series and its errors. Typically, we fit a model around the series we want to forecast.

A time-series foundation model moves part of the learning earlier: pretrain across many sequences, then transfer that learning to another forecasting task. Some support zero-shot forecasting; some can also be adapted further. This does not necessarily mean using a chat model or converting every number into prose.

The Timestral illustration has two stages. The upper half represents pretraining. The lower half applies the trained model to a shop’s data: sales are the target, past foot traffic is a historical covariate, and a promotion already on the calendar is a known future covariate. Covariates are simply additional variables that may help explain the target.

The output can include quantiles—a way to describe a range of possible outcomes rather than one exact number.

Statistical judgment still matters. Time order, seasonality and uncertainty do not disappear with pretraining. Tomorrow’s actual traffic cannot be treated as known when making today’s forecast.

A useful exercise is to compare a seasonal baseline, a classical model and a foundation model on the same rolling time splits. Examine forecast errors and interval coverage. This is a particularly interesting project for someone bringing a statistics or analytics background into AI.

[Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #DataScience #CareerTransition

---

## S03

**Hybrid retrieval, explained with a four-document RRF example.**

Document assistants and many agents need to find evidence before answering or acting. Hybrid retrieval is a useful building block for that job.

In this example, BM25 scores term matches using lexical statistics. Embedding-based retrieval compares vector representations to find semantically related content. Their raw scores are on different scales, so simply adding them is not a sound default.

Reciprocal Rank Fusion (RRF) combines positions instead. Each list contributes 1 / (k + rank); ranks start at 1. Use k = 60 for this toy example. An absent document contributes zero from that list.

BM25 returns A, B, C. Vector search returns C, A, D.

- A: 1/61 + 1/62 ≈ 0.03252
- C: 1/63 + 1/61 ≈ 0.03227
- B: 1/62 ≈ 0.01613
- D: 1/63 ≈ 0.01587

The fused order is A, C, B, D. A places well in both lists. We have combined ranking signals without directly calibrating BM25 and similarity scores; 60 is a parameter choice, not a universal requirement.

Try this hands-on: collect 20 short documents, write ten questions and label the relevant evidence. Retrieve three candidates from each method, merge them with RRF, then check whether the correct evidence appears in each method’s top three. Record latency too.

Manuals, reports and policy files are natural places to explore this. Different data may call for different combinations—the next post looks at grep in coding agents.

Want to turn the exercise into a retrieval portfolio project? We can work through the data, implementation and evaluation.

[Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #DataScience #CareerTransition

---

## S04

**Why does an AI coding agent still use grep?**

We often picture AI retrieval as turning documents into vectors and searching by meaning. Yet a coding agent can find useful context with a much older idea: searching for text patterns.

Anthropic has described Claude Code using grep and glob to discover context as it works. Glob finds filenames; grep finds matching content. That path does not always need a prebuilt vector index of the repository.

Code contains useful signposts: function names, paths, errors and call sites. For a refund bug, an agent might search for `refund`, read the matching function, then follow its callers. Each result informs the next search.

If the business calls it a reversal, try that term too. Aliases, alternate names and reusable directory filters can help navigation; they do not give grep semantic understanding. The agent supplies the iterative investigation.

BM25 plus embeddings is one useful hybrid. A broader retrieval design can also combine symbol lookup, directory navigation or structured queries. The right mix depends on the data and the task.

Exact identifiers favour text search. Natural-language descriptions may benefit from semantic search. Large repositories and unclear naming can make repeated grep calls expensive too. Compare complete task outcomes, time and context consumed—not just whether a search returned something.

Designing retrieval for an AI product? Bring a representative task and a few failure cases, and we can discuss a system that fits your data.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #CodeSearch #AIConsulting

---

## S05

**Why long conversations need KV caching.**

You paste a long document into a GPT-style assistant, ask for a summary, then ask it to expand one section. Why should the system redo all earlier work every time it generates another token?

Start with two stages. Prefill processes the input and produces intermediate attention data, including keys and values. Decode generates new tokens step by step. A token may be a word fragment or another unit; it is not always a word or character.

The KV cache keeps earlier keys and values so decoding can reuse them. It stores intermediate computation, not a finished answer or a persistent profile of the user.

There is a second opportunity: reuse across requests. If the next request begins with the same long document, a serving system with prefix caching may reuse the matching prefix instead of processing it again. Support, cache retention and an actual match all matter. This describes a general mechanism, not a claim about a particular chat product’s internals.

What if you edit the input? For a typical autoregressive Transformer, appending a new question may preserve a reusable prefix. Changing a sentence in the middle changes dependencies from that point onward, so that suffix generally needs processing again. Block boundaries and implementation details affect how much can be reused.

Long context therefore raises two questions: how much can the model accept, and how much work can the system reuse? Caching saves computation but consumes memory. Prefix reuse primarily reduces repeated input processing; it does not remove the work of generating every new token.

If you are moving from using models to building AI systems, this is a useful place to start learning inference engineering.

[Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #DataScience #CareerTransition

---

## S06

**Ollama, vLLM and SGLang: what inference infrastructure actually optimizes.**

Many people know that a trained model needs to be deployed for inference. Fewer have worked with the infrastructure between loading weights and serving users reliably.

These three tools are useful entry points. They are runtime and serving systems with overlapping capabilities, not three mutually exclusive model architectures.

**Ollama: simplify getting a model running and callable.**
It offers a convenient local workflow for downloading and running models through an API. Quantized weights can reduce memory requirements, with quality and speed trade-offs to test. Think personal document Q&A, learning experiments or internal prototypes. Ollama also supports concurrency when memory and configuration allow it.

**vLLM: use memory and batching more effectively.**
PagedAttention manages KV cache in blocks to reduce memory waste. Continuous batching lets completed requests leave and new requests join an active workload. Prefix caching can reuse repeated input computation.
This is relevant to concurrent Q&A and batch generation. With a supported vision-language model, vLLM can also serve image questions or document-image understanding. The engine serves the model; it does not add vision capabilities to a text-only model.

**SGLang: pay attention to reusable context and generation workflows.**
RadixAttention organizes reusable prefix KV data in a tree structure. Requests sharing an opening can avoid repeating some computation. A support service with a long shared policy, or agent branches sharing task context, provides a concrete workload to investigate.
SGLang is also a general serving framework. Prefix reuse is not exclusive to it; vLLM supports it too.

I would start selection with the workload: local experimentation, concurrent service, repeated long prefixes, or multimodal inputs. Then hold model, hardware and precision constant and measure time to first token, generation speed and latency under load.

For a career move into AI engineering, this is an important layer to learn. We can build a practical path from local inference to a small deployed service.

[Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #DataScience #CareerTransition

---

## S07

**The AI lab race is a moving picture, not a permanent tier list.**

When I see an AI lab tier list, I wonder how much of it will still look the same next month.

This is an ongoing race in training, post-training, compute, talent and product delivery. Progress is not revealed smoothly: labs work behind the scenes, then release concentrated bursts of capability. A quiet period is not necessarily a halt.

Two examples worth tracking in this cycle are Meta’s Muse family and Moonshot’s Kimi K3. On October 27, Meta and NVIDIA announced expanded work on Muse training and inference. Moonshot’s K3 materials emphasize native vision, long context and coding workloads. These are different routes into a changing competitive field, not evidence of a single universal winner.

My view is that the landscape deserves weekly attention, while weekly excitement deserves skepticism. “Top tier” could mean broad capability, coding, multimodal performance or strength of the open-model ecosystem. The answer changes with the dimension.

The supplied Frontier List puts Anthropic and OpenAI in its Frontier group places Google DeepMind, Meta and Moonshot in n-1, and puts Microsoft and Amazon further down. It is a survey of people’s judgments, not a controlled test that settles every comparison.

Before saying a lab is falling behind, I would look across multiple release cycles: is it narrowing gaps, delivering usable models and building an area of leadership? One missing launch or one chart is weak evidence for declaring it out of the race.

Who belongs in your top tier today? Who is catching up, and who is genuinely losing ground? Name the dimension behind your answer—research, coding, multimodality or ecosystem.

For a deeper conversation about the AI landscape and technical direction, you can find me on MentorCruise.

[Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIIndustry #FrontierModels #AI

---

## S08

**If the model improves next month, why will customers still need you?**

Charts comparing model companies with SaaS invite a dramatic question: will the model absorb the application?

I find a more useful starting point in the customer’s job.

Drafting an email is one capability. Connecting permissions, fitting a business process, recovering from failures and keeping an audit trail are parts of delivering the result. A strong engine still needs a vehicle built for its purpose.

My view: if your product depends mainly on a temporary model limitation, test that assumption carefully. If it delivers a difficult workflow reliably, examine integration effort, operating cost and customers’ willingness to keep paying.

A valuation chart cannot settle that question. Valuation and revenue describe different things, and comparisons need consistent dates and definitions.

Write down your answer to this: if the underlying model becomes stronger and cheaper next month, what will customers still pay your team to do?

Building an AI business? Bring a workflow and the assumptions behind it. We can discuss technical differentiation, delivery risks and where consulting could help.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #AIStartups #AIConsulting


---

## S09

**Does anyone in my network work on training or evaluation data for multimodal AI or agents?**

We’ve been working on video-to-3D reconstruction and a design benchmark. I’d like to connect with teams looking for data that captures how a task gets done, as well as the final result.

The video shows one prototype: original footage paired with our simplified 3D reconstruction. We’re still refining the motion and spatial alignment.

The broader directions we’re exploring include:

• Video / 3D pairs and motion trajectories.
• Design-task trajectories: the brief, tool actions, intermediate work, revisions, and final output.
• Benchmark tasks and quality checks for evaluating whether an agent actually meets the requirements.

If you work on multimodal LLMs, video understanding, spatial reasoning, or creative-tool agents, what data is hardest to source? What format and quality checks would you need?

I’d be happy to discuss a small pilot around a concrete requirement. These workflows are still being validated; we haven’t demonstrated a model-training benefit yet.

Message me if this is relevant, or introduce me to someone who owns datasets, evaluation, or data sourcing on your team.

#MultimodalAI #TrainingData #AIAgents

### S09 编辑备注（不复制进帖子）

2026-11-02新增，面向Jay专业圈子的多模态训练／评估数据需求，不投Curify历史文化号。当前仅草稿、未排期、未发布；LinkedIn与Facebook状态独立回填。[LinkedIn版本与素材边界](posts_linkedin.md#s09)。用户已选现有3D重建对照视频作配套素材；其为原型样段，不能当作design trajectory演示或已验证训练数据。动作轨迹与设计任务过程分别表述。无训练收益、规模化产能或具体客户背书的声明。


---

## S10

**What changes when a recommender system can understand what you mean?**

Think about asking for a book: “I know the basics of machine learning, but I want something that helps me build a real application.” That sentence contains a goal, a starting point, and a preference—useful context for a recommendation.

This is the intersection I explore in my book, Building Recommender Systems Using Large Language Models, published by Springer.

The book follows a progression from traditional recommendation methods to LLM-powered systems:

• Enhancing an existing recommender with LLMs.
• Using an LLM as the recommender itself.
• Building conversational recommendations that let users express and refine their needs.
• Bringing in multimodal information, then exploring generative recommendation and planning.

It combines technical explanations with coding exercises and case studies, and also covers challenges such as privacy and fairness. A basic grounding in machine learning and NLP will help you get the most from it.

For people moving from data science into AI, recommendation is a concrete application to study: the system has to connect an understanding of the user with a useful decision. For practitioners already working on personalization, the book offers a structured way to explore where LLMs fit.

You can find the book on Amazon:
https://www.amazon.com/dp/B0FX7N91FQ

If you work on recommendations, which part are you most interested in exploring with LLMs: understanding content, learning user preferences, or building a conversational experience? I’d love to hear what you’re working on.

#RecommenderSystems #LargeLanguageModels #DataScience #AppliedAI


---

## S11

**Build a portfolio your target team has a reason to care about.**

Many portfolios lose the reader at the project idea.

Learn a model, find a dataset to apply it to. Learn a framework, build another chatbot. The project works, but someone in industry has little reason to discuss it further. Too many portfolios arrive at the same place.

When I mentor someone on project selection, I look for two directions: depth in the method, or a close connection to a real application.

For a methods-focused project, choose one or two target teams. Read their technical blogs and papers. Identify a problem they are working on and understand why the existing approach is insufficient. Then take a manageable piece of it: reproduce a key result, change the data or constraints, and investigate where the method succeeds and fails.

That gives the team something relevant to discuss with you. “Frontier” needs to mean you understand a substantive technical question, including the limits of the evidence.

For an application-focused project, get close to actual work. A mentee I worked with recently used requirements from real design-department tasks to develop data simulations and benchmarks. This attracted interest from companies because they could recognise the connection to their own work. The project had a basis in real requirements and data.

Preserve the awkward details: the inputs people actually have, the variations they encounter, and what makes an output usable. With simulated data, explain what the simulation represents and what it leaves out.

Before starting, answer three questions: Which team should care? How does this connect to their work? Where will I go deep enough to have a useful technical conversation?

If you want to develop a project around your target teams, bring one or two of them to our discussion:
https://mentorcruise.com/mentor/jaywang/

#AIEngineering #DataScience #Portfolio #CareerDevelopment


---

## S12

**An AI project gets harder when you promise the unproven parts.**

In AI client work, a difficult conversation often starts much earlier than delivery: a capability was promised before anyone established that it worked.

The team thinks the first release is an assisted workflow. The customer is expecting full automation. Both remember agreeing on the project.

I separate two questions: what deserves priority, and what we can responsibly promise.

Prioritisation includes uncertainty. If the feature the customer wants depends on an unproven capability, the first milestone may need to test that capability before the team commits to the rest of the build.

Promises need concrete inputs, outputs, and operating conditions. “Handles complex documents” leaves too much room for different interpretations.

For a document-processing project, I would ask the customer for representative inputs, mark the fields they expect, and show the corresponding outputs. Identify what has been demonstrated, what needs human review, and how the first release handles poor scans, missing pages, or a new template.

Make feedback equally tangible. When a result is “not good enough,” ask the customer to mark the problem and show the expected result. Annotated examples, screenshots, and a working prototype can expose a disagreement that another page of prose will miss.

For each milestone, agree on what will be delivered, what data and feedback the customer must provide, and which findings determine the next phase. Discuss the effect of new requirements on scope and timing when they arise.

An uncertain capability can be tested. A promise made with a different definition of “finished” is much harder to repair.

If you are scoping an AI engagement, bring the requirement, a representative input, and the commitments already made:
https://mentorcruise.com/mentor/jaywang/

#AIStartups #ClientDelivery #ProductDevelopment


---

## S13

**An AI career transition needs a schedule that leaves room for depth.**

In AI career coaching, I often see broad exposure without much depth. Someone has tried the tools, finished tutorials, and built a working project. The conversation gets harder when we examine why the method works or what happens when the data changes.

Standing out takes a direction and sustained commitment. Once the direction is clear, I would plan in months, with time for repeated practice and revision.

For someone who already codes and wants to work on retrieval and AI applications, an illustrative six-month schedule could look like this:

Months 1–2: strengthen the relevant foundations. Implement small, important components yourself and explain their inputs, outputs, and failure conditions.

Months 3–4: investigate one concrete problem. Read the relevant methods, reproduce a baseline, analyse failures, and change one important factor at a time. Keep a record of what the experiments show.

Months 5–6: introduce realistic constraints: varied inputs, latency, cost, and failure handling. Turn the work into a reproducible portfolio project and practise discussing it in depth.

Six months is a planning example, not a promise of career readiness. The schedule depends on your starting point, target role, and weekly availability. Put the time in your calendar and leave room to revisit weak areas.

Use AI as a practice partner. Ask it to challenge your assumptions, supply a flawed implementation, or change the input conditions. Explain and fix the problem yourself, then check references and actual results. Its approval is not evidence of mastery.

Every two weeks, review what you still cannot explain, which experiments changed your understanding, and what to practise next. A portfolio can grow through increasingly serious versions of the same project.

If you are ready for that commitment, bring your target direction, current skills, and realistic weekly availability:
https://mentorcruise.com/mentor/jaywang/

#AIEngineering #CareerTransition #LearningPlan


---

## S14

**Your agent says “done.” What actually changed?**

An order-management assistant can produce a polite success message while changing the wrong record, acting twice, or saving nothing.

An evaluation of this assistant needs to check three things:

• Outcome: did the intended state change, with unrelated records left untouched?
• Behaviour: did the observable tool calls respect permissions, confirmations, and duplicate-action rules?
• Cost: how much time, model usage, retry work, and human intervention did a completed task require?

Start with a small, representative set of ordinary requests and exceptions: missing information, tool timeouts, and a user changing their mind. Write down expected and prohibited outcomes before running the system. This is a starting exercise, not proof of production readiness.

Check exact fields with explicit rules. Use a clear rubric for subjective quality; if an LLM grades it, calibrate that grading against human review.

Compare old and new versions under the same conditions when prompts, models, or tools change. Repeat trials where variability matters, and feed newly observed failures back into the test set.

Bring the final business state and the tool-call record to the release review. A good answer does not establish that the correct order was updated.

If your agent works in a demo but the release criteria are unclear, we can design an evaluation plan around one real task:
https://mentorcruise.com/mentor/jaywang/

#AIAgents #Evaluation #AIEngineering


---

## S15

**“Fully implemented.” Excellent. Now show me what actually works.**

Give AI a complicated requirement and wait a moment:

“Fully implemented. All tests passing.”

Excellent. Let’s establish which definition of “fully” we are celebrating.

You asked for batch processing; it may handle one record. You asked for persistence; the data may live in memory. You asked for a working workflow; the interface may be backed by mock responses. A very smooth demo of a quietly smaller requirement.

I would follow up with specific questions:

“Map each original requirement to its implementation.”
“Which calls are real, and which parts are mocked, stubbed, or omitted?”
“Run a new input through the whole workflow. Where is the result stored?”
“Show the failure path. Did you execute it, or do you expect it to work?”

Check the answers against the code and the running system. Another confident paragraph from the same AI is not independent verification.

Then build checks at the appropriate levels:

• Unit tests for local logic and boundaries: empty input, missing fields, duplicates.
• Integration tests for the connections: API, queue, worker, database. Critical connections need testing against real dependencies in an appropriate test environment, rather than relying entirely on mocks.
• Smoke tests after startup or deployment: run a critical user path and verify that the entry point, dependencies, and result are available.

Review the tests too. If the implementation covers half the requirement and the tests cover the same half, everything can be beautifully green. Deliberately break an important behaviour occasionally and check that the test catches it.

Trusting every completion report leaves the undiscovered work for a future debugging session. Those sessions rarely arrive at a convenient time.

If you want a second look at an AI-assisted project and its verification gaps:
https://mentorcruise.com/mentor/jaywang/

#AIEngineering #SoftwareTesting #CodeReview


---

## S16

**Prepare for the work behind the data science title.**

SQL, algorithms, statistics, machine learning, causal inference, agents: a preparation list can expand faster than you can work through it.

A preparation schedule needs to account for both the work and the interview format.

Read the job description for the work: product decisions and experiments, predictive modelling, or deployment and reliability. Ask the recruiter about the known interview format. One person’s experience of not being asked algorithms is not a reason to remove coding practice from your own plan.

Then use one diagnostic exercise. A product launches a feature and retention improves. Should it roll out more widely?

Explain the decision first. Define retention, ask what else changed, check whether users were randomly assigned, identify other important metrics, and state what evidence is still missing.

For a modelling role, try “offline predictions improved, but business results did not.” For an engineering-heavy role, try “the model works, but serving latency increased.”

Record where you get stuck: the concept, the implementation, or explaining a trade-off. Use that record to choose next week’s practice, then repeat the exercise.

If you can reason through the statistics but still struggle to write the code live, give coding more of the next practice block. The diagnostic should change how you spend your time.

If you want a focused preparation plan, bring a target job description and a question you recently struggled with:
https://mentorcruise.com/mentor/jaywang/

#DataScience #InterviewPreparation #CareerDevelopment


---

## S17

**A few years ago, everyone wanted to get into data science. Now I hear more questions about leaving.**

Around 2019–2020, data science still carried the “sexiest job” reputation that dates back to 2012. I remember people moving from finance, relocating from the East Coast to the West Coast, and investing in expensive programmes that combined statistics, computing, and business. They could see room to grow.

Over the past four or five years, the conversations I encounter have become more varied: moving into AI, returning to finance, exploring biostatistics, or taking data skills outside tech. That is an observation from my professional circle, not a measure of industry-wide outflows.

I see three different motivations worth separating.

**Ownership.** You analyse a problem and recommend an answer, while other people define the question, decide what happens, and own implementation. Some people feel caught between analyst and engineer, without responsibility for a complete outcome. A different team with clearer ownership may address that frustration.

**A move toward building AI.** Data, modelling, and experimentation experience can provide a foundation for AI work. Some people want to build products and own systems more directly. That requires specific new capabilities, not just a new title.

**A different working life.** Layoffs and organisational uncertainty lead some people to reconsider tech. They may still want to use data skills in another industry. Finance and biostatistics have their own requirements; a traditional employer is not automatically a stable one.

Before deciding to leave DS, I would ask: Do you want more decision-making responsibility, different work, or a different employment environment?

Those answers lead to very different moves.

If you are weighing that decision, bring your background and the part of your work you most want to change:
https://mentorcruise.com/mentor/jaywang/

#DataScience #CareerTransition #AI

---

## S18

**If AI handles the beginner tasks, where does a beginner get experience?**

We need to design more of that learning deliberately. I would combine simulation, real work, and feedback from someone who can assess the learner’s judgment.

Think of the role a simulator plays in pilot training. A controlled environment lets you practise difficult situations repeatedly without putting a live system at risk.

For a data project, start with a normal dataset, then introduce leakage, a distribution shift, or missing fields. The learner diagnoses the problem, chooses a response, and checks the result. AI can generate variations and play a demanding stakeholder. The exercise and its reference answers still need verification; an encouraging AI response does not establish competence.

Then add real work. Changing requirements, messy inputs, and people depending on the result teach things a tutorial rarely captures.

I have seen people gain that exposure through startup internships, including unpaid arrangements. A small team and an early-career learner may have complementary needs, but a limited budget is not enough to make an internship worthwhile. Look for defined work, actual supervision, regular feedback, and an agreed way to demonstrate what you learned. Be clear about compensation and duration; unpaid arrangements must meet local rules and should not disguise ordinary employment.

Finally, get feedback on your decisions. Repeating a project without noticing the same mistake can reinforce the mistake.

My coaching covers data science, AI, and deep learning. Depending on the person, that can mean an AMA-style conversation, guided reading, an experiment review, or closer mentorship through a project.

If you are looking for that first meaningful experience, tell me what you have tried and where you need feedback:
https://mentorcruise.com/mentor/jaywang/

#AI #CareerDevelopment #Mentorship
