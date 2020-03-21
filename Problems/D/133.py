# 34:52
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
summ = sum(a)
tmp = 0
for i in range(1, len(a), 2):
    tmp += a[i]
x1 = summ - 2 * tmp
print(x1, end=" ")
for i in range(1, n):
    x1 = 2 * a[i - 1] - x1
    if i != n - 1:
        print(x1, end=" ")
    else:
        print(x1)
