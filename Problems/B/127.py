r, d, x2000 = map(int, input().split())

x = x2000
for i in range(10):
    next_x = r*x-d
    print(next_x)
    x = next_x
