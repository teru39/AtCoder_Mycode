# 9:10
s = input()
ch = ['A', 'C', 'G', 'T']
ans = 0
tmp = 0
for c in s:
    if c in ch:
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)

print(ans)
