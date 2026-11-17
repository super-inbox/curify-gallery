
from PIL import Image
from pathlib import Path
import shutil

# === CONFIG ===
SOURCE_DIR = Path("/Users/qqwjq/curify-gallery/daily_inspirations/Jan_29")

BASE_DIR = Path("/Users/qqwjq/curify-frontend/public/images/")
IMAGE_DIR = BASE_DIR / "insp"
PREVIEW_DIR = BASE_DIR / "insp_preview"

# Max size for preview (keeps aspect ratio)
MAX_SIZE = (512, 512)

# JPEG quality for preview
JPEG_QUALITY = 70

# =================

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

for img_path in SOURCE_DIR.iterdir():
    if img_path.suffix.lower() not in {".jpg", ".jpeg"}:
        continue

    if img_path.name.endswith("-prev.jpg"):
        continue

    try:
        # -------- copy original --------
        target_img_path = IMAGE_DIR / img_path.name
        if not target_img_path.exists():
            shutil.copy2(img_path, target_img_path)
            print(f"📁 Copied original → {target_img_path.name}")
        else:
            print(f"⏭️ Original exists, skip → {target_img_path.name}")

        # -------- generate preview --------
        preview_name = f"{img_path.stem}-prev.jpg"
        preview_path = PREVIEW_DIR / preview_name

        if preview_path.exists():
            print(f"⏭️ Preview exists, skip → {preview_name}")
            continue

        with Image.open(img_path) as img:
            img = img.convert("RGB")
            img.thumbnail(MAX_SIZE)

            img.save(
                preview_path,
                "JPEG",
                quality=JPEG_QUALITY,
                optimize=True,
            )

            print(f"🖼️ Preview generated → {preview_name}")

    except Exception as e:
        print(f"❌ Failed {img_path.name}: {e}")
