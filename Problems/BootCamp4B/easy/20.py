# 7:42
def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


check = [False for _ in range(1000005)]

s = int(input())
cnt = 1
check[s] = True
while (1):
    s = f(s)
    cnt += 1
    if check[s]:
        print(cnt)
        exit()
    else:
        check[s] = True
