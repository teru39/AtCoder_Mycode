# 14:16
n = int(input())
s = input()
ans = 1001001001
ll = [0]
rl = [0]
l = 0
r = 0
for i in range(1, len(s)):
    if s[i - 1] == 'W':
        l += 1
    ll.append(l)
    if s[-i] == 'E':
        r += 1
    rl.append(r)
rl.reverse()

# print(ll)
# print(rl)

for a, b in zip(ll, rl):
    ans = min(ans, a + b)
print(ans)
