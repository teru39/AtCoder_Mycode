n = int(input())

b = list(map(int, input().split()))

a = [0]
a[0] = b[0]
for i in range(1, n-1):
    cal = min(b[i - 1], b[i])
    a.append(cal)
a.append(b[-1])
print(sum(a))
