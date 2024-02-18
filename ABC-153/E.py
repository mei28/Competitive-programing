h, n = map(int, input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
inf = 10**10
dp = [[inf] * (h + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(h + 1):
        dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
        dp[i + 1][min(a[i] + j, h)] = min(
            dp[i + 1][j] + b[i], dp[i + 1][min(a[i] + j, h)]
        )
print(dp[-1][-1])
