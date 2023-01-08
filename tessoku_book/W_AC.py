N, M = map(int, input().split())

INF = 10**10
dp = [[INF] * (1 << N) for _ in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    A = list(map(int, input().split()))
    bit = 0
    for j in range(N):
        if A[j]:
            bit += 1 << j
    for j in range(1 << N):
        dp[i + 1][j] = dp[i][j]
    for j in range(1 << N):
        dp[i + 1][j | bit] = min(dp[i + 1][j | bit], dp[i][j] + 1)

ans = dp[M][(1 << N) - 1]
if ans >= INF:
    print(-1)
else:
    print(ans)
