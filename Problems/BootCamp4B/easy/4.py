# 5:02
n = int(input())

for i in range(1, 50001):
    if (i * 1.08) // 1 == n:
        print(i)
        exit()
    if (i * 1.08) // 1 > n:
        print(':(')
        exit()
