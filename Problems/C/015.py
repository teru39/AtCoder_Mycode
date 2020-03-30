# 16:42 1WA
def dfs(now, count):
    if count == question:
        if now == 0:
            return True
        else:
            return False
    else:
        for i in range(choice):
            if dfs(now ^ l[count][i], count + 1):
                return True

        return False


question, choice = map(int, input().split())
l = []
for i in range(question):
    tmp = [int(c) for c in input().split()]
    l.append(tmp)

for i in l[0]:
    if dfs(i, 1):
        print('Found')
        exit()

print('Nothing')
