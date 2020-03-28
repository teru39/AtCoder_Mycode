import heapq


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign


x, y, a, b, c = map(int, input().split())

red = [int(i) for i in input().split()]
green = [int(i) for i in input().split()]
clear = [int(i) for i in input().split()]

red = Heapq(red, True)
green = Heapq(green, True)
clear = Heapq(clear, True)

ans = []
for i in range(x):
    clear.push(red.pop())
for j in range(y):
    clear.push(green.pop())
ans = 0
for k in range(x + y):
    ans += clear.pop()
print(ans)
