n = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [0] * (n + 5)
# dp[i]: 部屋iに来るまでにかかる時間
# dp[i] = min(dp[i-1]+A_i,dp[i-2]+B_i,dp[i])


for i in range(1, n):
    if i == 1:
        dp[i] = dp[i - 1] + A[i]
    else:
        dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

print(dp[n - 1])
