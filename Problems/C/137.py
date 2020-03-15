# 17:15
n = int(input())

dic = {}
count = 0
for i in range(n):
    s = list(input().strip())
    s.sort()
    s = "".join(s)
    if s not in dic:
        dic[s] = 0
    else:
        dic[s] += 1
        count += dic[s]

print(count)
