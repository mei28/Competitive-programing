W, H, N = map(int, input().split())

X, Y = 0, 0

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        X = max(X, x)
    elif a == 2:
        W = min(W, x)
    elif a == 3:
        Y = max(y, Y)
    else:
        H = min(y, H)


print(max(W - X, 0) * max(H - Y, 0))
