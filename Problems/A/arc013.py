from itertools import permutations
n, m, r = map(int, input().split())
pqr = map(int, input().split())
ans = 0
for i, j, k in permutations(pqr):
    ans = max(ans, (n // i) * (m // j) * (r // k))
print(ans)
