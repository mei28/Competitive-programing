n = int(input())
S = [input() for _ in range(n)]

dp = [[0] * 2 for _ in range(n + 1)]
# dp[i][0]:iまでにfalseのパターン数
# dp[i][1]:iまでにtrueのパターン数
# dp[i+1][0] = dp[i][0]

dp[0][1] = 1
dp[0][0] = 1

for i in range(n):
    if S[i] == "AND":
        dp[i + 1][0] = dp[i][0] * 2 + dp[i][1]
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][0] + dp[i][1] * 2


print(dp[n][1])
