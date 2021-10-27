n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j] :(i,j)にいる時に獲得する点数

dp = [[-1] * (m) for _ in range(n)]

dp[0][0] = 0

for i in range(n - 1):
    for j in range(m):
        if dp[i][j] < 0:
            continue

        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        if j + A[i] < m:
            dp[i + 1][j + A[i]] = max(dp[i + 1][j + A[i]], dp[i][j] + B[i])

print(dp[-1][-1])
