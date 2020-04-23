# 4:08
s = input()

alp = [True for _ in range(26)]

for c in s:
    alp[ord(c) - ord('a')] = False

for flag, i in zip(alp, range(26)):
    if flag:
        print(chr(ord('a') + i))
        exit()
print('None')
