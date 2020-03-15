# 09:30
import math
n, d = map(int, input().split())

point = []
for i in range(n):
    tmp = list(map(int, input().split()))
    point.append(tmp)

count = 0
for i in range(n):
    for j in range(i+1, n):
        cal = 0
        for y, z in zip(point[i], point[j]):
            cal += (y - z) ** 2
        # print(math.sqrt(cal))
        if math.sqrt(cal).is_integer():
            count += 1


print(count)
