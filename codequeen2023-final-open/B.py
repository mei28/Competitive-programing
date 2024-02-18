N = int(input())
queens = [tuple(map(int, input().strip().split())) for _ in range(N - 1)]

rows = [False] * N
cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)

# クイーンの位置を記録
for r, c in queens:
    r -= 1
    c -= 1
    rows[r] = True
    cols[c] = True
    diag1[r + c] = True
    diag2[r - c + N - 1] = True

# クイーンを配置できる場所を探す
for i in range(N):
    for j in range(N):
        if (
            not rows[i]
            and not cols[j]
            and not diag1[i + j]
            and not diag2[i - j + N - 1]
        ):
            print(i + 1, j + 1)
            exit()

print(-1)  # クイーンを配置できる場所がない場合
