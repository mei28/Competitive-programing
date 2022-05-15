n = int(input())
A = list(map(int, input().split()))
A = [0] + A

dp = [[0, 0] for _ in range(n + 10)]

ans = 1 << 30
INF = 1 << 30
dp[0][0] = 0
dp[0][1] = INF

for t in [0, 1]:
    dp[1][t] = A[1] * t
    dp[1][1 - t] = INF
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]

    if t == 0:
        ans = min(ans, dp[n][1])
    if t == 1:
        ans = min(ans, dp[n][1], dp[n][0])

print(ans)
