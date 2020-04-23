# 3:59
n, m, x = map(int, input().split())
a = list(map(int, input().split()))

up = 0
down = 0

for i in a:
    if i < x:
        down += 1
    elif i > x:
        up += 1
print(min(up, down))
