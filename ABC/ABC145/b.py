n = int(input())
s = input()

if n % 2 == 1:
    print('No')
else:
    tmp = s[:n // 2]
    #print(tmp+tmp)
    if s == (tmp + tmp):
        print('Yes')
    else:
        print('No')
