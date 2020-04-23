# 3:34
a, b = map(int, input().split())
s = input()

l = s[:a]
r = s[a + 1:]
if s[a] == '-' and '-' not in l and '-' not in r:
    print('Yes')
else:
    print('No')
