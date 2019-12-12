import sys

sys.setrecursionlimit(1000000)


def knight(x, y):
    #print(x, y)
    if dp[x][y] != '.':
        return dp[x][y]
    if x < 0 or y < 0:
        return 0
    if abs(x-y) > max(x, y):
        dp[x][y] = 0
        return dp[x][y]
    dp[x][y] = knight(x - 1, y - 2) + knight(x - 2, y - 1)
    return dp[x][y]


X, Y = map(int, input().split())


dp = [['.' for _ in range(Y+1)] for _ in range(X+1)]
dp[0][0] = 0
dp[1][2] = 1
dp[2][1] = 1

if (X + Y) % 3 != 0:
    print(0)
    exit()
print(knight(X, Y) % (10 ** 9 + 7))

# print(dp)
