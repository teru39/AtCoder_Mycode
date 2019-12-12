import math
a, b, x = map(int, input().split())

v = a * a * b

if x > v / 2:
    rad = math.atan(2*(v-x)/(a*a*a))
    print(math.degrees(rad))

elif x < v / 2:
    rad = math.atan(a * b * b / (2 * x))
    print(math.degrees(rad))


else:
    print(45)
