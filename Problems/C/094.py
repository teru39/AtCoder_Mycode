# 12:53
# coding: utf-8
n = int(input())

x = list(map(int, input().split()))
xs = sorted(x)
left = xs[n // 2 - 1]
right = xs[n // 2]

for i in range(n):
    if x[i] <= left:
        print(right)
    else:
        print(left)
