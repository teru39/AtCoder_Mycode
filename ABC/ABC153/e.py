# Python3ではTLE
# PyPyなら回る
h, n = map(int, input().split())
inf = 1001001001
dp = [inf for _ in range(h+1)]
dp[0] = 0
ans = inf
for i in range(n):
    a, b = map(int, input().split())
    for j in range(h + 1):
        # 外側参照しないように
        nj = min(j+a, h)
        dp[nj] = min(dp[nj], dp[j]+b)

print(dp[h])
