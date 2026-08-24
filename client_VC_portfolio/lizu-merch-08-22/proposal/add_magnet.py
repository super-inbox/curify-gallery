# -*- coding: utf-8 -*-
"""追加「冰箱贴专题」章节。只增不删。"""
from pathlib import Path
import re
p = Path("proposal_src.html"); s = p.read_text()
assert "冰箱贴专题" not in s, "已插入过"

anchor = '<section class="col">\n  <p class="num">10</p>'
assert anchor in s

SEC = '''<hr class="weave">

<section class="col">
  <p class="num">10</p>
  <h2>冰箱贴专题：从贴片到有机关的小物</h2>
  <p class="lede">景区文创里最走量的单品，值得单独铺开讲。以下含 V2 已出的方案与本轮新增的两组。</p>
  <p>冰箱贴是引流款的主力：单价低、决策快、几乎人人会买一个。但也正因为门槛低，它最容易做成"到此一游"。我们的思路是<strong>用同一副刀模承载多个图腾拉出款式，再用机关把其中一两款抬到主力价位</strong>。</p>

  <h3>一、V2 已出：图腾外形的三款</h3>
  <p>上一版的形式是对的——刀线沿图腾轮廓走，产品本身就是图腾。但当时纹样是模型示意的，与贵司图腾体系有出入。这一版起，全部换成贵司原稿矢量。</p>
</section>

<figure class="shot"><img src="{{IMG:v2_magnet}}" alt="V2 图腾外形冰箱贴三款">
  <figcaption>V2 方案（形式参考）。器形方向保留，纹样已按贵司《掼蛋扑克纹样参考》原稿全部替换。</figcaption></figure>

<section class="col">
  <h3>二、新增：图腾外形模切 × 五配色</h3>
  <p>下表是 5 个图腾 × 5 套配色的全组合。<strong>请贵司先定配色行，再圈款式列。</strong>同一副刀模下换图案不额外增加起订量，所以"款式多"在这里几乎是免费的——这是冰箱贴最适合做成收集系列的原因。</p>
</section>

<figure class="shot"><img src="{{IMG:v3_magnet_diecut}}" alt="冰箱贴 图腾外形模切 五配色">
  <figcaption>蛙（多子多福）· 鸟（爱情美满）· 鱼（年年丰收）· 蝴蝶（美好爱情）· 龟（延年益寿）。外圈留白边即模切刀线位置。</figcaption></figure>

<section class="col">
  <h3>三、新增：四种机关</h3>
  <p>这一组回应"要有巧思"与"不老气"。机关款的价值不只在好玩——<strong>它让冰箱贴从 ¥19 的顺手货变成 ¥35–49 的主动选择</strong>，也是货架上唯一会被拿起来玩一下的东西。以下四种都是工厂现有工艺，不需要为我们单独开发。</p>
</section>

<figure class="shot"><img src="{{IMG:v3_magnet_mech}}" alt="冰箱贴四种机关工艺">
  <figcaption>转转（转动换图腾）· 对开门（船型屋开门露出大力神）· 滑轨（抽拉露出寓意）· 双层磁吸（前层镂空、后层撞色）。</figcaption></figure>

<section class="col">
  <p>其中<strong>对开门</strong>与本项目最契合：船型屋是白查村最强的识别符号，"推开门看见祖先纹"这个动作本身就是叙事，吊牌上写"推开门，把守护带回家"即可。<strong>滑轨</strong>则是唯一能把八福寓意直接做进产品的形式——图腾在左，抽出来是这句话。</p>

  <h3>四、工艺 × 起订 × 价格对照</h3>
  <p>以下取自三家工厂的正式报价单，非估算。请注意<strong>起订量与工期差异极大</strong>，机关款普遍要 500 件起、30 天以上。</p>
</section>

<div class="scroll">
  <table>
    <thead>
      <tr><th>工艺</th><th class="n">起订</th><th class="n">刀模/开模</th><th class="n">单价</th><th class="n">建议零售</th><th class="n">大货工期</th><th>备注</th></tr>
    </thead>
    <tbody>
      <tr><td>亚克力单层 · 图腾外形模切</td><td class="n free">300</td><td class="n">¥300</td><td class="n">¥4–6</td><td class="n">¥19–25</td><td class="n">15–18 天</td><td>同模可出多图案</td></tr>
      <tr><td>木质平面</td><td class="n free">300</td><td class="n">¥300</td><td class="n">¥8–12</td><td class="n">¥29–35</td><td class="n">18–20 天</td><td>质感优于亚克力</td></tr>
      <tr><td><strong>木质开门款</strong></td><td class="n free">300</td><td class="n">¥300</td><td class="n">¥10–12</td><td class="n">¥35–39</td><td class="n">18–20 天</td><td><strong>唯一在价格带内的机关款</strong></td></tr>
      <tr><td>金属平面 / 字绘</td><td class="n">500</td><td class="n">¥600–1,000</td><td class="n">¥7–9</td><td class="n">¥29–35</td><td class="n">22–25 天</td><td>需 500 件起</td></tr>
      <tr><td>金属转转 / 滑轨 / 双层磁吸</td><td class="n">500</td><td class="n">¥1,000</td><td class="n">¥22–30</td><td class="n">¥59–79</td><td class="n">25–30 天</td><td>⚠️ 超出 ¥20–60 价格带</td></tr>
      <tr><td>金属对开门 / 吊坠</td><td class="n">500</td><td class="n">¥1,500</td><td class="n">¥25–35</td><td class="n">¥69–89</td><td class="n">25–30 天</td><td>⚠️ 超出价格带</td></tr>
      <tr><td>树脂立体</td><td class="n">500</td><td class="n">¥1,000–1,200</td><td class="n">¥8.5–20</td><td class="n">¥35–49</td><td class="n">30–35 天</td><td>工期最长</td></tr>
      <tr><td>毛绒</td><td class="n">500</td><td class="n">¥1,200</td><td class="n">¥9.5–12.5</td><td class="n">¥35–45</td><td class="n">30–35 天</td><td>触感差异化</td></tr>
    </tbody>
  </table>
</div>

<section class="col">
  <div class="note warn">
    <span class="tag">一个需要贵司权衡的冲突</span>
    <p>会议定的零售价带是 ¥20–60，但<strong>金属机关款（转转、对开门、滑轨）的成本决定了它必然卖到 ¥59–89</strong>，要么破价格带，要么不做。这是工厂报价的硬约束，不是我们的定价选择。</p>
    <p>我们的建议：<strong>首批用「木质开门款」担任机关角色</strong>——300 件起、开模仅 ¥300、零售 ¥35–39 稳在带内，而且木质的质感恰好避开负面参考里的塑料感。金属机关款留到试销之后：如果开门款卖得动，说明"机关"这个点成立，那时再上金属版并单独给它一个 ¥69–89 的镇店位，就有数据支撑了。</p>
  </div>

  <h3>五、建议的首批冰箱贴组合</h3>
  <div class="scroll">
    <table style="min-width:520px">
      <thead><tr><th>角色</th><th>做法</th><th class="n">款式</th><th class="n">数量</th><th class="n">零售</th></tr></thead>
      <tbody>
        <tr><td><span class="chip c-a">引流</span></td><td>亚克力图腾外形模切（同模）</td><td class="n">3 个图腾</td><td class="n">300</td><td class="n">¥19–25</td></tr>
        <tr><td><span class="chip c-b">主力</span></td><td>木质开门款 · 船型屋外形</td><td class="n">1–2 款</td><td class="n">300</td><td class="n">¥35–39</td></tr>
      </tbody>
    </table>
  </div>
  <p>这个组合与 §07 首批配置里已列的两行冰箱贴一致（亚克力 300 件 ¥1,800、木质开门 300 件 ¥3,300），<strong>不增加预算</strong>，只是把款式与机关讲清楚了。若要再加金属机关款做镇店，需另加约 ¥12,000–16,000（500 件 × ¥25–30 + 开模 ¥1,500），请贵司定夺是否值得破价格带。</p>
</section>

'''
s = s.replace(anchor, SEC + anchor, 1)
seq = iter([f"{i:02d}" for i in range(1, 20)])
s = re.sub(r'<p class="num">\d+</p>', lambda m: f'<p class="num">{next(seq)}</p>', s)
Path("proposal_src.html").write_text(s)
print("  ✓ 冰箱贴专题已插入")
print("  章节:", re.findall(r'<p class="num">(\d+)</p>', s))
