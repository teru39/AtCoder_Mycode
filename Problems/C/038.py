# 6:59
n = int(input())
a = [int(i) for i in input().split()]
ans = [1 for _ in range(n)]
bef = a[0]
for i in range(1, len(a)):
    now = a[i]
    if bef < now:
        ans[i] += ans[i - 1]
    bef = now

for i in range(1, len(a)):
    ans[i] += ans[i - 1]

print(ans[n - 1])
