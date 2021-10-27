n, m = map(int, input().split())
W = list(map(int, input().split()))

# dp[i][j]: i種類までを使って重さjのときの最小の個数
INF = 1 << 30
dp = [[INF] * (m + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == INF:
            continue

        # i番目のボールを使わない時
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        # i番目のボールを使う時
        if j + W[i] <= m:
            dp[i + 1][j + W[i]] = min(dp[i + 1][j + W[i]], dp[i][j] + 1)

ans = dp[n][m]
print(-1 if ans == INF else ans)
