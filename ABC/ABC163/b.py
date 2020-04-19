import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) > n:
    print(-1)
else:
    print(n - sum(a))
