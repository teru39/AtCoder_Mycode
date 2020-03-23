# def cmb(n, k, mod):
#     numerator = 1
#     for i in range(k):
#         numerator = (numerator * (n - i)) % mod

#     denominator = 1
#     for i in range(1, k + 1):
#         denominator = (denominator * i) % mod

#     return (numerator * pow(denominator, mod - 2, mod)) % mod


def ncr(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + i + 1 for i in range(r)]
    denominator = [i + 1 for i in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= numerator[k]
    return int(result)


import math


import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

inf = 1001001001
dp = [inf for _ in range(200005)]
dp2 = [inf for _ in range(200005)]
mod = 10**13 + 3

base = 0
for k, v in freq.items():
    if v > 2:
        dp[k] = ncr(v, 2)
        dp2[k] = ncr(v - 1, 2)
    elif v == 2:
        dp[k] = 1
        dp2[k] = 0
    else:
        dp[k] = 0
        dp2[k] = 0
    base += dp[k]

for i in a:
    print(base - dp[i] + dp2[i])
