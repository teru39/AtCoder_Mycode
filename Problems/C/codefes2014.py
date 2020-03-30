# 17:40 1WA
def n_change(n):
    ret = 0
    s = str(n)
    s = s[::-1]
    for i in range(len(s)):
        ret += int(s[i]) * (n**i)
    return ret


a = int(input())
for i in range(10, 10001):
    #print(n_change(i))
    ans = n_change(i)
    # print(ans)
    if ans == a:
        print(i)
        exit()
print(-1)
