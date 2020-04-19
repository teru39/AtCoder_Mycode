
n, k = map(int, input().split())

if n == 0:
    print(0)
else:
    n = n%k
    print(min(n,k-n))
