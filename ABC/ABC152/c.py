n = int(input())
l = list(map(int, input().split())
         )
ans = 0
now = 2*(10**5)
for i in l:
    if i <= now:
        ans += 1
        now = i
print(ans)
