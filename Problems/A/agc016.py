# 24:30
s = list(input())

if len(set(s)) == 1:
    print(0)
elif len(set(s)) == len(s):
    print((len(s) + 1) // 2)
else:
    ans = 10010001001
    for i in range(ord('a'), ord('z') + 1):
        tmp = 0
        tmp2 = 0
        for c in s:
            if c == chr(i):
                tmp = 0
            else:
                tmp += 1
            tmp2 = max(tmp, tmp2)
        ans = min(ans, tmp2)

    print(ans)
