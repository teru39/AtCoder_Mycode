import bisect
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
ans = 0
for b in range(n):
    for a in range(b):
        tmp = l[a] + l[b]
        r = bisect.bisect_left(l, tmp)
        ll = b + 1
        ans += max(0, r - ll)
print(ans)
