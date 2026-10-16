#!/usr/bin/env python3
"""Overlay / graphic generation for the Curify founder-vision LinkedIn cut."""
import os, math, glob, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gfx")
os.makedirs(OUT, exist_ok=True)

INTER = "/Users/qqwjq/curify-frontend/public/fonts/Inter-Bold.ttf"
HELV = "/System/Library/Fonts/HelveticaNeue.ttc"

def bold(sz):  return ImageFont.truetype(INTER, sz)
def reg(sz):   return ImageFont.truetype(HELV, sz, index=0)
def light(sz): return ImageFont.truetype(HELV, sz, index=5)

BG       = (10, 12, 18)
INK      = (12, 14, 20)
WHITE    = (255, 255, 255)
MUTED    = (138, 147, 166)
VIOLET   = (87, 0, 255)
BLUE     = (0, 79, 255)
LAYERS = [
    dict(num="01", name="PRODUCTION AI",         keys="Ship · Scale · ROI",              accent=(46, 123, 255)),
    dict(num="02", name="WORKSPACE INTELLIGENCE", keys="Capture · Reuse · Personalize",  accent=(123, 77, 255)),
    dict(num="03", name="FRONTIER RESEARCH",      keys="Explore · Evaluate · Invent",     accent=(194, 77, 255)),
]

# ---------------------------------------------------------------- helpers
def new_rgba(color=(0, 0, 0, 0)):
    return Image.new("RGBA", (W, H), color)

def vgrad(size, top, bottom):
    """Vertical gradient as an RGBA image (top/bottom are RGBA tuples)."""
    w, h = size
    g = Image.new("RGBA", (1, h))
    px = g.load()
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(4))
    return g.resize((w, h))

def scrim(img, height, at_top=True, strength=210):
    """Paste a fade-to-dark scrim at the top or bottom edge."""
    if at_top:
        g = vgrad((W, height), (0, 0, 0, strength), (0, 0, 0, 0))
        img.alpha_composite(g, (0, 0))
    else:
        g = vgrad((W, height), (0, 0, 0, 0), (0, 0, 0, strength))
        img.alpha_composite(g, (0, H - height))

def brand_bg():
    """Near-black canvas with a soft violet→blue glow."""
    img = Image.new("RGBA", (W, H), BG + (255,))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    d.ellipse([-380, -520, 760, 620], fill=VIOLET + (70,))
    d.ellipse([420, H - 640, W + 420, H + 380], fill=BLUE + (58,))
    glow = glow.filter(ImageFilter.GaussianBlur(190))
    img.alpha_composite(glow)
    return img

def curify_mark(size=44):
    """The Curify play-mark, drawn from the logo geometry."""
    s = size * 4
    m = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(m)
    r = s * 0.5
    pad = s * 0.06
    d.rounded_rectangle([pad, pad, s - pad, s - pad], radius=r * 0.72,
                        outline=VIOLET + (255,), width=int(s * 0.085))
    d.arc([pad, pad, s - pad, s - pad], 180, 360, fill=BLUE + (255,), width=int(s * 0.085))
    cx, cy, t = s * 0.5, s * 0.5, s * 0.20
    d.polygon([(cx - t * 0.62, cy - t), (cx - t * 0.62, cy + t), (cx + t * 0.78, cy)],
              fill=(28, 30, 40, 255))
    return m.resize((size, size), Image.LANCZOS)

def wordmark(height=40, color=(255, 255, 255)):
    """Curify play-mark + 'Curify' wordmark on one baseline."""
    mark = curify_mark(height)
    f = bold(int(height * 0.92))
    txt = "Curify"
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bb = tmp.textbbox((0, 0), txt, font=f)
    gap = int(height * 0.30)
    img = Image.new("RGBA", (height + gap + bb[2] - bb[0], height), (0, 0, 0, 0))
    img.alpha_composite(mark, (0, 0))
    ImageDraw.Draw(img).text((height + gap - bb[0], (height - (bb[3] - bb[1])) // 2 - bb[1]),
                             txt, font=f, fill=color + (255,))
    return img

def ladder_icon(active, w=104, h=64, dim=(90, 96, 118)):
    """Three ascending rungs; the active one lit in its layer accent."""
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    bh = 9
    for i in range(3):
        y = h - (i + 1) * (h // 3) + (h // 3 - bh) // 2
        x0 = i * (w * 0.16)
        x1 = x0 + w * 0.62
        lit = (i == active)
        col = LAYERS[i]["accent"] + (255,) if lit else dim + (150,)
        d.rounded_rectangle([x0, y, x1, y + bh], radius=bh / 2, fill=col)
    return img

def punch_hole(img, box, radius):
    """Cut a rounded transparent window into an opaque overlay."""
    mask = Image.new("L", (W, H), 255)
    ImageDraw.Draw(mask).rounded_rectangle(box, radius=radius, fill=0)
    a = img.getchannel("A")
    img.putalpha(Image.composite(a, Image.new("L", (W, H), 0), mask))
    return img

def kicker(img, text, accent, y=64, x=64):
    """Small uppercase eyebrow with a leading accent bar."""
    d = ImageDraw.Draw(img)
    f = bold(29)
    d.rounded_rectangle([x, y + 4, x + 7, y + 34], radius=3.5, fill=accent + (255,))
    d.text((x + 24, y), text.upper(), font=f, fill=WHITE + (235,))

def track(d, xy, text, font, fill, spacing):
    """Letter-spaced text. Returns the advance width."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + spacing
    return x - xy[0] - spacing

def track_w(d, text, font, spacing):
    return sum(d.textlength(c, font=font) for c in text) + spacing * (len(text) - 1)

# ---------------------------------------------------------------- chapters
def make_chapter(i):
    """Top-anchored chapter block, laid over the full-bleed founder shot."""
    L = LAYERS[i]
    img = new_rgba()
    # soft white lift so dark type always reads against the ceiling
    img.alpha_composite(vgrad((W, 400), (255, 255, 255, 112), (255, 255, 255, 0)), (0, 0))
    d = ImageDraw.Draw(img)
    img.alpha_composite(ladder_icon(i, 116, 72), (68, 84))
    fnum = bold(34)
    d.text((208, 100), L["num"], font=fnum, fill=L["accent"] + (255,))
    nw = d.textlength(L["num"], font=fnum)
    d.line([(208 + nw + 18, 118), (208 + nw + 92, 118)], fill=L["accent"] + (170,), width=3)
    ftitle = bold(56)
    track(d, (68, 182), L["name"], ftitle, INK + (255,), 2.0)
    d.text((70, 256), L["keys"], font=reg(30), fill=(58, 64, 82, 235))
    img.save(f"{OUT}/chapter_{i+1}.png")

# ---------------------------------------------------------------- b-roll frames
def make_full(name, kicker_text, accent, mark=True):
    """Overlay for media that fills the frame: scrims + eyebrow + wordmark."""
    img = new_rgba()
    scrim(img, 300, at_top=True, strength=165)
    scrim(img, 430, at_top=False, strength=205)
    kicker(img, kicker_text, accent)
    if mark:
        wm = wordmark(34, (255, 255, 255))
        img.alpha_composite(wm, (W - 64 - wm.width, 68))
    img.save(f"{OUT}/{name}.png")

CARD_BOX = (72, 250, 1008, 1060)

def card_hole(aspect):
    """Largest box of the given aspect that fits the card zone, centred."""
    x0, y0, x1, y1 = CARD_BOX
    bw, bh = x1 - x0, y1 - y0
    if aspect >= bw / bh:
        w = bw; h = int(round(w / aspect))
    else:
        h = bh; w = int(round(h * aspect))
    cx = x0 + (bw - w) // 2
    cy = y0 + (bh - h) // 2
    return (cx, cy, cx + w, cy + h)

def make_card(name, kicker_text, accent, aspect, mark=True):
    """Overlay for media shown inside a rounded card on the branded canvas."""
    box = card_hole(aspect)
    img = brand_bg()
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([box[0] - 2, box[1] - 2, box[2] + 2, box[3] + 2],
                        radius=30, outline=(255, 255, 255, 46), width=3)
    img = punch_hole(img, box, 28)
    kicker(img, kicker_text, accent)
    if mark:
        wm = wordmark(34, (255, 255, 255))
        img.alpha_composite(wm, (W - 64 - wm.width, 68))
    img.save(f"{OUT}/{name}.png")
    with open(f"{OUT}/{name}.box", "w") as fh:
        fh.write(" ".join(str(v) for v in (box[0], box[1], box[2] - box[0], box[3] - box[1])))

# ---------------------------------------------------------------- opening mark
def make_open_mark():
    img = new_rgba()
    img.alpha_composite(vgrad((W, 330), (255, 255, 255, 120), (255, 255, 255, 0)), (0, 0))
    wm = wordmark(52, (16, 18, 26))
    img.alpha_composite(wm, (66, 92))
    d = ImageDraw.Draw(img)
    d.text((70, 168), "Visual AI, from generation to production", font=reg(29),
           fill=(58, 64, 82, 230))
    img.save(f"{OUT}/open_mark.png")

# ---------------------------------------------------------------- inspiration mosaic
INSP_ROOT = "/Users/qqwjq/curify-gallery/daily_inspirations"
MONTHS = {m: i for i, m in enumerate(
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], 1)}

def inspiration_series(n_tiles):
    """One thumbnail per dated folder, spread evenly across the whole archive."""
    dated = []
    for d in os.listdir(INSP_ROOT):
        parts = d.split("_")
        if len(parts) == 2 and parts[0] in MONTHS and parts[1].isdigit():
            dated.append((MONTHS[parts[0]], int(parts[1]), d))
    dated.sort()
    picked = []
    if not dated:
        return picked
    step = max(1, len(dated) // n_tiles)
    for mo, day, d in dated[::step]:
        imgs = sorted(glob.glob(os.path.join(INSP_ROOT, d, "*.jpg")) +
                      glob.glob(os.path.join(INSP_ROOT, d, "*.png")))
        if imgs:
            picked.append((mo, day, imgs[len(imgs) // 2]))
        if len(picked) == n_tiles:
            break
    return picked

def tile_thumb(path, size):
    im = Image.open(path).convert("RGB")
    tw, th = size
    sc = max(tw / im.width, th / im.height)
    im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
    left = (im.width - tw) // 2
    top = (im.height - th) // 3
    im = im.crop((left, top, left + tw, top + th))
    r = Image.new("RGBA", size, (0, 0, 0, 0))
    r.paste(im, (0, 0))
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, tw - 1, th - 1], radius=12, fill=255)
    r.putalpha(mask)
    return r

def make_mosaic(nframes, fps=30):
    cols, rows = 6, 5
    gap = 12
    x0, y0, x1, y1 = CARD_BOX
    tw = (x1 - x0 - gap * (cols - 1)) // cols
    th = (y1 - y0 - gap * (rows - 1)) // rows
    series = inspiration_series(cols * rows)
    total_refs = len(glob.glob(os.path.join(INSP_ROOT, "*", "*.jpg"))) + \
                 len(glob.glob(os.path.join(INSP_ROOT, "*", "*.png")))
    thumbs = [(mo, day, tile_thumb(p, (tw, th))) for mo, day, p in series]
    base = brand_bg()
    kicker(base, "Inspiration, tracked over time", LAYERS[1]["accent"])
    wm = wordmark(34, (255, 255, 255))
    base.alpha_composite(wm, (W - 64 - wm.width, 68))
    slots = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(slots)
    for i in range(len(thumbs)):
        c, r = i % cols, i // cols
        ds.rounded_rectangle([x0 + c * (tw + gap), y0 + r * (th + gap),
                              x0 + c * (tw + gap) + tw, y0 + r * (th + gap) + th],
                             radius=12, fill=(255, 255, 255, 14))
    base.alpha_composite(slots)
    seq = os.path.join(OUT, "mosaic")
    os.makedirs(seq, exist_ok=True)
    reveal_end = int(nframes * 0.74)
    fmo, freg = bold(30), reg(26)
    for f in range(nframes):
        img = base.copy()
        shown = 0
        for i, (mo, day, th_img) in enumerate(thumbs):
            t_in = reveal_end * i / max(1, len(thumbs))
            k = (f - t_in) / 7.0
            if k <= 0:
                continue
            shown = i + 1
            a = min(1.0, k)
            c, r = i % cols, i // cols
            px, py = x0 + c * (tw + gap), y0 + r * (th + gap)
            if a < 1.0:
                s = 0.88 + 0.12 * a
                sw, sh = int(tw * s), int(th * s)
                t2 = th_img.resize((sw, sh), Image.LANCZOS)
                t2.putalpha(t2.getchannel("A").point(lambda v: int(v * a)))
                img.alpha_composite(t2, (px + (tw - sw) // 2, py + (th - sh) // 2))
            else:
                img.alpha_composite(th_img, (px, py))
        d = ImageDraw.Draw(img)
        if shown:
            mo, day, _ = thumbs[shown - 1]
            label = f"{list(MONTHS)[mo-1]} {day}"
        else:
            label = ""
        d.text((72, 1096), label, font=fmo, fill=LAYERS[1]["accent"] + (255,))
        d.text((72 + 150, 1098), f"{total_refs:,} references, one library", font=freg,
               fill=MUTED + (230,))
        img.convert("RGB").save(f"{seq}/{f:04d}.png")
    return seq

# ---------------------------------------------------------------- finale: ladder → logo
def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3

BAR_X, BAR_W, BAR_H = 120, 840, 150
BAR_Y = [900, 700, 500]          # index 0 = Production AI, at the bottom

def draw_bar(img, i, alpha, dy=0.0, scale=1.0):
    if alpha <= 0.01:
        return
    L = LAYERS[i]
    w = int(BAR_W * scale); h = int(BAR_H * scale)
    x = BAR_X + (BAR_W - w) // 2
    y = int(BAR_Y[i] + dy) + (BAR_H - h) // 2
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x, y, x + w, y + h], radius=int(26 * scale),
                        fill=(255, 255, 255, 16), outline=L["accent"] + (120,), width=2)
    d.rounded_rectangle([x, y, x + int(9 * scale), y + h], radius=int(4 * scale),
                        fill=L["accent"] + (255,))
    if scale > 0.7:
        d.text((x + 46, y + 24), L["num"], font=bold(int(23 * scale)), fill=L["accent"] + (255,))
        track(d, (x + 46, y + 56), L["name"], bold(int(40 * scale)), WHITE + (255,), 1.4)
        d.text((x + 46, y + 107), L["keys"], font=reg(int(25 * scale)), fill=MUTED + (245,))
    lay.putalpha(lay.getchannel("A").point(lambda v: int(v * alpha)))
    img.alpha_composite(lay)

def draw_riser(img, i, alpha):
    """Up-chevron in the gap below bar i."""
    if alpha <= 0.01:
        return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    cy = BAR_Y[i] - 25
    d.line([(540 - 16, cy + 9), (540, cy - 9), (540 + 16, cy + 9)],
           fill=LAYERS[i]["accent"] + (220,), width=5, joint="curve")
    lay.putalpha(lay.getchannel("A").point(lambda v: int(v * alpha)))
    img.alpha_composite(lay)

def draw_loop(img, prog):
    """Feedback arrow: research findings flow back down into production."""
    if prog <= 0.01:
        return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    col = (150, 160, 190, 190)
    top_y, bot_y, xin, xout = BAR_Y[2] + 75, BAR_Y[0] + 75, BAR_X, 64
    pts = [(xin, top_y), (xout, top_y + 34), (xout, bot_y - 34), (xin, bot_y)]
    total = 3
    seg = prog * total
    if seg > 0:
        d.line([pts[0], (xin + (xout - xin) * min(1, seg), top_y + 34 * min(1, seg))],
               fill=col, width=4)
    if seg > 1:
        k = min(1, seg - 1)
        d.line([pts[1], (xout, pts[1][1] + (pts[2][1] - pts[1][1]) * k)], fill=col, width=4)
    if seg > 2:
        k = min(1, seg - 2)
        ex = xin + (xout - xin) * (1 - k)
        d.line([pts[2], (ex, pts[2][1] + (bot_y - pts[2][1]) * k)], fill=col, width=4)
        if k > 0.75:
            d.line([(xin - 18, bot_y - 12), (xin, bot_y), (xin - 18, bot_y + 12)],
                   fill=col, width=4, joint="curve")
    lay.putalpha(lay.getchannel("A").point(lambda v: int(v * min(1.0, prog * 1.6))))
    img.alpha_composite(lay)

def make_finale(nframes, fps=30):
    """Frames 0..~243 assemble the ladder; the tail resolves into the logo."""
    seq = os.path.join(OUT, "finale")
    os.makedirs(seq, exist_ok=True)
    base = brand_bg()
    IN_T   = [0.10, 1.82, 4.94]       # seconds, matched to the spoken clauses
    LOOP_T = 6.55
    OUT_T  = 8.10                     # ladder starts resolving into the mark
    LOGO_T = 8.55
    ftitle = bold(27)
    for f in range(nframes):
        t = f / fps
        img = base.copy()
        d = ImageDraw.Draw(img)
        res = ease((t - OUT_T) / 0.55) if t > OUT_T else 0.0
        if res < 1.0:
            ta = min(1.0, max(0.0, (t - 0.0) / 0.45)) * (1 - res)
            tw_ = track_w(d, "HOW WE THINK ABOUT CURIFY", ftitle, 5.0)
            track(d, ((W - tw_) / 2, 372), "HOW WE THINK ABOUT CURIFY", ftitle,
                  MUTED + (int(235 * ta),), 5.0)
            for i in range(3):
                a = ease((t - IN_T[i]) / 0.55)
                if a <= 0:
                    continue
                a_out = a * (1 - res)
                draw_bar(img, i, a_out, dy=(1 - a) * 34, scale=1 - 0.10 * res)
                if i > 0:
                    draw_riser(img, i - 1, ease((t - IN_T[i] - 0.15) / 0.4) * (1 - res))
            draw_loop(img, ease((t - LOOP_T) / 0.9) * (1 - res))
            if t > LOOP_T + 0.5:
                la = ease((t - LOOP_T - 0.5) / 0.5) * (1 - res)
                lt = "Production feeds research. Research feeds production."
                lw = d.textlength(lt, font=reg(27))
                d.text(((W - lw) / 2, 1092), lt, font=reg(27), fill=MUTED + (int(225 * la),))
        if t > LOGO_T:
            k = ease((t - LOGO_T) / 0.7)
            hgt = int(58 + 44 * k)
            wm = wordmark(hgt, WHITE)
            wm.putalpha(wm.getchannel("A").point(lambda v: int(v * k)))
            img.alpha_composite(wm, ((W - wm.width) // 2, 566 - hgt // 2))
            k2 = ease((t - LOGO_T - 0.35) / 0.6)
            if k2 > 0:
                line = "Visual AI, from generation to production."
                fl = reg(33)
                d.text(((W - d.textlength(line, font=fl)) / 2, 672), line, font=fl,
                       fill=(214, 220, 236, int(255 * k2)))
                fu = bold(27)
                d.text(((W - d.textlength("curify-ai.com", font=fu)) / 2, 742),
                       "curify-ai.com", font=fu, fill=(140, 120, 255, int(255 * k2)))
        img.convert("RGB").save(f"{seq}/{f:04d}.png")
    return seq

# ---------------------------------------------------------------- entry point
if __name__ == "__main__":
    for i in range(3):
        make_chapter(i)
    make_open_mark()
    A = [L["accent"] for L in LAYERS]
    make_full("s03", "E-commerce listings, at volume", A[0])
    make_card("s04", "Studio retouching", A[0], 2752 / 1536)
    make_full("s05", "Product imagery", A[0])
    make_full("s06", "Merch & IP design", A[0])
    make_full("s09", "A design system that is yours", A[1])
    make_card("s10", "Reusable, layered assets", A[1], 1602 / 856)
    make_card("s14", "Design agents", A[2], 1329 / 1183)
    make_card("s15", "Evaluation", A[2], 1402 / 1122)
    make_card("s16", "Multimodal search", A[2], 1280 / 720)
    make_card("s17", "New interfaces — ASL", A[2], 640 / 360)
    make_mosaic(96)
    make_finale(330)
    print("gfx done")
