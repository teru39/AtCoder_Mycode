n, m = map(int, input().split())

x = list(map(int, input().split()))
x.sort()

distance = []

for i in range(len(x) - 1):
    tmp = x[i + 1] - x[i]
    distance.append(tmp)

distance.sort()
if n >= m:
    print(0)
else:
    for i in range(n - 1):
        distance.pop()

    print(sum(distance))
