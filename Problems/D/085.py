# 16:15
import sys
input = lambda: sys.stdin.readline().rstrip()
import math
n, h = map(int, input().split())
sl = 0
th = []
for i in range(n):
    a, b = map(int, input().split())
    sl = max(sl, a)
    th.append(b)

th.sort()
th_damage = th.pop()
turn = 0
while (h > 0):
    if th_damage > sl:
        h -= th_damage
        if len(th) != 0:
            th_damage = th.pop()
        else:
            th_damage = 0
    else:
        turn += math.ceil(h / sl)
        break
    turn += 1

print(turn)
