def cmb(n, k, mod):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n-i)) % mod

    denominator = 1
    for i in range(1, k+1):
        denominator = (denominator * i) % mod

    return (numerator * pow(denominator, mod-2, mod)) % mod


n, a, b = map(int, input().split())
mod = 10**9 + 7
bunsi = n
bunbo = 1
ans = 0
even = False
if n % 2 == 0:
    even = True

for i in range(1, n//2 + 1):
    if even and i == n//2:
        ans *= 2
    ans += int((bunsi/bunbo) % mod)
    bunsi *= (n-i) % mod
    bunbo *= i+1 % mod
if even:
    ans += 1
else:
    ans = (ans*2 + 1) % mod

print(int(ans) - cmb(n, a, mod)-cmb(n, b, mod))
