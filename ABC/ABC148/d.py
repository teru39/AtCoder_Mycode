n = int(input())

l = list(map(int, input().split())
         )

if 1 not in l:
    print(-1)
else:
    ans = 0
    now = 1
    for i in range(n):
        if l[i] != now:
            ans += 1
        else:
            now += 1
    print(ans)
