# 13:43
n, l = map(int, input().split())

taste = []

for i in range(n):
    tmp = l + i
    taste.append(tmp)


taste = sorted(taste, key=abs, reverse=True)
taste.pop()

print(sum(taste))
