s = list(input().strip())
t = list(input().strip())

count = 0

for i in range(3):
    if s[i] == t[i]:
        count += 1
print(count)
