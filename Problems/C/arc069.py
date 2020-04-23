# 9:20
# coding: utf-8
n, m = map(int, input().split())

ans = 0
# 最初のs使いきれるか
if 2 * n >= m:
    print(min(n, m // 2))
else:
    ans += n
    m -= 2 * n
    ans += m // 4
    print(ans)
