mat = [input() for _ in range(10)]
a = 10**10
b = -(10**10)
c = 10**10
d = -(10**10)

for i in range(10):
    for j in range(10):
        if mat[i][j] == "#":
            a = min(a, i + 1)
            b = max(b, i + 1)
            c = min(c, j + 1)
            d = max(d, j + 1)

print(a, b)
print(c, d)
