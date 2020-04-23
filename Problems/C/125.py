# 35:36
import sys
from fractions import gcd
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
# 左から
L = [0 for _ in range(n + 1)]
for i in range(n):
    L[i + 1] = gcd(L[i], a[i])

R = [0 for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    R[i] = gcd(R[i + 1], a[i])

# print(L)
# print(R)
m = 0
for i in range(n):
    m = max(m, gcd(L[i], R[i + 1]))
print(m)
