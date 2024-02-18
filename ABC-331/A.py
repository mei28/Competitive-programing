M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d + 1 < D:
    print(y, m, d + 1)
elif m + 1 < M:
    print(y, m + 1, 1)
else:
    print(y + 1, 1, 1)
