n = int(input())
l = list(map(int, input().split()))

if len(l) != len(set(l)):
    print('NO')
else:
    print("YES")
