import sys
input = sys.stdin.readline

n = int(input())
order = []
for _ in range(n):
    tmp = [int(c) for c in input().split()]
    order.append(tmp)
print(order)

day = 0
while (1):
    day += 1
    for i in range(len(order)):
        for j in range(len(order) - 1):
            if order[i][j] !=
