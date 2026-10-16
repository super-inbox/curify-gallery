#!/usr/bin/env python3
"""RedNote (小红书) contrast images for the 3D packaging-mockup case (仁寿 fortune box).

Mirrors the die-cut sticker set in
curify-gallery/designAI_manufacturing/sticker-print/cinnamoroll-teacup/xhs/
  labubu-前后对比.jpg  /  labubu-before-after-EN.jpg      (before -> after)
  CMYK-发灰vs补正.jpg  /  CMYK-washed-vs-fixed-EN.jpg     (原图 / ✗ / ✓)

Outputs 1080x1080 JPGs, rendered at 2x and downsampled for clean edges.
"""
import os
from PIL import Image, ImageDraw, ImageFont

S = 2                      # supersample factor
W = 1080                   # final canvas
OUT = "/Users/qqwjq/curify-gallery/designAI_manufacturing/3D-mockup/fortune-box/xhs"
RENDER45 = "/Users/qqwjq/curify-gallery/designAI_manufacturing/3D-mockup/fortune-box/仁寿盒-45度效果图.jpg"

BG        = (245, 245, 250)
INK       = (28, 28, 46)
GRAY      = (140, 140, 155)
GRAY_DK   = (90, 90, 108)
CARD      = (255, 255, 255)
CARD_EDGE = (226, 226, 236)
PURPLE    = (124, 107, 240)
RED       = (196, 42, 42)
RED_EDGE  = (232, 168, 168)
GREEN     = (24, 122, 62)
GREEN_EDGE= (152, 206, 172)

# box faces — echo the real 仁寿 box (cream -> coral gradient, gold edges)
FRONT_TOP = (247, 233, 183)
FRONT_BOT = (244, 168, 138)
TOP_FACE  = (250, 240, 208)
SIDE_FACE = (226, 186, 142)
EDGE      = (183, 138, 96)

CJK = "/System/Library/Fonts/Hiragino Sans GB.ttc"
HELV = "/System/Library/Fonts/Helvetica.ttc"


def font(size, bold=False, latin=False):
    size = int(size * S)
    if latin and os.path.exists(HELV):
        try:
            return ImageFont.truetype(HELV, size, index=1 if bold else 0)
        except Exception:
            pass
    return ImageFont.truetype(CJK, size, index=2 if bold else 0)


def text(d, xy, s, f, fill, anchor="mm"):
    d.text((xy[0] * S, xy[1] * S), s, font=f, fill=fill, anchor=anchor)


def card(d, box, edge=CARD_EDGE, width=2, radius=18, fill=CARD):
    x0, y0, x1, y1 = [v * S for v in box]
    d.rounded_rectangle([x0, y0, x1, y1], radius=radius * S, fill=fill,
                        outline=edge, width=int(width * S))


def tight_crop(im, thresh=244, pad=0.03):
    """Crop away the white studio background around the product."""
    g = im.convert("L")
    mask = g.point(lambda p: 255 if p < thresh else 0)
    bb = mask.getbbox()
    if not bb:
        return im
    px, py = int(im.width * pad), int(im.height * pad)
    return im.crop((max(0, bb[0] - px), max(0, bb[1] - py),
                    min(im.width, bb[2] + px), min(im.height, bb[3] + py)))


def whiten_bg(im, lo=232, hi=250):
    """Lift the studio off-white to pure white so the photo melts into the card."""
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            if r >= lo and g >= lo and b >= lo:
                t = min(1.0, (min(r, g, b) - lo) / max(1, hi - lo))
                px[x, y] = (int(r + (255 - r) * t), int(g + (255 - g) * t), int(b + (255 - b) * t))
    return im


def mark_x(d, cx, cy, r=13, col=RED, w=5):
    cx, cy, r, w = cx * S, cy * S, r * S, int(w * S)
    d.line([(cx - r, cy - r), (cx + r, cy + r)], fill=col, width=w)
    d.line([(cx - r, cy + r), (cx + r, cy - r)], fill=col, width=w)


def mark_check(d, cx, cy, r=14, col=GREEN, w=5):
    cx, cy, r, w = cx * S, cy * S, r * S, int(w * S)
    d.line([(cx - r, cy + r * 0.05), (cx - r * 0.25, cy + r * 0.72),
            (cx + r, cy - r * 0.75)], fill=col, width=w, joint="curve")


def fit(im, box):
    """Scale to fit inside box (x0,y0,x1,y1 in final px), return (img, paste_xy)."""
    bw, bh = (box[2] - box[0]) * S, (box[3] - box[1]) * S
    r = min(bw / im.width, bh / im.height)
    im2 = im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)
    x = int(box[0] * S + (bw - im2.width) / 2)
    y = int(box[1] * S + (bh - im2.height) / 2)
    return im2, (x, y)


# ---------------------------------------------------------------- dieline ---
def dieline(w_px, h_px):
    """Schematic flat layout (刀版展开图) of a 117x114x39mm tuck box."""
    Wp, Hp, Dp, G = 117, 114, 39, 16          # panel widths in mm, G = glue tab
    tot_w, tot_h = Dp + Wp + Dp + Wp + G, Dp + Hp + Dp
    im = Image.new("RGBA", (w_px, h_px), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    s = min(w_px / tot_w, h_px / tot_h) * 0.94
    ox, oy = (w_px - tot_w * s) / 2, (h_px - tot_h * s) / 2
    X = lambda v: ox + v * s
    Y = lambda v: oy + v * s

    cols = [(0, Dp), (Dp, Wp), (Dp + Wp, Dp), (Dp + Wp + Dp, Wp), (Dp + Wp + Dp + Wp, G)]
    body_y0, body_y1 = Dp, Dp + Hp

    # panels (body row) with a warm vertical gradient
    grad = Image.new("RGB", (1, 256))
    for i in range(256):
        t = i / 255
        grad.putpixel((0, i), tuple(int(FRONT_TOP[k] + (FRONT_BOT[k] - FRONT_TOP[k]) * t) for k in range(3)))
    for x0, cw in cols:
        if cw == G:
            continue
        bx = [X(x0), Y(body_y0), X(x0 + cw), Y(body_y1)]
        g = grad.resize((int(bx[2] - bx[0]), int(bx[3] - bx[1])), Image.BILINEAR).convert("RGBA")
        im.paste(g, (int(bx[0]), int(bx[1])))

    # flaps (top + bottom) — lighter tint
    flap = (250, 238, 214, 255)
    for x0, cw in cols:
        if cw == G:
            continue
        inset = cw * 0.06
        d.polygon([(X(x0 + inset), Y(0)), (X(x0 + cw - inset), Y(0)),
                   (X(x0 + cw), Y(body_y0)), (X(x0), Y(body_y0))], fill=flap)
        d.polygon([(X(x0), Y(body_y1)), (X(x0 + cw), Y(body_y1)),
                   (X(x0 + cw - inset), Y(tot_h)), (X(x0 + inset), Y(tot_h))], fill=flap)
    # glue tab
    gx0 = cols[-1][0]
    d.polygon([(X(gx0), Y(body_y0)), (X(gx0 + G), Y(body_y0 + G * 0.5)),
               (X(gx0 + G), Y(body_y1 - G * 0.5)), (X(gx0), Y(body_y1))], fill=flap)

    lw = max(2, int(round(1.6 * S)))
    # cut lines (solid, dark)
    for x0, cw in cols:
        if cw == G:
            continue
        inset = cw * 0.06
        d.line([(X(x0 + inset), Y(0)), (X(x0 + cw - inset), Y(0)),
                (X(x0 + cw), Y(body_y0))], fill=EDGE, width=lw, joint="curve")
        d.line([(X(x0), Y(body_y0)), (X(x0 + inset), Y(0))], fill=EDGE, width=lw)
        d.line([(X(x0), Y(body_y1)), (X(x0 + inset), Y(tot_h)),
                (X(x0 + cw - inset), Y(tot_h)), (X(x0 + cw), Y(body_y1))], fill=EDGE, width=lw, joint="curve")
    d.line([(X(0), Y(body_y0)), (X(0), Y(body_y1))], fill=EDGE, width=lw)
    d.line([(X(gx0), Y(body_y0)), (X(gx0 + G), Y(body_y0 + G * 0.5)),
            (X(gx0 + G), Y(body_y1 - G * 0.5)), (X(gx0), Y(body_y1))], fill=EDGE, width=lw, joint="curve")
    d.line([(X(0), Y(body_y0)), (X(gx0), Y(body_y0))], fill=EDGE, width=lw)
    d.line([(X(0), Y(body_y1)), (X(gx0), Y(body_y1))], fill=EDGE, width=lw)

    # fold lines (dashed, light)
    def dashed(p0, p1, dash=5 * S, gap=4 * S, col=(150, 150, 165, 255)):
        import math
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        L = math.hypot(dx, dy)
        if L == 0:
            return
        ux, uy, t = dx / L, dy / L, 0
        while t < L:
            e = min(t + dash, L)
            d.line([(p0[0] + ux * t, p0[1] + uy * t), (p0[0] + ux * e, p0[1] + uy * e)],
                   fill=col, width=max(1, int(S)))
            t = e + gap

    for x0, cw in cols[1:]:
        dashed((X(x0), Y(body_y0)), (X(x0), Y(body_y1)))
    for x0, cw in cols:
        if cw == G:
            continue
        dashed((X(x0), Y(body_y0)), (X(x0 + cw), Y(body_y0)))
        dashed((X(x0), Y(body_y1)), (X(x0 + cw), Y(body_y1)))
    return im


# ------------------------------------------------------------- iso 3D box ---
def iso_box(w_px, h_px, W_mm, H_mm, D_mm, scale=None, baseline=0.92):
    """Cabinet-projection box drawn to true W:H:D proportions."""
    im = Image.new("RGBA", (w_px, h_px), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    kx, ky = 0.70, 0.40
    if scale is None:
        scale = min(w_px * 0.86 / (W_mm + D_mm * kx), h_px * 0.86 / (H_mm + D_mm * ky))
    fw, fh, ox_, oy_ = W_mm * scale, H_mm * scale, D_mm * scale * kx, D_mm * scale * ky
    x0 = (w_px - (fw + ox_)) / 2
    y1 = h_px * baseline
    y0 = y1 - fh

    grad = Image.new("RGB", (1, 256))
    for i in range(256):
        t = i / 255
        grad.putpixel((0, i), tuple(int(FRONT_TOP[k] + (FRONT_BOT[k] - FRONT_TOP[k]) * t) for k in range(3)))
    face = Image.new("RGBA", (w_px, h_px), (0, 0, 0, 0))
    face.paste(grad.resize((max(1, int(fw)), max(1, int(fh))), Image.BILINEAR).convert("RGBA"),
               (int(x0), int(y0)))
    m = Image.new("L", (w_px, h_px), 0)
    ImageDraw.Draw(m).rectangle([x0, y0, x0 + fw, y0 + fh], fill=255)
    im.paste(face, (0, 0), m)

    d.polygon([(x0, y0), (x0 + ox_, y0 - oy_), (x0 + fw + ox_, y0 - oy_), (x0 + fw, y0)],
              fill=TOP_FACE)
    d.polygon([(x0 + fw, y0), (x0 + fw + ox_, y0 - oy_),
               (x0 + fw + ox_, y0 + fh - oy_), (x0 + fw, y0 + fh)], fill=SIDE_FACE)
    lw = max(2, int(round(1.5 * S)))
    for poly in ([(x0, y0), (x0 + ox_, y0 - oy_), (x0 + fw + ox_, y0 - oy_), (x0 + fw, y0), (x0, y0)],
                 [(x0 + fw, y0), (x0 + fw + ox_, y0 - oy_), (x0 + fw + ox_, y0 + fh - oy_),
                  (x0 + fw, y0 + fh), (x0 + fw, y0)],
                 [(x0, y0), (x0, y0 + fh), (x0 + fw, y0 + fh), (x0 + fw, y0)]):
        d.line(poly, fill=EDGE, width=lw, joint="curve")
    return im, scale


def title_arrow(d, cy, left, right, f, col=INK):
    """Centered '<left> → <right>' with a drawn arrow (Helvetica has no U+2192)."""
    lw, rw = d.textlength(left, font=f), d.textlength(right, font=f)
    gap, alen = 16 * S, 34 * S
    x = (W * S - (lw + gap + alen + gap + rw)) / 2
    d.text((x, cy * S), left, font=f, fill=col, anchor="lm")
    ax = x + lw + gap
    d.line([(ax, cy * S), (ax + alen - 7 * S, cy * S)], fill=col, width=int(3.5 * S))
    d.polygon([(ax + alen, cy * S), (ax + alen - 11 * S, cy * S - 7 * S),
               (ax + alen - 11 * S, cy * S + 7 * S)], fill=col)
    d.text((ax + alen + gap, cy * S), right, font=f, fill=col, anchor="lm")


def arrow(d, x0, x1, y, col=PURPLE, w=4):
    x0, x1, y, w = x0 * S, x1 * S, y * S, int(w * S)
    d.line([(x0, y), (x1 - 9 * S, y)], fill=col, width=w)
    d.polygon([(x1, y), (x1 - 13 * S, y - 9 * S), (x1 - 13 * S, y + 9 * S)], fill=col)


# ================================================================== image 1 ==
def before_after(lang):
    im = Image.new("RGB", (W * S, W * S), BG)
    d = ImageDraw.Draw(im)
    L = lang == "en"
    if L:
        title_arrow(d, 88, "One dieline", "a 3D box the client can read", font(33, True, True))
    else:
        text(d, (540, 88), "一张刀版图 → 客户能直接看的 3D 效果图", font(46, True), INK)

    lc, rc = (55, 290, 495, 660), (585, 290, 1025, 660)
    card(d, lc); card(d, rc)
    dl = dieline(int((lc[2] - lc[0] - 36) * S), int((lc[3] - lc[1] - 36) * S))
    im.paste(dl, (int((lc[0] + 18) * S), int((lc[1] + 18) * S)), dl)
    ph = whiten_bg(tight_crop(Image.open(RENDER45).convert("RGB")))
    ph2, xy = fit(ph, (rc[0] + 14, rc[1] + 14, rc[2] - 14, rc[3] - 14))
    im.paste(ph2, xy)
    arrow(d, 512, 568, 475)

    text(d, (275, 700), "1  Flat dieline (.ai / PDF)" if L else "① 刀版展开图（.ai / PDF）",
         font(24 if L else 27, False, L), GRAY_DK)
    text(d, (805, 700), "2  Folded 3D mockup" if L else "② 折叠后的 3D 效果图",
         font(24 if L else 27, False, L), PURPLE)
    text(d, (540, 800), "117 × 114 × 39 mm · 350g 卡纸 · 45° / 正面 / 白底" if not L
         else "117 × 114 × 39 mm · 350gsm board · 45° / front / white-bg",
         font(22 if L else 21, False, L), GRAY)
    text(d, (540, 1000),
         "Real size · fold logic · material — read from the file, not guessed" if L
         else "尺寸 · 折叠关系 · 材质 —— 全部从刀版文件里读，不靠猜",
         font(27 if L else 30, False, L), (58, 58, 74))
    return im.resize((W, W), Image.LANCZOS)


# ================================================================== image 2 ==
def proportion_trap(lang):
    im = Image.new("RGB", (W * S, W * S), BG)
    d = ImageDraw.Draw(im)
    L = lang == "en"
    text(d, (540, 82), "The #1 trap in AI packaging mockups: proportions" if L
         else "AI 做包装 3D 图，最大的坑是比例",
         font(34 if L else 46, True, L), INK)

    cards = [(45, 172, 345, 612), (390, 172, 690, 612), (735, 172, 1035, 612)]
    card(d, cards[0])
    card(d, cards[1], edge=RED_EDGE, width=3)
    card(d, cards[2], edge=GREEN_EDGE, width=3)

    cw = int((cards[0][2] - cards[0][0] - 40) * S)
    ch = int((cards[0][3] - cards[0][1] - 155) * S)
    art_y = int((cards[0][1] + 88) * S)
    dl = dieline(cw, ch)
    im.paste(dl, (int((cards[0][0] + 20) * S), art_y), dl)

    # identical W/H, only the depth differs -> the comparison is purely proportion
    b2, sc = iso_box(cw, ch, 117, 114, 112)
    im.paste(b2, (int((cards[1][0] + 20) * S), art_y), b2)
    b3, _ = iso_box(cw, ch, 117, 114, 39, scale=sc)
    im.paste(b3, (int((cards[2][0] + 20) * S), art_y), b3)

    # markers
    text(d, (195, 216), "1", font(30, True, True), GRAY)
    mark_x(d, 540, 216)
    mark_check(d, 885, 214)

    # the numbers are the punchline — same W/H, 112 vs 39 depth
    fdim = font(20, True, True)
    text(d, (195, 570), "117 × 114 × 39 mm", fdim, GRAY)
    text(d, (540, 570), "117 × 114 × 112 mm", fdim, RED)
    text(d, (885, 570), "117 × 114 × 39 mm", fdim, GREEN)

    labels = [
        (195, "Dieline states the size" if L else "刀版里写着尺寸", GRAY_DK),
        (540, "Prompt only: AI draws a cube" if L else "只丢提示词 · 画成方盒子", RED),
        (885, "Built from the dieline" if L else "按刀版尺寸建模 · 扁盒", GREEN),
    ]
    for cx, s, col in labels:
        text(d, (cx, 655), s, font(20 if L else 22, False, L), col)

    text(d, (540, 925),
         "Rule: read W×H×D out of the dieline — never let the model guess" if L
         else "诀窍：长宽高必须从刀版里读出来，别让模型自己猜",
         font(27 if L else 31, False, L), (58, 58, 74))
    text(d, (540, 985),
         "(a cube vs a flat box — every client spots it instantly)" if L
         else "（方盒子和扁盒子，客户和工厂一眼就看得出来）",
         font(21 if L else 24, False, L), GRAY)
    return im.resize((W, W), Image.LANCZOS)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    jobs = [
        (before_after("zh"),      "仁寿盒-刀版转3D.jpg"),
        (before_after("en"),      "renshou-dieline-to-3d-EN.jpg"),
        (proportion_trap("zh"),   "包装3D-比例坑.jpg"),
        (proportion_trap("en"),   "packaging-3d-proportion-trap-EN.jpg"),
    ]
    for img, name in jobs:
        p = os.path.join(OUT, name)
        img.save(p, quality=92, subsampling=0)
        print("wrote", p, os.path.getsize(p) // 1024, "KB")
