# coding: utf-8
import sys
input = sys.stdin.readline

n, k = map(int, input().split())


height = list(map(int, input().split()))

ans = 0
for i in height:
    if i >= k:
        ans += 1

print(ans)
