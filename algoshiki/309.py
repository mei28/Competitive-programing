n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

# dp[i][j] = iアイテム選んで値がjになるかどうか
dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if j - A[i] < 0:
            continue
        if dp[i - 1][j - A[i]]:
            dp[i][j] = True

if dp[n][m]:
    print("Yes")
else:
    print("No")
