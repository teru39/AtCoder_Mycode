n = int(input())
ans = 0

while (1):
    if pow(2, ans) > n:
        print(pow(2, ans - 1))
        exit()
    ans += 1
