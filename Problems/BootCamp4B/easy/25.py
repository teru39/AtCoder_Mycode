# 8:19
import itertools

n = int(input())
l = [i for i in range(1, n + 1)]
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
cnt = 0
for check in itertools.permutations(l, n):
    cnt += 1
    if a == check:
        cnta = cnt
    if b == check:
        cntb = cnt

print(abs(cnta - cntb))
