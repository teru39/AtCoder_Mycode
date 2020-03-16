import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

summ = sum(l)
big = max(l)
print(summ)
if big * 2 <= summ:
    print(0)
else:
    print(big - (summ - big))
