N, K, D = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j][k] = iこのうち，jこ選んだ時のあまりkの最大値

dp = [[[-1] * D for _ in range(K + 2)] for _ in range(N + 2)]

dp[0][0][0] = 0
for i in range(N):
    for j in range(K + 1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            # 選ばない時
            dp[i + 1][j][k] = max(dp[i][j][k], dp[i + 1][j][k])
            # 選ぶ時
            if j != k:
                dp[i + 1][j + 1][(k + A[i]) % D] = max(
                    dp[i + 1][j + 1][(k + A[i]) % D], dp[i][j][k] + A[i]
                )
print(dp[N][K][0])
