import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
count = 0
max_count = 0
for i in range(len(l)-1):
    if l[i] - l[i + 1] >= 0:
        count += 1
    else:
        count = 0
    max_count = max(count, max_count)

print(max_count)
