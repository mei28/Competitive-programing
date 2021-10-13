n = int(input())
A = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
MOD = 100

dp[0] = A

for i in range(1, n):
    for j in range(n):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= MOD
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD
        if j + 1 < n:
            dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD

print(dp[-1][-1])
