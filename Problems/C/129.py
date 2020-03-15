n, m = map(int, input().split())
dp = ['.' for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1
for i in range(m):
    mm = int(input())
    dp[mm] = 0

for i in range(2, n + 1):
    if dp[i] != 0:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 1000000007)
