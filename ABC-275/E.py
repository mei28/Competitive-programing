n, m, k = map(int, input().split())
MOD = 998244353

# dp[j][k] = i番目までつかってj回降った時にkに到達する回数
dp = [[-1] * (k + 2) for _ in range(1010)]

for kk in range(k + 2):
    dp[0][0] = 0

for a in range(1, m + 1):
    dp[1][a] = 1

for a in range(1, m + 1):
    for j in range(1, 1001):
        for kk in range(k + 1):
            if k - a < 0:
                continue
            if dp[j - 1][k - a] > 0:
                dp[j][k] = dp[j - 1][k - a] + 1
print(dp[1000][k])
