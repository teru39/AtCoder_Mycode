# 02:00
n = int(input())

a = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    ans += 1 / a[i]

print(1/ans)
