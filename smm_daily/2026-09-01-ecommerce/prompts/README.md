# Prompt tracking — ecommerce_ad_videos

Three `.json` files so far, one per product that has a recorded prompt, plus one `.md`:

| File | Product(s) | As-run | New prompts | Asset clearance |
|---|---|---|---|---|
| `rotation_chair.json` | ergonomic office chair | 1 free-form prompt | 8 shots → ~26s | ✅ ship |
| `beauty_cream.json` | skincare jar | 10-scene brief | 10 shots → 20s | ⛔ internal (branded) |
| `fabric_ad.json` | cotton-to-garment textile film | 1 timecoded 6-beat prompt **+ 1 partial re-gen** | 6 shots → 15s | ✅ ship |
| `ecommerce_workflow_products.md` | blender · sneakers · perfume · candle | — (new products) | 2 paragraphs + 20 scenes | ✅ all unbranded |

The `.json` files cover products that **already had** a prompt, decomposed into
per-shot H3 series. `fabric_ad.json` is the only one whose asset was generated *in this
workflow* rather than found in the folder afterwards, so it is the only one that carries a
real feedback round — the closing beat was rejected and re-run, and both the rejection and
the fix are recorded verbatim. The `.md` file covers **four new products picked from
`ecommerce_workflow`**, written in the source briefs' own two formats (paragraph for
hard goods, timecoded scene list for hero products) rather than decomposed — that folder's
29 videos are stills with caption bars, so these are the first motion prompts for it.

## Shape

Each file has the same three blocks:

- **`as_run`** — the prompt(s) that actually produced the file sitting in
  `ecommerce_ad_videos/`, verbatim. Provenance. Don't edit these; if a prompt gets
  revised, it becomes a new entry in `series`, not an overwrite here.
- **`series`** — the Minimax H3 shot list: one *single-intent* prompt per generation,
  plus `shared_style`, `negative`, and an `assembly` note.
- **`notes`** — engine caveats.

This follows the existing `segments.json` convention already used in
`ecommerce_ad_videos/popmart/`, `lego/` and `cg_hunter/` (per-scene `id` / `prompt` /
`style`), with `as_run` and clearance fields added — the first because the folder had
finished videos whose prompts weren't written down anywhere, the second because half the
folder turned out to be unpublishable and nothing recorded that.

## The counter-example: when one prompt is enough

The chair lesson below says one intent per generation. `fabric_ad` is the case that
qualifies it. Its as-run prompt is **six timecoded beats in a single 15s generation, and
all six rendered, in order, with the charcoal holding across five match cuts.** The
difference from the chair is that every beat is the *same subject under one light* —
cotton, in six states — whereas the chair's eight beats were eight different scenes
(a product, a diagram, a person working, an end card). **Decompose when the beats change
subject; a single prompt survives when they don't.**

It still needed a second pass, just not a decomposition: the closing shirt was rejected for
looking unnatural, one 4s replacement was generated, and 3.125s of it was spliced in over
the original audio bed. **One beat re-run beats fifteen seconds re-run** — and that only
works because the audio was a continuous bed with no sync points.

## The one structural lesson

The chair's `as_run` is eight scene ideas compressed into one prompt for a single 10s
clip. Three of them rendered; the human working-session beat, the skeletal diagram and
the end-card text simply didn't. That is the whole argument for the series format —
**one intent per generation, assembled in edit.** It's also why every `end_card` in
these files says to add text in post: generated on-screen type is unreliable, and in the
beauty case the overlay text is precisely where the trademark re-enters.

## Two things to verify when the API key lands

1. **Clip lengths.** Hailuo generates at 6s / 10s granularity, so the beauty brief's 2s
   beats can't map 1:1 — generate 6s and cut 2s. Confirm the exact duration and
   resolution parameters against the current API docs before hard-coding them.
2. **Camera directives.** The `[Push in]` / `[Static shot]` / `[Orbit]` brackets follow
   MiniMax's documented camera-movement convention. Check the accepted vocabulary before
   wiring this into a pipeline. If a token isn't supported it degrades to plain
   description, so the prompts are safe either way — but don't build a code path that
   assumes it works without checking.

Related: `~/curify-studio/dev/jayw/video_pipelines/ecommerce_to_video/spec.json` is the
assembly-side format for the 29 existing `ecommerce_workflow` videos (scene assets +
narration + CTA). These prompt files sit *upstream* of that — they generate the footage
that a spec like it would then assemble.
