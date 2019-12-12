import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

l = [int(c)*(-1) for c in input().split()]
# 優先度付きキューにする
heapq.heapify(l)

for _ in range(m):
    tmp = heapq.heappop(l)*(-1)
    heapq.heappush(l, (tmp // 2)*(-1))

print(sum(l)*(-1))
