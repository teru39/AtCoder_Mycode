a, b, c = map(int, input().split())

m = max(a, max(b, c))

if (3 * m - (a + b + c)) % 2 == 0:
    print((3 * m - (a + b + c)) // 2)
else:
    print((3 * (m + 1) - (a + b + c)) // 2)
