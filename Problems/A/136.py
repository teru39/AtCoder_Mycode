a, b, c = map(int, input().split())

hairu = a - b
nokori = c - hairu

if nokori <= 0:
    print(0)
else:
    print(nokori)
