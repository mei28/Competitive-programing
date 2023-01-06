n, w = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(n)]
WV = [[0, 0]] + WV

dp = [[-1] * (w + 2) for _ in range(n + 2)]
# dp[i][j]: i種類つかって重さがjのときの最大の価値
for i in range(w + 2):
    dp[0][i] = 0

for i in range(1, n + 1):
    for j in range(w + 1):
        # dp[i][j] = max(dp[i][j], dp[i - 1][j])
        dp[i][j] = dp[i - 1][j]
        if j - WV[i][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - WV[i][0]] + WV[i][1])

ans = -1
for a in dp[n]:
    ans = max(ans, a)
print(ans)
