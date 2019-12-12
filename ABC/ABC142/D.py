# coding: utf-8
import sys
import math
import fractions
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


a, b = map(int, input().split())
x = fractions.gcd(a, b)
check_list = []
i = 2
while x % 2 == 0:
    check_list.append(2)
    x //= 2
i = 3
while i * i <= x:
    if x % i == 0:
        check_list.append(i)
        x //= i
    else:
        i += 2
if x != 1:
    check_list.append(x)

print(len(set(check_list))+1)
