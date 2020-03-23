s = input()
sr = s[::-1]
mannnaka = (len(s) - 1) // 2

for i in range(mannnaka):
    if s[i] != sr[i]:
        print('No')
        exit()

for i in range(mannnaka // 2):
    if s[i] != s[mannnaka - i - 1] or sr[i] != sr[mannnaka - i - 1]:
        print('No')
        exit()

print('Yes')
