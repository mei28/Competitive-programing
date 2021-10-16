n, m = map(int, input().split())
W = list(map(int, input().split()))

# dp[i][j]: i種類目まででMになれるかどうか?

dp = [[False] * (m + 1) for _ in range(n + 1)]

dp[0][0] = True

for i in range(n):
    for j in range(m):
        if not dp[i][j]:
            continue

        # 使わない時
        dp[i + 1][j] = True

        if j + W[i] <= m:
            dp[i + 1][j + W[i]] = True

print("Yes" if dp[n][m] else "No")
