# 8:25
import math
ans = 0
lst = 10
for i in range(5):
    a = input()
    if int(a[-1]) != 0:
        lst = min(lst, int(a[-1]))
    ans += math.ceil(int(a) / 10) * 10

if lst == 10:
    print(ans)
else:
    print(ans - (10 - lst))
