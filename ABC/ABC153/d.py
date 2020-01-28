h = int(input())
count = 0
ans = 0
while (1):
    h //= 2
    ans += 2**count
    count += 1

    if h == 0:
        break


print(ans)
