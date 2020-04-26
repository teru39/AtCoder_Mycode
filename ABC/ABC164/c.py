n = int(input())
dic = {}
ans = 0
for i in range(n):
    s = input()
    if s not in dic:
        dic[s] = 1
        ans += 1
print(ans)
