bingo = [[int(c) for c in input().split()] for _ in range(3)]

n = int(input())

for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == b:
                bingo[j][k] = 0
# よこ
for i in bingo:
    if sum(i) == 0:
        print('Yes')
        exit()
# たて
for i in range(3):
    tmp = 0
    for j in range(3):
        tmp += bingo[j][i]
    if tmp == 0:
        print('Yes')
        exit()

# ななめ
n1 = 0
n2 = 0
for i in range(3):
    n1 += bingo[i][i]
    n2 += bingo[i][2-i]
if n1 == 0 or n2 == 0:
    print('Yes')
    exit()

print('No')
