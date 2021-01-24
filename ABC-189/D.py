N = int(input())
dp = [0]*(N+1)
dp[0] = 1
for i in range(N):
    if input() =="AND":
        dp[i+i] = dp[i]
    else:
        dp[i+1] = (1<<(i+1)) + dp[i]

print(dp[N])

