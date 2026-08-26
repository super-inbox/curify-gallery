# -*- coding: utf-8 -*-
"""把不严格来自美孚黎族原稿的内容移入附录。只移动，不删除。

被移动的六块（客户 2026-08-26 指定）：
  A 八福：纹样与寓意对照 + 可用纹样与母题  —— 我方按公开资料整理，非客户图腾体系
  C 工艺参考：档次靠工艺，不靠品类        —— 工厂过往案例，非黎族
  D 设计方案：每款三选一                  —— V2 生成式草案，纹样为示意
  E 关于"老气" + 负面参考图               —— 吴哥/高棉素材
  F 冰箱贴 · V2 已出的三款                —— 同 D

运行一次即可；重复运行会被 assert 挡住。
"""
from pathlib import Path
import json

p = Path(__file__).resolve().parent / "proposal_src.html"
s = p.read_text()
assert 'id="appendix"' not in s, "已重构过，勿重复运行"
moved = {}


def line_start(text, idx):
    return text.rindex("\n", 0, idx) + 1


def back_to(text, idx, tag):
    """从 idx 向前找最近的 tag，返回其所在行行首。"""
    return line_start(text, text.rindex(tag, 0, idx))


def cut(name, anchor, start_tag, end_anchor, end_tag):
    """剪出 [start, end)。start_tag/end_tag 为 None 时以 anchor 所在行为界。"""
    global s
    a = s.index(anchor)
    i = back_to(s, a, start_tag) if start_tag else line_start(s, a)
    b = s.index(end_anchor, a)
    j = back_to(s, b, end_tag) if end_tag else line_start(s, b)
    moved[name] = s[i:j]
    s = s[:i] + s[j:]
    head = moved[name].strip().replace("\n", " ")[:40]
    print("  cut %s: %5d chars  <<%s...>>" % (name, len(moved[name]), head))


cut("A", "<h3>八福：纹样与寓意对照</h3>", None,
    "文化红线", '<div class="note warn">')
cut("C", "<h3>工艺参考：档次靠工艺", '<div class="col">',
    "<h2>设计方案：每款三选一</h2>", "</section>")
cut("D", "<h2>设计方案：每款三选一</h2>", "<section>",
    "<h2>纹样准确性", '<section class="col">')
cut("E", '<h3>关于"老气"', '<section class="col">',
    "<h3>配色方案：五选一</h3>", '<section class="col">')
cut("F", "<h3>一、V2 已出：图腾外形的三款</h3>", None,
    "<h3>二、新增：图腾外形模切", '<section class="col">')

# 主线保留核心结论，并指向附录
s = s.replace(
    "<h3>配色方案：五选一</h3>",
    "<h3>配色方案：五选一</h3>\n"
    "    <p>先说一句贯穿全案的判断：<strong>黎族图腾本身就是平面、几何、等宽笔画的</strong>"
    "——因为它们是织机上织出来的，网格决定了只能走正交与 45° 折线。所以"
    "<strong>越忠于原纹样，出来的东西越现代</strong>，「准确」与「不老气」在这个项目上不冲突。"
    '（负面参考的逐条拆解见<a href="#appendix">附录 A4</a>。）</p>', 1)

s = s.replace(
    '<p class="lede">景区文创里最走量的单品，值得单独铺开讲。以下含 V2 已出的方案与本轮新增的两组。</p>',
    '<p class="lede">景区文创里最走量的单品，值得单独铺开讲。以下全部基于贵司原稿图腾。</p>', 1)

s = s.replace("<h3>二、新增：图腾外形模切 × 五配色</h3>",
              "<h3>一、图腾外形模切 × 五配色</h3>", 1)
s = s.replace("<h3>三、新增：四种机关</h3>", "<h3>三、四种机关</h3>", 1)

(p.parent / "_moved_blocks.json").write_text(json.dumps(moved, ensure_ascii=False, indent=1))
p.write_text(s)
print("  OK  moved %d blocks; body now %d chars" % (len(moved), len(s)))
