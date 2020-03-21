N = input()
n = len(N)
# dp[i][smaller][flag_one]
# i桁，小さいか，すでに1出たか
dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    max_digit = int(N[i])
    for smaller in range(2):
        for flag_one in range(2):
            range_digit = 9 if smaller else max_digit
            for x in range(range_digit + 1):
                smaller_next = 0
                flag_one_next = 0
                # 小さいのが確定
                if smaller or x < max_digit:
                    smaller_next = 1
                # 1がすでに出ている
                if flag_one or x == 1:
                    flag_one_next = 1

                dp[i +
                   1][smaller_next][flag_one_next] += dp[i][smaller][flag_one]

print(dp[n][0][1] + dp[n][1][1])
