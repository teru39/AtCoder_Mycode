n = int(input())
l = []
for i in range(n):
    a = int(input())
    for j in range(a):
        a1, a2 = map(int, input().split())
        l.append([i, a1-1, a2])
ans = 0
for i in range(1 << n):
    uso = False
    # print(i)
    for ll in l:
        # ll[0]が正直なのかをチェック]
        # print(ll)
        if i >> ll[0] & 1:  # 正直
            if ((i >> ll[1]) & 1) == ll[2]:
                pass
            else:
                uso = True
                break
        # else:  # 嘘
        #    if ((i >> ll[1]) & 1) == ll[2]:
        #        uso = True
        #        break
    if uso == False:
        # print(bin(i))
        ans = max(ans, len(str(bin(i)).replace('0b', "").replace('0', "")))
print(ans)
