#def dfs(v):


n, q = map(int, input().split())

bubunki = [[0] for _ in range(n+1)]
counter = [0 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    bubunki[a].append(b)

for i in range(q):
    p, x = map(int, input().split())
    counter[p] += x

print(bubunki)
print(counter)
