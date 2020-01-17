n, m = map(int, input().split())

ac_check = [0 for _ in range(n)]
wa_check = [0 for _ in range(n)]

for i in range(m):
    i, judge = input().split()
    i = int(i)-1
    if judge == 'AC':
        if ac_check[i] == 0:
            ac_check[i] = 1

    elif judge == 'WA':
        if ac_check[i] == 0:
            wa_check[i] += 1
wa = 0
for i in range(n):
    if ac_check[i] == 1 and wa_check != 0:
        wa += wa_check[i]

print(sum(ac_check), wa)
