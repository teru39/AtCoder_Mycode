# 3:03
s = input()
n = len(s)
target = 753
ans = 1001001001
for i in range(n - 3 + 1):
    ss = int(s[i:i + 3])
    ans = min(ans, abs(target - ss))
print(ans)
