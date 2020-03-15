# 28:59
n = int(input())
h = [list(map(int, input().split()))]
ans = 0


# hがあるうちは回る
while (len(h)):
    now_h = h.pop()
    min_k = min(now_h)
    ans += min_k
    tmp = []
    for i in range(len(now_h)):
        now = now_h[i] - min_k
        if now == 0:
            if len(tmp):
                h.append(tmp)
                tmp = []
        else:
            tmp.append(now)
    if len(tmp):
        h.append(tmp)

print(ans)
