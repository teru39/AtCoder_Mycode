# 17:02
# coding: utf-8
sx, sy, W = input().split()
sx = int(sx) - 1
sy = int(sy) - 1

field = [[c for c in input().strip()] for _ in range(9)]

dir_x = [1, 0, -1]
dir_y = [1, 0, -1]
dir_list = [['RD', 'R', 'RU'], ['D', 'NONE', 'U'], ['LD', 'L', 'LU']]

for i in range(3):
    for j in range(3):
        if W == dir_list[i][j]:
            dx = dir_x[i]
            dy = dir_y[j]

for i in range(4):
    print(field[sy][sx], end="")
    nx = sx + dx
    ny = sy + dy
    if nx not in range(9):
        nx = sx - dx
        dx *= -1
    if ny not in range(9):
        ny = sy - dy
        dy *= -1
    sx = nx
    sy = ny
print()
