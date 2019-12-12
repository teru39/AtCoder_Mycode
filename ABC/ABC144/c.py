n = int(input())
i = 1
ans = 10**12
while (i * i < n):
    i += 1
    if n % i == 0:
        ans = min(ans, (i-1) + (n//i - 1))
ans = min(ans, n-1)
print(ans)
