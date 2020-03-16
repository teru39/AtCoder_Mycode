# 3minくらい
ax, ay, bx, by, cx, cy = map(int, input().split())

print(abs((bx - ax) * (cy - ay) - (cx - ax) * (by - ay)) / 2)
