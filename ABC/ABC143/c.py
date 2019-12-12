n = int(input())
s = list(input().strip())
before = s[0]
ans = 1
for i in range(1, len(s)):
    if s[i] == before:
        continue
    else:
        before = s[i]
        ans += 1
print(ans)
