# modified
def f(x):
    if x == 1:
        return 1
    a = f(x // 2)
    return 2*a + 1


h = int(input())


print(f(h))
