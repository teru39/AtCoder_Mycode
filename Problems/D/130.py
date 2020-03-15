n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = 0
s = 0
t = -1
sum = 0

while (1):
    # k以上になるまで終端を広げる
    while (t < n-1 and sum < k):
        t += 1
        sum += l[t]
    # 回り切ったときにsumがk未満ならその区間は不可
    if sum < k:
        break
    # 一つ見つかったら頭を一つ前にずらす
    ans += n-t
    sum -= l[s]
    s += 1

print(ans)
