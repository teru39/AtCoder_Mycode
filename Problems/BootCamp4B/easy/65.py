# 4:22
s = input()
sr = s[::-1]

for i in range(len(s)):
    if s[i] == 'A':
        left = i
        break

for i in range(len(s)):
    if sr[i] == 'Z':
        right = i
        break

print(len(s) - right - left)
