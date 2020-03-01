n = int(input())

l = list(map(int, input().split()))

l.sort()

# print(max(l))
ans = 1001001001
for i in range(1, 101):
    tmp = 0
    for j in l:
        tmp += (j-i)**2
    ans = min(tmp, ans)
print(ans)
