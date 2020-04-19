n, k = map(int, input().split())
l = [int(i) for i in range(n + 1)]
lr = l[::-1]

if k == n + 1:
    print(1)
else:
    ans = 1
    mod = 10**9 + 7
    left = sum(l[:k])
    right = sum(lr[:k])
    # print(left)
    # print(right)
    for i in range(n - k + 1):
        ans += right - left + 1
        ans %= mod
        left += l[k + i]
        right += lr[k + i]
    print(ans)
