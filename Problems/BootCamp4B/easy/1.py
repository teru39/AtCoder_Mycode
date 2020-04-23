# 2:50
a, b = map(int, input().split())
if b == 1:
    print(0)
    exit()

if a >= b:
    print(1)
else:
    b -= a
    cnt = 1
    while (b > 0):
        b -= (a - 1)
        cnt += 1
    print(cnt)
