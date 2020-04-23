# 5:00
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in a:
    x -= i
    if x >= 0:
        ans += 1
    else:
        break
if x > 0:
    print(ans - 1)
else:
    print(ans)
