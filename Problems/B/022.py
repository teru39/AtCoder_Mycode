# 3:06
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dic = {}
ans = 0
for i in range(n):
    tmp = input()
    if tmp in dic:
        ans += 1
    else:
        dic[tmp] = 0
print(ans)
