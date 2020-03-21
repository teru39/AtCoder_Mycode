# 15:47 1WA
n, k, s = map(int, input().split())
flag = False
if s == 10**9:
    flag = True

for i in range(k):
    print(s, end=" ")
for i in range(n - k):
    if flag:
        if i != n - k - 1:
            print(1, end=" ")
        else:
            print(1)
    else:
        if i != n - k - 1:
            print(s + 1, end=" ")
        else:
            print(s + 1)
