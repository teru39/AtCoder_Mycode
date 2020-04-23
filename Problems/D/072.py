n = int(input())
p = list(map(int,input().split()))
left = 0
for i in range(len(p)):
    if p[i] == i+1:
        left += 1
        if i == len(p)-1:
            break
        tmp = p[i]
        p[i] = p[i+1]
        p[i+1] = tmp

print(left)
