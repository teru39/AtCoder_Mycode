# 4:11
n, m, c = map(int, input().split())
ans = 0
b = list(map(int, input().split()))

for i in range(n):
    a = list(map(int, input().split()))
    cal = 0
    for j in range(len(a)):
        cal += a[j] * b[j]
    cal += c
    if cal > 0:
        ans += 1
print(ans)
