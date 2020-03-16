n = int(input())
a = list(map(int, input().split()))

color = [False for _ in range(8)]
wild = 0
for i in a:
    if i < 3200:
        color[i // 400] = True
    else:
        wild += 1

mini = 0
for i in color:
    if i:
        mini += 1
if mini == 0:
    mini = 1
    maxi = wild
else:
    maxi = mini + wild
print(mini, maxi)
