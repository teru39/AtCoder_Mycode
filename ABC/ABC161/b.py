n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
a = a[::-1]
summ = sum(a)
asikiri = summ / (4 * m)

for i in range(m):
    if a[i] < asikiri:
        print('No')
        exit()

print('Yes')
