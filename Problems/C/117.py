n, m = map(int, input().split())

x = list(map(int, input().split()))
INF = 1000000
x_sorted = sorted(x)
x_sorted_abs = sorted(x, key=abs)
right = INF
left = -INF
ans = 0

print(x_sorted)
print(x_sorted_abs)
# 最初に置く位置
for i in range(n):
    now = x_sorted_abs.pop()
    if i in range(2):
        

    else:
        if abs(now - left) < abs(now - right):
            print("left")
            left = now
        else:
            print("right")
            right = now

print(left, right)

while (x_sorted_abs):
    now = x_sorted_abs.pop()
    if abs(now - left) < abs(now - right):
        left = now
    else:
        right = now
    ans += now
print(ans)
