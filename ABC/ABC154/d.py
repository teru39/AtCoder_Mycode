n, k = map(int, input().split())

l = list(map(int, input().split()))
dp = [0.5+0.5*i for i in range(max(l)+1)]
dp[0] = 0

# print(dp)
tmp = 0
for i in range(k-1):
    tmp += dp[l[i]]

ans = 0
for i in range(k-1, n):
    tmp += dp[l[i]]
    ans = max(ans, tmp)
    tmp -= dp[l[i-(k-1)]]
print(ans)
