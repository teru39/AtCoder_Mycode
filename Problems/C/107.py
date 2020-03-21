# 40:48
import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
x = [int(c) for c in input().split()]

ans = 1001001001
for i in range(n - k + 1):
    xl = x[i]
    xr = x[i + k - 1]
    ans = min(ans, min(abs(xl) + abs(xr - xl), abs(xr) + abs(xr - xl)))
print(ans)
