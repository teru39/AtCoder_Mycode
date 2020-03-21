# 3:00くらい
N = input()
N = N[::-1]
odd = 0
even = 0
for i in range(len(N)):
    if i % 2 == 0:
        odd += int(N[i])
    else:
        even += int(N[i])

print(even, odd)
