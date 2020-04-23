# 5:03
n = int(input())
d, x = map(int, input().split())
use = 0
for i in range(n):
    a = int(input())
    day = 1
    while (day <= d):
        use += 1
        day += a
print(x + use)
