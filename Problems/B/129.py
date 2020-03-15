# 04:17
n = int(input())
t = [int(i) for i in input().split()]
ans = 10000000000

for i in range(1, n):
    a = t[:i]
    b = t[i:]
    ans = min(ans, abs(sum(a) - sum(b)))

print(ans)
