import math

# 速いやつ
def cmb(n, k, mod):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n-i)) % mod

    denominator = 1
    for i in range(1, k+1):
        denominator = (denominator * i) % mod

    return (numerator * pow(denominator, mod-2, mod)) % mod

# 遅い
def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


X, Y = map(int, input().split())
mod = 10**9 + 7
if (X + Y) % 3 != 0:
    print(0)
    exit()
else:
    n = int((2 * Y - X) / 3)
    m = int(Y - 2 * n)
    print(m + n)
    print(n)
    if n < 0 or m < 0:
        print(0)
        exit()
    else:
        print(cmb(m+n, n, mod))
