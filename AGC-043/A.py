dx = [1, 0]
dy = [0, 1]
INF = 1 << 30


def solve() -> int:
    # dp[x][y] = (x,y)に辿り着くまでの最小のコスト
    if field[0][0] == "#":
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    for i in range(h):
        for j in range(w):
            for k in range(2):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni >= h or nj >= w:
                    continue
                add = 0
                if field[ni][nj] == "#" and field[i][j] == ".":
                    add = 1

                if dp[ni][nj] > dp[i][j] + add:
                    dp[ni][nj] = dp[i][j] + add

    return dp[h - 1][w - 1]


if __name__ == "__main__":
    h, w = map(int, input().split())
    field = [input() for _ in range(h)]
    dp = [[INF] * w for _ in range(h)]

    print(solve())
