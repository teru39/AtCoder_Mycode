n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for xx in x:
    if (k - xx) > xx:
        ans += 2 * xx
    else:
        ans += (k - xx) * 2

print(ans)
