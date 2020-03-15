# 02:10
n = int(input())

l = list(map(int, input().split()))

l.sort()

max_l = l.pop()

if max_l < sum(l):
    print('Yes')
else:
    print('No')
