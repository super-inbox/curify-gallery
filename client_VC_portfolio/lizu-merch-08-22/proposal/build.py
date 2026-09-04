#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild proposal_built.html from proposal_src.html + assets/.

proposal_src.html keeps {{IMG:key}} placeholders so it stays editable; this
inlines every image as a base64 data URI, which the Artifact CSP requires
(it blocks all external hosts).

    python3 build.py            # rebuild
    python3 build.py --check    # rebuild + reconcile every money figure

Then republish proposal_built.html to the SAME artifact URL (see NOTES.md).
"""
import base64, io, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC, OUT = HERE / "proposal_src.html", HERE / "proposal_built.html"
# key -> (path, target width px)
ASSETS = {
    **{k: (HERE / "assets/generated" / f"{k}.jpg", 1000)
       for k in ("dir_a", "dir_b", "dir_c", "v2_magnet", "v2_coaster", "v2_tote", "v2_book")},
    **{k: (HERE / "assets/factory-ref" / f"{k}.jpg", 560)
       for k in ("p_zhidiao", "p_rotate", "p_metal", "p_series", "p_scent")},
    # V3 (2026-08-24): 用客户真实图腾程序化渲染，非生成式产物
    **{k: (HERE / "assets/v3" / f"{k}.jpg", 1100)
       for k in ("v3_library", "v3_colorways", "v3_shapes", "v3_products", "v3_negcases",
                 "v3_magnet_diecut", "v3_magnet_mech")},
    # V4 (2026-08-26): 附录追加候选 SKU
    **{k: (HERE / "assets/v4" / f"{k}.jpg", 1100)
       for k in ("v4_magnet_shapes", "v4_cheap_skus")},
    # V5 (2026-08-27): 祝福语 / 黎锦带 / 复合冰箱贴 / 白查十二时
    **{k: (HERE / "assets/v5" / f"{k}.jpg", 1150)
       for k in ("v5_blessings", "v5_brocade", "v5_magnet_composite", "v5_baicha12")},
    # V6 (2026-09-04): 国博参考新款 + 全线接触表
    **{k: (HERE / "assets/v6" / f"{k}.jpg", 1200)
       for k in ("v6_museum_skus", "v6_contact_sheet")},
}


def encode(path: Path, width: int) -> str:
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def main() -> int:
    src = SRC.read_text()
    need = set(re.findall(r"\{\{IMG:(\w+)\}\}", src))
    missing = need - set(ASSETS)
    if missing:
        print(f"✗ src references unknown assets: {sorted(missing)}")
        return 1
    imgs = {k: encode(*ASSETS[k]) for k in need}
    out = re.sub(r"\{\{IMG:(\w+)\}\}", lambda m: imgs[m.group(1)], src)
    OUT.write_text(out)
    kb = len(out.encode()) // 1024
    print(f"✓ {OUT.name}  {len(need)} images  {kb} KB")
    if kb > 15000:
        print("⚠️  over the 16 MB artifact limit")

    if "--check" in sys.argv:
        rows = re.findall(
            r'<td class="n">¥([\d,]+\.\d)</td><td class="n">(\d+)</td><td class="n">¥([\d,]+)</td>', out)
        prod = sum(int(r[2].replace(",", "")) for r in rows)
        design = 9800
        print(f"  SKU rows      : {len(rows)}")
        print(f"  production sum: ¥{prod:,}")
        print(f"  + design      : ¥{design + prod:,}")
        for label, pct in (("押金 50%", .5), ("定稿 30%", .3), ("尾款 20%", .2)):
            v = round((design + prod) * pct)
            print(f"  {label}: ¥{v:,}  {'OK' if f'¥{v:,}' in out else 'NOT IN DOC'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
