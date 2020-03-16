# 8:56
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
f = 0
even = 0
odd = 0

for i in a:
    if i % 4 == 0:
        f += 1
    elif i % 2 == 0:
        even += 1
    else:
        odd += 1

even %= 2
if f - even - odd < -1:
    print('No')
else:
    print('Yes')
