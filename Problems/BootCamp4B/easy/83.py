# 5:30
n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
s = sum(a2) + a1[0]
ans = s
for i in range(1, n):
    s = s + a1[i] - a2[i - 1]
    ans = max(ans, s)
print(ans)
