n = int(input())

gohyaku = n // 500
go = (n-(gohyaku*500))//5

print(gohyaku*1000 + go*5)
