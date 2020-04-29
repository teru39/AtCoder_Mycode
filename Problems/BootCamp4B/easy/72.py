# 3:32
x = int(input())
ans = [1]
for i in range(2, 40):
    for j in range(2, 10):
        if i**j <= x:
            ans.append(i**j)
        else:
            break

ans.sort()
print(ans[-1])
