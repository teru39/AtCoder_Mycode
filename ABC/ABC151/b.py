n, k, m = map(int, input().split())

point = list(map(int, input().split()))


nec = (m*n) - sum(point)

if nec <= k:
    if nec < 0:
        print(0)
    else:
        print(nec)
else:
    print(-1)
