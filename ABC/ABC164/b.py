a, b, c, d = map(int, input().split())
turn = True

while (a > 0 and c > 0):
    if turn:
        c -= b
    else:
        a -= d
    turn = not turn

if a > c:
    print('Yes')
else:
    print('No')
