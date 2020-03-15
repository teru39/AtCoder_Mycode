# 14:22
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
tate = 0
yoko = 0
now = 0
#print(a)
for i in a:
    if tate == 0:
        if now == i:
            tate = now
            now = 0
            continue
    else:
        if now == i:
            yoko = now
            break
    now = i

print(tate * yoko)
