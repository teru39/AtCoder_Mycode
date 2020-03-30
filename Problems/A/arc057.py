import math
a, k = map(int, input().split())
target = 2 * (10**12)
if k == 0:
    print(target - a)
else:
    day = 0
    while (a < target):
        day += 1
        a += 1 + a * k
    print(day)
