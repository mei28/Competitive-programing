n, a = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

# dp[i][j] = i日目に店舗jで買った時
INF = 1 << 30
dp = [[INF] * 3 for _ in range(n + 1)]
dp[0][0] = P[0]
dp[0][1] = Q[0]
dp[0][2] = R[0]

for i in range(n - 1):
    dp[i + 1][0] = min(
        dp[i][0] + P[i + 1] - a, dp[i][1] + Q[i + 1], dp[i][2] + R[i + 1]
    )
    dp[i + 1][1] = min(
        dp[i][0] + P[i + 1], dp[i][1] + Q[i + 1] - a, dp[i][2] + R[i + 1]
    )
    dp[i + 1][2] = min(
        dp[i][0] + P[i + 1], dp[i][1] + Q[i + 1], dp[i][2] + R[i + 1] - a
    )

print(min(dp[n - 1]))
