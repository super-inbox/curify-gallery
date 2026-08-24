# -*- coding: utf-8 -*-
"""Extract clean binary masks of the client's authentic Li totems."""
from PIL import Image
import numpy as np, glob, os, json

NAMES = {  # docx 顺序 → 官方名称与寓意
 "image1":("大力神","自然与英雄崇拜"), "image2":("大力神·繁衍","繁衍生息 长久万代"),
 "image3":("龙图腾","风调雨顺"),       "image4":("蝴蝶图腾","美好爱情"),
 "image5":("牛图腾","农业丰饶 家庭幸福"),"image6":("人骑牛图腾","崇尚勇武"),
 "image7":("狗牙花图腾","辟邪护佑"),   "image8":("摇篮图腾","婴儿安宁 人丁兴旺"),
 "image9":("龟图腾","延年益寿"),       "image10":("狗图腾","护家平安"),
 "image11":("鸟图腾","爱情美满 排忧解难"),"image12":("鱼图腾","年年丰收 五谷丰登"),
 "image13":("鹿图腾","吉祥如意 幸福平安"),"image14":("蛙图腾","多子多福"),
 "image15":("人图腾","祖先崇拜"),
}
os.makedirs("mask", exist_ok=True)
meta = {}
for f in sorted(glob.glob("image*.jpg"), key=lambda x: int(''.join(c for c in x if c.isdigit()))):
    key = os.path.splitext(os.path.basename(f))[0]
    g = np.array(Image.open(f).convert("L")).astype(float)
    # 判断极性：边框均值高 => 浅底深纹；否则深底浅纹
    border = np.concatenate([g[:6].ravel(), g[-6:].ravel(), g[:,:6].ravel(), g[:,-6:].ravel()])
    ink_is_dark = border.mean() > 127
    thr = (g.min() + g.max()) / 2
    mask = (g < thr) if ink_is_dark else (g > thr)
    ys, xs = np.where(mask)
    if len(xs) == 0:
        continue
    mask = mask[ys.min():ys.max()+1, xs.min():xs.max()+1]
    Image.fromarray((mask*255).astype("uint8")).save(f"mask/{key}.png")
    n, m = NAMES.get(key, (key, ""))
    meta[key] = {"name": n, "meaning": m, "w": mask.shape[1], "h": mask.shape[0],
                 "fill": round(float(mask.mean()), 3)}
    print(f"  {key:8s} {n:10s} {mask.shape[1]}x{mask.shape[0]}  墨占比 {mask.mean():.2f}")
json.dump(meta, open("mask/meta.json","w"), ensure_ascii=False, indent=1)
