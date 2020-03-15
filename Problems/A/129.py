# 01:30
p, q, r = map(int, input().split())

ans = p+q
ans = min(ans, p + r)
ans = min(ans, q + r)

print(ans)
