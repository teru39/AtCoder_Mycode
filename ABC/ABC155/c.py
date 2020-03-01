n = int(input())

dic = {}
maxn = 1
for _ in range(n):
    s = input()
    if s in dic:
        dic[s] += 1
        maxn = max(maxn, dic[s])
    else:
        dic[s] = 1

dic = sorted(dic.items(), key=lambda x: x[0])
# print(dic)

for k, v in dic:
    if v == maxn:
        print(k)
