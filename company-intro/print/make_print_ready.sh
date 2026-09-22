#!/bin/bash
# Curify AI · 公司介绍（客户版） -> 印刷厂版本
#
# The client PDF is printed by headless Chromium (see ../deck/build.py). Skia
# embeds PingFang SC as *Type 3* fonts, which is what the print shop saw in
# Acrobat's 文档属性 → 字体 and why they asked for 转曲 (create outlines).
#
# Two things matter here:
#   -dNoOutputFonts  converts every glyph to a vector path (the 转曲 itself)
#   -dNOCACHE        without it Ghostscript's glyph cache silently rasterises a
#                    handful of CJK glyphs to 720dpi 1-bit stencils instead of
#                    outlining them — and a *different* handful on every run.
#
# Images are passed through untouched (-dPassThroughJPEGImages, no downsampling)
# so outlining costs nothing in image quality.
#
# Outputs, both with zero embedded fonts:
#   Curify_AI_公司介绍_客户版_转曲_A4.pdf        210 x 297mm, no bleed
#   Curify_AI_公司介绍_客户版_转曲_出血3mm.pdf   216 x 303mm, 3mm bleed all round
#
# The bleed pass CROPS 1.5pt off each edge before it pads (see step 3a). Without
# that crop the Chromium page-edge artifacts end up 3mm inside the sheet, right
# on the new trim line, and print as a dark hairline frame — the 黑边 the shop
# would have called back about.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="${1:-$HERE/../Curify_AI_公司介绍_客户版.pdf}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

COMMON=( -sDEVICE=pdfwrite
         -dPassThroughJPEGImages=true
         -dDownsampleColorImages=false -dDownsampleGrayImages=false -dDownsampleMonoImages=false
         -dAutoFilterColorImages=false -dAutoFilterGrayImages=false
         -dCompatibilityLevel=1.4 -dPrinted=true )

echo "1/3  转曲 (text -> outlines)"
gs -o "$WORK/outlined.pdf" "${COMMON[@]}" -dNoOutputFonts -dNOCACHE "$SRC" >/dev/null

echo "2/3  normalise to exact A4 (Chromium emits 210.2 x 297.3mm)"
gs -o "$HERE/Curify_AI_公司介绍_客户版_转曲_A4.pdf" "${COMMON[@]}" \
   -dFIXEDMEDIA -dDEVICEWIDTHPOINTS=595.276 -dDEVICEHEIGHTPOINTS=841.890 -dPDFFitPage \
   "$WORK/outlined.pdf" >/dev/null

echo "3/3  3mm bleed"
# Every page background is a flat colour (--navy / --cream / --paper), verified
# against the rendered corners, so the bleed is just that colour extended.
# One gs pass per page: gs does not increment the /BeginPage page counter
# reliably here, so the colour has to be a constant per pass, not an index.
COLS=( "0.06275 0.12157 0.23529" "0.96863 0.95686 0.92549" "1 1 1" \
       "0.96863 0.95686 0.92549" "1 1 1" "0.96863 0.95686 0.92549" \
       "1 1 1" "0.96863 0.95686 0.92549" "0.06275 0.12157 0.23529" )

# 3a. TRIM 1.5pt OFF EVERY EDGE FIRST — this is what removes the 黑边.
#     Chromium's printed page is not clean at its own edge: on every page it
#     leaves a 1px #6B6B76 rule along the bottom, a blend/rule + ~2px unpainted
#     white along the right, and ~3px unpainted white along the top (measured at
#     300dpi on all 9 pages of the source). At A4 those artifacts sit exactly ON
#     the cut line, so the guillotine eats them and nobody ever sees them.
#     Add bleed by centring the same page on a bigger sheet and they move 3mm
#     INSIDE the sheet — i.e. onto the new trim line — and print as a dark
#     hairline frame around the finished piece. Padding cannot fix that; the
#     artifact has to be cut off before the padding goes on.
#     1.5pt (0.53mm) is ~2x the widest artifact (3px@300dpi = 0.72pt). pdfwrite
#     clips to the fixed media, so a smaller media + negative PageOffset is a crop.
#     Safe because every page edge is flat colour — the bleed fill repaints it.
INSET=1.5
PARTS=()
for i in $(seq 1 9); do
  gs -o "$WORK/crop_$i.pdf" "${COMMON[@]}" -dFirstPage=$i -dLastPage=$i \
     -dFIXEDMEDIA -dDEVICEWIDTHPOINTS=592.276 -dDEVICEHEIGHTPOINTS=838.890 \
     -c "<< /PageOffset [-$INSET -$INSET] >> setpagedevice" \
     -f "$HERE/Curify_AI_公司介绍_客户版_转曲_A4.pdf" >/dev/null
  # 3b. re-centre on the 216x303mm sheet and flood the whole sheet with the page
  #     colour underneath. Offset 10.00394 = 8.50394 (3mm) + 1.5 (the inset),
  #     so the artwork lands in exactly the same place it had before the crop.
  gs -o "$WORK/bp_$i.pdf" "${COMMON[@]}" \
     -dFIXEDMEDIA -dDEVICEWIDTHPOINTS=612.283 -dDEVICEHEIGHTPOINTS=858.898 \
     -c "<< /PageOffset [10.00394 10.00394] /BeginPage { pop gsave ${COLS[$((i-1))]} setrgbcolor -40 -40 700 940 rectfill grestore } >> setpagedevice" \
     -f "$WORK/crop_$i.pdf" >/dev/null
  PARTS+=("$WORK/bp_$i.pdf")
done
gs -o "$HERE/Curify_AI_公司介绍_客户版_转曲_出血3mm.pdf" "${COMMON[@]}" \
   -dFIXEDMEDIA -dDEVICEWIDTHPOINTS=612.283 -dDEVICEHEIGHTPOINTS=858.898 "${PARTS[@]}" >/dev/null

echo "done:"
for f in "$HERE"/Curify_AI_公司介绍_客户版_转曲_*.pdf; do
  printf '  %-52s %s  fonts=%s\n' "$(basename "$f")" \
    "$(pdfinfo "$f" | awk '/Page size/{print $3"x"$5"pt"}')" \
    "$(pdffonts "$f" | tail -n +3 | grep -c . || true)"
done
