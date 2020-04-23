a, b, c = map(int, input().split())
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    print(0)
    exit()

if a == b and b == c and a % 2 == 0:
    print(-1)
else:
    ans = 0
    while (1):
        aa = 0
        bb = 0
        cc = 0
        aa += (b // 2 + c // 2)
        bb += (a // 2 + c // 2)
        cc += (a // 2 + b // 2)
        ans += 1
        if aa % 2 == 1 or bb % 2 == 1 or cc % 2 == 1:
            print(ans)
            exit()
        a = aa
        b = bb
        c = cc
