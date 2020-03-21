# 9:17
import math
sx, sy, gx, gy, T, V = map(int, input().split())
maxdis = T * V

n = int(input())
for i in range(n):
    xx, yy = map(int, input().split())
    if math.sqrt((xx - sx)**2 +
                 (yy - sy)**2) + math.sqrt((gx - xx)**2 +
                                           (gy - yy)**2) <= maxdis:
        print('YES')
        exit()
print('NO')
