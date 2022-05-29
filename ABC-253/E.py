MOD = 998244353

N, M, K = map(int, input().split())

dp = [[0] * (M + 3) for _ in range(N)]

for j in range(1, M + 1):
    dp[0][j] = 1

for i in range(1, N):
    accum = dp[i - 1]
    for j in range(1, M + 3):
        accum[j] += accum[j - 1]
        accum[j] %= MOD

    for j in range(1, M + 1):
        dp[i][j] = accum[M] - accum[0]
        if K != 0:
            dp[i][j] -= accum[min(M + 2, j + K - 1)] - accum[max(j - K, 0)]
        dp[i][j] %= MOD

print(sum(dp[-1]) % MOD)
