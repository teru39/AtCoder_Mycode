import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))
s.sort()
tmp = s.pop()
slime = []
slime.append(tmp)
for i in range(n):
    for x in slime:
        if x
