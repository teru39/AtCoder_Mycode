# 4:44
n = int(input())
turn = -1
bef = input()
dic = {bef: 0}
for i in range(n - 1):
    w = input()
    if w in dic or w[0] != bef[-1]:
        if turn == 1:
            print('LOSE')
        else:
            print('WIN')
        exit()
    else:
        dic[w] = 0
    bef = w
    turn *= -1

print('DRAW')
