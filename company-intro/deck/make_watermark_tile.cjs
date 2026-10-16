#!/usr/bin/env node
/**
 * Build the slanted watermark tile used by the deck's CSS.
 *
 * The house helper — curify-frontend/scripts/lib/watermark.cjs —
 * `applyTiledWatermark()` composites a slanted tiled logo ONTO an image. A deck
 * page is not an image, so this reproduces the helper's tile-construction steps
 * (resize → rotate → opacity → pad canvas) and writes the tile out on its own;
 * style.css then repeats it as a page background. Constants are imported from
 * that helper rather than copied, so the deck stays in sync with every other
 * watermarked Curify asset (logo 0.22 width, -30°, opacity 0.15, spacing 1.8).
 *
 * Usage: node make_watermark_tile.cjs
 *   -> assets/wm_tile.png        (for light pages)
 *      assets/wm_tile_dark.png   (same tile, forced white, for the navy pages)
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const FE = path.join(process.env.HOME, 'curify-frontend', 'scripts', 'lib', 'watermark.cjs');
const { DEFAULT_LOGO_PATH, TILE_DEFAULTS } = require(FE);

const OUT_DIR = path.join(__dirname, 'assets');
// A4 is 210mm wide; the helper sizes the logo at logoPct of the target width.
// At 300dpi that page is 2480px, so the logo lands at ~546px.
const PAGE_PX = 2480;
const logoPx = Math.round(PAGE_PX * TILE_DEFAULTS.logoPct);

// The helper's 0.15 is tuned for photos. On a mostly-white A4 page the mark sits
// on bare paper and competes with body text, so the deck dials it back. Logo,
// angle and spacing stay exactly as the helper defines them.
const PAGE_OPACITY = { light: 0.08, dark: 0.11 };

function buildTile(outPath, { white = false } = {}) {
  const tint = white ? '-fill white -colorize 100 ' : '';
  const opacity = white ? PAGE_OPACITY.dark : PAGE_OPACITY.light;
  execSync(
    `magick -background none "${DEFAULT_LOGO_PATH}" -resize ${logoPx}x ` +
      `-rotate ${TILE_DEFAULTS.rotate} ${tint}` +
      `-alpha set -channel A -evaluate multiply ${opacity} +channel "${outPath}"`,
    { stdio: 'pipe' }
  );
  const [w, h] = execSync(`magick identify -format "%wx%h" "${outPath}"`)
    .toString().trim().split('x').map(Number);
  const pw = Math.round(w * TILE_DEFAULTS.spacingFactor);
  const ph = Math.round(h * TILE_DEFAULTS.spacingFactor);
  execSync(
    `magick "${outPath}" -gravity center -background none -extent ${pw}x${ph} "${outPath}"`,
    { stdio: 'pipe' }
  );
  // tile width in mm, so style.css can size the background in page units
  const mm = (pw / PAGE_PX) * 210;
  console.log(`${path.basename(outPath)}  ${pw}x${ph}px  -> ${mm.toFixed(1)}mm wide`);
  return { pw, ph, mm };
}

fs.mkdirSync(OUT_DIR, { recursive: true });
const light = buildTile(path.join(OUT_DIR, 'wm_tile.png'));
buildTile(path.join(OUT_DIR, 'wm_tile_dark.png'), { white: true });
fs.writeFileSync(
  path.join(__dirname, 'wm_tile.json'),
  JSON.stringify({ widthMm: +light.mm.toFixed(2), heightMm: +((light.ph / PAGE_PX) * 210).toFixed(2) }, null, 2)
);
