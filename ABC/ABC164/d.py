s = input()
p = 2019
n = len(s)
ans = 0

d = [0 for _ in range(n + 1)]
ten = 1
for i in range(n - 1, -1, -1):
    a = int(s[i]) * ten % p
    d[i] = (d[i + 1] + a) % p
    ten *= 10
    ten %= p

cnt = [0 for _ in range(p)]
for i in range(n, -1, -1):
    ans += cnt[d[i]]
    cnt[d[i]] += 1

print(ans)
