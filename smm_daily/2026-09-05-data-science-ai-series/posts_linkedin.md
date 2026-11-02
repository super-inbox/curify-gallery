# Data Science × AI｜LinkedIn · Jay

S09 added 2026-11-02. Draft only; not scheduled or published. This file records LinkedIn status independently of Facebook. Earlier series posts have not been inferred to be LinkedIn posts.

## Publication Sequence

| ID | Audience | Topic | Copy | Status | Publication date / URL |
|---|---|---|---|---|---|
| S09 | Multimodal researchers, training-data leads, dataset QA and data sourcing teams | 3D reconstruction, design-task trajectories and evaluation data | [Draft](#s09) | Draft / unscheduled | — |

## S09

**Working on training or evaluation data for multimodal models or AI agents? I’d love to compare notes.**

We’ve been working on video-to-3D reconstruction and a design benchmark, and I’m interested in connecting with teams that need data capturing both an outcome and the process behind it.

The attached video is one example: original footage paired with our simplified, editable 3D animation. We’re refining motion, timing, camera alignment, and occlusion. It’s a short prototype demonstration, not a finished training dataset.

More broadly, we’re exploring:

• Paired video and 3D reconstructions, with motion trajectories and scene structure.
• Design-task trajectories: briefs, observable tool actions, intermediate artifacts, revisions, and final outputs.
• Evaluation cases and quality checks that capture whether a task meets its requirements.

I’d like to hear from researchers, engineers, data leads, and data sourcing teams working on multimodal LLMs, video or spatial understanding, and agents that use creative tools.

What data is difficult for your team to obtain? What would make it usable—specific annotations, action traces, temporal precision, coverage of failure cases, or a particular evaluation protocol?

If there’s a concrete fit, I’d be happy to discuss a small pilot using material you’re authorized to share, with an agreed data format and acceptance criteria. We’re still validating these workflows and haven’t established a model-training benefit.

If this is relevant to your work, please message me. Introductions to people who define or source this kind of data would also be very welcome.

#MultimodalAI #TrainingData #AIAgents

## S09 editorial notes

- Network-facing demand discovery and pilot discussion, not a claim of a validated training dataset or proven model improvement. Covers multimodal/video/spatial work and observable design-agent task trajectories. Trajectories mean tool actions, artifacts and revisions, not private chain-of-thought. Motion trajectories and agent task trajectories are separate data types.
- [Selected 3D reconstruction video](../../drama_animation/white-model-reconstruction-2026-11-02/source-vs-white-model-v14.mp4) · [Source and scope](../../drama_animation/white-model-reconstruction-2026-11-02/README.md). Two excerpts, 78 frames, 3.12 seconds; not a full reconstruction. Visual acceptance remains incomplete. Current video carries Souvenir Video branding and is reused as a candidate asset, not a new series-specific export.
- User selected the existing 3D reconstruction comparison as the attachment on 2026-11-02. Preserve its excerpt/prototype framing; it illustrates the reconstruction work, not a design-agent trajectory demo. Media selection is not a claim of completed visual acceptance, dataset licensing, or demonstrated training utility. No platform publication has been performed.
- Do not include private per-second quotes, subcontracting details, or ByteDance/Baidu names; no customer relationship or endorsement is established.
- CTA is a direct message or an introduction to a person responsible for the data requirement. No MentorCruise link for this data-sourcing post.
- Facebook adaptation: [S09](posts_fb.md#s09). Both remain drafts; no platform posting or outreach has been performed.
