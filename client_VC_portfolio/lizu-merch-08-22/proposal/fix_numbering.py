# -*- coding: utf-8 -*-
"""附录里的 D 块仍带 <h2> 与旧编号，降级为 A3 的一部分；正文重排 01..N。"""
from pathlib import Path
import re

p = Path(__file__).resolve().parent / "proposal_src.html"
s = p.read_text()

# 1) 附录内的「设计方案：每款三选一」降级：去掉 num、h2 → h3
i = s.index('id="appendix"')
head, tail = s[:i], s[i:]
tail = tail.replace('    <p class="num">05</p>\n', "", 1)
tail = tail.replace("<h2>设计方案：每款三选一</h2>",
                    "<h3>A3-1 · 设计方案：每款三选一（生成式草案）</h3>", 1)
tail = tail.replace('<p class="lede">按会议要求，每个产品出三个方向供选。以下为首批四款的设计草案。</p>',
                    '<p>按会议要求每款出三个方向。<strong>纹样为示意，不能下厂</strong>；器形方向已被正文采纳。</p>', 1)
s = head + tail

# 2) 正文重排 01..N（附录保持「附录」二字）
def renum(text):
    seq = iter(["%02d" % i for i in range(1, 40)])
    def rep(m):
        return m.group(0) if m.group(1) == "附录" else '<p class="num">%s</p>' % next(seq)
    return re.sub(r'<p class="num">([^<]+)</p>', rep, text)

i = s.index('id="appendix"')
s = renum(s[:i]) + s[i:]

p.write_text(s)
print("  num 序列:", re.findall(r'<p class="num">([^<]+)</p>', s))
print("  正文 h2 数:", len(re.findall(r"<h2>", s[: s.index('id=\"appendix\"')])))
