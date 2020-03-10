n, p = map(int, input().split())
s = input()
ans = 0
# p == 2,5
if 10 % p == 0:
    for r in range(n):
        if int(s[r]) % p == 0:
            ans += r + 1
    print(ans)
    exit()

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

#print(d)

print(ans)
