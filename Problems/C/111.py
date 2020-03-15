n = int(input())


v = [int(c) for c in input().split()]
ll = len(v)
v1 = [0 for _ in range(10**6)]
v2 = [0 for _ in range(10**6)]
for i in range(n):
    if i % 2 == 0:
        v1[v[i]] += 1
    else:
        v2[v[i]] += 1

if v1.index(max(v1)) == v2.index(max(v2)):
    m1 = sorted(set(v1))[-2]
    m2 = sorted(set(v2))[-2]
    ans = min(n-m1-max(v2), n-max(v1)-m2)
    print(ans)
else:
    print(n-max(v1)-max(v2))
