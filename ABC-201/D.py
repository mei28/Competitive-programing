if __name__ == "__main__":
    h, w = map(int, input().split())
    field = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]

    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i == h - 1 and j == w - 1:
                continue
            dp[i][j] = -(10**10)
            if i + 1 < h:
                if field[i + 1][j] == "+":
                    diff = 1
                else:
                    diff = -1
                dp[i][j] = max(dp[i][j], -dp[i + 1][j] + diff)
            if j + 1 < w:
                if field[i][j + 1] == "+":
                    diff = 1
                else:
                    diff = -1
                dp[i][j] = max(dp[i][j], -dp[i][j + 1] + diff)

    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] == 0:
        print("Draw")
    else:
        print("Aoki")
