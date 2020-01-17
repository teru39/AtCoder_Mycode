from collections import deque
h, w = map(int, input().split())

field = [[c for c in input().strip()] for _ in range(h)]

dir_x = [0, 1, 0, -1]
dir_y = [-1, 0, 1, 0]
ans = 0
# 全部のマスをスタートにしてチェックする
for i in range(h):
    for j in range(w):
        if field[i][j] == '#':
            continue

        field_flag = [[0 for _ in range(w)] for _ in range(h)]
        field_step = [[0 for _ in range(w)] for _ in range(h)]
        # スタート地点を入れる
        d = deque()
        d.append([i, j])
        while (d):
            y, x = d.popleft()
            field_flag[y][x] = 1  # スタート地点のフラグを入れる
            for xx, yy in zip(dir_x, dir_y):
                if xx+x in range(w) and yy+y in range(h):
                    if field[yy+y][xx+x] == '.' and field_flag[yy+y][xx+x] == 0:
                        field_flag[yy+y][xx+x] = 1  # チェック済
                        # そこへたどり着く最小歩数
                        field_step[yy + y][xx + x] = field_step[y][x] + 1
                        ans = max(ans, field_step[yy + y][xx + x])  # 答えの更新
                        d.append([yy+y, xx+x])

print(ans)
