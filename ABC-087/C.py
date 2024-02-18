n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(2)]

dp[0][0] = A[0]
dp[1][0] = B[0] + A[0]

for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + A[i]
    dp[1][i] = max(dp[0][i], dp[1][i - 1]) + B[i]

print(dp[1][n - 1])
