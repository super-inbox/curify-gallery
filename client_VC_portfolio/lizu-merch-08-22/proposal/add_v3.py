# -*- coding: utf-8 -*-
"""Append the V3 sections (2026-08-24 客户反馈) to proposal_src.html.
Adds only — nothing from V2 is removed."""
from pathlib import Path
p = Path("proposal_src.html"); s = p.read_text()
assert "V3 · 图腾库与配色扩展" not in s, "V3 已插入过，勿重复运行"

anchor = '<section class="col">\n  <p class="num">09</p>'
assert anchor in s

V3 = '''<hr class="weave">

<section class="col">
  <p class="num">09</p>
  <h2>V3 · 图腾库与配色扩展</h2>
  <p class="lede">8 月 23 日收到两份新材料后的补充方案。V2 的内容全部保留，这一节是新增。</p>

  <div class="note">
    <span class="tag">贵司提供的《掼蛋扑克纹样参考》解决了最大的一个卡点</span>
    <p>我们此前提出的最大风险是"纹样可能出偏差"，需要可追溯的考据源头。<strong>这份文件正是那个源头</strong>——它带有 15 个图腾的官方名称与寓意，且已经用在贵司自己的产品上。我们已把其中每一个图腾<strong>逐一提取为矢量图形</strong>，作为本项目的纹样母版。</p>
    <p>同时要更正我们 V2 里的一处：V2 的"八福"对照表是我们依据公开资料整理的，其中<strong>稻穗纹、水波纹、太阳纹并不在贵司的图腾体系内</strong>，而贵司体系中的<strong>龙、蝴蝶、牛、人骑牛、狗牙花、摇篮、龟、狗</strong>我们此前没有收录。<strong>以下 15 式为准，V2 的八福表作废。</strong></p>
  </div>
</section>

<figure class="shot"><img src="{{IMG:v3_library}}" alt="美孚黎族图腾库 15 式">
  <figcaption>全部取自贵司原稿逐一矢量化，未作再创作。这套矢量库交付后归贵司所有，可持续用于后续产品。</figcaption></figure>

<section class="col">
  <h3>关于"老气"：问题不在民族元素，在处理手法</h3>
  <p>贵司提供的几张负面参考（吴哥/高棉主题纪念品）指向同一组特征，我们把它拆开，作为本项目的<strong>反向清单</strong>：</p>
  <div class="scroll">
    <table style="min-width:560px">
      <thead><tr><th>老气的来源</th><th>本项目的做法</th></tr></thead>
      <tbody>
        <tr><td>土黄、褐、暗红等低彩度暖土色</td><td>墨蓝为主，或高明度浅底；暖色只作点缀</td></tr>
        <tr><td>做旧质感（软木、仿古木、牛皮纸、泛黄）</td><td>干净平涂、哑光釉、原色帆布，不做旧</td></tr>
        <tr><td>写实浮雕拓片与实景照片</td><td>平面几何图腾，单色剪影</td></tr>
        <tr><td>满版繁复花边，不留白</td><td>大留白，单一主体居中</td></tr>
        <tr><td>深底 + 大面积描金</td><td>金只用于极细分割线，或完全不用</td></tr>
      </tbody>
    </table>
  </div>
  <p><strong>这里有一个对我们有利的巧合：黎族图腾本身就是平面、几何、等宽笔画的</strong>——因为它们是织机上织出来的，网格结构决定了只能走正交与 45° 折线。所以<strong>越忠于原纹样，出来的东西越现代</strong>。准确性和"不老气"这两个要求，在这个项目上指向同一个方向，不冲突。</p>
</section>

<figure class="shot"><img src="{{IMG:v3_negcases}}" alt="客户提供的负面参考案例">
  <figcaption>贵司提供的负面参考。问题不在于"用了民族纹样"，而在于土色系 + 做旧质感 + 写实浮雕 + 满版无留白这一组处理手法。</figcaption></figure>

<section class="col">
  <h3>配色方案：五选一</h3>
  <p>下面五套配色用的是<strong>同一组真实图腾</strong>，只换配色。请贵司圈选一套作为全系列基调，或指定"主推一套 + 备选一套"（不同品类可分用，例如杯垫走 B、小件走 C）。</p>
</section>

<figure class="shot"><img src="{{IMG:v3_colorways}}" alt="五套配色方案">
  <figcaption>A 墨蓝本白（V2 已定基调）· B 浅底反转（留白最多、最不老气）· C 海岛明快 · D 椰林清新 · E 暖阳撞色</figcaption></figure>

<section class="col">
  <p>我们的建议：<strong>以 B（浅底反转）作为主基调，A 作为深色系列的补充</strong>。理由是浅底最能拉开与负面参考的距离——那几款的共同点正是深色底加满版纹样。C 与 E 适合放在小件引流款上做跳色，让货架有层次而不散。</p>

  <h3>版式方案：四选一</h3>
  <p>配色之外的另一个变量是排布方式。同一个图腾可以有四种做法，决定了产品是"安静"还是"热闹"：</p>
</section>

<figure class="shot"><img src="{{IMG:v3_shapes}}" alt="四种版式方案">
  <figcaption>① 单一主体大留白 · ② 超大裁切局部特写 · ③ 网格重复满版 · ④ 横向纹样带</figcaption></figure>

<section class="col">
  <p>② 超大裁切是这四种里最现代的一种——把图腾放大到出血、只保留局部，是当代平面设计的常用手法，也最不可能被看成旅游纪念品。建议至少在一款主力品（帆布袋或方巾）上用它。</p>

  <h3>落到产品上</h3>
</section>

<figure class="shot"><img src="{{IMG:v3_products}}" alt="新配色的产品应用">
  <figcaption>冰箱贴取图腾外形模切；杯垫走浅底与撞色两版；帆布袋分别用鸟图腾与狗牙花图腾。所有纹样均为贵司原稿矢量，非再创作。</figcaption></figure>

<section class="col">
  <div class="note warn">
    <span class="tag">需要贵司确认：鹿图腾中的万字纹</span>
    <p>贵司原稿的<strong>鹿图腾</strong>中央有一对<strong>万字纹（卍 / 卐）</strong>。在黎锦与中国传统语境中这是正当的吉祥符号，寓意万福万寿，且已经用在贵司现有的扑克牌上，我们不会擅自改动。</p>
    <p>但需要提请注意：<strong>该符号与纳粹标志在外形上高度接近</strong>，海南有境外游客，商品又会被拍照传播。作为国企主体，这一点值得先做个决定。三个选项供选：<strong>①</strong> 照原样使用（文化上完全站得住）；<strong>②</strong> 鹿图腾保留、仅省略中央万字部分；<strong>③</strong> 鹿图腾只用于内销导向的品类。<strong>这是贵司的决定，我们按指示执行。</strong></p>
  </div>

  <h3>这一版之后还需要什么</h3>
  <ul class="plain">
    <li><strong>圈定配色</strong>（五选一，或主推 + 备选）与<strong>版式</strong>（四选一）</li>
    <li><strong>鹿图腾万字纹</strong>按上面三个选项择一</li>
    <li>若能提供<strong>原稿矢量文件</strong>（AI / EPS / CDR），精度会高于我们从图片提取的版本；没有也不影响推进</li>
    <li>确认后即可进入正式设计：15 式图腾 × 选定配色 × 选定版式，按品类铺开</li>
  </ul>
</section>

'''
s = s.replace(anchor, V3 + anchor, 1)
# 09/10 顺延为 10/11
import re
tail = s[s.index(V3) + len(V3):]
tail = tail.replace('<p class="num">09</p>', '<p class="num">10</p>', 1)
tail = tail.replace('<p class="num">10</p>', '<p class="num">11</p>', 1) if tail.count('<p class="num">10</p>') > 1 else tail
s = s[:s.index(V3) + len(V3)] + tail
Path("proposal_src.html").write_text(s)
print("  ✓ V3 章节已插入")
