n, k = map(int, input().split())

h = list(map(int, input().split()))
h = sorted(h)

for i in range(k):
    if len(h) == 0:
        h.append(0)
        break
    h.pop()

print(sum(h))
