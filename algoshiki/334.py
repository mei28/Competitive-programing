n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: (i,j)にいるときの累計スコア

dp = [[0] * n for _ in range(n)]
dp[0][0] = A[0][0]

for i in range(n):
    for j in range(n):
        dp[i][j] = A[i][j]
        if i - 1 < 0:
            dp[i][j] += dp[i][j - 1]
        elif j - 1 < 0:
            dp[i][j] += dp[i - 1][j]
        else:
            dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
