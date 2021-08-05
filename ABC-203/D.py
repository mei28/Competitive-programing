def ok(m):
    for i in range(n):
        for j in range(n):
            if field[i][j] <= m:
                field2[i + 1][j + 1] = 1
            else:
                field2[i + 1][j + 1] = 0

    for i in range(n):
        for j in range(n):
            if i - 1 > 0:
                field2[i][j] += field2[i - 1][j]
    for i in range(n):
        for j in range(n):
            if j - 1 > 0:
                field2[i][j] += field2[i][j - 1]

    for i in range(n):
        for j in range(n):
            if i + k > n or j + k > n:
                cnt = (
                    field2[i][j]
                    - field2[i][j + k]
                    + field2[i + k][j]
                    + field2[i + k][j + k]
                )
                if cnt >= mid_pos:
                    return True
    return False


if __name__ == "__main__":
    n, k = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    field2 = [[0] * (n + 1) for _ in range(n + 1)]

    mid_pos = k * k + 1 - (k * k // 2 + 1)
    bottom, top = 0, 10 ** 10

    while top - bottom > 1:
        mid = (top + bottom) // 2
        if ok(mid):
            top = mid
        else:
            bottom = mid
    print(top)
