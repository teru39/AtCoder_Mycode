# 10:53
s = input()
out = False
if s[0] != 'A':
    out = True
C = False

if s[1].isupper():
    out = True

for ss in s[2:-1]:
    if ss == 'C':
        if C:
            out = True
        C = True
    elif s.isupper():
        out = True

if not C or s[-1].isupper():
    out = True

if out:
    print('WA')
else:
    print('AC')
