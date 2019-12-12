s = list(input().strip())
s_re = s[::-1]
ans = 0
for i in range(len(s) // 2):
    if s[i] != s_re[i]:
        ans += 1

print(ans)
