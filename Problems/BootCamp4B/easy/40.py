# 5:02
a, b = map(int, input().split())
if a * b <= 0:
    print('Zero')
elif a > 0 and b > 0:
    print('Positive')
else:
    if (b - a) % 2 == 0:
        print('Negative')
    else:
        print('Positive')
