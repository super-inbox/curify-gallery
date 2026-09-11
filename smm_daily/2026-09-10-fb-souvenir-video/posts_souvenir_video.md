# Souvenir video — SMM thread (2026-09-10)

_The third product line. `smm_daily` already has threads for ecommerce
(`2026-09-01-ecommerce`) and retouching
(`2026-09-01-retouching` — `posts_fb.md` and `posts_rednote.md`); this opens the missing one._

**Offer:** a visitor's photo becomes a 20–30s cinematic souvenir video — sold as an add-on to a photo
package that already exists, with no second shoot.
**CTA:** DM, or WhatsApp **+86 176 9219 0183**.

## The one rule that decides whether this works

**The demo must be of the place the group is about.** A Kyoto video posted into a Bali group is the
generic pitch this whole design exists to avoid — the entire advantage is that the viewer recognises
their own location before reading a word.

## Assets

| Destination | File | Status |
|---|---|---|
| Kyoto / kimono | `cultural_videos/kyoto/kyoto-kimono-30s-watermarked.mp4` (30MB) | ✅ ready |
| China heritage (滕王阁) | `cultural_videos/tengwangge/tengwangge-30s-preview-watermarked.mp4` (22MB) | ✅ ready |
| — compressed for email | `client_VC_portfolio/tourism-souvenir-demo-09-08/tengwangge-30s-souvenir-preview.mp4` (3MB) | ✅ |
| **Bali** | `cultural_videos/bali/bali-resort-30s-watermarked.mp4` (26MB, 1080x1920) | ✅ **built 2026-09-10** |
| — compressed for email | `client_VC_portfolio/tourism-souvenir-demo-09-08/bali-30s-souvenir-preview.mp4` (3.5MB) | ✅ |
| Dubai / desert | `cultural_videos/dubai/dubai-desert-30s-watermarked.mp4` (21MB) | ✅ built 09-10 |
| Santorini | — | ❌ |

✅ **The Bali gap is closed (2026-09-10).** Four Bali photographers are tracked in
`relationship_leads.json` and one was already DM'd about this offer with nothing to show; there is now
a Bali demo for that conversation.

Built through `dev/jayw/video_pipelines/costume_story_video/projects/bali-resort/` — an original
character look-locked from a costume sheet, 11 shots (cliff sunrise → temple gate → rice terrace →
water temple → jungle swing → beach → frangipani courtyard → ocean pool → cliff temple → sunset
shoreline → last light), exactly 30.0s at 9:16. No real person, no real resort or brand mark, and
every sign left blank by instruction.

⚠️ **Music is a neutral placeholder** (`leberch-travel`). It is deliberately NOT the Kyoto track
(Japanese) or the Tengwangge cue (guzheng) — either reads as the wrong country — but it was chosen for
neutrality, not because it is the right piece of music. Swap it before this becomes the flagship.

The costume try-on library is **Chinese costumes only**. Extending it — kimono, abaya, Greek, Balinese
— is what unlocks destinations beyond the two we have.

## Groups, by destination × tourism trade

Not generic travel groups. Buyers cluster by place and by trade:

- **Kyoto:** `Kyoto photographers`, `Japan photographers`, `Kimono photographers`,
  `Kyoto wedding photographers`, `Japan tour operators`
- **Bali:** `Bali photographers`, `Bali wedding photographers`, `Bali expats & business owners`,
  `Bali villa & tour operators`
- **Dubai:** `Dubai photographers`, `Dubai desert safari operators`, `UAE luxury travel`
- **China:** `Hanfu photography`, `China travel photographers`, regional tour-operator groups

## Post

> **For photographers in Kyoto — what if every kimono session also came with a 30-second cinematic
> souvenir video?**
>
> We made this from a single portrait. No second shoot — it can be sold as an add-on to the package
> you already offer.
>
> If you run photo experiences in Kyoto, I'll make one free sample from one of your photos.
> DM me, or WhatsApp +86 176 9219 0183.

Swap the place name and the video together — never one without the other.

## ⚠️ What must not be claimed

The **only closed deal** in this vertical (client-007, ¥27,800) was **文创 merchandise, not video**,
and `gtm-progress.md` rates that shape low-repeat / high-manufacturing-risk / 做完案例不复制.

So: **no attraction or photographer has bought this format.** Present the videos as examples of the
format. Do not imply a client engagement, and do not name one.

## Log

Same five columns as the other channels, into `gtm_tools/outreach_denominator.csv`:

```
date | group | members | demo | views | comments | DMs | samples | paid
```

Stop and evaluate per cell rather than per channel. The question is whether
`destination photographer × souvenir video` converts, not whether "Facebook works".
