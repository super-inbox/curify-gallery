# Data Science × AI｜LinkedIn · Jay

S09 added 2026-11-02. Draft only; not scheduled or published. This file records LinkedIn status independently of Facebook. Earlier series posts have not been inferred to be LinkedIn posts.

## Publication Sequence

| ID | Audience | Topic | Copy | Status | Publication date / URL |
|---|---|---|---|---|---|
| S09 | Multimodal researchers, training-data leads, dataset QA and data sourcing teams | 3D reconstruction, design-task trajectories and evaluation data | [Draft](#s09) | Draft / unscheduled | — |
| S17 | Experienced DS / career transitions | What does a data scientist actually want to leave? | [Draft](#s17) | Draft / unscheduled | — |
| S18 | Early-career practitioners / engineering leads | Designing how juniors learn when AI handles routine tasks | [Draft](#s18) | Draft / unscheduled | — |

## S09

**Training or evaluation data for multimodal AI or agents**

At Curify, we’re exploring video-to-3D pairs, motion trajectories, and design-task traces—from briefs and tool actions to revisions and final outputs.

The attached clip compares source footage with simplified 3D reconstruction. These paired examples could support research in motion understanding, spatial reasoning, and camera tracking, or serve as evaluation cases for video and 3D models.

I’d love to hear what data your team struggles to source and what quality standards matter. We’re open to small pilots using authorized material and agreed acceptance criteria.

DM me—or introduce me to someone in your network working on these needs.

#MultimodalAI #TrainingData #AIAgents

## S09 editorial notes

- Network-facing demand discovery and pilot discussion, not a claim of a validated training dataset or proven model improvement. Covers multimodal/video/spatial work and observable design-agent task trajectories. Trajectories mean tool actions, artifacts and revisions, not private chain-of-thought. Motion trajectories and agent task trajectories are separate data types.
- [Selected 3D reconstruction video](../../drama_animation/white-model-reconstruction-2026-11-02/source-vs-white-model-v14.mp4) · [Source and scope](../../drama_animation/white-model-reconstruction-2026-11-02/README.md). Two excerpts, 78 frames, 3.12 seconds; not a full reconstruction. Visual acceptance remains incomplete. Current video carries Souvenir Video branding and is reused as a candidate asset, not a new series-specific export.
- User selected the existing 3D reconstruction comparison as the attachment on 2026-11-02. Preserve its excerpt/prototype framing; it illustrates the reconstruction work, not a design-agent trajectory demo. Media selection is not a claim of completed visual acceptance, dataset licensing, or demonstrated training utility. No platform publication has been performed.
- Do not include private per-second quotes, subcontracting details, or ByteDance/Baidu names; no customer relationship or endorsement is established.
- CTA is a direct message or an introduction to a person responsible for the data requirement. No MentorCruise link for this data-sourcing post.
- Facebook adaptation: [S09](posts_fb.md#s09). Both remain drafts; no platform posting or outreach has been performed.


---

## S17

**When a data scientist says “I want to leave,” I first ask what they want to stop doing.**

Around 2019–2020, the conversation I remember was largely about entering the field. Data science retained the “sexiest job” reputation dating back to 2012. People moved from finance and other disciplines, sometimes from the East Coast to the West Coast. Interdisciplinary training programmes attracted substantial investment from students who saw a growing career opportunity.

Over the past four or five years, I have encountered more conversations about moving elsewhere: AI engineering, finance, biostatistics, or data work outside the tech industry. This is a professional observation, not evidence of a measured net exodus.

The distinction that matters in coaching is the reason behind the move.

**1. Responsibility without enough ownership.**
A DS may produce the evidence while stakeholders retain control of the question, the decision, and implementation. For someone who wants to own outcomes, years of advisory work can become frustrating. Before recommending a career change, I would examine whether another role could give them responsibility from problem definition through implementation and measurement.

**2. A deliberate move into AI.**
Some people want to apply their data and modelling background to building AI systems. This is an expansion of their work, with a concrete skills gap to address. The relevant question is which systems they want to build and what competence those systems require.

**3. A different relationship with work.**
Tech layoffs and organisational instability can change what someone values in an employer. Moving into another industry may preserve the technical work they enjoy. It still requires examining domain knowledge, daily responsibilities, and the actual conditions of the role.

“Leaving data science” can describe all three. They call for different plans: a change in ownership, a technical transition, or a change of employment environment.

In a career conversation, I would start by identifying which problem the proposed move is supposed to solve.

For a discussion of your own options:
https://mentorcruise.com/mentor/jaywang/

#DataScience #CareerDevelopment #AIEngineering

---

## S18

**When AI takes over routine tasks, teams need to be deliberate about how juniors learn.**

A beginner needs opportunities to make a decision, see its consequences, and receive a useful correction. Waiting for a suitable ticket to appear is only one way to provide that.

I would build a learning path around three settings.

**Simulation: practise the situations you cannot safely manufacture in production.**
The analogy is pilot training. In a controlled data or engineering exercise, introduce missing inputs, leakage, changed data distributions, or a failing dependency. Ask the learner to explain a diagnosis before attempting a fix, then compare the outcome with verified expectations.

AI can vary the scenario and ask follow-up questions. Someone still has to check that the exercise is valid and that the feedback is correct.

**Real work: encounter constraints that someone else cares about.**
A startup project or internship can expose a learner to changing requirements, imperfect data, and handoffs to real users. I have also seen unpaid internships used for this purpose. The attraction is understandable when a team has limited funding and a learner wants experience, but the educational value must be real: an accountable supervisor, bounded tasks, regular reviews, and clear terms. Compensation, duration, and permission to show the work need discussion; any unpaid arrangement must comply with the applicable rules.

**Mentorship: identify what the learner cannot yet diagnose alone.**
Feedback should name a specific gap: an assumption they missed, an experiment they misread, or a trade-off they cannot explain. That gap becomes the next practice task.

In my data science, AI, and deep learning coaching, the format depends on the person. An AMA-style session may clarify direction. Guided reading and experiment reviews can deepen a topic. Ongoing project mentorship provides a closer feedback loop.

The goal is to build judgment through progressively more demanding work, with someone checking whether that judgment is improving.

If you are developing your own experience—or thinking about how your team trains newcomers—let’s discuss the learning path:
https://mentorcruise.com/mentor/jaywang/

#EngineeringLeadership #AI #Mentorship
