import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, m = map(int, input().split())

if n <= 1:
    ans1 = 0
else:
    ans1 = combinations_count(n, 2)
if m <= 1:
    ans2 = 0
else:
    ans2 = combinations_count(m, 2)
print(ans1 + ans2)
