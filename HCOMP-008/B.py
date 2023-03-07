C = [list(map(int, input().split())) for _ in range(3)]

# tate
tate0 = [C[0][0], C[1][0], C[2][0]]
tate1 = [C[0][1], C[1][1], C[2][1]]
tate2 = [C[0][2], C[1][2], C[2][2]]

# yoko
yoko0 = C[0]
yoko1 = C[1]
yoko2 = C[2]


def chmax(a, b):
    if a > b:
        a, b = b, a
    return a, b


# tate
tates = [tate0, tate1, tate2]
for i, j in [[0, 1], [0, 2], [1, 2]]:
    a, b = chmax(tates[i][0], tates[j][0])
    c, d = chmax(tates[i][1], tates[j][1])
    e, f = chmax(tates[i][2], tates[j][2])

    h = abs(a - b)
    i = abs(c - d)
    j = abs(e - f)

    if h == i == j:
        continue
    else:
        print("No")
        exit()
yokos = [tate0, tate1, tate2]
for i, j in [[0, 1], [0, 2], [1, 2]]:
    a, b = chmax(tates[i][0], tates[j][0])
    c, d = chmax(tates[i][1], tates[j][1])
    e, f = chmax(tates[i][2], tates[j][2])

    h = abs(a - b)
    i = abs(c - d)
    j = abs(e - f)

    if h == i == j:
        continue
    else:
        print("No")
        exit()
print("Yes")
