# 13:26
n, X = map(int, input().split())
a = [int(c) for c in input().split()]
ans = 0
for i in range(n):
    if X >> i & 1:
        ans += a[i]

print(ans)
