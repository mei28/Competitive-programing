n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = [[False] * (s + 1) for _ in range(n + 1)]

# dp[i][j]: i種類使ってjになるかどうか
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(s + 1):
        # 使わないとき
        dp[i][j] = dp[i - 1][j]
        if j - A[i] >= 0:
            dp[i][j] = dp[i][j] or dp[i - 1][j - A[i]]

print("Yes" if dp[n][s] else "No")
