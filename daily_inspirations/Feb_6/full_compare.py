import json
from pathlib import Path

B = json.loads(Path("nano_templates_289.json").read_text(encoding="utf-8"))

bad = []
for t in B:
    tid = t.get("id")
    locales = t.get("locales", {})
    has_any = False
    empty_locales = []
    for loc, obj in locales.items():
        params = obj.get("parameters")
        if params is None:
            continue
        if isinstance(params, list) and len(params) > 0:
            has_any = True
        else:
            empty_locales.append(loc)

    if not has_any:
        bad.append((tid, "NO locale parameters at all"))
    elif empty_locales:
        bad.append((tid, f"empty parameters in locales: {empty_locales}"))

print("bad templates:", len(bad))
for x in bad[:50]:
    print(x)
