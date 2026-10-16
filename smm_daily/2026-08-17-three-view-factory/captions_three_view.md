# SMM · Curify — 三视图 / Three-view for manufacturing · 2026-08-17

## ⛔ STATUS: copy is ready, the hero image is NOT

The `image_to_threeview` tool's view generation **has never successfully run** —
the Gemini project is at its monthly spending cap (429 RESOURCE_EXHAUSTED),
retried again today. So there is **no generated three-view sheet to show**.

**Do not publish a version that implies the tool works.** The copy below is
deliberately written as a *factory-requirement / demand probe* rather than a tool
demo, so it is publishable today using the real factory photos. The moment the
cap is raised, generate the hero and the same copy can carry a product claim.

```bash
cd curify-studio/dev/jayw/design-agent-v0/threeview
python image_to_threeview.py <photo.jpg> --w 95 --h 150 --d 90 \
  --name "盘蛇摆件" --material "锌合金压铸 + 黑色磨砂电镀" --out case_snake
```

**CTA:** https://www.curify-ai.com/contact

## Assets

| file | status |
|---|---|
| `live1.jpg` (coiled snake), `live2.jpg` (dragon cup), `live3.jpg` (dragon figurine) | ✅ real, from the 2026-08-16 factory visit — `curify-frontend/raw/3d-model-08-16/` |
| three-view sheet | ❌ blocked on quota |

⚠️ The photos include another company's booth signage and banner text. **Crop or
blur before publishing** — they identify a supplier who did not agree to appear
in our marketing.

---

## EN · Facebook

> We spent a day in a Dongguan metal-craft factory asking a boring question:
> *what do you actually need from us to quote a piece?*
>
> For stickers and acrylic, the answer is files — cut line, white ink, bleed,
> CMYK. We build those.
>
> For a figurine like the ones in these photos, the answer is completely
> different, and it stopped us:
>
> **三视图 → 3D → STL/STEP + CMF.**
>
> A three-view drawing. Front, side, top, at real dimensions. Not a render — a
> render is unquotable, because it doesn't tell a factory how deep the piece is
> or where the wall thickness sits. Plush is the same story: three-view, sizes,
> fabric, embroidery placement, Pantone.
>
> That's the gap we're working on now. It's also the honest reason our
> design-to-manufacturing tools currently stop at flat products — cut lines and
> dielines are 2D problems, and a figurine isn't.
>
> **If you make 3D product — figurines, plush, metal collectibles — tell us what
> your factory asks you for.** We'd rather build against your supplier's real
> spec sheet than our guess at one.
>
> 🔗 (first comment)

### EN · short

> "Send us the files" means something different for a figurine.
>
> Stickers/acrylic: cut line, white ink, CMYK. Solved.
> Figurines: **三视图 → 3D → STL/STEP + CMF.** A render can't be quoted from — it
> doesn't say how deep the piece is.
>
> Making 3D product? Tell us what your factory actually asks for 👇

---

## 中文 · 小红书

> **去了趟东莞五金工艺厂，问了个很笨的问题：你们到底需要我给什么，才能报价？**
>
> 贴纸、亚克力，答案是文件：刀线、白墨、出血、CMYK——这些我们已经能做。
>
> 但图里这种摆件，答案完全不一样，也把我们问住了：
>
> **三视图 → 3D → STL/STEP + CMF。**
>
> 要的是**三视图**：正视、侧视、俯视，带真实尺寸。**不是效果图**——效果图报不了价，
> 因为它不告诉工厂这件东西有多厚、壁厚在哪。毛绒也一样：三视图、尺寸、面料、
> 绣花位置、Pantone。
>
> 这就是我们现在在补的缺口。也是我们的设计到生产工具目前只做到平面品类的**真实原因**——
> 刀线和刀版是二维问题，摆件不是。
>
> **如果你在做立体产品（手办、毛绒、金属摆件），告诉我们你的工厂到底要什么。**
> 与其我们猜一份规格，不如照着你供应商真实的那份来做。
>
> 📩 主页链接 / 私信

**Tags:** #手办 #谷子 #三视图 #工业设计 #产品设计 #东莞 #供应链 #外贸

### 中文 · 短版

> 「发个文件过来」——对摆件来说完全是另一回事。
> 贴纸/亚克力：刀线、白墨、CMYK，已解决。
> 手办：**三视图 → 3D → STL/STEP + CMF**。效果图报不了价，它不告诉工厂厚度。
> 做立体产品的朋友，**告诉我们你的工厂要什么**。

---

## Claims ledger

- ✅ **The factory requirement** — from the 2026-08-16 roadmap table: 毛绒 needs
  三视图/尺寸/面料/绣花位置/Pantone; 潮玩/手办 needs 三视图 → 3D → STL/STEP + CMF.
- ✅ **"our tools stop at flat products"** — sticker, acrylic and packaging are
  shipped; 三视图 is not.
- ❌ **Do NOT claim we generate three-views.** The tool exists as a script and has
  never produced one.
- ❌ **Do NOT claim STL/STEP output.** A single photo does not determine hidden
  geometry, and a wrong mesh costs a steel mould rather than a re-render.
