n = int(input())

grid = [[0 for _ in range(9)] for _ in range(9)]
ans = 0
for i in range(1, n + 1):
    if i % 10 == 0:
        continue
    else:
        s = str(i)
        grid[int(s[0]) - 1][int(s[-1]) - 1] += 1

for i in range(9):
    for j in range(9):
        ans += grid[i][j] * grid[j][i]
print(ans)
