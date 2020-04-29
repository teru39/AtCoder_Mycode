# 7:16
s = input()

d = [False for _ in range(4)]

for c in s:
    if c == 'N':
        d[0] = True
    elif c == 'S':
        d[1] = True
    elif c == 'W':
        d[2] = True
    else:
        d[3] = True

if d[0] ^ d[1] or d[2] ^ d[3]:
    print('No')
else:
    print('Yes')
