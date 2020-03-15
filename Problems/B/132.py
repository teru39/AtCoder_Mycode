# 06:24
n = int(input())

l = [int(i) for i in input().split()]
count = 0
for i in range(n - 2):
    tmp = []
    for j in range(i, i + 3):
        tmp.append(l[j])
    if tmp[1] == max(tmp) or tmp[1] == min(tmp):
        pass
    else:
        count += 1

print(count)
