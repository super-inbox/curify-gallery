import asyncio, sys
sys.path.insert(0, "/Users/qqwjq/curify-studio/curify_background")
from dotenv import load_dotenv
load_dotenv("/Users/qqwjq/curify-studio/curify_background/.env")
from app.services import imagen_service as im

OUT = "/private/tmp/claude-501/-Users-qqwjq-curify-frontend/0403e8b8-e23d-4f08-ab3c-00bdf9c19e54/scratchpad"

# 墨蓝为主 + 美孚絣染的朦胧晕边 + 图腾外形 + 祈福语义
DNA = ("Design language: deep ink-blue and navy ground (#14202B to #1E3A5F) with indigo-dyed "
       "cloth texture, motifs in undyed white, pale sky blue and small accents of vermilion and "
       "ochre. Geometric woven look with soft feathered edges like warp-resist ikat dyeing. "
       "Motifs are flat, symmetrical, geometric — stylised ancestor figures, frogs, birds, deer, "
       "fish, rice-ear and water bands. Refined, restrained, premium. ")

SHEET = ("A product design presentation sheet showing THREE distinct design options of the SAME "
         "product, arranged side by side in one row on a light neutral studio background, "
         "each option clearly separated, no text labels, no people. ")

JOBS = {
 "v2_magnet": SHEET + DNA + (
  "PRODUCT: three die-cut acrylic fridge magnets. Each magnet's OUTLINE follows the silhouette of "
  "a different Li totem — option 1 a standing ancestor figure, option 2 a squat frog, option 3 a "
  "bird with spread tail. The totem shape itself is the product shape, not a rectangle with a "
  "picture on it. Glossy acrylic with layered depth."),
 "v2_coaster": SHEET + DNA + (
  "PRODUCT: three round ceramic drink coasters, each glazed with a different symmetrical woven "
  "medallion pattern in ink blue and white — a frog medallion, a deer medallion, a fish and water "
  "medallion. Matte glaze, cork backing visible at a slight angle. Quiet and premium."),
 "v2_tote": SHEET + DNA + (
  "PRODUCT: three laminated canvas tote bags standing upright, each printed differently — option 1 "
  "one large centred ancestor totem, option 2 a full-width horizontal band of repeating geometric "
  "motifs across the lower third, option 3 an all-over small repeated diamond and frog pattern. "
  "Natural undyed canvas body with deep ink-blue printing."),
 "v2_book": SHEET + DNA + (
  "PRODUCT: three hardcover notebooks, each cover carrying a die-cut window revealing a layered "
  "paper-carving scene inside: option 1 an arched thatched boat-shaped house, option 2 a woven "
  "brocade medallion, option 3 a bird and rice-ear composition. Deep ink-blue covers with gold "
  "foil hairlines, layered paper depth clearly visible in the window."),
}

async def main():
    for k, p in JOBS.items():
        try:
            full, _ = await im.generate_full_and_preview_bytes(prompt=p)
            open(f"{OUT}/{k}.jpg","wb").write(full)
            print(f"  OK {k}  {len(full)//1024} KB")
        except Exception as e:
            print(f"  FAIL {k}: {type(e).__name__} {str(e)[:110]}")

asyncio.run(main())
