# 2:25
import math
n = int(input())
a = [int(i) for i in input().split()]
bug = 0
bugsum = 0
for i in a:
    if i != 0:
        bug += 1
        bugsum += i

if bug != 0:
    print(math.ceil(bugsum / bug))
else:
    print(0)
