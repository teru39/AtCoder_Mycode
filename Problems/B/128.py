# 16:06
n = int(input())
score = []
for i in range(n):
    a, b = list(input().split())
    tmp = [a, int(b)]
    tmp.append(i)
    score.append(tmp)

score.sort(key=lambda x: (x[0], -x[1]))


for i in range(n):
    print(score[i][2]+1)
