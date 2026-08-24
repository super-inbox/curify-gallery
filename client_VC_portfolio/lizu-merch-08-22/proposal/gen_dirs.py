import asyncio, os, sys
sys.path.insert(0, "/Users/qqwjq/curify-studio/curify_background")
from dotenv import load_dotenv
load_dotenv("/Users/qqwjq/curify-studio/curify_background/.env")
from app.services import imagen_service as im

OUT = "/private/tmp/claude-501/-Users-qqwjq-curify-frontend/0403e8b8-e23d-4f08-ab3c-00bdf9c19e54/scratchpad"

BASE = ("A design moodboard sheet for a Chinese cultural-tourism merchandise line, "
        "flat-lay grid composition on a neutral studio background, no people, no text captions. ")

DIRS = {
 "dir_a": BASE + (
  "THEME: Hainan Li ethnic brocade as a writing system. Show a grid of woven Li brocade "
  "textile swatches with deep indigo-black ground and dense geometric figures in vermilion red, "
  "ochre yellow and grass green: stylised standing human ancestor figures, geometric frogs, "
  "zigzag water bands. Include close-up macro of the woven warp and weft threads, a colour chip "
  "row of indigo, vermilion, ochre, green and undyed hemp, and simple line-drawn pattern studies "
  "on cream paper. Museum textile-archive aesthetic, even soft daylight, highly organised."),
 "dir_b": BASE + (
  "THEME: the Li boat-shaped thatched house of Baicha village. Show architectural studies of a "
  "low arched thatch-roofed dwelling that looks like an upturned wooden boat: elevation sketches, "
  "a cross-section drawing, macro of dry thatch straw texture, macro of woven bamboo wall lashing, "
  "and a small clay maquette of the arched house. Warm straw-brown, weathered timber and deep "
  "indigo accents on a sand-toned ground. Architectural field-study aesthetic, raking daylight."),
 "dir_c": BASE + (
  "THEME: one day in a Li mountain village, illustrated. Show a set of warm flat-vector "
  "illustration vignettes arranged in a grid: a thatched arched village house at dawn with cooking "
  "smoke, a woman seated weaving on a backstrap loom, coconut palms and banana leaves, a village "
  "market scene, an evening gathering. Bright tropical palette of sun yellow, leaf green, terracotta "
  "and sky blue with indigo linework. Cheerful contemporary editorial illustration, clean and airy."),
}

async def main():
    for k, p in DIRS.items():
        try:
            full, _ = await im.generate_full_and_preview_bytes(prompt=p)
            open(f"{OUT}/{k}.jpg", "wb").write(full)
            print(f"  OK {k}  {len(full)//1024} KB")
        except Exception as e:
            print(f"  FAIL {k}: {type(e).__name__} {str(e)[:120]}")

asyncio.run(main())
