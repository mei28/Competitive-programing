n = int(input())
S = [input() for _ in range(n)]

# dp[i][j]: (i,j)までに何通りあるか
dp = [[0] * (n + 1) for _ in range(n + 1)]

dp[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if S[i - 1][j - 1] == "#":
            continue
        if i - 1 >= 0 and S[i - 2][j - 1] == ".":
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0 and S[i - 1][j - 2] == ".":
            dp[i][j] += dp[i][j - 1]

print(dp[n][n])
