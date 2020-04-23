# 12:17
# coding: utf-8
n, k = map(int, input().split())

three = (k - 1) * (n - k) * 6
two = (n - 1) * 3
one = 1

print((three + two + one) / n**3)
