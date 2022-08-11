X, Y, Z = map(int, input().split())

if Y * Z // X == Y * Z / X:
    print(Y * Z // X - 1)
else:
    print(Y * Z // X)
