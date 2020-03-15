# 2:52 WA1
s = list(input().strip())
s.sort()

if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
    print('Yes')
else:
    print('No')
