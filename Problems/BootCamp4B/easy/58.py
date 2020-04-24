# 5:02
def deg(x):
    return t - x * 0.006


n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

tmp = 1001001001
ans = 1
for i in range(len(h)):
    d = deg(h[i])
    if abs(a - d) < tmp:
        ans = i + 1
        tmp = abs(a - d)
print(ans)
