n, m = map(int, input().split())

dic = {}
for i in range(1, n+1):
    dic[i] = -1

for i in range(m):
    s, c = map(int, input().split())
    if dic[s] == -1:
        dic[s] = c
    else:
        if dic[s] != c:
            print(-1)
            exit()

if m == 0:
    if n == 1:
        print(0)
    elif n == 2:
        print(10)
    elif n == 3:
        print(100)
    exit()

if n > 1 and dic[1] == 0:
    print(-1)
    exit()
elif n > 1 and dic[1] == -1:
    print(1, end="")
else:
    print(dic[1], end="")

for i in range(2, n+1):
    if dic[i] == -1:
        print(0, end="")
    else:
        print(dic[i], end="")
print()
