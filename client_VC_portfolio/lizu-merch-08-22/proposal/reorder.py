# -*- coding: utf-8 -*-
"""V8：整体重排 —— 结论先行，依据在后；并清理已作废的附录内容。

正文按 h2 切成单元（含其后的 figure 与子 section），再按 ORDER 重排。
分部标题在 ORDER 里显式声明位置，不靠回溯 <hr> 猜——那样会插错格。
"""
from pathlib import Path
import re

H = Path(__file__).resolve().parent
p = H / "proposal_src.html"
s = p.read_text()
assert "<!--V8-->" not in s, "已重排过；如需重跑请先从 /tmp/src_before_v8.html 恢复"

apx_i = s.index('<section class="col" id="appendix"')
apx_i = s.rfind('<hr class="weave">', 0, apx_i)
first_hr = s.index('<hr class="weave">')
head, body, appendix = s[:first_hr], s[first_hr:apx_i], s[apx_i:]

starts = []
for m in re.finditer(r"<h2[^>]*>(.*?)</h2>", body, re.S):
    title = re.sub("<.*?>", "", m.group(1)).strip()
    j = body.rfind('<hr class="weave">', 0, m.start())
    k = body.rfind("<section", 0, m.start())
    b = body.rfind("\n", 0, max(j, k)) + 1
    starts.append((b, title))
starts.sort()
units = {}
for i, (b, title) in enumerate(starts):
    e = starts[i + 1][0] if i + 1 < len(starts) else len(body)
    units[title] = body[b:e]
print("  切出单元 %d 个" % len(units))

def U(key):
    for k in list(units):
        if k.startswith(key):
            return units.pop(k)
    raise KeyError(key)

def part(title, sub):
    return ('<hr class="weave">\n\n<section class="col">\n'
            '  <p class="num">——</p>\n  <h2 style="margin-bottom:4px">%s</h2>\n'
            '  <p class="lede">%s</p>\n</section>\n\n' % (title, sub))

ORDER = [
  ("我们对这个项目的理解",
   ("第一部分 · 提案", "结论先行：做什么、多少钱、什么时候签。后面两部分是它的依据与备选。")),
  ("我们提议做什么", None),
  ("选品深度与首批配置", None),
  ("排期与预计签约时间", None),

  ("设计元素",
   ("第二部分 · 设计依据", "上面每一款是怎么来的：文化考据、纹样体系、祝福语、配色版式、材质选择。")),
  ("三个系列方向", None),
  ("纹样准确性", None),
  ("祝福语", None),
  ("黎锦元素", None),
  ("冰箱贴 · 复合款", None),
  ("V3 · 图腾库与配色扩展", None),
  ("冰箱贴专题", None),
  ("「白查十二时」", None),
  ("材质说明", None),
  ("品类与选品", None),

  ("依贵司国博参考新增的款式",
   ("第三部分 · 候选与备选", "以下均未计入首批报价，供贵司圈选后追加或替换。")),
  ("更多 SKU", None),

  ("需要贵司提供的资料",
   ("第四部分 · 下一步", "确认这几项，我们即可进入正式设计。")),
  ("为什么是我们", None),
]

chunks = []
for key, hdr in ORDER:
    if hdr:
        chunks.append(part(*hdr))
    chunks.append(U(key))
new_body = "".join(chunks)
assert not units, "有单元未被排入: %s" % list(units)

def cut_between(text, k1, k2, label, tag="<section"):
    a = text.index(k1); a = text.rfind("\n", 0, text.rfind(tag, 0, a)) + 1
    b = text.index(k2); b = text.rfind("\n", 0, text.rfind(tag, 0, b)) + 1
    print("  删除 %s：%d 字符" % (label, b - a))
    return text[:a] + text[b:]

appendix = cut_between(appendix, "<h3>A1 · 八福对照表与母题", "<h3>A2 · 工艺参考", "A1 八福表与母题")
appendix = appendix.replace(
  "<h3>A2 · 工艺参考（合作工厂过往案例）</h3>",
  "<h3>A1 · 已作废：自拟的八福纹样体系</h3>\n"
  "  <p>V2 阶段我方依公开资料整理过一套 8 纹样对照表。收到贵司原稿后确认：其中稻穗纹、水波纹、"
  "太阳纹<strong>不在贵司图腾体系内</strong>，而贵司体系中的龙、蝴蝶、牛、人骑牛、狗牙花、摇篮、"
  "龟、狗我方此前未收录。<strong>整表作废，以正文的 15 式为准</strong>；原表已从本方案删除，"
  "不再留档，以免日后被误用。</p>\n"
  '</section>\n\n<section class="col">\n  <h3>A2 · 工艺参考（合作工厂过往案例）</h3>', 1)

appendix = cut_between(appendix, "<h3>覆膜帆布袋 — 三种版式</h3>", "<h3>船型屋立体纸雕本</h3>",
                       "覆膜帆布袋三种版式（材质已否决）", tag='<div class="col">')
appendix = appendix.replace("  <h3>一、V2 已出：图腾外形的三款</h3>\n", "", 1)

s = head + new_body + appendix + "\n<!--V8-->\n"

apx = s.index('id="appendix"')
seq = iter(["%02d" % i for i in range(1, 40)])
s = re.sub(r'<p class="num">([^<]+)</p>',
           lambda m: m.group(0) if m.group(1) in ("附录", "——") else '<p class="num">%s</p>' % next(seq),
           s[:apx]) + s[apx:]

p.write_text(s)
print("  section %d/%d  imgs %d" % (s.count("<section"), s.count("</section>"),
                                    len(set(re.findall(r"\{\{IMG:(\w+)\}\}", s)))))
print("  正文顺序:")
for h in re.findall(r"<h2[^>]*>(.*?)</h2>", s[: s.index('id="appendix"')], re.S):
    t = re.sub("<.*?>", "", h).strip()
    print(("  " if t.startswith("第") else "      ") + t[:42])
