# 19:26
s = input()
reply = False
name = ""
l = []
for i in range(len(s)):
    if s[i] == '@':
        reply = True
        if len(name) != 0:
            l.append(name)
            name = ""
    elif s[i].isalpha() and reply:
        name += s[i]
    else:
        if reply:
            if len(name) != 0:
                l.append(name)
            reply = False
        name = ""

if reply and len(name) != 0:
    l.append(name)

l = list(set(l))
l.sort()

for i in l:
    print(i)
