# 2:48
n, m = map(int, input().split())
like = [0 for _ in range(m + 1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in tmp[1:]:
        like[j] += 1
ans = 0
for i in like:
    if i == n:
        ans += 1
print(ans)
