# coding: utf-8
from fractions import gcd
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
a = min(x, y)
b = max(x, y)

check = str(bin(a ^ b))
# print(check)
ans = 0

for i in range(1, len(bin(a)) - 2):
    print(i)
    if check[-i] == '1':
        ans += 1
if ans == 0:
    ans += 1
print(ans)
print(len(bin(a)))
