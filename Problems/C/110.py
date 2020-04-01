# 3:42
s = input()
t = input()

s_f = [0 for _ in range(26)]
t_f = [0 for _ in range(26)]

for ss, tt in zip(s, t):
    s_f[ord(ss) - ord('a')] += 1
    t_f[ord(tt) - ord('a')] += 1

s_f.sort()
t_f.sort()

for ss, tt in zip(s_f, t_f):
    if ss != tt:
        print('No')
        exit()

print('Yes')
