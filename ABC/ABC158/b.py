n, a, b = map(int, input().split())

shuu = n // (a+b)
amari = n % (a+b)

print(a*shuu + min(amari, a))
