n = int(input())
count = 0
for i in range(1, 6):
    # 10,1000,100000
    if i % 2 == 1:
        if n < 10 ** i:
            count += n - 10 ** (i-1) + 1
            print(count)
            exit()
        else:
            count += 10 ** i - (10**(i-1))

    else:
        if n < 10 ** i:
            print(count)
            exit()

print(count)
