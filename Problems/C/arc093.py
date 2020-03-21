# 19:40
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))

pay = [abs(a[0])]
dis = [a[0]]
for i in range(len(a) - 1):
    pay.append(abs(a[i + 1] - a[i]))
    dis.append(a[i + 1] - a[i])
pay.append(abs(0 - a[-1]))
dis.append(0 - a[-1])
summ = sum(pay)

for i in range(n):
    ans = summ - (pay[i] + pay[i + 1]) + abs(dis[i] + dis[i + 1])
    print(ans)
