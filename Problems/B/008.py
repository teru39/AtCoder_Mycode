# 3:40
n = int(input())
dic = {}

for i in range(n):
    w = input()
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1

print(max(dic, key=dic.get))

