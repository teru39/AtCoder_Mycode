# coding: utf-8
import sys
input = sys.stdin.readline

n = int(input())

ai = list(map(int, input().split()))
dic = {}
for i in range(1, n + 1):
    dic[ai[i-1]] = i

ans = sorted(dic.items())


for i in range(len(ans)):
    print(ans[i][1], end="")
    if i != len(ans)-1:
        print(end=" ")
    else:
        print()
