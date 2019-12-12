n = int(input())

order = list(map(int, input().split()))
manzoku = list(map(int, input().split()))
add = list(map(int, input().split()))


ans = 0
before = order[0]

for i in range(n):
    if order[i] == before+1:
        ans += manzoku[order[i]-1] + add[before-1]
    else:
        ans += manzoku[order[i]-1]

    before = order[i]

print(ans)
