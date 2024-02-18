s = input()
MOD = 1000000007
n = len(s)

T = "chokudai"

dp = [[0] * 9 for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1

for i in range(n):
    for j in range(8):
        if s[i] != T[j]:
            dp[i + 1][j + 1] = dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD

print(dp[n][8])
