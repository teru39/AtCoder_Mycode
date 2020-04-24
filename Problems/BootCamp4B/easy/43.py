# 1:53
s = input()
alp = [0 for _ in range(26)]

for c in s:
    alp[ord(c) - ord('a')] += 1

for i in alp:
    if i % 2 != 0:
        print('No')
        exit()
print('Yes')
