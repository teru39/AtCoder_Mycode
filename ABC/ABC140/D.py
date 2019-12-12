n, k = map(int, input().split())
s = list(input().strip())
count = 0
for i in range(len(s)):
    if (i == 0 and s[i] == 'L') or (i == len(s) - 1 and s[i] == 'R'):
        pass
    elif (s[i] == 'R' and s[i + 1] == 'R') or (s[i] == 'L' and s[i - 1] == 'L'):
        count += 1

count = min(count+(k*2), n-1)

print(count)
