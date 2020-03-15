# 09:52
import heapq

n = int(input())
item = [int(i) for i in input().split()]
heapq.heapify(item)

while (len(item) != 1):
    a = heapq.heappop(item)
    b = heapq.heappop(item)
    heapq.heappush(item, (a + b) / 2)

print(item[0])
