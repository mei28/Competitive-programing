N, W = map(int, input().split())

WV = []
for _ in range(N):
    w, v = map(int, input().split())
    WV.append([w, v])

# dp[i][j]:iまでの商品を選んだ時の重さjまでの最大価値
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-WV[i])
dp = [[-1] * 1010 for _ in range(110)]
for i in range(1010):
    dp[0][i] = 0

for i in range(N):
    for j in range(W + 1):
        dp[i + 1][j] = dp[i][j]
        if j - WV[i][0] >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - WV[i][0]] + WV[i][1])
print(max(dp[N][: W + 1]))
