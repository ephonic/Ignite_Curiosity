# -*- coding: utf-8 -*-
"""把 literal.md 中每章提纲拆成 briefs/chNNN.md。"""
import os
import re

with open("literal.md", encoding="utf-8") as f:
    lines = f.read().splitlines()

os.makedirs("briefs", exist_ok=True)

current = None
buf = []
count = 0

def flush():
    global count
    if current is not None:
        with open("briefs/ch%03d.md" % current, "w", encoding="utf-8") as f:
            f.write("\n".join(buf).strip() + "\n")
        count += 1

for line in lines:
    m = re.match(r"^### 第\s*(\d+)\s*章", line)
    if m:
        flush()
        current = int(m.group(1))
        buf = [line]
        continue
    if current is not None:
        if re.match(r"^#{1,3} ", line):  # 同级或更高级标题，结束本章
            flush()
            current = None
            buf = []
        else:
            buf.append(line)
flush()
print("brief 数:", count)
