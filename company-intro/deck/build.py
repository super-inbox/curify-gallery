#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the portfolio PDFs from their *_src.html + assets/.

Two documents share one asset pool and one stylesheet:
  ip          — 吊坠 / IP 衍生品（给毛毛镇这类 IP 品牌看）
  industrial  — 工业设计与产品 3D（给硬件/工业客户看）


portfolio_src.html keeps {{IMG:key}} / {{SVG:key}} placeholders so it stays
editable; this resolves each key under assets/ (or <key>.svg beside the source),
downsizes it and inlines it as a base64 data URI, then prints the result to A4
with headless Chrome.

    python3 build.py             # rebuild HTML + PDF
    python3 build.py --html      # HTML only (fast, for iterating on layout)

IMG keys are asset paths without the extension, relative to assets/ —
"vp/吉他" resolves assets/vp/吉他.jpg. A key with no matching file is a hard
error rather than a silent gap, because a missing case image in a client-facing
deck is worse than a failed build.
"""
import argparse
import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
DOCS = {
    "intro":      ("intro_src.html", "Curify_AI_公司介绍_客户版.pdf"),
}
ASSETS = HERE / "assets"

# Widest any image is placed on an A4 page is ~182mm; 1400px covers that at
# print resolution with room to spare, and keeps the PDF under ~10MB.
MAX_W = 1000
EXTS = (".jpg", ".jpeg", ".png", ".webp")


def resolve(key: str) -> Path:
    for ext in EXTS:
        p = ASSETS / f"{key}{ext}"
        if p.exists():
            return p
    raise SystemExit(f"✗ no asset for key {key!r} (looked in {ASSETS})")


def inline_img(key: str) -> str:
    im = Image.open(resolve(key)).convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build(src_name: str, pdf_name: str, html_only: bool) -> None:
    src = HERE / src_name
    out_html = HERE / (src_name.replace("_src.html", "_built.html"))
    out_pdf = HERE / pdf_name
    html = src.read_text()

    # inline the stylesheet — Chrome would load it from disk anyway, but a
    # self-contained built file is also what the Artifact CSP needs if this
    # ever gets published as a page.
    css = (HERE / "style.css").read_text()
    html = html.replace(
        '<link rel="stylesheet" href="style.css">', f"<style>\n{css}\n</style>"
    )

    for key in sorted(set(re.findall(r"\{\{SVG:([\w-]+)\}\}", html))):
        svg = (HERE / f"{key}.svg").read_text()
        html = html.replace("{{SVG:%s}}" % key, svg)

    keys = sorted(set(re.findall(r"\{\{IMG:([^}]+)\}\}", html)))
    for key in keys:
        html = html.replace("{{IMG:%s}}" % key, inline_img(key))
    print(f"inlined {len(keys)} images")

    out_html.write_text(html)
    print(f"  {out_html.name}  ({out_html.stat().st_size / 1e6:.1f} MB)")

    if html_only:
        return

    # Playwright's bundled Chromium, not the installed Google Chrome: the
    # latter's --print-to-pdf hangs on this machine (it also fails on a
    # one-line test page, so it is the printer, not this document).
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(out_html.as_uri(), wait_until="load")
        page.emulate_media(media="print")
        page.pdf(path=str(out_pdf), format="A4", print_background=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        browser.close()
    print(f"  {out_pdf.name}  ({out_pdf.stat().st_size / 1e6:.1f} MB)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("doc", nargs="?", choices=[*DOCS, "all"], default="all")
    ap.add_argument("--html", action="store_true", help="skip the PDF print")
    a = ap.parse_args()
    for key in (DOCS if a.doc == "all" else [a.doc]):
        print(key)
        build(*DOCS[key], a.html)
    return 0


if __name__ == "__main__":
    sys.exit(main())
