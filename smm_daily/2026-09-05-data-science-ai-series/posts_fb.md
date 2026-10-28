# Data Science × AI｜Facebook · Jay

本表仅维护 Facebook 状态，所有帖子仍为草稿、未排期；不沿用小红书的发布状态。 各篇按主题采用不同视角：技术总览、机制科普、专家对比、工程实践或行业讨论。

下方为英文文案，面向 Jay 的专业受众；CTA 直接附 MentorCruise 链接。

定位、素材说明及资料核对见 [系列编辑说明](README.md)。

## Publication Sequence

| 顺序 | ICP | 视角 | 主题／标题 | 素材 | 文案 | 状态 | 发布日期／链接 |
|---|---|---|---|---|---|---|---|
| S01 | A · 转行入门 | 技术总览＋学习路径 | The AI stack: nine layers, and how to connect them. | [素材](assets/ai-stack.jpeg) | [查看文案](#s01) | 草稿／未排期 | — |
| S02 | A · 统计／DS 转 AI | 统计×AI 科普 | Time-series foundation models sit at the intersection of statistics and AI. | [素材](assets/time-series-forecsting.gif) | [查看文案](#s02) | 草稿／未排期 | — |
| S03 | A · 检索实践 | 技术教学＋动手练习 | Hybrid retrieval, explained with a four-document RRF example. | [素材](assets/hybrid-retrieval.png) | [查看文案](#s03) | 草稿／未排期 | — |
| S04 | A → B · 场景适配 | 场景适配／工程观点 | Why does an AI coding agent still use grep? | [延展自 Hybrid Retrieval](assets/hybrid-retrieval.png)；以文字场景讲解 | [查看文案](#s04) | 草稿／未排期 | — |
| S05 | A · AI 工程基础 | 机制科普 | Why long conversations need KV caching. | [素材](assets/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%A8%E7%90%86%E5%8A%A0%E9%80%9F1%EF%BC%9AKV%20Cache_1_Dev.E_%E6%9D%A5%E8%87%AA%E5%B0%8F%E7%BA%A2%E4%B9%A6%E7%BD%91%E9%A1%B5%E7%89%88.jpg) | [查看文案](#s05) | 草稿／未排期 | — |
| S06 | A · 转行 AI Engineering | 专家对比＋职业学习 | Ollama, vLLM and SGLang: what inference infrastructure actually optimizes. | [素材](assets/AI-inference.jpeg) | [查看文案](#s06) | 草稿／未排期 | — |
| S07 | B · AI 行业观察 | 行业观察／争议讨论 | The AI lab race is a moving picture, not a permanent tier list. | [素材](assets/frontier-labs.png) | [查看文案](#s07) | 草稿／未排期 | — |
| S08 | B · AI 创业与咨询 | 创业观点 | If the model improves next month, why will customers still need you? | [素材](assets/anthropic_vs_saas.jpeg) | [查看文案](#s08) | 草稿／未排期 | — |

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
