# coding: utf-8
# Your code here!

n = int(input())
l = []
check = []
count = []
sdict = {}
for i in range(n):
    w = input()
    _w = ''.join(sorted(w))
    if _w not in sdict.keys():
        sdict[_w] = 1
    else:
        sdict[_w] += 1


def nC2(n):
    return int(n*(n-1)/2)


ans = sum([nC2(val) for val in sdict.values() if val > 1])
print(ans)
