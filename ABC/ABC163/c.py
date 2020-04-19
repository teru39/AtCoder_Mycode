import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
buka = [0 for _ in range(n)]

for i in a:
    buka[i - 1] += 1

for i in buka:
    print(i)
