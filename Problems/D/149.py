n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
mod = ["" for _ in range(k)]
# mod k の値同士しか干渉しない
for i in range(1, n + 1):
    mod[i % k] += t[i - 1]

ans = 0

# for modk in mod:
#     my_hand = ""
#     for your_hand in modk:
#         if your_hand == 'r' and my_hand != 'p':
#             my_hand = 'p'
#             ans += p
#         elif your_hand == 's' and my_hand != 'r':
#             my_hand = 'r'
#             ans += r
#         elif your_hand == 'p' and my_hand != 's':
#             my_hand = 's'
#             ans += s
#         else:
#             my_hand = ""

# for modk in mod:
#     # dp[i][j]: iターン目までで，直前にjを出した
#     # j:0=r, 1=s, 2=p
#     dp = [[0 for _ in range(3)] for _ in range(len(modk) + 1)]
#     for i in range(len(modk)):
#         for j in range(2):
#             dp[i+1][j] = dp[i][j]
#         if modk[i] == 'r':
#             dp[i + 1][2] = max(dp[i][0], dp[i][1]) + p
#         elif modk[i] == 's':
#             dp[i + 1][0] = max(dp[i][1], dp[i][2]) + r
#         else:
#             dp[i + 1][1] = max(dp[i][0], dp[i][2]) + s
#     print(dp)

print(ans)
