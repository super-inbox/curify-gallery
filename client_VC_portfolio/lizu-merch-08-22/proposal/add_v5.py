# -*- coding: utf-8 -*-
"""V5：祝福语 / 黎锦元素 / 复合冰箱贴 / 材质 / 白查十二时；并把附录 A5 提到正文。"""
from pathlib import Path
import re

H = Path(__file__).resolve().parent
p = H / "proposal_src.html"
s = p.read_text()
assert "V5 新增" not in s, "已插入过"

# ── 1. 把附录 A5 整块剪出（提到正文）──────────────────────
a = s.index("<h3>A5 · 追加候选 SKU")
i = s.rindex('<section class="col">', 0, a)
i = s.rindex("\n", 0, i) + 1
# A5 一直到附录结束（文件尾）
a5 = s[i:].rstrip() + "\n"
s = s[:i].rstrip() + "\n"
# A5 内的小标题降级适配正文
a5 = a5.replace("<h3>A5 · 追加候选 SKU（纹样均取自贵司原稿）</h3>",
                "<h2>更多 SKU：器形与低成本印刷品</h2>")
a5 = a5.replace(
  '<p class="lede">参考太原北齐壁画博物馆店在售形态，补充两组候选。均<strong>未计入</strong>正文 §07 的首批配置与 ¥27,800 报价，供贵司圈选后再并入。</p>',
  '<p class="lede">参考太原北齐壁画博物馆店在售形态。以下均<strong>未计入</strong>首批配置与 ¥27,800 报价，供贵司圈选后并入。</p>')
a5 = a5.replace('<hr class="weave">\n\n', "", 1)
a5 = a5.replace('<section class="col">\n  <h3>A5', '<section class="col">\n  <p class="num">14</p>\n  <h3>A5', 1)

MAT = """<hr class="weave">

<section class="col">
  <p class="num">13</p>
  <h2>材质说明：覆膜帆布袋建议改掉</h2>
  <p class="lede">贵司问覆膜帆布袋是否合适。我们的意见是：<strong>不合适，建议换。</strong></p>

  <p><strong>覆膜</strong>是在印好的帆布表面压一层塑料薄膜。它便宜、颜色鲜艳、略防水，但代价是三条：手感发硬发假、<strong>有明显塑料感</strong>；折叠处日久起皱开裂、膜会翘边；不透气也不好洗。</p>
  <p>更要紧的是它和本项目的方向冲突。我们在负面参考里列的第一条就是"塑料感与做旧感"，而覆膜恰恰把一只本可以有布纹质感的袋子，变成一张亮面塑料片。<strong>贵司畅销款之所以成立，靠的正是真实材质——木、织物、银</strong>，覆膜是反方向。</p>

  <h3>建议的三种替代</h3>
  <div class="scroll">
    <table style="min-width:640px">
      <thead><tr><th>方案</th><th>做法</th><th class="n">单价</th><th>适合</th></tr></thead>
      <tbody>
        <tr><td><strong>① 本色加厚帆布 + 丝网印</strong><br><span style="color:var(--muted);font-size:12px">推荐</span></td>
            <td>12oz 全棉本色帆布，水性丝网印。无膜、可水洗、越用越软</td>
            <td class="n">¥16–24</td><td>主力款，质感与价格最平衡</td></tr>
        <tr><td><strong>② 帆布 + 真实织锦拼接</strong><br><span style="color:var(--red);font-size:12px">最贴合畅销款逻辑</span></td>
            <td>袋身丝网印，袋口或袋底缝一条真实黎锦织带（宽 4–6cm）</td>
            <td class="n">¥26–38</td><td>形象款。把畅销款赢在"真实织物"这一点直接搬过来</td></tr>
        <tr><td>③ RPET 再生涤纶折叠袋</td>
            <td>轻、可折进小袋、真防水，带环保叙事</td>
            <td class="n">¥12–18</td><td>更实用向：游客当天就能装东西、能塞进行李</td></tr>
      </tbody>
    </table>
  </div>

  <div class="note">
    <span class="tag">如果只能选一个</span>
    <p>选 <strong>②</strong>。织带是整只袋子上唯一"摸得到"的黎族元素，成本只增加 ¥6–10，却把产品从"印着图案的帆布袋"变成"带着一段黎锦的帆布袋"——这正是贵司畅销款已经验证过的东西。织带可向本地织娘小批量定制，同时构成一条可讲的在地供应链故事。</p>
    <p>若追求实用与轻便，③ 作为补充款并行；<strong>③ 不能替代 ②</strong>，涤纶没有质感叙事。</p>
  </div>
</section>

"""

V5 = """<hr class="weave">

<section class="col">
  <p class="num">11</p>
  <h2>祝福语：给游客一个带走的理由</h2>
  <p class="lede">V5 新增。图腾不只是图案，每一式都对应一句可以送人的话。</p>
  <p>纪念品和礼物的区别，在于<strong>有没有一句话可以随手说出口</strong>。"这是黎族的蛙纹"是知识；"多子多福，雨水丰沛"是祝福——后者才让人愿意多买一个送人。以下 15 句由贵司原稿的官方寓意改写，可直接印在吊牌与背卡上。</p>
</section>

<figure class="shot"><img src="{{IMG:v5_blessings}}" alt="十五式图腾与祝福语">
  <figcaption>每款产品认领一句。吊牌正面写祝福语，背面写纹样名与出处——收藏性与赠礼性一次给足。</figcaption></figure>

<section class="col">
  <h2 style="margin-top:34px">黎锦元素：畅销款真正抓眼的东西</h2>
  <p>看过贵司畅销款后，有一处必须修正我们此前的做法。<strong>那几款卖得好，靠的不是单一图腾，而是密集的织锦纹样 + 木框 + 银饰这三层材质叠加。</strong>我们之前的方案偏"极简单腾"，在货架上会显得单薄。</p>
  <p>好消息是黎锦的结构本身就是<strong>「图腾横向重复 + 行间细线」</strong>，所以可以用 15 式忠实生成纹样带，不需要另找素材，也不会引入偏差。</p>
</section>

<figure class="shot"><img src="{{IMG:v5_brocade}}" alt="由真实图腾生成的黎锦纹样带">
  <figcaption>四种纹样带，全部由 15 式图腾按黎锦的行列结构生成。可用作产品底纹、包装边饰、背卡装饰与织带图稿。</figcaption></figure>

<section class="col">
  <h2 style="margin-top:34px">冰箱贴 · 复合款（回应"不能只有图腾"）</h2>
  <p>贵司提出冰箱贴不能只有图腾图案，需要平衡复杂度与吸引力。以下四款直接对标畅销款的材质层次：<strong>米色品牌背卡 + 木框 + 织锦纹样 + 金色图腾 + 银饰 + 祝福语</strong>，图腾退为视觉焦点而非全部内容。</p>
</section>

<figure class="shot"><img src="{{IMG:v5_magnet_composite}}" alt="复合式冰箱贴四款">
  <figcaption>圆形木框织锦嵌片 · 筒裙形织锦满嵌 · 扇形纹样带加银饰 · 方形卡装纹样带底。造型取自贵司畅销款的成功形制。</figcaption></figure>

<section class="col">
  <div class="note">
    <span class="tag">关于那款"太现代"的参考</span>
    <p>贵司提供的掐丝珐琅 Q 版磁贴（卡通人物 + 金线满彩）被判为太现代。加上此前的吴哥土色拓片被判为老气，贵司的口味区间其实已经被两头框定了——<strong>而畅销款正落在中间：真实材质、密集织锦、克制配色、不卡通。</strong>上面这组就是照着这个中点做的。</p>
  </div>
</section>

<hr class="weave">

<section class="col">
  <p class="num">12</p>
  <h2>「白查十二时」· 纸品系列</h2>
  <p class="lede">会议已定方向 C 只用于纸品。这里把它做成一条可收集的六件套。</p>
  <p>以六个时辰串起村落的一天：晨炊、织锦、稻田、溪浴、归家、火塘。每张配一式图腾与一句短句，底部统一压一条黎锦纹样带。<strong>成套是收集动机</strong>——单张 ¥6–12，六张成套可卖 ¥39–49，是提高客单价最便宜的办法。</p>
</section>

<figure class="shot"><img src="{{IMG:v5_baicha12}}" alt="白查十二时六件套">
  <figcaption>同一套画面可同时做明信片、贴纸与书签三种载体，共用一次设计费。</figcaption></figure>

<section class="col">
  <p>这条系列还有一个额外用处：<strong>它是整个商品线里唯一有"场景"的部分。</strong>其余产品讲的是纹样与寓意，这六张讲的是"白查村的一天长什么样"——对没来过的人是种草，对来过的人是回忆锚点。建议同时用作景区导览图与门票背面的视觉。</p>
</section>

"""

# ── 2. 插入：正文尾部（在「需要贵司提供的资料」之前）────────
anchor_i = s.index("<h2>需要贵司提供的资料</h2>")
sec_i = s.rindex('<section class="col">', 0, anchor_i)
sec_i = s.rindex("\n", 0, sec_i) + 1
s = s[:sec_i] + V5 + MAT + a5 + "\n" + s[sec_i:]

# ── 3. 附录说明同步（A5 已移出）────────────────────────────
s = s.replace("<p>A5 是本轮新增的追加候选 SKU，纹样均取自贵司原稿，只是尚未进入首批清单，待贵司圈选。</p>",
              "<p>原附录 A5「追加候选 SKU」已按贵司要求<strong>提到正文</strong>（见 §14）。</p>")

# ── 4. 重排编号 ────────────────────────────────────────────
apx = s.index('id="appendix"')
seq = iter(["%02d" % i for i in range(1, 40)])
def renum(m):
    return m.group(0) if m.group(1) == "附录" else '<p class="num">%s</p>' % next(seq)
s = re.sub(r'<p class="num">([^<]+)</p>', renum, s[:apx]) + s[apx:]

p.write_text(s)
print("  nums:", re.findall(r'<p class="num">([^<]+)</p>', s))
print("  h2 count:", len(re.findall(r"<h2>", s)))
print("  section balance %d/%d" % (s.count("<section"), s.count("</section>")))
print("  imgs:", len(set(re.findall(r"\{\{IMG:(\w+)\}\}", s))))
