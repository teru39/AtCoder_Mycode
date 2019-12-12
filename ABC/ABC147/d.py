n = int(input())
mod = 10**9+7
a = [int(i) for i in input().split()]
print(len(a))
ans = 0
for i in range(n-1):
    for k in range(i+1, n):
        ans += (a[i] ^ a[k])
        pass

print(ans % mod)
