# -*- coding: utf-8 -*-
"""V6：简化纹样准确性 / 重排 SKU 表 / 新增国博款 / 接触表前置。"""
from pathlib import Path
import re

H = Path(__file__).resolve().parent
p = H / "proposal_src.html"
s = p.read_text()
assert "v6_contact_sheet" not in s, "已插入过"

# ── a. 纹样准确性：极简化 ─────────────────────────────────
i = s.index('<h2>纹样准确性')
i = s.rindex('<section class="col">', 0, i); i = s.rindex("\n", 0, i) + 1
j = s.index("</section>", i) + len("</section>\n")
SIMPLE = '''<section class="col">
  <p class="num">05</p>
  <h2>纹样准确性</h2>
  <p class="lede">这一条现在很简单：<strong>我们用的就是贵司自己在用的那 15 式。</strong></p>
  <p>纹样全部取自贵司《掼蛋扑克纹样参考》原稿，逐一矢量化，未作再创作，也没有引入任何
  外部素材或生成式产物。名称与寓意沿用贵司的官方口径。<strong>所以不存在"会不会有偏差"的问题——
  比对的对象就是原件本身。</strong></p>
  <p>唯一仍需贵司确认的是<strong>鹿图腾中央的一对万字纹</strong>（详见 §08）。若日后要扩充到
  15 式之外，我们会先取实物或图录，仍按"照原样描摹、不做再创作"处理。</p>
</section>

'''
s = s[:i] + SIMPLE + s[j:]

# ── b. SKU 表重排 ─────────────────────────────────────────
old_start = s.index('<tr><td><span class="chip c-b">主力</span></td><td>船型屋立体纸雕本 ★</td>')
old_end = s.index("</tbody>", old_start)
NEW_ROWS = '''<tr><td><span class="chip c-a">引流</span></td><td>图腾外形亚克力冰箱贴（同模 3 纹样）</td><td>UV 打印 + 激光切</td><td class="n">300</td><td class="n">¥300</td><td class="n">¥5.0</td><td class="n">300</td><td class="n">¥1,800</td></tr>
        <tr><td><span class="chip c-a">引流</span></td><td>木质开门冰箱贴</td><td>木质模切 + 丝印</td><td class="n">300</td><td class="n">¥300</td><td class="n">¥10.0</td><td class="n">300</td><td class="n">¥3,300</td></tr>
        <tr><td><span class="chip c-a">引流</span></td><td>亚克力钥匙扣 / 挂绳（同模 3 款）</td><td>UV 打印 + 激光切</td><td class="n">300</td><td class="n">¥300</td><td class="n">¥4.0</td><td class="n">300</td><td class="n">¥1,500</td></tr>
        <tr><td><span class="chip c-a">引流</span></td><td>异形贴纸套装 ★</td><td>模切贴纸</td><td class="n">200</td><td class="n">¥300</td><td class="n">¥2.5</td><td class="n">300</td><td class="n">¥1,050</td></tr>
        <tr><td><span class="chip c-a">引流</span></td><td>明信片 / 票根卡（白查十二时）</td><td>四色印刷</td><td class="n">200</td><td class="n">¥300</td><td class="n">¥7.0</td><td class="n">200</td><td class="n">¥1,700</td></tr>
        <tr><td><span class="chip c-b">主力</span></td><td>陶瓷杯垫（放射纹章 4 款）</td><td>釉面转印 + 软木底</td><td class="n">500</td><td class="n">¥300</td><td class="n">¥3.6</td><td class="n">500</td><td class="n">¥2,100</td></tr>
        <tr><td><span class="chip c-b">主力</span></td><td><strong>本色帆布袋（不覆膜）</strong></td><td>12oz 本色帆布 + 丝网印</td><td class="n">300</td><td class="n">¥300</td><td class="n">¥12.0</td><td class="n">300</td><td class="n">¥3,900</td></tr>
        <tr><td><span class="chip c-b">主力</span></td><td>集章卡 + 印章 ★</td><td>纸卡 + 木柄橡胶章</td><td class="n">200</td><td class="n">¥300</td><td class="n">¥3.0</td><td class="n">300</td><td class="n">¥1,200</td></tr>
      '''
s = s[:old_start] + NEW_ROWS + s[old_end:]
s = s.replace('<tr><td colspan="6">生产小计（含打样与刀模费 ¥1,800）</td><td class="n">约 2,000 件</td><td class="n">¥18,000</td></tr>',
              '<tr><td colspan="6">生产小计（含打样与刀模费 ¥2,400）</td><td class="n">约 2,400 件</td><td class="n">¥16,550</td></tr>')
s = s.replace('<tr><td>首批生产</td><td>7 款 · 约 2,000 件（含打样与刀模费 ¥1,800）</td><td class="n">¥18,000</td></tr>',
              '<tr><td>首批生产</td><td>8 款 · 约 2,400 件（含打样与刀模费 ¥2,400）</td><td class="n">¥16,550</td></tr>')
for a, b in (("¥27,800","¥26,350"), ("¥13,900","¥13,175"), ("¥8,340","¥7,905"), ("¥5,560","¥5,270")):
    s = s.replace(a, b)
s = s.replace("7 款 SKU，约 2,000 件，全部落在 ¥20–60 零售带内。数量不是我们定的，是工厂起订量定的。",
              "8 款 SKU，约 2,400 件，全部落在 ¥19–69 零售带内。数量不是我们定的，是工厂起订量定的。")
s = s.replace("7 款 SKU，但因为用了“同模不同图”，货架上实际是 <strong>16 个可收集的图案</strong>——冰箱贴 3 款、挂绳 3 款、杯垫 4 款，加上其余单品。",
              "8 款 SKU，但因为用了“同模不同图”，货架上实际是 <strong>20 个以上可收集的图案</strong>——冰箱贴 3 款、挂绳 3 款、杯垫 4 款、贴纸一版多腾，加上其余单品。")
s = s.replace("首批货值约 ¥6.2 万", "首批货值约 ¥6.6 万")

# ── c+d. 接触表 + 国博新款，插在「品类与选品」之前 ────────
k = s.index("<h2>品类与选品</h2>")
k = s.rindex("<section>", 0, k); k = s.rindex("\n", 0, k) + 1
NEW = '''<hr class="weave">

<section class="col">
  <p class="num">04</p>
  <h2>我们提议做什么：八款，两档</h2>
  <p class="lede">先给结论。以下是本次首批建议落地的完整清单，后面各节是它的展开与依据。</p>
  <p>全部使用贵司原稿的 15 式图腾，零售价全部落在 <strong>19–69 元</strong>。★ 为本轮依贵司提供的
  国博/敦煌参考新增。图中第 9、10 两款（折扇、木质滑动亮灯）为<strong>候选</strong>，未计入首批报价，
  贵司圈选后可替换或追加。</p>
</section>

<figure class="shot"><img src="{{IMG:v6_contact_sheet}}" alt="本次提案的完整 SKU 一览">
  <figcaption>引流款五件负责触达与拍照传播；主力款负责营收与客单价。十款共用同一套图腾与配色，货架上是一个系列而非十个单品。</figcaption></figure>

<section class="col">
  <div class="note">
    <span class="tag">这一版相对上一版的三处调整</span>
    <p><strong>① 贴纸与集章卡进主线。</strong>两者都免开模、200 起订、单价个位数，是把货架铺满与提高连带率最便宜的办法。集章尤其值得做——它给游客走完全程的理由，能改变动线与停留时长。</p>
    <p><strong>② 帆布袋去掉覆膜。</strong>改 12oz 本色帆布丝网印，单价从 ¥15 降到 ¥12，同时去掉塑料感（详见 §12）。</p>
    <p><strong>③ 船型屋立体纸雕本移出首批。</strong>它单价偏高、且与「简单系列」的定位不完全一致，移入附录作二期候选。</p>
  </div>
</section>

<hr class="weave">

<section class="col">
  <h2>依贵司国博参考新增的款式</h2>
  <p>贵司提供的国博/敦煌店参考里，有一款几乎是为本项目准备的：<strong>「五星出东方利中国」木质亮灯滑动冰箱贴</strong>——
  那件文物本身就是<strong>汉代织锦</strong>，与黎锦同类。它证明了一条路：织锦类文物完全可以做成有机关、有光、
  可把玩的木质产品，而不必停留在平面印刷。</p>
</section>

<figure class="shot"><img src="{{IMG:v6_museum_skus}}" alt="依国博参考新增的五款 SKU">
  <figcaption>木质滑动亮灯冰箱贴 · 十五式图腾格册 · 陶瓷杯垫放射纹章 · 织锦折扇 · 纸雕小夜灯。均以贵司原稿图腾生成。</figcaption></figure>

<section class="col">
  <ul class="plain">
    <li><strong>木质滑动亮灯冰箱贴</strong>——镇店款。拉动内片换景，背光透出织锦纹样。对标那件汉代织锦护臂的做法。</li>
    <li><strong>十五式图腾格册</strong>——借用生肖玲珑杯的格子构成。同一版面可作杯身、贴纸、集章卡三种载体，一次设计三处使用。</li>
    <li><strong>陶瓷杯垫 · 放射纹章</strong>——借用国博杯垫的花瓣构图，中心一腾、周围八腾，比平铺更有仪式感。</li>
    <li><strong>织锦折扇</strong>——海南气候下真正会被用起来的品类，扇面正好承载纹样带。</li>
    <li><strong>纸雕小夜灯</strong>——纸雕本的立体版本，分层透光打出船型屋剪影。</li>
  </ul>
  <p>其中前三款可直接并入首批（格册与杯垫已在清单内），<strong>折扇与滑动亮灯建议作为候选</strong>：
  两者单价与起订量都更高，适合在试销跑出数据后再上。</p>
</section>

'''
s = s[:k] + NEW + s[k:]

# 附录补一句：纸雕本移入
s = s.replace("<h3>A1 · 八福对照表与母题（<u>已作废</u>，仅存档）</h3>",
  "<h3>A0 · 船型屋立体纸雕本（移出首批 · 二期候选）</h3>\n"
  "  <p>现货结构、50 本起做、免开模，仍是很好的一款。移出首批的原因只是单价偏高，"
  "且与本轮「先做简单系列」的定位不完全一致。二期或礼盒线重启时优先考虑。</p>\n"
  "</section>\n\n<section class=\"col\">\n"
  "  <h3>A1 · 八福对照表与母题（<u>已作废</u>，仅存档）</h3>")

# 编号重排
apx = s.index('id="appendix"')
seq = iter(["%02d" % i for i in range(1, 40)])
s = re.sub(r'<p class="num">([^<]+)</p>',
           lambda m: m.group(0) if m.group(1) == "附录" else '<p class="num">%s</p>' % next(seq),
           s[:apx]) + s[apx:]

p.write_text(s)
print("  nums:", re.findall(r'<p class="num">([^<]+)</p>', s))
print("  section %d/%d" % (s.count("<section"), s.count("</section>")))
print("  imgs:", len(set(re.findall(r"\{\{IMG:(\w+)\}\}", s))))
