import math
import itertools
n = int(input())
city = [[int(i) for i in input().split()] for j in range(n)]


allnum = math.factorial(n)

city_num = [int(i) for i in range(n)]

ans = 0

for v in itertools.permutations(city_num):
    # print(v)
    pre = -1
    for i in v:
        if pre == -1:
            pre = i
            continue
        ans += math.sqrt((city[i][0] - city[pre][0]) **
                         2 + (city[i][1] - city[pre][1]) ** 2)
        pre = i

print(ans/allnum)
