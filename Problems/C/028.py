# 3:42
# coding: utf-8
from itertools import combinations

a = list(map(int, input().split()))
ans = []
for i in combinations(a, 3):
    summ = sum(i)
    if summ not in ans:
        ans.append(summ)

ans.sort()
print(ans[-3])
