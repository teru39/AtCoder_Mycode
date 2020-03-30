# 11:40
import math
n = int(input())

if math.sqrt(n).is_integer():
    print(0)
else:
    ans = 1001001001
    for i in range(1, n):
        j = n // i
        amari = n - i * j
        ans = min(ans, abs(i - j) + amari)

    print(ans)
