import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def coupon(i, m, pay):
    if m == 0 or i == n:
        return sum(l[i:])
    for maisuu in range(1, m+1):
        #print("{}に{}まい使う".format(i, maisuu))
        print(maisuu)
        now = l[i] // (2 ** maisuu)
        pay = min(pay, coupon(
            i + 1, m - maisuu, pay) + now)
        if now == 0:
            break

    return pay


n, m = map(int, input().split())

l = [int(c) for c in input().split()]
l.sort()
l.reverse()
max_pay = sum(l)
# print(l)


print(coupon(0, m, max_pay))
