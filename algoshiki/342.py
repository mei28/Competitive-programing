n, m = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

# dp[i][j]: i種類までのものを使って重さjになるまでの最大価値
dp = [[-1] * (m + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    for j in range(m + 1):
        # i番目を使わない
        if dp[i][j] < 0:
            continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        if j + W[i] <= m:
            # i番目を使う時
            dp[i + 1][j + W[i]] = max(dp[i][j] + V[i], dp[i + 1][j + W[i]])

print(max(dp[-1]))
