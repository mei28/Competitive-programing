if __name__ == "__main__":
    n = int(input())
    X, Y = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    if n % 2 == 0:
        x_mid = (X[n // 2 - 1] + X[n // 2]) // 2
        y_mid = (Y[n // 2 - 1] + Y[n // 2]) // 2
    else:
        x_mid = X[n // 2]
        y_mid = Y[n // 2]

    ans = 0
    for x, y in zip(X, Y):
        ans += abs(x - x_mid)
        ans += abs(y - y_mid)

    print(ans)
