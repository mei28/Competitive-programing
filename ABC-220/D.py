n = int(input())
A = list(map(int, input().split()))
MOD = 998244353

# dp[i][j]: i回目の操作を行った時に，一番左がjであるときのパターン数
# 操作F,GからもらうDPを考える

dp = [[0] * 10 for _ in range(n + 1)]
dp[0][A[0]] = 1

for i in range(1, n):
    for j in range(10):
        if dp[i - 1][j] <= 0:
            continue
        dp[i][(A[i] + j) % 10] += dp[i - 1][j]
        dp[i][(A[i] * j) % 10] += dp[i - 1][j]

        dp[i][(A[i] + j) % 10] %= MOD
        dp[i][(A[i] * j) % 10] %= MOD

print(*dp[n - 1])
