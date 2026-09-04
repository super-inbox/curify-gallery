# -*- coding: utf-8 -*-
"""V7：在三处加入「加字版」，与无字版并存。"""
from pathlib import Path
p = Path("proposal_src.html"); s = p.read_text()
assert "v7_diecut_text" not in s, "已插入过"

# ① §04 接触表之后 —— 总说明
a = '<figcaption>引流款五件负责触达与拍照传播；主力款负责营收与客单价。十款共用同一套图腾与配色，货架上是一个系列而非十个单品。</figcaption></figure>'
assert a in s
s = s.replace(a, a + '''

<section class="col">
  <div class="note">
    <span class="tag">每款都有「无字版」与「加字版」两种</span>
    <p>上图为<strong>无字版</strong>——图腾干净、最耐看，也最像收藏品。但贵司提出「让人有带走的理由」，
    所以每款我们都另出一版<strong>把祝福语做进产品本身</strong>：无字版适合自留与陈列，加字版适合送人，
    两版共用同一套刀模与印版，<strong>不增加开模成本</strong>，只是印刷内容不同。</p>
    <p>建议做法：<strong>同一款同时上架两版</strong>，或按品类分——小件（冰箱贴、挂绳）走加字版做伴手礼，
    大件（杯垫、帆布袋）走无字版做日用。具体见 §11 与 §12。</p>
  </div>
</section>''', 1)

# ② 冰箱贴专题「一、图腾外形模切 × 五配色」之后
b = '<figcaption>蛙（多子多福）· 鸟（爱情美满）· 鱼（年年丰收）· 蝴蝶（美好爱情）· 龟（延年益寿）。外圈留白边即模切刀线位置。</figcaption></figure>'
assert b in s
s = s.replace(b, b + '''

<section class="col">
  <h4 style="font-family:inherit;font-size:16px;margin:30px 0 8px">加字版：三种做法</h4>
  <p>图腾即外形之后，产品本体没有平面留白可以放字。所以加字有三条路，成本与观感各不相同，
  请贵司圈选一种作为全系列统一做法：</p>
</section>

<figure class="shot"><img src="{{IMG:v7_diecut_text}}" alt="图腾外形模切的三种加字做法">
  <figcaption>① 底座条：图腾下接一条刀模底座，横排四字，仍是单件模切、成本不变。② 竖排侧栏：图腾偏左、右侧竖排八字加朱印，最像传统器物。③ 图腾纯粹：本体不加字，祝福语印在背卡上，保图腾完整。</figcaption></figure>

<section class="col">
  <p>我们的建议是 <strong>①</strong>。理由是它把字变成了产品轮廓的一部分——底座条本身就是刀模的一段，
  远看是图腾、近看有话，而且四字横排在冰箱上贴着时最好认。<strong>②</strong> 最有气质但占宽，
  小尺寸下字会太小；<strong>③</strong> 成本最低、图腾最纯粹，但字留在背卡上，游客拆开包装后那句话就没了——
  而「带走一句祝福」恰恰是要留在产品上的。</p>
</section>''', 1)

# ③ 冰箱贴专题「四种机关」之后
c = '<figcaption>转转（转动换图腾）· 对开门（船型屋开门露出大力神）· 滑轨（抽拉露出寓意）· 双层磁吸（前层镂空、后层撞色）。</figcaption></figure>'
assert c in s
s = s.replace(c, c + '''

<section class="col">
  <h4 style="font-family:inherit;font-size:16px;margin:30px 0 8px">加字版：让祝福语成为「被揭开的那句话」</h4>
  <p>机关款是全系列里加字最自然的一类——<strong>字不印在表面，而是转开、拉开、推开之后才出现。</strong>
  这样那句祝福不是被读到的，是被<strong>揭开</strong>的，动作本身成了一个小仪式，也解释了为什么它值 ¥35–49。</p>
</section>

<figure class="shot"><img src="{{IMG:v7_mech_text}}" alt="四种机关的加字版">
  <figcaption>转转：转动内盘，窗口依次显示图腾与对应祝福。对开门：推开是祖先纹与那句话。滑轨：抽出即是这一式的祝福语。双层磁吸：前层镂空图腾，后层透出朱字。</figcaption></figure>

<section class="col">
  <p><strong>滑轨</strong>与<strong>对开门</strong>两款的机关与内容咬合得最紧：滑轨抽出来的正好是一句话，
  对开门推开看到的正好是守护纹——机关不是噱头，是叙事的一部分。这两款建议优先做加字版。</p>

  <h4 style="font-family:inherit;font-size:16px;margin:30px 0 8px">其余 SKU 的加字版</h4>
  <p>同一套祝福语铺到相关品类上，排式随器形走：圆的走弧排，窄的走竖排，平的走双行竖排配朱印。</p>
</section>

<figure class="shot"><img src="{{IMG:v7_sku_text}}" alt="其余 SKU 的加字版">
  <figcaption>陶瓷杯垫（弧排环绕，上蓝下朱）· 亚克力挂绳（竖排四字，窄面最省空间）· 异形贴纸（每腾配四字，一版多句）· 本色帆布袋（纹样带 + 竖排题款 + 朱印）· 明信片／票根卡（双行竖排，留白最多）。</figcaption></figure>''', 1)

p.write_text(s)
import re
print("  ok; imgs=%d  section %d/%d" % (
    len(set(re.findall(r"\{\{IMG:(\w+)\}\}", s))), s.count("<section"), s.count("</section>")))
