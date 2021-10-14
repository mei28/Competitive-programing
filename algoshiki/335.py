n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

dp = [[1 << 60] * n for _ in range(n)]

dp[0][n - 1] = A[0][n - 1]

for i in range(n):
    for j in range(n - 1, -1, -1):
        if i - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + A[i][j])
        if j + 1 < n:
            dp[i][j] = min(dp[i][j], dp[i][j + 1] + A[i][j])

print(dp[-1][0])
