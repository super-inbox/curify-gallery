# Minimax H3 prompts — 4 products from `ecommerce_workflow`

Written in the two formats from the source briefs: the **paragraph** form (chair) for
hard goods where the story is mechanism, and the **timecoded scene list** form (beauty
cream) for hero products where the story is surface and light.

## Why these four

`ecommerce_workflow` holds 26 distinct products. The 29 videos there are **stills with
caption bars** — `棚拍主图 / 瓶身细节 / 梳妆场景`, a slideshow. Nothing in that folder
moves. So the pick isn't "which products are nicest", it's **which four cover the most
distinct motion problems**, so the prompt library ends up with four techniques rather
than four variations of one.

| Product | Motion problem it solves | Format | Why not something else |
|---|---|---|---|
| **Blender** | Transformation — ingredients becoming a different substance | paragraph | The only product in the catalog whose *process* is the selling point |
| **Sneakers** | Material under load + human motion | paragraph | Apparel's real problem is how fabric behaves, which stills cannot show |
| **Perfume** | Glass, refraction, liquid | timecoded | Different render problem from the opaque cream jar — refraction, not surface |
| **Candle** | Making the invisible visible — flame, warmth, scent | timecoded | Same class as the chair's airflow shot, and it **replaces `oilight`**, which is blocked on client clearance |

Deliberately skipped: coffee / tea / fruit_drinks (`matcha_drink` already covers
beverage), skincare / serum (too close to `beauty_cream`), camera / earbuds / speaker /
game_stick (all the same "small black object with a detail macro" problem — one of them
would do, none is urgent).

All four are unbranded generic products. No IP exposure, unlike four of the ten in
`ecommerce_ad_videos`.

---

## 1. Blender — paragraph form

> 360° display of a matte-black high-performance countertop blender in a bright modern kitchen. Close-up of the stainless steel blade assembly spinning up to full speed. Strawberries, banana slices and ice cubes falling into the glass pitcher in slow motion. A vortex forming as the mixture turns from chunky to completely smooth. Macro of the finished smoothie pouring into a tall glass, thick and glossy, folding over itself. Engineering animation of motor torque and blade geometry, luminous overlay lines. A hand pressing the control dial, the LED readout stepping up in response. Morning-routine scene — someone lifting the glass from the counter, kitchen window light behind them. Ends with the text "Whole Ingredients, Perfectly Broken Down" fading in. Clean bright kitchen aesthetic, warm neutral tones, crisp product-film lighting, slow deliberate camera work.

**Note:** the vortex beat is the one to spend seeds on — a blend turning from chunky to
smooth in one continuous shot is the entire product claim, and it's the hardest thing
here to get without the liquid tearing.

---

## 2. Sneakers — paragraph form

> 360° display of a white knit-upper running sneaker on a seamless light-grey studio floor. Macro of the woven knit texture flexing and relaxing. Cutaway animation of the midsole foam compressing under load and rebounding, luminous energy-return lines tracing through the sole stack. Close-up of the outsole tread pressing into wet pavement, water displacing around the lugs. A runner mid-stride on a city street at dawn, foot striking and rolling through to toe-off in slow motion. Slow-motion detail of the heel counter and laces under tension. Product hero on a raw concrete plinth, soft directional daylight. Ends with the text "Built to Return Every Step" fading in. Clean athletic aesthetic, cool daylight tones, high-contrast product lighting, slow deliberate camera work.

**Note:** keep the runner shot framed below the knee. Feet and shoes are reliable;
faces bring in the likeness question for no benefit here.

---

## 3. Perfume — timecoded scene form

Scene 1 (0:00 - 0:02): Faceted clear glass perfume bottle amidst drifting golden light and slow-moving sheer silk. 3D high-end fragrance ad.

Scene 2 (0:02 - 0:03): Close-up pan across the polished gold cap and the bottle's cut crystal edges. Sharp refractive highlights travelling across the facets.

Scene 3 (0:03 - 0:05): Bottle centered on a still black reflective water surface. Concentric ripples spreading outward, warm rim light.

Scene 4 (0:05 - 0:07): Floating bottle in a warm amber void. Golden light trails, suspended dust motes, soft bokeh.

Scene 5 (0:07 - 0:09): Bottle on a brushed brass podium. Amber liquid refracting light through the glass, a slow caustic pattern moving across the surface behind it.

Scene 6 (0:09 - 0:11): Macro of amber fragrance liquid swirling and folding, glossy and viscous, catching light at the edges.

Scene 7 (0:11 - 0:13): A woman's wrist, close, as she touches the applicator to her pulse point and lowers her hand. Natural window light, warm neutral interior.

Scene 8 (0:13 - 0:15): Bottle resting among white ranunculus and eucalyptus on a marble vanity. Soft floating petals, warm side light.

Scene 9 (0:15 - 0:17): Bottle on a clear glass podium, backlit by strong low sunbeams that burst around its silhouette and throw refracted light across the frame.

Scene 10 (0:17 - 0:20): Packshot of the bottle on a reflective warm-stone surface, generous empty space above for text.

**Note:** glass is the whole difficulty. Refraction and caustics are where these break —
expect more seeds than the cream jar needed. Keep the cap **unengraved**: generated
lettering fails at macro scale, and text composited in post is both cleaner and the
thing that keeps a house name out of trademark territory.

---

## 4. Candle — timecoded scene form

Scene 1 (0:00 - 0:02): Ribbed amber glass candle vessel in soft shadow, a single flame igniting and settling. Warm cinematic product ad.

Scene 2 (0:02 - 0:03): Extreme close-up of the flame, wick glowing, the melt pool beginning to form and catch light.

Scene 3 (0:03 - 0:05): Candle on a dark wood side table beside a folded linen throw, warm light pooling outward across the grain.

Scene 4 (0:05 - 0:07): Macro of a thin ribbon of smoke rising and curling slowly through a dark frame, backlit, dissolving at the top.

Scene 5 (0:07 - 0:09): Translucent warm-toned scent trails drifting outward from the vessel into the surrounding air, soft and luminous.

Scene 6 (0:09 - 0:11): Macro of the wax surface, molten and glossy at the centre, matte and solid toward the rim.

Scene 7 (0:11 - 0:13): A hand lifting the wooden lid from the vessel and setting it down beside it. Evening interior, low warm light.

Scene 8 (0:13 - 0:15): Wide shot of a dim living room at dusk, the candle the only light source, soft glow falling on a sofa arm and a stack of books.

Scene 9 (0:15 - 0:17): Candle on a stone ledge, backlit by low golden window light, warm rim glow around the ribbed glass.

Scene 10 (0:17 - 0:20): Packshot of the vessel on a warm neutral surface, flame steady, generous empty space above for text.

**Note:** scenes 4 and 5 are the reason to make this one. Smoke and scent-trail are the
same problem as the chair's airflow — an invisible product benefit that photography
cannot reach and that a 3D artist normally quotes for. This is also the unblocked
stand-in for `oilight`.

---

## Production notes

Same two caveats as the other files:

- **Clip length.** Hailuo generates at 6s / 10s granularity, so the 2s beats above don't
  map 1:1 — generate each at 6s and cut the best 2s. The paragraph prompts are written
  as single dense briefs to match the source format, but the chair's `as_run` showed
  what happens when eight ideas share one 10s clip: three render, five don't. **Split
  each paragraph into its sentences and generate one per shot.**
- **On-screen text.** Both "Ends with the text …" lines and the packshot overlays go in
  post. Generated type is unreliable, and it's where a brand name would re-enter.

Confirm duration and resolution parameters against the MiniMax API docs when the key
lands rather than trusting these numbers in code.
