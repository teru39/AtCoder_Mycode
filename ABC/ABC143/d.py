n = int(input())
l = [int(i) for i in input().split()]
l = sorted(l, reverse=True)

ans = 0
for i in range(len(l)-2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if l[i] < l[j] + l[k]:
                ans += 1
            else:
                break

print(ans)
