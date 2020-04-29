# 3:18
from collections import deque

o = deque(input())
e = deque(input())
s = ""
while (o and e):
    s += o.popleft()
    s += e.popleft()

if o:
    s += o.popleft()
print(s)
