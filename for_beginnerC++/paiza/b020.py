n = int(input())
l = []
stack = []
for i in range(n):
    tmp = list(input().split(" ", 2))
    if tmp[0] == 'go':
        l.append(tmp[2:])
        stack.append(tmp[2:])
    else:
        stack.pop()
        l.append(stack[-1])


for i in l:
    print(" ".join(i))
