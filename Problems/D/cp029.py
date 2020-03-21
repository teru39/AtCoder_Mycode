N = str(int(input()) + 1)
n = len(N)
# dp[i][smaller][flag_one]
# i桁，小さいか，1が出た回数
dp = [[[0 for _ in range(n + 1)] for _ in range(2)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    max_digit = int(N[i])
    for smaller in range(2):
        for num_one in range(n):
            range_digit = 9 if smaller else max_digit
            for x in range(range_digit + 1):
                smaller_next = 0
                # 小さいのが確定
                if smaller or x < max_digit:
                    smaller_next = 1
                if x == 1:
                    dp[i + 1][smaller_next][num_one +
                                            1] += dp[i][smaller][num_one]
                else:
                    dp[i + 1][smaller_next][num_one] += dp[i][smaller][num_one]

ans = 0
for num, onenum in zip(dp[n][1], range(n + 1)):
    ans += num * onenum
print(ans)
