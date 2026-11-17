# Production record · 2026-10-29

## Creative and asset provenance

Fifteen new vertical first frames generated with the built-in imagegen tool. One original adult female character, dark olive studio, full-length framing and soft cinematic light establish the common visual language. Subsequent images use the first 1900 frame as identity/composition reference. Original tool outputs remain in the Codex generated-images directory; all selected frames are copied into Gallery `cultural_videos/costume_tryon/2026-10-29-fashion-through-time/frames/`.

[Prompt specification](image-prompts.md) records the common constraints and per-era wardrobe direction. No external museum photograph, celebrity likeness or reference video's soundtrack was used in generation. Garments and hairstyles are interpretations; details are not presented as scholarly reconstructions.

Dynamic footage: 15 successful MiniMax-Hailuo-2.3 image-to-video tasks, requesting six seconds and 1080P. Uses the existing CN API helper in `curify-studio/dev/jayw/video_pipelines/costume_story_video/animate.py`. Task IDs, motion prompts and download statuses live in [motion-jobs.json](../../../cultural_videos/costume_tryon/2026-10-29-fashion-through-time/motion-jobs.json); credentials are not stored. [animate_batch.py](../../../cultural_videos/costume_tryon/2026-10-29-fashion-through-time/animate_batch.py) resumes recorded jobs and does not automatically resubmit ambiguous/failed submissions.

## Editorial choices

Each film contains five continuous moving clips with matching cuts, six seconds each. Raw outputs are about six seconds; their actual duration is read and motion is retimed slightly to exactly six seconds. No still-image pan/zoom substitute is used. Clips are composed within a dark editorial frame, leaving space for captions without obscuring face, hands or garment outline. English/Chinese text and era progress are typeset deterministically with Arial, Georgia and STHeiti, not generated in the garment images.

- H1: c.1900 / 1925 / 1950 / 1975 / 2000.
- H2: c.1550 / 1750 / 1810 / 1860 / 1950. “400 years” matches the selected 1550–1950 range, instead of claiming full coverage beginning in 1500.
- H3: c.1920 / 1950 / 1980 / 2000 / 2020. Selected white-bridalwear fashions only, not a global or universal wedding history.

All outputs omit brand watermarks and advertising end cards, following the existing RedNote no-ending convention. Service CTAs stay in platform-specific copy. No voiceover: music and bilingual labels carry the visual sequence.

Music: existing Gallery `assets/music/alexgrohl-sweet-life-luxury-chill-438146.mp3`, excerpt beginning at 8 seconds. Same track across the batch reduces music variation during topic exploration. AAC 192kbps / 48kHz; loudness filter targets -16 LUFS and -1.5dBTP; final 1.5-second fade. This pass reuses the established local music library and does not claim a fresh license audit.

[build.py](../../../cultural_videos/costume_tryon/2026-10-29-fashion-through-time/build.py) reproduces editing, overlays, soundtrack mix, covers, inspection sheets and ffprobe reports. Raw generation clips and intermediate edits are retained under the asset directory.

## Historical reference boundaries

Sources consulted 2026-10-29 to ground silhouette vocabulary, not to copy objects. The generated garments combine styling references and do not reproduce one catalogued garment.

- [FIT: 1550–1559](https://fashionhistory.fitnyc.edu/1550-1559/): Renaissance-period context; H2 starts with Italian-inspired rich sleeves and fitted bodice.
- [The Met: robe à l’anglaise](https://www.metmuseum.org/art/collection/search/81529): eighteenth-century open gown/petticoat context. The H2 1750 frame is a broader Rococo interpretation, not this later dated object or an asserted exact match.
- [The Met: evening dress, 1810–12](https://www.metmuseum.org/art/collection/search/157539) and [NGV: Regency fashion](https://www.ngv.vic.gov.au/explore/collection/collection-on-display/regency-fashion/): high-waisted classical silhouette.
- [Reading Museum dress collection note](https://collections.readingmuseum.org.uk/pdfs/H60A.pdf): broad crinoline-supported skirt context around the mid-nineteenth century.
- [FIT: 1900–1909](https://fashionhistory.fitnyc.edu/1900-1909/) and [FIT: 1970–1979](https://fashionhistory.fitnyc.edu/1970-1979/): period framing for H1.
- [FIT: 1950–1959](https://fashionhistory.fitnyc.edu/1950-1959/): fitted-waist/full-skirt silhouette, alongside other contemporary shapes. Not all 1950s clothes used that silhouette.
- [V&A: shopping for the dress](https://www.vam.ac.uk/articles/shopping-for-the-dress), [V&A: four wedding dresses](https://www.vam.ac.uk/articles/dresses-of-character), [V&A wedding dress collection](https://www.vam.ac.uk/collections/wedding-dress): variation within British bridalwear and specific period examples. The 1980/2000/2020 frames are broad style interpretations, not claims that these were the sole or statistically dominant fashions.

## QA and publication

First frames visually reviewed for character continuity and distinct silhouettes. Final review uses two frames per era (1/4, 7/10, 13/16, 19/22, 25/28 seconds) to inspect motion, hands, costume stability and bilingual layout. Full FFmpeg decode plus ffprobe verifies each final deliverable; individual reports and contact sheets accompany the batch.

No social publishing, scheduling, account changes or messaging performed. H1–H3 are new local Facebook/RedNote drafts; parent historical publication confirmations do not apply to them. No commit/push performed for this batch unless separately recorded.
