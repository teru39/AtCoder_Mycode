# 最大公約数，最小公倍数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


dp = [[0 for _ in range(205)] for _ in range(205)]

k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(a, k + 1):
        for c in range(b, k + 1):
            if len(set([a, b, c])) == 1:
                ans += a
            elif len(set([a, b, c])) == 2:
                ans += gcd(a, gcd(b, c)) * 3
            else:
                ans += gcd(a, gcd(b, c)) * 6
print(ans)
