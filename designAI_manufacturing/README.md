# designAI_manufacturing

Reference material and worked cases for the design-AI → manufacturing track.

- **top level** — design-AI reference: the designer AI-workflow infographic (and its post
  context), the design-tool agent API / maturity matrix, the design-agent research brief,
  and the Curify "agent managing design tools" poster.
- **`3D-mockup/fortune-box/`** — dieline → folded 3D mockup (仁寿 gift box, 117 × 114 × 39 mm).
- **`sticker-print/`** — die-cut sticker production packages as emitted by
  `design-agent-v0/factory/sticker_exporter.py`
  (`01_artwork` / `02_cutline` / `03_artwork_cmyk` / `04_preview` / `05_spec`).
- **`*/xhs/`** — RedNote cards (CN + EN) + captions, with the generator script beside them.

## Publishing rules — this repo is public

- **No client production vector files.** `*.ai` is gitignored under this folder. Note that an
  overlay drawn on a PDF/AI is *not* a redaction: the text layer underneath stays extractable
  with `pdftotext`. Publish a flattened raster with the identifying block mosaicked instead —
  e.g. `3D-mockup/fortune-box/仁寿盒-刀版展开图-脱敏.png`, where the commissioning company,
  address and barcode are masked.
- **Third-party handles are masked** in screenshots of other people's posts.
