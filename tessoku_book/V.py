n = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

# dp[i]

INF = 10**10

dp = [-INF] * (n + 5)
dp[0] = 0

for i in range(n - 1):
    dp[A[i]] = max(dp[A[i]], dp[i] + 100)
    dp[B[i]] = max(dp[B[i]], dp[i] + 150)
print(dp[n - 1])
