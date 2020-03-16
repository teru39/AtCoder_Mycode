# 11:14
from collections import deque

aa = input()
bb = input()
cc = input()
a, b, c = deque(aa), deque(bb), deque(cc)
now = 'a'
while (1):
    if now == 'a':
        if len(a) == 0:
            print('A')
            exit()
        now = a.popleft()
    elif now == 'b':
        if len(b) == 0:
            print('B')
            exit()
        now = b.popleft()
    else:
        if len(c) == 0:
            print('C')
            exit()
        now = c.popleft()
