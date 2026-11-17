import json
from collections import defaultdict
from pathlib import Path

FILE_A = Path("nano_templates_336.json")
FILE_B = Path("nano_templates_289.json")

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

A = load(FILE_A)
B = load(FILE_B)

print(f"A templates: {len(A)}")
print(f"B templates: {len(B)}")

# ---------------------------
# Index by template id
# ---------------------------
mapA = {t["id"]: t for t in A}
mapB = {t["id"]: t for t in B}

idsA = set(mapA)
idsB = set(mapB)

print("\nID diff:")
print("  Missing in B:", idsA - idsB)
print("  Missing in A:", idsB - idsA)

# ---------------------------
# Helpers
# ---------------------------
def keyset(obj):
    return set(obj.keys()) if isinstance(obj, dict) else set()

def diff_keys(a, b):
    return sorted(a - b), sorted(b - a)

# ---------------------------
# Deep comparison
# ---------------------------
problems = defaultdict(list)

for tid in sorted(idsA & idsB):
    ta = mapA[tid]
    tb = mapB[tid]

    # 1️⃣ Top-level keys
    miss_b, miss_a = diff_keys(keyset(ta), keyset(tb))
    if miss_b or miss_a:
        problems[tid].append(("top_level", miss_b, miss_a))

    # 2️⃣ Locales
    la = ta.get("locales", {})
    lb = tb.get("locales", {})

    miss_b, miss_a = diff_keys(set(la), set(lb))
    if miss_b or miss_a:
        problems[tid].append(("locales_missing", miss_b, miss_a))

    # 3️⃣ Locale internal keys
    for loc in set(la) & set(lb):
        ka = keyset(la[loc])
        kb = keyset(lb[loc])
        miss_b, miss_a = diff_keys(ka, kb)
        if miss_b or miss_a:
            problems[tid].append((f"locale:{loc}", miss_b, miss_a))

    # 4️⃣ Parameters
    pa = {p["name"]: p for p in ta.get("parameters", [])}
    pb = {p["name"]: p for p in tb.get("parameters", [])}

    miss_b, miss_a = diff_keys(set(pa), set(pb))
    if miss_b or miss_a:
        problems[tid].append(("parameters_missing", miss_b, miss_a))

    # 5️⃣ Parameter internal keys
    for pname in set(pa) & set(pb):
        ka = keyset(pa[pname])
        kb = keyset(pb[pname])
        miss_b, miss_a = diff_keys(ka, kb)
        if miss_b or miss_a:
            problems[tid].append((f"param:{pname}", miss_b, miss_a))

# ---------------------------
# Report
# ---------------------------
print("\n=== DIFFERENCES ===")
if not problems:
    print("✅ No key differences found.")
else:
    for tid, issues in problems.items():
        print(f"\n--- {tid} ---")
        for scope, miss_b, miss_a in issues:
            if miss_b:
                print(f"  ❌ Missing in B @ {scope}: {miss_b}")
            if miss_a:
                print(f"  ➕ Extra in B @ {scope}: {miss_a}")

print(f"\nTemplates with differences: {len(problems)}")
