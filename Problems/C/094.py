n = int(input())

x = list(map(int, input().split()))
x_s = sorted(x)
ct = 0
print(x_s)
for i in x_s:
    if ct == len(x) // 2-1:
        left = i
    elif ct == len(x) // 2:
        right = i
        break
    ct += 1

for i in x_s:
    if i <= left:
        print(right)
    else:
        print(left)
