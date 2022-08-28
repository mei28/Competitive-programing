N = int(input())
Tmax = 10**5
X = [0] * (Tmax + 1)
A = [0] * (Tmax + 1)
for _ in range(N):
    t, x, a = map(int, input().split())
    X[t] = x
    A[t] = a

dp = [[-(10**18)] * (Tmax + 1) for _ in range(5)]
dp[0][0] = 0

for t in range(1, Tmax + 1):
    for i in range(5):
        dp[i][t] = dp[i][t - 1]
        if i != 0:
            dp[i][t] = max(dp[i][t], dp[i - 1][t - 1])
        if i != 4:
            dp[i][t] = max(dp[i][t], dp[i + 1][t - 1])
    dp[X[t]][t] += A[t]

print(max(dp[i][Tmax] for i in range(5)))
