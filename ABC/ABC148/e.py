n = int(input()
        )


if n % 2 == 1:
    print(0)
else:
    n = n//10
    ans = n
    while (n > 0):
        n //= 5
        ans += n
    print(ans)
