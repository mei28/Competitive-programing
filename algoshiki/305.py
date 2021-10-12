n = int(input())

dp = [0] * (n + 10)
# dp[i] = iまでのパターン数
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

dp[0] = 1
dp[1] = 1
dp[2] = dp[0] + dp[1]

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]


print(dp[n])
