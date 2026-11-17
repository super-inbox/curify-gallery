import json
import shutil
import re
from pathlib import Path
from PIL import Image
from typing import Optional, Any

# === CONFIG ===
SOURCE_DIR = Path("/Users/qqwjq/curify-gallery/daily_inspirations/Feb_9")
IMAGE_DIR = Path("/Users/qqwjq/curify-frontend/public/images/insp/")
PREVIEW_DIR = Path("/Users/qqwjq/curify-frontend/public/images/insp_preview/")
TEMPLATE_JSON_PATH = Path("nano_templates.json")
JSON_PATH = Path("nano_inspiration.generated.json")

# Preview constraints
MAX_SIZE = (512, 512)
MAX_PREVIEW_KB = 250
MIN_QUALITY = 45
START_QUALITY = 80

# =================

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

LOCALE_RE = re.compile(r"^[a-z]{2}$")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def make_preview_with_size_cap(
    src_img: Path,
    out_path: Path,
    max_size=(512, 512),
    max_kb=250,
    min_quality=45,
    start_quality=80,
):
    with Image.open(src_img) as img:
        img = img.convert("RGB")
        img.thumbnail(max_size)

        quality = start_quality
        while True:
            img.save(
                out_path,
                "JPEG",
                quality=quality,
                optimize=True,
                progressive=True,
            )
            size_kb = out_path.stat().st_size / 1024
            if size_kb <= max_kb or quality <= min_quality:
                break
            quality -= 8


def build_template_indexes(template_json: Any):
    """
    Supports either:
    - a list of templates
    - or { "templates": [...] }

    Returns:
      templates_by_id: {template_id: template_obj}
      card_map: {card_id: {"template_id":..., "params": {...}}}
      template_ids_sorted: [template_id ...] sorted by length desc (for filename prefix match)
    """
    if isinstance(template_json, dict) and "templates" in template_json:
        templates = template_json["templates"]
    elif isinstance(template_json, list):
        templates = template_json
    else:
        raise ValueError("TEMPLATE_JSON must be a list or a dict with key 'templates'.")

    if not isinstance(templates, list):
        raise ValueError("TEMPLATE_JSON['templates'] must be a list.")

    templates_by_id: dict[str, dict] = {}
    card_map: dict[str, dict] = {}

    for t in templates:
        if not isinstance(t, dict) or "id" not in t:
            continue
        tid = t["id"]
        templates_by_id[tid] = t

        cards = t.get("cards") or t.get("examples") or []
        if isinstance(cards, list):
            for c in cards:
                if not isinstance(c, dict):
                    continue
                cid = c.get("card_id") or c.get("id")
                if not cid or not isinstance(cid, str):
                    continue
                params = {k: v for k, v in c.items() if k not in {"card_id", "id"}}
                card_map[cid] = {"template_id": tid, "params": params}

    template_ids_sorted = sorted(templates_by_id.keys(), key=len, reverse=True)
    return templates_by_id, card_map, template_ids_sorted


def match_template_id_from_stem(stem: str, template_ids_sorted: list[str]) -> Optional[str]:
    for tid in template_ids_sorted:
        if stem == tid or stem.startswith(tid + "-"):
            return tid
    return None


def parse_stem(stem: str, template_id: str) -> tuple[Optional[str], str]:
    """
    stem: template-education-zh-dna-double-helix
    => (locale="zh", slug="dna-double-helix")

    If no locale segment, locale=None and slug is remaining.
    """
    rest = stem[len(template_id):]
    if rest.startswith("-"):
        rest = rest[1:]
    if not rest:
        return None, ""

    parts = rest.split("-", 1)
    if len(parts) == 2 and LOCALE_RE.match(parts[0]):
        return parts[0], parts[1]
    return None, rest


def pick_title_from_params(params: dict, fallback_slug: str, fallback_stem: str) -> str:
    for k in ["topic", "book_name", "costume_style", "scene_type", "character_name"]:
        v = params.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    for v in params.values():
        if isinstance(v, str) and v.strip():
            return v.strip()
    if fallback_slug:
        return fallback_slug.replace("-", " ").strip()
    return fallback_stem


# === Load template json ===
template_json = load_json(TEMPLATE_JSON_PATH)
templates_by_id, card_map, template_ids_sorted = build_template_indexes(template_json)

# === 0) Enumerate SOURCE_DIR JPGs ONLY (authoritative file list) ===
source_images: list[Path] = []
for p in sorted(SOURCE_DIR.iterdir()):
    if not p.is_file():
        continue
    if p.suffix.lower() not in {".jpg", ".jpeg"}:
        continue
    if p.name.lower().endswith("-prev.jpg") or p.name.lower().endswith("-prev.jpeg"):
        continue
    source_images.append(p)

print(f"📌 Found {len(source_images)} JPG/JPEG files in SOURCE_DIR: {SOURCE_DIR}")

# === 1) Copy SOURCE_DIR JPG/JPEG -> IMAGE_DIR (keep same name) ===
copied_paths: list[Path] = []
for src in source_images:
    dst = IMAGE_DIR / src.name
    shutil.copy2(src, dst)
    copied_paths.append(dst)

print(f"✅ Copied {len(copied_paths)} images to: {IMAGE_DIR}")

# === 2) Generate previews ONLY for copied_paths ===
generated = 0
preview_paths: dict[str, Path] = {}

for img_path in copied_paths:
    out_name = f"{img_path.stem}-prev.jpg"
    out_path = PREVIEW_DIR / out_name

    # rerun safe
    if not out_path.exists():
        try:
            make_preview_with_size_cap(
                img_path,
                out_path,
                max_size=MAX_SIZE,
                max_kb=MAX_PREVIEW_KB,
                min_quality=MIN_QUALITY,
                start_quality=START_QUALITY,
            )
            generated += 1
            print(f"✅ Preview {img_path.name} → {out_name}")
        except Exception as e:
            print(f"❌ Failed preview {img_path.name}: {e}")
            continue

    preview_paths[img_path.name] = out_path

print(f"✅ Generated {generated} previews in: {PREVIEW_DIR}")

# === 3) Build JSON ONLY for copied_paths (NOT scanning IMAGE_DIR) ===
records = []
skipped = 0

for img_path in copied_paths:
    stem = img_path.stem
    prev_name = f"{stem}-prev.jpg"
    prev_fs_path = PREVIEW_DIR / prev_name
    if not prev_fs_path.exists():
        print(f"⚠️ Missing preview for {img_path.name}, skipping.")
        skipped += 1
        continue

    template_id = match_template_id_from_stem(stem, template_ids_sorted)
    if not template_id:
        print(f"⚠️ Cannot match template_id from filename stem: {stem}, skipping.")
        skipped += 1
        continue

    tpl = templates_by_id.get(template_id, {})
    tpl_locales = tpl.get("locales", {}) if isinstance(tpl.get("locales"), dict) else {}

    locale_from_name, slug = parse_stem(stem, template_id)

    # choose locale
    if locale_from_name and locale_from_name in tpl_locales:
        locale = locale_from_name
    elif len(tpl_locales) == 1:
        locale = next(iter(tpl_locales.keys()))
    else:
        locale = "zh" if "zh" in tpl_locales else ("en" if "en" in tpl_locales else (next(iter(tpl_locales.keys())) if tpl_locales else None))

    # params from card_map if possible
    derived_card_id = f"{template_id}-{slug}" if slug else stem
    if derived_card_id in card_map:
        params = card_map[derived_card_id]["params"]
        out_id = derived_card_id
    elif stem in card_map:
        params = card_map[stem]["params"]
        out_id = stem
    else:
        # best-effort: if template has exactly one parameter, infer from slug
        params = {}
        tpl_params = tpl.get("parameters", [])
        if isinstance(tpl_params, list) and len(tpl_params) == 1:
            key = tpl_params[0].get("name")
            if isinstance(key, str) and key:
                params[key] = slug.replace("-", " ").strip() if slug else ""
        out_id = derived_card_id

    # locales in output
    locales_out = {}
    if locale and locale in tpl_locales:
        cat = tpl_locales[locale].get("category")
        title = pick_title_from_params(params, slug, stem)
        locales_out[locale] = {}
        if isinstance(cat, str) and cat.strip():
            locales_out[locale]["category"] = cat.strip()
        locales_out[locale]["title"] = title

    rec = {
        "id": out_id,
        "template_id": template_id,
        "asset": {
            "image_path": f"/images/insp/{img_path.name}",
            "preview_path": f"/images/insp_preview/{prev_name}",
        },
        "params": params,
        "locales": locales_out,
    }
    records.append(rec)

dump_json(JSON_PATH, records)
print(f"✅ Wrote {len(records)} records (skipped {skipped}) to: {JSON_PATH}")
