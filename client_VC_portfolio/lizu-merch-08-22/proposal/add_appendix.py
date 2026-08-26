# -*- coding: utf-8 -*-
"""组装附录：被移出正文的五块 + 本轮新增的候选 SKU。"""
from pathlib import Path
import json, re

H = Path(__file__).resolve().parent
p = H / "proposal_src.html"
s = p.read_text()
assert 'id="appendix"' not in s, "附录已存在"
m = json.loads((H / "_moved_blocks.json").read_text())

INTRO = """<hr class="weave">

<section class="col" id="appendix">
  <p class="num">附录</p>
  <h2>附录 · 备查材料与追加候选</h2>
  <p class="lede">正文只保留严格取自贵司原稿图腾的内容。以下四类留档备查，不构成本次交付主张。</p>
  <div class="note warn">
    <span class="tag">为什么放在附录</span>
    <p>贵司要求图腾与黎锦<strong>不能有偏差</strong>。附录 A1–A4 的纹样<strong>不是</strong>来自贵司《掼蛋扑克纹样参考》原稿——A1 是我方依公开资料整理、A2 为合作工厂过往案例、A3 为生成式形式草案、A4 为吴哥/高棉负面参考。它们对判断方向仍有参考价值，但<strong>一律不作为下厂依据</strong>。</p>
    <p>A5 是本轮新增的追加候选 SKU，纹样均取自贵司原稿，只是尚未进入首批清单，待贵司圈选。</p>
  </div>
</section>

<section class="col">
  <h3>A1 · 八福对照表与母题（<u>已作废</u>，仅存档）</h3>
  <p>V2 阶段我方依公开资料整理的纹样体系。收到贵司原稿后已确认：其中<strong>稻穗纹、水波纹、太阳纹并不在贵司图腾体系内</strong>，而贵司体系中的龙、蝴蝶、牛、人骑牛、狗牙花、摇篮、龟、狗此前未收录。<strong>以正文 §09 的 15 式为准。</strong></p>
</section>

"""

A2 = """<section class="col">
  <h3>A2 · 工艺参考（合作工厂过往案例）</h3>
  <p>服务对象含故宫、国家博物馆、湖北省博物馆、南昌文旅等。<strong>非本项目设计稿</strong>，仅用于说明工艺水平——同样在 ¥20–60 价格带里，工艺决定它看起来是旅游纪念品还是文创商品。</p>
</section>

"""

A3 = """<section class="col">
  <h3>A3 · V2 生成式形式草案</h3>
  <p>用于快速探索<strong>器形、版式与配色</strong>的草案，纹样为示意性，<strong>不能下厂</strong>。器形方向已被正文采纳，纹样已全部替换为贵司原稿矢量。</p>
</section>

"""

A4 = """<section class="col">
  <h3>A4 · 负面参考拆解（贵司提供）</h3>
</section>

"""

A5 = """<hr class="weave">

<section class="col">
  <h3>A5 · 追加候选 SKU（纹样均取自贵司原稿）</h3>
  <p class="lede">参考太原北齐壁画博物馆店在售形态，补充两组候选。均<strong>未计入</strong>正文 §07 的首批配置与 ¥27,800 报价，供贵司圈选后再并入。</p>

  <h4 style="font-family:inherit;font-size:16px;margin:26px 0 8px">冰箱贴 · 图腾外形之外的五种器形</h4>
  <p>正文主推的「图腾外形模切」之外，博物馆店里真正走量的其实是<strong>圆角方形深底款</strong>——成本最低、最好陈列、也最不像旅游纪念品。以下五种可与模切款混搭，丰富货架层次。</p>
</section>

<figure class="shot"><img src="{{IMG:v4_magnet_shapes}}" alt="冰箱贴五种器形">
  <figcaption>圆角方形（主推备选）· 圆形徽章式（磁贴/胸针两用）· 票根式（写景区名与日期）· 立牌式（可立可贴）· 九宫格套装（一版九腾，收集感最强）。</figcaption></figure>

<section class="col">
  <p>其中<strong>票根式</strong>值得单独一提：把"白查村 / BAICHA / 年年丰收"排成门票样式，游客带走的是一张"到过这里"的凭证，比一个通用图案更有留存理由。<strong>九宫格套装</strong>则是把 15 式图腾变成收集品的最直接做法——一版九腾，凑齐是动机。</p>

  <h4 style="font-family:inherit;font-size:16px;margin:26px 0 8px">低成本可印刷品</h4>
  <p>全部<strong>免开模、起订低、单价个位数</strong>。作用不是赚钱，是<strong>把货架铺满并提高连带率</strong>——游客买了 ¥39 的冰箱贴，顺手加一件 ¥12 的清洁布，客单价就上去了。</p>
</section>

<figure class="shot"><img src="{{IMG:v4_cheap_skus}}" alt="低成本可印刷 SKU">
  <figcaption>镜片清洁布 · 异形贴纸套装 · 集章卡 + 印章 · 纸质书签套装 · 明信片／票根卡。</figcaption></figure>

<section class="col">
  <div class="scroll">
    <table style="min-width:560px">
      <thead><tr><th>单品</th><th>工艺</th><th class="n">起订</th><th class="n">开模</th><th class="n">单价</th><th class="n">建议零售</th></tr></thead>
      <tbody>
        <tr><td>镜片清洁布</td><td>超细纤维印花</td><td class="n">200</td><td class="n free">免</td><td class="n">¥3–5</td><td class="n">¥12–19</td></tr>
        <tr><td>异形贴纸套装</td><td>模切贴纸</td><td class="n">200</td><td class="n">¥300</td><td class="n">¥1.5–3</td><td class="n">¥9–19</td></tr>
        <tr><td>集章卡 + 印章</td><td>纸卡 + 木柄橡胶章</td><td class="n">200</td><td class="n">¥300</td><td class="n">¥2–4</td><td class="n">¥9–15</td></tr>
        <tr><td>纸质书签套装（四腾）</td><td>四色印刷 + 覆膜</td><td class="n">200</td><td class="n free">免</td><td class="n">¥3–5</td><td class="n">¥15–25</td></tr>
        <tr><td>明信片 / 票根卡</td><td>四色印刷</td><td class="n">200</td><td class="n free">免</td><td class="n">¥1–2</td><td class="n">¥6–12</td></tr>
      </tbody>
    </table>
  </div>

  <div class="note">
    <span class="tag">集章值得单独考虑</span>
    <p>太原那家店专门贴了「禁止在卫生纸、带毛的纸上盖章」的告示——<strong>说明盖章的人多到需要管理</strong>。景区做集章的价值不在卖章，在于<strong>它给了游客走完全程的理由</strong>：章分设在船型屋、织锦展示点、观景台，集齐换一张纪念卡。成本极低，但能直接改变游客的动线与停留时长，这是其他任何 SKU 都做不到的。</p>
  </div>
</section>

"""

parts = [INTRO, m["A"] + "\n\n", A2, m["C"] + "\n\n", A3,
         m["D"] + "\n\n" + m["F"] + "\n\n", A4, m["E"] + "\n\n", A5]
s = s.rstrip() + "\n\n" + "".join(parts)
p.write_text(s)
print("  appendix appended; body now %d chars" % len(s))
print("  section balance: %d / %d" % (s.count("<section"), s.count("</section>")))
print("  imgs: %s" % sorted(set(re.findall(r"\{\{IMG:(\w+)\}\}", s))))
