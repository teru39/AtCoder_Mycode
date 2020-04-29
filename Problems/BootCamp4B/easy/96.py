# 2:40
n = int(input())
a = list(map(int, input().split()))

minus = 1
for i in a:
    if i % 2 == 0:
        minus *= 2

print(3**len(a) - minus)
