n = int(input())

dp = [0] * (n + 10)
# dp[i]: i段目にいくまでになん通りあるか
# dp[i] = dp[i-2] + dp[i-1]
dp[0] = 1
dp[1] = 1

for i in range(2, n + 2):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])
