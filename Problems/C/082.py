# 7:41
# coding: utf-8
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = [int(i) for i in input().split()]
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = 0

for k, v in dic.items():
    if k > v:
        ans += v
    else:
        ans += v - k

print(ans)
