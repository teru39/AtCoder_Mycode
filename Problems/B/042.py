n, l = map(int, input().split())
d = []
for i in range(n):
    d.append(input())
d.sort()

print("".join(d))
