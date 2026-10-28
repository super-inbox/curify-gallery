# Data Science × AI｜Facebook · Jay

建议先后顺序，尚未预约或发布；本表仅维护Facebook状态。前三篇面向转入 Data Science / AI 的学习者，S04 从代码检索过渡到后续 AI 创业与咨询内容。

下方为英文文案，面向 Jay 的专业受众；CTA 直接附 MentorCruise 链接。

定位、素材说明及资料核对见 [系列编辑说明](README.md)。

## Publication Sequence

| 顺序 | ICP | 主题／标题 | 素材 | 文案 | 状态 | 发布日期／链接 |
|---|---|---|---|---|---|---|
| S01 | A · 转行入门 | Build one useful AI workflow before collecting tools. | [素材](assets/ai-stack.jpeg) | [查看文案](#s01) | 草稿／未排期 | — |
| S02 | A · 转行入门 | Forecasting starts with what you could know at the time. | [素材](assets/time-series-forecsting.gif) | [查看文案](#s02) | 草稿／未排期 | — |
| S03 | A · 转行入门 | Why an AI search system still needs keywords. | [素材](assets/hybrid-retrieval.png) | [查看文案](#s03) | 草稿／未排期 | — |
| S04 | A → B · 场景适配 | Why does an AI coding agent still use grep? | [延展自 Hybrid Retrieval](assets/hybrid-retrieval.png)；以文字场景讲解 | [查看文案](#s04) | 草稿／未排期 | — |
| S05 | B · AI创业与咨询 | Faster generation can come with a memory bill. | [素材](assets/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%A8%E7%90%86%E5%8A%A0%E9%80%9F1%EF%BC%9AKV%20Cache_1_Dev.E_%E6%9D%A5%E8%87%AA%E5%B0%8F%E7%BA%A2%E4%B9%A6%E7%BD%91%E9%A1%B5%E7%89%88.jpg) | [查看文案](#s05) | 草稿／未排期 | — |
| S06 | B · AI创业与咨询 | A model that runs is not yet a service that scales. | [素材](assets/AI-inference.jpeg) | [查看文案](#s06) | 草稿／未排期 | — |
| S07 | B · AI创业与咨询 | A lab leaderboard is not your product evaluation. | [素材](assets/frontier-labs.png) | [查看文案](#s07) | 草稿／未排期 | — |
| S08 | B · AI创业与咨询 | If the model improves next month, why will customers still need you? | [素材](assets/anthropic_vs_saas.jpeg) | [查看文案](#s08) | 草稿／未排期 | — |

---

## S01

**Build one useful AI workflow before collecting tools.**

An AI stack diagram can look like a shopping list for a career change. Start with one small problem instead: an assistant that answers questions about expense policies.

It needs to read the documents, find relevant passages, produce an answer, and check whether that answer is useful. Think of a small shop: supplies, shelves, staff and quality checks have different jobs.

The model is one component. You do not need every database, agent framework and monitoring tool on the diagram to build your first project.

Try ten realistic questions with expected answers. Build the simplest workflow that handles them, inspect its mistakes, and add tools when you can explain what they fix.

That is a much stronger portfolio story than a list of libraries you have tried.

Changing careers into Data Science or AI? Bring your background and a project idea, and we can discuss a practical learning plan.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#DataScience #CareerTransition #AI

---

## S02

**Forecasting starts with what you could know at the time.**

How many loaves should a bakery prepare tomorrow? That is a forecasting problem before it is a model-selection problem.

Past sales and a promotion already on the calendar can help. Tomorrow’s actual foot traffic cannot be used as if it were already known.

Time-series foundation models learn from many sequences before being applied to another forecasting task. Timestral is one example. Pretraining is a starting point, not a guarantee that it will beat a simple baseline on your data.

For a first portfolio project, compare a model with “same as last week.” Train on earlier observations and test on later ones. Repeat across several periods.

Show a forecast range as well as a central estimate. A business decision needs to account for uncertainty and the different costs of overstocking and running out.

Want to turn forecasting into a portfolio project? We can discuss the business question, baseline and evaluation design.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#DataScience #CareerTransition #AI

---

## S03

**Why an AI search system still needs keywords.**

“AX-17 error” and “When will my travel expenses be reimbursed?” ask different things of a search engine.

The first needs precise terminology. The second may need a connection to a document titled “Expense reimbursement timelines.”

Hybrid retrieval combines keyword-based and semantic search. Imagine two librarians: one looks up names and codes, the other looks for related topics.

Reciprocal Rank Fusion, or RRF, merges their ranked lists using positions rather than adding raw scores from different scoring systems. It is a way to combine candidates, not proof that the final answer is correct.

For a portfolio exercise, compare keyword, vector and hybrid search on a small set of realistic questions. Include exact codes and everyday paraphrases. Check whether the right evidence appears before evaluating the generated answer.

Building your first retrieval project? We can work through the dataset, comparison and evaluation so you can explain your choices.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#DataScience #CareerTransition #AI

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

**Faster generation can come with a memory bill.**

Imagine rewriting a report while repeatedly rebuilding your notes from the beginning. A cache lets you reuse some of that work.

A model’s KV cache stores intermediate attention data for earlier tokens. It reduces repeated computation; it is not a saved final answer.

For common full-attention implementations, longer sequences need more cache memory. Serving more simultaneous requests also adds memory pressure.

That matters to founders because “the AI is slow” can describe different experiences: waiting for the first output or waiting between later pieces of output.

Before choosing a replacement model, record input length, output length, concurrency and memory use. Separating those factors gives your team a better starting point for diagnosis than treating latency as one number.

If your AI product is hitting latency or memory limits, bring a workload description and measurements. We can discuss an architecture review and a practical investigation plan.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #AIStartups #AIConsulting

---

## S06

**A model that runs is not yet a service that scales.**

A demo feels fast with one person. Then several people arrive together and start waiting.

Think of inference serving as a restaurant kitchen. Scheduling orders, sharing preparation and managing limited space all affect the experience.

Ollama can be a useful starting point for local experiments. vLLM and SGLang are also candidates when evaluating a serving stack. Their capabilities overlap: these are not three exclusive tiers, and Ollama is not limited to one request at a time.

Compare candidates on the same workload, model and hardware, with precision settings recorded. Measure time to first output, generation speed, latency under concurrency and failures. Then consider cost per successful task.

The useful question is not “Which engine wins?” It is “Which setup meets our users’ needs with an operating burden we can sustain?”

Moving from a demo to real users? We can discuss serving options, a fair benchmark and the trade-offs behind your deployment decision.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #AIStartups #AIConsulting

---

## S07

**A lab leaderboard is not your product evaluation.**

You would not hire a restaurant chef solely on competition results. You would also ask whether they can serve your menu reliably on a busy evening.

An AI lab reputation survey can be interesting context. It is not a test of your support queue, document workflow or business assistant.

Build a small evaluation set from real tasks: common cases, awkward edge cases and outputs that must follow a format. Define success before comparing candidates.

Alongside correctness, record waiting time, failure handling and total cost per acceptable result. A cheap call that needs repeated retries may be an expensive workflow.

A useful model decision should explain both why you chose it and which jobs you would not give it. That is stronger evidence of product judgment than citing a ranking.

Choosing models for an AI product? We can discuss task-specific evaluation, failure cases and a selection process your team can explain.

[Mentoring / consulting enquiry — Jay Wang on MentorCruise](https://mentorcruise.com/mentor/jaywang/)

#AIEngineering #AIStartups #AIConsulting

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
