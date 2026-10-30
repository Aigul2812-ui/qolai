import re

src = open(r"C:\Users\пк\Documents\Проект по умолчанию\qolai\index.html", encoding="utf-8").read()
defined = set(re.findall(r'^\s{2,4}([a-zA-Z][a-zA-Z0-9]*):\s*N\(', src, flags=re.M))
used = set(re.findall(r't\(\s*"([a-zA-Z0-9]+)"', src))
for m in re.finditer(r'data-i18n(?:-ph)?="([a-zA-Z0-9]+)"', src):
    used.add(m.group(1))
missing = used - defined
print("defined:", len(defined))
print("used:", len(used))
print("missing:", sorted(missing) if missing else "нет - все ключи на месте")
