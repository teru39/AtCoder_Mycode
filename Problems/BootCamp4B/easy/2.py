# 3:02
n = int(input())
x = list(map(int, input().split()))
ans = 1001001001
for i in range(1, 101):
    tmp = 0
    for xx in x:
        tmp += (xx - i)**2
    ans = min(tmp, ans)
print(ans)
