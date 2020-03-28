n, x, y = map(int, input().split())

dic = {i: 0 for i in range(1, n)}
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        dist = min(j - i, abs(i - x) + abs(j - y) + 1)
        dic[dist] += 1


for i in range(1, n):
    print(dic[i])
