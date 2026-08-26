# -*- coding: utf-8 -*-
"""块 F 的剪切把冰箱贴专题小节的 </section> 一并带走，导致正文少一个闭合标签。
把它还给正文，并从附录块里剥掉。"""
from pathlib import Path
import json

H = Path(__file__).resolve().parent
p = H / "proposal_src.html"
s = p.read_text()
mp = H / "_moved_blocks.json"
m = json.loads(mp.read_text())

# 1) 附录块 F 去掉那个孤立的 </section>（它在块中间，不在末尾）
f = m["F"]
assert f.count("</section>") == 1 and f.count("<section") == 0, (f.count("<section"), f.count("</section>"))
m["F"] = f.replace("</section>\n", "", 1)
mp.write_text(json.dumps(m, ensure_ascii=False, indent=1))

# 2) 正文：冰箱贴专题引言段后补回 </section>
anchor = "（V2 阶段的三款形式草案见"
if anchor in s:
    end = s.index("</p>", s.index(anchor)) + 4
else:
    key = "再用机关把其中一两款抬到主力价位</strong>。</p>"
    end = s.index(key) + len(key)
s = s[:end] + "\n</section>\n" + s[end:]

p.write_text(s)
print("  body <section %d / </section> %d" % (s.count("<section"), s.count("</section>")))
tot_o = sum(v.count("<section") for v in m.values())
tot_c = sum(v.count("</section>") for v in m.values())
print("  moved <section %d / </section> %d" % (tot_o, tot_c))
