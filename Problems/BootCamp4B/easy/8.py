a, b = input().split()
ab = int(a + b)

for i in range(1, 1005):
    if i * i == ab:
        print('Yes')
        exit()
    if i * i > ab:
        print('No')
        exit()
