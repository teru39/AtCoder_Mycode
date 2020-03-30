# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

from fractions import gcd

n = int(input())
a = list(map(int, input().split()))
ans = 1001001001
g = a[0]
for i in range(1,n):
    g = gcd(a[i], g)
    ans = min(ans, g)

print(ans)
