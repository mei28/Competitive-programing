n = int(input())
A = list(map(int, input().split()))

# dp[i]: iまでにかかる最小のコスト
dp = [1 << 60] * (n + 10)
dp[0] = 0
dp[1] = A[1]

for i in range(2, n):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + 2 * A[i])

print(dp[n - 1])
