n = int(input())
X, Y = [], []

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def solve() -> int:
    if n == 1:
        return 1

    ret: int = n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            dx: int = X[j] - X[i]
            dy: int = Y[j] - Y[i]

            sub: int = 0

            for i2 in range(n):
                for j2 in range(n):
                    if j2 == i2:
                        continue
                    if dx == X[j2] - X[i2] and dy == Y[j2] - Y[i2]:
                        sub += 1

            ret = min(ret, n - sub)

    return ret


print(solve())
