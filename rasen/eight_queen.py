N = 8
FREE = -1
NOT_FREE = 1

rows = [0] * N
cols = [0] * N
dpos = [0] * (2 * N - 1)
dneg = [0] * (2 * N - 1)
X = [[False] * N for _ in range(N)]


def initialize() -> None:
    for i in range(N):
        rows[i] = FREE
        cols[i] = FREE
    for i in range(2 * N - 1):
        dpos[i] = FREE
        dneg[i] = FREE


def print_board() -> None:
    for i in range(N):
        for j in range(N):
            if X[i][j]:
                if rows[i] != j:
                    return

    for i in range(N):
        for j in range(N):
            print("Q" if rows[i] == j else "-", end="")
        print()
    exit()


def recursive(i: int) -> None:
    if i == N:
        print_board()
        return

    for j in range(N):
        if (
            cols[j] == NOT_FREE
            or dpos[i + j] == NOT_FREE
            or dneg[i + j] == NOT_FREE
        ):
            continue
        rows[i] = j
        cols[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE
        recursive(i + 1)
        rows[i] = cols[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE


def main() -> None:
    initialize()
    for i in range(N):
        for j in range(N):
            X[i][j] = False
    k = int(input())
    for _ in range(k):
        r, c = map(int, input().split())
        X[r][c] = True

    recursive(0)
    return


main()
