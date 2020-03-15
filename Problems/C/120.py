s = input()

s0 = 0
s1 = 0

for c in s:
    if c == '0':
        s0 += 1
    else:
        s1 += 1

print(min(s0, s1)*2)
