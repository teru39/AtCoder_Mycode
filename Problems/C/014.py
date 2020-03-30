from itertools import accumulate
import sys
input = lambda: sys.stdin.readline().rstrip()
num = 1000005
n = int(input())
imos = [0 for _ in range(num)]

for i in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1

# for i in range(1, num):
#     imos[i] += imos[i - 1]
ans = accumulate(imos)

print(max(ans))
