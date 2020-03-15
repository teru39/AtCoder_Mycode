# 11:34
n, m = map(int, input().split())
first = [False for _ in range(n + 1)]
second = [False for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        first[b] = True
    if b == n:
        second[a] = True

for i, j in zip(first, second):
    if i and j:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
