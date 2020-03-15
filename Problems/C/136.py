# 04:27
n = int(input())

h = [int(i) for i in input().split()]

left = h[0]

for i in range(1, n):
    if left < h[i]:
        h[i] -= 1
    elif left == h[i]:
        pass
    else:
        print('No')
        exit()
    left = h[i]

print('Yes')
