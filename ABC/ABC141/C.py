import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
point = [0 for _ in range(n)]
for l in sys.stdin:
    point[int(l)-1] += 1

# print(point)


for p in point:
    if p >= (q - k) + 1:
        print('Yes')
    else:
        print('No')
