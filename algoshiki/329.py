n = int(input())

# dp[i][j] = (i,j)にくるまでの通りの数

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]

print(dp[-1][-1])
