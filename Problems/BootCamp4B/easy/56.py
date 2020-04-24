# 4:59
a, b, k = map(int, input().split())
l = []

for i in range(a, min(a + k, b + 1)):
    l.append(i)

for i in range(max(b - k + 1, a), b + 1):
    l.append(i)
l = list(set(l))
l.sort()
for i in l:
    print(i)
