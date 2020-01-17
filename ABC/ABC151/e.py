import itertools
n, k = map(int, input().split())

l = list(map(int, input().split())
         )
mod = 10**9 + 7
ans = 0
for v in itertools.combinations(l, k):
    #print(v)
    ans += max(v) - min(v)
print(ans % mod)
