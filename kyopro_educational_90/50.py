N, L = map(int, input().split())
dp = [0] * (100010)
MOD = 1000000007
dp[0] = 1

for i in range(1, N + 1):
    if i - L >= 0:
        dp[i] = dp[i - 1] + dp[i - L]
    else:
        dp[i] = dp[i - 1]
    dp[i] %= MOD
print(dp[N])
