n, m = map(int, input().split())
A = list(map(int, input().split()))

# dp[i]: iまでに最短で行く速さ
# dp[n] = min(dp[n-1]*A[n], dp[n-2]*A[n-2]*2)

dp = [1 << 50] * (n + 10)
dp[0] = 0

for i in range(1, n):
    for j in range(1, m + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + j * A[i])


print(dp[n - 1])
