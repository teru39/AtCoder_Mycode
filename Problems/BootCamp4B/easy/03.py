# 7:04
n, a, b = map(int, input().split())
s = input()
maxim = a + b
foreign = 1
through = 0
for c in s:
    if c == 'a' and through < maxim:
        print('Yes')
        through += 1
    elif c == 'b' and through < maxim and foreign <= b:
        print('Yes')
        through += 1
        foreign += 1
    else:
        print('No')
