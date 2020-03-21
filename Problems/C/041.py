# 6:29
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
tmpl = [int(i) for i in input().split()]
d = {}
for i in range(1, n + 1):
    tmp = tmpl[i - 1]
    d[tmp] = i

d = sorted(d.items(), key=lambda x: -x[0])

for k, v in d:
    print(v)




