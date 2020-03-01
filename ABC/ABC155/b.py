n = int(input())
l = list(map(int, input().split()))

ok = True

for i in l:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            ok = False

if ok:
    print("APPROVED")
else:
    print("DENIED")
