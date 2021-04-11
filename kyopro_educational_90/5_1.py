N, B, K = map(int, input().split())
C = list(map(int, input().split()))

mod = 1000000007

dp = [[0 for _ in range(100000)] for _ in range(35)]

# 桁DPをおこなう
# dp[上から何桁目か][現時点でBで割ったときのあまり] = 何通り
# dp[i][j] -> dp[i+1][10*j+k mod B]

dp[0][0] = 1

for i in range(N):
    for j in range(B):
        for k in range(K):
            new = (10 * j + C[k]) % B
            dp[i + 1][new] += dp[i][j]
            dp[i + 1][new] %= mod


print(dp[N][0])
