from collections import deque
n = int(input())
s = input()
if s == 'b':
    print(0)
    exit()

now = deque(['b'])
turn = 0
while (len(now) <= n):
    turn = turn + 1
    if turn % 3 == 0:
        now.appendleft('b')
        now.append('b')
    elif turn % 3 == 1:
        now.appendleft('a')
        now.append('c')
    else:
        now.appendleft('c')
        now.append('a')
    if "".join(now) == s:
        print(turn)
        exit()
print(-1)
