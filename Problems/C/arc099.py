# 15:53
import sys
import math
input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())

a = list(map(int, input().split()))

print(math.ceil((n-1)/(k-1)))
