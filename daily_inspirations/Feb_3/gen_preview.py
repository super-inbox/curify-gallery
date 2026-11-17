from PIL import Image
from pathlib import Path

# === CONFIG ===
SOURCE_DIR = Path("/Users/qqwjq/curify-gallery/daily_inspirations/Feb_4")
PREVIEW_DIR = Path("/Users/qqwjq/curify-frontend/public/images/insp_preview/")

# Max size for preview (keeps aspect ratio)
MAX_SIZE = (512, 512)  # you can change to (384, 384) if you want smaller

# JPEG quality (lower = smaller file)
JPEG_QUALITY = 70

# =================

PREVIEW_DIR.mkdir(exist_ok=True)

for img_path in SOURCE_DIR.iterdir():
    if img_path.suffix.lower() not in {".jpg", ".jpeg"}:
        continue

    # Skip previews if script is rerun
    if img_path.name.endswith("-prev.jpg"):
        continue

    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            img.thumbnail(MAX_SIZE)

            out_name = f"{img_path.stem}-prev.jpg"
            out_path = PREVIEW_DIR / out_name

            img.save(out_path, "JPEG", quality=JPEG_QUALITY, optimize=True)

            print(f"✅ {img_path.name} → {out_name}")

    except Exception as e:
        print(f"❌ Failed {img_path.name}: {e}")
