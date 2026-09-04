# -*- coding: utf-8 -*-
"""把三张代表作从下方各节「移」到 §02 提案总览（移动，不复制）。
被移走的节改为一句指回，避免同一张图在文档里出现两次。"""
from pathlib import Path
import re

p = Path(__file__).resolve().parent / "proposal_src.html"
s = p.read_text()
assert "HEROES-LIFTED" not in s, "已上提过"

def take(img_key):
    """剪出包含该图的整个 <figure>…</figure>。"""
    i = s.index("{{IMG:%s}}" % img_key)
    a = s.rfind("<figure", 0, i); a = s.rfind("\n", 0, a) + 1
    b = s.index("</figure>", i) + len("</figure>")
    b = s.index("\n", b) + 1
    return a, b

heroes = []
for key in ("v5_magnet_composite", "v7_diecut_text", "v5_baicha12"):
    a, b = take(key)
    heroes.append((key, s[a:b]))
    s = s[:a] + s[b:]

INTRO = '''
<section class="col">
  <h3 style="margin-top:34px">三款代表作</h3>
  <p>下面三张是这条线里最能说明问题的三款。<strong>它们已计入上面的清单</strong>，
  放在这里是为了让贵司不必往下翻就能看到成品长什么样；工艺细节与其余款式在第二部分展开。</p>
</section>

'''
CAPS = {
 "v5_magnet_composite":
   ('<section class="col">\n  <h4 style="font-family:inherit;font-size:16px;margin:26px 0 6px">'
    '① 复合款冰箱贴 —— 对标贵司自己的畅销款</h4>\n'
    '  <p>米色品牌背卡 + 木框 + 织锦纹样 + 金色图腾 + 银饰 + 祝福语。'
    '贵司畅销款赢在<strong>三层材质叠加</strong>而非单一图腾平面图，这一款把那套结构原样保留，'
    '只把织锦与图腾换成贵司原稿纹样。</p>\n</section>\n\n'),
 "v7_diecut_text":
   ('<section class="col">\n  <h4 style="font-family:inherit;font-size:16px;margin:26px 0 6px">'
    '② 图腾外形模切 —— 三种加字做法</h4>\n'
    '  <p>刀线沿图腾轮廓走，产品本身即图腾。图腾即外形之后本体没有留白放字，'
    '所以加字有三条路，请贵司圈选一种作全系列统一做法（我们建议 ①底座条）。'
    '<strong>每款都另有无字版</strong>，两版共用同一副刀模，不增加开模成本。</p>\n</section>\n\n'),
 "v5_baicha12":
   ('<section class="col">\n  <h4 style="font-family:inherit;font-size:16px;margin:26px 0 6px">'
    '③ 「白查十二时」明信片 / 贴纸 —— 六件成套</h4>\n'
    '  <p>方向 C 的插画语言按会议决定只用于纸品。六个时辰串起村落一天，'
    '每张配一式图腾与一句短句，底部统一压黎锦纹样带。<strong>成套是收集动机</strong>：'
    '单张 6–12 元，六张成套可卖 39–49 元，是提高客单价最便宜的办法。</p>\n</section>\n\n'),
}

block = INTRO + "".join(CAPS[k] + fig for k, fig in heroes)

anchor = ("<section class=\"col\">\n  <div class=\"note\">\n"
          "    <span class=\"tag\">每款都有「无字版」与「加字版」两种</span>")
assert anchor in s
s = s.replace(anchor, block + anchor, 1)

# 被移走的三节改为指回
s = s.replace(
 '''  <p>贵司提出冰箱贴不能只有图腾图案，需要平衡复杂度与吸引力。以下四款直接对标畅销款的材质层次：<strong>米色品牌背卡 + 木框 + 织锦纹样 + 金色图腾 + 银饰 + 祝福语</strong>，图腾退为视觉焦点而非全部内容。</p>''',
 '''  <p>贵司提出冰箱贴不能只有图腾图案，需要平衡复杂度与吸引力。做法是直接对标畅销款的材质层次：<strong>米色品牌背卡 + 木框 + 织锦纹样 + 金色图腾 + 银饰 + 祝福语</strong>，图腾退为视觉焦点而非全部内容。<strong>四款成品图见第一部分「三款代表作 ①」。</strong></p>''', 1)
s = s.replace(
 '''  <p>图腾即外形之后，产品本体没有平面留白可以放字。所以加字有三条路，成本与观感各不相同，
  请贵司圈选一种作为全系列统一做法：</p>''',
 '''  <p>图腾即外形之后，产品本体没有平面留白可以放字，所以加字有三条路，成本与观感各不相同。
  <strong>三种做法的对比图见第一部分「三款代表作 ②」</strong>，此处只说取舍：</p>''', 1)
s = s.replace(
 '''  <p>以六个时辰串起村落的一天：晨炊、织锦、稻田、溪浴、归家、火塘。每张配一式图腾与一句短句，底部统一压一条黎锦纹样带。<strong>成套是收集动机</strong>——单张 ¥6–12，六张成套可卖 ¥39–49，是提高客单价最便宜的办法。</p>''',
 '''  <p>以六个时辰串起村落的一天：晨炊、织锦、稻田、溪浴、归家、火塘。每张配一式图腾与一句短句，底部统一压一条黎锦纹样带。<strong>六张成套图见第一部分「三款代表作 ③」。</strong></p>''', 1)

s = s.replace("<!--V8-->", "<!--V8 HEROES-LIFTED-->")
p.write_text(s)
imgs = re.findall(r"\{\{IMG:(\w+)\}\}", s)
dup = [k for k in set(imgs) if imgs.count(k) > 1]
print("  上提 3 张；重复引用:", dup or "无")
print("  section %d/%d" % (s.count("<section"), s.count("</section>")))
