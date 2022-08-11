n = int(input())
MOD = 998244353

dp = [[0] * (n + 5) for _ in range(11)]

for i in range(1, 11):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, 10):
        dp[j][i] = dp[j][i - 1]
        if 1 <= j - 1 <= 9:
            dp[j][i] += dp[j - 1][i - 1]
        if 1 <= j + 1 <= 9:
            dp[j][i] += dp[j + 1][i - 1]
        dp[j][i] %= MOD


ans = 0
for i in range(1, 11):
    ans += dp[i][n - 1]
    ans %= MOD
print(ans)
