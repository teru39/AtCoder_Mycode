# 8:57 1WA
# coding: utf-8
sx, sy, tx, ty = map(int, input().split())

ans = ""
dx = tx - sx
dy = ty - sy

for i in range(dx):
    ans += "R"
for i in range(dy):
    ans += "U"
for i in range(dx):
    ans += "L"
for i in range(dy + 1):
    ans += "D"
for i in range(dx + 1):
    ans += "R"
for i in range(dy + 1):
    ans += "U"
ans += "LU"
for i in range(dx + 1):
    ans += "L"
for i in range(dy + 1):
    ans += "D"
ans += "R"

print(ans)
# UURDDLLUUURRDRDDDLLU
