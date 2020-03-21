# 25:18
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
mod = 10**9 + 7
dic = {}
for i in range(2, n + 1):
    tmp = prime_factorize(i)
    for j in tmp:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

ans = 1
for i in dic.values():
    ans *= i + 1

if ans == 1:
    print(1)
else:
    print(ans % mod)
