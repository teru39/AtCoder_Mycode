l = list(input().strip())

for i in range(len(l)):
    # odd
    if i % 2 == 0:
        if l[i] not in ['R', 'U', 'D']:
            print('No')
            exit()
    else:
        if l[i] not in ['L', 'U', 'D']:
            print('No')
            exit()

print('Yes')
