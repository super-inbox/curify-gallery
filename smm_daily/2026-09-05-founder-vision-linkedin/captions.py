#!/usr/bin/env python3
"""Turn Scribe word timings into a burned-in caption track (ASS)."""
import json, os, sys

SCRIBE = sys.argv[1]
OUT    = sys.argv[2]
MIN_DUR = 0.6

words = [w for w in json.load(open(SCRIBE))["words"] if w.get("type") == "word"]

MAX_CH, TARGET = 34, 25

def is_end(w):            # sentence-final punctuation forces a break
    return w["text"].rstrip().endswith((".", "?", "!", ":"))

def cue_text(a, b):
    return " ".join(w["text"] for w in words[a:b])

def cue_cost(a, b):
    """Penalise over-long lines, stubby tails, and breaks that cut a phrase."""
    t = cue_text(a, b)
    if len(t) > MAX_CH:
        return None
    c = 0.06 * (len(t) - TARGET) ** 2
    if (b - a) <= 2 and not is_end(words[b - 1]):
        c += 9.0
    if b < len(words):                      # reward breaking on a natural beat
        gap = words[b]["start"] - words[b - 1]["end"]
        c -= min(gap, 0.9) * 11.0
        if is_end(words[b - 1]):
            c -= 14.0
        elif words[b - 1]["text"].rstrip().endswith(","):
            c -= 6.0
    return c

# Shortest-path line breaking over the word sequence.
N = len(words)
best = [float("inf")] * (N + 1); back = [0] * (N + 1); best[0] = 0.0
for b in range(1, N + 1):
    for a in range(max(0, b - 9), b):
        if best[a] == float("inf"):
            continue
        if any(is_end(words[k]) for k in range(a, b - 1)):
            continue                        # never run past a sentence end
        c = cue_cost(a, b)
        if c is None:
            continue
        if best[a] + c < best[b]:
            best[b] = best[a] + c; back[b] = a

bounds, b = [N], N
while b > 0:
    b = back[b]; bounds.append(b)
bounds.reverse()
cues = [dict(start=words[a]["start"], end=words[b - 1]["end"], text=cue_text(a, b))
        for a, b in zip(bounds, bounds[1:])]

# Hold each cue until the next one starts (up to 0.4s) so captions never flicker.
for i, c in enumerate(cues):
    nxt = cues[i + 1]["start"] if i + 1 < len(cues) else c["end"] + 0.4
    c["end"] = min(max(c["end"] + 0.28, c["start"] + MIN_DUR), nxt - 0.01)

def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1350
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter,54,&H00FFFFFF,&H00FFFFFF,&HDD101014,&H90000000,-1,0,0,0,100,100,0.6,0,1,5,2,2,80,80,64,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
lines = [f"Dialogue: 0,{ts(c['start'])},{ts(c['end'])},Cap,,0,0,0,,{c['text']}" for c in cues]
open(OUT, "w").write(head + "\n".join(lines) + "\n")
print(f"{len(cues)} cues -> {OUT}")
for c in cues[:6]:
    print(f"  {c['start']:6.2f}-{c['end']:6.2f}  {c['text']}")
